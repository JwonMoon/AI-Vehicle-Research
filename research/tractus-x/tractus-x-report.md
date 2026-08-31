# Eclipse Tractus-X 조사 보고서

> 작성일: 2026-07-07 | 상세 근거·부가 자료: [tractus-x-research.md](tractus-x-research.md)
> 모든 사실 주장에 출처 병기. 출처 없는 항목은 `[출처 미확인]` 표기.

---

## 1. 요약 (Executive Summary)

| 항목 | 내용 |
|---|---|
| 정체 | **회사가 아님.** Eclipse Foundation 산하 오픈소스 소프트웨어 프로젝트 |
| 역할 | 자동차 데이터 생태계 **Catena-X**의 표준을 실제 동작하는 소프트웨어(참조 구현)로 만드는 "개발 본부" |
| 설립 | 2021-04-07 (Eclipse creation review) — Catena-X 컨소시엄 발의 ([projects.eclipse.org](https://projects.eclipse.org/projects/automotive.tractusx/reviews/creation-review)) |
| 소속 | Eclipse Foundation (비영리 오픈소스 재단, 회원 320+) ([About Us](https://eclipse-tractusx.github.io/AboutUs)) |
| 라이선스 | 코드 Apache-2.0 / 문서·모델 CC-BY-4.0 → 누구나 무료 사용·수정·재배포 ([GitHub](https://github.com/eclipse-tractusx)) |
| 규모 | 리포지토리 80개, 최근 12개월 커밋 8,270건·기여자 171명 ([metrics.eclipse.org](https://metrics.eclipse.org/projects/automotive.tractusx/), 2026-07 조회) |
| 왜 중요 | EU 규제(배터리 여권 등)로 기업 간 데이터 공유가 의무화되는 흐름에서, 그 인프라의 사실상 표준 구현체. 자동차를 넘어 화학·건설·반도체 등으로 확산 중 ([GitHub org README](https://github.com/eclipse-tractusx)) |

**한 문장 정리**: Tractus-X는 "독일 자동차 산업이 공동으로 만든 데이터 교환 인프라의 오픈소스 구현 프로젝트"이며, 회사(Catena-X 협회·Cofinity-X)들은 그 주변에서 표준 제정과 상용 운영을 맡는다.

---

## 2. 배경 — 본론을 읽기 위한 최소 지식

### 2.1 어떤 문제에서 출발했나

| 문제 | 구체 상황 |
|---|---|
| 공급망 깜깜이 | 완성차 업체는 1차 협력사까지만 보임. 2021년 반도체 대란 때 어느 하위 공장이 병목인지 파악 불가 — 이 위기가 직접적 출범 계기 (SAP 임원 Hagen Heubach 인터뷰, [diginomica](https://diginomica.com/inside-catena-x-automotive-industry-consortium-biggest-story-sap-isnt-talking-about-yet)) |
| EU 규제 | 배터리 규정(이력·탄소발자국 공개), 공급망 실사법 → 회사 간 데이터 공유가 법적 의무화 ([AWS 블로그](https://aws.amazon.com/blogs/industries/rapidly-experimenting-with-catena-x-data-space-technology-on-aws/)) |
| 신뢰 부재 | "내 원가·공급처 데이터가 경쟁사에 새면?" → 아무도 데이터를 안 내놓음 |

### 2.2 해법: 데이터스페이스(dataspace)

- 개념: 데이터를 중앙 서버에 모으지 않고(플랫폼 방식 아님), **각 회사가 데이터를 자기 서버에 둔 채** 표준 "커넥터"로 **계약 조건대로만** 상대에게 전달하는 분산 네트워크.
- 핵심 원칙 = **데이터 주권(data sovereignty)**: 내 데이터를 누가·언제·어떤 목적으로 쓸지 내가 통제하고, 그 계약이 기술적으로 강제됨.
- 비유: 중앙 창고(플랫폼)에 물건 다 맡기는 방식 ↔ 각자 창고를 지키면서 표준 규격 택배(커넥터)로 주고받는 방식.
- 블록체인 아님. 유럽 Gaia-X 원칙 + IDS(International Data Spaces) 표준 기반 ([diginomica](https://diginomica.com/inside-catena-x-automotive-industry-consortium-biggest-story-sap-isnt-talking-about-yet), [IDSA](https://internationaldataspaces.org/catena-x-network-for-cross-company-data-exchange-in-the-automotive-industry-relies-on-ids/)).

### 2.3 생태계 지도 — 3계층 분업 (Tractus-X의 위치)

```
[① 규칙]  Catena-X Automotive Network e.V. (독일 등록 협회, 베를린)
           표준 제정 · 인증 · "Catena-X" 상표 보유
                │ 표준을 넘김 / 위원회로 조율
[② 코드]  ★ Eclipse Tractus-X ★ (Eclipse Foundation 산하 오픈소스)
           표준의 참조 구현 + KIT 개발 — 본 보고서의 조사 대상
                │ 코드는 무료 공개 (Apache 2.0)
[③ 운영]  Cofinity-X 등 운영사 + 솔루션 기업들 (영리)
           온보딩 · 인증 앱 마켓플레이스 · 상용 서비스
```

- 왜 나눴나: 한 회사가 규칙+코드+운영을 다 쥐면 종속(lock-in) 발생 → 경쟁사 참여 거부. 규칙은 중립 협회, 코드는 오픈소스, 운영은 경쟁 시장으로 분산 ([About Us](https://eclipse-tractusx.github.io/AboutUs)).
- 이름이 다른 이유: 협회가 "Catena-X"를 상표로 지키고 싶어 오픈소스 프로젝트는 별도 이름 "Tractus-X" 사용 ([About Us](https://eclipse-tractusx.github.io/AboutUs)).
- 개발 프로젝트만 협회 산하가 아니라 **외부 재단(Eclipse)에 위탁** — 중립성 장치. 협회는 위원회·전문가 그룹으로 조율만 ([Tractus-X 101 공식 문서](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf)).

### 2.4 필수 용어 8개 (전체 용어집: 상세 자료집 §2)

| 용어 | 뜻 |
|---|---|
| OSS | 오픈소스 소프트웨어. 코드 공개 → 누구도 독점 못 함 |
| Eclipse Foundation | 세계 최대급 오픈소스 비영리 재단. 기업들이 공동 개발할 때 중립 심판·법적 틀 제공 |
| 커넥터 / EDC | 데이터스페이스 접속 장치("데이터 출입국 관리소"). EDC = 그 표준 구현 소프트웨어 |
| KIT | Keep It Together. 하나의 업무 시나리오(예: 탄소발자국 교환)에 필요한 표준+API+코드+가이드 "조립 키트" |
| 참조 구현 | "표준을 코드로 이렇게 구현하면 된다"는 공식 견본. 그대로 상용은 아니고 기준점 |
| 디지털 트윈 | 실물 부품의 디지털 분신. 표준 포맷 = AAS |
| PCF / DPP | 제품 탄소발자국 / 디지털 제품 여권(EU가 배터리에 의무화하는 제품 이력서) |
| 시맨틱 모델 | 데이터 의미 사전("배터리 용량 = kWh 숫자"). 회사마다 다른 양식 문제 제거 |

---

## 3. 본론 — Tractus-X 프로젝트 프로필

### 3.1 개요

- 공식 명칭: Eclipse Tractus-X™. Catena-X 생태계 및 Manufacturing-X 계열의 **공식 오픈소스 프로젝트** ([About Us](https://eclipse-tractusx.github.io/AboutUs)).
- 미션: "신뢰 가능한 오픈 표준으로 공급망 전반의 안전·효율적 데이터 교환과 매끄러운 협업" ([GitHub org](https://github.com/eclipse-tractusx)).
- 개발 철학 ([Tractus-X 101](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf)):
  - **code-first**: 코드 먼저 만들고, 검증된 것을 표준 후보로 역추출
  - **open core**: 차별화 안 되는 공통 기능은 공동 개발, 각사는 그 위에 확장으로 경쟁
  - "자동차 산업이 자동차 산업을 위해 정의·개발, 단일 기업이 통제하지 않음"

### 3.2 연혁

| 시기 | 사건 | 출처 |
|---|---|---|
| 2021-04-07 | Eclipse creation review — Catena-X 컨소시엄 발의 | [projects.eclipse.org](https://projects.eclipse.org/projects/automotive.tractusx/reviews/creation-review) |
| 2022 | 첫 릴리스 2.0/2.1 | [changelog](https://eclipse-tractusx.github.io/blog-changelog/) |
| 2023-04 | 릴리스 3.0. 이후 23.09부터 연월(YY.MM) 버저닝 | [changelog](https://eclipse-tractusx.github.io/blog-changelog/) |
| 2023 Q3~Q4 | 전체 팀 공개 협업 전환 | [Tractus-X 101](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf) |
| 2024 Q1~Q2 | 협회와 협업 거버넌스 확립, Eclipse incubation(수습) 졸업 계획 | [Tractus-X 101](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf) |
| 2024 | 24.05/24.08 breaking change 릴리스 | [Cofinity-X 해설](https://www.cofinity-x.com/blog/catena-x-breaking-change-release-2024) |
| 2026-03-18 | 릴리스 26.03: 신규 KIT 6종(AI Service, CBAM 등), Identity Hub 도입, 기여자 151명 | [26.03 changelog](https://eclipse-tractusx.github.io/blog-changelog/release-26-03/) |
| 2026-06-17 | 릴리스 26.06 (최신): 신규 KIT 2종(Material Accounting, Autonomous Operation), 기여자 112명 | [changelog](https://eclipse-tractusx.github.io/blog-changelog/) |
| 2026-07-02~03 | 6차 Community Days (슈투트가르트 ARENA2036). 모토 "Making Data Spaces Work – Together", Manufacturing-X 프로젝트 간 협업·E2E 보안·virtual EDC 주제 | [ARENA2036](https://arena2036.de/en/reader/sixth-eclipse-tractus-x-community-days/) |

### 3.3 조직·거버넌스

- 소속: Eclipse Foundation → 오픈 거버넌스(행동강령, ECA 기여자 계약, 커미터 선출제) ([GitHub org](https://github.com/eclipse-tractusx)).
- **프로젝트 리드 4인**: Mikel Garcia, Mathias Brunkow Moser, Stephan Bauer, Björn Roy. 활동 커미터 40+명, 추가 기여자 100+명 ([projects.eclipse.org/who](https://projects.eclipse.org/projects/automotive.tractusx/who), 2026-07 조회).
- **SIG(분과) 4개**: Architecture / Infrastructure / Release / Security. 회의록 공개 운영 ([사이트 sitemap](https://eclipse-tractusx.github.io/), [sig-release](https://github.com/eclipse-tractusx/sig-release)).
- 공통 규칙 = **TRG**(Tractus-X Release Guidelines) ([GitHub org README](https://github.com/eclipse-tractusx)).

### 3.4 제품 라인업 ① — 핵심 소프트웨어 컴포넌트

리포 80개 중 대표 ([GitHub](https://github.com/eclipse-tractusx), ★는 2026-07 조회):

| 컴포넌트 | 역할 |
|---|---|
| **tractusx-edc** (★87) | 간판 제품. 데이터스페이스 접속 커넥터. upstream인 [Eclipse EDC](https://projects.eclipse.org/projects/technology.edc)에 Catena-X 확장 + 배포 패키징. 계약 협상(Control-Plane)과 실제 전송(Data-Plane) 분리 |
| **sldt-digital-twin-registry / sldt-semantic-models** (★50) | 디지털 트윈 "전화번호부"(AAS 표준) + 데이터 의미 사전(SAMM) |
| **portal / bpdm** | 참여자 등록·온보딩 포털 + 사업자 식별번호(BPN) 관리 — 운영사가 돌리는 코어 서비스 ([Operator 페이지](https://eclipse-tractusx.github.io/Operator/)) |
| **digital-product-pass** (★50) | 디지털 제품 여권(DPP) 뷰어 — EU 배터리 규정 대응 |
| **traceability-foss / puris** | 부품 추적성 / 단기 수요·공급 실시간 공유 |
| **industry-core-hub** | 최근 12개월 최다 커밋(1,658) — 유스케이스 도입 가속이 현재 주력 방향 ([metrics](https://metrics.eclipse.org/projects/automotive.tractusx/)) |
| **tractus-x-umbrella** | 전체 스택 로컬 체험용 통합 배포판 |

### 3.5 제품 라인업 ② — KIT 프레임워크

- KIT = 유스케이스별 "조립 키트": 표준·시맨틱 모델·API 명세·참조 구현·설치 스크립트를 한 상자에 ([KITs 101](https://catena-x.academy/wp-content/uploads/2024/09/4.4-Catena-X-Development-Area-KIT-101.pdf)).
- 모든 KIT 공통 구조 = **5개 뷰**: Adoption(경영 관점) / Development(개발) / Operations(운영) / Documentation / Industry Extensions ([KIT Framework 문서](https://eclipse-tractusx.github.io/documentation/kit-framework/)).
- 카탈로그 4분류 ([Kits 페이지](https://eclipse-tractusx.github.io/Kits)):
  1. Dataspace Foundation (Connector, Digital Twin, Business Partner 등)
  2. Industry Core Foundation (Traceability, Data Chain 등)
  3. Cross-Industry 20+ (탄소발자국 PCF, 순환경제, CBAM, 수요·공급 DCM 등)
  4. 산업별 (자동차·제조·반도체·건설·화학)
- **Framework 2.0**: 자동차 전용 → 멀티 산업·멀티 데이터스페이스 지원으로 확장 ([KIT Framework 문서](https://eclipse-tractusx.github.io/documentation/kit-framework/)).

### 3.6 릴리스 체계

- 분기 릴리스 + 캘린더 버저닝(YY.MM). 연간 **메이저 1회**(호환성 깨는 변경 허용) + **마이너 3회**(하위 호환) + 수시 패치 ([sig-release](https://github.com/eclipse-tractusx/sig-release)).
- Catena-X 표준이 "인증 취득의 구속력 있는 기준"이며 Tractus-X 구현이 이에 정렬 ([sig-release](https://github.com/eclipse-tractusx/sig-release)).

### 3.7 활동 지표 (최근 12개월, [metrics.eclipse.org](https://metrics.eclipse.org/projects/automotive.tractusx/) 2026-07 조회)

- 커밋 8,270 / 기여자 171명 / 이슈 1,138 / 코드리뷰 1,468.
- 언어: Java 중심 + TypeScript, Python, C#, Kotlin.

---

## 4. 생태계 — 주변 조직 상세

### 4.1 Catena-X Automotive Network e.V. (표준·거버넌스 협회)

- **2021-05-15 창립** ([공식 발표](https://catena-x.net/en/news-dates/artikel/may-15-2021-catena-x-automotive-network-ev-founded)). 창립 17개사: BMW·Mercedes-Benz·VW(완성차), Bosch·ZF·Schaeffler(부품), SAP·Siemens·Telekom(IT), BASF·Henkel(화학), Fraunhofer·DLR(연구), ARENA2036, SupplyOn, German Edge Cloud, ISTOS.
- 초대 의장 Oliver Ganser(BMW), 부의장 Boris Otto(Fraunhofer ISST), 재무 Claus Cremers(Siemens) ([공식 발표](https://catena-x.net/en/news-dates/artikel/may-15-2021-catena-x-automotive-network-ev-founded)).
- 자금: 독일 연방경제기후보호부(BMWK) 1억 유로 이상, 컨소시엄 2021-08~2024-07 `[2차 출처 — DLR·Fraunhofer 페이지 경유, 원문 재확인 권장]`.
- **2023-10 데이터스페이스 상용 가동(go-live)** — 최초의 산업화된 Gaia-X 호환 생태계 ([BMW Group](https://www.bmwgroup.com/en/news/general/2023/catenax.html)).
- 회원: 공식 명단(2025-03-04자) 기준 약 170개사 — Microsoft·AWS·IBM·Huawei·Fujitsu·CATL·Renault·Volvo·Ford·Magna·Valeo 등 글로벌 확대. 한국계는 INTERX, Taelim 정도로 소수, 국내 대기업 부재 ([회원 명단 PDF](https://catena-x.net/wp-content/uploads/2025/04/Catena-X_List-of-Members.pdf) 자체 집계).
- 주력 유스케이스 5영역: 품질관리·물류·유지보수·공급망관리·지속가능성 ([BMW Group](https://www.bmwgroup.com/en/news/general/2023/catenax.html)).
- 주요 회원 솔루션: SAP(추적성·Scope 3 배출량, [SAP](https://www.sap.com/sea/industries/automotive/industry-network-automotive.html)), Siemens(중소기업용 앱), T-Systems(온보딩 패스트트랙, [T-Systems](https://www.t-systems.com/de/en/insights/newsroom/news/t-systems-fast-tracks-catena-x-supplier-onboarding-1086404)).

### 4.2 Cofinity-X (운영사) + 마켓플레이스

- 2023년 T-Systems 포함 10개사(BMW·SAP·Siemens·VW 등) 합작 설립. 1호 운영사 ([Telekom](https://www.telekom.com/en/media/media-information/archive/cofinity-x-open-marketplace-for-catena-x-1025336)).
- 역할: BPN 발급·온보딩·인프라 + **인증 앱 마켓플레이스**(B2B 앱스토어). 45개+ 인증 앱·서비스가 OEM·Tier 1에서 실사용 중 ([Cofinity-X](https://www.cofinity-x.com/apps)).
- 운영 위임 2028년까지 연장 ([Cofinity-X 발표](https://www.cofinity-x.com/blog/cofinity-x-extends-mandate-as-operating-company-for-catena-x-through-2028)).
- 혼동 주의: GM·Magna·Wipro의 [SDVerse](https://www.magna.com/stories/news-press-release/2024/general-motors--magna-and-wipro-team-up-to-develop-automotive-software-marketplace--'sdverse')는 **차량 탑재용 임베디드 SW** 거래 플랫폼 — 형식만 비슷, 무관.

### 4.3 Manufacturing-X 확산 (Tractus-X 코드의 재사용처)

GitHub org README가 공식 명시한 관련 프로젝트 ([원문](https://github.com/eclipse-tractusx)):

| 프로젝트 | 분야 |
|---|---|
| [Eclipse EDC](https://projects.eclipse.org/projects/technology.edc) | upstream 커넥터 기술 |
| [Catena-X](https://catena-x.net/en/) | 자동차 (운영: Cofinity-X) |
| [Factory-X](https://factory-x.org) | 공장 운영·설비 |
| [Chem-X](https://www.chem-x.de) | 화학 |
| [Construct-X](https://construct-x.org) | 건설 |
| [Wind-X](https://www.iat.rwth-aachen.de/cms/iat/forschung/projekte/~bkmazw/wind-x/) | 풍력 |
| [Semiconductor-X](https://www.semiconductor-x.com) | 반도체 공급망 |

- Catena-X↔Factory-X 상호운용 쇼케이스: Hannover Messe 2026-04 시연 (GEC+Cofinity-X, [GEC 발표](https://gec.io/en/news/news-detail/catena-x-meets-factory-x-gec-and-cofinity-x-realize-a-showcase-for-interoperable-data-exchange-193/)).

### 4.4 국제 행보

- 지역 허브: 북미 AIAG(1호 국제 허브 계약), 프랑스 GALIA/PFA, 스페인, 스웨덴, 중국은 CAAM·VDA 협력 ([catena-x.net](https://catena-x.net/about-us/)).
- 일본: 2024-04 IPA와 MoU → 2025-03 **Ouranos Ecosystem과 상호운용 실증 성공**(배터리 탄소발자국 교환, EU 배터리 규정 대응) ([Catena-X 발표](https://catena-x.net/news/catena-x-and-ouranos-ecosystem-successfully-demonstrate-data-space-interoperability/), [IPA](https://www.ipa.go.jp/en/pressrelease/press20250331.html)). DENSO가 일본계 최초 EcoPass 인증 ([DENSO](https://www.denso.com/global/en/news/newsroom/2025/20250324-g01/)).

---

## 5. 참여 관점 — 누가 어떻게 쓰나

| 역할 | 정체 | 시작 방법 | 출처 |
|---|---|---|---|
| **User/Adopter** | 데이터 주고받을 제조·부품 기업 | ① 유스케이스 선택(예: PCF KIT) ② E2E 가이드로 기술 요건 충족 ③ 사내 시스템을 시맨틱 모델에 매핑 | [User 페이지](https://eclipse-tractusx.github.io/User/) |
| **App Provider** | 앱 만들어 파는 SW 기업 | KIT+API 명세+시맨틱 모델 조합해 개발 → 인증 → 마켓플레이스 배포 | [AppProvider 페이지](https://eclipse-tractusx.github.io/AppProvider/) |
| **Operator** | 코어 서비스 운영사 | 포털·BPDM·Semantic Hub·Discovery 등 운영 | [Operator 페이지](https://eclipse-tractusx.github.io/Operator/) |
| **개발자(개인/기업)** | 오픈소스 기여자 | Eclipse 계정 + ECA 서명 → GitHub 기여, Matrix·오피스아워 참여 | [Getting Started](https://eclipse-tractusx.github.io/docs/getting-started/) |

- 체험 환경: **MXD**(최소 데이터스페이스 샌드박스, [E2E 튜토리얼](https://eclipse-tractusx.github.io/docs/tutorials/e2e/)), AWS 배포 샘플 ([AWS 블로그](https://aws.amazon.com/blogs/industries/rapidly-experimenting-with-catena-x-data-space-technology-on-aws/)).

---

## 6. 평가·전망

**강점 (사실 기반)**
- 실가동 중: 2023-10 go-live 후 45+ 상용 인증 앱, OEM·Tier 1 실사용 ([Cofinity-X](https://www.cofinity-x.com/apps)).
- 살아있는 개발: 최근 1년 커밋 8,270건, 분기 릴리스 유지 ([metrics](https://metrics.eclipse.org/projects/automotive.tractusx/)).
- 확장성 입증: 코드가 6개+ 타 산업 이니셔티브에 재사용, 일본과 국경 간 상호운용 실증 ([IPA](https://www.ipa.go.jp/en/pressrelease/press20250331.html)).

**과제·리스크 (사실 + 해석 구분)**
- 독일·유럽 중심 편중 — 회원 명단상 한국 대기업 부재 (사실, [명단](https://catena-x.net/wp-content/uploads/2025/04/Catena-X_List-of-Members.pdf)). 글로벌 표준 되려면 아시아 OEM 참여가 관건 (해석).
- breaking change 릴리스(24.05/24.08)가 참여 기업에 마이그레이션 부담 (사실, [Cofinity-X](https://www.cofinity-x.com/blog/catena-x-breaking-change-release-2024)).
- 25.09 릴리스 때 테스트·출시에 상용 앱 기반 임시 브리징 사용 — 순수 오픈소스 자립성에 대한 시사점 (사실, [25.09 changelog](https://eclipse-tractusx.github.io/blog-changelog/release-25-09/); 평가는 해석).
- 제3자 시각: "SAP 마케팅 아니냐"는 초기 의심에 대해 diginomica는 진성 산업 협력 모델로 평가 ([기사](https://diginomica.com/inside-catena-x-automotive-industry-consortium-biggest-story-sap-isnt-talking-about-yet), 2021년 기사임에 유의).

**최신 동향 (2026-07 기준)**
- 26.06 릴리스(6/17) 직후, 6차 Community Days(7/2~3) 직후 시점. 협회 5주년 기념행사 2026-10-15 뮌헨 예정 ([catena-x.net](https://catena-x.net/news/)).

---

## 7. 부록 안내

상세 자료집([tractus-x-research.md](tractus-x-research.md))에 수록:
- 전체 용어집(20개) / Catena-X 연혁 전체 타임라인 / KIT 전체 카탈로그
- 원 레퍼런스 4건 분석(YouTube 자막 포함) / 소스별 요약·접근 실패 기록 / 미확인 사항 목록
