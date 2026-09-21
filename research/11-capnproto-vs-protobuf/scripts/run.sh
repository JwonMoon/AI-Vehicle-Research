#!/usr/bin/env bash
# Cap'n Proto vs Protobuf 벤치마크 실행 스크립트
# 보고서 §4.2 의 수치를 이 스크립트가 만든다.
#
# 사전 준비 (Ubuntu/Debian):
#   sudo apt-get install -y capnproto libcapnp-dev protobuf-compiler libprotobuf-dev zlib1g-dev
#
# 사용:
#   ./run.sh [출력디렉터리]      기본값: ../reference/bench-logs

set -euo pipefail
cd "$(dirname "$0")"

OUT_DIR="${1:-../reference/bench-logs}"
mkdir -p "$OUT_DIR"
OUT_DIR="$(cd "$OUT_DIR" && pwd)"

BUILD=".build"
rm -rf "$BUILD"; mkdir -p "$BUILD"

echo "== 1/4 코드 생성 =="
capnp compile -oc++:"$BUILD" --src-prefix=. vehicle.capnp
protoc --cpp_out="$BUILD" vehicle.proto

echo "== 2/4 빌드 =="
CXXFLAGS="-O2 -std=c++17 -I$BUILD"
g++ $CXXFLAGS -c bench.cpp -o "$BUILD/bench.o"
g++ $CXXFLAGS -c "$BUILD/vehicle.capnp.c++" -o "$BUILD/vehicle.capnp.o"
g++ $CXXFLAGS -c "$BUILD/vehicle.pb.cc" -o "$BUILD/vehicle.pb.o"
g++ "$BUILD"/bench.o "$BUILD"/vehicle.capnp.o "$BUILD"/vehicle.pb.o \
    -o "$BUILD/bench" \
    $(pkg-config --libs capnp) $(pkg-config --libs protobuf) -lz
gcc -O2 -fPIC -shared -o "$BUILD/alloc_counter.so" alloc_counter.c

echo "== 3/4 환경 기록 =="
{
  echo "# 벤치마크 실행 환경"
  echo
  echo "| 항목 | 값 |"
  echo "|---|---|"
  echo "| 측정일 | $(date -u '+%Y-%m-%d %H:%M UTC') |"
  echo "| CPU | $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | xargs) |"
  echo "| 코어 수 | $(nproc) |"
  echo "| OS | $(. /etc/os-release && echo "$PRETTY_NAME") |"
  echo "| 커널 | $(uname -r) |"
  echo "| 컴파일러 | $(g++ --version | head -1) |"
  echo "| 컴파일 옵션 | \`$CXXFLAGS\` |"
  echo "| Cap'n Proto | $(capnp --version) |"
  echo "| Protobuf | $(protoc --version) |"
  echo "| zlib | $(pkg-config --modversion zlib 2>/dev/null || echo 'n/a') |"
  echo
  echo "## 산출물 크기 (생성 코드·바이너리)"
  echo
  echo "| 항목 | 값 |"
  echo "|---|---|"
  echo "| vehicle.capnp.h + .c++ | $(cat "$BUILD"/vehicle.capnp.h "$BUILD"/vehicle.capnp.c++ | wc -l) 줄 / $(cat "$BUILD"/vehicle.capnp.h "$BUILD"/vehicle.capnp.c++ | wc -c) B |"
  echo "| vehicle.pb.h + .cc | $(cat "$BUILD"/vehicle.pb.h "$BUILD"/vehicle.pb.cc | wc -l) 줄 / $(cat "$BUILD"/vehicle.pb.h "$BUILD"/vehicle.pb.cc | wc -c) B |"
  echo "| vehicle.capnp.o | $(stat -c%s "$BUILD"/vehicle.capnp.o) B |"
  echo "| vehicle.pb.o | $(stat -c%s "$BUILD"/vehicle.pb.o) B |"
  for l in libcapnp libkj libprotobuf libprotobuf-lite; do
    # 코어 라이브러리 ELF 본체만. libcapnp-rpc / libkj-http 같은 부가 모듈과
    # 심볼릭 링크·링커 스크립트는 제외한다.
    f=$(find /usr/lib -maxdepth 2 -type f \
          \( -name "$l-[0-9]*.so" -o -name "$l.so.[0-9]*" \) 2>/dev/null | sort | head -1)
    [ -n "$f" ] && echo "| $(basename "$f") | $(stat -c%s "$f") B |"
  done
} > "$OUT_DIR/env.md"
cat "$OUT_DIR/env.md"

echo
echo "== 4/4 측정 =="
echo "-- (a) 시간 측정 (할당 후킹 없음) --"
"$BUILD/bench" "$OUT_DIR/results.csv" | tee "$OUT_DIR/raw-timing.txt"

echo
echo "-- (b) 할당 측정 (LD_PRELOAD 후킹, 시간값은 무시할 것) --"
LD_PRELOAD="$BUILD/alloc_counter.so" "$BUILD/bench" "$OUT_DIR/results-alloc.csv" \
  | tee "$OUT_DIR/raw-alloc.txt"

echo
echo "완료. 결과: $OUT_DIR"
ls -la "$OUT_DIR"
