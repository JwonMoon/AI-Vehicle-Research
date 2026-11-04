# ETAS × Elektrobit 파트너십 — 두 회사는 누구이고, 무엇을 팔며, 왜 손을 잡았나

> **작성일**: 2026-10-06 · **2판** 2026-11-04 (가독성 개선 — 장별 요점 박스, 글머리 재구성, 출처를 키로 정리)
> **배경**: 두 회사가 공동 진행한 웨비나형 패널 토론(영문 자동 전사본)을 바탕으로, 두 회사를 처음 접하는 독자도 이해할 수 있게 정리한다. ① 각 회사가 무엇을 하고 무엇을 파는지, ② 이번에 합친 제품이 무엇인지, ③ 왜 손을 잡았고 합의점을 어디서 찾았는지. 합의점은 패널 토론 외에 보도자료·언론·오픈소스 프로젝트 공개 자료로 보강했다.
> **출처 표기**: 사실 문장 끝에 출처 키를 단다. 🎙️ = 패널 토론([원문](reference/panel-transcript-raw-en.md) · [글머리 정리](reference/panel-summary-ko.md)) · `[A1]`~`[D6]` = [출처 기록](reference/references.md)의 표 번호(A 발표 · B Elektrobit · C ETAS · D S-CORE) · ⚠️ = 미확인 또는 본 보고서의 해석.
> **조사 제약**: 네트워크 정책으로 etas.com·elektrobit.com·보도자료 전재 사이트·Eclipse 사이트 대부분을 직접 열지 못했다. 외부 출처는 **웹 검색이 돌려준 본문 발췌**로 확인했으며, 직접 열람한 것은 Canonical 블로그 1건이다. 상세는 [출처 기록](reference/references.md).

---

## 0. 한눈에 보기

**세 줄 요약**

1. **ETAS는 Bosch의 100% 자회사, Elektrobit은 Continental에서 분사한 AUMOVIO의 100% 자회사다.** 둘 다 "모회사 밖 시장에도 소프트웨어를 파는" 독일 차량 소프트웨어 회사이고, 모회사끼리는 ADAS 부품 시장에서 정면 경쟁한다. 그래서 일본 언론은 이 협력을 **"금단의 태그(禁断のタッグ)"**라고 불렀다. [C1][B2][A7]
2. **합친 것은 "안전 인증 리눅스(Elektrobit) + ADAS용 결정적 미들웨어(ETAS)"라는 서로 다른 두 층이다.** EB corbos Linux for Safety Applications는 ISO 26262 ASIL B 평가를 받은 세계 첫 오픈소스 기반 OS이고, ETAS Vehicle Software Platform Suite ADAS 프로파일(핵심은 EDMS)은 ADAS 데이터 흐름을 결정적·고속으로 처리하는 미들웨어다. 2026-05-27 요코하마 JSAE 전시회에서 "사전 통합된 ADAS 소프트웨어 기반"으로 처음 공개했고, 통합 솔루션은 ASIL-B를 지원한다. [A1][A2][B7][C7]
3. **합의점은 다섯 가지가 맞물린 결과다.** ① 경쟁 제품은 그대로 두고 겹치지 않는 층만 결합, ② 비차별 기반은 Eclipse S-CORE 오픈소스로 함께 투자하고 차별화는 각자, ③ "리눅스로 개발하다 양산 직전 독점 OS로 갈아타는" 고객 리스크 제거, ④ 각 그룹 안에서 외부 시장을 공략할 자유, ⑤ 예산 압박 속 "SOP 이후에도 살아남을 파트너" 수요와 개방형 협업 문화. 다음 목표는 **첫 양산(SOP) 적용**이다. 🎙️

**핵심 숫자**

| 항목 | 값 | 출처 |
|---|---|---|
| ETAS 규모 | 약 3,000명 · 13개국 · 2024 매출 5.99억 유로 (서드파티 집계, 미교차 ⚠️) | [C3] |
| Elektrobit 규모 | 약 3,000명 · 회사 주장 "6.3억 대 차량·50억 디바이스 탑재" | [B3][B4] |
| EB corbos Linux for Safety Applications | TÜV Nord 긍정 평가 ISO 26262 **ASIL B** / IEC 61508 SIL 2 · 최대 15년 유지보수 | [B7] |
| EDMS | 제로카피 IPC **10 GB/s 이상** · ASIL-D까지 지원 | [C5][C7] |
| 통합 솔루션 | **ASIL-B** · 2026-05-27 첫 공개 · 파일럿 가용, 양산 사례 0 | [A1][A6] |
| S-CORE 레퍼런스 OS | QNX · Red Hat AutoSD · **EB corbos Linux for Safety Applications** (0.5-alpha 2025-11, 0.6.0 2026-02) | [D2][D3] |

---

## 1. 두 회사는 누구인가

> **요점**
> - ETAS = Bosch가 차량 소프트웨어 사업을 모아 둔 회사. 개발 도구(INCA)에서 출발해 기본 SW·미들웨어·사이버보안으로 확장.
> - Elektrobit = Continental(현 AUMOVIO) 계열의 차량 기본 소프트웨어 회사. AUTOSAR 기본 SW(EB tresos)에서 출발해 리눅스·하이퍼바이저·콕핏으로 확장.
> - 둘 다 모회사 경쟁사에도 판다. 기본 SW·HPC 미들웨어에서는 서로 경쟁하고, 안전 리눅스(EB)와 ADAS 결정적 미들웨어(ETAS)는 각자만 가진 자산이다.

