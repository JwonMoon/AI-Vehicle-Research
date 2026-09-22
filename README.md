# AI-Vehicle-Research

차량용 AI(자율주행·차량 HPC·모빌리티 데이터 생태계) 관련 리서치, 스터디 세미나, 뉴스 다이제스트 아카이브.

## 구조

```
├── seminars/    # 사내 자율주행 스터디 세미나 자료
├── research/    # 주제별 심층 리서치 보고서
└── news/        # 데일리 AI 뉴스 다이제스트
```

## seminars — 자율주행 스터디

차량용 HPC 아키텍처 설계 관점의 자율주행/ADAS 스터디. → [개요](seminars/README.md)

| 회차 | 주제 | 자료 |
|---|---|---|
| ⭐ 통합 | 자율주행 기술 + 차량용 HPC 아키텍처 통합 보고서 | [report.html](seminars/full-report/report.html) |
| 1 | 자율주행 AD 워크로드 | [material](seminars/01-ad-workloads/material.md) · [slides](seminars/01-ad-workloads/slides.html) |
| 2 | 차량용 HPC 플랫폼 | [material](seminars/02-hpc-platform/material.md) · [slides](seminars/02-hpc-platform/slides.html) |

## research — 주제별 심층 리서치

| 주제 | 요약 | 작성 | 핵심 문서 |
|---|---|---|---|
| [11-capnproto-vs-protobuf](research/11-capnproto-vs-protobuf/) | Cap'n Proto vs Protobuf 직렬화 비교 — 직렬화 개념부터 시작해 두 와이어 포맷을 실제 바이트로 해부(같은 값이 Protobuf 25 B vs Cap'n Proto 88 B, packed 29 B), C++ 자체 벤치마크로 성능·크기·힙 할당 실측(1 MiB 디코딩 9.1배·헤더 1필드 읽기 653배는 Cap'n Proto 우위, 100 B 인코딩 62 ns vs 77 ns는 Protobuf 우위, Cap'n Proto 디코딩 malloc 0회), 유지보수·생태계 정합성·보안·풋프린트·거버넌스 7개 관점 비교, 차량 5개 구간별 도입 가능성 지도(SOME/IP 1400 B 상한·CAN·클라우드는 자리 없음, SoC 내 IPC 하나만 후보), ISO 26262·AUTOSAR C++14 동적할당/예외 관문, FlatBuffers·iceoryx·Apollo CyberRT 대안 비교와 의사결정 플로차트 | 2026-09 | [보고서](research/11-capnproto-vs-protobuf/capnproto-vs-protobuf.md) · [웹 버전](research/11-capnproto-vs-protobuf/capnproto-vs-protobuf.html) · [벤치마크](research/11-capnproto-vs-protobuf/scripts/README.md) · [출처 기록](research/11-capnproto-vs-protobuf/reference/references.md) |
| [10-qualcomm-83xx-cockpit-elite](research/10-qualcomm-83xx-cockpit-elite/) | 퀄컴 83xx(SA8397P · Snapdragon Cockpit Elite) vs 82xx(SA8255P/SA8295P) — 품번·계보 정리, Oryon CPU(Kryo→자체 설계)·NPU 12×(30→320 TOPS)·256-bit LPDDR5X ~273 GB/s·ASIL-D safety island·Type-1 하이퍼바이저 차이 6가지, 8397P vs 8797P 역할 구분, 2026 양산 현황(Leapmotor·Li Auto·JLR×체리·LG전자), 공개 툴체인 미등재, IPCU 성능형 SoC 관점 시사점 | 2026-09 | [보고서](research/10-qualcomm-83xx-cockpit-elite/qualcomm-83xx-cockpit-elite.md) · [웹 버전](research/10-qualcomm-83xx-cockpit-elite/qualcomm-83xx-cockpit-elite.html) · [출처 기록](research/10-qualcomm-83xx-cockpit-elite/reference/references.md) |
| [09-ad-sw-stack-deep-dive](research/09-ad-sw-stack-deep-dive/) | 자율주행 SW 스택 심층편 5부작 — 20년 진화(신경망 경계 6단계), Autoware 7개 컴포넌트 + System·AD API와 센서→제어 데이터 흐름 해부(Agnocast·cuda_blackboard·Generator–Selector)와 NVIDIA DRIVE AV 층별 해부(Thor·DriveOS·TensorRT safety runtime·Alpamayo 카메라→궤적 추론 흐름·Halos), 데이터 플라이휠·개루프/폐루프 검증(Bench2Drive·pseudo-sim), 양산 필수 기술(혼합 중요도·ASIL 근거 형태·EDR/DSSAD·NHTSA 2026), 미래 방향(증류 + 독립 검증층·메모리 대역폭·zero-copy 경로 분화) · 고정 커밋 소스 코드 대조(Autoware 1.9.0·Alpamayo) + 사내 기사 · 후속 Thor 배포편(Jetson vs DRIVE Thor 사양·Alpamayo 시리즈별 적재 가능성·Autoware 실행 조건·서버 실행 사례·Alpamayo 2 코드 기반 SW 컴포넌트 그림·Alpamayo 1/1.5/2 소스 코드 기반 컴포넌트 구조도·단계별 계획) | 2026-09 | [보고서](research/09-ad-sw-stack-deep-dive/ad-sw-stack-deep-dive.md) · [기사](research/09-ad-sw-stack-deep-dive/article.md) · [출처 기록](research/09-ad-sw-stack-deep-dive/reference/references.md) · [폴더 안내](research/09-ad-sw-stack-deep-dive/README.md) · [Thor 배포 보고서](research/09-ad-sw-stack-deep-dive/thor-deployment/thor-deployment.md) |
| [08-autonomous-driving-sw-stack](research/08-autonomous-driving-sw-stack/) | 자율주행 SW 스택 12종 해부 — 8층 스택 지도, Autoware·Apollo·openpilot 코드 실측 비교(패키지 365·dag 109·프로세스 44), UniAD→DiffusionDrive 학계 계보, Alpamayo·DRIVE AV·Tesla·Wayve·Waymo·Mobileye·Huawei·Momenta·XPeng 비교표, ROS 2 rmw·Agnocast·Zenoh·AUTOSAR Adaptive·S-CORE·SOAFEE 미들웨어 층과 IPC 실측(D4), 2026 동향 뉴스, 차량 HPC 관점 시사점·자사 관점 + 사내 기사 | 2026-09 | [보고서](research/08-autonomous-driving-sw-stack/autonomous-driving-sw-stack.md) · [웹 버전](research/08-autonomous-driving-sw-stack/autonomous-driving-sw-stack.html) · [기사](research/08-autonomous-driving-sw-stack/article.md) · [출처 기록](research/08-autonomous-driving-sw-stack/reference/references.md) · [폴더 안내](research/08-autonomous-driving-sw-stack/README.md) |
| [07-tier4-alpamayo-autoware](research/07-tier4-alpamayo-autoware/) | TIER IV × NVIDIA 협력의 실체 — Alpamayo 1.5·2 Super VLA를 Autoware에 얹은 ROS 2 노드 전 브랜치 코드 해부, 0.600s→3.35s 지연 현실, Cosmos × Co-MLOps 데이터 축, Isuzu L4 버스와 자체 E2E 모델 트랙 | 2026-09 | [보고서](research/07-tier4-alpamayo-autoware/tier4_alpamayo_autoware_보고서.md) · [웹 버전](research/07-tier4-alpamayo-autoware/tier4_alpamayo_autoware_보고서.html) · [출처 기록](research/07-tier4-alpamayo-autoware/reference/references.md) |
| [06-aumovio-sensor-cleaning](research/06-aumovio-sensor-cleaning/) | 센서 세정 2부작 — ① AUMOVIO 세정 시스템 기술 해부(Coanda 노즐·유체 체인·CERTINA 매각) ② 센서 오염의 인지 영향 실측과 SW 대응 5계층(검출·복원·강건화·융합·축퇴), 특허 폐루프 | 2026-09 | [1편 세정 HW](research/06-aumovio-sensor-cleaning/aumovio-sensor-cleaning.md) · [1편 웹](research/06-aumovio-sensor-cleaning/aumovio-sensor-cleaning.html) · [2편 SW 대응](research/06-aumovio-sensor-cleaning/sensor-soiling-sw-compensation.md) · [2편 웹](research/06-aumovio-sensor-cleaning/sensor-soiling-sw-compensation.html) |
| [05-nvidia-fullstack](research/05-nvidia-fullstack/) | NVIDIA 차량용 풀스택 SW 7장 분담 조사 — 3장 자율주행 스택(Alpamayo 1→2 Super, AlpaSim·AlpaGym 폐루프 시뮬·RL, DRIVE AV 듀얼 스택, Hyperion 10), 7장 Physical AI/Cosmos(세대·데이터 파이프라인·Omniverse 역할 구분·활용 패턴), 부록 Tier-1 관점 작업 범위(Android 대입) | 2026-09 | [3장 보고서 (HTML)](research/05-nvidia-fullstack/report-03-autonomous-driving-stack.html) · [7장 보고서 (HTML)](research/05-nvidia-fullstack/report-07-physical-ai-cosmos.html) · [부록 A 보고서 (HTML)](research/05-nvidia-fullstack/report-appendix-a-tier1.html) · md 원본: [3장](research/05-nvidia-fullstack/03-autonomous-driving-stack.md) · [7장](research/05-nvidia-fullstack/07-physical-ai-cosmos.md) · [부록 A](research/05-nvidia-fullstack/appendix-a-tier1-workscope.md) · [폴더 안내](research/05-nvidia-fullstack/README.md) |
| [04-flashdrive](research/04-flashdrive/) | Z Lab(UCSD)의 자율주행 VLA 추론 4.5× 가속 논문 분석 — Alpamayo 1.5를 716→159ms로 | 2026-09 | [분석 보고서](research/04-flashdrive/flashdrive_analysis.md) |
| [03-nvidia-alpamayo](research/03-nvidia-alpamayo/) | NVIDIA Alpamayo(추론형 주행 VLA)와 자율주행 패러다임 전환 — 종합·1vs2 비교·SW/HW 요구사항 | 2026-07 | [종합 보고서](research/03-nvidia-alpamayo/alpamayo_종합보고서.md) · [1 vs 2 비교](research/03-nvidia-alpamayo/alpamayo_1_vs_2_비교보고서.md) · [SW/HW 요구사항](research/03-nvidia-alpamayo/alpamayo_sw_hw_요구사항.md) |
| [02-tractus-x](research/02-tractus-x/) | Eclipse Tractus-X — Catena-X 자동차 데이터 스페이스 오픈소스 조사 | 2026-07 | [보고서](research/02-tractus-x/tractus-x-report.md) · [상세 자료집](research/02-tractus-x/tractus-x-research.md) |
| [01-liquid-ai](research/01-liquid-ai/) | Liquid AI 기업 조사 — 리퀴드 신경망 기반 엣지 AI 스타트업 | 2026-06 | [보고서](research/01-liquid-ai/liquid_ai_research.md) |
| [12-autoware-e2e-architecture](research/12-autoware-e2e-architecture/) | Autoware의 E2E/하이브리드 아키텍처 전환 2트랙 해부 — 트랙 A 로보택시(TIER IV): Architecture 1.0 고정 파이프라인 → 2.0 **Generator-Selector**로 교체, Monolithic E2E(VAD)·Modular E2E(Diffusion Planner)·MTR 실험 실패, Selector의 Safety Gate와 Trajectory Ranker 5메트릭/6구현, 메시지 정의 분기(new_planning_msgs vs internal_planning_msgs), 트랙 B 개인차량 ADAS(POV Work Group, `autoware_vision_pilot`): vision-only·mapless·저전력 엣지, AutoSeg 기반 모델(SceneSeg/Scene3D/EgoLanes)과 Lite Models 20–28× 가속(10→87–104 FPS), VisionPilot 0.9 런타임 · TIER IV 공식 발표(일본 50개 지역 실증, 도쿄·피츠버그·뮌헨 3허브) · VAD/Diffusion Planner/MTR/Bench2Drive/BEVFormer arXiv 계보 · 로컬 Autoware 1.8.0 / universe 0.51.0 코드 직접 대조, 불확실 항목 별도 명시 | 2026-06 | [보고서](research/12-autoware-e2e-architecture/autoware-e2e-architecture-transition.md) · [웹 버전](research/12-autoware-e2e-architecture/autoware-e2e-architecture-transition.html) |

각 주제 폴더 구성: 보고서 `.md`(원본) · `.html`(웹 버전, 있는 경우) · `images/`·`assets/`(그림) · `reference/`(출처·자막·원시 수집 자료).

## news — 데일리 다이제스트

| 날짜 | 문서 |
|---|---|
| 2026-06-08 | [NVIDIA 관련 5건](news/2026-06-08-nvidia.md) · [상세 HTML](news/2026-06-08-nvidia-detailed.html) |
