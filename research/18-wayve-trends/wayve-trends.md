# Wayve 최근 12개월 동향 — 라이선스형 End-to-End 자율주행의 상용화 전환기

> **작성일**: 2026-10-30
> **조사 범위**: Wayve(영국 런던, 2017년 창업)의 2025-11-01 ~ 2026-10-30 동향. 창업~2025년 계보는 배경으로 압축. 사업·자금·파트너십 / 기술·연구 / 제품·배포·규제 / 경쟁 지형·시사점의 4축으로 정리.
> **출처 표기 원칙**: 모든 사실 문장·표 행에 출처를 병기하고, 말미 번호 목록에 URL을 수록. 등급 — 🔍 공식(기업·정부 1차 자료) · 📄 논문·기술 블로그 · 📰 언론·서드파티. 단일 약한 출처(주식 필러·집계 사이트·커뮤니티)에만 의존하는 항목과 미검증 보도는 본문에서 제외했다(8장 참조). "발표·계획(MoU)"과 "실제 운영·체결"은 구분해 표기한다.

---

## 0. 세 줄 요약

1. **자본과 고객이 동시에 확보됐다.** 2026-02 Series D $1.2B(post-money $8.6B)에 Mercedes-Benz·Nissan·Stellantis가 OEM으로는 처음 직접 투자했고, 같은 세 회사가 각각 FY2027(일본)·2028(북미)·"2년 내"(글로벌) 양산 적용을 약속하는 계약을 체결했다(🔍 Wayve 보도자료 2026-02-24 [18]; 🔍 Nissan 2025-12-10 [34]; 🔍 Stellantis 2026-05-21 [46]; 🔍 Wayve 2026-09-22 [55]).
2. **첫 유료 서비스는 시작됐지만 "무인"은 아니다.** 2026-09-03 런던에서 Uber 앱으로 호출되는 감독형(안전 운전자 탑승) 서비스가 TfL의 일반 PHV 면허(최대 15대, 1년)로 개시됐고, Automated Vehicles Act 2024상 무인 여객 서비스(APS) 허가는 2026-10 말까지 어떤 사업자에게도 발급되지 않았다(🔍 Wayve 2026-08-05 [83]; 📰 Reuters 2026-09-03 [92]; 📰 Automotive World 2026-09 [96]).
3. **경쟁의 축은 "같은 칩 위의 모델 경쟁"으로 이동했다.** Nissan 로보택시와 프랑스 L4 프로젝트는 NVIDIA Hyperion 위에 Wayve 모델을, Mercedes CLA는 같은 NVIDIA 컴퓨트 위에 NVIDIA 자체 Alpamayo 스택을 올리며, Mercedes는 두 공급사와 모두 계약을 유지한다(🔍 NVIDIA 2026-03-16 [41]; 📰 Electrek 2026-01-05 [122]; 🔍 Mercedes-Benz 2026-10-16 [59]).

---

## 1. Wayve는 어떤 회사인가 — 창업 이후 계보

Wayve는 2017년 영국 케임브리지에서 Alex Kendall과 Amar Shah가 창업한 end-to-end 학습 기반 자율주행 소프트웨어 기업으로, 차량을 만들거나 로보택시를 직접 운영하지 않고 OEM·모빌리티 플랫폼에 "Wayve AI Driver"를 라이선스한다(🔍 Companies House [1]; 🔍 Wayve 보도자료 2026-02-24 [18]). 현재 CEO는 공동창업자 Alex Kendall이며, 2024년 이후 미국·독일·일본에 거점을 열고 Nissan·Uber와 첫 상업 파트너십을 발표하면서 연구 기업에서 공급사로 전환했다(🔍 Wayve [5][6][7]; 🔍 Nissan 2025-04-10 [8]; 📰 BusinessWire 2025-06-10 [9]).

| 시기 | 사건 | 출처 |
|---|---|---|
| 2017-08 | 케임브리지에서 창업, Wayve Technologies Ltd 등기(회사번호 10924127) | 🔍 [1] |
| 2019-11 | Series A $20M, Eclipse Ventures 주도 | 📰 [2] |
| 2022-01 | Series B $200M, Eclipse 주도(D1 Capital 등 참여) | 📰 [3] |
| 2024-05 | Series C $1.05B, SoftBank Group 주도, NVIDIA·Microsoft 참여 | 🔍 [4] |
| 2024-10 ~ 2025-04 | Sunnyvale(미국)·Stuttgart 권역(독일)·Yokohama(일본) 테스트·개발 거점 개설 | 🔍 [5][6][7] |
| 2025-04 ~ 06 | Nissan 첫 글로벌 OEM 파트너 발표(차세대 ProPILOT), Uber와 런던 L4 시범 파트너십 발표 | 🔍 [8]; 📰 [9] |
| 2025-09 | Gen 3 차량 플랫폼(NVIDIA DRIVE AGX Thor) 발표, NVIDIA $500M 투자 검토 LOI | 📄 [11]; 🔍 [12]; 📰 [13] |

**모델 계보**(공개 발표 기준)

| 모델 | 시기 | 한 줄 | 출처 |
|---|---|---|---|
| LINGO-1 | 2023-09 | 주행 장면을 자연어로 설명·질의응답하는 비전-언어 모델 | 📰 [14] |
| GAIA-1 | 2023-10 | 비디오·텍스트·행동 조건 생성형 세계모델(9B 파라미터) | 📰 [15] |
| LINGO-2 | 2024-04 | 공공도로에서 테스트된 closed-loop vision-language-action 주행 모델(Wayve 표현) | 🔍 [16] |
| GAIA-2 | 2025-03 | 잠재 확산 기반 멀티뷰 세계모델, 최대 5카메라 동시 생성(arXiv 2503.20523) | 📄 [17] |
| GAIA-3 | 2025-12 | 15B 파라미터, 오프라인 평가·안전 검증용 세계모델 | 📄 [67]; 🔍 [68] |
| LA-Pose | 2026-04 | 무라벨 주행 영상 1,020만 클립으로 사전학습한 자가지도 포즈 추정(CVPR 2026) | 📄 [71][72] |
| GAIA-4 | 2026-08 | AI Driver를 루프 안에 넣은 폐루프 시뮬레이션용 멀티모달 세계모델 | 📄 [70] |

---

## 2. 최근 12개월 타임라인 (2025-11 ~ 2026-10)

| 날짜 | 사건 | 구분 | 출처 |
|---|---|---|---|
| 2025-12-02 | GAIA-3 공개(15B latent diffusion 세계모델, 오프라인 평가 목적) | 기술 | [67][68] |
| 2025-12-06 | NeurIPS 2025 "Embodied World Models" 워크숍 산업 데모(Corrado·Bertoni) | 기술 | [78] |
| 2025-12-10 | Nissan–Wayve 차세대 ProPILOT 확정 계약(definitive agreements), 첫 모델 FY2027 일본 | 사업 | [34][35] |
| 2025-12-15 | 영국 AV Act 2024 Commencement No.1 규정 제정(2026-01-01 일부 시행) | 규제 | [101] |
| 2025-12 | AI-500 로드쇼 완료: 6~12월 90→500개 도시, AI Driver 작동 1.45M km | 기술 | [76][77] |
| 2026-02-24 | Series D $1.2B(post $8.6B), 리드 Eclipse·Balderton·SoftBank Vision Fund 2; Mercedes·Nissan·Stellantis 첫 OEM 투자 | 사업 | [18][19][23] |
| 2026-03-10 | Qualcomm Snapdragon Ride + Active Safety 스택과 AI Driver 사전 통합 발표 | 기술 | [60][61] |
| 2026-03-12 | Wayve·Uber·Nissan 도쿄 로보택시 MoU(2026년 말 파일럿 목표, 안전 운전자 탑승) — 발표 | 배포 | [37][38] |
| 2026-03-16 | GTC 2026에서 Nissan LEAF 로보택시 프로토타입 공개(듀얼 DRIVE AGX Thor, Hyperion) | 기술 | [39][40][41] |
| 2026-04 | LA-Pose arXiv 2604.27448 공개 | 기술 | [71] |
| 2026-04-15 | Series D 연장 $60M — AMD, Arm, Qualcomm Ventures | 사업 | [25][26][27] |
| 2026-04-20 | AV Act Commencement No.2(SI 2026/437): Part 5 APS 허가제 2026-05-15 발효 | 규제 | [102] |
| 2026-04-23 | 영국 정부, APS 허가제 협의 응답 및 규정 의회 제출 | 규제 | [103] |
| 2026-05-21 | Stellantis–Wayve 파트너십: STLA AutoDrive에 AI Driver 통합, L2++ 핸즈프리, 북미 2028 첫 양산 | 사업 | [46][47][48] |
| 2026-05-29 | Wayve Labs 출범 선언("Building Intelligence That Can Act in the World") | 기술 | [74][75] |
| 2026-06-03 / 06-07 | CVPR 2026 WAD에서 Kendall 초청강연, LA-Pose 포스터 발표 | 기술 | [79][73] |
| 2026-06-17 | Stellantis·Wayve·Uber L4 로보택시 글로벌 전개 MoU(비구속) — 발표 | 사업 | [49][50] |
| 2026-06 | Uber·Wayve 런던 로보택시 대기자 명단(interest list) 개설 | 배포 | [89] |
| 2026-06-30 | $85M 직원 테더오퍼, 밸류에이션 $8.5B, 인력 약 1,200명 | 사업 | [28][29][30] |
| 2026-07-01 | AV Act Commencement No.3(SI 2026/731): Part 4 마케팅 규제 2027-01-07 시행 | 규제 | [104] |
| 2026-08-03 | GAIA-4 공개(AI Driver in-the-loop 폐루프 시뮬레이션, 반응형 에이전트, 합성 레이더) | 기술 | [70] |
| 2026-08-05 | TfL, Wayve 개조 Ford Mustang Mach-E 최대 15대에 PHV 면허(1년, 안전 운전자 필수) | 규제 | [83][84][85] |
| 2026-08-13 | Uber Japan, 도쿄 택시회사 Hinomaru Kotsu와 파일럿 운영 파트너십 | 배포 | [42][43] |
| 2026-09-03 | **런던 Uber–Wayve 승객 탑승 서비스 실제 개시**(감독형, 표준 요금) | 배포 | [90][91][92] |
| 2026-09-16 | 전 Waymo CFO Elisa de Martel, CFO 선임(Max Warburton은 전략 자문으로) | 사업 | [31][32] |
| 2026-09-22 | Mercedes-Benz–Wayve 양산 확정 계약(2년 내 도심 point-to-point 주행보조, MB.OS 통합) | 사업 | [55][56] |
| 2026-10-01 | Valeo, Nissan 차세대 ProPILOT 시스템 Tier-1 선정 — 주행 지능은 Wayve AI Driver | 사업 | [44][45] |
| 2026-10-07~09 | Wave by Vento(토리노): Fiat 500e·Maserati Grecale 개발차 L2++ 핸즈프리 시승 | 배포 | [51][52] |
| 2026-10-12 | 런던의회 교통위원회, TfL에 AV 대수 상한·허가 철회 권한 요구 보고서 발간 | 규제 | [99] |
| 2026-10-17 | ADCU(앱 운전자·배달원 노조), Wayve 런던 본사 앞 로보택시 반대 시위 | 배포 | [97][98] |
| 2026-10-23 | Wayve·Stellantis·NVIDIA, 프랑스 정부와 AV 배포 협력 발표(파리 Assises du Véhicule Autonome) | 사업·규제 | [63][64][65] |

