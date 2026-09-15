# Autoware 코드 대조 노트

기준 (src/PINS.md, 클론일 2026-09-15, depth 1):

| 디렉터리 | 저장소 | ref | 커밋 SHA | 커밋 날짜 |
|---|---|---|---|---|
| autoware_core | autowarefoundation/autoware_core | 1.9.0 | f25f83c632c1984ec276c894c41857d4abc0dad8 | 2026-06-26 |
| autoware_launch | autowarefoundation/autoware_launch | 0.52.0 | f942598d44b5769353167c76b784323d5c14c8c7 | 2026-07-13 |
| autoware_msgs | autowarefoundation/autoware_msgs | 1.13.0 | bb8e7bf5d97168663e0e7b357929e4fcdbd3a967 | 2026-05-20 |
| autoware_universe | autowarefoundation/autoware_universe | 0.52.1 | 02a589200c1af644ca4b4cb3ed98695b4b62118b | 2026-07-15 |
| autoware | autowarefoundation/autoware | 1.9.0 | 10718787ba6e28f038a0cb29ff99cc627b5abfd2 | 2026-07-15 |

약어: AW=`autoware@1.9.0`, CO=`autoware_core@1.9.0`, UN=`autoware_universe@0.52.1`, LA=`autoware_launch@0.52.0`, MS=`autoware_msgs@1.13.0`.
보고서: R1=`ad-sw-stack-deep-dive.md`, R2=`thor-deployment/thor-deployment.md`.

## 요약

- 대조 행 수: 91
- 판정별: 일치 65(보강 문안 포함) / 일부 일치 3 / 수정 필요 14 / 코드와 반대 2 / 코드로 확인 불가 7 (문서 전용 사실은 아래 확인 불가 목록에 따로 정리)

**가장 중요한 수정 5개**