### 1.1 한눈에 비교

| 항목 | ETAS | Elektrobit (EB) |
|---|---|---|
| 모회사 | Robert Bosch GmbH 100% [C1] | AUMOVIO SE 100%. AUMOVIO는 Continental 자동차 사업부가 2025-09-18 프랑크푸르트 증시에 분사 상장한 회사 [B2][B3] |
| 본사 | 독일 슈투트가르트 [C3] | 독일 에를랑겐 [B5] |
| 연혁 | 1994 Bosch 자회사로 설립 → 2021-12 Bosch가 "응용 독립적 차량 SW" 개발·판매를 ETAS로 집약 결정, 2022년 중반까지 약 2,300명 통합 [C1][C2] | 핀란드 Elektrobit Oyj 자동차 사업부 → 2015-05 Continental이 6억 유로에 인수(당시 약 1,900명) → 2025 AUMOVIO 분사로 소속 변경 [B1][B2] |
| 규모 | 약 3,000명 · 13개국 · 2024 매출 5.99억 유로 (⚠️ 서드파티 집계) [C3] | 약 3,000명(2025-09 추정) · 2025-02 480명 감원 발표 · "6.3억 대 차량·50억 디바이스"(회사 주장) [B3][B4] |
| 한 줄 정체성 | Bosch 그룹의 차량 소프트웨어 플랫폼·개발 도구·보안 회사 | Continental 계열의 차량 기본 소프트웨어 회사 |
| 오픈소스 | Eclipse SDV 워킹그룹 창립 멤버, Eclipse S-CORE 발의자 [C6] | 2022 Eclipse SDV 워킹그룹 가입, EB corbos Linux는 Ubuntu 기반 [B10][B6] |

### 1.2 ETAS — Bosch의 차량 소프트웨어 회사

**어떤 회사인가**
- 1994년 Bosch가 세운 자회사. 원래는 ECU(전자제어장치)를 개발·측정·보정하는 **개발 도구** 회사였다. [C1]
- 2021년 말 Bosch는 "응용에 독립적인 차량 소프트웨어(기본 SW·미들웨어·클라우드·개발 도구)를 모두 ETAS 한 곳에서 개발·판매한다"고 결정했고, 각 사업부 전문가 약 2,300명을 ETAS로 모았다. Bosch 모빌리티 부문 회장 Stefan Hartung: "응용 독립적 차량 소프트웨어의 선도 공급자가 되겠다." [C2]
- ETAS 자회사지만 **Bosch의 경쟁사에도 판다.** ETAS Subhash Sindhya: "우리는 이 포트폴리오를 Bosch의 경쟁사에도 공급하고, Elektrobit도 마찬가지일 것." 🎙️

**무엇을 파는가** — 공식 소개: "차량 기본 소프트웨어, 미들웨어, 개발 도구, 클라우드 운영 서비스, 사이버보안, 엔드투엔드 엔지니어링·컨설팅" [C1]

| 제품군 | 대표 제품 | 쉬운 설명 | 출처 |
|---|---|---|---|
| 측정·보정·진단 도구 | **INCA**, ETK, RALO | ECU 안의 변수를 실시간으로 보고 파라미터를 조정하는 개발자 도구. ETAS의 전통 주력 | [C4] |
| 기본 소프트웨어 | **RTA-CAR** (AUTOSAR Classic 프로파일) | 마이크로컨트롤러급 ECU에 들어가는 표준 기본 SW | [C4] |
| 미들웨어 **(이번 협력 대상)** | **Vehicle Software Platform Suite** — ADAS/AD 프로파일(핵심: **EDMS**), General Purpose 프로파일(S-CORE 기반) | 고성능 차량 컴퓨터(HPC)에서 애플리케이션과 OS 사이를 잇는 층. §2.2 상세 | [C5][C6] |
| 사이버보안 | **ESCRYPT** 브랜드 | HSM 펌웨어·차량 방화벽·키 관리·취약점 관리. 옛 자회사 ESCRYPT를 흡수 | [C9] |
| 클라우드 | OTA·데이터·코어 서비스 | 차량 소프트웨어 배포·운영 | [C1] |

### 1.3 Elektrobit — Continental 계열의 차량 기본 소프트웨어 회사

**어떤 회사인가**
- 독일 에를랑겐 본사. 핀란드 Elektrobit Oyj의 자동차 사업부였고, 2015년 Continental이 6억 유로에 인수했다(브랜드도 함께 넘어가 핀란드 모회사는 Bittium으로 개명). [B1]
- 2025년 Continental이 자동차 부문을 AUMOVIO로 분사 상장하면서 지금은 **AUMOVIO의 100% 자회사**다. [B2][B3]
- 회사 소개는 "35년 이상 자동차 산업에 복무, 6억 대 이상 차량·50억 개 이상 디바이스에 탑재"라고 주장한다. [B3]
- 역시 **AUMOVIO 경쟁사에도 판다.** 2026-02-24 Mobileye의 L4 자율주행 시스템 Mobileye Drive에 EB corbos Linux for Safety Applications 통합을 발표했다. [B9]