---

## 3. 사업·자금·파트너십

### 3.1 Series D와 자본 구조

2026-02-24 발표된 Series D는 Wayve 역사상 최대 라운드로, 지분 라운드 $1.2B에 Uber의 마일스톤 연동 추가 자본을 합쳐 "총 $1.5B 확보"로 공식 표현됐다(🔍 Wayve 보도자료 2026-02-24 [18]; 📰 CNBC 2026-02-24 [19]). Uber의 추가 투자는 로보택시 배치 진전에 연동된 조건부 자본으로 최대 $300M이며, 따라서 $1.5B는 확정 입금액이 아니다(📰 Reuters 2026-02-24 [21]). 2개월 뒤 반도체 3사가 $60M을 연장 라운드로 추가했고, 6월 말에는 직원 유동화를 위한 $85M 테더오퍼가 $8.5B 밸류에이션으로 진행됐다(🔍 Wayve 2026-04-15 [25]; 📰 TechCrunch 2026-06-30 [28]).

| 항목 | 내용 | 출처 |
|---|---|---|
| 규모·밸류에이션 | $1.2B, post-money $8.6B | 🔍 [18]; 📰 [19][20] |
| 공동 리드 | Eclipse, Balderton, SoftBank Vision Fund 2 | 📰 Weil [23]; 📰 electrive [22] |
| 기존 투자자 참여 | Microsoft, NVIDIA, Uber | 📰 [20][22] |
| OEM 첫 직접 투자 | Mercedes-Benz, Nissan, Stellantis(금액 비공개) | 📰 [20][24] |
| 기타 참여 | Ontario Teachers' Pension Plan, Baillie Gifford, British Business Bank 등 | 📰 [24]; 🔍 OTPP [133] |
| Uber 조건부 자본 | 최대 $300M, 로보택시 배치 마일스톤 연동 → 합산 "$1.5B secured" | 📰 Reuters [21]; 🔍 [18] |
| Series D 연장(2026-04-15) | $60M, AMD·Arm·Qualcomm Ventures; 각사 하드웨어에서 AI Driver 구동 협력 | 🔍 [25]; 📰 [26][27] |
| 테더오퍼(2026-06-30) | 약 $85M 직원 주식 매각, 밸류에이션 $8.5B, 2024년 이후 두 번째 유동화 | 📰 [28][29]; 🔍 [30] |
| 공개 라운드 합산 | A $20M + B $200M + C $1.05B + D $1.2B + 연장 $60M ≈ $2.5B(Uber 조건부 제외) | 📰 [2][3]; 🔍 [4][18][25] |

Kendall은 Series D 발표 당시 2024년 Series C $1.05B의 "대부분(vast majority)"이 아직 남아 있다고 말했다(📰 Reuters 2026-02-24 [21]). NVIDIA의 2025-09 $500M 투자 검토 LOI가 Series D에서 어떤 금액으로 집행됐는지는 공개되지 않았다(🔍 Wayve 2025-09-19 [12]; 📰 TechCrunch 2025-09-19 [13]).

### 3.2 OEM 양산 계약 3건 — 체결된 것과 공개되지 않은 것

12개월 동안 Wayve는 Nissan·Stellantis·Mercedes-Benz와 각각 양산 적용을 전제로 한 계약을 체결했다. 세 건 모두 적용 차종·금액·물량은 비공개이며, 양산 시점만 공개됐다.

| OEM | 체결일·성격 | 제품 범위 | 양산 시점(공식) | 하드웨어·통합 | 비공개 사항 | 출처 |
|---|---|---|---|---|---|---|
| Nissan | 2025-12-10 확정 계약(definitive agreements) | 차세대 ProPILOT, 운전자 감독형 L2(Nissan 명시) | 첫 모델 FY2027(2027-04~2028-03) 일본, 이후 북미 등 글로벌 | Nissan "Ground Truth Perception"(차세대 LiDAR) + Wayve AI Driver; 프로토타입 센서 카메라 11·레이더 5·LiDAR 1; Tier-1은 Valeo(2026-10-01) | 차종명, 양산 ECU, 물량 | 🔍 [33][34][35]; 📰 [36]; 🔍 Valeo [44] |
| Stellantis | 2026-05-21 전략적 기술 파트너십 | STLA AutoDrive에 AI Driver 통합, 고속도로·도심 핸즈프리 감독형 "Level 2++"(door-to-door) | 북미 2028 첫 양산 | 개발차 Jeep Grand Cherokee(5월), Fiat 500e·Maserati Grecale(10월); 통합→도로 시험 4주 미만(Stellantis) | 브랜드·차종, 금액 | 🔍 [46][47][51]; 📰 [48] |
| Mercedes-Benz | 2026-09-22 양산 확정 계약(definitive production agreement) | 도심·고속 point-to-point 주행보조(운전자 개입 준비 필요) | "향후 2년 내" 고객 제공, 글로벌 시장 | Mercedes 자체 하드웨어·MB.OS·지도 인터페이스에 통합 완료(Wayve 주장) | 차종, SAE 레벨, 금액 | 🔍 [55]; 📰 [56][57] |

Nissan은 자사를 "광범위한 차량 세그먼트에 Wayve AI 시스템을 대규모로 배포하기로 약속한 첫 자동차 제조사"로 표현했다(🔍 Nissan 2025-12-10 [34]). Reuters는 2026-07 Nissan 기술 책임자 Eiichi Akashi를 인용해 첫 적용 차량이 일본 시장 Elgrand 밴(2028-03 종료 회계연도 내)이라고 보도했으나, Nissan 공식 자료에는 차종이 명시되지 않았다(📰 Reuters 2026-07-01 [107]; 🔍 [34]). Mercedes CTO Jörg Burzer는 이 계약을 "프리미엄 세그먼트 최초의 Wayve AI Driver 통합"이라 했고, 3주 뒤 Mercedes는 NVIDIA와의 자동화 주행 파트너십도 확장 발표해 두 공급사를 병행하고 있음을 보여줬다(🔍 Wayve 2026-09-22 [55]; 📰 City A.M. [58]; 🔍 Mercedes-Benz 2026-10-16 [59]).

### 3.3 Uber — 투자자이자 유통 채널

Uber는 Series D 참여 투자자이면서 조건부 $300M을 약정했고, Wayve의 로보택시는 모두 Uber 네트워크를 통해 전개된다(📰 Reuters [21]; 🔍 Wayve [18]). Series D 당시 Kendall은 2026년 중 Uber와 전 세계 10개 도시에 로보택시를 배치할 계획이라 밝혔지만 도시명은 공개하지 않았고, 2026-10 말까지 공식 발표된 도시는 런던(운영 중)과 도쿄(파일럿 준비)뿐이다(📰 Reuters 2026-02-24 [21]; 🔍 Uber IR 2026-03-12 [37]). 로보택시 모델은 OEM이 L4 대응 차량을 만들고, Wayve가 AI Driver를 탑재하고, Uber가 플릿을 소유·운영하는 구조로, Nissan(도쿄)과 Stellantis(글로벌 MoU) 두 건이 같은 3자 구조로 발표됐다(🔍 Wayve 2026-02-24 [18]; 🔍 Uber IR [37]; 🔍 Stellantis 2026-06-17 [49]). Stellantis 3자 MoU는 비구속(non-binding)이며 차종·시장·일정은 미정이다(🔍 Stellantis [49]; 🔍 Wayve [50]).

### 3.4 Tier-1 — Valeo의 Nissan ProPILOT 시스템 통합 선정

2026-10-01 Valeo는 Nissan 차세대 ProPILOT 프로그램의 시스템 Tier-1(리드 시스템 통합자)로 선정됐다고 발표했다. Valeo가 센서, ADAS 도메인 컨트롤러(중앙집중형 연산), 하드웨어·소프트웨어 플랫폼을 공급·통합하고, Wayve AI Driver가 그 안에서 주행 의사결정을 담당한다(🔍 Valeo 2026-10-01 [44]; 📰 just-auto [45]). 적용 차종과 출시 시점은 Valeo 보도자료에 명시되지 않았다(🔍 [44]).

### 3.5 경영진·인력·거점

- 2026-09-16 전 Alphabet Waymo CFO(2022-09~2026-01) Elisa de Martel을 CFO로 선임. Sunnyvale에서 글로벌 재무 조직을 총괄하며 Kendall에게 직보하고, 2024-11 합류한 전임 CFO Max Warburton은 전략 자문 역할로 이동(📰 TechCrunch 2026-09-16 [31]; 📰 CFO Dive [32]).
- 인력은 2025-07 약 650명에서 2026-06 약 1,200명으로 1년 만에 2배 이상 증가했으며, Wayve는 "6개국 3대륙 오피스"와 미국 채용 확대를 밝혔다(📰 Tech.eu 2025-07-28 [10]; 🔍 Wayve 블로그 2026-06-30 [30]).
- 조사 기간 중 새 오피스 개설 공식 발표는 확인되지 않았고, 지리적 확장은 런던 상용 서비스·도쿄 파일럿 준비·토리노 시연 형태로 나타났다(🔍 [90]; 🔍 [37]; 🔍 [51]).

### 3.6 재무 공시 — 확인된 사실만

Companies House에 제출된 최신 계정(FY 2024-08-31)은 세전손실 £62m(전년 약 £41m)이며 R&D 단계로 실질 매출이 없다고 보도됐다(📰 Tech.eu 2025-07-28 [10]; 🔍 Companies House [1]). Wayve는 매출·수주잔고·계약 금액·현금 소진율을 공개하지 않으며, 3건의 OEM 계약 보도자료 모두 재무 조건을 비공개로 명시했다(🔍 [35][46][55]). 라이선스 매출이 발생하는 양산 시점은 FY2027(Nissan)이 가장 이르다(🔍 Nissan [34]).

---

## 4. 기술·연구

### 4.1 AV2.0 접근 — 맵리스·end-to-end·센서 비종속

