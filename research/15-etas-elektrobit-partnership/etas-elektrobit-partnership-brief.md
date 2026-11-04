# ETAS × Elektrobit 파트너십 — 요약판

- 작성일: 2026-11-04 · 상세판: [etas-elektrobit-partnership.md](etas-elektrobit-partnership.md) · 출처: [reference/references.md](reference/references.md)
- 출처 표기: 🎙️ 패널 토론(2026-10-06 Mobex 웨비나) · `[A1]`~`[E8]` 출처 기록 표 번호 · ⚠️ 미확인/해석
- 조사 제약: 대부분의 원문 사이트 접근 불가, 웹 검색 발췌로 확인

## 요약

- **무엇**: Bosch 자회사 ETAS와 AUMOVIO(옛 Continental) 자회사 Elektrobit이 ADAS용 소프트웨어 기반을 공동 출시. Elektrobit의 안전 인증 리눅스(EB corbos Linux for Safety Applications, ASIL B) 위에 ETAS의 ADAS 결정적 미들웨어(EDMS)를 사전 통합. 통합 안전 수준 ASIL-B [A1][B7][C5]
- **언제**: 2026-05-27 요코하마 JSAE 첫 공개 → 2026-10-06 공동 웨비나 → 2026-10-20 ETAS Connections. 현재 Tier-1·OEM 파일럿 가능 단계, 양산(SOP) 사례 없음 [A1][E1][E2]
- **왜**: 모회사는 ADAS 경쟁사이지만 두 소프트웨어 자회사는 ① 서로에게 없는 층(OS vs 미들웨어)만 결합 ② Eclipse S-CORE에 비차별 기반을 공동 투자하고 차별화는 각자 상용 ③ "리눅스로 개발 → 양산 직전 독점 OS 전환" 고객 리스크 제거 ④ 그룹 외부 시장 공략 자유 ⑤ OEM 예산 압박·협업 문화 — 다섯 가지가 맞물려 성립 🎙️
- **한 달 뒤(2026-11-04)**: 공동 신규 발표 없음. 각사 단독 활동(Elektrobit–Microchip AUTOSAR, ETAS Connections S-CORE 데모)과 S-CORE 0.9 릴리스만 진행. Aumovio SE가 S-CORE 참여사에 직접 등재 [E1]~[E8]

## 시사점

- **ADAS 플랫폼의 OS 선택지가 바뀌고 있음**: 독점 RTOS(QNX 등) 일변도였던 ADAS 기반에 "안전 인증 리눅스 + 결정적 미들웨어"가 공급사 보증을 받은 선택지로 등장. AI·E2E 모델 툴체인이 리눅스 중심이라는 점이 배경 [A7][B7]
- **ASIL-B가 현실적 경계**: 통합 솔루션 상한은 ASIL-B. L2/L2+ 대중화 영역을 노린 제품이며, ASIL-D 기능은 여전히 별도 안전 섬·다른 OS 조합 필요 (⚠️ 해석)
- **오픈 코어가 협력의 공통 언어**: 비차별 레이어(S-CORE)를 함께 만들고 그 위에서 경쟁하는 모델이 자리 잡음. Aumovio·Bosch·BMW·Mercedes·Qualcomm까지 참여사로 들어와, HPC 미들웨어 표준화 압력은 계속 커질 전망 [D1][E6]
- **프레너미 협력의 선례**: 모회사 경쟁과 무관하게 소프트웨어 자회사끼리 층별로 묶는 비독점 협력이 가능함을 보여줌. 같은 리눅스가 Mobileye에도, 같은 ETAS 미들웨어가 ThunderSoft 등에도 공급되는 구조 [B9][C10]
- **검증 포인트는 SOP**: 양측이 다음 목표로 꼽은 첫 양산 사례가 나오기 전까지는 "파일럿 가능한 사전 통합 제품"에 머무름. 후속 모니터링 기준: SOP 공표, 고객명 공개, 통합 솔루션의 ASIL 수준 변화, S-CORE 1.0 [E8] 🎙️

## 1. 결론