**무엇을 파는가** — 공식 소개: "차량 인프라 소프트웨어, 연결성·보안, 자율주행과 관련 도구, 사용자 경험" [B5]

| 제품군 | 대표 제품 | 쉬운 설명 | 출처 |
|---|---|---|---|
| Classic AUTOSAR 기본 SW | **EB tresos** (BSW + Studio) | 마이크로컨트롤러급 ECU의 표준 기본 SW. 업계 대표 구현 | [B5] |
| HPC용 SW **(이번 협력 대상)** | **EB corbos** — AdaptiveCore(Adaptive AUTOSAR, ASIL-D까지), Hypervisor(ASIL-D까지), **Linux**(Ubuntu 기반), **Linux for Safety Applications** | SoC급 차량 컴퓨터에서 여러 OS·앱을 안전하게 돌리는 바닥 층. §2.1 상세 | [B5][B6][B7] |
| 차량 네트워크 | **EB zoneo** (GatewayCore 등) | 존(zonal) 아키텍처의 게이트웨이·스위치 SW | [B5] |
| 보안 | **EB zentur** | 임베디드 보안 모듈 | [B5] |
| 콕핏·HMI | **EB civion**, EB GUIDE | 디지털 콕핏 플랫폼·HMI 개발 도구. 일부 구제품(EB cadian OTA 등)은 단종 | [A9][B5] |
| 서비스 | 엔지니어링 서비스 | OEM·Tier-1 수탁 개발 | [B5] |

### 1.4 어디서 경쟁하고 어디서 겹치지 않나

패널은 "일부 분야에서는 경쟁하고, 그 분야에서는 당연히 협업하지 않는다"고 명시했다(Elektrobit Moritz Neukirchner). 🎙️ 공개 제품군으로 보면:

| 영역 | ETAS | Elektrobit | 관계 |
|---|---|---|---|
| Classic AUTOSAR 기본 SW | RTA-CAR | EB tresos | **경쟁** |
| Adaptive AUTOSAR / HPC 미들웨어 | Vehicle Software Platform Suite | EB corbos AdaptiveCore | **경쟁** |
| 하이퍼바이저 | — (⚠️ 미확인) | EB corbos Hypervisor | — |
| **안전 인증 리눅스 OS** | 없음 | **EB corbos Linux for Safety Applications** | **EB만** |
| **ADAS 전용 결정적 미들웨어** | **EDMS** (ADAS/AD 프로파일) | 없음 | **ETAS만** |
| 측정·보정 도구 | INCA | 없음 | ETAS만 |
| 사이버보안 | ESCRYPT | EB zentur | 부분 경쟁 |

이번 협력은 굵게 표시한 두 칸, 즉 **서로에게 없는 것**을 합친 것이다. (표의 경쟁/비경쟁 판정은 본 보고서 해석 ⚠️)

---

## 2. 무엇을 합쳤나 — 공동 제품의 구조

> **요점**
> - 바닥 층: Elektrobit의 **EB corbos Linux for Safety Applications** — 리눅스 커널을 고치지 않고 외부 감시 구조로 ASIL B를 받은 OS.
> - 미들웨어 층: ETAS의 **VSP Suite ADAS 프로파일(EDMS)** — 복사 없이 10 GB/s 이상을 흘리고, 같은 입력이면 같은 결과를 내는 ADAS 미들웨어.
> - 둘을 사전 통합한 "ADAS 소프트웨어 기반"은 **ASIL-B**. 2026-05 첫 공개, 파일럿 가능 단계, 양산 사례는 아직 없음.

```
┌─────────────────────────────────────────────────────────┐
│  고객(OEM·Tier-1)의 ADAS 애플리케이션                       │
│  인지·융합·계획 알고리즘, AI 모델 — 고객이 차별화하는 부분     │
├─────────────────────────────────────────────────────────┤
│  ETAS Vehicle Software Platform Suite — ADAS 프로파일      │
│  핵심: EDMS (ETAS Deterministic Middleware Solution)       │
│  · 결정적 실행(같은 입력→같은 출력), 기록·재생                │
│  · 제로카피 공유메모리 IPC, 10 GB/s 이상                     │
│  · ISO 26262 ASIL-D까지 지원하도록 개발                      │
├─────────────────────────────────────────────────────────┤
│  Elektrobit EB corbos Linux for Safety Applications        │
│  · Ubuntu 기반 리눅스 + 외부 안전 감시 구조                   │
│  · TÜV Nord 긍정 평가: ISO 26262 ASIL B / IEC 61508 SIL 2    │
│  · 최대 15년 유지보수                                        │
├─────────────────────────────────────────────────────────┤
│  SoC·하드웨어 — 특정 칩에 종속되지 않는 것이 목표              │
└─────────────────────────────────────────────────────────┘
      ⇧ 통합 솔루션의 안전 수준: ASIL-B (양사 보도자료)
```

### 2.1 Elektrobit의 몫 — EB corbos Linux for Safety Applications (바닥 층)

