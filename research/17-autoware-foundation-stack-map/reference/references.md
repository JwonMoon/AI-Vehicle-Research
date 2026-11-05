# 출처 기록 — Autoware 재단 스택 지도

> **조사일**: 2026-10-30 · 3판 추가분(76~92) 2026-11-05
> **등급**: 💻 저장소 원본(raw 파일·shallow clone으로 직접 확인) · 🔍 1차 페이지(GitHub 릴리스·이슈·토론을 직접 열람) · 📰 검색 요약(원문 차단, 78번에만 사용)
> 번호는 본 보고서 [`../autoware-foundation-stack-map.md`](../autoware-foundation-stack-map.md)의 인라인 인용 번호와 일치한다.

## 수집 방법

Autoware 재단(AWF)의 GitHub 저장소·문서 원본·GitHub 1차 페이지만 사용했다. 세션 네트워크 정책으로 autoware.org, docs.autoware.org(autowarefoundation.github.io), medium.com, 언론 사이트, GitHub 조직 API에 접근할 수 없었다. 공식 문서는 `autoware-documentation` 저장소의 Markdown 원본(main, 2026-10-30)을 clone해 읽었고, 저장소 목록은 조직 페이지를 직접 열람했다. 원문으로 확인하지 못한 항목(웹 검색 요약에만 있던 언론 보도 등)과 이 저장소의 다른 보고서는 출처로 쓰지 않았다.

## 출처 목록