- ETAS(Bosch 자회사)와 Elektrobit(AUMOVIO 자회사)이 **안전 인증 리눅스 + ADAS 미들웨어**를 사전 통합한 ADAS 소프트웨어 기반을 공동 출시. 2026-05-27 요코하마 JSAE 첫 공개, ASIL-B [A1][A2]
- 모회사는 ADAS 시장 경쟁사. 일본 언론 표현 "금단의 태그" [A7]
- 협력 성립 근거: ① 비경쟁 층만 결합 ② Eclipse S-CORE 오픈 코어 철학 공유 ③ 고객의 OS 전환 리스크 제거 ④ 자회사의 외부 시장 자유 ⑤ 예산 압박·협업 문화 🎙️
- 현재 파일럿 가능 단계, 양산 사례 없음. 다음 목표 첫 SOP [A1] 🎙️

## 2. 두 회사

| | ETAS | Elektrobit (EB) |
|---|---|---|
| 모회사 | Robert Bosch 100% | AUMOVIO 100% (Continental 자동차 부문, 2025-09 분사 상장) |
| 본사 | 슈투트가르트 | 에를랑겐 |
| 연혁 | 1994 설립. 2022 Bosch 차량 SW 개발·판매 집약(약 2,300명 통합) | 핀란드 Elektrobit Oyj 자동차 사업부. 2015 Continental 인수(6억 유로) |
| 규모 | 약 3,000명, 2024 매출 5.99억 유로(⚠️ 서드파티) | 약 3,000명. "6.3억 대 차량 탑재"(회사 주장) |
| 주력 | 개발 도구 INCA, 기본 SW RTA-CAR, 미들웨어 Vehicle Software Platform Suite, 보안 ESCRYPT | 기본 SW EB tresos, HPC용 EB corbos(AdaptiveCore·Hypervisor·Linux), 네트워크 EB zoneo, 콕핏 EB civion |
| 오픈소스 | Eclipse SDV 창립 멤버, S-CORE 발의 | 2022 Eclipse SDV 가입, Ubuntu 기반 리눅스 |
| 외부 판매 | Bosch 경쟁사에도 공급 | AUMOVIO 경쟁사에도 공급(예: Mobileye Drive) |

출처: [B1][B2][B3][B5][B6][B9][C1][C2][C3][C4][C6][C9] 🎙️

**경쟁·비경쟁 지도**

| 영역 | ETAS | EB | 관계 |
|---|---|---|---|
| Classic AUTOSAR 기본 SW | RTA-CAR | EB tresos | 경쟁 |
| HPC 미들웨어(Adaptive) | VSP Suite | EB corbos AdaptiveCore | 경쟁 |
| 안전 인증 리눅스 | — | **corbos Linux for Safety Applications** | EB만 |
| ADAS 결정적 미들웨어 | **EDMS** | — | ETAS만 |

이번 협력 = 굵은 두 칸의 결합. 경쟁 칸은 제외 (⚠️ 판정은 본 보고서 해석)

## 3. 공동 제품

```
고객 ADAS 애플리케이션
──────────────────────────────────────────
ETAS VSP Suite ADAS 프로파일 (EDMS)   ← 미들웨어
──────────────────────────────────────────
EB corbos Linux for Safety Applications ← OS
──────────────────────────────────────────
SoC (특정 칩 비종속 목표)
```

**EB corbos Linux for Safety Applications** [B6][B7][B8][B9]
- 2024-04 발표. 오픈소스 기반 OS로 첫 기능 안전 평가
- TÜV Nord 긍정 평가: ISO 26262 ASIL B, IEC 61508 SIL 2 (SEooC)
- 방식: 커널 수정 없이 하이퍼바이저 환경의 외부 감시 컴포넌트가 커널 동작 검증 → 리눅스 업데이트 시 재인증 불필요
- Ubuntu 기반, 최대 15년 유지보수. 어떤 리눅스 환경에도 적용 가능한 안전 역량으로 확장(2026-03)
- 적용: Mobileye Drive L4 플랫폼(2026-02), 안전 콕핏 데모(Telechips·Kernkonzept·Qt)

**ETAS VSP Suite ADAS 프로파일 / EDMS** [C5][C6][C7] 🎙️
- 제로카피 공유 메모리 IPC(iceoryx), 10 GB/s 이상 처리 목표
- 결정적 실행: 단일 스레드 runnable, 입력·출력·상태 정의 → 기록·재생(virtual drive) 지원
- POSIX 런타임 SDK, ASPICE·ISO 26262 개발, ASIL-D까지 지원
- Bosch ADAS 프로그램의 도메인 지식 기반
- 범용 부분은 S-CORE 기반 General Purpose 프로파일로 분리