**무엇인가**
- 자동차 기능 안전 표준(ISO 26262)에 맞게 평가받은 **세계 첫 오픈소스 기반 운영체제 솔루션.** 2024-04-23 발표. [B7]
- 독일 인증기관 TÜV Nord로부터 SEooC(맥락 외 안전 요소) 기준 ISO 26262 **ASIL B**, IEC 61508 **SIL 2** 긍정 기술 평가. [B7]
- Ubuntu 기반(Canonical과 2023-02-21 공동 발표), 최대 15년 유지보수, 회사 주장으로 출시 기간 최대 50% 단축. [B6][B7]

**왜 "성배"인가**
- 리눅스는 개발자가 익숙하고 도구가 풍부하지만, 커널 자체를 ISO 26262로 인증하기는 사실상 불가능했다. 그래서 ADAS 같은 안전 기능은 QNX 등 독점 실시간 OS를 써 왔다. [A7]
- Elektrobit은 커널을 고치는 대신 **하이퍼바이저 환경에 외부 감시 컴포넌트를 두고, Arm 아키텍처 기능으로 커널 동작을 가로채 검증**한다. 리눅스는 빠르게 업데이트하면서도 재인증 없이 쓸 수 있다는 것이 핵심 주장이다. [B7]
- Elektrobit Isaac Trebs: "업계가 수년간 요구해 온 성배(holy grail)." 🎙️

**어디까지 쓰이나**
- 2026-02 Mobileye Drive(L4 로보택시 플랫폼) 통합 발표, 2026-03 embedded world에서 Telechips·Kernkonzept·Qt와 안전 콕핏 데모. [B9][B8]
- embedded world 2026에서 "특정 플랫폼·구성에 묶이지 않는, **어떤 리눅스 환경에도 적용 가능한** 재사용·라이선스 가능한 안전 역량"으로 확장 발표. 패널의 "Elektrobit 안전 솔루션은 어떤 리눅스와도 동작한다"는 발언과 일치한다. [B8] 🎙️

### 2.2 ETAS의 몫 — Vehicle Software Platform Suite ADAS 프로파일과 EDMS (미들웨어 층)

**무엇인가**
- ETAS의 HPC용 미들웨어 제품군 "Vehicle Software Platform Suite"는 용도별 프로파일로 나뉜다. 이번 협력 대상은 **ADAS/AD 프로파일**, 그 핵심이 **EDMS(ETAS Deterministic Middleware Solution)**다. [C5]
- 패널은 줄곧 "EDMS", 보도자료는 "ADAS 프로파일"이라 부른다. 같은 것을 가리킨다. 🎙️ [A1]

**EDMS가 푸는 문제** — ADAS는 카메라·레이더·라이다 데이터를 초당 수 GB씩 받아 여러 단계를 거쳐 제어 명령을 낸다. 여기서 두 가지가 어렵다.
- **데이터 양**: 복사하며 전달하면 CPU와 메모리 대역폭이 바닥난다. → 공유 메모리 기반 **제로카피** 통신(iceoryx 활용)으로 복사 없이 전달, **10 GB/s 이상** 목표. [C7]
- **재현성**: 도로에서 생긴 문제를 사무실에서 똑같이 재현하지 못하면 디버깅도 안전 입증도 어렵다. → 실행 단위(runnable)는 단일 스레드이고 입력·출력·내부 상태가 정의되어, 미들웨어가 **결정적 기록·재생(deterministic recompute, virtual drive)**을 지원한다. [C7]
- µP/POSIX 플랫폼용 런타임과 개발 도구를 SDK로 제공. ASPICE·ISO 26262에 따라 개발, **ASIL-D까지** 지원. [C5][C7]

**어디서 왔나** — ETAS Subhash Sindhya: "ADAS 프로그램에서 Bosch와 함께 개발하며 쌓은 결정성·데이터 처리량 도메인 지식"을 별도 상용 제품으로 내놓은 것. Bosch의 ADAS 양산 경험이 ETAS가 내세우는 차별점이다. 🎙️

**다른 프로파일과의 관계** — 범용 부분(오케스트레이션·IPC·로깅 등)은 **General Purpose 프로파일**로 제공하며 Eclipse S-CORE 기반으로 전환 중이다(S-CORE 0.6 기반 첫 배포판을 Experience Package로 제공). ADAS 프로파일은 그 위에 ADAS 특화 기능을 더한 것이다. [C6] 🎙️

### 2.3 통합 솔루션 — "ADAS 소프트웨어 기반(ADAS software foundation)"

| 항목 | 내용 | 출처 |
|---|---|---|
| 공식 명칭 | 통합 ADAS 소프트웨어 기반 (integrated ADAS software foundation) | [A1][A2] |
| 구성 | EB corbos Linux for Safety Applications + ETAS Vehicle Software Platform Suite ADAS 프로파일 | [A1][A2] |
| 안전 수준 | 통합 솔루션으로 **ASIL-B** 지원. 두 구성 요소 모두 ISO 26262 ASIL-B 요구 충족 | [A1][A6][A7] |
| 첫 공개 | 2026-05-27, 요코하마 "인간과 자동차 테크놀로지전 2026(JSAE)", 5/27~29, ETAS 부스 N77 | [A6] |
| 가용성 | Tier-1·OEM이 현재 스택·차량 프로그램에 통합해 **초기 양산 평가·파일럿** 가능 | [A1][A2] |
| 포지셔닝 | "기존에 ADAS 플랫폼 기반으로 쓰이던 독점 OS에 대한 개방형 대안" | [A1][A4] |
| ETAS 코멘트 | Tobias Kreuzinger(Compute Middleware 제품 분야 책임): "결정성, 대량 데이터의 고효율 처리, 기능 안전은 양산 준비된 ADAS 시스템의 필수 요건" | [A4][A5] |