Wayve는 HD맵·지오펜스·도시별 재학습 없이 센서 입력에서 주행 행동까지 하나의 학습 모델로 연결하는 접근을 취하며, Mercedes 계약 발표 시에도 이 점을 재확인했다(📰 Electrek 2026-09-22 [56]). Kendall은 소프트웨어가 "OEM 파트너가 이미 차량에 보유한 GPU"에서 구동될 수 있다고 말했고, Wayve 제품 페이지는 "유연하고 센서 비종속적인 하드웨어 스택" 호환을 내세운다(📰 TechCrunch 2026-02-24 [20]; 🔍 Wayve 제품 페이지 [82]). 센서 철학에 대해 Kendall은 2026-09 Axios에 Wayve AI가 카메라·레이더·LiDAR와 함께 작동하도록 설계됐으며 "맵리스 일반화와 다중 센서 안전"을 "best of both worlds"라고 표현해, 카메라 전용 노선(Tesla)과 구분했다(📰 Axios 2026-09-16 [80]). 실제로 Nissan 양산 ProPILOT은 Nissan의 차세대 LiDAR와 Wayve AI Driver를 결합한다(🔍 Nissan 2025-09-22 [33]; 🔍 Nissan 2025-12-10 [34]).

### 4.2 GAIA-3·GAIA-4 — 세계모델을 "검증 인프라"로

| 항목 | GAIA-3 (2025-12-02) | GAIA-4 (2026-08-03) |
|---|---|---|
| 규모·구조 | 15B 파라미터 latent diffusion; GAIA-2 대비 모델 2배·비디오 토크나이저 2배·학습 데이터 10배 | 파라미터 수 미공개; 멀티모달(카메라 + 합성 레이더) |
| 목적 | "확장 가능·현실적·제어 가능한 오프라인 평가" | AI Driver를 루프 안에 넣은 폐루프 시뮬레이션 — "scene generation에서 end-to-end 안전 측정으로" |
| 제어 방식 | ego 행동 조건화 + "World-on-Rails" 교란으로 실주행 클립의 통제된 변형 생성 | world-on-rails(타 도로사용자 녹화 궤적 유지) vs reactive agents(ego에 반응; 공개 예시는 선행차만 반응) |
| 평가 모드 | 안전 임계 시나리오 생성, embodiment transfer(차량 구성 간 평가), 통제된 시각 다양성 | 반사실 테스트(안전요원이 개입하지 않았다면, 양보 대신 진행했다면) |
| 주장(Wayve) | 합성 개입과 실도로 실험 간 상관 연구가 "상대적 정책 성능을 신뢰성 있게 예측"함을 시사 | 고속도로 장면을 카메라만→카메라+레이더로 폐루프 실행 시 궤적 변화·적절한 감속 발생 → 레이더가 의사결정에 유효 |
| 외부 연계 | DriveSafeSim: 영국 정부 그랜트, Warwick Manufacturing Group과 생성형 세계모델의 공식 안전평가 활용 검증 | "검증은 도로 마일이 아니라 컴퓨트로 스케일한다"는 "Simulation 2.0" 프레임 |
| 출처 | 📄 [67]; 🔍 [68]; 📰 [69] | 📄 [70] |

GAIA 계보는 GAIA-1(생성 데모) → GAIA-2(제어 가능 멀티뷰) → GAIA-3(평가 도구) → GAIA-4(정책 in-the-loop)로, 용도가 데이터 생성에서 안전 검증 인프라로 이동했다(📰 [15]; 📄 [17][67][70]). GAIA-3·4는 arXiv 논문 없이 블로그·보도자료 형식으로 공개됐고, 모델 가중치·코드는 공개되지 않았다(📄 [67][70]). 상관 연구의 방법론·표본 수와 GAIA-4의 해상도·카메라 수·실시간성 수치는 공개되지 않았으며, 모든 성능 주장은 Wayve 자체 주장이고 독립 검증은 확인되지 않았다(📄 [67][70]).

### 4.3 LA-Pose — 기간 내 유일한 정식 논문

LA-Pose(arXiv 2604.27448, CVPR 2026 포스터 2026-06-07)는 Genie 스타일 inverse-dynamics 모델을 무라벨 주행 비디오로 사전학습해 연속 프레임 쌍마다 "latent action"을 산출한 뒤, 경량 pose head를 붙여 라벨 3D 데이터로 후학습하는 2단계 방식이다(📄 arXiv [71]; 📄 Wayve 블로그 2026-05-05 [72]). 내부 무라벨 주행 스니펫 1,020만 개로 사전학습하고 Waymo·nuScenes·Argoverse로 pose를 학습했으며, Waymo held-out AUC@5 91.4%(vs VGGT 74.8%), PandaSet 86.3%(vs 75.0%)를 보고했다(📄 [72]; 📄 CVPR [73]). 50차원 latent bottleneck이 1,536차원보다 downstream pose에 유리했고, 후진(reversing) 모션에서 성능이 저하된다는 한계를 Wayve가 명시했다(📄 [72]). 조사 기간 중 Wayve 소속 저자의 다른 arXiv 논문은 검색 범위에서 확인되지 않았다.

### 4.4 Wayve Labs와 학회 활동

2026-05-29 Wayve는 Chief Scientist Jamie Shotton이 이끄는 프런티어 연구 조직 "Wayve Labs"를 출범하고, 연구 영역을 world models·vision-language-action·robot learning·cross-embodiment로, 핵심 열린 문제를 cross-embodiment transfer로 제시했다(📄 Wayve 블로그 2026-05-29 [74]; 🔍 Wayve Labs [75]). 학회 노출은 논문보다 초청강연·산업 데모 중심이었다: NeurIPS 2025 Embodied World Models 워크숍 산업 데모 "Scaling World Models to Power Evaluation and Validation"(2025-12-06), CVPR 2026 Workshop on Autonomous Driving의 Kendall 초청강연 "Frontier Challenges in Bringing AI to 1B Robots"(2026-06-03), LA-Pose 본회의 포스터(📄 [78][79][73]). LINGO 계열의 새 모델 발표는 기간 내 확인되지 않았고, Labs 페이지의 최신 LINGO 항목은 2024-04 LINGO-2다(🔍 [16]).

### 4.5 데이터 플라이휠 — 공개된 수치

| 지표 | 수치 | 출처 |
|---|---|---|
| AI-500 로드쇼(2025-06~12) | 단일 파운데이션 모델, 재학습·HD맵 없이 90개 도시(90일) → 500개 도시; AI Driver 작동 1.45M km | 📄 [76][77] |
| 도시별 사전 데이터 | 219개 도시 사전 로컬 데이터 없음(zero-shot), 260개 도시 10 km 미만, 81개 도시 100 km 미만; Wayve는 "상당 부분의 도시에서 신뢰성 있는 zero-shot 동작"으로 표현 | 📄 [76] |
| OEM 플랫폼 이식 속도 | Stellantis 프로토타입 2개월 미만(Kendall, 5월); Fiat 500e·Maserati Grecale 통합→도로 시험 4주 미만(Stellantis, 10월) | 📰 [48]; 🔍 [51] |
| 학습 인프라 | Microsoft Azure(Storage·Databricks·AKS로 수천 GPU 연결), 2025-10 Strategic Framework Agreement로 확대 | 🔍 Microsoft [81] |
| 미공개 | 총 플릿 대수, 누적 주행 시간·PB, OEM 플릿으로부터의 데이터 환류, 로드쇼 개입 횟수 | — |

### 4.6 컴퓨트 플랫폼 — 실리콘 포트폴리오 확대

| 플랫폼 | 용도·구성 | 상태(2026-10) | 출처 |
|---|---|---|---|
| NVIDIA DRIVE Orin | 개발 플릿(런던 Mach-E 포함) | 실도로 운행 중 | 📰 [20] |
| NVIDIA DRIVE AGX Thor(Gen 3) | L3 eyes-off·L4 driverless 겨냥 차량 플랫폼, DriveOS·Halos | 2025-09 발표 | 📄 [11] |
| NVIDIA Hyperion + 듀얼 Thor | Nissan LEAF 로보택시 프로토타입: 360° 카메라, 서라운드·전방 이미징 레이더, 전방 LiDAR, DriveOS, Halos, 완전 이중화(Nissan 개발 중) | 프로토타입(도쿄 파일럿 기준 차량) | 🔍 [39][40]; 📰 [132] |
| NVIDIA Hyperion + Halos | 프랑스 L4 프로젝트(Stellantis L4-Ready 차량) | 2026-10-23 발표 | 🔍 [63][64] |
| Qualcomm Snapdragon Ride + Active Safety | 사전 통합 "production-ready" ADAS/AD 패키지, entry hands-off~eyes-off, Ride Elite~메인스트림 | 2026-03-10 발표 | 🔍 [60]; 📰 [61][62] |
| AMD·Arm | Series D 연장 투자와 함께 각사 플랫폼 하드웨어 통합 협력 | 2026-04-15 발표 | 🔍 [25]; 📰 [27] |
| Mercedes 자체 하드웨어 + MB.OS | 양산 아키텍처에 AI Driver 통합 완료(Wayve 주장) | 계약 체결, 2년 내 양산 | 🔍 [55]; 📰 [56] |
| Valeo ADAS 도메인 컨트롤러(Nissan) | 센서·중앙집중형 연산·플랫폼 통합, AI는 Wayve | 2026-10-01 발표 | 🔍 [44] |

AI Driver의 **모델 파라미터 수, 추론 지연시간, 프레임레이트, 최소 TOPS·메모리 요구치는 어떤 공개 자료에도 없다**. Nissan·Stellantis·Mercedes 양산 ECU의 구체 SoC도 공개되지 않았으며, 2026-10 기준 실도로에서 돌고 있는 것은 Orin(런던)과 Thor(도쿄 프로토타입)뿐이다(📰 [20]; 🔍 [39]).

---

## 5. 제품·배포·규제

### 5.1 AI Driver 제품 라인업

Wayve 제품 페이지는 단일 플랫폼을 3단계로 구분한다(🔍 Wayve 제품 페이지 [82]).

| 티어 | 레벨 | 설명 | 적용 사례(2026-10) | 출처 |
|---|---|---|---|---|
| AI Driver Assist | L2(hands-free, eyes-on) | 핸즈프리 주행보조 | Nissan ProPILOT(FY2027, L2), Stellantis "L2++"(2028), Mercedes point-to-point(2년 내) | 🔍 [82]; 📰 [36]; 🔍 [46][55] |
| AI Driver CoPilot | L3 | eyes-off 주행 | 공개된 OEM·일정 없음 | 🔍 [82] |
| AI Driver | L4(도심 eyes-off) | 무인 운행 | 런던 Uber(감독형 운행), 도쿄 LEAF(프로토타입), Stellantis L4-Ready(MoU) | 🔍 [82][90][39][49] |

Series D 보도자료는 "2027년부터 구매자가 L2+ hands-off 기능의 Wayve AI Driver 탑재 승용차를 구매할 수 있다"고 명시했다(🔍 Wayve 2026-02-24 [18]). 2026-10 기준 소비자 판매 제품은 0건이며, 실도로에 있는 것은 런던의 감독형 개발차량과 OEM 프로토타입이다(🔍 [90]; 🔍 [51]).

