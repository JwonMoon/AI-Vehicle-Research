# Tractus-X 상세 자료집 (보고서 부록)

> 본편: [tractus-x-report.md](tractus-x-report.md) | 갱신일: 2026-07-07
> 성격: 보고서에 다 못 담은 근거·원문 분석·전체 목록 모음. 섹션 번호는 독립.

---

## A. 전체 용어집

| 용어 | 뜻 |
|---|---|
| OSS (Open Source Software) | 소스코드 공개 소프트웨어. 무료보다 "투명·비독점"이 핵심 |
| Eclipse Foundation | 오픈소스 비영리 재단(회원 320+). 기업 공동 개발의 중립 심판·인프라·법적 틀. Eclipse IDE로 유명하나 현재는 수백 개 프로젝트의 우산 |
| e.V. | eingetragener Verein, 독일 등록 협회(비영리 사단법인) |
| 데이터스페이스(dataspace) | 중앙 집중 없이 표준 커넥터로 계약 기반 데이터 교환하는 분산 네트워크 |
| 데이터 주권(data sovereignty) | 데이터 소유자가 사용 조건(누가/언제/목적)을 통제하는 원칙 |
| cxOS | Catena-X operating system. 생태계 공통 기반 SW 묶음의 별칭 — "그 위에서 앱이 도는 판" ([Tractus-X 101](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf)) |
| KIT (Keep It Together) | 유스케이스별 표준·API 명세·데이터 모델·참조 구현·설치 가이드 묶음 |
| 참조 구현(reference implementation) | 표준의 공식 견본 코드. 일부 산업화 작업 필요 — 그대로 프로덕션 아님 (Tractus-X 101 명시) |
| EDC (Eclipse Dataspace Components) | 커넥터 소프트웨어. Control-Plane(자산·계약·협상)/Data-Plane(실전송) 분리 |
| 디지털 트윈 / AAS / DTR | 실물의 디지털 분신 / 그 표준 포맷(Asset Administration Shell) / 분신들의 레지스트리 |
| 시맨틱 모델 / SAMM | 데이터 의미 사전 / 그 작성 언어. sldt = Semantic Layer Digital Twin |
| BPN / BPDM | Business Partner Number(참여사 고유 식별번호) / 그 관리 컴포넌트 |
| SSI / DID / MIW | 자기주권신원 / 분산 식별자 / Managed Identity Wallet(초기 구현; 26.03부터 Identity Hub로 진화) |
| PCF | Product Carbon Footprint, 제품 탄소발자국 |
| DPP | Digital Product Passport, 디지털 제품 여권(EU 배터리 의무화) |
| PLM | Product Lifecycle Management, 제품 전 생애 관리 |
| OEM / Tier N | 완성차 업체 / N차 협력사 |
| 커미터 / PMC / ECA | 코드 반영 권한자 / 프로젝트 운영위 / Eclipse 기여자 계약 |
| TRG | Tractus-X Release Guidelines — 전 리포 공통 규칙·모범사례 |
| Helm / K8s | 컨테이너 오케스트레이션(K8s)과 그 패키지 매니저(Helm). Tractus-X 배포 방식 |
| CBAM | EU 탄소국경조정제도 (해당 KIT 존재) |
| DCM | Demand & Capacity Management, 수요·공급 관리 |

---

## B. Catena-X 전체 타임라인