> **주의 (⚠️ 해석)** EDMS 단독은 ASIL-D까지 지원하지만, 리눅스 층이 ASIL B이므로 **통합 솔루션의 안전 수준은 ASIL-B로 묶인다.** L2/L2+ ADAS의 많은 기능은 ASIL-B 범위에서 설계할 수 있지만, ASIL-D가 필요한 기능은 별도 안전 섬(safety island)이나 다른 OS 조합이 필요하다. 보도자료도 "ASIL-B 지원"으로만 표현한다.

---

## 3. 왜 손잡았나 — 합의점은 어디서 찾았나

> **요점** — 패널 발언과 공개 자료를 대조하면 합의점은 다섯 가지다.
> ① 겹치지 않는 층만 결합 · ② S-CORE 오픈 코어 철학 공유 · ③ 고객의 "리눅스 개발 → 양산 전 OS 교체" 리스크 제거 · ④ 자회사의 외부 시장 자유 · ⑤ 예산 압박·협업 문화·비독점성

### 3.1 합의점 ① "경쟁 제품은 그대로, 겹치지 않는 층만 합친다"

- **패널.** ETAS Subhash Sindhya: "특정 분야에서는 분명히 경쟁하지만, 보완 가능한 분야, 특히 오픈소스와 협업 영역에서는 공동 가치가 있다. Elektrobit의 corbos Linux for Safety Applications와 우리 ADAS 역량은 보완 자산이다." 🎙️
- **패널.** Elektrobit Moritz Neukirchner: "corbos Linux for Safety Applications는 기반을 마련하는 기본 SW일 뿐이고, 그 위에 기능을 개발하려면 도메인 특화 요소가 많이 필요하다. ETAS의 EDMS는 그 보완재로 아주 자연스럽다. 이 두 제품에 관해서는 분명히 경쟁 관계가 아니다." 🎙️
- **공개 자료.** 보도자료도 역할을 나눈다. Elektrobit은 "기능 안전이 필요한 자동차 환경용 리눅스 기반 안전 플랫폼", ETAS는 "ADAS 워크로드용 결정적 미들웨어와 컴퓨트 통합 기능". §1.4 표에서 보듯 두 제품은 서로의 포트폴리오에 없다. [A4]

### 3.2 합의점 ② "비차별 기반은 오픈소스(Eclipse S-CORE)로 함께, 차별화는 각자"

**배경 — Eclipse S-CORE란**
- Eclipse 재단 SDV 워킹그룹 산하 오픈소스 프로젝트(Eclipse Safe Open Vehicle Core). OS와 애플리케이션 사이에서 오케스트레이션·프로세스 간 통신(IPC)·로깅·데이터 영속성 같은, **모든 SDV가 필요로 하지만 차별화 요소는 아닌 기본 서비스**를 제공한다. [D1]
- 2024년 Accenture·BMW·ETAS·Mercedes-Benz·Qorix가 시작. Bosch·QNX가 참여하고 2025-11 Qualcomm 합류. 2025-06 유럽 자동차 업계가 오픈소스 지지 MoU를 체결했고 S-CORE가 대표 사례. [D1][D2]
- 첫 공개 릴리스 0.5-alpha 2025-11-17, 0.6.0 2026-02(C++·Rust 이중 언어). [D2][D3]

**ETAS가 S-CORE를 시작한 이유**
- Subhash Sindhya: "HPC가 도입된 지 7~8년이 지났는데 컴퓨트 소프트웨어 시장은 여전히 파편화되어 있다. 고객과 '어디서 비용을 나누고 공동 투자할 수 있나'를 논의할 때마다 이 레이어가 거론됐고, 그것이 Eclipse에서 S-CORE를 시작한 계기다." 🎙️
- ETAS 공식 페이지도 ETAS를 "S-CORE 프로젝트의 발의자"로 소개한다. [C6]

**Elektrobit의 S-CORE 참여가 결정적 신호였다**
- ETAS Björn Reistel: "이 파트너십이 통할 수 있다는 걸 보여 준 결정적 계기 중 하나는 Elektrobit의 S-CORE 참여였다. 누가 억지로 끌어당긴 게 아니다." 🎙️
- Moritz Neukirchner: "EB는 리눅스를 S-CORE의 레퍼런스 OS 중 하나로 만드는 데 집중하고 있다. 이 미들웨어는 안전 솔루션용 최고 수준의 OS 위에서 돌아야 한다고 보기 때문이다." 🎙️
- **공개 기록과 일치.** S-CORE 0.5-alpha는 QNX·Red Hat AutoSD·**EB corbos Linux for Safety Applications** 세 가지를 레퍼런스 이미지로 제공했고, 0.6.0에서 지원을 강화했다. Elektrobit의 Oliver Pajonk는 Eclipse 행사(OCX 2026)에서 S-CORE × corbos Linux 통합을 시연했다. [D2][D3][D4]