### 5.2 런던 Uber 서비스 — 발표 vs 실제

| 단계 | 발표·계획 | 실제 | 출처 |
|---|---|---|---|
| 2025-06-10 | "2026년 봄 런던 L4 완전자율 시범" 발표; 영국 정부도 무인 파일럿을 2026년 봄으로 1년 앞당김 | — | 📰 [9]; 🔍 Hansard [100] |
| 2026-06 | Uber 앱 내 대기자 명단 개설, "수개월 내 출범" | 개설됨 | 📰 [89] |
| 2026-08-05 | — | TfL이 개조 Ford Mustang Mach-E 최대 15대에 **일반 PHV 면허**(자동차량 면허 아님) 부여, 1년 유효, 안전 운전자 필수, 운영자(Uber)·운전자·차량 "triple lock" 면허 | 🔍 [83][84]; 📰 [85][86] |
| 2026-09-03 | — | **승객 탑승 서비스 개시**: UberX·Comfort·Electric 호출 시 무작위 매칭(직접 선택 불가), 표준 요금, 공항 제외 런던 전역, 모든 차량에 TfL 면허 보유 안전 운전자 탑승 | 🔍 [90][91]; 📰 Reuters [92]; 📰 [93][94][95] |
| 무인화 | Uber는 2026년 무인 운행을 예고 | AV Act 2024상 APS 허가 필요; TfL은 2026-09 "어떤 운영자도 무감독 서비스 등록 첫 단계를 완료하지 않았다"고 밝힘; Wayve·Uber의 APS 신청 착수 보도 없음 | 📰 [87][88]; 📰 Automotive World [96] |

2025-06 발표 대비 약 5개월 늦은 2026-09에, "L4 시범"이 아닌 "안전 운전자가 있는 PHV 서비스" 형태로 개시된 셈이다(📰 [9]; 📰 [92]). 언론 시승에서 Bloomberg는 약 40분간 안전 운전자 개입 2회를, BBC는 1회를 보고했고, Kendall은 Guardian에 안전 운전자 제거 시점을 밝히지 않은 채 "가능한 한 빨리 추진 중"이라고 말했다(📰 Automotive World 2026-09 [96]). Uber는 14만 명 이상이 사전 등록했다고 밝혔으나, 탑승 건수·개입(disengagement) 데이터는 공개되지 않았다(📰 Tech.eu [93]; 📰 ITV [97]). 런던은 자그레브에 이어 Uber가 로보택시를 제공하는 두 번째 유럽 도시다(📰 Reuters [92]).

### 5.3 도쿄 파일럿 — 준비 중, 미개시

2026-03-12 3자 MoU는 Nissan LEAF 기반 차량을 Uber 앱으로 호출하는 도쿄 파일럿을 "2026년 말" 목표로, 초기엔 훈련된 안전 운전자가 탑승하고 "관계 당국과의 협의를 전제"로 한다고 명시했다(🔍 Uber IR [37]; 🔍 Nissan [38]). 기준 차량은 GTC 2026에서 공개된 L4 설계 프로토타입이며, Nissan은 파일럿 전까지 완전 이중화 시스템과 차내 디스플레이를 추가 개발 중이다(🔍 Nissan 2026-03-16 [40]). 2026-08-13 Uber Japan은 도쿄 택시회사 Hinomaru Kotsu를 운영 파트너로 선정했는데, 일본 법상 여객운송은 면허 택시사업자가 수행해야 하므로 Hinomaru가 차고·정비·충전과 초기 안전 운전자를 담당하고 Uber는 매칭 플랫폼 역할을 맡는다(📰 Nasdaq/RTTNews [42]; 📰 just-auto [43]). 2026-10-30 기준 파일럿 개시·차량 대수·일본 당국 허가에 대한 보도는 확인되지 않았다.

### 5.4 영국 Automated Vehicles Act 2024 시행 일정

| 일자 | 조치 | 의미 | 출처 |
|---|---|---|---|
| 2025-06-10 | DfT, 무인 택시·버스형 상업 파일럿을 2026년 봄으로 1년 조기화 | Part 5 APS 허가제 가속 | 🔍 Hansard [100] |
| 2025-12-15 | Commencement No.1(SI 2025/1339) 제정, 2026-01-01 일부 조항 시행 | 개조 범죄 등 | 🔍 [101] |
| 2026-04-20 | Commencement No.2(SI 2026/437) 제정 → Part 5 APS 허가제 2026-05-15 발효 | 무인 여객 서비스 허가의 법적 근거 | 🔍 [102] |
| 2026-04-23 | 정부 APS 협의 응답, Automated Vehicles (Permits for APS) Regulations 2026 의회 제출 | 허가 세부 규정 | 🔍 GOV.UK [103] |
| 2026-07-01 | Commencement No.3(SI 2026/731) 제정 → Part 4 마케팅 제한 2027-01-07 시행 | "self-driving" 용어 규제 | 🔍 [104] |
| 2027 하반기(목표) | ASDE 인가 체계 포함 전면 시행 | 상업 무인 운행의 완전한 틀 | 📰 Shoosmiths [105]; 📰 [106] |

법적 틀(APS 허가제)은 2026-05에 갖춰졌지만 2026-10 말까지 APS 허가 발급 사례는 보도되지 않았고, 런던 Wayve–Uber 서비스는 기존 PHV 법제로 운영되고 있다(🔍 [102]; 📰 [88][96]). 무인 전환에는 VCA·DVSA·TfL 다기관 평가가 필요하며 명확한 일정은 없다(📰 TNW [95]). 2026-10-12 런던의회 교통위원회는 "런던이 자율주행 승객 서비스를 환영해야 한다고 설득될 충분한 증거를 듣지 못했다"며, 2027년 전면 시행 시 TfL에 AV 대수 상한 설정·운영 허가 철회 권한을 주고 사고·준사고 정보를 24시간 내 제출하도록 정부에 요구했다(🔍 London Assembly 2026-10-12 [99]).

### 5.5 프랑스 — 정부 차원 협력 선언

2026-10-23 파리 Assises du Véhicule Autonome에서 Wayve·Stellantis·NVIDIA는 프랑스 정부와 함께 프랑스 내 AV 배포 가속 협력을 발표했다. Stellantis가 L4-Ready 플랫폼 차량·제조, Wayve가 AI Driver, NVIDIA가 Hyperion 컴퓨트·센서 아키텍처와 Halos를 담당한다(🔍 Wayve [63]; 🔍 Stellantis [64]). "Greater Paris Autonomous Driving Living Lab"을 EU ADACities에 제출해 2028년부터 first/last-mile 실증을 계획하고, 교통장관 Philippe Tabarot는 안전·데이터 요건을 유지하면서 2027년부터 관련 규칙을 개정하겠다고 밝혔다(📰 electrive 2026-10-26 [65]; 📰 TNW [66]). 차량 출시일·플릿 규모·도시는 미정이다(🔍 [63]).

### 5.6 안전 접근

- **검증 인프라**: GAIA-3(오프라인 평가)·GAIA-4(폐루프)를 안전 평가 도구로 제시하고, DriveSafeSim(영국 정부 그랜트, WMG 협력)으로 생성형 세계모델의 공식 안전평가 활용 가능성을 검증 중(📄 [67][70]; 📰 [69]).
- **차량 측 안전**: Nissan LEAF 로보택시 프로토타입은 NVIDIA Halos(기능안전·사이버보안 프레임워크)와 완전 이중화 시스템을 적용(🔍 Nissan [40]).
- **운영 측 안전**: 런던 모든 차량에 TfL 면허 보유 안전 운전자가 상시 탑승하며 법적 책임을 보유(📰 Reuters [92]; 🔍 [83]).
- **미공개·미확인**: 정기 안전 보고서, disengagement 데이터, ISO/UL 4600 등 인증 주장, 사고·리콜 보도 모두 확인되지 않음. 런던 운행이 PHV 틀이어서 AV Act상 ASDE 사고 보고 의무가 적용되지 않는다(🔍 [83]; 📰 [96]).

### 5.7 사회적 반응

TfL 면허 결정에 GMB 노조가 반대했고, 2026-10-17 ADCU(App Drivers and Couriers Union)는 King's Cross의 Wayve 본사 앞에서 약 20명 규모 시위를 열어 안전·일자리·혼잡 우려 제기, 대체 운전자 보상, 롤아웃 중단, 런던시장의 입장 표명을 요구했다(📰 Fleet News [85]; 📰 ITV 2026-10-17 [97]; 📰 Silicon UK [98]). Wayve는 "TfL과 함께 단계적으로 전개 중"이라고 답했다(📰 ITV [97]).

---

## 6. 경쟁 지형과 Wayve의 위치

### 6.1 비교표

