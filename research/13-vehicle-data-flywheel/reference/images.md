# 그림 출처 — 자율주행 데이터 플라이휠

작성일 2026-09-22(원본 그림 추가 2026-09-22). 보고서의 그림 23장 중 10장은 자체 작성 SVG, 13장은 공개 GitHub 저장소에서 내려받은 원본 그림이다. 이 세션에서는 GitHub 이외의 사이트(기업 블로그·논문 사이트)에 접근할 수 없어, 원본 그림은 **라이선스를 파일로 확인할 수 있는 GitHub 저장소**에서만 가져왔다. 기업 발표 슬라이드 화면(Tesla·Waymo·Momenta·Baidu)은 학술 서베이 저장소(Apache-2.0)에 수록된 것을 그대로 옮긴 것이며, 원 저작권은 각 회사에 있다.

자체 SVG는 폰트 폭 추정 기반 자동 줄바꿈으로 생성했고 Chromium에서 글자 넘침 0건을 확인했다. 원본 그림은 내용을 바꾸지 않고 크기만 줄이거나 JPEG로 변환했다(Chromium 렌더링으로 축소).

| 본문 번호 | 파일 | 내용 | 출처·라이선스 | 비고 |
|---|---|---|---|---|
| 그림 1 | `images/fig1-rule-vs-learned-loop.svg` | 규칙 기반 개발 루프 vs 학습 기반 개발 루프 | 자체 작성 | Tesla AI Day 2021 데이터 엔진 📰, NVIDIA data-flywheel README 🔍 (1.2·2.1절) |
| 그림 2 | `images/src-chen2024-e2e-overview.jpg` | 고전 파이프라인 vs 종단간 패러다임(서베이 개요도) | [OpenDriveLab/End-to-end-Autonomous-Driving](https://github.com/OpenDriveLab/End-to-end-Autonomous-Driving) `assets/overview.jpg` · MIT · Chen et al., TPAMI 2024(arXiv 2306.16927) | 원본 2966×1829 → 폭 1800 JPEG로 축소 |
| 그림 3 | `images/src-li2024-long-tail.png` | 주행 시나리오 롱테일 분포 | [LincanLi-X/Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) `img_resource/1-1_Long_Tail_Distribution.png` · Apache-2.0 · Li et al., arXiv 2401.12888 | 원본 5946×2452 → 폭 1600으로 축소 |
| 그림 4 | `images/src-li2024-upper-bound.png` | 고정 데이터셋의 성능 상한(개념도) | 같은 저장소 `img_resource/1-2_Illustration-of-AD-Model-Performance-Upper-Bound.png` · Apache-2.0 | 원본 3728×2482 → 폭 1400으로 축소. 개념도이며 실측 아님 |
| 그림 5 | `images/fig2-general-ai-flywheel.svg` | 일반 AI(LLM 에이전트) 데이터 플라이휠 6단계 | 자체 작성 | NVIDIA-AI-Blueprints/data-flywheel README 🔍 (2.1절) |
| 그림 6 | `images/src-nvidia-data-flywheel-blueprint-annotated.png` (원본 `images/src-nvidia-data-flywheel-blueprint.png`) | NVIDIA 데이터 플라이휠 블루프린트 구조도 + README 6단계 번호·범례(자체 표기) | [NVIDIA-AI-Blueprints/data-flywheel](https://github.com/NVIDIA-AI-Blueprints/data-flywheel) `docs/images/data-flywheel-blueprint.png` · Apache-2.0 | 원본 4008×2475 → 폭 1800으로 축소. 번호 배지·범례를 덧그린 파생본이며 원본 파일도 함께 둠 |
| 그림 7 | `images/fig3-vehicle-flywheel.svg` | 차량 데이터 플라이휠 전체 구조(9 마디) | 자체 작성 | 2.2절 표의 근거(Tesla 데이터 엔진 📰, AWS·NVIDIA AV 3.0 파이프라인 📰, 학술 서베이 7단계 🔍) |
| 그림 8 | `images/src-waymo-ml-factory-slide.jpg` | Waymo "ML Factory for Self Driving Models" 슬라이드 | Waymo 발표 슬라이드 화면. LincanLi-X 서베이 저장소 `img_resource/3-2-2_Waymo_close_loop.png`에 수록(저장소 Apache-2.0). **원 저작권 Waymo** | 원본 2184×1226 → 폭 1600 JPEG. 발표 행사·연도는 저장소에 기재 없음 ⚠️ |
| 그림 9 | `images/fig4-general-vs-vehicle.svg` | 일반 AI 플라이휠(안쪽)과 차량 플라이휠(바깥쪽) 비교 | 자체 작성 | 2.3절 표 |
| 그림 10 | `images/src-tesla-data-engine-slide.jpg` | Tesla 데이터 엔진 슬라이드 | Tesla 발표 화면(저장소는 "Tesla AutoPilot Data Platform" 강연으로 표기, [YouTube](https://www.youtube.com/watch?v=6x-Xb_uT7ts)). LincanLi-X 서베이 저장소 `img_resource/3-2-1_Tesla_close_loop.png`에 수록(저장소 Apache-2.0). **원 저작권 Tesla** | 원본 2556×1428 → 폭 1600 JPEG. 강연 연도 미확인 ⚠️ |
| 그림 11 | `images/fig5-old-vs-new-loop.svg` | 2021년 데이터 엔진 vs 2026년 플라이휠 부품 비교 | 자체 작성 | 2.4절 표 |
| 그림 12 | `images/fig6-case-flow.svg` | 가상 사례(콘 옆 작업자) 네 단계 경로 | 자체 작성 | 3.1~3.4절 |
| 그림 13 | `images/src-nvidia-cosmos-curator-pipelines.png` | Cosmos Curator 파이프라인 | [nvidia-cosmos/cosmos-curate](https://github.com/nvidia-cosmos/cosmos-curate) `docs/assets/cosmos-curator-pipelines.png` · Apache-2.0 | 원본 1900×918, 무수정 |
| 그림 14 | `images/src-li2024-labeling-pipelines.png` | 라벨링 파이프라인 세 유형(수작업·반자동·완전 자동) | LincanLi-X 서베이 저장소 `img_resource/3-5-Mainstream-AD-Labeling-Pipelines.png` · Apache-2.0 | 원본 9066×1212 → 폭 2400으로 축소. 원본에 저자 워터마크 있음 |
| 그림 15 | `images/src-waymo-3d-label-example.jpg` | Waymo Open Dataset 보행자 3D 라벨 예 | [waymo-research/waymo-open-dataset](https://github.com/waymo-research/waymo-open-dataset) `docs/images/pedestrian-3D-labeling-example.png` · 저장소 Apache-2.0(데이터 자체는 Waymo Open Dataset 이용약관) | 원본 1200×760 PNG → JPEG 변환 |
| 그림 16 | `images/fig7-synthetic-three-routes.svg` | 합성 데이터 세 갈래(재생·재구성·생성) | 자체 작성 | 3.3절 표 |
| 그림 17 | `images/src-nvidia-cosmos-transfer1.png` | Cosmos Transfer1 구조도 | [nvidia-cosmos/cosmos-transfer1](https://github.com/nvidia-cosmos/cosmos-transfer1) `assets/transfer1_diagram.png` · Apache-2.0 | 원본 1280×720, 무수정 |
| 그림 18 | `images/src-nvidia-alpamayo-rl-framework.png` | Alpamayo 강화학습 프레임워크 | [NVlabs/alpamayo-recipes](https://github.com/NVlabs/alpamayo-recipes) `recipes/alpamayo1_x_rl/assets/alpamayo_rl_framework.png` · Apache-2.0 | 원본 1024×527, 무수정 |
| 그림 19 | `images/alpasim-architecture.png` | NVIDIA AlpaSim 마이크로서비스 구조 | [NVlabs/alpasim](https://github.com/NVlabs/alpasim) `docs/assets/images/alpasim-architecture.png` · Apache-2.0 | 원본 1414×569, 무수정 |
| 그림 20 | `images/fig8-company-map.svg` | 기업별 플라이휠 유형 지도(데이터 원천 × 공개도) | 자체 작성 | 4.6절 비교표(수치는 각 사 공개 주장) |
| 그림 21 | `images/src-baidu-closed-loop.png` | Baidu 폐쇄루프 데이터 시스템 | Baidu Apollo 공개 자료. LincanLi-X 서베이 저장소 `img_resource/3-2-4_Baidu_Close_Loop_Data_System.jpg`에 수록(저장소 Apache-2.0). **원 저작권 Baidu** | 원본 1024×376, 무수정(PNG 저장). 중국어 원문 |
| 그림 22 | `images/src-momenta-roadmap-slide.jpg` | Momenta 데이터 기반 알고리즘 로드맵 슬라이드 | Momenta 발표 슬라이드 화면. LincanLi-X 서베이 저장소 `img_resource/3-1_momenta_data_driven_planning.png`에 수록(저장소 Apache-2.0). **원 저작권 Momenta** | 원본 2038×1172 → 폭 1600 JPEG. 발표 연도 미확인(내용상 2023년 전후) ⚠️ |
| 그림 23 | `images/fig9-bottleneck-to-competitiveness.svg` | 네 가지 병목 → 푸는 기술 → 다섯 가지 경쟁력 | 자체 작성 | 5.1~5.5절 |

- 도식 규약(자체 SVG): 실선 = 출처로 확인한 구조, 점선 = 추정. 파란색 = 일반 AI 플라이휠에도 있는 마디, 주황색 = 차량에서만 생기는 마디.
- 가져오지 않은 후보: Cosmos Dataset Search 구조도(NVIDIA Software License Agreement, 재배포 조건 불명확), Bench2Drive 개요도(CC BY-NC-ND 4.0), 3D Gaussian Splatting 티저(Inria 비상업 라이선스), Cosmos·InstantNuRec 데모 GIF(4~9MB, 용량).
- 접근이 차단된 사이트(nvidia.com·waymo.com·tesla.com·wayve.ai 등)의 그림은 내려받지 않았다.