**같은 사업 철학 — "오픈소스 그린워싱이 아니다"**
- Björn Reistel: "오픈소스를 재미로 하는 게 아니다. 의미 있는 사업을 만들기 위해서다. '전부 공개, 전부 무료'가 아니라, 공동 기반 위의 핵심·기본 요소만 오픈소스로 공유하고 그 위에 차별화 요소를 얹는다. Elektrobit은 리눅스 위에, ETAS는 S-CORE 위에." 🎙️
- 두 회사 모두 "오픈 코어 + 상용 차별화" 모델이기에, 상대가 공동 기반을 무임승차하거나 독점하려 한다는 의심 없이 손잡을 수 있었다는 것이 패널의 설명이다. 🎙️

### 3.3 합의점 ③ "고객의 '리눅스 개발 → 양산 직전 독점 OS 전환' 문제를 함께 없앤다"

- **공통 진단.** Elektrobit Isaac Trebs: "개발자는 대학 때부터 리눅스와 Docker·컴파일러·gdb에 익숙하고, SoC 공급사도 리눅스를 기본 제공한다. 그래서 리눅스로 프로토타입을 만들다가 양산 직전에 '기능 안전이 필요하다'며 독점 OS로 갈아탄다. 공통 인터페이스가 있으니 잘 돌아갈 거라고 하지만, '그냥 돌아가야 하는 것'은 절대 그냥 돌아가지 않는다. 엄청난 리스크와 일정 타격이다." 🎙️
- **공동 제품의 답.** 처음부터 끝까지 안전 인증 리눅스를 쓰면 이 단절이 사라지고, 미들웨어까지 사전 통합되어 "함께 동작하는지"는 더 이상 고객의 숙제가 아니다. 보도자료도 핵심 가치를 "OS와 미들웨어 사전 통합, 따로 조달할 때의 검증 공수·호환성 문제·통합 리스크 감소"로 요약한다. 🎙️ [A1]
- **언론의 맥락.** MONOist: "ADAS 개발은 역사적으로 실시간 OS를 써 왔지만, AI 기술 발전과 엔드투엔드 자율주행 알고리즘 개발로 리눅스와의 조합이 점점 검토되고 있다." AI 프레임워크·툴체인이 리눅스 중심이라는 점이 "리눅스로 ADAS"를 밀어 올린다. [A7]
- **벤더 종속 회피도 합의 사항.** EDMS는 POSIX 위에 있어 아래 OS를 바꿀 수 있고, Elektrobit 안전 솔루션은 어떤 리눅스와도 동작한다. 양측 모두 "특정 하드웨어 구매에 묶이지 않는 표준화·반복 가능한 ADAS 플랫폼"을 지향한다. 🎙️

### 3.4 합의점 ④ "모회사는 경쟁해도, 소프트웨어 자회사는 외부 시장을 공략할 자유가 있다"

- Subhash Sindhya: "우리 모회사들은 아주 치열한 경쟁사다. 그런데 각 그룹 안의 소프트웨어 회사로서 두 회사 모두 그룹 밖 시장을 공략할 자유가 있다. ETAS는 Bosch의 경쟁사에도 공급하고, Elektrobit도 마찬가지다. 컴퓨트 시장이 아직 특정 플랫폼으로 통합되지 않았기에, 지금 두 자산을 묶어 내놓을 기회와 빈틈이 있다." 🎙️
- 공개 사실과 부합한다. ETAS는 2022년 Bosch의 "응용 독립적 차량 SW"를 외부에도 파는 회사로 재편됐고(§1.2), Elektrobit은 "완전 자회사이되 독립 운영"을 내세우며 Mobileye 등 외부에 공급한다(§1.3). [C2][B9]
- 그래서 일본 언론은 "Bosch와 AUMOVIO의 소프트웨어 자회사가 금단의 태그를 짰다"고 보도했고, 패널은 그 반응("존재해서는 안 될 파트너십") 자체가 시장 관심을 끌었다고 평가했다. ETAS는 과거 OEM이 "왜 X·Y·Z와 협업하지 않느냐"고 물었던 것을 언급하며, 이번 협력이 그 답이라고도 했다. [A7] 🎙️

### 3.5 합의점 ⑤ "시장 환경과 문화가 맞았다"

- **시장 환경.** Subhash Sindhya: "시장은 예산이 극도로 빠듯하고, OEM은 SOP 시점과 그 이후에도 살아남아 있을 파트너를 찾는다. 보완 자산을 합쳐 '연합 전력'을 보여 주고 고객의 SOP가 위태로워지지 않게 하는 것이 주된 동기다." Moritz Neukirchner: "SDV 프로그램이 과도한 기대에서 벗어나 현실화되면서 협업에 훨씬 큰 비중이 실리고 있다." 🎙️
- **문화.** 양측 모두 "교류를 시작해 보니 문화적으로 잘 맞았다", "둘 다 개방형 협업을 믿는다"를 성공 요소로 꼽았다. 🎙️
- **비독점성.** Björn Reistel: "협력과 비독점성(non-exclusivity)이 새로운 표준이다." 이 파트너십은 서로를 묶는 독점 계약이 아니다. Elektrobit은 같은 리눅스를 Mobileye에도 공급하고, ETAS는 ThunderSoft 등과도 HPC 미들웨어 협력을 한다. 🎙️ [B9][C10]