| 시기 | 사건 | 출처 |
|---|---|---|
| 2020-12 | 독일 연방정부 디지털 서밋에서 구상 발표 | 검색 경유 `[원문 재확인 필요]` |
| 2021-03 | 얼라이언스 가속 발표 | [SAP News](https://news.sap.com/2021/03/catena-x-automotive-alliance-picks-up-speed/) |
| 2021-04-07 | Eclipse Tractus-X creation review | [projects.eclipse.org](https://projects.eclipse.org/projects/automotive.tractusx/reviews/creation-review) |
| 2021-05-15 | 협회 창립 총회 (17개사) — ⚠️ 일부 소스 5/7 표기, 공식 발표는 5/15 | [catena-x.net](https://catena-x.net/en/news-dates/artikel/may-15-2021-catena-x-automotive-network-ev-founded) |
| 2021-08 | BMWK 컨소시엄 시작(28개 파트너, 1억 유로+, ~2024-07) | 검색 경유 `[2차 출처]` |
| 2021-11 | 회원 62개사 | [diginomica](https://diginomica.com/inside-catena-x-automotive-industry-consortium-biggest-story-sap-isnt-talking-about-yet) |
| 2023 | Cofinity-X 설립(T-Systems 외 9개사) | [Telekom](https://www.telekom.com/en/media/media-information/archive/cofinity-x-open-marketplace-for-catena-x-1025336) |
| 2023-05 | BETA 완료(표준 확정) | 검색 경유 |
| 2023-10 | 데이터스페이스 go-live | [BMW Group](https://www.bmwgroup.com/en/news/general/2023/catenax.html) |
| 2024-04 | 일본 IPA와 MoU | [IPA](https://www.ipa.go.jp/en/pressrelease/press20250331.html) |
| 2024-07 | 컨소시엄 종료 → 협회 주도 | 검색 경유 |
| 2025-03 | Ouranos 상호운용 실증(배터리 PCF) / DENSO 일본계 최초 EcoPass 인증 | [Catena-X](https://catena-x.net/news/catena-x-and-ouranos-ecosystem-successfully-demonstrate-data-space-interoperability/), [DENSO](https://www.denso.com/global/en/news/newsroom/2025/20250324-g01/) |
| 2025-04 | NTT DATA 배터리 추적 플랫폼 상호운용 실증 | [NTT DATA](https://www.nttdata.com/global/en/news/press-release/2025/april/042200) |
| 2026-04 | Hannover Messe: Catena-X↔Factory-X 쇼케이스 | [GEC](https://gec.io/en/news/news-detail/catena-x-meets-factory-x-gec-and-cofinity-x-realize-a-showcase-for-interoperable-data-exchange-193/) |
| 2026-04-23 | 협회 총회(General Assembly) | [catena-x.net](https://catena-x.net/news/) |
| 2026-07-02~03 | 6차 Tractus-X Community Days (슈투트가르트) | [ARENA2036](https://arena2036.de/en/reader/sixth-eclipse-tractus-x-community-days/) |
| 2026-10-15 | 협회 5주년 기념행사 (뮌헨) 예정 | [catena-x.net](https://catena-x.net/news/) |

---

## C. 회원 명단 분석 ([공식 PDF, 2025-03-04자](https://catena-x.net/wp-content/uploads/2025/04/Catena-X_List-of-Members.pdf))

- 규모: 3페이지 명단, 약 170개사(자체 집계 — 페이지당 약 60개).
- 글로벌 빅테크·IT: Microsoft, AWS, IBM, Huawei, Fujitsu, Palantir, Accenture, Capgemini, Deloitte, T-Systems.
- 완성차·부품 (독일 외): Renault, Volvo Car/Volvo Purchasing, Ford Werke, Magna, Valeo, Faurecia, Brembo, CATL(Contemporary Amperex), Continental, Dräxlmaier, Witte.
- 아시아: 중국(Nanjing Fuchuang, Shanghai Ecarbon, Shenzhen Precise Testing, Suzhou Tech-D, CATL, Huawei), 일본(Asahi Kasei Europe, Denso Automotive Deutschland, NTT Communications, Fujitsu), 대만(ITRI), 한국(INTERX Co., Ltd., Taelim Co., Ltd. — 소수).
- 산업 단체: AIAG(미), GALIA·PFA(프), Mobility Sweden, VDA(독), ADAC, ECLASS.
- **관찰**: 한국 대기업(현대차·LG·삼성 계열) 명단에 없음(2025-03 기준). EU 배터리 규정 당사자인 한국 배터리 3사 부재는 눈에 띄는 공백.

---

## D. 원 레퍼런스 4건 분석

### D.1 [projects.eclipse.org](https://projects.eclipse.org/projects/automotive.tractusx)
- 접근: 메인 페이지는 fetch 반복 실패했으나 **/who 하위 페이지 접속 성공**(2026-07-07) → 리드 검증 완료.
- 확인 사실: 리드 4인(Mikel Garcia, Mathias Brunkow Moser, Stephan Bauer, Björn Roy), 활동 커미터 40+, 추가 기여자 100+ ([who 페이지](https://projects.eclipse.org/projects/automotive.tractusx/who)).
- Creation review 2021-04-07. 릴리스 리뷰·progress review 문서 다수 존재(2025.07, 2025.10 등).

### D.2 YouTube "Tractus-X" ([링크](https://www.youtube.com/watch?v=iIaH71z7ENg))
- 채널: Catena-X Automotive Network e.V. 공식 (oembed 확인). 업로드일·조회수 `[출처 미확인 — API 차단]`.
- 자막(`[English] Tractus-X.tct`) 전문 분석:
  - 참여자 2유형: Adopter(DIY로 데이터 제공/소비 연결) / Solution Provider(상호운용 솔루션 개발, KIT·오픈소스로 가속).
  - Tractus-X = "KIT의 본거지(home of our Kits)". Eclipse Foundation 산하.
  - KIT는 Apache 2.0 → 어떤 환경에서든 사용·수정·배포 가능.
  - 프로젝트는 **4개 도메인**: Shared Network(기반) / PLM & Quality / Resiliency / Sustainability. 도메인마다 아티팩트 툴박스 페이지 제공.
  - Solution Provider: KIT 조합+API 스펙+시맨틱 모델로 신규 앱. Adopter: 참조 구현+퀵셋업 가이드로 사내 인프라 연결.

### D.3 [About Us](https://eclipse-tractusx.github.io/AboutUs)
- 생태계 3분할: 협회(표준화·인증·거버넌스) / 개발 환경(참조 구현) / 운영 환경(자유 사용·수정·운영).
- 명칭 분리 이유: 협회가 Catena-X 상표 유지 희망.
- Factory-X·Manufacturing-X·Construct-X·Semiconductor-X 협력 명시.

### D.4 [GitHub org](https://github.com/eclipse-tractusx) — README 전문 반영
- 슬로건 "Where we build dataspaces!", 리포 80개, 2FA 강제.
- 비전 5항: 협력 활성화 / 투명성·지속가능성 / 오픈 표준 혁신 / 데이터 주권·프라이버시 / KIT 방식 유스케이스 커버.
- **Related Projects 7개 (README 명시 전체)**:

| 프로젝트 | 설명 | 링크 |
|---|---|---|
| Eclipse Dataspace Components | 안전·표준화 데이터 공유 컴포넌트 (tractusx-edc의 upstream) | [projects.eclipse.org/projects/technology.edc](https://projects.eclipse.org/projects/technology.edc) |
| Catena-X Ecosystem | 자동차 데이터 생태계 (운영 Cofinity-X) | [catena-x.net](https://catena-x.net/en/) |
| Chem-X | 화학 데이터스페이스 | [chem-x.de](https://www.chem-x.de) |
| Construct-X | 건설 데이터스페이스 | [construct-x.org](https://construct-x.org) |
| Wind-X | 풍력 연합형 분산 데이터스페이스 (RWTH Aachen IAT) | [iat.rwth-aachen.de](https://www.iat.rwth-aachen.de/cms/iat/forschung/projekte/~bkmazw/wind-x/) |
| Semiconductor-X | 반도체 공급망 디지털 트윈 표준 | [semiconductor-x.com](https://www.semiconductor-x.com) |
| Factory-X | 공장 운영자·설비사용 협업 생태계 | [factory-x.org](https://factory-x.org) |

- 참여 절차: Eclipse 계정 → GitHub(2FA) → ECA 서명 → 기여. 컨트리뷰터 역할은 커미터 추가 또는 이슈 템플릿 "Support: Add me as Tractus-X project contributor".
- 거버넌스: 행동강령, TRG, 보안 신고 TRG 8 + sig-security.
- 채널: tractusx-dev 메일링리스트, [Matrix](https://matrix.to/#/#tractusx:matrix.eclipse.org), 블로그, 오피스아워, [릴리스 플래닝 보드](https://github.com/orgs/eclipse-tractusx/projects/26).

---

## E. Tractus-X 기술 상세

### E.1 주요 리포지토리 (★ 2026-07 조회)
| 리포 | 역할 |
|---|---|
| tractusx-edc (★87) | EDC의 Catena-X 배포판. upstream 확장 + 도커/헬름 패키징 |
| digital-product-pass (★50) | DPP 뷰어 |
| sldt-semantic-models (★50) | SAMM 시맨틱 모델 모음 |
| sldt-digital-twin-registry | AAS 디지털 트윈 레지스트리 |
| traceability-foss | 추적성 앱 ([arc42 문서](https://eclipse-tractusx.github.io/traceability-foss/docs/arc42/full.html)) |
| puris | 단기 수요·공급 실시간 공유 |
| industry-core-hub | 최근 12개월 최다 커밋(1,658) |
| tractus-x-umbrella | 통합 헬름 배포 |
| bpdm / portal-frontend | BPN 관리 / 포털·마켓 접근 ([Operator 페이지](https://eclipse-tractusx.github.io/Operator/)) |

### E.2 운영사(Operator) 담당 코어 컴포넌트 ([Operator 페이지](https://eclipse-tractusx.github.io/Operator/))
BPDM(파트너 데이터·BPN), Portal & Marketplace(등록·온보딩), Semantic Hub(모델 관리), Discovery Finder / BPN Discovery(검색).

### E.3 커뮤니티 운영 ([community/intro](https://eclipse-tractusx.github.io/community/intro), [sig-release](https://github.com/eclipse-tractusx/sig-release))
- SIG 4개: Architecture / Infrastructure / Release / Security. 회의록 월별 공개.
- 미팅 3분류: General Office Hours / Product Meetings / One-Time Events. 미팅 추가도 PR(`data/meetings.js`).
- 릴리스 전략: 분기 캘린더 버저닝, 연 메이저 1 + 마이너 3 + 패치.

### E.4 릴리스 이력 전체 ([changelog](https://eclipse-tractusx.github.io/blog-changelog/))
2.0/2.1(2022) → 3.0(2023-04)/3.0.1/3.1.0 → 23.09/23.12 → 24.03/**24.05/24.08(breaking)**/24.12 → 25.03/25.06(2025-07-16)/25.09(2025-10-01, 상용 앱 기반 임시 브리징으로 테스트·출시)/25.12 → 26.03(2026-03-18, KIT 6종+Identity Hub, 기여자 151) → 26.06(2026-06-17, KIT 2종, 기여자 112·커미터 20, K8s 1.34.1/PostgreSQL ≥15.4 기준).

### E.5 체험·실습 경로
- [E2E Adopter Journey](https://eclipse-tractusx.github.io/docs/tutorials/e2e/): IT 부서 대상 3장(Inform→Connect→Boost). **MXD** = EDC+Keycloak+MIW 로컬 샌드박스. Docker/K8s/Helm/Terraform 필요.
- [AWS 샘플](https://aws.amazon.com/blogs/industries/rapidly-experimenting-with-catena-x-data-space-technology-on-aws/): EKS+Aurora+S3 배포, 자산→정책→계약→전송 데모.

---

## F. KIT 상세

### F.1 구조 ([KITs 101](https://catena-x.academy/wp-content/uploads/2024/09/4.4-Catena-X-Development-Area-KIT-101.pdf), 2023-10-09 v1.0)
- 최소 요소: 시맨틱 모델, 로직/스키마, API 명세, 접근·사용 정책.
- 툴박스 4층: Adoption(비전/가치/튜토리얼/백서) → 표준화·인증 대상(모델/스키마/프로세스/정책) → Development(API/프로토콜/샘플데이터/참조구현/아키텍처 = 적합성 평가 기준) → Operation(퀵셋업/HELM 스크립트).
- 편익 5: 투명성 / 재사용 비용절감 / 혁신 / 상호운용·주권 정합 / 생태계 형성.

### F.2 Framework 2.0 ([kit-framework 문서](https://eclipse-tractusx.github.io/documentation/kit-framework/))
- 필수: 저작권(CC-BY-4.0), Changelog(시맨틱 버저닝), 5개 뷰(Adoption/Development/Operations/Documentation/Industry Extensions).
- 1.0→2.0: 자동차 전용 → 멀티 산업·멀티 데이터스페이스.

### F.3 카탈로그 ([Kits](https://eclipse-tractusx.github.io/Kits), graduated/incubating 등급제)
- Dataspace Foundation: Connector, Data Governance, Data Trust & Security, Business Partner, Digital Twin
- Industry Core Foundation: Industry Core, AI Service, Data Chain, Knowledge Agents, Supply Chain Disruption Notification, Traceability
- Cross-Industry 20+: Behaviour Twin, CBAM, Circularity, PCF, PURIS, DCM, Eco Pass, Logistics, Material Accounting, ESS, Customs, Geometry 등
- 산업별: 자동차(Engineering as a Service, Modular Engineering), 제조(Autonomous Operation, MaaS, Modular Production), 반도체·건설·화학

---

## G. 소스 대장 (전체)

| 소스 | 유형 | 내용 | 접근 상태 |
|---|---|---|---|
| [projects.eclipse.org](https://projects.eclipse.org/projects/automotive.tractusx) | 공식 | 프로젝트 등록·리드·릴리스 | 메인 실패 / [who](https://projects.eclipse.org/projects/automotive.tractusx/who) 성공(2026-07-07) |
| [YouTube Tractus-X](https://www.youtube.com/watch?v=iIaH71z7ENg) | 공식 영상 | 소개 영상 | 메타데이터 차단, 자막 로컬 확보 |
| [About Us](https://eclipse-tractusx.github.io/AboutUs) | 공식 | 3계층 구조 | 정상 |
| [GitHub org](https://github.com/eclipse-tractusx) + [README raw](https://raw.githubusercontent.com/eclipse-tractusx/.github/main/profile/README.md) | 공식 | 비전·related projects·참여 | 정상 |
| [Tractus-X 101 PDF](https://catena-x.academy/wp-content/uploads/2024/09/4.2_Catena-X-Development-Area-Eclipse-Tractus-X-101.pdf) / [KITs 101 PDF](https://catena-x.academy/wp-content/uploads/2024/09/4.4-Catena-X-Development-Area-KIT-101.pdf) | 공식 교육자료(2023-10) | cxOS·open core·KIT 구조 | 정상(PDF 직접 판독) |
| [catena-x.net](https://catena-x.net/about-us/) + [회원 명단 PDF](https://catena-x.net/wp-content/uploads/2025/04/Catena-X_List-of-Members.pdf) | 공식 | 협회 구조·회원 | 정상 |
| [metrics.eclipse.org](https://metrics.eclipse.org/projects/automotive.tractusx/) | 공식 | 활동 지표 | 정상 |
| [changelog](https://eclipse-tractusx.github.io/blog-changelog/) / [sig-release](https://github.com/eclipse-tractusx/sig-release) | 공식 | 릴리스 이력·전략 | 정상 |
| [KIT Framework](https://eclipse-tractusx.github.io/documentation/kit-framework/) / [Kits](https://eclipse-tractusx.github.io/Kits) / [Kit-Deepdive](https://eclipse-tractusx.github.io/Kit-Deepdive) | 공식 | KIT 체계 | 정상 (`/community/sigs`는 404) |
| 역할 페이지 [User](https://eclipse-tractusx.github.io/User/)·[AppProvider](https://eclipse-tractusx.github.io/AppProvider/)·[Operator](https://eclipse-tractusx.github.io/Operator/)·[Getting Started](https://eclipse-tractusx.github.io/docs/getting-started/)·[E2E](https://eclipse-tractusx.github.io/docs/tutorials/e2e/) | 공식 | 역할·실습 | 정상 |
| [Cofinity-X](https://www.cofinity-x.com/) | 운영사 | 마켓 45+ 앱, 2028 연장 | 정상 |
| [BMW](https://www.bmwgroup.com/en/news/general/2023/catenax.html)·[SAP](https://news.sap.com/2021/03/catena-x-automotive-alliance-picks-up-speed/)·[Telekom](https://www.telekom.com/en/media/media-information/archive/cofinity-x-open-marketplace-for-catena-x-1025336)·[DENSO](https://www.denso.com/global/en/news/newsroom/2025/20250324-g01/)·[NTT DATA](https://www.nttdata.com/global/en/news/press-release/2025/april/042200)·[IPA](https://www.ipa.go.jp/en/pressrelease/press20250331.html)·[GEC](https://gec.io/en/news/news-detail/catena-x-meets-factory-x-gec-and-cofinity-x-realize-a-showcase-for-interoperable-data-exchange-193/) | 회원사·기관 발표 | 개별 사건 | 정상 |
| [diginomica](https://diginomica.com/inside-catena-x-automotive-industry-consortium-biggest-story-sap-isnt-talking-about-yet) | 제3자 언론(2021) | 비판적 검증 | 정상 |
| [ARENA2036](https://arena2036.de/en/reader/sixth-eclipse-tractus-x-community-days/) | 커뮤니티 | 6차 Community Days | 정상 |
| SAP 팟캐스트 [The Open Source Way](https://podcast.opensap.info/open-source-way/2025/04/16/catena-x-tractus-x/) (2025-04-16) | 공식 팟캐스트 | Tractus-X 에피소드 | 리다이렉트, 상세 미청취 |

---

## H. 미확인·불일치 사항

| 항목 | 상태 |
|---|---|
| YouTube 영상 업로드일·조회수 | 출처 미확인 (API 차단) |
| BMWK 지원 정확 금액·기간 | "1억 유로+, 2021-08~2024-07"은 2차 출처 — BMWK 원문 미확인 |
| 협회 설립일 | 공식 5/15 vs 일부 소스 5/7 — 공식 우선 채택 |
| Tractus-X 명칭 유래 | 공식 설명 미발견 (Tractus = 라틴어 추정) |
| 팟캐스트 출연자·내용 | 미청취 |
| 회원사 수 "약 170" | 명단 PDF 자체 집계(±10 오차 가능) |

## I. 다음 조사 후보
- [ ] Catena-X 표준 라이브러리(CX-번호 표준 원문)
- [ ] TRG 원문 정독 (품질 기준)
- [ ] MIW → Identity Hub 전환 기술 배경
- [ ] 6차 Community Days(2026-07-02~03) 발표자료·후기 (직후 시점 — 자료 공개 대기)
- [ ] 한국 기업 참여 심층 (INTERX·Taelim 활동 내용, 배터리 3사 대응 동향)
- [ ] Ouranos Ecosystem 구조
- [ ] 24.05/24.08 breaking change 기술 상세
- [ ] Cofinity-X 마켓 앱 45개 목록
- [ ] docs-kits 개별 KIT 문서(25.12 버전) 심층
