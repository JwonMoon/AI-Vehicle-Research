@0xdb2650c5a8d50d73;
# Cap'n Proto vs Protobuf 벤치마크용 스키마 (Cap'n Proto 판)
#
# vehicle.proto 와 의미가 1:1 대응되도록 작성했다.
# 필드 개수·타입·중첩 깊이를 양쪽이 동일하게 유지하는 것이 비교의 전제다.

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("vbcapnp");

struct Header {
  timestampNs @0 :UInt64;
  seq         @1 :UInt32;
  sourceId    @2 :UInt32;
}

# ---------- A. 고빈도 차량 상태 ----------
struct VehicleState {
  header            @0  :Header;
  speedMps          @1  :Float32;
  steeringAngleRad  @2  :Float32;
  yawRateRps        @3  :Float32;
  accelX            @4  :Float32;
  accelY            @5  :Float32;
  gear              @6  :UInt32;
  brakeActive       @7  :Bool;
  indicatorLeft     @8  :Bool;
  indicatorRight    @9  :Bool;
  wheelSpeed        @10 :List(Float32);  # 4륜
}

# ---------- B. 인지 객체 리스트 ----------
struct Object3d {
  id          @0  :UInt32;
  cls         @1  :UInt32;
  confidence  @2  :Float32;
  x           @3  :Float32;
  y           @4  :Float32;
  z           @5  :Float32;
  length      @6  :Float32;
  width       @7  :Float32;
  height      @8  :Float32;
  heading     @9  :Float32;
  vx          @10 :Float32;
  vy          @11 :Float32;
  covariance  @12 :List(Float32);  # 3x3
  ageFrames   @13 :UInt32;
  isTracked   @14 :Bool;
}

struct ObjectList {
  header  @0 :Header;
  objects @1 :List(Object3d);
}

# ---------- C. 대용량 센서 페이로드 ----------
struct SensorFrame {
  header   @0 :Header;
  width    @1 :UInt32;
  height   @2 :UInt32;
  encoding @3 :UInt32;
  payload  @4 :Data;
}