| 회사 | 사업 모델 | 기술 접근 | 최근 12개월 OEM·플랫폼 거래 | 규모 지표(공개치) | 출처 |
|---|---|---|---|---|---|
| **Wayve**(영국) | OEM·모빌리티 플랫폼에 AI Driver 라이선스; 차량·플릿 운영 안 함 | End-to-end, 맵리스, 센서·칩 비종속(개발 플릿 Orin, Gen 3 Thor); 세계모델 연구 블로그 공개, 가중치 비공개 | Nissan 확정계약(FY2027), Stellantis(2028 북미), Stellantis·Uber MoU, Mercedes 양산계약(2년 내), Valeo 통합, 프랑스 정부 협력, Qualcomm 사전통합 | Series D $1.2B/$8.6B; 런던 감독형 서비스 1개 도시(최대 15대); 양산 매출 미발생 | 🔍 [18][34][46][55][44][60] |
| **Tesla**(미국) | 자사 차량 FSD 구독 + 자사 로보택시 운영(수직통합) | End-to-end, 카메라 전용, HD맵 미사용; 연구 비공개 | 외부 OEM FSD 라이선스 공개 사례 없음 | FSD 활성 구독 174만(Q3 2026), 무감독 누적 약 200만 마일, Cybercab 오스틴 운행 2026-09-03 개시, 텍사스·플로리다 도시에서 무감독 운행 | 🔍 Tesla 10-Q [113]; 📰 Electrek [114] |
| **Waymo**(미국) | 자사 로보택시 운영; 소프트웨어 라이선스 없음 | "Waymo Foundation Model": end-to-end 이점 + 독립 안전검증 레이어(하이브리드), 카메라+LiDAR+레이더; 연구 공개 | 운영자; 런던 운영 파트너 Moove | 주 50만 유료 승차·10개 도시(2026-03); 런던 공공도로 테스트 2026-04-14 개시(I-Pace 약 100대, 안전 운전자); 플릿 약 4,000대(2026-10 보도) | 📰 [110][111][112]; 📄 [108] |
| **Mobileye**(이스라엘/미국) | OEM에 칩+SW(SuperVision·Chauffeur·Drive) 공급; 로보택시는 VW 등 파트너 운영 | "Compound AI"(투명성 강조), EyeQ6H 4개로 ID.Buzz AD 구동 | VW SuperVision·Chauffeur 2027~2028 출시, Chauffeur ASP 약 $2,500(Q3 2026 콜) | Q3 2026 매출 $492M(-2% YoY); ID.Buzz AV 100대 이상 테스트(Q1 2026), ID.Buzz AD 프리시리즈 생산(2026-03), 양산 2027 | 🔍 [115][117]; 📰 [116]; 📄 [118]; 📰 [119] |
| **NVIDIA**(미국) | 컴퓨트(Orin/Thor)+레퍼런스(Hyperion)+오픈 모델(Alpamayo)+풀스택 DRIVE AV; **Wayve 투자자 겸 플랫폼 공급자** | Alpamayo 1: 10B 파라미터 오픈 추론 VLA, 가중치 공개; Halos 안전 프레임워크 | Mercedes CLA MB.DRIVE ASSIST PRO(L2+, Orin급 254 TOPS, 2026 Q1); Hyperion L4 채택 BYD·Geely·Isuzu·Nissan(Nissan은 Wayve SW); Mercedes 파트너십 확장(2026-10-16) | — | 📰 [120]; 📄 [121]; 📰 [122][123]; 🔍 [41][59] |
| **Momenta**(중국) | OEM ADAS 공급 + Mercedes·Uber와 로보택시 | 데이터 중심 학습(상세 비공개) | Mercedes S-Class 로보택시 아부다비(2025-12), Audi E7X L3(2026-05), 독일 KBA L4 전국 테스트 승인·Uber 지분 확대(2026-07-29), DSAT(Stellantis 계열) Peugeot·Jeep 글로벌 ADAS(2026-09-24) | — | 📰 [124][126][127]; 🔍 [125] |
| **Pony.ai / WeRide**(중국) | 자사 운영 + Uber 플랫폼 공급 | LiDAR 포함 멀티센서 L4 | Pony·Uber 유럽 2,000대+ 계약(2026-08-14), Uber·Pony 런던 진출 계획(2026-10-08); WeRide·Uber 중동·유럽 | Pony 로보택시 플릿 1,975대(2026-06-30); WeRide 글로벌 L4 플릿 약 3,400대(2026-07-31) | 🔍 [128][129][130]; 📰 [131] |

### 6.2 "같은 칩 위 모델 경쟁" 구조

NVIDIA는 Wayve의 Series D 참여 투자자이자 2018년부터의 개발 파트너이면서, 동시에 Mercedes CLA에 자사 DRIVE AV·Alpamayo 스택을 L2+로 양산 공급하는 경쟁 소프트웨어 공급자다(📰 TechCrunch 2026-02-24 [20]; 📰 Electrek 2026-01-05 [122]). GTC 2026 보도자료에서 NVIDIA는 Nissan의 L4 프로그램을 "Wayve 소프트웨어로 구동되며 Hyperion 기반"으로 명시했고, 프랑스 협력에서도 Wayve AI Driver는 Hyperion + Halos 위에서 구동된다(🔍 NVIDIA [41]; 🔍 Stellantis [64]). Mercedes는 CLA(NVIDIA 스택), 중국(Momenta), 글로벌 미래 차종(Wayve)의 세 공급원을 병행하며, Wayve 계약 3주 후 NVIDIA와의 파트너십 확장을 발표했다(📰 Electrek [56]; 📰 CnEVPost [124]; 🔍 Mercedes-Benz 2026-10-16 [59]). Stellantis도 북미(Wayve, STLA AutoDrive)와 DSAT 계열 Peugeot·Jeep(Momenta)로 복수 소싱한다(🔍 [46]; 📰 CnEVPost 2026-09-28 [127]). Wayve가 Qualcomm·AMD·Arm 투자를 유치하고 Snapdragon Ride 사전 통합을 발표한 것은 NVIDIA 외 실리콘으로의 확장 신호지만, 2026-10 기준 NVIDIA 외 칩에서의 실도로 배치 사례는 확인되지 않았다(🔍 [25][60]).

### 6.3 검증된 발언 — 기술 접근을 둘러싼 입장

- **Waymo(비판)**: 온보드 소프트웨어 VP Srikanth Thirumalai는 2026-08-26 블로그에서 "원시 픽셀을 받아 조향 명령을 직접 출력하는 순수 end-to-end 신경망 아키텍처는 블랙박스 실패 위험을 안고 있다"고 썼고, 카메라만으로는 부족하며 독립 검증 레이어와 폐루프 시뮬레이션이 필요하다고 주장했다(📄 Waymo 블로그 2026-08-26 [108]). 같은 날 Axios에 "순수 end-to-end 시스템은 우리가 운영하는 규모에서 안전 기준을 충족하지 못한다"고 말했다(📰 Axios 2026-08-26 [109]).
- **Nissan(고객의 유보)**: 기술 책임자 Eiichi Akashi는 Reuters에 Wayve 시스템을 "가장 진보했다"고 하면서도 "안을 들여다보고 어떻게 결정하는지 보기 어렵다"고 말하고, 배치 전 안전을 면밀히 평가 중이라고 밝혔다(📰 Reuters 2026-07-01 [107]).
- **Stellantis(구매 동기)**: CEO Antonio Filosa는 2026-10-09 토리노에서 Wayve 파트너십이 ADAS 개발 비용과 기간을 모두 줄일 수 있으며, Stellantis의 제조 규모가 핸즈프리를 저렴하게 만드는 보완 자산이라고 말했다(📰 Reuters 2026-10-09 [52]; 📰 Detroit News [53]).
- **Wayve(자기 규정)**: Kendall은 기술을 "사실상 어떤 자율주행 개발사에도" 라이선스할 수 있고 도로 매핑이나 현지 코드 작성이 필요 없어 신규 시장 진입이 빠르다고 주장했으며, 토리노에서는 이런 기술이 "안전벨트·AEB처럼 차량 필수 장비가 될 것"이고 1,000달러 미만 하드웨어로 대량 보급을 목표한다고 말했다(📰 Reuters [107]; 📰 TNW 2026-10-10 [54]).

### 6.4 위치 요약

운영자 모델(Waymo·Tesla·Pony·WeRide)이 유료 승차·플릿·무감독 마일을 축적하는 동안, Wayve의 공개 규모 지표는 런던 감독형 서비스 1개 도시에 그치고 라이선스 매출은 FY2027~2028 OEM 양산에 종속된다(📰 [110][113][129]; 🔍 [34][46][55]). 반면 Wayve는 12개월 안에 글로벌 OEM 3사와 양산 계약, Tier-1(Valeo) 통합, 2개 정부(영국·프랑스)와의 규제 트랙, Uber 유통 채널을 확보한 유일한 독립 end-to-end 라이선서이며, 유럽에서는 Uber가 Wayve·Pony.ai를 런던에, Waymo는 자체 운영으로 각각 진입하는 다자 경쟁이 형성됐다(🔍 [44][63]; 📰 TechCrunch 2026-10-08 [131]; 📰 [111]).

---

## 7. 시사점 — 차량용 HPC·Tier-1 관점

출처 있는 사실에서 직접 도출되는 것만 적는다.

1. **컴퓨트·안전 OS는 플랫폼화되고, 차별화는 주행 모델 레이어로 올라간다.** 근거: Nissan L4·프랑스 L4 프로젝트는 NVIDIA Hyperion + Halos 위에 Wayve 모델을, Mercedes CLA는 같은 NVIDIA 컴퓨트 위에 NVIDIA 자체 모델을 올리며, Mercedes·Stellantis는 복수 모델 공급사를 병행한다(🔍 [41][64][59]; 📰 [122][127]). HPC 공급사에게 "어떤 모델이 올라가든 돌아가는 컴퓨트·검증 레퍼런스"가 판매 단위가 되고 있다.
2. **단일 AI Driver의 멀티 실리콘 이식성이 OEM 선정 조건이 됐다.** 근거: Wayve는 Orin(런던)·듀얼 Thor(로보택시)·Snapdragon Ride(사전 통합)·AMD·Arm·Mercedes 자체 하드웨어로 통합 사례를 늘렸고, 반도체 3사는 투자와 함께 자사 플랫폼 구동 협력을 조건으로 걸었다(🔍 [25][60][55]; 📰 [20]). HPC 설계에서 특정 모델 공급사 종속을 피하는 OEM 요구가 실제 계약에 반영되고 있다.
3. **Tier-1의 역할은 "AI 개발"이 아닌 "시스템 통합·중앙집중형 도메인 컨트롤러"로 재정의되는 사례가 나왔다.** 근거: Valeo는 Nissan ProPILOT에서 센서·ADAS 도메인 컨트롤러·HW/SW 플랫폼을 공급·통합하고 주행 지능은 Wayve가 담당한다(🔍 Valeo [44]). Stellantis CEO는 외부 AI 도입의 동기를 개발 비용·기간 단축으로 명시했다(📰 Reuters [52]).
4. **검증 부하가 도로 주행에서 컴퓨트(시뮬레이션)로 옮겨가고 있고, 규제는 safety case 기반이다.** 근거: Wayve GAIA-4는 "검증은 컴퓨트로 스케일한다"를 명시하고, Waymo도 폐루프 시뮬레이션과 독립 검증 레이어를 필수로 제시하며, 영국은 APS 허가·ASDE 인가 체계를 2026~2027에 단계 시행한다(📄 [70][108]; 🔍 [102][104]). 차량 HPC 외에 데이터센터급 시뮬레이션 컴퓨트 수요가 자율주행 공급망의 일부가 됐다.
5. **상업 일정은 "양산 ADAS 2027~2028, 무인 로보택시는 그 이후"로 수렴한다.** 근거: Nissan FY2027(L2), Stellantis 2028(L2++), Mercedes 2년 내(주행보조), 프랑스 2028(실증)이며, 영국 무인 허가는 2026-10 말까지 0건, AV Act 전면 시행은 2027 하반기 목표다(🔍 [34][46][55][63]; 🔍 [102]; 📰 [96][105]). HPC·Tier-1의 L2+/L2++용 중앙집중형 컴퓨트 수요가 L4용 이중화 컴퓨트 수요보다 먼저 양산 규모에 도달한다.

---

## 8. 조사 방법과 한계