1. 💻 Autoware 문서 — Autoware 2.0 architecture (What 2.0.0 does today · Packages · Generator-Selector 개요) — 2026-10-29 — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/index.md
2. 💻 Autoware 문서 — Autoware Architecture: Executive Summary (Autoware 1.0 → 2.0) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/roadmap/index.md
3. 💻 Autoware 문서 — Autonomous Driving Stack Architecture (Autoware E2E Step 1~4, Figure 1~9) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/roadmap/autonomous-driving-stack-architecture.md
4. 💻 Autoware 문서 — Detailed Architectural Interface (Generator-Selector Framework) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/roadmap/detailed-architectural-interface.md
5. 💻 Autoware 문서 — Development Roadmap (본문 "TBD") — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/roadmap/development-roadmap.md
6. 💻 Autoware 문서 — Autoware concepts (Microautonomy, Core & Universe) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-concepts/index.md
7. 🔍 Autoware 문서 — Repository structure — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/repository-structure.md
8. 🔍 Autoware 문서 — repositories/*.repos files — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/repos-files.md
9. 🔍 Autoware 문서 — Versioning and release process ("Autoware 2.0.0 uses autoware_core 1.10.0") — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/versioning-and-release.md
10. 💻 Autoware 문서 — Autoware Multi-Year Roadmap (Objective 1~8, Year 1~3) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/home/roadmap/multi-year-roadmap.md
11. 💻 Autoware 문서 — Reference design (Deployment Profile + Reference Software Stack) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/index.md
12. 💻 Autoware 문서 — Autoware Index (aw-index-cli, --reference-design) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/installation/autoware/autoware-index.md
13. 💻 Autoware 문서 — Home (Autoware 2.0 release notes 배지, Validated use cases) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/home/index.md
14. 🔍 Autoware 문서 — Architecture 1.0 overview — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v1/index.md
15. 🔍 Autoware 문서 — Installation (Target platforms, Universe vs Core) — main — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/installation/index.md
16. 🔍 autoware-documentation PR #839 — docs: update the documentation for the Autoware 2.0 release — 2026-10-29 — https://github.com/autowarefoundation/autoware-documentation/pull/839
17. 💻 POV 레퍼런스 디자인 — Introduction (Vision Pilot · Plus · Pro · Vision Drive 4단계) — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/index.md
18. 💻 POV 레퍼런스 디자인 — System Configuration (프레임워크·TOPS·미들웨어) — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/system-configuration/index.md
19. 💻 POV 레퍼런스 디자인 — ODD Definition — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/odd-definition/index.md
20. 💻 POV 레퍼런스 디자인 — Hardware Configuration — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/hardware-configuration/index.md
21. 💻 POV 레퍼런스 디자인 — Software Configuration (AutoSeg 6개 모델) — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/software-configuration/index.md
22. 💻 POV 레퍼런스 디자인 — Evaluation and Testing (ADLINK AL30 · Jetson AGX Orin 벤치마크) — main — https://github.com/autowarefoundation/autoware.pov-reference-design-docs/blob/main/docs/evaluation-and-testing/index.md
23. 💻 autoware — repositories/autoware.repos 외 tools·simulator·extra-packages.repos (태그 2.0.0, 1.9.0 대조) — 2026-10 — https://github.com/autowarefoundation/autoware/blob/2.0.0/repositories/autoware.repos
24. 💻 autoware_core — README — main — https://github.com/autowarefoundation/autoware_core
25. 💻 autoware_universe — README — main — https://github.com/autowarefoundation/autoware_universe
26. 💻 openadkit — README — main — https://github.com/autowarefoundation/openadkit
27. 💻 vision_pilot — README · VisionPilot/modules 트리 — main — https://github.com/autowarefoundation/vision_pilot
28. 💻 vision_pilot — Functional_Safety/SAFETY_ELEMENT_OUT_OF_CONTEXT.md (SEooC 초안) — main — https://github.com/autowarefoundation/vision_pilot/tree/main/Functional_Safety
29. 💻 auto_steer — README (AutoSteer 2.0) — main — https://github.com/autowarefoundation/auto_steer
30. 💻 auto_speed — README (AutoSpeed) — main — https://github.com/autowarefoundation/auto_speed
31. 💻 auto_drive — README (AutoDrive) — main — https://github.com/autowarefoundation/auto_drive
32. 💻 auto_e2e — README (AutoE2E, 벤치마크 표) — main — https://github.com/autowarefoundation/auto_e2e
33. 💻 auto_e2e — ONBOARDING.md (Robotaxi work group) — main — https://github.com/autowarefoundation/auto_e2e/blob/main/ONBOARDING.md
34. 💻 autoware_latent_drive — README (LatentDrive) — main — https://github.com/autowarefoundation/autoware_latent_drive
35. 💻 autoware_oneplanner — README (OnePlanner) — main — https://github.com/autowarefoundation/autoware_oneplanner
36. 💻 autoware-safety-island — README (Zephyr/FreeRTOS, S32Z·R-Car X5H, Arm Limited 저작권 주석) — main — https://github.com/autowarefoundation/autoware-safety-island
37. 💻 RFC_L4_SafetyIslandDesign — README — main — https://github.com/autowarefoundation/RFC_L4_SafetyIslandDesign
38. 💻 autoware-index — README — main — https://github.com/autowarefoundation/autoware-index
39. 💻 aw-index-cli — README — main — https://github.com/autowarefoundation/aw-index-cli
40. 💻 autoware_system_designer — README — main — https://github.com/autowarefoundation/autoware_system_designer
41. 💻 agnocast — README — main — https://github.com/autowarefoundation/agnocast
42. 💻 cuda_blackboard — README — main — https://github.com/autowarefoundation/cuda_blackboard
43. 💻 callback_isolated_executor — README — main — https://github.com/autowarefoundation/callback_isolated_executor
44. 💻 autoware.off-road — README — main — https://github.com/autowarefoundation/autoware.off-road
45. 💻 autoware_off-road_sim — README — main — https://github.com/autowarefoundation/autoware_off-road_sim
46. 💻 autoware.trucks — README — main — https://github.com/autowarefoundation/autoware.trucks
47. 💻 alpamayo-autoware — README (Alpamayo ROS 2 노드) — main — https://github.com/autowarefoundation/alpamayo-autoware
48. 💻 domain_seg — README (DomainSeg) — main — https://github.com/autowarefoundation/domain_seg
49. 💻 autoware_simple_planning_simulator — README — main — https://github.com/autowarefoundation/autoware_simple_planning_simulator
50. 💻 autoware-projects 위키 — Home(WG 목록) · Privately Owned Vehicles · Software · Safety Assurance · Reference Design · Truck · Low Speed Autonomy WG 페이지 — 2026-10-30 — https://github.com/autowarefoundation/autoware-projects/wiki
51. 💻 autoware-harness — README — main — https://github.com/autowarefoundation/autoware-harness
52. 💻 3dgs_io — README — main — https://github.com/autowarefoundation/3dgs_io
53. 🔍 GitHub — autowarefoundation 조직 저장소 목록(6쪽, 157개) · fork:true 필터(24개) — 2026-10-30 — https://github.com/orgs/autowarefoundation/repositories
54. 🔍 GitHub Release — Autoware 2.0.0 — 2026-10-29 — https://github.com/autowarefoundation/autoware/releases/tag/2.0.0
55. 🔍 GitHub Releases — autoware 릴리스 목록(1.8.0 · 1.9.0 · 2.0.0) — 2026-10-30 — https://github.com/autowarefoundation/autoware/releases
56. 🔍 openadkit issue #91 — Open AD Kit 2026-2027 Roadmap (2026-10 갱신) — 2026-10 — https://github.com/autowarefoundation/openadkit/issues/91
57. 🔍 Discussion #6786 — Privately Owned Vehicle Work Group Meeting 2026/02/09 — 2026-02-09 — https://github.com/orgs/autowarefoundation/discussions/6786
58. 🔍 Discussion #6838 — Privately Owned Vehicle Work Group Meeting 2026/02/23 — 2026-02-23 — https://github.com/orgs/autowarefoundation/discussions/6838
59. 🔍 Discussion #7115 — Privately Owned Vehicle Work Group Meeting 2026/05/18 — 2026-05-18 — https://github.com/orgs/autowarefoundation/discussions/7115
60. 🔍 Discussion #7148 — Privately Owned Vehicle Work Group Meeting 2026/06/08 — 2026-06-08 — https://github.com/orgs/autowarefoundation/discussions/7148
61. 🔍 Discussion #7335 — ADAS Work Group Meeting 2026/09/28 — 2026-09-28 — https://github.com/orgs/autowarefoundation/discussions/7335
62. 🔍 Discussion #7341 — ADAS Work Group Meeting 2026/10/05 — 2026-10-05 — https://github.com/orgs/autowarefoundation/discussions/7341
63. 🔍 Discussion #7366 — ADAS Work Group Meeting 2026/10/19 — 2026-10-19 — https://github.com/orgs/autowarefoundation/discussions/7366
64. 🔍 Discussion #7371 — ADAS Work Group Meeting 2026/10/26 — 2026-10-26 — https://github.com/orgs/autowarefoundation/discussions/7371
65. 🔍 Discussion #7156 — Repository restructuring: Extracting shared CUDA components into core — 2026-06-11 (10월 갱신) — https://github.com/orgs/autowarefoundation/discussions/7156
66. 🔍 Discussion #7375 — Software WG Meeting 2026/10/27 — 2026-10-27 — https://github.com/orgs/autowarefoundation/discussions/7375
67. 🔍 Discussion #7358 — Reference Design WG Meeting (2026-10) — 2026-10-16 — https://github.com/orgs/autowarefoundation/discussions/7358
68. 🔍 Discussion #7357 — Open ADKit Working Group Meeting 2026/10/15 — 2026-10-15 — https://github.com/orgs/autowarefoundation/discussions/7357
69. 🔍 Discussion #7370 — Trucks WG Meeting 2026/10/22 — 2026-10-22 — https://github.com/orgs/autowarefoundation/discussions/7370
70. 🔍 autoware issue #7090 — Establish Autoware Index to federate Universe community packages — 2026-05-02 — https://github.com/autowarefoundation/autoware/issues/7090
71. 🔍 vision_pilot Releases (v0.5 · v0.9 · v1.0 · v1.1 · v1.2, 태그 커밋일 대조) — 2026-01 ~ 08 — https://github.com/autowarefoundation/vision_pilot/releases
72. 💻 autoware 태그 목록과 태그 커밋일(git ls-remote · fetch) — 2026-10-30 — https://github.com/autowarefoundation/autoware/tags
73. 🔍 Discussion #7101 — Off-road/Racing Working Group Meeting 2026/05/07 — 2026-05-07 — https://github.com/orgs/autowarefoundation/discussions/7101
74. 🔍 openadkit issue #120 — Reproduce the CES 2026 MCO/MRM edge stack on a single R-Car X5H ECU (AutoSD + FreeRTOS) — 2026-08-07 (2026-09-02 완료) — https://github.com/autowarefoundation/openadkit/issues/120
75. 💻 README가 한 줄뿐인 저장소 8개 — lite_models · scene_seg · scene_3d · ego_lanes · blindspot_detector · auto_speed_limit · vision_pilot_model_recipes · autoware_launch_v2 — 2026-10-30 — https://github.com/autowarefoundation/lite_models
76. 🔍 GitHub Discussions 인덱스(2026-10-30 ~ 11-05 게시물 6건) — 2026-11-05 — https://github.com/orgs/autowarefoundation/discussions
77. 🔍 Discussion #7388 — Software WG Meeting 2026/11/03 ("Released Autoware 2.0" 링크, docs.autoware.org, "Registered new E2E models to Autoware Index") — 2026-11-03 — https://github.com/orgs/autowarefoundation/discussions/7388
78. 📰 TIER IV 보도자료 — TIER IV spearheads Autoware 2.0 initiatives (Arm Total Design for Physical AI · AWS · Red Hat AutoSD · ASSC US 2026) — 2026-11-02 — https://tier4.co.jp/en/updates/press-release/20261102-tieriv-spearheads-autoware2.0-initiatives (PR Newswire 전재: https://www.prnewswire.com/news-releases/tier-iv-spearheads-autoware-2-0-initiatives-302925841.html) · 재단 보도자료 제목·URL: https://autoware.org/autoware-foundation-releases-autoware-2-0-to-expand-ai-support-for-open-source-autonomous-driving/
79. 🔍 Discussion #7384 — Introducing OnePlanner: End-to-End Planning from the Features of Existing Perception Models (Show and tell, Max-Bin) — 2026-11-02 — https://github.com/orgs/autowarefoundation/discussions/7384
80. 💻 autoware_oneplanner — 1.1.0 커밋(CandidateTrajectory·GeneratorInfo 채움, 방향지시등 포함) — 2026-10-30 — https://github.com/autowarefoundation/autoware_oneplanner
81. 💻 autoware README — 2.0 설계로 갱신(docs.autoware.org 안내, Autoware Index 문서 링크) — 2026-11-04 — https://github.com/autowarefoundation/autoware/pull/7389
82. 💻 autoware-documentation — 2026-10-30 ~ 11-04 머지 PR 26건(#848 도식 재작성, #849 설계 절 갱신, #858 로드맵, #864 레퍼런스 디자인, #870 CUDA 층, #877 AGENTS.md), 커밋 037c3a2 — https://github.com/autowarefoundation/autoware-documentation/pulls?q=is%3Apr+merged%3A%3E%3D2026-10-30
83. 💻 Autoware 문서 — Development roadmap(Generator-Selector 이행 Phase 0~6 상태, Step 1~4의 2.0.0 상태) — 2026-10-30 — https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/design/autoware-architecture-v2/roadmap/development-roadmap.md
84. 💻 autoware-documentation — AGENTS.md(AI 에이전트용 규칙, Zensical·llms.txt) — 2026-11-04 — https://github.com/autowarefoundation/autoware-documentation/blob/main/AGENTS.md
85. 🔍 autoware issue #7340 — Extract the shared CUDA base packages into a new autoware_cuda repository ("The cutover is done", 일자별 진행표) — 2026-10-05 ~ 11-04 — https://github.com/autowarefoundation/autoware/issues/7340
86. 💻 autoware — repositories/autoware.repos(main: core/cuda/autoware_cuda 1.0.0 · cuda_blackboard 0.5.0 · negotiated), PR #7379·#7383·#7386 — 2026-10-31 ~ 11-02 — https://github.com/autowarefoundation/autoware/blob/main/repositories/autoware.repos
87. 💻 autoware_cuda README · Autoware 문서 "The CUDA layer"(core-package-inclusion-criteria.md) — 2026-11-04 — https://github.com/autowarefoundation/autoware_cuda
88. 💻 autoware-index — distributions/jazzy.yaml(autoware_oneplanner 1.1.0 · autoware_latent_drive 1.0.1 · vision_pilot reference_design · Index 이동 패키지 5개 · tamagawa_imu_driver) — 2026-11-05 — https://github.com/autowarefoundation/autoware-index/blob/main/distributions/jazzy.yaml
89. 💻 auto_e2e — README 라이선스 절(체크포인트 CC BY-NC-SA 4.0, 코드 Apache-2.0, 11-02) · 커밋 이력(폐루프 통합 PR #177·#233 머지 11-01, 논문 초고 11-04) — https://github.com/autowarefoundation/auto_e2e
90. 💻 autoware_latent_drive — 커밋 이력(ROS 패키지 latentdrive_ros → autoware_latent_drive, 10-30) — https://github.com/autowarefoundation/autoware_latent_drive
91. 🔍 Discussion #7387 — ADAS Work Group Meeting 2026/11/02 — 2026-11-02 — https://github.com/orgs/autowarefoundation/discussions/7387
92. 🔍 Discussion #7382 — Release-to-release interface change report from interface_manifest.json(autoware_core 1.10.0부터 interface_manifest.json·RIHS01 lockfile) — 2026-11-01 — https://github.com/orgs/autowarefoundation/discussions/7382
