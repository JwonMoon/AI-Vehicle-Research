# 출처 수집·검증 기록 — Cap'n Proto vs Protobuf

> **조사일**: 2026-09-21
> **대상 보고서**: [`../capnproto-vs-protobuf.md`](../capnproto-vs-protobuf.md) · [웹 버전](../capnproto-vs-protobuf.html)
> **벤치마크 원시 로그**: [`bench-logs/`](bench-logs/)

## 수집 방법

1. **1차 출처 우선.** 두 프로젝트의 공식 문서를 먼저 읽고, 그 문서가 말하지 않는 것만 서드파티로 보충했다.
2. **직접 실행·측정.** 성능·크기·할당 수치는 전부 이 저장소의 [`../scripts/`](../scripts/) 로 직접 쟀다. 인용한 공개 벤치마크는 교차 검증용이며 본문 수치로 쓰지 않았다.
3. **바이트 예제도 직접 생성.** 보고서 §2.3·§3.3 의 hex 덤프는 `protoc --encode` / `capnp encode` 를 실제로 돌린 출력이다. 손으로 만든 예시가 아니다.
4. **구조체 레이아웃 확인.** `capnp compile -ocapnp vehicle.capnp` 로 필드별 비트 오프셋을 확인해 §3.3 의 서술과 대조했다.

### 접근 제약 — 반드시 알아 둘 것

조사 환경의 egress 정책으로 **`capnproto.org`, `protobuf.dev`, `autosar.org`, `arxiv.org`, `wikipedia.org` 에 직접 HTTP 접근이 차단**되었다(403 connect_rejected). 따라서:

- Cap'n Proto·Protobuf 공식 문서는 **그 사이트의 소스인 업스트림 GitHub 저장소에서 원문 마크다운을 받아 검증**했다. `capnproto.org/encoding.html` 의 본문은 `github.com/capnproto/capnproto/blob/master/doc/encoding.md` 와 동일하다.
- 본문 인용은 **독자가 찾아갈 정본 URL** 과 **실제로 읽은 원문 파일 URL** 을 함께 표기했다.
- AUTOSAR 규격 PDF 와 arXiv 논문은 **직접 열지 못했고**, 검색 결과가 제공한 발췌만 근거로 삼았다. 해당 항목은 아래 표에서 등급을 낮춰 표기한다.

## 등급 정의

| 등급 | 뜻 |
|---|---|
| **자체 측정** | 이 저장소의 코드로 직접 실행·계측한 값. 원시 로그가 `bench-logs/` 에 있다 |
| **공식 원문** | 프로젝트 공식 문서의 원문을 직접 읽음 |
| **공식 발췌** | 공식 문서지만 원문 전체를 열지 못하고 발췌만 확인 |
| **서드파티** | 언론·블로그·논문 |
| **해석** | 본 보고서가 근거로부터 내린 판단 |
| **미확인** | 확인하지 못함 |

---

## 출처 목록