**통합 솔루션** [A1][A4][A6]
- 명칭: integrated ADAS software foundation
- 안전 수준: ASIL-B (⚠️ EDMS는 ASIL-D 가능하나 리눅스 층이 ASIL B → 통합 상한 B)
- 가용성: Tier-1·OEM 초기 양산 평가·파일럿 가능
- 포지셔닝: 독점 OS에 대한 개방형 대안
- ETAS Tobias Kreuzinger: "결정성·대량 데이터 고효율 처리·기능 안전이 양산 ADAS의 필수 요건"

## 4. 협력 근거

| # | 합의점 | 내용 | 근거 |
|---|---|---|---|
| ① | 층 분담 | OS(EB) + 미들웨어(ETAS). 기본 SW·HPC 미들웨어 등 경쟁 제품은 제외 | 🎙️ [A4] |
| ② | 오픈 코어 철학 | S-CORE로 비차별 기반 공동 투자, 차별화는 각자 상용. EB가 S-CORE에 참여해 corbos Linux를 레퍼런스 OS로 추진한 것이 결정적 신호. S-CORE 0.5/0.6 레퍼런스 OS에 실제 포함 | 🎙️ [D2][D3][D4] |
| ③ | 고객 문제 | "리눅스로 개발 → 양산 직전 독점 OS 전환" 패턴의 리스크·지연 제거. 사전 통합으로 호환성은 공급사 책임. AI·E2E 알고리즘 확산으로 ADAS에 리눅스 검토 증가 | 🎙️ [A1][A7] |
| ④ | 지배구조 | 모회사는 경쟁하나 SW 자회사는 외부 시장 공략 자유. 컴퓨트 SW 시장 미통합 → 공동 제안 여지 | 🎙️ [C2][B9] |
| ⑤ | 환경·문화 | OEM 예산 압박, "SOP 이후 존속 파트너" 요구. 개방형 협업 문화 일치. 비독점(EB→Mobileye, ETAS→ThunderSoft 등 병행) | 🎙️ [B9][C10] |

**Eclipse S-CORE** [D1][D2][D3]
- Eclipse 재단 SDV 워킹그룹 오픈소스 프로젝트. OS와 앱 사이의 비차별 기본 서비스(오케스트레이션·IPC·로깅·영속성)
- 2024 시작: Accenture·BMW·ETAS·Mercedes-Benz·Qorix. Bosch·QNX 참여, 2025-11 Qualcomm 합류
- 0.5-alpha 2025-11-17(레퍼런스 OS: QNX·Red Hat AutoSD·EB corbos Linux for Safety Applications), 0.6.0 2026-02(C++·Rust), 0.7 2026-04~05, 0.9 2026-07~09(발표일 출처 간 상이 ⚠️) [E6]
- 참여사 목록에 Accenture·Aumovio SE·BMW·Elektrobit·ETAS 등 등재. Elektrobit 모회사도 직접 참여 [E6]

## 5. 타임라인

| 시점 | 사건 | 출처 |
|---|---|---|
| 2015-05 | Continental, Elektrobit 인수 | [B1] |
| 2022 | Bosch 차량 SW를 ETAS로 집약 · EB, Eclipse SDV 가입 | [C2][B10] |
| 2024 | S-CORE 시작 · EB corbos Linux for Safety Applications 발표(04-23) | [D1][B7] |
| 2025-09-18 | AUMOVIO 상장 | [B2] |
| 2025-11-17 | S-CORE 0.5-alpha, corbos Linux 레퍼런스 포함 | [D2] |
| 2026-02 | S-CORE 0.6.0 · Mobileye Drive 통합 발표(02-24) | [D3][B9] |
| **2026-05-27** | **JSAE 요코하마, 통합 ADAS 기반 첫 공개** | [A1][A6] |
| 2026-06-10~11 | Bosch Connected World, ETAS S-CORE 기반 VSP Suite 시연 | [E5] |
| 2026-07~09 | S-CORE 0.9 마일스톤 | [E6] |
| **2026-10-06** | **공동 웨비나(본 패널 토론)** — Mobex 주최 | [E1] 🎙️ |
| 2026-10-15 | Elektrobit–Microchip 사전 통합 AUTOSAR 협력(단독) | [E3] |
| 2026-10-20 | ETAS Connections 슈투트가르트 — S-CORE 폐막 패널, VSP Suite 데모. Elektrobit 참여는 공개 기록 없음 | [E2] |
| 미정 | 첫 SOP | 🎙️ |

## 6. 후속 동향 (2026-11-04 기준)

패널 토론(10-06) 이후 한 달간 공개 소식. 원문 사이트 직접 열람 불가, 검색 발췌 기준.