- **조사일**: 2026-10-30. 조사 범위 2025-11-01 ~ 2026-10-30.
- **방법**: 웹 검색 기반. 원문 페이지 직접 열람(WebFetch)이 네트워크 정책으로 제한되어(wayve.ai, nissannews.com, stellantis.com, gov.uk, legislation.gov.uk, techcrunch.com 등) 검색 엔진이 반환한 원문 발췌·스니펫과 복수 매체 교차 확인으로 검증한 항목이 많다. 인용 전 URL을 한 번 열어 대조하기를 권한다.
- **입력 자료**: 사용자의 tech-monitoring 일일 아카이브(2026-09-19 ~ 2026-10-30, 97건)를 사건 단위로 중복 제거한 뒤 1차 출처와 교차 검증했다. 아카이브 97건은 실질적으로 8개 핵심 사건으로 압축됐고, 약 50건은 중복 보도, 약 20건은 주식 필러·집계 페이지·커뮤니티 글이었다.
- **제외 기준**: 단일 약한 출처(주식 필러 사이트, 데이터 집계 사이트, 커뮤니티, 프로필 추론)에만 의존하는 항목, 날짜가 확정되지 않은 항목, 당사자가 확인하지 않은 보도는 제외했다. 대표적 제외 항목: Volkswagen의 Wayve 선정 보도(Der Spiegel 인용, 계약 미체결·3사 노코멘트), Nissan 양산 ProPILOT ECU가 Thor라는 보도, 집계 사이트의 매출 추정치, 이스라엘 오피스, 프랑스 협력의 Uber 참여, "Mercedes가 Alpamayo를 대체한다"는 해석, Stellantis 2027 중간 단계 보도, Momenta IPO 조달액(출처 상충), 경쟁사 밸류에이션 2차 수치.
- **수치 상충 처리**: 런던 플릿 대수(15대 vs 20대 미만), Series D 날짜(02-24 vs 02-25) 등은 공식·1차 자료 기준(TfL 면허 상한 15대, 미국 시간 기준 02-24 보도)으로 통일했다.
- **구조적 한계**: Wayve의 매출·수주·현금 소진율·플릿 대수·모델 사양은 어떤 공개 자료에도 없다. OEM 계약 3건의 금액·차종도 비공개다. Reuters 원문(2026-07-01, 2026-09-22, 2026-10-09)은 reuters.com 경로가 검색에 노출되지 않아 전재 매체 URL로 대체했다.

---

## 출처

