// bench.cpp — Cap'n Proto vs Protobuf 직렬화 벤치마크
//
// 보고서: ../capnproto-vs-protobuf.md  §4.2
// 빌드·실행: ./run.sh
//
// 측정 원칙
//  - 두 포맷에 의미가 동일한 스키마(vehicle.capnp / vehicle.proto)를 준다.
//  - "애플리케이션 데이터 -> 전송 가능한 바이트 버퍼"까지를 인코딩으로 본다.
//    (Protobuf 의 SerializeToArray, Cap'n Proto 의 messageToFlatArray 구간)
//  - "받은 바이트 -> 필드를 읽을 수 있는 상태 + 실제로 읽기"까지를 디코딩으로 본다.
//  - Protobuf 쪽에 arena / 객체 재사용 변형을 함께 넣는다. 이 둘 없이 재면
//    Protobuf 에 불리하게 기울어진 비교가 된다.
//  - 시간은 배치 총시간/N(throughput 기준)과 per-op 중앙값·p99 를 함께 낸다.
//    per-op 값에는 clock 호출 오버헤드가 포함되므로 그 오버헤드도 같이 출력한다.

#include <capnp/message.h>
#include <capnp/serialize.h>
#include <capnp/serialize-packed.h>
#include <kj/io.h>

#include <google/protobuf/arena.h>

#include "vehicle.capnp.h"
#include "vehicle.pb.h"

#include <zlib.h>
#include <sys/resource.h>

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

// ---------------------------------------------------------------- alloc hook
extern "C" {
__attribute__((weak)) void ac_reset(void);
__attribute__((weak)) void ac_stop(void);
__attribute__((weak)) unsigned long long ac_count(void);
__attribute__((weak)) unsigned long long ac_bytes(void);
__attribute__((weak)) int ac_present(void);
}
static bool allocHookAvailable() { return ac_present != nullptr; }

// ---------------------------------------------------------------- 공통 유틸
using Clock = std::chrono::steady_clock;

static uint64_t g_rng = 0x9E3779B97F4A7C15ull;
static inline uint32_t xrand() {
    g_rng ^= g_rng << 13;
    g_rng ^= g_rng >> 7;
    g_rng ^= g_rng << 17;
    return static_cast<uint32_t>(g_rng >> 32);
}
static inline float frand() { return static_cast<float>(xrand() & 0xFFFF) / 65535.0f; }
static void rngReset() { g_rng = 0x9E3779B97F4A7C15ull; }

struct Timing {
    double totalNsPerOp;  // 루프 밖에서만 시계를 읽은 깨끗한 평균 (대표값)
    double medianNs;      // per-op 중앙값 — clock 호출 오버헤드가 포함된다
    double p99Ns;         // per-op 99 분위 — 위와 동일
};

// f() 를 두 번에 나눠 잰다.
//   pass 1: 루프 안에 시계를 두지 않고 배치 전체 시간만 재서 평균을 구한다.
//           A 메시지처럼 op 자체가 100 ns 대인 경우, 루프 안에서 시계를 읽으면
//           clock 호출 오버헤드(이 기계에서 ~50 ns)가 그대로 결과에 섞인다.
//   pass 2: per-op 로 재서 분포(중앙값·p99)만 얻는다. 이 값들에는 오버헤드가
//           포함되어 있으므로 절대값이 아니라 흔들림의 크기를 보는 용도다.
template <typename F>
static Timing timeOp(int iters, F&& f) {
    for (int i = 0; i < iters / 20 + 1; ++i) f();  // 워밍업

    auto t0 = Clock::now();
    for (int i = 0; i < iters; ++i) f();
    auto t1 = Clock::now();

    std::vector<double> samples;
    samples.reserve(iters);
    for (int i = 0; i < iters; ++i) {
        auto a = Clock::now();
        f();
        auto b = Clock::now();
        samples.push_back(std::chrono::duration<double, std::nano>(b - a).count());
    }

    std::sort(samples.begin(), samples.end());
    Timing t;
    t.totalNsPerOp = std::chrono::duration<double, std::nano>(t1 - t0).count() / iters;
    t.medianNs = samples[samples.size() / 2];
    t.p99Ns = samples[static_cast<size_t>(samples.size() * 0.99)];
    return t;
}

// 할당 후킹이 붙어 있을 때만 유효한 값을 돌려준다.
template <typename F>
static void countAlloc(int iters, F&& f, unsigned long long* nOut, unsigned long long* bOut) {
    if (!allocHookAvailable()) { *nOut = 0; *bOut = 0; return; }
    f();  // 한 번 돌려 내부 lazy init 을 끝내 놓는다
    ac_reset();
    for (int i = 0; i < iters; ++i) f();
    ac_stop();
    *nOut = ac_count() / iters;
    *bOut = ac_bytes() / iters;
}