1. **Planning 출력 토픽 이름이 틀렸다 (코드와 반대).** R1 2.1.3 요약표와 2.1.4 흐름도의 `/planning/scenario_planning/trajectory`는 옛 이름이다. Core 인터페이스 사양과 launch는 `/planning/trajectory`를 쓴다. 이름은 core 1.5.0(#602)에서 바뀌었다. `CO:common/autoware_component_interface_specs/include/autoware/component_interface_specs/planning.hpp:70` `name[] = "/planning/trajectory"`
2. **autoware.repos의 universe 고정 버전은 0.52.1이 아니라 0.52.0이다 (코드와 반대).** R1 2.1.2 표의 "repos 고정은 0.52.1"이 틀렸다. `AW:repositories/autoware.repos:58-61` `universe/autoware_universe: … version: 0.52.0`. 0.52.1 태그는 존재하지만 메타 저장소 1.9.0이 가리키는 버전이 아니다. universe 패키지의 package.xml도 `<version>0.52.0</version>`이다.
3. **PID 지연 보상 값은 두 가지다.** R1은 "약 100 ms"라고 적었다. 이는 autoware_launch 오버라이드 값이다. 패키지 기본값은 0.17 s다. `UN:control/autoware_pid_longitudinal_controller/config/autoware_pid_longitudinal_controller.param.yaml:3` `delay_compensation_time: 0.17`, `LA:autoware_launch/config/control/trajectory_follower/longitudinal/pid.param.yaml:16` `delay_compensation_time: 0.1 # {OVERRIDE}`
4. **planning_validator 옵션 번호는 README 본문과 파라미터 정의가 서로 어긋난다.** R1은 "그대로 발행 / 발행 안 함 / 마지막 유효 궤적"이라고 적었다. 이 표현은 README 3행만 따른 것이다. 실제 param과 코드의 enum은 `0: 그대로 발행`, `1: 마지막 유효 궤적`, `2: 마지막 유효 궤적 + soft stop`이다. "발행 안 함" 옵션은 없다. 기본값 0은 패키지와 launch 모두 같다.
5. **Localization 4개 패키지만 Core에 있는 것이 아니다.** Planning의 `mission_planner`, `velocity_smoother`, `behavior_velocity_planner`(본체 + stop_line), `motion_velocity_planner`(본체 + obstacle_stop)도 Core에 있다. Core에는 GPU 없이 동작하는 `autoware_euclidean_cluster_object_detector`도 있다. 따라서 Sensing은 "Universe 중심", Planning은 "Core + Universe"라는 표기는 맞다. 다만 R1 2.1.3의 "GPU 없이 가능한 검출은 `euclidean_cluster`뿐" 문장은 Core/Universe 구분을 함께 적어야 한다. 추가로 R2 3.3의 "checksum 검증은 없다"는 부분적으로 틀렸다. artifacts role은 get_url 77건에 모두 sha256 checksum이 있다. HF 태그 고정 + checksum 없음은 centerpoint 1건뿐이다.

그 밖의 수정 필요 항목: behavior_velocity 플러그인 "12종"(default preset의 launch 인자는 14개, 기본 활성은 9개), CenterPoint 모델 버전(README는 v2 URL, ansible은 HF v3.0), diffusion_planner 백엔드(기본 `tensorrt`, ONNX Runtime은 선택 빌드), vehicle_cmd_gate heartbeat(시스템 비상 heartbeat는 기본 0.5 s timeout, 외부 heartbeat는 선택), mrm_handler(launch는 comfortable_stop 활성, 패키지 기본은 비활성), CUDA 전처리 691,200 포인트·128 ring(코드·설정에서 찾지 못함), tensorrt 22.04 aarch64 기본값(10.3) 누락.

## 대조표

| # | 보고서 | 위치(절) | 주장 요지 | 판정 | 코드 근거 | 수정 문안 |
|---|---|---|---|---|---|---|
| 1 | R1 | 2.1.1 | Core 편입 기준 "Keep the default build CPU-only…" | 코드로 확인 불가 | CO·AW 전체 grep에서 "Keep the default build" 0건. 문서 사이트 전용 문구로 판단 | — |
| 2 | R1 | 2.1.1 | Core는 Universe에 의존하지 않음(Depend only downward) | 코드로 확인 불가(정황 일치) | CO에는 universe 패키지가 없다(71 package.xml). 의존성 전수 검사는 하지 않음 | — |
| 3 | R1 | 2.1.1/2.1.8 | 코드 라이선스 Apache 2.0 | 일치 | `UN:planning/autoware_diffusion_planner/package.xml:12` `<license>Apache License 2.0</license>` (저장소 LICENSE 존재) | — |
| 4 | R1 | 2.1.2 | autoware 메타 1.9.0 | 일치 | PINS: AW ref 1.9.0. `AW:repositories/autoware.repos` `core/autoware_core … version: 1.9.0` | — |
| 5 | R1 | 2.1.2 | autoware_core 1.9.0 = 메타 버전과 동일 | 일치 | `CO:localization/autoware_ekf_localizer/package.xml:5` `<version>1.9.0</version>` | — |
| 6 | R1 | 2.1.2 | universe 최신 0.52.0, **repos 고정은 0.52.1** | 코드와 반대 | `AW:repositories/autoware.repos:58-61` `version: 0.52.0`. `UN:control/autoware_vehicle_cmd_gate/package.xml` `<version>0.52.0</version>` | autoware 1.9.0의 autoware.repos는 autoware_universe를 0.52.0으로 고정하며, 0.52.1은 그 뒤 나온 패치 태그다. |
| 7 | R1 | 2.1.2 | core 1.8.0에서 `autoware_agnocast_wrapper`가 Core로 이동 | 일치(위치) / 버전은 확인 불가 | `CO:common/autoware_agnocast_wrapper/package.xml:5` `<version>1.9.0</version>`. 이동 시점은 CHANGELOG로 확인하지 않음 | — |
| 8 | R1 | 2.1.2 | 1.9.0 릴리스 노트 "Support NVIDIA Thor…", diffusion_planner v5.0 | 일부 일치 | 릴리스 노트 본문은 저장소에 없음. v5.0 모델: `AW:ansible/roles/artifacts/tasks/main.yaml:534` `diffusion_planner/v5.0`, `LA:autoware_launch/config/planning/neural_net_planner/diffusion_planner.param.yaml:24` `v5.0/diffusion_planner.onnx` | — |
| 9 | R1 | 2.1.3 요약 | `/map/vector_map` (LaneletMapBin), Core | 일치 | `CO:common/autoware_component_interface_specs/include/autoware/component_interface_specs/map.hpp:47-49` `LaneletMapBin`, `"/map/vector_map"`, QoS reliable + transient_local | — |
| 10 | R1 | 2.1.3 요약 | `/localization/kinematic_state` (Odometry), NDT+EKF, Core | 일치 | `CO:…/component_interface_specs/localization.hpp:45-47` `nav_msgs::msg::Odometry`, `"/localization/kinematic_state"` | — |
| 11 | R1 | 2.1.3 요약 | `/perception/object_recognition/objects` (PredictedObjects) | 일치 | `CO:…/component_interface_specs/perception.hpp:27-29` `PredictedObjects`, `"/perception/object_recognition/objects"` | — |
| 12 | R1 | 2.1.3 요약, 2.1.4 | Planning 출력 `/planning/scenario_planning/trajectory` | 코드와 반대 | `CO:…/component_interface_specs/planning.hpp:70` `"/planning/trajectory"`. `LA:tier4_universe_launch/tier4_planning_launch/launch/planning.launch.xml:84` `output_trajectory value="/planning/trajectory"`. `CO:common/autoware_component_interface_specs/CHANGELOG.rst:50` "change planning output topic name to /planning/trajectory (#602)"(1.5.0 절) | Planning 최종 출력 토픽은 `/planning/trajectory`(autoware_planning_msgs/Trajectory)이다. `/planning/scenario_planning/trajectory`는 core 1.5.0 이전 이름이다. |
| 13 | R1 | 2.1.3 요약 | `/control/command/control_cmd` (Control) | 일치 | `CO:…/component_interface_specs/control.hpp:27-29` `autoware_control_msgs::msg::Control`, `"/control/command/control_cmd"` | — |
| 14 | R1 | 2.1.3 요약 | Control은 "Universe 중심" | 일치(보강 가능) | MPC·PID·vehicle_cmd_gate는 UN에 있다. CO/control에도 `autoware_command_gate`, `autoware_simple_pure_pursuit`가 있다 | — |
| 15 | R1 | 2.1.3 요약 | `/vehicle/status/*` | 일치 | `CO:…/component_interface_specs/vehicle.hpp:34,43,52,61` `/vehicle/status/steering_status`, `gear_status`, … | — |
| 16 | R1 | 2.1.3 요약 | `/system/operation_mode/availability`, Universe | 일치 | `UN:system/autoware_diagnostic_graph_aggregator/launch/aggregator.launch.xml:28` remap to `/system/operation_mode/availability`. 타입은 README:48의 `tier4_system_msgs/msg/OperationModeAvailability` | — |
| 17 | R1 | 2.1.3 요약 | AD API default_adapi는 Core + Universe | 일치 | `CO:api/autoware_default_adapi`, `UN:system/autoware_default_adapi_universe` | — |
| 18 | R1 | 2.1.3 요약 | `/sensing/lidar/<group>/pointcloud` | 일치(형식) | `LA:sensor_kit/sample_sensor_kit_launch/sample_sensor_kit_launch/config/concatenate_and_time_sync_node.param.yaml:14-16` `/sensing/lidar/top/pointcloud_before_sync` 등 | — |
| 19 | R1 | 2.1.3 Sensing | pointcloud_preprocessor는 composable container + intra-process | 일치 | `UN:sensing/autoware_pointcloud_preprocessor/README.md:77` "designed to run within composable node containers, leveraging intra-process" | — |
| 20 | R1 | 2.1.3 Sensing | CUDA 전처리기가 cuda_blackboard로 GPU 상주 전달 | 일치 | `UN:sensing/autoware_cuda_pointcloud_preprocessor/docs/cuda-pointcloud-preprocessor.md:16` "uses the `cuda_blackboard`… zero-copy mechanism between GPU and GPU memory" | — |
| 21 | R1 | 2.1.3 Sensing | CUDA판 버퍼 상한 691,200 포인트·128 ring | 수정 필요(코드에서 미확인) | UN의 cuda_pointcloud_preprocessor 전체(.cu/.hpp/.cpp/.yaml/.md)에서 `691200` 0건. ring 수·링당 포인트는 런타임 값(`cuda_pointcloud_preprocessor.hpp:81-82` `num_rings_`, `max_points_per_ring_`). 128은 CPU ring_outlier_filter 설정 `LA:sensor_kit/sample_sensor_kit_launch/common_sensor_launch/config/ring_outlier_filter_node.param.yaml:5` `max_rings_num: 128`에서만 확인 | 691,200 포인트 상한은 0.52.x 코드·설정에서 찾지 못했으므로, 출처 문서 버전을 밝히거나 "출처 미확인"으로 낮춘다. |
| 22 | R1 | 2.1.3 Sensing | CUDA판은 CPU판과 "will not offer the same numerical results" | 일치 | `UN:sensing/autoware_cuda_pointcloud_preprocessor/docs/cuda-pointcloud-preprocessor.md:44` | — |
| 23 | R1 | 2.1.3 Sensing, 2.1.4 | CUDA 전처리를 선택 경로로 표기 | 일치(보강) | `LA:tier4_universe_launch/tier4_perception_launch/launch/perception.launch.xml:184` `cuda_pointcloud_preprocessing default="false"` | — |
| 24 | R1 | 2.1.3 Map | map_loader 부분·차분 로딩 서비스 | 일치 | `CO:map/autoware_map_loader/README.md:14-15` "partial … differential pointcloud map loading via ROS 2 service" | — |
| 25 | R1 | 2.1.3 Loc | NDT 기본 4스레드 | 일치 | 패키지 `CO:localization/autoware_ndt_scan_matcher/config/ndt_scan_matcher.param.yaml:38` `num_threads: 4` / launch `LA:autoware_launch/config/localization/ndt_scan_matcher/ndt_scan_matcher.param.yaml:51` `num_threads: 4` | — |
| 26 | R1 | (추가) | NDT resolution | 일치(참고) | 패키지 `…ndt_scan_matcher.param.yaml:32` `resolution: 2.0` / launch `:45` `resolution: 2.0` | — |
| 27 | R1 | 2.1.3 Loc | NDT 문서에 GPU 경로 언급 없음 | 일치 | `CO:localization/autoware_ndt_scan_matcher/README.md` grep `gpu|cuda` 0건 | — |
| 28 | R1 | 2.1.3 Loc, 2.1.4 | EKF 50 Hz 예측 + 지연 보상 | 일치 | 패키지 `CO:localization/autoware_ekf_localizer/config/ekf_localizer.param.yaml:6` `predict_frequency: 50.0`, `:8` `extend_state_step: 50` / launch `LA:autoware_launch/config/localization/ekf_localizer.param.yaml:19,21` 같은 값 | — |
| 29 | R1 | 2.1.3 Loc | gyro_odometer는 IMU + 차속으로 twist 추정 | 일치 | `CO:localization/autoware_gyro_odometer/README.md:5` "estimate twist by combining imu and vehicle speed" | — |
| 30 | R1 | 2.1.3 Loc | NDT·EKF·gyro·map_loader 네 패키지는 Core | 일치 | `CO:localization/{autoware_ndt_scan_matcher,autoware_ekf_localizer,autoware_gyro_odometer}`, `CO:map/autoware_map_loader` | — |
| 31 | R1 | 2.1.3 Loc | yabloc·eagleye는 Universe | 일치(보강) | yabloc: `UN:localization/yabloc`. eagleye는 UN 트리 밖 외부 저장소: `AW:repositories/autoware.repos:79-81` `universe/external/eagleye … MapIV/eagleye` | eagleye는 autoware_universe 안이 아니라 autoware.repos의 universe/external로 포함되는 외부 저장소(MapIV)다. |
| 32 | R1 | 2.1.3 Perc | CenterPoint는 PointPillars 계열, TensorRT fp16, 엔진 2개(voxel encoder, backbone-neck-head) | 일치 | `UN:perception/autoware_lidar_centerpoint/README.md:9` "PointPillars-based", `:46` `trt_precision` 기본 `fp16`, `:71` `pts_voxel_encoder_centerpoint.onnx`, `pts_backbone_neck_head_centerpoint.onnx` / launch `LA:…/lidar_model/centerpoint.param.yaml:17-21` encoder/head onnx·engine, `trt_precision: fp16` | — |
| 33 | R1 | 2.1.3 Perc | CenterPoint 학습 데이터 nuScenes + 내부 데이터, CC BY-NC-SA 4.0 | 일치 | `UN:perception/autoware_lidar_centerpoint/README.md:74` "trained in nuScenes (~28k lidar frames) and TIER IV's internal database (~11k…)", `:362-363` "non-commercial … Attribution-NonCommercial-ShareAlike 4.0" | — |
| 34 | R1 | (추가) CenterPoint 모델 버전·범위 | README 링크는 v2, 배포는 HF v3.0 | 수정 필요(버전 명시 권장) | README `:71` `…/centerpoint/v2/…` vs `AW:ansible/roles/artifacts/tasks/main.yaml:206-207` `hf download AutowareFoundation/lidar_centerpoint --revision v3.0`. 범위: `UN:…/config/centerpoint_ml_package.param.yaml:7-8` `point_cloud_range: [-76.8,-76.8,-4.0,76.8,76.8,6.0]`, `voxel_size: [0.32,0.32,10.0]` | 1.9.0 ansible이 받는 CenterPoint는 HF `AutowareFoundation/lidar_centerpoint` v3.0이며, README의 v2 URL과 다르다. |
| 35 | R1 | 2.1.3 Perc | lidar_transfusion = TransFusion + TensorRT | 일치 | `UN:perception/autoware_lidar_transfusion/README.md:9` "bases on TransFusion… uses TensorRT" | — |
| 36 | R1 | 2.1.3 Perc | tensorrt_yolox fp32/fp16/int8 | 일치 | `UN:perception/autoware_tensorrt_yolox/config/yolox_s_plus_opt.param.yaml:17` `precision: "int8" # … [fp32, fp16, int8]` | — |
| 37 | R1 | 2.1.3 Perc | image_projection_based_fusion은 collector + timeout으로 동기화 | 일치 | `UN:perception/autoware_image_projection_based_fusion/README.md:32-41` "Matching and Creating a Collector", `msg3d_timeout_sec`/`rois_timeout_sec` | — |
| 38 | R1 | 2.1.3 Perc | multi_object_tracker는 muSSP + EKF | 일치 | `UN:perception/autoware_multi_object_tracker/README.md:9` "data association and EKF", `:16` "mussp … is used as solver" | "클래스별 EKF"는 README 19-23행의 차량·대형차·보행자·자전거별 모델과 맞는다. |
| 39 | R1 | 2.1.3 Perc, 2.1.4 | tracker 10 Hz 발행 | 일치 | 패키지 `UN:perception/autoware_multi_object_tracker/config/multi_object_tracker_node.param.yaml:9` `publish_rate: 10.0` / launch `LA:autoware_launch/config/perception/object_recognition/tracking/multi_object_tracker/multi_object_tracker_node.param.yaml:22` `publish_rate: 10.0` | — |
| 40 | R1 | 2.1.3 Perc | map_based_prediction은 차선 연관 + Frenet 5차 궤적 | 일치(세부 보강) | `UN:perception/autoware_map_based_prediction/README.md:65` "minimum jerk trajectory implemented by 4th/5th order spline for lateral/longitudinal", `:114` "generated on the frenet frame" | 경로는 Frenet 좌표에서 횡방향 4차·종방향 5차 스플라인으로 만든다고 적는 편이 정확하다. |
| 41 | R1 | 2.1.3 Perc | GPU 없는 검출은 euclidean_cluster뿐, "CUDA installation is recommended" | 수정 필요(문구는 확인 불가) | 문구는 저장소 전체 grep 0건(문서 사이트 전용). Core에 CPU 검출기가 있다: `CO:perception/autoware_euclidean_cluster_object_detector`. Universe에는 `UN:perception/autoware_euclidean_cluster`가 있다 | GPU 없이 쓸 수 있는 LiDAR 검출은 euclidean clustering 계열이며, Core에도 `autoware_euclidean_cluster_object_detector`가 들어 있다. |
| 42 | R1 | 2.1.3 Plan | mission_planner는 Lanelet2 routing graph 최단경로 | 일치 | `CO:planning/autoware_mission_planner/README.md:11,82` "only the plugin for Lanelet2", "Routing graph, which plans route in Lanelet2" | — |
| 43 | R1 | 2.1.3 Plan | behavior_path_planner scene module(차선유지·회피·차선변경·출발·도착) | 일치 | `UN:planning/behavior_path_planner/` 아래 `…static_obstacle_avoidance_module`, `…dynamic_obstacle_avoidance_module`, `…lane_change_module`, `…start_planner_module`, `…goal_planner_module` 등 11개 모듈 | — |
| 44 | R1 | 2.1.3 Plan | behavior_velocity_planner 플러그인 12종 | 수정 필요 | `LA:autoware_launch/config/planning/preset/default_preset.yaml:51-91` behavior_velocity launch 인자 14개(crosswalk, walkway, traffic_light, intersection, roundabout, merge_from_private, blind_spot, detection_area, virtual_traffic_light, no_stopping_area, stop_line, occlusion_spot, speed_bump, no_drivable_lane). 기본 true는 9개, occlusion_spot·speed_bump·no_drivable_lane·roundabout·merge_from_private는 false. 패키지는 UN 12개 모듈 + CO `autoware_behavior_velocity_stop_line_module` | 0.52.0 기본 preset에는 behavior_velocity 모듈 14종이 있고, 기본으로 켜진 것은 9종이다(stop_line 모듈은 Core). |
| 45 | R1 | 2.1.3 Plan | velocity_smoother는 jerk 제약 최적화를 OSQP로 푼다 | 일치 | `CO:planning/autoware_velocity_smoother/README.md:65-66` "chosen from JerkFiltered, L2 and Linf… use OSQP as the solver". 기본 `CO:planning/autoware_velocity_smoother/launch/velocity_smoother.launch.xml:12` `velocity_smoother_type default="JerkFiltered"` | — |
| 46 | R1 | 2.1.3 Plan | velocity_smoother 등 흐름 패키지의 저장소 | 수정 필요(보강) | `CO:planning/{autoware_mission_planner,autoware_velocity_smoother,behavior_velocity_planner,motion_velocity_planner}` 존재. Universe에는 확장 모듈만 있다 | mission_planner·velocity_smoother와 behavior/motion_velocity_planner 본체는 Core에, 대부분의 모듈 플러그인은 Universe에 있다. |
| 47 | R1 | 2.1.3 Plan | planning_validator는 지연·궤적·충돌 검사 플러그인 | 일치 | `UN:planning/planning_validator/` 아래 `…_latency_checker`, `…_trajectory_checker`, `…_intersection_collision_checker`, `…_rear_collision_checker` | — |
| 48 | R1 | 2.1.3 Plan | 무효 궤적 3옵션 "그대로 / 발행 안 함 / 마지막 유효", 옵션 0 = 그대로 | 수정 필요 | `UN:planning/planning_validator/autoware_planning_validator/config/planning_validator.param.yaml:5-9` "0: publish the trajectory even if it is invalid / 1: publish the last validated trajectory / 2: … with soft stop", `default_handling_type: 0`. `src/node.cpp:188,206,214` enum `PUBLISH_AS_IT_IS`, `USE_PREVIOUS_RESULT`, `USE_PREVIOUS_RESULT_WITH_SOFT_STOP`. launch도 `LA:…/planning_validator/planning_validator.param.yaml:22` `default_handling_type: 0`. README:3의 "1. stop publishing"은 코드와 어긋나는 낡은 문구다 | planning_validator의 무효 궤적 처리는 0=그대로 발행(패키지·launch 기본), 1=마지막 유효 궤적, 2=마지막 유효 궤적 + soft stop의 세 가지다. |
| 49 | R1 | 2.1.3 Plan | diffusion_planner는 ONNX/TensorRT, Apache 2.0 | 수정 필요(보강) | `package.xml:12` Apache 2.0, `package.xml:31` `autoware_tensorrt_common` 의존. ONNX Runtime은 `CMakeLists.txt:7` `find_package(onnxruntime QUIET)`일 때만 선택 빌드. launch 기본 `LA:…/neural_net_planner/diffusion_planner.param.yaml:19` `backend: "tensorrt" # "tensorrt" "ort_cpu" "ort_cuda" "ort_tensorrt"` | diffusion_planner는 ONNX 모델을 TensorRT 백엔드(기본)로 돌리며, ONNX Runtime 백엔드는 선택 빌드다. |
| 50 | R1 | 2.1.3 Plan | trajectory_ranker는 후보 궤적을 점수화해 고른다 | 일치 | `UN:planning/autoware_trajectory_ranker/README.md:5` "evaluating and ranking multiple trajectory candidates… attaching a scalar score" | "Architecture 2.0 초기 구현"이라는 성격 규정은 README에서 확인하지 못함 |
| 51 | R1 | 2.1.3 Ctrl | trajectory_follower = 횡 MPC + 종 PID | 일치 | `UN:control/autoware_trajectory_follower_node`, `UN:control/autoware_mpc_lateral_controller`, `UN:control/autoware_pid_longitudinal_controller` | — |
| 52 | R1 | 2.1.3 Ctrl | MPC horizon 50 × 0.1 s, input_delay 0.24 s | 일치 | 패키지 `UN:control/autoware_mpc_lateral_controller/param/lateral_controller_defaults.param.yaml:19-20,47` `mpc_prediction_horizon: 50`, `mpc_prediction_dt: 0.1`, `input_delay: 0.24` / launch `LA:autoware_launch/config/control/trajectory_follower/lateral/mpc.param.yaml:32-33,60` 같은 값 | — |
| 53 | R1 | 2.1.3 Ctrl | QP는 Eigen 기반 해법 또는 OSQP | 일치(기본값 보강) | `UN:control/autoware_mpc_lateral_controller/README.md:36-37` "unconstraint_fast: … with eigen", "osqp". 기본: 패키지 `…defaults.param.yaml:18` / launch `mpc.param.yaml:31` `qp_solver_type: "osqp"` | 기본 QP 해법은 패키지·launch 모두 OSQP다. |
| 54 | R1 | 2.1.3 Ctrl | PID 약 100 ms 지연 보상 + 경사 보상 | 수정 필요(값 두 개 병기) | 패키지 `UN:control/autoware_pid_longitudinal_controller/config/autoware_pid_longitudinal_controller.param.yaml:3` `delay_compensation_time: 0.17`, `:8` `enable_slope_compensation: true` / launch `LA:autoware_launch/config/control/trajectory_follower/longitudinal/pid.param.yaml:16` `delay_compensation_time: 0.1 # {OVERRIDE}` | PID 지연 보상은 패키지 기본 0.17 s이고, autoware_launch가 0.1 s로 덮어쓴다. |
| 55 | R1 | 2.1.3 Ctrl | PID 상태기계 DRIVE·STOPPING·STOPPED·EMERGENCY | 일치 | `UN:control/autoware_pid_longitudinal_controller/README.md:16-27` "four state transitions … STOPPING … EMERGENCY" | — |
| 56 | R1 | 2.1.3 Ctrl | vehicle_cmd_gate는 자동·외부·비상 명령 중 하나를 선택 | 일치 | `UN:control/autoware_vehicle_cmd_gate/README.md:9` "Receive multiple control commands and select one", 입력 `~/input/auto/control_cmd`, `~/input/external/control_cmd`, `~/input/emergency/control_cmd`(18-28행) | — |
| 57 | R1 | 2.1.3 Ctrl | heartbeat가 끊기면 비상으로 전환 | 수정 필요(조건 명시) | `UN:control/autoware_vehicle_cmd_gate/config/vehicle_cmd_gate.param.yaml:4-6,10` `system_emergency_heartbeat_timeout: 0.5`, `use_emergency_handling: true`, `check_external_emergency_heartbeat: $(var …)`, `external_emergency_stop_heartbeat_timeout: 0.0`. README:135-137은 외부 heartbeat가 선택 기능이며 쓰지 않으면 false로 두라고 적는다. launch `LA:…/vehicle_cmd_gate.param.yaml:17-23` 같은 값 | vehicle_cmd_gate는 시스템 비상 heartbeat 0.5 s timeout을 기본으로 감시하고, 외부 비상정지 heartbeat 감시는 `check_external_emergency_heartbeat`로 켜는 선택 기능이다. |
| 58 | R1 | 2.1.3 Ctrl | 속도 의존 한계로 가속·jerk·횡가속·조향각 필터 | 코드로 확인 불가(미조사) | 이번 대조에서 필터 파라미터(`nominal.*`, `on_transition.*`)는 열람하지 않음 | — |
| 59 | R1 | 2.1.3 Ctrl | control_validator: 역주행 속도·과속·궤적 편차 → `/diagnostics` | 일치(항목 보강) | `UN:control/autoware_control_validator/README.md:3,14-20` Inverse velocity, Overspeed, Overrun estimation, Lateral jerk, Deviation, Yaw deviation | 검사 항목에는 overrun 추정·횡 jerk·yaw 편차도 있다. |
| 60 | R1 | 2.1.3 Veh | raw_vehicle_cmd_converter: accel/brake map CSV, 조향은 기어비 모델 | 일치(기본 설정 보강) | `UN:vehicle/autoware_raw_vehicle_cmd_converter/config/raw_vehicle_cmd_converter.param.yaml:3-5` accel/brake/steer map csv, `:8` `convert_steer_cmd: false`, `:29-32` `convert_steer_cmd_method: "vgr"`, `vgr_coef_a: 15.713`, `b: 0.053`, `c: 0.042` / launch `LA:autoware_launch/config/vehicle/raw_vehicle_cmd_converter/raw_vehicle_cmd_converter.param.yaml:42-45` 같은 VGR 값 | 조향 변환은 기본 비활성(`convert_steer_cmd: false`)이며, 켜면 VGR 또는 steer_map 방식을 쓴다. |
| 61 | R1 | 2.1.3 Sys | diagnostic_graph_aggregator가 availability 생성 | 일치 | `UN:system/autoware_diagnostic_graph_aggregator/src/node/converter.cpp:37` `create_publisher<OperationModeAvailability>("~/operation_mode/availability", …)` | — |
| 62 | R1 | 2.1.3 Sys, 4.5 | mrm_handler는 emergency stop·comfortable stop·pull over 중 선택 | 일치(기본값 병기 필요) | `UN:system/autoware_mrm_handler/README.md:22-37` emergency_stop / comfortable_stop / pull_over_manager operate. 패키지 `config/mrm_handler.param.yaml:12-13` `use_pull_over: false`, `use_comfortable_stop: false` / launch `LA:autoware_launch/config/system/mrm_handler/mrm_handler.param.yaml:12-13` `use_pull_over: false`, `use_comfortable_stop: true` | 기본 launch에서 쓰는 MRM은 comfortable stop과 emergency stop이며, pull over는 꺼져 있다(패키지 기본은 둘 다 꺼짐). |
| 63 | R1 | 4.5 | `use_emergency_holding`이 켜지면 비상에서 복귀 안 함 | 일치(기본값 보강) | 패키지 `UN:system/autoware_mrm_handler/config/mrm_handler.param.yaml:9-10` `use_emergency_holding: false`, `timeout_emergency_recovery: 5.0` / launch `LA:…/mrm_handler.param.yaml:9` `false` | 기본값은 false(패키지·launch)다. |
| 64 | R1 | 2.1.3 Sys, 4.3 | pipeline_latency_monitor 기본 1000 ms 초과 시 ERROR | 일치 | 패키지 `UN:system/autoware_pipeline_latency_monitor/config/pipeline_latency_monitor.param.yaml:4` `latency_threshold_ms: 1000.0`, README:43 기본 1000, `:34` ERROR / launch 파일 `LA:autoware_launch/config/system/pipeline_latency_monitor/pipeline_latency_monitor.param.yaml` 존재(값은 미열람) | — |
| 65 | R1 | 2.1.3 API | AD API 4개 통신 패턴 QoS | 코드로 확인 불가(정황 일치) | 패턴 정의는 문서 사이트 전용. `CO:api/autoware_adapi_specs/include`에 RELIABLE 12 / BEST_EFFORT 7, TRANSIENT_LOCAL 8 / VOLATILE 11 조합이 실제로 쓰인다 | — |
| 66 | R1 | 2.1.5, 5.5, 2.3 | ansible 기본 rmw = rmw_cyclonedds_cpp | 일치 | `AW:ansible/roles/rmw_implementation/defaults/main.yaml:2` `rmw_implementation__name: rmw_cyclonedds_cpp`. Docker도 `AW:docker/base.Dockerfile:66` `ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp` | — |
| 67 | R1 | 2.1.5 | sysctl rmem_max=2147483647, ipfrag_high_thresh=134217728 | 일치 | `AW:docker/docker-entrypoint.sh:20-22` `net.core.rmem_max=2147483647`, `net.ipv4.ipfrag_time=3`, `net.ipv4.ipfrag_high_thresh=134217728`. "소켓 수신 버퍼 최소 10 MB"는 확인 불가 | — |
| 68 | R1 | 2.1.5 | `take()`, loaned message 미구현(2024-05) | 코드로 확인 불가 | 코딩 가이드 문서 전용 | — |
| 69 | R1 | 2.1.5 | Agnocast는 heaphook(LD_PRELOAD) + 커널 모듈 | 일치 | `AW:ansible/roles/agnocast/defaults/main.yaml:2-3` `agnocast-heaphook-v…`, `agnocast-kmod-v…`, `agnocast_version: 2.3.5`. `CO:common/autoware_agnocast_wrapper/…/agnocast_env.launch.py:21-25` "ld_preload_value: LD_PRELOAD value with heaphook prepended" | — |
| 70 | R1 | 2.1.5, 2.3 | Agnocast 기본 비활성, `ENABLE_AGNOCAST=1`로 빌드 | 일치 | `CO:common/autoware_agnocast_wrapper/README.md:9` "default build command, Agnocast is **not enabled**… `ENABLE_AGNOCAST=1`", `CMakeLists.txt:16` `STREQUAL "1"`. launch 기본값 `UN:planning/planning_validator/autoware_planning_validator/launch/planning_validator.launch.xml:2` `$(env ENABLE_AGNOCAST 0)` | 빌드 시점뿐 아니라 실행 시 환경변수로 rclcpp/agnocast Node를 고르는 경로도 있다(README:17). |
| 71 | R1 | 2.1.5 | cuda_blackboard 목표·"All nodes must reside in the same process" | 코드로 확인 불가 | cuda_blackboard는 외부 저장소(`AW:repositories/autoware.repos:103-105` `universe/external/cuda_blackboard`)이며 클론하지 않음 | — |
| 72 | R1 | 2.1.6, 2.1.9 | CUDA 22.04 = 12.8, 24.04 = 13.0 | 일치 | `AW:ansible/roles/cuda/defaults/main.yaml:5` `cuda_version: "{{ '13.0' if ansible_distribution_version == '24.04' else '12.8' }}"` | — |
| 73 | R1/R2 | 2.1.6 / 3.1·3.2 | TensorRT 22.04 x86 = 10.8, 24.04 = 10.13(10.13.3.9) | 수정 필요(누락 보강) | `AW:ansible/roles/tensorrt/defaults/main.yaml:8-10` `'10.13.3.9-1+cuda13.0' if 24.04 else '10.3.0.26-1+cuda12.5' if aarch64 else '10.8.0.43-1+cuda12.8'` | TensorRT 기본값은 24.04 10.13.3.9, 22.04 x86 10.8.0.43, 22.04 aarch64(Jetson Orin) 10.3.0.26(CUDA 12.5)이다. |
| 74 | R2 | 3.1 | `CMAKE_CUDA_ARCHITECTURES=86;87;89;90;110` | 일치 | `AW:docker/universe-cuda.Dockerfile:36,126` `ENV CMAKE_CUDA_ARCHITECTURES="86;87;89;90;110"` | — |
| 75 | R2 | 3.1, 결론 3 | Jetson Thor(L4T R38.4.0, CUDA 13.0)에서만 검증, DRIVE Thor는 미검증 | 일치 | `AW:docker/README.md:169` "verified end-to-end on a local Jetson Thor (L4T R38.4.0 / CUDA 13.0). DRIVE Thor is expected to work by design". "480 패키지·44분"과 PR 리뷰 코멘트는 확인 불가(PR 본문) | — |
| 76 | R2 | 3.3 | Thor docker run 명령(--net host, --runtime nvidia, env 2개, HOST_UID/GID, maps·ml_models 볼륨, `source /opt/autoware/setup.bash`) | 일치 | `AW:docker/README.md:185-195` 문자 단위로 같다 | — |
| 77 | R2 | 3.3 | 호스트 준비 `nvidia-ctk runtime configure --runtime=docker`, `--gpus all` 미사용 | 일치 | `AW:docker/README.md:177-179`(apt install + `nvidia-ctk runtime configure --runtime=docker` + `systemctl restart docker`), `:199` "`--gpus all` is **not** used on Tegra" | — |
| 78 | R2 | 3.3, 3.7 | 이미지에서 DLA, VPI, NVDEC/NVENC, Argus 제외 | 일치 | `AW:docker/README.md:219` "DLA, VPI, NVDEC/NVENC, and Argus camera support are intentionally out of scope for this image" | — |
| 79 | R2 | 3.3 | 공개 태그 `ghcr.io/…:universe-cuda-jazzy`, 버전 태그 `universe-jazzy-1.9.0` | 일부 일치 | `AW:docker/README.md:81` `universe-cuda-jazzy`. CI 캐시 태그 `AW:.github/workflows/keep-build-cache-small.yaml:41-42` `ci-universe-cuda-jazzy-{amd64,arm64}-main`. `universe-jazzy-1.9.0` 형식은 저장소에서 찾지 못함 | — |
| 80 | R2 | 3.3 | artifacts 명령 `--tags artifacts -e "data_dir=…" --ask-become-pass` | 일치 | `AW:ansible/roles/artifacts/README.md:68` 같은 명령 | — |
| 81 | R2 | 3.3 | HF AutowareFoundation에서 태그 고정, checksum 검증 없음 | 수정 필요 | HF는 1건: `AW:ansible/roles/artifacts/tasks/main.yaml:206-207` `hf download AutowareFoundation/lidar_centerpoint --revision v3.0`(checksum 없음). 나머지 `get_url` 77건에는 모두 `checksum: sha256:`가 있다(awf.ml.dev.web.auto·S3). README:71 "validate the checksums" | ML 모델 대부분은 S3·awf.ml.dev.web.auto에서 sha256 checksum으로 검증해 받고, HF 태그 고정(checksum 없음)은 lidar_centerpoint v3.0 한 건뿐이다. |
| 82 | R2 | 3.3 | DDS sysctl 3줄(rmem_max, ipfrag_time=3, ipfrag_high_thresh) | 일치 | `AW:docker/docker-entrypoint.sh:20-22` | — |
| 83 | R2 | 3.3 | Jazzy에서 CycloneDDS ParticipantIndex "none" | 일치 | `AW:docker/files/cyclonedds.xml:6` `<ParticipantIndex>none</ParticipantIndex>` | — |
| 84 | R2 | 3.4 | spconv cu130-rev1이 upstream 릴리스 대기로 막힘 | 일치 | `AW:ansible/roles/spconv/tasks/main.yaml:2-3` "skipped on Ubuntu 24.04 until cu130-rev1 release lands", `when: ansible_distribution_version != '24.04'`. `defaults/main.yaml:7-11` | 1.9.0 ansible 경로로는 24.04 이미지에 spconv가 설치되지 않는다. |
| 85 | R2 | 3.4 | autoware_ptv3·bevfusion·tensorrt_vad·system_monitor 존재 | 일치(존재만) | `UN:perception/autoware_ptv3`, `UN:perception/autoware_bevfusion`, `UN:e2e/autoware_tensorrt_vad`, `UN:system/autoware_system_monitor/CMakeLists.txt:8` `find_package(NVML)`. PR·이슈 상태는 확인 불가 | — |
| 86 | R2 | 3.4 | centerpoint `build_only`로 엔진 사전 생성 | 일치 | `UN:perception/autoware_lidar_centerpoint/README.md:45,54-56` `build_only` 기본 false | — |
| 87 | R2 | 3.6 | 샘플 데이터 S3 공개, sha256이 ansible role에 있음 | 일치 | `AW:ansible/roles/demo_artifacts/tasks/main.yaml:19,22` `…/maps/demos/sample-map-planning.zip` `sha256:5536fce7…93b9`; `:33,36` `sample-map-rosbag.zip` `sha256:07e2da0b…bc8`; `:53,56` `…/recordings/bags/demos/sample-rosbag.zip` `sha256:5f9d3635…cf88` | — |
| 88 | R2 | 3.6 | planning_simulator / bag play 명령 | 코드로 확인 불가 | 문서 사이트 전용. `sample_vehicle`, `sample_sensor_kit`의 launch 패키지는 LA에 존재(`LA:sensor_kit/sample_sensor_kit_launch`) | — |
| 89 | R2 | 3.2, 결론 5 | Autoware 고정 CUDA 13.0 · TensorRT 10.13.3.9 (24.04) | 일치 | #72, #73 근거와 같다 | — |
| 90 | R2 | 4.1 | 2a 단계: universe-cuda-jazzy 이미지로 logging simulator | 일치(전제) | #76 근거. 단, 기본 인지 `lidar_detection_model default="centerpoint"`(`LA:autoware_launch/launch/components/tier4_perception_component.launch.xml:64`)이며, 모델은 HF 토큰이 필요한 centerpoint v3.0 | 2a 단계 준비물에 `HF_TOKEN`(centerpoint v3.0 HF 다운로드용)을 넣는다. |
| 91 | R1 | 2.3 L6 | 규칙 플래너 + diffusion_planner + trajectory_ranker | 일치(기본값 보강) | 패키지 존재(#49·#50). 기본 launch는 `LA:autoware_launch/launch/autoware.launch.xml:11` `planning_setting default="rule_based"`. autoware_launch 전체에서 trajectory_ranker 참조 0건 | 기본 launch는 rule_based이며, diffusion_planner는 `planning_setting:=diffusion_planner`로 켜고 trajectory_ranker는 기본 launch에 연결돼 있지 않다. |

## 코드에서 새로 확인한 사실

| 사실 | 근거 |
|---|---|
| 기본 launch의 인지 모드는 `lidar`, LiDAR 검출기는 `centerpoint`다(transfusion·bevfusion 아님) | `LA:autoware_launch/launch/autoware.launch.xml:48` `perception_mode default="lidar"`; `LA:autoware_launch/launch/components/tier4_perception_component.launch.xml:64` `lidar_detection_model default="centerpoint"` |
| 기본 planning은 `rule_based`다. diffusion_planner는 선택이며, 켜면 기본 백엔드는 TensorRT, 모델은 v5.0이다 | `LA:autoware_launch/launch/autoware.launch.xml:11`; `LA:…/neural_net_planner/diffusion_planner.param.yaml:19,24` |
| trajectory_ranker는 autoware_launch 0.52.0 어디에도 연결되지 않았다 | `grep -rn ranker autoware_launch/autoware_launch/launch` 0건 |
| CUDA 포인트클라우드 전처리는 기본 꺼짐이다 | `LA:tier4_universe_launch/tier4_perception_launch/launch/perception.launch.xml:184` `cuda_pointcloud_preprocessing default="false"` |
| Agnocast는 기본 꺼짐이지만, ansible·repos로 소스 빌드 대상(agnocast 2.3.5)에는 들어 있다. pointcloud_container launch는 agnocast_env를 include한다 | `AW:repositories/autoware.repos:7-10` `core/agnocast … version: 2.3.5`; `LA:autoware_launch/launch/pointcloud_container.launch.py:32-38` |
| Docker 이미지 기본 rmw도 CycloneDDS다 | `AW:docker/base.Dockerfile:66` |
| tier4_*_launch 패키지(perception·planning·control 등 10개)는 0.52.0에서 autoware_launch 저장소 `tier4_universe_launch/` 아래에 있다(universe 저장소에는 `launch/` 디렉터리가 없다) | `LA:tier4_universe_launch/`; `autoware_universe/launch` 없음 |
| 패키지 수(package.xml): core 71, universe 242, launch 29, msgs 12 | `find <repo> -name package.xml \| wc -l` |
| Core는 Planning 본체(mission_planner, velocity_smoother, behavior/motion_velocity_planner, path_generator)와 CPU 검출기 `euclidean_cluster_object_detector`, `ground_filter`, `simple_pure_pursuit`, `command_gate`를 갖는다 | `CO:planning/`, `CO:perception/`, `CO:control/` 디렉터리 목록 |
| 기본 preset에서 behavior_velocity 중 occlusion_spot·speed_bump·no_drivable_lane·roundabout·merge_from_private는 꺼져 있다 | `LA:autoware_launch/config/planning/preset/default_preset.yaml:63-91` |
| MRM 기본 구성(launch): comfortable_stop 사용, pull_over 미사용, emergency_holding false, availability timeout 0.5 s, update_rate 10 | `LA:autoware_launch/config/system/mrm_handler/mrm_handler.param.yaml:9-13`; `UN:system/autoware_mrm_handler/config/mrm_handler.param.yaml:5-6` |
| planning_validator는 기본 10 Hz로 동작 가정(`planning_hz: 10.0`) | `UN:planning/planning_validator/autoware_planning_validator/config/planning_validator.param.yaml:3` |
| OGM 기본값: map_length 150 m, resolution 0.5 m, `OccupancyGridMapFixedBlindSpot`(패키지·launch 같음) | `UN:perception/autoware_probabilistic_occupancy_grid_map/config/pointcloud_based_occupancy_grid_map.param.yaml:3-4,28`; `LA:autoware_launch/config/perception/occupancy_grid_map/pointcloud_based_occupancy_grid_map.param.yaml:16-17,41` |
| CenterPoint ML 패키지 범위 ±76.8 m, z −4~6 m, voxel 0.32 m, max_voxel 40000 | `UN:perception/autoware_lidar_centerpoint/config/centerpoint_ml_package.param.yaml:6-8` |
| cuda·tensorrt ansible 주석은 Jetson Thor와 DRIVE Thor가 같은 sm_110 SBSA 패키지 셋을 공유한다고 명시한다 | `AW:ansible/roles/cuda/defaults/main.yaml:2-4`; `AW:ansible/roles/tensorrt/defaults/main.yaml:2-3` |

## 확인 불가 목록

| 항목 | 이유 |
|---|---|
| Core 편입 기준 문구(CPU-only, Depend only downward, 라이선스, Humble/Jazzy CI, clang-tidy) | 저장소에 해당 문서 없음(문서 사이트 전용) |
| Architecture 1.0 범위 제외 문구, Microautonomy 설명 | 설계 문서 전용 |
| 릴리스 정책(SemVer·월간), ROS 2 전환 일정, 0.45.1→1.5.0 번호 점프 | 문서·GitHub Releases 전용 |
| 1.9.0 릴리스 노트 본문, PR #7108 본문(480 패키지·44분, 리뷰 코멘트) | GitHub 릴리스·PR 전용 |
| `take()`·loaned message 코딩 가이드 문구 | 문서 사이트 전용 |
| cuda_blackboard "same process" 제약 | 외부 저장소, 미클론 |
| Agnocast 성능 수치(IceOryx 비교, 트래픽 2/3 감소) | AWF 게시글·논문 전용 |
| AD API 4패턴 정의 | 문서 전용(adapi_specs에 QoS 조합이 있다는 정황만 확인) |
| 최소 사양 8코어/16 GB, 레퍼런스 HW 목록, CycloneDDS "recommended and most tested", 소켓 버퍼 10 MB | 문서 사이트 전용 |
| "CUDA installation is recommended"(euclidean_cluster 문맥) | 저장소 grep 0건 |
| CUDA 전처리 691,200 포인트 상한 | 0.52.1 코드·설정·docs에서 값을 찾지 못함 |
| vehicle_cmd_gate 필터 세부(속도 의존 한계) | 이번 대조에서 미열람 |
| planning_simulator·bag play 명령, sample-rosbag에 이미지 없음 | 문서·데이터 전용 |
| `universe-jazzy-1.9.0` 태그 형식, PR #13158/#13160, 이슈(bevfusion nvrtc, NVML) 상태 | GHCR·GitHub 이슈 전용 |
