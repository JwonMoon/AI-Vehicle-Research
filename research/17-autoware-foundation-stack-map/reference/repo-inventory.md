# autowarefoundation 저장소 전수 목록 (157개)

> **수집일**: 2026-10-30 · **출처**: GitHub 조직 페이지(https://github.com/orgs/autowarefoundation/repositories, 6쪽, 157개 표기)와 `fork:true` 필터(24개), 각 저장소 README.
> - 분류(A~J)는 이 보고서의 정리 기준이다.
> - 별·포크 수는 목록 페이지 표기(1,000 이상은 k 단위 반올림)다.
> - '최근 갱신'은 목록의 Updated 날짜다. '활성'은 2026년 갱신, '휴면'은 2025년 이전이 마지막 갱신이다.

## 분류별 개수

| 분류 | 개수 |
|---|---|
| A. 메타·핵심 — Autoware 2.0.0 워크스페이스를 이루는 저장소 | 17 |
| B. 로보택시·L4 트랙 — E2E 모델과 런타임 | 6 |
| C. ADAS·POV 트랙 — Vision Pilot 계열 | 13 |
| D. 미들웨어·실행 기반·GPU 가속 | 14 |
| E. 배포·안전 — Open AD Kit·Safety Island | 6 |
| F. 패키지 레지스트리·개발 인프라·도구 | 19 |
| G. 시뮬레이션·평가·데이터 | 19 |
| H. ODD별 프로젝트·레퍼런스 디자인·WG 운영 | 22 |
| I. 센서·차량 드라이버와 Index로 옮겨간 소형 패키지 | 10 |
| J. 레거시·아카이브·포크·벤더 패키지 | 31 |
| **합계** | **157** (아카이브 27, 포크 24) |

## A. 메타·핵심 — Autoware 2.0.0 워크스페이스를 이루는 저장소

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [autoware](https://github.com/autowarefoundation/autoware) | 메타 저장소. 소스 코드는 없고 repositories/*.repos 로 하위 저장소 버전을 고정, Docker·Ansible 설치 스크립트 보유 | 12k / 3.7k | 2026-10-29 | 활성 | 2.0.0 (2026-10-29 공개) |
| [autoware_core](https://github.com/autowarefoundation/autoware_core) | AWF가 직접 유지하는 고품질·안정 패키지(sensing·perception·localization·planning·control·map·API) | 191 / 175 | 2026-10-29 | 활성 | 1.10.0이 Autoware 2.0.0에 고정 |
| [autoware_universe](https://github.com/autowarefoundation/autoware_universe) | 커뮤니티 확장 패키지 모음(241개 패키지). Diffusion Planner·trajectory selector·VAD 등 E2E 부품도 여기 | 1.8k / 979 | 2026-10-29 | 활성 | 0.53.1이 2.0.0에 고정. Index로 분산 중 |
| [autoware_lanelet2_extension](https://github.com/autowarefoundation/autoware_lanelet2_extension) | Lanelet2 HD맵 확장 라이브러리 | 8 / 43 | 2026-10-29 | 활성 | 1.3.0 |
| [autoware_rviz_plugins](https://github.com/autowarefoundation/autoware_rviz_plugins) | RViz 플러그인 | 8 / 24 | 2026-10-29 | 활성 | 0.6.0. 추가 플러그인은 Index의 autoware_extra_rviz_plugins로 분리 제안 중 |
| [autoware_tools](https://github.com/autowarefoundation/autoware_tools) | 개발·평가 도구(주행 중 실행하지 않는 것들). tools.repos로 별도 체크아웃 | 39 / 72 | 2026-10-29 | 활성 | 0.8.0 |
| [autoware_system_designer](https://github.com/autowarefoundation/autoware_system_designer) | YAML로 노드·모듈·시스템을 기술하면 ROS 2 런치·다이어그램·파라미터 템플릿을 생성하는 툴체인 | 5 / 4 | 2026-10-29 | 활성 | v0.4.2, core 그룹에 포함 |
| [autoware-documentation](https://github.com/autowarefoundation/autoware-documentation) | 공식 문서 원본(MkDocs). Architecture 2.0·Index·Reference Design 문서가 여기 | 135 / 180 | 2026-10-29 | 활성 | 2.0 반영 PR #839 2026-10-29 머지 |
| [autoware_simple_planning_simulator](https://github.com/autowarefoundation/autoware_simple_planning_simulator) | Universe에서 옮겨온 단독 planning simulator(+dummy perception, learning-based vehicle model) | 1 / 7 | 2026-10-27 | 활성 | 1.1.0, core 그룹 |
| [autoware_launch](https://github.com/autowarefoundation/autoware_launch) | 런치 파일·파라미터. planning_setting 인자(rule_based/diffusion_planner)가 여기 정의 | 60 / 495 | 2026-10-26 | 활성 | 0.53.0 |
| [autoware_cmake](https://github.com/autowarefoundation/autoware_cmake) | 공통 CMake 매크로 | 2 / 25 | 2026-10-21 | 활성 | 1.4.0 |
| [autoware_utils](https://github.com/autowarefoundation/autoware_utils) | C++ 공통 유틸(math·geometry·system 등 서브패키지) | 8 / 51 | 2026-10-21 | 활성 | 1.11.0 |
| [autoware_msgs](https://github.com/autowarefoundation/autoware_msgs) | 컴포넌트 간(inter-component) 메시지 정의(perception→planning 등). 시뮬레이터 연동에도 사용 | 42 / 75 | 2026-10-12 | 활성 | 1.13.0 |
| [autoware_internal_msgs](https://github.com/autowarefoundation/autoware_internal_msgs) | 컴포넌트 내부(intra-component) 메시지. CandidateTrajectories 등 Generator-Selector 메시지 포함 | 2 / 40 | 2026-10-12 | 활성 | 1.16.0 |
| [autoware_adapi_msgs](https://github.com/autowarefoundation/autoware_adapi_msgs) | 외부 시스템(HMI·원격·플릿) 용 AD API 메시지 | 7 / 39 | 2026-10-12 | 활성 | 1.9.2 |
| [autoware_cuda](https://github.com/autowarefoundation/autoware_cuda) | CUDA and TensorRT base packages for Autoware Core(조직 페이지 설명). Universe CUDA 공통 패키지 이동 대상 | 0 / 0 | 2026-10-05 | 활성 | 전환 목표일 2026-10-15 |
| [autoware_launch_v2](https://github.com/autowarefoundation/autoware_launch_v2) | README 제목만 있는 저장소(설명 없음) | 0 / 2 | 2026-03-31 | 활성 |  |

## B. 로보택시·L4 트랙 — E2E 모델과 런타임

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [auto_e2e](https://github.com/autowarefoundation/auto_e2e) | AWF 자체 E2E 주행 모델(AutoE2E). 서라운드 6카메라→BEV→GRU 플래너, 79.9M 파라미터, 10 Hz, 6.4 s 궤적. 로보택시 WG 개발 | 183 / 35 | 2026-10-30 | 활성 | HF에 v1.0 체크포인트. 2026 최신 활동 |
| [autoware_latent_drive](https://github.com/autowarefoundation/autoware_latent_drive) | LatentDrive: V-JEPA 잠재 월드모델 위의 카메라 전용 E2E 플래너 TensorRT C++ 런타임 + ROS 2 재생 노드 | 0 / 1 | 2026-10-30 | 활성 | 연구용, 공도 제어 금지 명시 |
| [autoware_oneplanner](https://github.com/autowarefoundation/autoware_oneplanner) | OnePlanner: LiDAR BEV(BEVFusion-L 백본)+벡터맵+신호등 → 궤적. Autoware Core 위에서 TensorRT로 LiDAR 주기 실행 | 1 / 0 | 2026-10-28 | 활성 | RTX PRO 6000에서 p50 12.7 ms |
| [3dgs_io](https://github.com/autowarefoundation/3dgs_io) | 3D Gaussian Splatting 장면(glTF·3D Tiles·SPZ)+Autoware 맵 번들 I/O 라이브러리. alpasim ENU 월드 프레임 사용 | 1 / 4 | 2026-10-27 | 활성 |  |
| [alpamayo-autoware](https://github.com/autowarefoundation/alpamayo-autoware) | NVIDIA Alpamayo 1.5·2 Super VLA를 Autoware ROS 2 노드로 돌리는 포크(TIER IV 기원) | 143 / 347 | 2026-08-06 | 포크 | NVIDIA GPU 24 GB+ VRAM 권장 |
| [modelzoo](https://github.com/autowarefoundation/modelzoo) | 머신러닝 모델 모음(2023년 이후 갱신 없음) | 63 / 22 | 2023-02-06 | 휴면 | 비활성 |

## C. ADAS·POV 트랙 — Vision Pilot 계열

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [auto_steer](https://github.com/autowarefoundation/auto_steer) | AutoSteer 2.0: 카메라 프레임→자차 미래 경로 웨이포인트(차선 검출 없이 E2E). Vision Pilot 횡방향 모델 | 9 / 4 | 2026-10-30 | 활성 | mAP@50 0.969, INT8 ONNX 제공 |
| [vision_pilot](https://github.com/autowarefoundation/vision_pilot) | 오픈소스 L2 ADAS 스택(ACC·FCW·AEB·LKAS·LDW·ISA·단일차로 오토파일럿). 단안 카메라 1대, HD맵 불필요, 하이브리드 E2E | 921 / 195 | 2026-10-19 | 활성 | v1.2(2026-08-10). 옛 이름 autoware.privately-owned-vehicles·autoware_vision_pilot 주소가 같은 저장소로 연결 |
| [auto_speed_limit](https://github.com/autowarefoundation/auto_speed_limit) | 속도제한 표지 검출·인식 모델(ISA용) | 2 / 0 | 2026-10-08 | 활성 | README 한 줄 |
| [blindspot_detector](https://github.com/autowarefoundation/blindspot_detector) | 측면 어안 카메라 사각지대 점유 검출 모델 | 4 / 1 | 2026-10-06 | 활성 | README 한 줄 |
| [ego_lanes](https://github.com/autowarefoundation/ego_lanes) | EgoLanes: 차선·도로 경계 분할·분류(AutoSeg 계열). Vision Pilot 0.5의 조향 입력 | 1 / 0 | 2026-09-10 | 활성 | 설명 잘림 |
| [domain_seg](https://github.com/autowarefoundation/domain_seg) | DomainSeg: 공사구간·로드워크 객체 분할(AutoSeg 계열). ROADWork 데이터셋 mIoU 46.6 | 3 / 1 | 2026-09-09 | 활성 | RTX3060 FP16 23.9 FPS |
| [auto_drive](https://github.com/autowarefoundation/auto_drive) | AutoDrive: 연속 2프레임→CIPO 거리·도로 곡률·CIPO 존재 확률을 내는 소형 E2E 모델 | 10 / 4 | 2026-07-28 | 활성 | Vision Pilot 1.0의 'E2E' 축 |
| [auto_speed](https://github.com/autowarefoundation/auto_speed) | AutoSpeed: YOLOv11 변형의 경로 내 객체(CIPO) 검출기. ACC·FCW·AEB용 종방향 모델 | 8 / 5 | 2026-07-08 | 활성 | AutoSpeed 2.0 권장 |
| [vision_pilot_model_recipes](https://github.com/autowarefoundation/vision_pilot_model_recipes) | Vision Pilot 모델의 추론·컨테이너·미들웨어 레시피 | 2 / 2 | 2026-06-15 | 활성 | README 한 줄 |
| [scene_seg](https://github.com/autowarefoundation/scene_seg) | SceneSeg: 전경 객체 시맨틱 분할(AutoSeg 계열) | 1 / 0 | 2026-06-09 | 활성 | README 한 줄 |
| [scene_3d](https://github.com/autowarefoundation/scene_3d) | Scene3D: 단안 깊이 추정(AutoSeg 계열) | 2 / 1 | 2026-06-09 | 활성 | README 한 줄 |
| [lite_models](https://github.com/autowarefoundation/lite_models) | 제약 장치용 경량 모델 패밀리(SceneSeg·Scene3D·EgoLanes Lite) | 2 / 0 | 2026-06-09 | 활성 | README 한 줄 |
| [autoware.pov-reference-design-docs](https://github.com/autowarefoundation/autoware.pov-reference-design-docs) | 개인차량(PoV) 레퍼런스 디자인 가이드(MkDocs): Vision Pilot→Plus→Pro→Vision Drive 4단계, ODD·센서·ECU·벤치마크 | 0 / 5 | 2025-12-23 | 휴면 | 2025-09 기준 작성 |

## D. 미들웨어·실행 기반·GPU 가속

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [agnocast](https://github.com/autowarefoundation/agnocast) | rclcpp 호환 진정한 제로카피 IPC(모든 ROS 메시지 타입). Autoware 2.0.0에 소스 빌드로 포함 | 211 / 37 | 2026-10-27 | 활성 | 2.4.1이 Autoware 2.0.0에 소스 빌드로 고정 |
| [callback_isolated_executor](https://github.com/autowarefoundation/callback_isolated_executor) | 콜백 그룹마다 전용 스레드를 주는 컴포넌트 컨테이너·Executor. Agnocast에 통합 | 79 / 12 | 2026-10-27 | 활성 | RTAS 2025 논문 |
| [cuda_blackboard](https://github.com/autowarefoundation/cuda_blackboard) | REP-2007/2009 타입 적응·협상으로 GPU 메모리를 노드 간 복사 없이 공유 | 25 / 15 | 2026-10-27 | 활성 | 0.4.0. universe/external→core/cuda로 이동 예정 |
| [negotiated](https://github.com/autowarefoundation/negotiated) | ROS 2 타입 협상(REP-2009) 포크(osrf) | 0 / 4 | 2026-10-21 | 포크 | autoware.repos는 osrf 원본 커밋을 고정 |
| [agnocast_doc](https://github.com/autowarefoundation/agnocast_doc) | Agnocast 문서 사이트 | 1 / 5 | 2026-10-20 | 활성 |  |
| [callback_isolated_executor_doc](https://github.com/autowarefoundation/callback_isolated_executor_doc) | 위 문서 사이트 | 0 / 1 | 2026-10-20 | 활성 |  |
| [managed_transform_buffer](https://github.com/autowarefoundation/managed_transform_buffer) | TF 버퍼 관리 라이브러리 | 7 / 9 | 2026-09-22 | 활성 | 0.3.0 |
| [ros2_socketcan](https://github.com/autowarefoundation/ros2_socketcan) | Linux SocketCAN ROS 2 래퍼(Continental 호환 버전) | 197 / 106 | 2026-09-07 | 활성 |  |
| [bevdet_vendor](https://github.com/autowarefoundation/bevdet_vendor) | BEVDet TensorRT C++ 구현 벤더 패키지(Orin 실시간) | 9 / 59 | 2026-09-01 | 포크 | 0.2.1 |
| [transport_drivers](https://github.com/autowarefoundation/transport_drivers) | 전송 계층 드라이버 포크(복사 감소 버전) | 1 / 89 | 2026-06-10 | 포크 |  |
| [cyclonedds](https://github.com/autowarefoundation/cyclonedds) | Eclipse Cyclone DDS 포크. Safety Island용 0.11.0 AWF 포크 | 0 / 487 | 2026-06-01 | 포크 |  |
| [spconv_cpp](https://github.com/autowarefoundation/spconv_cpp) | 희소 컨볼루션(spconv/cumm) C++ 라이브러리. OnePlanner·BEVFusion 의존 | 25 / 10 | 2026-05-26 | 활성 |  |
| [agnocast_ci_test](https://github.com/autowarefoundation/agnocast_ci_test) | 이관 전 CI 테스트용 복사본 | 1 / 0 | 2026-02-18 | 아카이브 | 아카이브 |
| [trt_batched_nms](https://github.com/autowarefoundation/trt_batched_nms) | TensorRT batched NMS 플러그인 ROS 2 패키지 | 4 / 6 | 2026-01-22 | 활성 | CUDA 재구조화에서 제외 |

## E. 배포·안전 — Open AD Kit·Safety Island

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [open-ad-kit-docs](https://github.com/autowarefoundation/open-ad-kit-docs) | Open AD Kit 문서(MkDocs) | 13 / 12 | 2026-10-26 | 활성 |  |
| [RFC_L4_SafetyIslandDesign](https://github.com/autowarefoundation/RFC_L4_SafetyIslandDesign) | L4 Safety Island 설계 RFC·설계 문서·슬라이드(NTU Reference Design WG) | 1 / 0 | 2026-10-24 | 활성 | HPC/안전섬 노드 분할 논의 중 |
| [autoware-safety-island](https://github.com/autowarefoundation/autoware-safety-island) | Arm 안전 코어(Cortex-R52 등)에서 Autoware 궤적 추종기(MPC+PID)를 Zephyr/FreeRTOS로 돌리고 DDS로 교환. S32Z·R-Car X5H 타깃 | 7 / 5 | 2026-10-20 | 활성 | README 원본에 Arm Limited 저작권 주석. L2 Safety Island 실험(2026-10) |
| [openadkit](https://github.com/autowarefoundation/openadkit) | Open AD Kit: Autoware·Vision Pilot·Safety Island를 컨테이너·증거(evidence) 기반으로 배포하는 SOAFEE 블루프린트 CLI·이미지·번들 | 12 / 12 | 2026-10-19 | 활성 | v2.0.0 2026-10 말 목표(10-15 회의 '리스크'), v2.1에 Vision Pilot |
| [openadkit_demo](https://github.com/autowarefoundation/openadkit_demo) | 옛 Open AD Kit 데모 아카이브 | 6 / 3.7k | 2025-11-14 | 아카이브·포크 | 아카이브 |
| [open_ad_kit](https://github.com/autowarefoundation/open_ad_kit) | 초기 Open AD Kit 포크 | 5 / 6 | 2023-12-21 | 포크 | 비활성 |

## F. 패키지 레지스트리·개발 인프라·도구

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [autoware-index](https://github.com/autowarefoundation/autoware-index) | Autoware Index: 커뮤니티 패키지 레지스트리(distribution.yaml)+최신 릴리스 대상 빌드·테스트 이력. index.autoware.org | 0 / 1 | 2026-10-29 | 활성 | 2.0.0 릴리스 노트 항목 |
| [autoware-repos-visualizer](https://github.com/autowarefoundation/autoware-repos-visualizer) | 릴리스별 autoware.repos 핀 이력을 스윔레인으로 보여주는 웹 시각화 | 1 / 1 | 2026-10-29 | 활성 |  |
| [autoware-ci-metrics](https://github.com/autowarefoundation/autoware-ci-metrics) | CI 빌드 시간·이미지 크기 대시보드 | 7 / 3 | 2026-10-29 | 활성 |  |
| [autoware-spell-check-dict](https://github.com/autowarefoundation/autoware-spell-check-dict) | 스펠체크 사전 | 2 / 10 | 2026-10-29 | 활성 |  |
| [autoware-harness](https://github.com/autowarefoundation/autoware-harness) | 코딩 에이전트용 Autoware 스킬·에이전트·MCP 묶음(Claude Code·Codex·Cursor 플러그인) | 4 / 2 | 2026-10-27 | 활성 | 2026 신규 |
| [autoware-github-actions](https://github.com/autowarefoundation/autoware-github-actions) | 공용 GitHub Actions | 26 / 34 | 2026-10-26 | 활성 |  |
| [.github](https://github.com/autowarefoundation/.github) | 조직 프로필·공용 템플릿 | 1 / 1 | 2026-10-26 | 활성 |  |
| [aw-index-cli](https://github.com/autowarefoundation/aw-index-cli) | Index 소비 CLI: compose(.repos 생성)·check·list. --reference-design 옵션 | 0 / 1 | 2026-10-20 | 활성 | pipx 배포 |
| [autoware-contributor-metrics](https://github.com/autowarefoundation/autoware-contributor-metrics) | 기여자 통계 | 3 / 2 | 2026-10-20 | 활성 |  |
| [colcon-dashboard](https://github.com/autowarefoundation/colcon-dashboard) | colcon 빌드 실시간 웹 대시보드 | 0 / 1 | 2026-10-20 | 활성 | 2026 신규 |
| [sync-file-templates](https://github.com/autowarefoundation/sync-file-templates) | 저장소 공통 파일 템플릿 동기화 | 2 / 8 | 2026-10-20 | 활성 |  |
| [autoware-github-runner-ansible](https://github.com/autowarefoundation/autoware-github-runner-ansible) | 셀프호스트 러너 Ansible | 3 / 1 | 2026-10-05 | 활성 |  |
| [autoware-index-github-actions](https://github.com/autowarefoundation/autoware-index-github-actions) | Index 등록 패키지가 호출하는 재사용 워크플로(validate-package 등) | 0 / 1 | 2026-09-30 | 활성 |  |
| [autoware-deb-packages](https://github.com/autowarefoundation/autoware-deb-packages) | Debian 패키징(아카이브) | 0 / 0 | 2026-08-06 | 아카이브 | 아카이브 |
| [autowarefoundation.github.io](https://github.com/autowarefoundation/autowarefoundation.github.io) | autoware.universe→autoware_universe 문서 리다이렉트 | 1 / 1 | 2026-07-08 | 활성 |  |
| [autoware-guideline-check](https://github.com/autowarefoundation/autoware-guideline-check) | 가이드라인 검사기 | 1 / 1 | 2026-03-27 | 활성 |  |
| [autoware_dummy_repository](https://github.com/autowarefoundation/autoware_dummy_repository) | 릴리스 프로세스 테스트용 더미 | 2 / 2 | 2025-06-18 | 휴면 |  |
| [autoware-launch-gui](https://github.com/autowarefoundation/autoware-launch-gui) | Tauri/Next.js 런치 GUI | 36 / 4 | 2024-08-12 | 휴면 | 비활성 |
| [autoware-build-gui](https://github.com/autowarefoundation/autoware-build-gui) | 빌드 GUI | 22 / 6 | 2024-06-11 | 휴면 | 비활성 |

## G. 시뮬레이션·평가·데이터

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [autoware_carla_scenario](https://github.com/autowarefoundation/autoware_carla_scenario) | CARLA 시나리오(설명 없음) | 0 / 1 | 2026-10-30 | 활성 |  |
| [odd-usecase-scenario](https://github.com/autowarefoundation/odd-usecase-scenario) | ODD 유스케이스·시나리오 자연어 기술(ODD WG) | 8 / 3 | 2026-10-27 | 활성 |  |
| [AWSIM](https://github.com/autowarefoundation/AWSIM) | 오픈소스 디지털 트윈 시뮬레이터 | 758 / 161 | 2026-10-20 | 활성 |  |
| [autoware_lanelet2_to_opendrive](https://github.com/autowarefoundation/autoware_lanelet2_to_opendrive) | Lanelet2 맵→OpenDRIVE 변환(CARLA 등 시뮬 연동용) | 0 / 2 | 2026-10-20 | 활성 |  |
| [lanelet2_to_sumo](https://github.com/autowarefoundation/lanelet2_to_sumo) | Lanelet2 맵→SUMO 변환 | 1 / 2 | 2026-09-17 | 활성 |  |
| [TeraSim](https://github.com/autowarefoundation/TeraSim) | 생성형 시뮬로 미지의 위험 이벤트 탐색(포크) | 0 / 29 | 2026-09-16 | 포크 |  |
| [carla-autoware-extension](https://github.com/autowarefoundation/carla-autoware-extension) | CARLA 확장(아카이브) | 3 / 0 | 2026-09-05 | 아카이브 | 아카이브 |
| [autoware_msg_bag_converter](https://github.com/autowarefoundation/autoware_msg_bag_converter) | rosbag 메시지 변환기 | 1 / 1 | 2026-07-10 | 포크 |  |
| [autoware_off-road_sim](https://github.com/autowarefoundation/autoware_off-road_sim) | NVIDIA Isaac Sim 기반 오프로드·RoboRacer 다차량 시뮬레이터(UPenn CoE) | 15 / 7 | 2026-06-25 | 활성 |  |
| [autoware_sample_scenarios](https://github.com/autowarefoundation/autoware_sample_scenarios) | 샘플 시나리오 | 0 / 0 | 2026-05-03 | 활성 |  |
| [custom_dataset_composer](https://github.com/autowarefoundation/custom_dataset_composer) | 데이터셋 구성 도구(아카이브) | 1 / 1 | 2026-04-06 | 아카이브 | 아카이브 |
| [carla-agent-controller](https://github.com/autowarefoundation/carla-agent-controller) | Autoware planning simulator의 더미 객체·신호등을 CARLA 에이전트와 동기화하는 ROS 2 브리지(TIER IV 기원) | 6 / 1 | 2026-04-03 | 활성 |  |
| [carla-scenario-database](https://github.com/autowarefoundation/carla-scenario-database) | CARLA 시나리오 DB(설명 없음) | 0 / 0 | 2026-03-18 | 활성 |  |
| [carla](https://github.com/autowarefoundation/carla) | CARLA 시뮬레이터 포크 | 1 / 4.7k | 2026-03-10 | 포크 |  |
| [AWSIM-Labs](https://github.com/autowarefoundation/AWSIM-Labs) | AWSIM 커뮤니티 포크(아카이브) | 45 / 161 | 2026-01-11 | 아카이브·포크 | 아카이브 |
| [2025-Autoware-scenario-running-on-CARLA](https://github.com/autowarefoundation/2025-Autoware-scenario-running-on-CARLA) | scenario_simulator_v2 시나리오를 CARLA에서 돌리는 TIER IV 프로젝트 | 0 / 1 | 2025-08-04 | 포크 |  |
| [autoware_rosbag2_anonymizer](https://github.com/autowarefoundation/autoware_rosbag2_anonymizer) | rosbag 익명화 도구 | 13 / 9 | 2025-01-09 | 포크 |  |
| [scenario-simulator-failure-evaluation-tool](https://github.com/autowarefoundation/scenario-simulator-failure-evaluation-tool) | 시나리오 실패를 일으킨 커밋 탐색 도구 | 5 / 1 | 2023-11-30 | 휴면 | 비활성 |
| [perception_benchmark_tool](https://github.com/autowarefoundation/perception_benchmark_tool) | 인식 벤치마크 도구 | 1 / 2 | 2023-03-21 | 휴면 | 비활성 |

## H. ODD별 프로젝트·레퍼런스 디자인·WG 운영

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [autoware.off-road](https://github.com/autowarefoundation/autoware.off-road) | 오프로드 자율주행 파일럿(광산 트럭·RoboRacer·행성 로버). EfficientNet-B0 기반 주행가능영역·고도 네트워크, CARLA 광산 데모 | 18 / 2 | 2026-04-15 | 활성 | 오프로드 WG 2026-05 일시 중단 |
| [autoware.orv-reference-design-docs](https://github.com/autowarefoundation/autoware.orv-reference-design-docs) | 오프로드 차량(OrV) 레퍼런스 디자인 가이드 | 1 / 1 | 2026-03-20 | 활성 | 2026 Q1/Q2 예정 |
| [LSA-reference-design-docs](https://github.com/autowarefoundation/LSA-reference-design-docs) | 저속 자율주행(LSA) 레퍼런스 디자인 가이드(RoboRacer·GoKart 포함) | 4 / 9 | 2026-02-27 | 활성 |  |
| [autoware.trucks](https://github.com/autowarefoundation/autoware.trucks) | 고속도로 자율 트럭(L4) 프로젝트. 현재 Vision Pilot 트럭 모델·J1939 인터페이스 작업 | 2 / 0 | 2025-12-07 | 휴면 | Trucks WG |
| [autoware.low-speed-autonomy-vehicles](https://github.com/autowarefoundation/autoware.low-speed-autonomy-vehicles) | LSA 차량 목표·유스케이스·설계 | 1 / 4 | 2025-08-14 | 휴면 |  |
| [autoware_individual_params](https://github.com/autowarefoundation/autoware_individual_params) | 개별 차량 파라미터(아카이브) | 5 / 319 | 2025-04-14 | 아카이브 | 아카이브 |
| [sample_vehicle_launch](https://github.com/autowarefoundation/sample_vehicle_launch) | 샘플 차량 launch(아카이브) | 12 / 319 | 2025-04-01 | 아카이브 | 아카이브 |
| [single_lidar_sensor_kit_launch](https://github.com/autowarefoundation/single_lidar_sensor_kit_launch) | 단일 LiDAR 센서킷(아카이브) | 2 / 16 | 2025-04-01 | 아카이브 | 아카이브 |
| [awsim_labs_vehicle_launch](https://github.com/autowarefoundation/awsim_labs_vehicle_launch) | AWSIM Labs 차량 launch(아카이브) | 1 / 319 | 2025-04-01 | 아카이브·포크 | 아카이브 |
| [awsim_labs_sensor_kit_launch](https://github.com/autowarefoundation/awsim_labs_sensor_kit_launch) | AWSIM Labs 센서킷(아카이브) | 2 / 34 | 2025-04-01 | 아카이브·포크 | 아카이브 |
| [sample_sensor_kit_launch](https://github.com/autowarefoundation/sample_sensor_kit_launch) | 샘플 센서킷 launch(아카이브) | 17 / 359 | 2025-03-28 | 아카이브 | 아카이브 |
| [autoware_launch.gdwbus](https://github.com/autowarefoundation/autoware_launch.gdwbus) | 특정 버스용 launch 포크 | 1 / 495 | 2025-01-18 | 포크 |  |
| [RefDesignWG](https://github.com/autowarefoundation/RefDesignWG) | Reference Design WG 문서 저장소 | 3 / 0 | 2025-01-03 | 휴면 |  |
| [autoware_tier4_robot](https://github.com/autowarefoundation/autoware_tier4_robot) | TIER IV 로봇용 autoware 포크 | 1 / 3.7k | 2024-09-10 | 포크 |  |
| [autoware_challenge_2024](https://github.com/autowarefoundation/autoware_challenge_2024) | Autoware Challenge 2024 | 3 / 0 | 2024-08-02 | 휴면 |  |
| [autoware-coe](https://github.com/autowarefoundation/autoware-coe) | Autoware Center of Excellence 웹사이트 | 0 / 1 | 2024-05-28 | 휴면 |  |
| [awf_reference_sensor_kit_launch](https://github.com/autowarefoundation/awf_reference_sensor_kit_launch) | AWF 레퍼런스 센서킷 launch | 0 / 3 | 2024-01-24 | 휴면 |  |
| [autoware-projects](https://github.com/autowarefoundation/autoware-projects) | 비코드 과제·WG 위키(워킹그룹 목록·거버넌스) | 8 / 0 | 2023-09-11 | 휴면 | 위키가 WG 목록의 공식 출처 |
| [awf_reference_vehicle_launch](https://github.com/autowarefoundation/awf_reference_vehicle_launch) | AWF 레퍼런스 차량 description·launch | 0 / 1 | 2023-09-04 | 휴면 |  |
| [itri_bus_sensor_kit](https://github.com/autowarefoundation/itri_bus_sensor_kit) | ITRI 버스 센서킷 | 0 / 1 | 2023-09-04 | 휴면 |  |
| [autoware_challenge_2023](https://github.com/autowarefoundation/autoware_challenge_2023) | Autoware Challenge 2023 | 1 / 0 | 2023-04-10 | 휴면 |  |
| [cbus_vehicle_launch](https://github.com/autowarefoundation/cbus_vehicle_launch) | ITRI 프로젝트 차량 launch | 0 / 0 | 2023-02-01 | 휴면 |  |

## I. 센서·차량 드라이버와 Index로 옮겨간 소형 패키지

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [autoware_component_monitor](https://github.com/autowarefoundation/autoware_component_monitor) | 컴포넌트 컨테이너 CPU·메모리 모니터. Index 등록 | 1 / 1 | 2026-10-28 | 활성 |  |
| [autoware_image_diagnostics](https://github.com/autowarefoundation/autoware_image_diagnostics) | 카메라 이미지 진단. Index로 이동 | 0 / 0 | 2026-10-19 | 활성 | 2026-10 |
| [autoware_pose2twist](https://github.com/autowarefoundation/autoware_pose2twist) | pose→twist 계산. Index 등록 | 0 / 0 | 2026-10-13 | 활성 |  |
| [autoware_livox_tag_filter](https://github.com/autowarefoundation/autoware_livox_tag_filter) | Livox 포인트 필터. Universe에서 빠져 Autoware Index로 이동한 첫 패키지 | 0 / 1 | 2026-10-12 | 활성 | 2.0.0 업그레이드 노트 |
| [autoware_bluetooth_monitor](https://github.com/autowarefoundation/autoware_bluetooth_monitor) | 블루투스 연결 모니터. Index 등록 | 0 / 0 | 2026-10-12 | 활성 |  |
| [applanix](https://github.com/autowarefoundation/applanix) | Applanix POS-LVX GNSS/INS 드라이버 | 5 / 9 | 2024-09-18 | 휴면 |  |
| [ros2_socketcan-release](https://github.com/autowarefoundation/ros2_socketcan-release) | 릴리스 저장소(아카이브) | 4 / 1 | 2024-07-16 | 아카이브 | 아카이브 |
| [lucid_vision_driver](https://github.com/autowarefoundation/lucid_vision_driver) | Lucid Vision 카메라 ROS 2 드라이버 | 27 / 25 | 2024-02-14 | 휴면 |  |
| [awf_velodyne](https://github.com/autowarefoundation/awf_velodyne) | Velodyne VLS 드라이버 포크 | 3 / 47 | 2023-06-06 | 포크 |  |
| [autoware-mih-dbw-interface](https://github.com/autowarefoundation/autoware-mih-dbw-interface) | MIH DBW 인터페이스 | 7 / 0 | 2022-11-03 | 휴면 |  |

## J. 레거시·아카이브·포크·벤더 패키지

| 저장소 | 설명 | ★ / ⑂ | 최근 갱신 | 상태 | 비고 |
|---|---|---|---|---|---|
| [zmqpp_vendor](https://github.com/autowarefoundation/zmqpp_vendor) | zmqpp 벤더(scenario simulator 의존) | 2 / 4 | 2025-12-22 | 휴면 |  |
| [autoware-backup](https://github.com/autowarefoundation/autoware-backup) | 수명 종료 태그 보관(아카이브) | 1 / 1 | 2025-12-10 | 아카이브 |  |
| [autoware_common](https://github.com/autowarefoundation/autoware_common) | 옛 공통 패키지(아카이브) | 26 / 70 | 2025-12-02 | 아카이브 | 아카이브 |
| [ament_cmake](https://github.com/autowarefoundation/ament_cmake) | ament_cmake 포크 | 1 / 149 | 2024-07-04 | 포크 |  |
| [mmdetection3d](https://github.com/autowarefoundation/mmdetection3d) | OpenMMLab mmdetection3d 포크 | 6 / 1.8k | 2024-06-13 | 포크 |  |
| [autoware_auto_msgs_adapter](https://github.com/autowarefoundation/autoware_auto_msgs_adapter) | Autoware.Auto 메시지 어댑터 | 1 / 0 | 2024-06-02 | 휴면 |  |
| [aw-universe](https://github.com/autowarefoundation/aw-universe) | Universe 포크 | 0 / 979 | 2024-03-25 | 포크 |  |
| [autodistill](https://github.com/autowarefoundation/autodistill) | autodistill 포크(파운데이션 모델로 라벨링) | 0 / 227 | 2024-03-12 | 포크 |  |
| [autoware.universe_planning](https://github.com/autowarefoundation/autoware.universe_planning) | Universe planning 포크 | 0 / 979 | 2023-12-01 | 포크 |  |
| [autoware_ai](https://github.com/autowarefoundation/autoware_ai) | Autoware.AI(ROS 1, 1세대) 메타(아카이브) | 53 / 17 | 2023-03-13 | 아카이브 | EOL 2022 |
| [autoware_ai_perception](https://github.com/autowarefoundation/autoware_ai_perception) | Autoware.AI 인식(아카이브) | 427 / 196 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_planning](https://github.com/autowarefoundation/autoware_ai_planning) | Autoware.AI 계획(아카이브) | 225 / 147 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_messages](https://github.com/autowarefoundation/autoware_ai_messages) | Autoware.AI 메시지(아카이브) | 15 / 25 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_simulation](https://github.com/autowarefoundation/autoware_ai_simulation) | Autoware.AI 시뮬(아카이브) | 53 / 31 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_visualization](https://github.com/autowarefoundation/autoware_ai_visualization) | Autoware.AI 시각화(아카이브) | 28 / 30 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_drivers](https://github.com/autowarefoundation/autoware_ai_drivers) | Autoware.AI 드라이버(아카이브) | 17 / 19 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_utilities](https://github.com/autowarefoundation/autoware_ai_utilities) | Autoware.AI 유틸(아카이브) | 62 / 36 | 2023-03-10 | 아카이브 |  |
| [autoware_ai_common](https://github.com/autowarefoundation/autoware_ai_common) | Autoware.AI 공통(아카이브) | 36 / 46 | 2023-03-08 | 아카이브 |  |
| [tvm_vendor](https://github.com/autowarefoundation/tvm_vendor) | Apache TVM 벤더 패키지(Autoware.Auto 시절) | 10 / 8 | 2023-01-24 | 휴면 |  |
| [autoware_ai_documentation](https://github.com/autowarefoundation/autoware_ai_documentation) | Autoware.AI 문서(아카이브) | 23 / 18 | 2022-08-31 | 아카이브 |  |
| [autoware_core_universe_prototype](https://github.com/autowarefoundation/autoware_core_universe_prototype) | Core/Universe 초기 프로토타입(아카이브) | 261 / 51 | 2022-07-25 | 아카이브 |  |
| [autoware_ai_docker](https://github.com/autowarefoundation/autoware_ai_docker) | Autoware.AI Docker(아카이브) | 24 / 31 | 2022-06-14 | 아카이브 |  |
| [qpoases_vendor](https://github.com/autowarefoundation/qpoases_vendor) | qpOASES 벤더 | 6 / 7 | 2022-05-23 | 휴면 |  |
| [rancher-cows-demo](https://github.com/autowarefoundation/rancher-cows-demo) | Rancher 데모 포크(무관) | 0 / 318 | 2022-01-20 | 포크 |  |
| [qpoases_vendor-release](https://github.com/autowarefoundation/qpoases_vendor-release) | 릴리스 저장소 | 1 / 2 | 2021-06-25 | 휴면 |  |
| [tvm_vendor-release](https://github.com/autowarefoundation/tvm_vendor-release) | 릴리스 저장소 | 1 / 1 | 2021-06-16 | 휴면 |  |
| [acado_vendor](https://github.com/autowarefoundation/acado_vendor) | ACADO 벤더 | 2 / 1 | 2020-12-17 | 휴면 |  |
| [ansys-vrxperience-ros2](https://github.com/autowarefoundation/ansys-vrxperience-ros2) | ANSYS VRXPERIENCE 인터페이스 | 2 / 2 | 2020-11-19 | 휴면 | 비활성 |
| [ansys-vrxperience-ros2-release](https://github.com/autowarefoundation/ansys-vrxperience-ros2-release) | 위 릴리스 저장소 | 0 / 0 | 2020-11-19 | 휴면 |  |
| [autocore_sim](https://github.com/autowarefoundation/autocore_sim) | ROS1/ROS2 다중 로봇 시뮬레이터(AutoCore) | 44 / 16 | 2020-11-18 | 휴면 | 비활성 |
| [autoware_ai_messages-release](https://github.com/autowarefoundation/autoware_ai_messages-release) | 릴리스 저장소 | 2 / 2 | 2020-11-03 | 휴면 |  |