static size_t gzipSize(const void* p, size_t n) {
    uLongf bound = compressBound(static_cast<uLong>(n));
    std::vector<unsigned char> out(bound);
    if (compress2(out.data(), &bound, static_cast<const Bytef*>(p), static_cast<uLong>(n), 6) != Z_OK)
        return 0;
    return bound;
}

static volatile double g_sink = 0;  // 최적화로 읽기가 통째로 사라지는 것을 막는다

static FILE* g_csv = nullptr;
static void emit(const char* msg, const char* variant, const char* metric, double value, const char* unit) {
    if (g_csv) fprintf(g_csv, "%s,%s,%s,%.4f,%s\n", msg, variant, metric, value, unit);
}
static void emitTiming(const char* msg, const char* variant, const char* metric, const Timing& t) {
    char buf[128];
    snprintf(buf, sizeof buf, "%s_mean", metric); emit(msg, variant, buf, t.totalNsPerOp, "ns");
    snprintf(buf, sizeof buf, "%s_median", metric); emit(msg, variant, buf, t.medianNs, "ns");
    snprintf(buf, sizeof buf, "%s_p99", metric); emit(msg, variant, buf, t.p99Ns, "ns");
}

static void row(const char* label, const Timing& t, double baseline) {
    printf("  %-34s %10.1f %10.1f %10.1f   %6.2fx\n", label, t.totalNsPerOp, t.medianNs, t.p99Ns,
           baseline > 0 ? t.totalNsPerOp / baseline : 1.0);
}
static void header(const char* what) {
    printf("  %-34s %10s %10s %10s   %7s\n", what, "mean", "median", "p99", "vs PB");
    printf("  %s\n", std::string(78, '-').c_str());
}

// ================================================================ A. 차량 상태
static constexpr int kWheels = 4;

static void fillPb(vbpb::VehicleState* m) {
    auto* h = m->mutable_header();
    h->set_timestamp_ns(1726900000000000000ull + xrand());
    h->set_seq(xrand() & 0xFFFF);
    h->set_source_id(7);
    m->set_speed_mps(frand() * 40.0f);
    m->set_steering_angle_rad(frand() * 0.6f - 0.3f);
    m->set_yaw_rate_rps(frand() * 0.4f - 0.2f);
    m->set_accel_x(frand() * 4.0f - 2.0f);
    m->set_accel_y(frand() * 2.0f - 1.0f);
    m->set_gear(4);
    m->set_brake_active(false);
    m->set_indicator_left(false);
    m->set_indicator_right(true);
    m->clear_wheel_speed();
    for (int i = 0; i < kWheels; ++i) m->add_wheel_speed(frand() * 40.0f);
}

static void fillCapnp(vbcapnp::VehicleState::Builder b) {
    auto h = b.initHeader();
    h.setTimestampNs(1726900000000000000ull + xrand());
    h.setSeq(xrand() & 0xFFFF);
    h.setSourceId(7);
    b.setSpeedMps(frand() * 40.0f);
    b.setSteeringAngleRad(frand() * 0.6f - 0.3f);
    b.setYawRateRps(frand() * 0.4f - 0.2f);
    b.setAccelX(frand() * 4.0f - 2.0f);
    b.setAccelY(frand() * 2.0f - 1.0f);
    b.setGear(4);
    b.setBrakeActive(false);
    b.setIndicatorLeft(false);
    b.setIndicatorRight(true);
    auto ws = b.initWheelSpeed(kWheels);
    for (int i = 0; i < kWheels; ++i) ws.set(i, frand() * 40.0f);
}

static double readPb(const vbpb::VehicleState& m) {
    double s = m.header().timestamp_ns() + m.header().seq() + m.header().source_id();
    s += m.speed_mps() + m.steering_angle_rad() + m.yaw_rate_rps() + m.accel_x() + m.accel_y();
    s += m.gear() + m.brake_active() + m.indicator_left() + m.indicator_right();
    for (int i = 0; i < m.wheel_speed_size(); ++i) s += m.wheel_speed(i);
    return s;
}
static double readCapnp(vbcapnp::VehicleState::Reader r) {
    double s = r.getHeader().getTimestampNs() + r.getHeader().getSeq() + r.getHeader().getSourceId();
    s += r.getSpeedMps() + r.getSteeringAngleRad() + r.getYawRateRps() + r.getAccelX() + r.getAccelY();
    s += r.getGear() + r.getBrakeActive() + r.getIndicatorLeft() + r.getIndicatorRight();
    for (auto v : r.getWheelSpeed()) s += v;
    return s;
}

// ================================================================ B. 객체 리스트
static constexpr int kObjects = 64;
static constexpr int kCov = 9;