1. 🔍 Companies House — WAYVE TECHNOLOGIES LTD (회사번호 10924127) — 설립 2017-08-21 — https://find-and-update.company-information.service.gov.uk/company/10924127
2. 📰 Unquote — Eclipse leads USD 20m Series A for Wayve — 2019-11-18 — https://www.unquote.com/uk/official-record/3017287/eclipse-leads-usd20m-series-a-for-wayve
3. 📰 Eclipse Ventures 블로그 — Accelerating the Next Wave of Autonomous Vehicles: Our Series B in Wayve — 2022-01 — https://eclipse.vc/blog/accelerating-the-next-wave-of-autonomous-vehicles-our-series-b-in-wayve
4. 🔍 Wayve 보도자료 — Series C ($1.05B, SoftBank 주도) — 2024-05 — https://wayve.ai/press/series-c/
5. 🔍 Wayve 보도자료 — US expansion (Sunnyvale office, SF Bay Area testing) — 2024-10-23 — https://wayve.ai/press/us-expansion/
6. 🔍 Wayve 보도자료 — Wayve Germany expansion (Stuttgart region hub) — 2025-03 — https://wayve.ai/press/wayve-germany-expansion/
7. 🔍 Wayve 보도자료 — Wayve Japan launch (Yokohama testing & development centre) — 2025-04-22 — https://wayve.ai/press/wayve-japan-launch/
8. 🔍 Nissan Global Newsroom — Nissan and Wayve partnership on next-generation ProPILOT (250410-01-e) — 2025-04-10 — https://global.nissannews.com/en/releases/250410-01-e
9. 📰 BusinessWire — Wayve and Uber announce partnership for L4 autonomous trials in London — 2025-06-10 — https://www.businesswire.com/news/home/20250610938773/en
10. 📰 Tech.eu — Wayve sees leap in headcount to 650 amid expansion into new markets — 2025-07-28 — https://tech.eu/2025/07/28/wayve-sees-leap-in-headcount-to-650-amid-expansion-into-new-markets/
11. 📄 Wayve 블로그 — Wayve Gen 3 robot vehicle platform built on NVIDIA DRIVE AGX Thor — 2025-09 — https://wayve.ai/thinking/wayve-gen-3/
12. 🔍 Wayve 보도자료 — Wayve and NVIDIA announcement ($500M strategic investment LOI) — 2025-09-19 — https://wayve.ai/press/wayve-nvidia-announcement/
13. 📰 TechCrunch — Nvidia eyes $500M investment into self-driving tech startup Wayve — 2025-09-19 — https://techcrunch.com/2025/09/19/nvidia-eyes-500m-investment-into-self-driving-tech-startup-wayve
14. 📰 BusinessWire — Robot car talk: Introducing Wayve's new AI model LINGO-1 — 2023-09-14 — https://www.businesswire.com/news/home/20230914118208/en/5519094/Robot-car-talk-Introducing-Wayves-new-AI-model-LINGO-1
15. 📰 BusinessWire — Wayve GAIA-1 technical report (9B generative world model) — 2023-10-03 — https://www.businesswire.com/news/home/20231003373396/en
16. 🔍 Wayve Labs — LINGO (LINGO-2 closed-loop VLA) — https://wayve.ai/labs/lingo/
17. 📄 arXiv 2503.20523 — GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving — 2025-03-26 — https://arxiv.org/abs/2503.20523v1
18. 🔍 Wayve 보도자료 — Wayve secures $1.5B to deploy its global autonomy platform (Series D) — 2026-02-24 — https://wayve.ai/press/series-d/
19. 📰 CNBC — Wayve raises $1.2 billion from Nvidia, Microsoft and automakers — 2026-02-24 — https://www.cnbc.com/2026/02/24/wayve-fundraise-nvidia-microsoft.html
20. 📰 TechCrunch — Self-driving tech startup Wayve raises $1.2B from Nvidia, Uber and three automakers — 2026-02-24 — https://techcrunch.com/2026/02/24/self-driving-tech-startup-wayve-raises-1-2b-from-nvidia-uber-and-three-automakers/
21. 📰 Reuters (MarketScreener 전재) — UK self-driving startup Wayve raises $1.2 billion from investors including Mercedes, Stellantis — 2026-02-24 — https://uk.marketscreener.com/news/uk-self-driving-startup-wayve-raises-1-2-billion-from-investors-including-mercedes-stellantis-ce7e5cdad080f424
22. 📰 electrive — Mercedes, Stellantis, Uber and others invest in Wayve — 2026-02-26 — https://www.electrive.com/2026/02/26/mercedes-stellantis-uber-and-others-invest-in-wayve/
23. 📰 Weil, Gotshal & Manges — Weil advises Balderton Capital as a lead investor in the $1.2B Series D for Wayve — 2026-02 — https://www.weil.com/articles/weil-advises-balderton-capital-as-a-lead-investor-in-the-1-point-2-b-series-d-for-wayve
24. 📰 Zag Daily — Global automakers back Wayve in $1.2bn funding raise — 2026-02 — https://zagdaily.com/connected/global-automakers-back-wayve-in-1-2bn-funding-raise/
25. 🔍 Wayve 보도자료 — Series D Extension ($60M from AMD, Arm, Qualcomm Ventures) — 2026-04-15 — https://wayve.ai/press/series-d-extension/
26. 📰 CNBC — Wayve raises $60 million from AMD, Qualcomm and Arm — 2026-04-15 — https://www.cnbc.com/2026/04/15/wayve-fund-raise-amd-qualcomm-arm.html
27. 📰 TechCrunch — Chipmakers AMD, Arm and Qualcomm are all investing in this buzzy self-driving tech startup — 2026-04-15 — https://techcrunch.com/2026/04/15/chipmakers-amd-arm-and-qualcomm-are-all-investing-in-this-buzzy-self-driving-tech-startup/
28. 📰 TechCrunch — Wayve launches $85M employee tender offer at $8.5B valuation — 2026-06-30 — https://techcrunch.com/2026/06/30/wayve-launches-85m-employee-tender-offer-at-8-5b-valuation
29. 📰 Tech.eu — Wayve undertakes $85M employee tender offer to retain talent — 2026-07-01 — https://tech.eu/2026/07/01/wayve-undertakes-85m-employee-tender-offer-to-retain-talent/
30. 🔍 Wayve 블로그 — Wayve announces employee tender offer (1,200 people, 6 countries) — 2026-06-30 — https://wayve.ai/thinking/wayve-announces-employee-tender-offer/
31. 📰 TechCrunch — Former Waymo CFO jumps to self-driving startup Wayve — 2026-09-16 — https://techcrunch.com/2026/09/16/former-waymo-cfo-jumps-to-self-driving-startup-wayve/
32. 📰 CFO Dive — Wayve nabs former Waymo CFO as finance chief — 2026-09 — https://www.cfodive.com/news/wayve-nabs-former-waymo-cfo-finance-chief-autos/830699/
33. 🔍 Nissan Global Newsroom — Nissan unveils next-generation ProPILOT featuring AI ahead of FY27 launch — 2025-09-22 — https://global.nissannews.com/en/releases/next-gen-propilot-technology
34. 🔍 Nissan Global Newsroom — Nissan and Wayve sign definitive agreements to deliver next-generation driver assistance technology (251210-01-e) — 2025-12-10 — https://global.nissannews.com/en/releases/251210-01-e
35. 🔍 Wayve 보도자료 — Nissan and Wayve sign definitive agreements — 2025-12-10 — https://wayve.ai/press/nissan-wayve-sign-definitive-agreements/
36. 📰 S&P Global AutoTechInsight — Nissan collaborates with Wayve to integrate AI in next-gen ProPILOT series vehicles — 2025-12 — https://autotechinsight.spglobal.com/news/5285581/nissan-collaborates-with-wayve-to-integrate-ai-in-next-gen-propilot-series-vehicles
37. 🔍 Uber Investor Relations — Wayve, Uber and Nissan Announce Collaboration on Robotaxis — 2026-03-12 — https://investor.uber.com/news-events/news/press-release-details/2026/Wayve-Uber-and-Nissan-Announce-Collaboration-on-Robotaxis/default.aspx
38. 🔍 Nissan Global Newsroom — Wayve, Uber and Nissan announce collaboration on robotaxis — 2026-03-12 — https://global.nissannews.com/en/releases/wayve-uber-and-nissan-announce-collaboration-on-robotaxis
39. 🔍 Wayve 보도자료 — Wayve and Nissan reveal global robotaxi prototype at NVIDIA GTC 2026 — 2026-03-16 — https://wayve.ai/press/wayve-nissan-robotaxi-gtc/
40. 🔍 Nissan Global Newsroom — Wayve and Nissan to exhibit global robotaxi prototype vehicle at NVIDIA GTC 2026 — 2026-03-16 — https://global.nissannews.com/en/releases/wayve-and-nissan-to-exhibit-global-robotaxi-prototype-vehicle-at-nvidia-gtc-2026
41. 🔍 NVIDIA Newsroom — BYD, Geely, Isuzu and Nissan Adopt NVIDIA DRIVE Hyperion for Level 4 Vehicles — 2026-03-16 — https://nvidianews.nvidia.com/news/drive-hyperion-level-4
42. 📰 Nasdaq/RTTNews — Uber Japan partners with Hinomaru Kotsu for robotaxi pilot deployment in Tokyo — 2026-08-13 — https://nasdaq.com/articles/uber-japan-partners-hinomaru-kotsu-robotaxi-pilot-deployment-tokyo
43. 📰 just-auto — Uber, Hinomaru Kotsu team up for Tokyo robotaxi pilot — 2026-08 — https://www.just-auto.com/newsletters/uber-hinomaru-kotsu-robotaxi-pilot
44. 🔍 Valeo 보도자료 — Valeo selected by Nissan as partner for next-generation ProPILOT program — 2026-10-01 — https://www.valeo.com/en/valeo-selected-by-nissan-as-partner-for-next-generation-propilot-program/
45. 📰 just-auto — Valeo selected by Nissan as partner for ProPILOT — 2026-10-01 — https://www.just-auto.com/news/valeo-selected-by-nissan-as-partner-for-propilot/
46. 🔍 Stellantis 보도자료 — Stellantis and Wayve partner to bring hands-free, door-to-door supervised automated driving at scale — 2026-05-21 — https://www.stellantis.com/en/news/press-releases/2026/may/stellantis-and-wayve-partner-to-bring-hands-free-door-to-door-supervised-automated-driving-at-scale
47. 🔍 Stellantis — Investor Day 2026 (Auburn Hills) — 2026-05-21 — https://www.stellantis.com/en/investors/events/stellantis-investor-day-2026
48. 📰 TechCrunch — Wayve's self-driving tech is headed to US cars made by Stellantis — 2026-05-21 — https://techcrunch.com/2026/05/21/wayves-self-driving-tech-is-headed-to-us-cars-made-by-stellantis/
49. 🔍 Stellantis 보도자료 — Stellantis, Wayve and Uber partner to scale robotaxis globally — 2026-06-17 — https://www.stellantis.com/en/news/press-releases/2026/june/stellantis-wayve-and-uber-partner-to-scale-robotaxis-globally
50. 🔍 Wayve 보도자료 — Stellantis, Wayve and Uber robotaxi partnership — 2026-06-17 — https://wayve.ai/press/stellantis-wayve-uber-robotaxi-partnership/
51. 🔍 Stellantis 보도자료 — Stellantis and Wayve to demonstrate AI-powered hands-free driving at Wave by Vento 2026 — 2026-10-01 — https://www.media.stellantis.com/em-en/corporate/press/stellantis-and-wayve-to-demonstrate-ai-powered-hands-free-driving-at-wave-by-vento-2026
52. 📰 Reuters (Yahoo Finance 전재) — Stellantis CEO says Wayve tie-up can cut self-driving costs, development time — 2026-10-09 — https://finance.yahoo.com/technology/ai/articles/stellantis-ceo-says-wayve-deal-131915133.html
53. 📰 The Detroit News — Stellantis CEO says partnership can speed self-driving tech, cut costs — 2026-10-09 — https://www.detroitnews.com/story/business/autos/chrysler/2026/10/09/stellantis-ceo-says-partnership-can-speed-self-driving-tech-cut-costs/92168084007/
54. 📰 The Next Web — Alex Kendall: AI driving will be required 'like a seatbelt' — 2026-10-10 — https://thenextweb.com/news/alex-kendall-wayve-stellantis-ai-driving-seatbelt-wave-by-vento
55. 🔍 Wayve 보도자료 — Wayve and Mercedes-Benz announce production agreement — 2026-09-22 — https://wayve.ai/press/wayve-mercedes-benz-announce-production-agreement/
56. 📰 Electrek — Mercedes-Benz signs production agreement for Wayve AI Driver — 2026-09-22 — https://electrek.co/2026/09/22/mercedes-benz-wayve-ai-driver-production-agreement/
57. 📰 Automotive World — Mercedes-Benz signs production deal for Wayve AI Driver — 2026-09-22 — https://www.automotiveworld.com/news/mercedes-benz-signs-production-deal-for-wayve-ai-driver/
58. 📰 City A.M. — Mercedes rides the AI Wayve with self-driving deal — 2026-09-22 — https://www.cityam.com/mercedes-rides-the-ai-wayve-with-self-driving-deal/
59. 🔍 Mercedes-Benz Group — Mercedes-Benz and NVIDIA expand strategic partnership for next-generation automated driving — 2026-10-16 — https://group.mercedes-benz.com/company/news/mb-and-nvidia-expand-strategic-partnership.html
60. 🔍 Wayve 보도자료 — Qualcomm and Wayve collaborate on production-ready ADAS/AD system (Snapdragon Ride) — 2026-03-10 — https://wayve.ai/press/qualcomm-wayve-collaboration/
61. 📰 Reuters (The Star 전재) — Qualcomm, Wayve partner to accelerate AI-powered self-driving system rollout — 2026-03-10 — https://www.thestar.com.my/tech/tech-news/2026/03/10/qualcomm-wayve-partner-to-accelerate-ai-powered-self-driving-system-rollout
62. 📰 Automotive World — Qualcomm and Wayve partner on production ADAS/AD system — 2026-03 — https://www.automotiveworld.com/news/qualcomm-and-wayve-partner-on-production-adas-ad-system/
63. 🔍 Wayve 보도자료 — Wayve, Stellantis and NVIDIA collaborate to advance safe and responsible AV deployment across France — 2026-10-23 — https://wayve.ai/press/wayve-stellantis-nvidia-collaborate-on-deployment-across-france/
64. 🔍 Stellantis 미디어 — Wayve, Stellantis and NVIDIA collaborate to advance safe and responsible autonomous vehicle deployment across France — 2026-10-23 — https://www.media.stellantis.com/em-en/corporate/press/wayve-stellantis-and-nvidia-collaborate-to-advance-safe-and-responsible-autonomous-vehicle-deployment-across-france
65. 📰 electrive — Stellantis moves forward with autonomous mobility initiatives in France — 2026-10-26 — https://www.electrive.com/2026/10/26/stellantis-moves-forward-with-autonomous-mobility-initiatives-in-france/
66. 📰 The Next Web — Wayve, Stellantis and NVIDIA join France's self-driving push — 2026-10-24 — https://thenextweb.com/news/wayve-stellantis-nvidia-france-self-driving
67. 📄 Wayve 블로그 — GAIA-3: Scaling World Models to Power Safety and Evaluation — 2025-12-02 — https://wayve.ai/thinking/gaia-3/
68. 🔍 Wayve 보도자료 — Wayve launches GAIA-3 — 2025-12-02 — https://wayve.ai/press/wayve-launches-gaia3/
69. 📰 Automotive World — Wayve unveils GAIA-3 for autonomous driving tests (DriveSafeSim, WMG) — 2025-12 — https://www.automotiveworld.com/news/wayve-unveils-gaia-3-for-autonomous-driving-tests/
70. 📄 Wayve 블로그 — GAIA-4: Multimodal World Models Powering Closed-Loop Simulation for Safe and Scalable Autonomy — 2026-08-03 — https://wayve.ai/thinking/gaia-4/
71. 📄 arXiv 2604.27448 — LA-Pose: Latent Action Pretraining Meets Pose Estimation — 2026-04 — https://arxiv.org/html/2604.27448v1
72. 📄 Wayve 블로그 — LA-Pose: What 10 million driving videos taught us about self-supervised perception — 2026-05-05 — https://wayve.ai/thinking/la-pose/
73. 📄 CVPR 2026 — LA-Pose poster (2026-06-07, ExHall F, Denver) — https://cvpr.thecvf.com/virtual/2026/poster/40064
74. 📄 Wayve 블로그 — Building Intelligence That Can Act in the World (Wayve Labs 출범) — 2026-05-29 — https://wayve.ai/thinking/building-intelligence-that-can-act-in-the-world/
75. 🔍 Wayve — Wayve Labs 페이지 (research areas) — https://wayve.ai/labs/
76. 📄 Wayve 블로그 — The AI-500 Roadshow: 500 Cities and What We Learned — 2025-12 로드쇼 완료 — https://wayve.ai/thinking/ai-500-roadshow-500-cities/
77. 📄 Wayve 블로그 — AI-500 Roadshow: 90 cities in 90 days — 2025 — https://wayve.ai/thinking/ai-500-roadshow-90-cities/
78. 📄 NeurIPS 2025 Workshop on Embodied World Models for Decision Making — Industry demo "Scaling World Models to Power Evaluation and Validation" (Wayve) — 2025-12-06 — https://embodied-world-models.github.io/
79. 📄 CVPR 2026 Workshop on Autonomous Driving — Invited talk, Alex Kendall "Frontier Challenges in Bringing AI to 1B Robots" — 2026-06-03 — https://cvpr2026.wad.vision/
80. 📰 Axios — Wayve's robotaxi bet: not Tesla, not Waymo (Kendall on sensors) — 2026-09-16 — https://www.axios.com/2026/09/16/wayve-robotaxi-av-tesla-waymo
81. 🔍 Microsoft Source — AI that drives change: Wayve rewrites self-driving playbook with deep learning in Azure — 2025-10 — https://news.microsoft.com/source/emea/features/ai-that-drives-change-wayve-rewrites-self-driving-playbook-with-deep-learning-in-azure/
82. 🔍 Wayve 제품 페이지 — From Assisted to Fully Automated Driving: The Wayve AI Driver Solution — https://wayve.ai/product/wayve-ai-driver/
83. 🔍 Wayve 보도자료 — Wayve and Uber secure TfL private hire vehicle licences for London — 2026-08-05 — https://wayve.ai/press/wayve-uber-phv-license/
84. 🔍 Uber Investor Relations — Wayve and Uber Move a Step Closer to Autonomous Rides in London — 2026-08-05 — https://investor.uber.com/news-events/news/press-release-details/2026/Wayve-and-Uber-Move-a-Step-Closer-to-Autonomous-Rides-in-London/default.aspx
85. 📰 Fleet News — Wayve granted private hire licences for autonomous rides in London (GMB 반대 포함) — 2026-08-05 — https://www.fleetnews.co.uk/news/wayve-granted-private-hire-licences-for-autonomous-rides-in-london
86. 📰 Bloomberg — Uber and Wayve win licenses for supervised robotaxis in London — 2026-08-05 — https://www.bloomberg.com/news/articles/2026-08-05/uber-and-wayve-win-licenses-for-supervised-robotaxis-in-london
87. 📰 Electrifying.com — Wayve wins first TfL approval for self-driving taxis (APS 절차 미개시) — 2026-08 — https://www.electrifying.com/blog/article/wayve-wins-first-tfl-approval-for-self-driving-taxis
88. 📰 TechTimes — London robotaxi riders promised 2026 driverless trips; TfL says no rush — 2026-08-27 — https://www.techtimes.com/articles/325810/20260827/london-robotaxi-riders-promised-2026-driverless-trips-tfl-says-no-rush.htm
89. 📰 City A.M. — Uber and Wayve open London robotaxi interest list — 2026-06 — https://www.cityam.com/?p=2431692
90. 🔍 Wayve 보도자료 — Wayve and Uber launch first-ever autonomous rides in the UK — 2026-09-03 — https://wayve.ai/press/wayve-uber-launch-autonomous-rides/
91. 🔍 Uber Newsroom — Wayve on Uber: autonomous rides in London — 2026-09-03 — https://www.uber.com/us/en/newsroom/wayve-on-uber/
92. 📰 Reuters (The Star 전재) — Uber and AI firm Wayve launch London's first robotaxis — 2026-09-03 — https://www.thestar.com.my/tech/tech-news/2026/09/03/uber-and-ai-firm-wayve-launch-london039s-first-robotaxis
93. 📰 Tech.eu — Londoners can now hail Wayve autonomous vehicles through Uber — 2026-09-03 — https://tech.eu/2026/09/03/londoners-can-now-hail-wayve-autonomous-vehicles-through-uber
94. 📰 electrive — Wayve and Uber launch autonomous rides in London — 2026-09-03 — https://www.electrive.com/2026/09/03/wayve-and-uber-launch-autonomous-rides-in-london/
95. 📰 The Next Web — Uber and Wayve launch London robotaxis — with a safety driver — 2026-09-03 — https://thenextweb.com/news/uber-wayve-london-robotaxi-launch-safety-driver
96. 📰 Automotive World — London's first self-driving taxis hit the road with Wayve (시승 개입·TfL 입장) — 2026-09 — https://www.automotiveworld.com/news/londons-first-self-driving-taxis-hit-the-road-with-wayve/
97. 📰 ITV News London — "I feel like an old car": drivers protest against robotaxis outside Wayve HQ — 2026-10-17 — https://www.itv.com/news/london/2026-10-17/i-feel-like-an-old-car-drivers-protest-against-robotaxis
98. 📰 Silicon UK — Drivers protest Uber–Wayve robotaxis in London — 2026-10 — https://www.silicon.co.uk/e-innovation/artificial-intelligence/wayve-protest-robotaxi-631925
99. 🔍 London Assembly Transport Committee — Who's driving the future of autonomous transport in London? — 2026-10-12 — https://www.london.gov.uk/who-we-are/what-london-assembly-does/london-assembly-work/london-assembly-publications/whos-driving-future-autonomous-transport-london
100. 🔍 Hansard (House of Commons) — Automated Vehicles Act 2024: Implementation — 2025-06-10 — https://hansard.parliament.uk/Commons/2025-06-10/debates/25061070000006/AutomatedVehiclesAct2024Implementation
101. 🔍 legislation.gov.uk — The Automated Vehicles Act 2024 (Commencement No. 1) Regulations 2025 (SI 2025/1339) — 2025-12-15 — https://www.legislation.gov.uk/uksi/2025/1339/made
102. 🔍 legislation.gov.uk — The Automated Vehicles Act 2024 (Commencement No. 2) Regulations 2026 (SI 2026/437) — 2026-04-20 — https://www.legislation.gov.uk/uksi/2026/437/made
103. 🔍 GOV.UK — Automated passenger services permitting scheme: government response — 2026-04-23 — https://www.gov.uk/government/speeches/automated-passenger-services-permitting-scheme-government-response
104. 🔍 legislation.gov.uk — The Automated Vehicles Act 2024 (Commencement No. 3) Regulations 2026 (SI 2026/731) — 2026-07-01 — https://www.legislation.gov.uk/uksi/2026/731/made
105. 📰 Shoosmiths — Automated vehicles: government launches self-driving pilot scheme (전면 시행 2027 하반기) — 2025-06 — https://www.shoosmiths.com/perspectives/stories/articles/automated-vehicles-government-launches-self-driving-pilot-scheme
106. 📰 Automotive World — Uber and Wayve to trial London robotaxis in spring 2026 — 2025/2026 — https://www.automotiveworld.com/articles/uber-and-wayve-to-trial-london-robotaxis-in-spring-2026/
107. 📰 Reuters (Investing.com 전재) — Wayve courts automakers with AI driving system that learns like humans (Nissan Akashi 발언) — 2026-07-01 — https://www.investing.com/news/stock-market-news/wayve-courts-automakers-with-ai-driving-system-that-learns-like-humans-4769850
108. 📄 Waymo 블로그 — 10 AI Lessons from Driving 200+ Million Fully Autonomous Miles (Srikanth Thirumalai) — 2026-08-26 — https://waymo.com/blog/2026/08/10ailessons/
109. 📰 Axios — Waymo says there's no AI shortcut to self-driving — 2026-08-26 — https://www.axios.com/2026/08/26/waymo-ai-shortcut-self-driving
110. 📰 TechCrunch — Waymo's skyrocketing ridership in one chart (주 50만 유료 승차, 10개 도시) — 2026-03-27 — https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/
111. 📰 TechCrunch — London gets closer to its first robotaxi service as Waymo begins testing — 2026-04-14 — https://techcrunch.com/2026/04/14/london-gets-closer-to-its-first-robotaxi-service-as-waymo-begins-testing/
112. 📰 Claims Journal — Waymo fleet about 4,000 vehicles — 2026-10-20 — https://www.claimsjournal.com/news/national/2026/10/20/340813.htm
113. 🔍 Tesla, Inc. — Form 10-Q, quarter ended 2026-09-30 (SEC) — 2026-10 — https://www.sec.gov/Archives/edgar/data/0001318605/000162828026066775/tsla-20260930.htm
114. 📰 Electrek — Tesla (TSLA) Q3 2026 financial results — 2026-10-21 — https://electrek.co/2026/10/21/tesla-tsla-q3-2026-financial-results/
115. 🔍 Mobileye — Form 8-K Exhibit 99.1, Q3 2026 results (SEC) — 2026-10-29 — https://www.sec.gov/Archives/edgar/data/0001910139/000110465926119830/tm2628197d1_ex99-1.htm
116. 📰 Investing.com — Earnings call transcript: Mobileye Q3 2026 — 2026-10-29 — https://www.investing.com/news/transcripts/earnings-call-transcript-mobileye-misses-q3-2026-estimates-as-stock-drops-premarket-93CH-4983845
117. 🔍 Mobileye — Form 8-K Exhibit 99.1, Q1 2026 results (SEC) — 2026-04 — https://www.sec.gov/Archives/edgar/data/0001910139/000110465926047231/tm2612233d1_ex99-1.htm
118. 📄 Mobileye 블로그 — From pilot testing to auto-pilot: driven by Mobileye (EyeQ6H x4, Compound AI) — https://www.mobileye.com/blog/from-pilot-testing-to-auto-pilot-driven-by-mobileye/
119. 📰 electrive — VW Commercial Vehicles ramps up pre-series production of the autonomous ID. Buzz AD — 2026-03-06 — https://www.electrive.com/2026/03/06/vw-commercial-vehicles-ramps-up-pre-series-production-of-the-autonomous-id-buzz-ad/
120. 📰 TechCrunch — Nvidia launches Alpamayo, open AI models that allow autonomous vehicles to think like a human — 2026-01-05 — https://techcrunch.com/2026/01/05/nvidia-launches-alpamayo-open-ai-models-that-allow-autonomous-vehicles-to-think-like-a-human/
121. 📄 GitHub — NVlabs/alpamayo (Alpamayo 1, 10B open-weight reasoning VLA) — https://github.com/NVlabs/alpamayo
122. 📰 Electrek — Nvidia unveils open-source AI for autonomous driving, ships in Mercedes-Benz CLA in Q1 2026 — 2026-01-05 — https://electrek.co/2026/01/05/nvidia-unveils-open-source-ai-for-autonomous-driving-ships-in-mercedes-benz-cla-in-q1-2026/
123. 📰 Counterpoint Research — Test driving NVIDIA's L2 Hyperion AV stack (Mercedes CLA, Orin급 254 TOPS) — 2026 — https://counterpointresearch.com/en/insights/test-driving-nvidias-l2-hyperion-av-stack
124. 📰 CnEVPost — Mercedes, Momenta launch robotaxi service in Abu Dhabi — 2025-12-09 — https://cnevpost.com/2025/12/09/mercedes-momenta-launch-robotaxi-service-abu-dhabi/
125. 🔍 Momenta — Audi E7X pre-sale with Momenta co-developed L3 — 2026-05-08 — https://www.momenta.ai/en/article/569.html
126. 📰 CnEVPost — Momenta cleared to test robotaxis across Germany, Uber invests more — 2026-07-29 — https://cnevpost.com/2026/07/29/momenta-cleared-test-robotaxis-across-germany/
127. 📰 CnEVPost — Momenta to develop driver assistance systems for Peugeot, Jeep (DSAT) — 2026-09-28 — https://cnevpost.com/2026/09/28/momenta-develop-driver-assistance-peugeot-jeep/
128. 🔍 Uber Investor Relations — Pony.ai and Uber Expand Partnership to Deploy Over 2,000 Robotaxis in Europe — 2026-08-14 — https://investor.uber.com/news-events/news/press-release-details/2026/Pony-ai-and-Uber-Expand-Partnership-to-Deploy-Over-2000-Robotaxis-in-Europe/default.aspx
129. 🔍 Pony.ai — Form 6-K, Q2 2026 results (SEC) — 2026-08 — https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-2.htm
130. 🔍 WeRide — Form 6-K (SEC), global L4 fleet about 3,400 — 2026 — https://www.sec.gov/Archives/edgar/data/0001867729/000110465926059704/tm2614059d1_ex99-1.htm
131. 📰 TechCrunch — Uber and China's Pony.ai plan to launch robotaxis in London — 2026-10-08 — https://techcrunch.com/2026/10/08/uber-and-chinas-pony-ai-plan-to-launch-robotaxis-in-london/
132. 📰 Automotive World — Wayve and Nissan reveal LEAF-based robotaxi prototype at GTC — 2026-03 — https://www.automotiveworld.com/news/wayve-and-nissan-reveal-leaf-based-robotaxi-prototype-at-gtc/
133. 🔍 Ontario Teachers' Pension Plan — Wayve secures funding to deploy global autonomy platform — 2026-02 — https://www.otpp.com/en-ca/about-us/news-and-insights/2026/wayve-secures-funding-to-deploy-global-autonomy-platform/