### 3.6 합의점 요약표

| 합의점 | 한 줄 요약 | 패널 근거 | 외부 근거 |
|---|---|---|---|
| ① 층 분담 | OS(EB) + 미들웨어(ETAS), 경쟁 제품은 제외 | Sindhya·Neukirchner | 보도자료의 역할 분담 [A4] |
| ② 오픈소스 철학 | S-CORE 공동 기반 + 각자 차별화 | Reistel "그린워싱 아님", EB의 S-CORE 참여 | S-CORE 0.5/0.6 레퍼런스 OS에 corbos Linux 포함 [D2][D3] |
| ③ 고객 문제 | "리눅스 개발→양산 전 OS 교체" 단절 제거, 사전 통합 | Trebs | 보도자료 "통합 리스크 감소" [A1], MONOist "RTOS→Linux 흐름" [A7] |
| ④ 지배구조 | 자회사는 외부 시장 공략 자유, 미통합 시장의 빈틈 | Sindhya | ETAS 2022 재편 [C2], EB의 Mobileye 공급 [B9] |
| ⑤ 환경·문화 | 예산 압박·SOP 생존, 개방형 협업, 비독점 | Sindhya·Neukirchner·Reistel | 각자의 다른 파트너십 [B9][C10] |

---

## 4. 타임라인

| 시점 | 사건 | 출처 |
|---|---|---|
| 2015-05 | Continental, Elektrobit 자동차 사업부 6억 유로 인수 | [B1] |
| 2021-12 → 2022-중 | Bosch, 응용 독립적 차량 SW를 ETAS로 집약(약 2,300명) | [C2] |
| 2022 | Elektrobit, Eclipse SDV 워킹그룹 가입 | [B10] |
| 2023-02-21 | Elektrobit·Canonical, Ubuntu 기반 EB corbos Linux 발표 | [B6] |
| 2024 | Accenture·BMW·ETAS·Mercedes-Benz·Qorix, Eclipse S-CORE 시작 | [D1] |
| 2024-04-23 | EB corbos Linux for Safety Applications 발표(TÜV Nord ASIL B/SIL 2) | [B7] |
| 2025-중 | ETAS, 컴퓨트 시장 파편화 진단 → S-CORE 활동 본격화 (패널 발언 "작년 중반" 기준 ⚠️) | 🎙️ |
| 2025-09-18 | AUMOVIO 프랑크푸르트 상장 → Elektrobit의 새 모회사 | [B2] |
| 2025-11-17 | S-CORE 0.5-alpha, EB corbos Linux for Safety Applications 레퍼런스 이미지 포함 | [D2] |
| 2026-02 | S-CORE 0.6.0(C++·Rust 이중 언어, 세 플랫폼 지원 강화) | [D3] |
| 2026-02-24 | EB corbos Linux for Safety Applications, Mobileye Drive 통합 발표 | [B9] |
| **2026-05-27~29** | **요코하마 JSAE에서 통합 ADAS 소프트웨어 기반 첫 공개.** MONOist "금단의 태그" 보도, MarkLines가 ETAS K.K. 사장 미즈모토 분고·Elektrobit Japan 사장 가와이 아키히코 인터뷰 | [A1][A6][A7][A8] |
| 2026-06~10 (추정) | 본 패널 토론 웨비나 (날짜 미기재 ⚠️) | 🎙️ |
| 2026-10-20 | ETAS Connections, 슈투트가르트 — 공동 데모 예고 (행사 페이지 미확인 ⚠️) | 🎙️ |
| 미정 | 첫 양산(SOP) 적용 — 양측이 꼽은 다음 마일스톤 | 🎙️ |

---

## 5. 고객 입장에서 보는 가치와 한계

> **요점** — 내세우는 가치는 통합 부담 제거·개발 연속성·종속 회피·안전 실증·공급사 생존성. 한계는 ASIL-B 상한, 양산 실적 부재, S-CORE 미성숙, 경쟁 영역의 긴장, 모회사 변수.

### 5.1 패널과 보도자료가 내세우는 가치

1. **통합 부담 제거** — OS와 미들웨어가 "함께 동작함"을 두 공급사가 보증. 🎙️ [A1]
2. **개발 연속성** — 프로토타입부터 양산까지 같은 리눅스, 같은 도구. 🎙️
3. **벤더 종속 회피** — POSIX 기반 미들웨어, 어떤 리눅스와도 동작하는 안전 솔루션, 특정 SoC 비종속. 🎙️ [B8]
4. **안전 실증** — 리눅스 층은 TÜV Nord 평가, 미들웨어는 ISO 26262 개발 프로세스. [B7][C5]
5. **공급사 생존성** — 두 대형 그룹 계열사의 "연합 전력". 🎙️

### 5.2 본 보고서가 보는 한계와 열린 질문 (⚠️ 해석)