static void fillObjPb(vbpb::Object3d* o, int i) {
    o->set_id(1000 + i);
    o->set_cls(xrand() % 8);
    o->set_confidence(frand());
    o->set_x(frand() * 120.0f - 60.0f);
    o->set_y(frand() * 40.0f - 20.0f);
    o->set_z(frand() * 3.0f);
    o->set_length(frand() * 5.0f + 1.0f);
    o->set_width(frand() * 2.0f + 0.5f);
    o->set_height(frand() * 2.0f + 0.5f);
    o->set_heading(frand() * 6.28f);
    o->set_vx(frand() * 30.0f - 15.0f);
    o->set_vy(frand() * 6.0f - 3.0f);
    for (int k = 0; k < kCov; ++k) o->add_covariance(frand());
    o->set_age_frames(xrand() % 200);
    o->set_is_tracked(true);
}
static void fillListPb(vbpb::ObjectList* m) {
    auto* h = m->mutable_header();
    h->set_timestamp_ns(1726900000000000000ull + xrand());
    h->set_seq(xrand() & 0xFFFF);
    h->set_source_id(11);
    m->clear_objects();
    for (int i = 0; i < kObjects; ++i) fillObjPb(m->add_objects(), i);
}
static void fillListCapnp(vbcapnp::ObjectList::Builder b) {
    auto h = b.initHeader();
    h.setTimestampNs(1726900000000000000ull + xrand());
    h.setSeq(xrand() & 0xFFFF);
    h.setSourceId(11);
    auto objs = b.initObjects(kObjects);
    for (int i = 0; i < kObjects; ++i) {
        auto o = objs[i];
        o.setId(1000 + i);
        o.setCls(xrand() % 8);
        o.setConfidence(frand());
        o.setX(frand() * 120.0f - 60.0f);
        o.setY(frand() * 40.0f - 20.0f);
        o.setZ(frand() * 3.0f);
        o.setLength(frand() * 5.0f + 1.0f);
        o.setWidth(frand() * 2.0f + 0.5f);
        o.setHeight(frand() * 2.0f + 0.5f);
        o.setHeading(frand() * 6.28f);
        o.setVx(frand() * 30.0f - 15.0f);
        o.setVy(frand() * 6.0f - 3.0f);
        auto cov = o.initCovariance(kCov);
        for (int k = 0; k < kCov; ++k) cov.set(k, frand());
        o.setAgeFrames(xrand() % 200);
        o.setIsTracked(true);
    }
}
static double readListPb(const vbpb::ObjectList& m) {
    double s = m.header().timestamp_ns();
    for (const auto& o : m.objects()) {
        s += o.id() + o.cls() + o.confidence() + o.x() + o.y() + o.z() + o.length() + o.width() +
             o.height() + o.heading() + o.vx() + o.vy() + o.age_frames() + o.is_tracked();
        for (int k = 0; k < o.covariance_size(); ++k) s += o.covariance(k);
    }
    return s;
}
static double readListCapnp(vbcapnp::ObjectList::Reader r) {
    double s = r.getHeader().getTimestampNs();
    for (auto o : r.getObjects()) {
        s += o.getId() + o.getCls() + o.getConfidence() + o.getX() + o.getY() + o.getZ() +
             o.getLength() + o.getWidth() + o.getHeight() + o.getHeading() + o.getVx() + o.getVy() +
             o.getAgeFrames() + o.getIsTracked();
        for (auto v : o.getCovariance()) s += v;
    }
    return s;
}

// ================================================================ C. 센서 프레임
static constexpr size_t kPayload = 1u << 20;  // 1 MiB

// 실제 영상 비슷하게: 그라데이션 + 노이즈. 전부 0 으로 채우면 packing/gzip 에
// 비현실적으로 유리해진다.
static std::vector<uint8_t> makePayload() {
    std::vector<uint8_t> v(kPayload);
    for (size_t i = 0; i < kPayload; ++i)
        v[i] = static_cast<uint8_t>((i / 1280) * 3 + (xrand() & 0x1F));
    return v;
}

