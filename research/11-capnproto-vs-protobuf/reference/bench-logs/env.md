# 벤치마크 실행 환경

| 항목 | 값 |
|---|---|
| 측정일 | 2026-09-21 10:10 UTC |
| CPU | Intel(R) Xeon(R) Processor @ 2.10GHz |
| 코어 수 | 4 |
| OS | Ubuntu 24.04.4 LTS |
| 커널 | 6.18.44-fc-v37 |
| 컴파일러 | g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 |
| 컴파일 옵션 | `-O2 -std=c++17 -I.build` |
| Cap'n Proto | Cap'n Proto version 1.0.1 |
| Protobuf | libprotoc 3.21.12 |
| zlib | 1.3 |

## 산출물 크기 (생성 코드·바이너리)

| 항목 | 값 |
|---|---|
| vehicle.capnp.h + .c++ | 2153 줄 / 81620 B |
| vehicle.pb.h + .cc | 4525 줄 / 153840 B |
| vehicle.capnp.o | 9976 B |
| vehicle.pb.o | 110328 B |
| libcapnp-1.0.1.so | 571720 B |
| libkj-1.0.1.so | 510400 B |
| libprotobuf.so.32.0.12 | 3056272 B |
| libprotobuf-lite.so.32.0.12 | 850984 B |