- **ASIL-B 상한.** 통합 솔루션은 ASIL-B다(§2.3). ASIL-D 기능은 별도 구조가 필요하다.
- **양산 실적 부재.** 2026-11 현재 공개된 것은 "평가·파일럿 가능" 단계이고, SOP 사례는 없다. 양측도 이를 다음 목표로 명시했다.
- **S-CORE 성숙도.** S-CORE는 0.6 단계이고, ETAS General Purpose 프로파일의 S-CORE 전환도 "진행 중"이다. ADAS 프로파일(EDMS)은 S-CORE와 별개 코드베이스이며, "S-CORE 기반 플랫폼과의 추가 통합"은 로드맵 사항이다. 🎙️ [C6]
- **경쟁 영역의 긴장.** Adaptive AUTOSAR/HPC 미들웨어에서 두 회사는 여전히 경쟁한다. 고객이 EB corbos AdaptiveCore와 ETAS 미들웨어를 함께 쓸 때 누가 통합 책임을 지는지는 공개 자료에 없다.
- **모회사 변수.** Elektrobit의 모회사가 Continental에서 AUMOVIO로 바뀌었고 2025년 감원을 겪었다. 파트너십의 지속성은 양 그룹의 전략에 따라 달라질 수 있다. [B2][B4]

---

## 6. 용어

| 용어 | 뜻 |
|---|---|
| SDV | Software-Defined Vehicle. 소프트웨어로 기능을 정의·갱신하는 차량 |
| HPC | 차량용 고성능 컴퓨터(High-Performance Computer). 여러 ECU 기능을 통합하는 SoC급 컴퓨터 |
| ADAS / AD | 첨단 운전자 보조 시스템 / 자율주행 |
| OEM / Tier-1 | 완성차 제조사 / 1차 부품 공급사 |
| SOP | Start of Production, 양산 개시 |
| ISO 26262, ASIL | 자동차 기능 안전 국제 표준과 그 위험 등급(A < B < C < D) |
| IEC 61508, SIL | 범용 산업 기능 안전 표준과 그 등급 |
| SEooC | Safety Element out of Context. 특정 차량 맥락 없이 안전 요소로 평가받은 부품 |
| TÜV Nord | 독일의 제3자 시험·인증 기관 |
| POSIX | 유닉스 계열 OS의 표준 인터페이스. 이를 지키면 OS를 바꿔도 앱 이식이 쉽다 |
| AUTOSAR Classic / Adaptive | 마이크로컨트롤러용 / 고성능 프로세서용 차량 SW 표준 아키텍처 |
| 미들웨어 | OS와 애플리케이션 사이에서 통신·실행 제어·로깅 등을 담당하는 층 |
| 제로카피 | 데이터를 복사하지 않고 공유 메모리로 전달하는 기법 |
| 결정적(deterministic) 실행 | 같은 입력·타이밍이면 항상 같은 결과가 나오도록 보장하는 실행 방식. 재현·검증에 필수 |
| Eclipse S-CORE | Eclipse Safe Open Vehicle Core. Eclipse 재단의 오픈소스 차량 미들웨어 코어 프로젝트 |
| 하이퍼바이저 | 한 하드웨어에서 여러 OS를 격리해 돌리는 소프트웨어 |
| 존(zonal) 아키텍처 | 차량을 구역별로 나눠 제어기를 통합하는 전기·전자 구조 |
| 프레너미 | Friend + Enemy. 경쟁하면서 협력하는 관계 |
| 오픈 코어 | 핵심은 오픈소스로 공개하고 부가 기능·지원은 상용으로 파는 사업 모델 |

---

## 7. 출처 키

본문의 `[A1]`~`[D6]`은 [출처 기록](reference/references.md)의 표 번호다. 자주 인용한 것만 적는다.

| 키 | 출처 |
|---|---|
| A1 · A2 | ETAS·Elektrobit 보도자료 "integrated ADAS software foundation" (2026-05-27) |
| A4 · A5 | Automotive World · Autocar Pro 등 보도자료 전재 (Tobias Kreuzinger 인용) |
| A6 | ETAS 일본어 보도자료 전재(財経新聞) — 부스 N77, ASIL-B |
| A7 | MONOist 2026-05-28 "ボッシュとオモビオのソフト子会社が禁断のタッグ!?" |
| A8 | MarkLines 인터뷰 (ETAS K.K.·Elektrobit Japan 사장) |
| A9 | Elektrobit JSAE 2026 블로그 |
| B1 · B2 · B3 · B4 | Continental 인수(Noerr·Bloomberg) · AUMOVIO 상장(Deutsche Börse) · Elektrobit CES 2026 보도 · Revelio/Automotive World |
| B5 · B6 · B7 | Elektrobit 제품 페이지 · Canonical 블로그(2023-02-21, 직접 열람) · EB corbos Linux for Safety Applications 발표(2024-04-23) |
| B8 · B9 · B10 | embedded world 2026 보도 · Mobileye Drive 통합(2026-02-24) · Eclipse SDV WG 가입(2022) |
| C1 · C2 · C3 | OSADL ETAS 소개 · Bosch SW 집약(2021-12) · bitscale/Wikipedia 수치 |
| C4 · C5 · C6 · C7 | ETAS VSP Suite 플라이어 · ADAS/AD 프로파일 · General Purpose 프로파일 · EDMS 공개 문서 |
| C9 · C10 | ESCRYPT 제품 · ETAS×ThunderSoft(2025) |
| D1 · D2 · D3 · D4 | S-CORE 출범(Eclipse 뉴스룸) · 0.5-alpha(2025-11-17) · 0.6.0(2026-02) · Eclipse S-CORE articles(OCX 2026 시연) |