**공동**
- 2026-10-06 Mobex 웨비나 "Elektrobit and ETAS: accelerating the future of ADAS through strategic partnership" — 본 패널 토론. 보고서 1판의 "날짜 미기재" 항목 확정. 녹화·자료는 Elektrobit Tech corner 다운로드 센터 게재 추정 [E1]
- 그 외 공동 보도자료·SOP·고객명 발표 없음 [E4]
- Mobex 연사 목록상 Elektrobit PM 이름은 "Isaac Trefz". 전사본의 "Isaac Trebs"는 오기 가능성 (⚠️ 미확정) [E1]

**ETAS Connections 2026 (10-20, 슈투트가르트 Wagenhallen)** [E2]
- Bosch 공동 주최, 약 400명 규모
- 폐막 패널 "The Moment of Delivery: Turning Our Promise into Reality with Eclipse S-CORE" — ETAS·Bosch·Mercedes-Benz·Eclipse 재단 참여
- 데모: Vehicle SW Platform Suite Experience Package 0.6(S-CORE 0.9 기반), 하드웨어 시연
- 패널에서 예고한 Elektrobit 공동 데모는 행사 페이지·회고 글에서 확인되지 않음

**Elektrobit 단독**
- 10-15 Microchip과 사전 통합 AUTOSAR(EB tresos MCAL, SAMA5) 협력. 아시아 시장 우선 [E3]
- 10-29 Integration-as-code, Gasgoo Awards 2026 Best Technical Practice 수상(회사 사이트 기준) [E4]

**Eclipse S-CORE** [E6]
- 0.9 마일스톤 릴리스(발표일 7-28 / 9-09 / 9-24로 출처 간 상이). 통합 전략 일원화, 설정 관리 서비스, 툴체인 갱신
- 참여사 목록에 Aumovio SE 직접 등재 → Elektrobit 모회사도 S-CORE 참여. §4 ②의 논지 보강
- 1판에서 "최신 0.6"으로 기술한 부분은 0.7·0.9 릴리스로 갱신 필요

**ETAS 단독**
- 06-10~11 Bosch Connected World에서 S-CORE 기반 VSP Suite 시연 [E5]
- 10~11월 신규 보도자료는 검색상 없음 [E7]

## 7. 평가

**가치**
- 통합 부담 제거, 개발 연속성(프로토타입→양산 동일 OS·도구), OS·SoC 종속 회피, 안전 실증, 공급사 생존성

**한계 (⚠️ 해석)**
- 통합 안전 수준 ASIL-B 상한. ASIL-D 기능은 별도 구조 필요
- 양산 실적 없음
- S-CORE 0.9 단계(1.0 목표), ETAS General Purpose 프로파일의 S-CORE 전환 진행 중(Experience Package 0.6). EDMS는 S-CORE와 별개 코드베이스
- HPC 미들웨어 경쟁 지속. EB corbos AdaptiveCore와 ETAS 미들웨어 병용 시 통합 책임 불명
- EB 모회사 변경(Continental→AUMOVIO)·2025 감원 → 지속성 변수

## 용어

| 용어 | 뜻 |
|---|---|
| SDV | 소프트웨어 정의 차량 |
| HPC | 차량용 고성능 컴퓨터 |
| ADAS / AD | 첨단 운전자 보조 시스템 / 자율주행 |
| OEM / Tier-1 | 완성차 제조사 / 1차 부품 공급사 |
| SOP | 양산 개시 |
| ISO 26262 / ASIL | 자동차 기능 안전 표준 / 위험 등급(A<B<C<D) |
| IEC 61508 / SIL | 범용 산업 기능 안전 표준 / 등급 |
| SEooC | 특정 차량 맥락 없이 평가받은 안전 요소 |
| POSIX | 유닉스 계열 OS 표준 인터페이스 |
| AUTOSAR Classic / Adaptive | 마이크로컨트롤러용 / 고성능 프로세서용 차량 SW 표준 |
| 미들웨어 | OS와 앱 사이에서 통신·실행 제어·로깅 담당 층 |
| 제로카피 | 복사 없이 공유 메모리로 데이터 전달 |
| 결정적 실행 | 같은 입력 → 같은 결과. 재현·검증에 필수 |
| Eclipse S-CORE | Eclipse 재단 오픈소스 차량 미들웨어 코어 |
| 오픈 코어 | 핵심은 오픈소스, 부가 기능·지원은 상용 |
