# 출처 목록 — Autoware 재단 스택 지도

> **열람일**: 2026-10-30 · ID는 [보고서](../autoware-foundation-stack-map.md)의 인용 표기와 같다.
>
> **등급**: 💻 저장소 원본(raw 파일·shallow clone 직접 확인) · 🔍 1차 페이지 직접 열람(GitHub 릴리스·이슈·토론, 웹 fetch) · 📚 이 저장소의 앞선 보고서가 직접 확인한 기록 · 📰 웹 검색 요약 · ⚠️ 추정·미확인
>
> **조사 환경 제약**: 세션 네트워크 정책으로 autoware.org · docs.autoware.org(autowarefoundation.github.io) · medium.com · api.github.com(조직 API) 접근 불가. 공식 문서는 `autoware-documentation` 저장소의 Markdown 원본(main, 2026-10-30 clone)으로 읽었다. GitHub 조직 저장소 목록은 조직 페이지 6쪽을 직접 열람했다. 그림은 각 저장소의 원본 파일을 복사했고 캡션에 경로를 적었다.

## [D] Autoware 공식 문서 원본 (`autowarefoundation/autoware-documentation`, main @ 2026-10-30)

| ID | 문서 | 경로 | 등급 |
|---|---|---|---|
| D1 | Autoware 2.0 architecture (What 2.0.0 does today · Packages 표 · Generator-Selector 개요) | docs/design/autoware-architecture-v2/index.md | 💻 |
| D2 | Autoware Architecture — Executive Summary(1.0→2.0 프레임워크) | docs/design/autoware-architecture-v2/roadmap/index.md | 💻 |
| D3 | Autonomous Driving Stack Architecture (Autoware E2E, Step 1~4, Figure 1~9) | docs/design/autoware-architecture-v2/roadmap/autonomous-driving-stack-architecture.md | 💻 |
| D4 | Detailed Architectural Interface (요구사항 3, Generator-Selector Framework, Figure 1~2) | docs/design/autoware-architecture-v2/roadmap/detailed-architectural-interface.md | 💻 |
| D5 | Development Roadmap ("TBD") | docs/design/autoware-architecture-v2/roadmap/development-roadmap.md | 💻 |
| D6 | Autoware concepts (Microautonomy, Core & Universe) | docs/design/autoware-concepts/index.md | 💻 |
| D7 | Repository structure | docs/design/repository-structure.md | 🔍(문서 저장소 페이지 열람) |
| D8 | repositories/*.repos files | docs/design/repos-files.md | 🔍 |
| D9 | Versioning and release process ("Autoware 2.0.0 uses autoware_core 1.10.0") | docs/design/versioning-and-release.md | 🔍 |
| D10 | Autoware Multi-Year Roadmap (Objective 1~8, Y1~Y3) | docs/home/roadmap/multi-year-roadmap.md | 💻 |
| D11 | Reference design (Deployment Profile + Reference Software Stack, POV·LSA·Off-road·RoboRacer·GoKart·ITRI Bus) | docs/reference-design/index.md | 💻 |
| D12 | Autoware Index 사용 안내(aw-index-cli, --reference-design) | docs/installation/autoware/autoware-index.md | 💻 |
| D13 | Home (2.0 release notes 배지, Validated use cases) | docs/home/index.md | 💻 |
| D14 | Architecture 1.0 overview | docs/design/autoware-architecture-v1/index.md | 🔍 |
| D15 | Installation (Target platforms, Universe vs Core 설치) | docs/installation/index.md | 🔍 |
| D16 | Difference from Autoware.AI and Autoware.Auto | docs/design/autoware-concepts/difference-from-ai-and-auto.md | 🔍 |
| D17 | PR #839 "docs: update the documentation for the Autoware 2.0 release" (xmfcx, 2026-10-29 머지) | https://github.com/autowarefoundation/autoware-documentation/pull/839 | 🔍 |
| D-nav | 네비게이션 파일 | docs/.nav.yml, docs/design/.nav.yml, docs/design/autoware-architecture-v2/roadmap/.nav.yml | 💻 |

## [P] POV 레퍼런스 디자인 문서 (`autowarefoundation/autoware.pov-reference-design-docs`, main @ 2026-10-30)

| ID | 문서 | 경로 | 등급 |
|---|---|---|---|
| P1 | Introduction (4 Phase 정의) | docs/index.md | 💻 |
| P2 | System Configuration (프레임워크, TOPS 요구, 미들웨어) | docs/system-configuration/index.md | 💻 |
| P3 | ODD Definition (Vision Pilot/Plus/Pro/Vision Drive) | docs/odd-definition/index.md | 💻 |
| P4 | Hardware Configuration (Phase별 센서) | docs/hardware-configuration/index.md, ECUs/ | 💻 |
| P5 | Software Configuration (AutoSeg 6 모델, ROS 2/Zenoh) | docs/software-configuration/index.md | 💻 |
| P6 | Evaluation and Testing (ADLINK AL30·Jetson AGX Orin·Advantech 벤치마크) | docs/evaluation-and-testing/index.md | 💻 |

## [R] 저장소 README·매니페스트 (raw.githubusercontent.com 또는 shallow clone, 2026-10-30)

| ID | 저장소·파일 | 등급 |
|---|---|---|
| R1 | autoware — repositories/autoware.repos·extra-packages.repos·tools.repos·simulator.repos (main, 태그 2.0.0·1.9.0 대조) | 💻 |
| R2 | autoware README | 💻 |
| R3 | autoware_core README | 💻 |
| R4 | autoware_universe README | 💻 |
| R5 | openadkit README | 💻 |
| R6 | vision_pilot README · Functional_Safety/(SAFETY_PLAN, SAFETY_ELEMENT_OUT_OF_CONTEXT, SAFETY_METRICS, SOFTWARE_REQUIREMENTS) · VisionPilot/modules 트리 · Media/ | 💻 |
| R7 | auto_steer README | 💻 |
| R8 | auto_speed README | 💻 |
| R9 | auto_drive README | 💻 |
| R10 | auto_e2e README · ONBOARDING.md · Media/ · 디렉터리 트리(Design·Docs·Platform·Safety) | 💻 |
| R11 | autoware_latent_drive README · docs/ | 💻 |
| R12 | autoware_oneplanner README · media/ | 💻 |
| R13 | autoware-safety-island README | 💻 |
| R14 | RFC_L4_SafetyIslandDesign README | 💻 |
| R15 | autoware-index README | 💻 |
| R16 | aw-index-cli README | 💻 |
| R17 | autoware_system_designer README · doc/images/node_diagram.png | 💻 |
| R18 | autoware-harness README | 💻 |
| R19 | agnocast README | 💻 |
| R20 | cuda_blackboard README | 💻 |
| R21 | callback_isolated_executor README | 💻 |
| R22 | autoware.off-road README | 💻 |
| R23 | autoware_off-road_sim README | 💻 |
| R24 | autoware.trucks README | 💻 |
| R25 | 3dgs_io README | 💻 |
| R26 | alpamayo-autoware README | 💻 |
| R27 | domain_seg README | 💻 |
| R28 | autoware_simple_planning_simulator README | 💻 |
| R29 | autoware-repos-visualizer README | 💻 |
| R30 | 한 줄 README 저장소: lite_models · scene_seg · scene_3d · ego_lanes · blindspot_detector · auto_speed_limit · vision_pilot_model_recipes · autoware_launch_v2 | 💻 |
| R31 | autoware-projects 위키: Home(WG 목록) · Privately-Owned-Vehicles-Working-Group · Software-Working-Group · Autoware-Safety-Assurance-Working-Group · Autoware-Reference-Design-Working-Group · Truck-Working-Group · Low-Speed-Autonomy-Working-Group | 💻 |
| R32 | carla-agent-controller README | 💻 |

## [G] GitHub 1차 페이지 (웹 fetch, 2026-10-30)

| ID | 페이지 | URL | 등급 |
|---|---|---|---|
| G1 | autowarefoundation 조직 저장소 목록(6쪽, 157개) + fork:true 필터(24개) | https://github.com/orgs/autowarefoundation/repositories | 🔍 |
| G2 | Release 2.0.0 (2026-10-29) | https://github.com/autowarefoundation/autoware/releases/tag/2.0.0 | 🔍 |
| G3 | Releases 목록(1.8.0 05-04, 1.9.0 07-16, 2.0.0 10-29) | https://github.com/autowarefoundation/autoware/releases | 🔍 |
| G4 | Open AD Kit 2026-2027 Roadmap (issue #91, 2026-10 갱신) | https://github.com/autowarefoundation/openadkit/issues/91 | 🔍 |
| G5 | POV WG Meeting 2026/02/09 (#6786) | https://github.com/orgs/autowarefoundation/discussions/6786 | 🔍 |
| G6 | POV WG Meeting 2026/02/23 (#6838) | https://github.com/orgs/autowarefoundation/discussions/6838 | 🔍 |
| G7 | POV WG Meeting 2026/05/18 (#7115) | https://github.com/orgs/autowarefoundation/discussions/7115 | 🔍 |
| G8 | POV WG Meeting 2026/06/08 (#7148) | https://github.com/orgs/autowarefoundation/discussions/7148 | 🔍 |
| G9 | Discussions 인덱스(카테고리·최근 제목) | https://github.com/orgs/autowarefoundation/discussions | 🔍 |
| G10 | ADAS WG Meeting 2026/09/28 (#7335) | https://github.com/orgs/autowarefoundation/discussions/7335 | 🔍 |
| G11 | ADAS WG Meeting 2026/10/05 (#7341) | https://github.com/orgs/autowarefoundation/discussions/7341 | 🔍 |
| G12 | ADAS WG Meeting 2026/10/19 (#7366) | https://github.com/orgs/autowarefoundation/discussions/7366 | 🔍 |
| G13 | ADAS WG Meeting 2026/10/26 (#7371) | https://github.com/orgs/autowarefoundation/discussions/7371 | 🔍 |
| G14 | Repository restructuring: Extracting shared CUDA components into core (#7156, 2026-06-11, 10월 갱신) | https://github.com/orgs/autowarefoundation/discussions/7156 | 🔍 |
| G15 | Software WG Meeting 2026/10/27 (#7375) | https://github.com/orgs/autowarefoundation/discussions/7375 | 🔍 |
| G16 | Reference Design WG Meeting 2026-10 (#7358) | https://github.com/orgs/autowarefoundation/discussions/7358 | 🔍 |
| G17 | Open ADKit WG Meeting 2026/10/15 (#7357) | https://github.com/orgs/autowarefoundation/discussions/7357 | 🔍 |
| G18 | Trucks WG Meeting 2026/10/22 (#7370) | https://github.com/orgs/autowarefoundation/discussions/7370 | 🔍 |
| G19 | Establish Autoware Index to federate Universe community packages (autoware#7090, 2026-05-02) | https://github.com/autowarefoundation/autoware/issues/7090 | 🔍 |
| G20 | vision_pilot Releases (1.2·1.1·1.0·0.9·0.5) | https://github.com/autowarefoundation/vision_pilot/releases | 🔍 |
| G21 | autoware 태그 목록과 태그 커밋 날짜(git ls-remote·shallow fetch) | https://github.com/autowarefoundation/autoware/tags | 💻 |

## [W] 웹 검색 요약

| ID | 내용 | URL | 등급 |
|---|---|---|---|
| W1 | TIER IV at Automotive World 2026: Vision Pilot(L2) + Renesas R-Car X5H, 레퍼런스 모델 Jetson Orin | https://www.automotiveworld.com/news/tier-iv-at-automotive-world-2026-with-adas-and-ai-demos/ | 📰 |
| W2 | autoware.org "Real-World E2E Model Validation with BrightDrive"(제목·요지만) | https://autoware.org/real-world-e2e-model-validation-with-brightdrive/ | 📰 |
| W3 | Off-road/Racing WG Meeting 2026/05/07 "일시 중단" (#7101) | https://github.com/orgs/autowarefoundation/discussions/7101 | 📰 |

## [📚] 이 저장소의 앞선 보고서

| 보고서 | 활용 |
|---|---|
| [12-autoware-e2e-architecture](../../12-autoware-e2e-architecture/autoware-e2e-architecture-transition.md) (2026-06, Autoware 1.8.0) | Generator-Selector 초기 상태, VisionPilot 0.9·Lite 모델 20–28× 가속, 옛 POV 4단계 명칭 |
| [09-ad-sw-stack-deep-dive](../../09-ad-sw-stack-deep-dive/ad-sw-stack-deep-dive.md) | Agnocast·cuda_blackboard 데이터 흐름 |
| [07-tier4-alpamayo-autoware](../../07-tier4-alpamayo-autoware/tier4_alpamayo_autoware_보고서.md), [14-alpamayo-hardware-alternatives](../../14-alpamayo-hardware-alternatives/alpamayo-hardware-alternatives.md) | alpamayo-autoware 포크 상세·성능 |
| [15-etas-elektrobit-partnership](../../15-etas-elektrobit-partnership/etas-elektrobit-partnership.md) | 안전 OS·미들웨어 층 비교 |
