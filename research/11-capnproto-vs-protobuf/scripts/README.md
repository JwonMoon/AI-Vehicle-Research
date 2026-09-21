# 벤치마크 재현 방법

보고서 [§4.2](../capnproto-vs-protobuf.md#42-성능--직접-측정) 의 모든 수치를 만드는 코드다.
손으로 옮겨 적은 숫자는 없다 — 표와 그림 모두 여기 출력에서 나온다.

## 준비

Ubuntu / Debian 계열 기준:

```bash
sudo apt-get install -y capnproto libcapnp-dev protobuf-compiler libprotobuf-dev zlib1g-dev
```

`g++`(C++17), `make` 는 별도로 필요하지 않다 — `run.sh` 가 직접 컴파일한다.

## 실행

```bash
./run.sh                      # 결과가 ../reference/bench-logs/ 에 쌓인다
./run.sh /tmp/my-results      # 출력 위치 지정
python3 make_chart.py         # 결과 CSV 로 ../images/05-bench-results.svg 재생성
```

`run.sh` 가 하는 일:

1. `capnp compile` · `protoc` 로 C++ 코드 생성
2. `-O2 -std=c++17` 로 빌드 (+ LD_PRELOAD 용 할당 카운터 `.so`)
3. 환경·산출물 크기를 `env.md` 로 기록
4. **시간 측정** — 할당 후킹 없이 실행 (`raw-timing.txt`, `results.csv`)
5. **할당 측정** — `LD_PRELOAD` 로 `malloc` 을 가로채 실행 (`raw-alloc.txt`, `results-alloc.csv`)

4와 5를 나눈 이유: 후킹을 얹으면 할당 경로가 느려져 시간 측정이 오염된다.
**`raw-alloc.txt` 의 시간 값은 읽지 말 것.**

## 파일

| 파일 | 역할 |
|---|---|
| `vehicle.proto` / `vehicle.capnp` | 의미가 1:1 대응하는 스키마 쌍. 필드 개수·타입·중첩 깊이를 동일하게 맞췄다 |
| `bench.cpp` | 벤치마크 본체 |
| `alloc_counter.c` | `LD_PRELOAD` 용 힙 할당 카운터 (glibc `__libc_malloc` 직접 호출) |
| `run.sh` | 코드 생성 → 빌드 → 측정 → 기록 |
| `make_chart.py` | `results.csv` → `images/05-bench-results.svg` |

## 측정 설계에서 신경 쓴 것

- **양쪽을 같은 조건에 둔다.** 「앱 데이터 → 전송 가능한 바이트 버퍼」까지를 인코딩,
  「받은 바이트 → 필드를 실제로 읽기」까지를 디코딩으로 정의했다.
- **Protobuf 를 불리하게 두지 않는다.** 기본 사용법 외에 **arena 할당**과
  **객체 재사용 + `Clear()`** 변형을 함께 잰다. 이 둘 없이 재면 기울어진 비교가 된다.
  같은 이유로 Cap'n Proto 쪽에도 스크래치 버퍼 재사용 변형을 넣었다.
- **시계 오버헤드를 분리한다.** 대표값(`mean`)은 **루프 밖에서만** 시계를 읽어 구한다.
  `median`·`p99` 는 per-op 측정이라 clock 호출 비용(이 기계에서 ~26 ns)이 포함된다 —
  절대값이 아니라 흔들림의 크기를 보는 용도다. 실행 첫 줄에 이 값이 출력된다.
- **최적화로 사라지지 않게 한다.** 읽은 값을 `volatile` 변수에 누적한다.
- **페이로드를 0으로 채우지 않는다.** 1 MiB 블롭은 그라데이션 + 노이즈로 만든다.
  전부 0이면 packing·gzip 에 비현실적으로 유리해진다.
- **난수를 고정한다.** 같은 시드에서 시작하므로 두 포맷이 같은 값을 담는다.

## 읽을 때 주의

측정 기계는 **공용 클라우드 vCPU**(Intel Xeon @ 2.10GHz, 4 vCPU)다.
다른 테넌트의 간섭이 있을 수 있으므로 **절대값보다 같은 표 안의 비율**을 봐야 한다.
차량용 ARM SoC 에서 재면 배수가 달라질 수 있다 (보고서 §4.2.7).