| # | 출처 | 등급 | 확인 내용 |
|---|---|---|---|
| 1 | [`scripts/bench.cpp`](../scripts/bench.cpp) 실행 결과 → [`bench-logs/results.csv`](bench-logs/results.csv), [`raw-timing.txt`](bench-logs/raw-timing.txt) | 자체 측정 | §4.2.2 인코딩·디코딩 속도, §4.2.5 단일 필드 읽기 전체 |
| 2 | 같은 코드 + [`alloc_counter.c`](../scripts/alloc_counter.c) LD_PRELOAD → [`results-alloc.csv`](bench-logs/results-alloc.csv) | 자체 측정 | §4.2.4 할당 횟수·바이트 |
| 3 | [`bench-logs/env.md`](bench-logs/env.md) | 자체 측정 | §4.2.1 측정 환경, §4.6 생성 코드·오브젝트·라이브러리 크기 |
| 4 | `protoc --encode=vbpb.VehicleState vehicle.proto` 출력 | 자체 측정 | §2.3 25바이트 hex 덤프 전체와 필드별 분해 |
| 5 | `capnp encode vehicle.capnp VehicleState` 출력 | 자체 측정 | §3.3 88바이트 hex 덤프, §3.5 packed 29바이트 |
| 6 | `capnp compile -ocapnp vehicle.capnp` 출력 | 자체 측정 | `VehicleState` = 32바이트 데이터 + 2포인터, `gear` 가 `bits[160,192)` 에 고정됨 |
| 7 | [Cap'n Proto Encoding Spec](https://capnproto.org/encoding.html) / [원문 `doc/encoding.md`](https://github.com/capnproto/capnproto/blob/master/doc/encoding.md) | 공식 원문 | 8바이트 워드 정렬, 구조체/리스트/far/케이퍼빌리티 포인터 비트 배치, 기본값 XOR 저장, packed 알고리즘(0x00·0xff 특수 태그, 2 KiB당 2 B 최악 오버헤드), 정규형 규칙, 포인터 경계 검사, 순회 한도 기본 64 MiB, 포인터 깊이 기본 64 |
| 8 | [Cap'n Proto FAQ](https://capnproto.org/faq.html) / [원문 `doc/faq.md`](https://github.com/capnproto/capnproto/blob/master/doc/faq.md) | 공식 원문 | "파싱을 지연시킨 게 아니다", packed 로 Protobuf 유사 크기 달성 주장, `required` 가 실수였다는 구글 내부 사고 서술, 동적 API·텍스트 파서 보안 경고, **공식 보안 검토 미수행 고지** |
| 9 | [Cap'n Proto C++](https://capnproto.org/cxx.html) / [원문 `doc/cxx.md`](https://github.com/capnproto/capnproto/blob/master/doc/cxx.md) | 공식 원문 | `kj` 툴킷 의존, 예외 없는 빌드 시 동적 API 회피 권고, `MallocMessageBuilder` 스크래치 버퍼 사용법(첫 세그먼트 0 초기화 요구) |
| 10 | [Cap'n Proto Other Languages](https://capnproto.org/otherlang.html) / [원문 `doc/otherlang.md`](https://github.com/capnproto/capnproto/blob/master/doc/otherlang.md) | 공식 원문 | 언어별 구현 목록과 유지보수 주체, "C++ 외 구현은 검토하지 않았다"는 고지, 도구 목록에 [Toyota/capnp-trace](https://github.com/Toyota/capnp-trace) 등재 |
| 11 | [Cap'n Proto 1.0 릴리스 노트 (2023-07-28)](https://capnproto.org/news/2023-07-28-capnproto-1.0.html) | 공식 발췌 | 2013-04-01 첫 공개 후 10년 만의 1.0, LTS 지정, Cloudflare Workers 와의 관계 |
| 12 | [Cap'n Proto, FlatBuffers, and SBE (2014-06-17)](https://capnproto.org/news/2014-06-17-capnproto-flatbuffers-sbe.html) | 공식 원문 | FlatBuffers 가 스칼라 타입 단위 정렬로 Cap'n Proto(8바이트 워드)보다 공간 효율이 좋다는 서술 |
| 13 | [Cap'n Proto Security Advisory (2015-03-02)](https://capnproto.org/news/2015-03-02-security-advisory-and-integer-overflow-protection.html) | 공식 원문 | 정수 오버플로 취약점 1건과 템플릿 메타프로그래밍 기반 대응 |
| 14 | [Protobuf Encoding](https://protobuf.dev/programming-guides/encoding/) / [원문 소스](https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/programming-guides/encoding.md) | 공식 원문 | 태그 = (필드번호 << 3) \| 와이어타입, 와이어타입 5종(3·4 폐기), varint 규칙, packed repeated 인코딩 |
| 15 | [Protobuf Arena Allocation](https://protobuf.dev/reference/cpp/arenas/) / [원문 소스](https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/reference/cpp/arenas.md) | 공식 원문 | arena 사용법과 권장 시나리오(메시지 다수 생성 시 이득). §4.2.2 에서 단일 메시지 arena 가 느려진 이유의 근거 |
| 16 | [Protobuf Version Support](https://protobuf.dev/support/version-support/) / [원문 소스](https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/support/version-support.md) | 공식 원문 | 언어별 메이저 버전 분리(릴리스 34.1 ↔ Java 4.34.1, C# 3.34.1), 분기 릴리스 주기, 메이저 교체 후 4분기 지원 |
| 17 | [Protobuf Proto Limits](https://protobuf.dev/programming-guides/proto-limits/) | 공식 원문 | 메시지당 65,535 필드 상한, 직렬화 크기 2 GiB 상한, 언마샬 깊이 제한(Java·C++ 100) |
| 18 | [GHSA-735f-pc8j-v9w8 (CVE-2024-7254)](https://github.com/protocolbuffers/protobuf/security/advisories/GHSA-735f-pc8j-v9w8) 및 검색 결과 | 공식 발췌 | CVE-2022-1941(C++/Python OOM), CVE-2022-3171/3509/3510(Java DoS), CVE-2024-7254(중첩 그룹 무한 재귀, 3.25.5/4.27.5/4.28.2 에서 수정) |
| 19 | [AUTOSAR SOME/IP Protocol Specification R23-11](https://www.autosar.org/fileadmin/standards/R23-11/FO/AUTOSAR_FO_PRS_SOMEIPProtocol.pdf) | 공식 발췌 | **UDP 사용 시 SOME/IP 페이로드 0~1400 B 제한** (IPv6 전환·보안 헤더 여유 확보 목적). PDF 직접 열람 실패, 검색 발췌로 확인 |
| 20 | [AUTOSAR C++14 Guidelines R22-11](https://www.autosar.org/fileadmin/standards/R22-11/AP/AUTOSAR_RS_CPP14Guidelines.pdf) + [MathWorks A18-5-7](https://www.mathworks.com/help/bugfinder/ref/autosarc14rulea1857.html) + [Parasoft 해설](https://www.parasoft.com/blog/breaking-down-the-autosar-c14-coding-guidelines-for-adaptive-autosar/) | 공식 발췌 + 서드파티 | 동적 할당 전면 금지가 아니라 **결정적 WCET·무단편화·고갈 없음 보장 요구**. A18-5-5(커스텀 메모리 관리자), A18-5-7(비실시간 구간에서만 할당) |
| 21 | [Explanation of ara::com API](https://www.autosar.org/fileadmin/standards/R17-10_R1.2.0/AP/AUTOSAR_EXP_ARAComAPI.pdf) + [RTI 블로그](https://www.rti.com/blog/implementing-autosars-dds-network-binding) | 공식 발췌 + 서드파티 | ara::com 이 전송 기술 비의존 API 이며 SOME/IP 를 기본, DDS 를 대안 바인딩으로 둠. DDS 바인딩 제로카피 최적화로 2 MB 통신 12 ms → 3 ms |
| 22 | [A Faster and More Reliable Middleware for Autonomous Driving Systems (arXiv 2510.11448)](https://arxiv.org/pdf/2510.11448) | 서드파티 (발췌) | CyberRT 1.72 µs vs FastDDS 3,807 µs — **공유메모리 vs 네트워크 전송의 차이**이지 직렬화 포맷 차이가 아님. PDF 직접 열람 실패 |
| 23 | [Apollo 소프트웨어 플랫폼 문서](https://github.com/nap-lab/apollo-documentation/blob/master/software-platform.md) + [Autoware·Apollo 비교 (arXiv 2501.18942)](https://arxiv.org/pdf/2501.18942) | 서드파티 | CyberRT 가 Protobuf 를 직렬화로 쓰되 대용량 데이터는 공유메모리로 직접 전달. Autoware 는 ROS 2/DDS 기반 |
| 24 | `dpkg -l` / `pkg-config` / `stat` 출력 → [`bench-logs/env.md`](bench-logs/env.md) | 자체 측정 | libcapnp 571,720 B · libkj 510,400 B · libprotobuf 3,056,272 B · libprotobuf-lite 850,984 B |

---

## 본문에서 인용하지 않기로 한 것

| 내용 | 이유 |
|---|---|
| "Cap'n Proto 전환으로 메모리 사용량 70% 감소" (서드파티 블로그) | 대상 시스템·측정 방법·비교 기준 미공개. 재현 불가 |
| "직렬화가 일어나지 않으므로 무한대로 빠르다" 를 그대로 옮기는 것 | 자체 측정에서 반례(메시지 A 인코딩)가 나옴. §4.2.6 에서 조건부로만 언급 |
| 각종 블로그의 "N배 빠르다" 수치 | 메시지 모양·하드웨어·컴파일 옵션이 제각각. 자체 측정으로 대체 |
| ISO 26262 인증 관련 벤더 마케팅 자료 | 1차 규격 문서를 확인하지 못한 상태에서 인용하면 오도 가능. §7 에 미확인으로 기록 |

## 후속 조사가 필요한 항목

1. **ARM 차량용 SoC(예: Qualcomm 8295P, NVIDIA Thor)에서 재측정** — 비정렬 접근 페널티 차이로 배수가 달라질 수 있다.
2. **FlatBuffers 를 같은 하네스에 추가** — L4 IPC 에서 Cap'n Proto 의 실질적 경쟁자이므로 3자 비교가 필요하다.
3. **iceoryx 공유메모리 전송 위에서의 조합 측정** — "복사 0 전송 + 데이터 배치 규약" 조합의 실제 이득.
4. **Protobuf 최신 릴리스(30번대)로 재측정** — 배포판 3.21.12 와의 성능 차이 확인.
5. **AUTOSAR 규격 PDF 원문 확보** — 현재는 검색 발췌 기반. 사내 네트워크에서 재확인 필요.