// ================================================================ main
int main(int argc, char** argv) {
    GOOGLE_PROTOBUF_VERIFY_VERSION;

    const char* csvPath = (argc > 1) ? argv[1] : nullptr;
    if (csvPath) {
        g_csv = fopen(csvPath, "w");
        fprintf(g_csv, "message,variant,metric,value,unit\n");
    }

    const bool allocMode = allocHookAvailable();
    printf("=========================================================================\n");
    printf(" Cap'n Proto vs Protobuf serialization benchmark\n");
    printf(" capnp %d.%d.%d / protobuf %d.%d.%d / mode=%s\n", CAPNP_VERSION_MAJOR,
           CAPNP_VERSION_MINOR, CAPNP_VERSION_MICRO, GOOGLE_PROTOBUF_VERSION / 1000000,
           (GOOGLE_PROTOBUF_VERSION / 1000) % 1000, GOOGLE_PROTOBUF_VERSION % 1000,
           allocMode ? "ALLOC-COUNT" : "TIMING");
    printf("=========================================================================\n\n");

    // clock 오버헤드 실측 — per-op median/p99 를 읽을 때 이만큼을 감안해야 한다.
    {
        auto noop = timeOp(200000, [] { g_sink += 1.0; });
        printf("[clock overhead] 빈 연산: 깨끗한 평균 %.1f ns / per-op 중앙값 %.1f ns\n",
               noop.totalNsPerOp, noop.medianNs);
        printf("  -> median/p99 열에는 이 중앙값만큼의 계측 오버헤드가 포함되어 있다.\n");
        printf("     mean 열은 루프 밖에서만 시계를 읽었으므로 오버헤드가 없다.\n");
        emit("_meta", "clock", "empty_op_clean_mean", noop.totalNsPerOp, "ns");
        emit("_meta", "clock", "empty_op_perop_median", noop.medianNs, "ns");
        printf("\n");
    }

    // ============================================================ A
    {
        printf("### A. VehicleState (고빈도 차량 상태, 4륜 + 헤더)\n\n");
        const int N = 200000;

        // --- 크기 ---
        rngReset();
        vbpb::VehicleState pbA;
        fillPb(&pbA);
        std::string pbBuf;
        pbA.SerializeToString(&pbBuf);

        rngReset();
        capnp::MallocMessageBuilder mbA;
        fillCapnp(mbA.initRoot<vbcapnp::VehicleState>());
        auto cpWords = capnp::messageToFlatArray(mbA);
        auto cpBytes = cpWords.asBytes();

        kj::VectorOutputStream packedOut;
        capnp::writePackedMessage(packedOut, mbA);
        auto cpPacked = packedOut.getArray();

        printf("  크기: protobuf %zu B | capnp %zu B | capnp-packed %zu B\n", pbBuf.size(),
               cpBytes.size(), cpPacked.size());
        printf("  gzip: protobuf %zu B | capnp %zu B | capnp-packed %zu B\n",
               gzipSize(pbBuf.data(), pbBuf.size()), gzipSize(cpBytes.begin(), cpBytes.size()),
               gzipSize(cpPacked.begin(), cpPacked.size()));
        emit("A", "protobuf", "size", pbBuf.size(), "B");
        emit("A", "capnp", "size", cpBytes.size(), "B");
        emit("A", "capnp-packed", "size", cpPacked.size(), "B");
        emit("A", "protobuf", "gzip", gzipSize(pbBuf.data(), pbBuf.size()), "B");
        emit("A", "capnp", "gzip", gzipSize(cpBytes.begin(), cpBytes.size()), "B");
        emit("A", "capnp-packed", "gzip", gzipSize(cpPacked.begin(), cpPacked.size()), "B");
        printf("\n");

        // --- 인코딩 (애플리케이션 데이터 -> 바이트 버퍼) ---
        std::vector<char> out(4096);
        Timing base{};
        printf("  [인코딩] 단위: ns/op\n");
        header("");

        auto encPbNew = [&] {
            vbpb::VehicleState m;
            fillPb(&m);
            m.SerializeToArray(out.data(), static_cast<int>(out.size()));
        };
        base = timeOp(N, encPbNew);
        row("protobuf (매번 새 객체)", base, base.totalNsPerOp);
        emitTiming("A", "protobuf", "encode", base);

        {
            vbpb::VehicleState reuse;
            auto t = timeOp(N, [&] {
                reuse.Clear();
                fillPb(&reuse);
                reuse.SerializeToArray(out.data(), static_cast<int>(out.size()));
            });
            row("protobuf (객체 재사용 + Clear)", t, base.totalNsPerOp);
            emitTiming("A", "protobuf-reuse", "encode", t);
        }
        {
            auto t = timeOp(N, [&] {
                google::protobuf::Arena arena;
                auto* m = google::protobuf::Arena::CreateMessage<vbpb::VehicleState>(&arena);
                fillPb(m);
                m->SerializeToArray(out.data(), static_cast<int>(out.size()));
            });
            row("protobuf (arena)", t, base.totalNsPerOp);
            emitTiming("A", "protobuf-arena", "encode", t);
        }
        {
            auto t = timeOp(N, [&] {
                capnp::MallocMessageBuilder mb;
                fillCapnp(mb.initRoot<vbcapnp::VehicleState>());
                auto w = capnp::messageToFlatArray(mb);
                memcpy(out.data(), w.asBytes().begin(), w.asBytes().size());
            });
            row("capnp (매번 새 builder)", t, base.totalNsPerOp);
            emitTiming("A", "capnp", "encode", t);
        }
        {
            // capnp 는 스크래치 첫 세그먼트가 0 으로 채워져 있기를 요구한다.
            // (builder 소멸자가 사용분을 다시 0 으로 되돌려 주므로 최초 1회면 된다)
            capnp::word scratch[256];
            memset(scratch, 0, sizeof scratch);
            auto t = timeOp(N, [&] {
                capnp::MallocMessageBuilder mb(kj::ArrayPtr<capnp::word>(scratch, 256));
                fillCapnp(mb.initRoot<vbcapnp::VehicleState>());
                kj::ArrayOutputStream os(kj::ArrayPtr<kj::byte>(
                    reinterpret_cast<kj::byte*>(out.data()), out.size()));
                capnp::writeMessage(os, mb);
            });
            row("capnp (스크래치 버퍼 재사용)", t, base.totalNsPerOp);
            emitTiming("A", "capnp-scratch", "encode", t);
        }
        printf("\n");

        // --- 디코딩 (바이트 -> 모든 필드 읽기) ---
        printf("  [디코딩 + 전체 필드 읽기] 단위: ns/op\n");
        header("");
        auto decPb = [&] {
            vbpb::VehicleState m;
            m.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
            g_sink += readPb(m);
        };
        base = timeOp(N, decPb);
        row("protobuf (매번 새 객체)", base, base.totalNsPerOp);
        emitTiming("A", "protobuf", "decode", base);
        {
            vbpb::VehicleState reuse;
            auto t = timeOp(N, [&] {
                reuse.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
                g_sink += readPb(reuse);
            });
            row("protobuf (객체 재사용)", t, base.totalNsPerOp);
            emitTiming("A", "protobuf-reuse", "decode", t);
        }
        {
            auto words = kj::ArrayPtr<const capnp::word>(
                reinterpret_cast<const capnp::word*>(cpBytes.begin()),
                cpBytes.size() / sizeof(capnp::word));
            auto t = timeOp(N, [&] {
                capnp::FlatArrayMessageReader r(words);
                g_sink += readCapnp(r.getRoot<vbcapnp::VehicleState>());
            });
            row("capnp (FlatArrayMessageReader)", t, base.totalNsPerOp);
            emitTiming("A", "capnp", "decode", t);
        }
        {
            auto t = timeOp(N, [&] {
                kj::ArrayInputStream in(cpPacked);
                capnp::PackedMessageReader r(in);
                g_sink += readCapnp(r.getRoot<vbcapnp::VehicleState>());
            });
            row("capnp-packed (unpack 필요)", t, base.totalNsPerOp);
            emitTiming("A", "capnp-packed", "decode", t);
        }
        printf("\n");

        // --- 할당 ---
        if (allocMode) {
            unsigned long long n, b;
            printf("  [할당] op 당 malloc 호출 수 / 요청 바이트\n");
            countAlloc(2000, encPbNew, &n, &b);
            printf("    protobuf 인코딩 (새 객체)      %4llu calls %7llu B\n", n, b);
            emit("A", "protobuf", "encode_alloc_calls", n, "calls");
            emit("A", "protobuf", "encode_alloc_bytes", b, "B");
            countAlloc(2000,
                       [&] {
                           capnp::MallocMessageBuilder mb;
                           fillCapnp(mb.initRoot<vbcapnp::VehicleState>());
                           auto w = capnp::messageToFlatArray(mb);
                           memcpy(out.data(), w.asBytes().begin(), w.asBytes().size());
                       },
                       &n, &b);
            printf("    capnp 인코딩 (새 builder)      %4llu calls %7llu B\n", n, b);
            emit("A", "capnp", "encode_alloc_calls", n, "calls");
            emit("A", "capnp", "encode_alloc_bytes", b, "B");
            countAlloc(2000, decPb, &n, &b);
            printf("    protobuf 디코딩                %4llu calls %7llu B\n", n, b);
            emit("A", "protobuf", "decode_alloc_calls", n, "calls");
            emit("A", "protobuf", "decode_alloc_bytes", b, "B");
            auto words = kj::ArrayPtr<const capnp::word>(
                reinterpret_cast<const capnp::word*>(cpBytes.begin()),
                cpBytes.size() / sizeof(capnp::word));
            countAlloc(2000,
                       [&] {
                           capnp::FlatArrayMessageReader r(words);
                           g_sink += readCapnp(r.getRoot<vbcapnp::VehicleState>());
                       },
                       &n, &b);
            printf("    capnp 디코딩                   %4llu calls %7llu B\n", n, b);
            emit("A", "capnp", "decode_alloc_calls", n, "calls");
            emit("A", "capnp", "decode_alloc_bytes", b, "B");
            printf("\n");
        }
    }

    // ============================================================ B
    {
        printf("### B. ObjectList (인지 객체 %d개)\n\n", kObjects);
        const int N = 20000;

        rngReset();
        vbpb::ObjectList pbB;
        fillListPb(&pbB);
        std::string pbBuf;
        pbB.SerializeToString(&pbBuf);

        rngReset();
        capnp::MallocMessageBuilder mbB;
        fillListCapnp(mbB.initRoot<vbcapnp::ObjectList>());
        auto cpWords = capnp::messageToFlatArray(mbB);
        auto cpBytes = cpWords.asBytes();
        kj::VectorOutputStream packedOut;
        capnp::writePackedMessage(packedOut, mbB);
        auto cpPacked = packedOut.getArray();

        printf("  크기: protobuf %zu B | capnp %zu B | capnp-packed %zu B\n", pbBuf.size(),
               cpBytes.size(), cpPacked.size());
        printf("  gzip: protobuf %zu B | capnp %zu B | capnp-packed %zu B\n",
               gzipSize(pbBuf.data(), pbBuf.size()), gzipSize(cpBytes.begin(), cpBytes.size()),
               gzipSize(cpPacked.begin(), cpPacked.size()));
        emit("B", "protobuf", "size", pbBuf.size(), "B");
        emit("B", "capnp", "size", cpBytes.size(), "B");
        emit("B", "capnp-packed", "size", cpPacked.size(), "B");
        emit("B", "protobuf", "gzip", gzipSize(pbBuf.data(), pbBuf.size()), "B");
        emit("B", "capnp", "gzip", gzipSize(cpBytes.begin(), cpBytes.size()), "B");
        emit("B", "capnp-packed", "gzip", gzipSize(cpPacked.begin(), cpPacked.size()), "B");
        printf("\n");

        std::vector<char> out(1 << 16);
        Timing base{};
        printf("  [인코딩] 단위: ns/op\n");
        header("");
        auto encPbNew = [&] {
            vbpb::ObjectList m;
            fillListPb(&m);
            m.SerializeToArray(out.data(), static_cast<int>(out.size()));
        };
        base = timeOp(N, encPbNew);
        row("protobuf (매번 새 객체)", base, base.totalNsPerOp);
        emitTiming("B", "protobuf", "encode", base);
        {
            auto t = timeOp(N, [&] {
                google::protobuf::Arena arena;
                auto* m = google::protobuf::Arena::CreateMessage<vbpb::ObjectList>(&arena);
                fillListPb(m);
                m->SerializeToArray(out.data(), static_cast<int>(out.size()));
            });
            row("protobuf (arena)", t, base.totalNsPerOp);
            emitTiming("B", "protobuf-arena", "encode", t);
        }
        {
            vbpb::ObjectList reuse;
            auto t = timeOp(N, [&] {
                reuse.Clear();
                fillListPb(&reuse);
                reuse.SerializeToArray(out.data(), static_cast<int>(out.size()));
            });
            row("protobuf (객체 재사용 + Clear)", t, base.totalNsPerOp);
            emitTiming("B", "protobuf-reuse", "encode", t);
        }
        auto encCapnp = [&] {
            capnp::MallocMessageBuilder mb;
            fillListCapnp(mb.initRoot<vbcapnp::ObjectList>());
            auto w = capnp::messageToFlatArray(mb);
            memcpy(out.data(), w.asBytes().begin(), w.asBytes().size());
        };
        {
            auto t = timeOp(N, encCapnp);
            row("capnp (매번 새 builder)", t, base.totalNsPerOp);
            emitTiming("B", "capnp", "encode", t);
        }
        {
            std::vector<capnp::word> scratch(2048);
            memset(scratch.data(), 0, scratch.size() * sizeof(capnp::word));
            auto t = timeOp(N, [&] {
                capnp::MallocMessageBuilder mb(
                    kj::ArrayPtr<capnp::word>(scratch.data(), scratch.size()));
                fillListCapnp(mb.initRoot<vbcapnp::ObjectList>());
                kj::ArrayOutputStream os(kj::ArrayPtr<kj::byte>(
                    reinterpret_cast<kj::byte*>(out.data()), out.size()));
                capnp::writeMessage(os, mb);
            });
            row("capnp (스크래치 버퍼 재사용)", t, base.totalNsPerOp);
            emitTiming("B", "capnp-scratch", "encode", t);
        }
        printf("\n");

        printf("  [디코딩 + 전체 필드 읽기] 단위: ns/op\n");
        header("");
        auto decPb = [&] {
            vbpb::ObjectList m;
            m.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
            g_sink += readListPb(m);
        };
        base = timeOp(N, decPb);
        row("protobuf (매번 새 객체)", base, base.totalNsPerOp);
        emitTiming("B", "protobuf", "decode", base);
        {
            vbpb::ObjectList reuse;
            auto t = timeOp(N, [&] {
                reuse.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
                g_sink += readListPb(reuse);
            });
            row("protobuf (객체 재사용)", t, base.totalNsPerOp);
            emitTiming("B", "protobuf-reuse", "decode", t);
        }
        auto words = kj::ArrayPtr<const capnp::word>(
            reinterpret_cast<const capnp::word*>(cpBytes.begin()),
            cpBytes.size() / sizeof(capnp::word));
        auto decCapnp = [&] {
            capnp::FlatArrayMessageReader r(words);
            g_sink += readListCapnp(r.getRoot<vbcapnp::ObjectList>());
        };
        {
            auto t = timeOp(N, decCapnp);
            row("capnp (FlatArrayMessageReader)", t, base.totalNsPerOp);
            emitTiming("B", "capnp", "decode", t);
        }
        {
            auto t = timeOp(N, [&] {
                kj::ArrayInputStream in(cpPacked);
                capnp::PackedMessageReader r(in);
                g_sink += readListCapnp(r.getRoot<vbcapnp::ObjectList>());
            });
            row("capnp-packed (unpack 필요)", t, base.totalNsPerOp);
            emitTiming("B", "capnp-packed", "decode", t);
        }
        printf("\n");

        // --- 단일 필드만 읽기: 제로카피가 결정적으로 갈리는 지점 ---
        printf("  [단일 필드만 읽기] 받은 바이트에서 header.timestampNs 하나만. 단위: ns/op\n");
        header("");
        base = timeOp(N, [&] {
            vbpb::ObjectList m;
            m.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
            g_sink += m.header().timestamp_ns();
        });
        row("protobuf (전체 파싱 필요)", base, base.totalNsPerOp);
        emitTiming("B", "protobuf", "peek", base);
        {
            auto t = timeOp(N, [&] {
                capnp::FlatArrayMessageReader r(words);
                g_sink += r.getRoot<vbcapnp::ObjectList>().getHeader().getTimestampNs();
            });
            row("capnp (포인터만 따라감)", t, base.totalNsPerOp);
            emitTiming("B", "capnp", "peek", t);
        }
        printf("\n");

        if (allocMode) {
            unsigned long long n, b;
            printf("  [할당] op 당 malloc 호출 수 / 요청 바이트\n");
            countAlloc(500, encPbNew, &n, &b);
            printf("    protobuf 인코딩 (새 객체)      %4llu calls %7llu B\n", n, b);
            emit("B", "protobuf", "encode_alloc_calls", n, "calls");
            emit("B", "protobuf", "encode_alloc_bytes", b, "B");
            countAlloc(500, encCapnp, &n, &b);
            printf("    capnp 인코딩 (새 builder)      %4llu calls %7llu B\n", n, b);
            emit("B", "capnp", "encode_alloc_calls", n, "calls");
            emit("B", "capnp", "encode_alloc_bytes", b, "B");
            countAlloc(500, decPb, &n, &b);
            printf("    protobuf 디코딩                %4llu calls %7llu B\n", n, b);
            emit("B", "protobuf", "decode_alloc_calls", n, "calls");
            emit("B", "protobuf", "decode_alloc_bytes", b, "B");
            countAlloc(500, decCapnp, &n, &b);
            printf("    capnp 디코딩                   %4llu calls %7llu B\n", n, b);
            emit("B", "capnp", "decode_alloc_calls", n, "calls");
            emit("B", "capnp", "decode_alloc_bytes", b, "B");
            printf("\n");
        }
    }

    // ============================================================ C
    {
        printf("### C. SensorFrame (%zu KiB 페이로드)\n\n", kPayload / 1024);
        const int N = 2000;

        rngReset();
        auto payload = makePayload();

        vbpb::SensorFrame pbC;
        pbC.mutable_header()->set_timestamp_ns(1726900000000000000ull);
        pbC.mutable_header()->set_seq(42);
        pbC.mutable_header()->set_source_id(3);
        pbC.set_width(1280);
        pbC.set_height(819);
        pbC.set_encoding(2);
        pbC.set_payload(payload.data(), payload.size());
        std::string pbBuf;
        pbC.SerializeToString(&pbBuf);

        capnp::MallocMessageBuilder mbC;
        {
            auto b = mbC.initRoot<vbcapnp::SensorFrame>();
            auto h = b.initHeader();
            h.setTimestampNs(1726900000000000000ull);
            h.setSeq(42);
            h.setSourceId(3);
            b.setWidth(1280);
            b.setHeight(819);
            b.setEncoding(2);
            auto p = b.initPayload(payload.size());
            memcpy(p.begin(), payload.data(), payload.size());
        }
        auto cpWords = capnp::messageToFlatArray(mbC);
        auto cpBytes = cpWords.asBytes();
        kj::VectorOutputStream packedOut;
        capnp::writePackedMessage(packedOut, mbC);
        auto cpPacked = packedOut.getArray();

        printf("  크기: protobuf %zu B | capnp %zu B | capnp-packed %zu B\n", pbBuf.size(),
               cpBytes.size(), cpPacked.size());
        printf("  gzip: protobuf %zu B | capnp %zu B\n", gzipSize(pbBuf.data(), pbBuf.size()),
               gzipSize(cpBytes.begin(), cpBytes.size()));
        emit("C", "protobuf", "size", pbBuf.size(), "B");
        emit("C", "capnp", "size", cpBytes.size(), "B");
        emit("C", "capnp-packed", "size", cpPacked.size(), "B");
        emit("C", "protobuf", "gzip", gzipSize(pbBuf.data(), pbBuf.size()), "B");
        emit("C", "capnp", "gzip", gzipSize(cpBytes.begin(), cpBytes.size()), "B");
        printf("\n");

        std::vector<char> out(kPayload + (1 << 16));
        Timing base{};
        printf("  [인코딩] 단위: ns/op\n");
        header("");
        auto encPb = [&] {
            vbpb::SensorFrame m;
            m.mutable_header()->set_timestamp_ns(1726900000000000000ull);
            m.set_width(1280);
            m.set_height(819);
            m.set_encoding(2);
            m.set_payload(payload.data(), payload.size());
            m.SerializeToArray(out.data(), static_cast<int>(out.size()));
        };
        base = timeOp(N, encPb);
        row("protobuf", base, base.totalNsPerOp);
        emitTiming("C", "protobuf", "encode", base);
        auto encCapnp = [&] {
            capnp::MallocMessageBuilder mb;
            auto b = mb.initRoot<vbcapnp::SensorFrame>();
            b.initHeader().setTimestampNs(1726900000000000000ull);
            b.setWidth(1280);
            b.setHeight(819);
            b.setEncoding(2);
            auto p = b.initPayload(payload.size());
            memcpy(p.begin(), payload.data(), payload.size());
            kj::ArrayOutputStream os(
                kj::ArrayPtr<kj::byte>(reinterpret_cast<kj::byte*>(out.data()), out.size()));
            capnp::writeMessage(os, mb);
        };
        {
            auto t = timeOp(N, encCapnp);
            row("capnp", t, base.totalNsPerOp);
            emitTiming("C", "capnp", "encode", t);
        }
        printf("\n");

        printf("  [디코딩 + 페이로드 전체 체크섬] 단위: ns/op\n");
        header("");
        auto decPbFull = [&] {
            vbpb::SensorFrame m;
            m.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
            const auto& p = m.payload();
            uint64_t s = 0;
            for (size_t i = 0; i < p.size(); i += 64) s += static_cast<uint8_t>(p[i]);
            g_sink += s;
        };
        base = timeOp(N, decPbFull);
        row("protobuf", base, base.totalNsPerOp);
        emitTiming("C", "protobuf", "decode", base);
        auto words = kj::ArrayPtr<const capnp::word>(
            reinterpret_cast<const capnp::word*>(cpBytes.begin()),
            cpBytes.size() / sizeof(capnp::word));
        auto decCapnpFull = [&] {
            capnp::FlatArrayMessageReader r(words);
            auto p = r.getRoot<vbcapnp::SensorFrame>().getPayload();
            uint64_t s = 0;
            for (size_t i = 0; i < p.size(); i += 64) s += p[i];
            g_sink += s;
        };
        {
            auto t = timeOp(N, decCapnpFull);
            row("capnp", t, base.totalNsPerOp);
            emitTiming("C", "capnp", "decode", t);
        }
        printf("\n");

        printf("  [단일 필드만 읽기] header.timestampNs 하나만. 단위: ns/op\n");
        header("");
        base = timeOp(N, [&] {
            vbpb::SensorFrame m;
            m.ParseFromArray(pbBuf.data(), static_cast<int>(pbBuf.size()));
            g_sink += m.header().timestamp_ns();
        });
        row("protobuf (1 MiB 전체 파싱)", base, base.totalNsPerOp);
        emitTiming("C", "protobuf", "peek", base);
        {
            auto t = timeOp(N, [&] {
                capnp::FlatArrayMessageReader r(words);
                g_sink += r.getRoot<vbcapnp::SensorFrame>().getHeader().getTimestampNs();
            });
            row("capnp (포인터만 따라감)", t, base.totalNsPerOp);
            emitTiming("C", "capnp", "peek", t);
        }
        printf("\n");

        if (allocMode) {
            unsigned long long n, b;
            printf("  [할당] op 당 malloc 호출 수 / 요청 바이트\n");
            countAlloc(200, encPb, &n, &b);
            printf("    protobuf 인코딩                %4llu calls %9llu B\n", n, b);
            emit("C", "protobuf", "encode_alloc_calls", n, "calls");
            emit("C", "protobuf", "encode_alloc_bytes", b, "B");
            countAlloc(200, encCapnp, &n, &b);
            printf("    capnp 인코딩                   %4llu calls %9llu B\n", n, b);
            emit("C", "capnp", "encode_alloc_calls", n, "calls");
            emit("C", "capnp", "encode_alloc_bytes", b, "B");
            countAlloc(200, decPbFull, &n, &b);
            printf("    protobuf 디코딩                %4llu calls %9llu B\n", n, b);
            emit("C", "protobuf", "decode_alloc_calls", n, "calls");
            emit("C", "protobuf", "decode_alloc_bytes", b, "B");
            countAlloc(200, decCapnpFull, &n, &b);
            printf("    capnp 디코딩                   %4llu calls %9llu B\n", n, b);
            emit("C", "capnp", "decode_alloc_calls", n, "calls");
            emit("C", "capnp", "decode_alloc_bytes", b, "B");
            printf("\n");
        }
    }

    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    printf("peak RSS: %ld KiB\n", ru.ru_maxrss);
    emit("_meta", "process", "peak_rss", ru.ru_maxrss, "KiB");
    printf("sink=%g (최적화 방지용)\n", g_sink);

    if (g_csv) fclose(g_csv);
    google::protobuf::ShutdownProtobufLibrary();
    return 0;
}
