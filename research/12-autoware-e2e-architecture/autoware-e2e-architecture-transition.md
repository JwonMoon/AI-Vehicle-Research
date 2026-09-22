# Autoware의 E2E / 하이브리드 아키텍처 전환

> 작성일: 2026-06-02 · 대상: 자율주행 아키텍처에 익숙한 엔지니어 · 로컬 코드 기준 **Autoware 1.8.0 / autoware_universe 0.51.0**
> 검증: 공식 설계 문서·보도자료·arXiv 원문·GitHub 코드/위키·로컬 소스를 직접 확인. AI 요약 인용 배제. 불확실 항목은 §10에 별도 명시.

---

## 1. 핵심 요약 (먼저 읽기)

Autoware 진영의 학습 기반 전환은 **두 갈래**로 진행된다. 같은 철학(modular → monolithic → hybrid E2E)을 공유하지만 **주체·타깃·센서가 다른 별개 노력**이다. "단계"가 아니라 "두 트랙"으로 보는 게 정확하다.

### 트랙 A — 로보택시 (TIER IV 주도, Architecture 1.0 → 2.0)

> 핵심 문장: **고정 파이프라인(v1)에서 Generator-Selector 구조(v2)로 전환 중이고, "하이브리드"란 그 v2 구조 자체다.**

- **무엇**: Sensing→Perception→Localization→Planning→Control 고정 파이프라인(Architecture 1.0)을, E2E·diffusion 모델을 품을 수 있는 **Generator-Selector(Architecture 2.0)** 로 교체. 이는 tier4의 사견이 아니라 [**Autoware 공식 설계 문서**](https://autowarefoundation.github.io/autoware-documentation/main/design/autoware-architecture-v2/)의 방향(상태 "Under Construction").
- **하이브리드의 정체**: 별도 시스템이 아님. rule-based와 E2E generator를 **Safety Gate 달린 Selector**로 함께 굴리는 v2 구조 자체가 곧 하이브리드.
- **타깃**: 무인 robotaxi/버스, **Level 4+**, HD맵·LiDAR 사용 가능.
- **현황**: 구조는 정해졌고 부품은 머지됐으나 production 기본 경로로 배선·검증 안 된 **실험 단계**. 성숙도 **Diffusion > VAD**.

### 트랙 B — 개인차량 ADAS (POV 워크그룹 주도, vision-only)

> **용어**: **POV 워크그룹** = Privately Owned Vehicle(개인 소유 차량) Work Group. Autoware Foundation 산하의 분과(개발 그룹)로, robotaxi가 아니라 일반 승용차용 ADAS를 만든다. **Foundation Model(기반 모델)** = 하나의 큰 신경망을 여러 인식 과제에 공통으로 쓰는 모델(여기선 AutoSeg).

> 핵심 문장: **싼 카메라·싼 칩으로 양산차에 넣는 ADAS를 오픈소스로 푸는 것. 그래서 경량화(Lite)가 핵심.**

- **무엇**: `autoware_vision_pilot` 저장소. **vision-only**(카메라만) + **mapless**(HD맵 없음) + **저전력 임베디드**(Jetson Orin Nano, INT8, 수 TOPS). 비싼 센서·맵 없이 인간처럼 카메라로 주행.
- **경량화 = Lite Models**: SceneSeg/Scene3D/EgoLanes를 ~20–28× 압축해 싼 칩에서 실시간(80–100+ FPS). 이게 "양산차 탑재 가능"의 열쇠.
- **타깃·사업성**: 양산 승용차 L2 → 점진적 L4. **TIER IV가 직접 파는 제품이 아니라**, OEM·Tier-1이 양산차에 통합하도록 **오픈소스(Apache 2.0, 가중치까지 공개)** 로 제공 → 대중차 ADAS 민주화. "productionizable/safety-certifiable" 표방.
- **현황**: VisionPilot 0.9 릴리스, 실차 테스트 진행.

### 두 트랙 비교

| | **트랙 A — 로보택시** | **트랙 B — 개인차량 ADAS** |
|---|---|---|
| 주체 | TIER IV | POV Work Group(커뮤니티: BrightDrive·AEI 등) |
| 저장소 | `autoware_universe` + `tier4/new_planning_framework` | `autoware_vision_pilot` |
| 타깃 | 무인 robotaxi/버스, **L4+** | 양산 승용차 **L2→L4**, OEM 통합용 |
| 센서·맵 | 카메라+LiDAR, HD맵 가능 | **카메라만, mapless** |
| 하드웨어 | 고성능 GPU | **저전력 엣지**(수 TOPS) |
| 대표 기술 | Generator-Selector, VAD, Diffusion Planner | AutoSeg(SceneSeg/Scene3D/DomainSeg), AutoSteer/AutoSpeed, **Lite Models** |
| 공통 철학 | modular → monolithic → hybrid E2E 로 진화 | (좌동) |

### 트랙 A 구조도 (목표 = Architecture 2.0)

```
Autoware Architecture 2.0  (공식 "Under Construction")
└─ Generator-Selector
   ├─ Generator  (여러 개 병렬, "어떤 방식이든 궤적만 내면 됨")
   │    • rule-based / optimization  ← 기존 Autoware planner 재사용   [성숙]
   │    • Modular E2E   = Diffusion Planner  ← tracked obj + map → 궤적  [머지·실험]
   │    • Monolithic E2E = VAD / DiffusionDrive ← 카메라 → 궤적(블랙박스)  [VAD 머지·sim학습 / DDrive 진행중]
   └─ Selector
        • Safety Gate : 블랙박스 출력 안전성 검증(신호·정지선·주행가능영역)
        • Ranking     : 후보 점수화 → 최적 선택   →   Controller → 차량
```

### 부품별 현황 한눈에 (트랙 A)

| 부품 | 분류 | 상태 |
|---|---|---|
| Generator-Selector 프레임워크 | 목표 구조 | 공식 "Under Construction"; `autoware_trajectory_*` 코드 존재(양쪽 저장소) |
| Diffusion Planner | Modular E2E generator | universe 머지([PR #10957](https://github.com/autowarefoundation/autoware_universe/pull/10957)), 일본 데이터 재학습, 튜토리얼 OK. **수동 런치 패치 필요·기본값 아님** |
| VAD | Monolithic E2E generator | universe `e2e/` 머지. **CARLA-sim 학습만**, `use_e2e_planning` 미배선, 실시간 통합 이슈 |
| DiffusionDrive | Monolithic E2E generator | 재학습·ROS 노드화 **진행 중**, 미머지 |
| MTR | generator 실험(placeholder) | sim 부진(대부분 unsafe) → "plug-and-play planner 아님" |

---

## 2. 왜 바꾸는가 — AV 1.0의 한계와 AV 2.0

(출처: [tier4/new_planning_framework wiki](https://github.com/tier4/new_planning_framework/wiki), [Autoware Architecture Proposal](https://github.com/tier4/AutowareArchitectureProposal.proj))

현 Autoware 아키텍처는 **5년 전의 "Autoware Architecture Proposal"** 에 기반한다. 위키와 공식 문서가 지적하는 한계:

- **AV 1.0 (Autonomy 1.0)**: 인간이 개선 방법을 설계하고 엔지니어링으로 성능을 올리는 방식(classical robotics + 수작업 규칙). 충분히 정확한 perception만 있으면 고전 robotics planning으로 인간 수준 주행이 가능하다는 믿음.
- **한계**: long-tail(희귀 이벤트)에 약하고 지역마다 재튜닝 필요. **컴포넌트 분할로 인한 정보 손실** — perception→planning 인터페이스가 전달 가능한 정보량을 구조적으로 제약(예: "스마트폰 보며 걷는 보행자"를 표현하려면 인터페이스를 매번 확장해야 함). 공도 테스트에서 복잡·long-tail 시나리오의 override가 다수 관찰됐고, 이를 AV 1.0로 메우면 소프트웨어가 과복잡해져 품질이 저하.
- 특히 **behavior planning과 motion planning 분리에서 오는 의사결정 불일치(decision discrepancy)** 가 구조적 결함으로 지목됨.

![계층형 아키텍처의 의사결정 불일치](assets/npf/hierarchical_discrepancy.png)

- **AV 2.0 (Autonomy 2.0)**: 시스템 개선이 **데이터로 구동**되고 인간 개입 없이 자율 진화. E2E 머신러닝이 핵심 수단. 대표 오픈소스로 **UniAD, VAD**를 명시.

![AV 1.0 개념](assets/npf/av1_concept.png)

---

## 3. 목표 구조 — Autoware Architecture 2.0 (Generator-Selector)

(출처: [Autoware 공식 설계 문서 — Architecture 2.0](https://autowarefoundation.github.io/autoware-documentation/main/design/autoware-architecture-v2/), [tier4 wiki](https://github.com/tier4/new_planning_framework/wiki))

공식 문서는 전통적 고정 파이프라인을 다음처럼 규정한다:

> "Traditional autonomous driving follows a fixed pipeline: Sensing → Perception → Localization → Planning → Trajectory"

이 방식은 rule-based planner에는 맞지만 **E2E·diffusion 모델은 이 파이프라인에 들어맞지 않는다**. 그래서 Architecture 2.0은 파이프라인을 버리고 **Generator-Selector** 구조를 채택한다.

![Generator-Selector 아키텍처](assets/npf/generator_selector.png)

### Generator (궤적 생성기)
> "A Generator is any module that outputs trajectories"

- rule-based/optimization(인식·맵 사용), **E2E 모델(원시 센서 입력)**, 학습/샘플링 기반 등 무엇이든 가능.
- **여러 generator를 병렬 실행** 가능. 위 그림에서 Robotics Approach / Modular E2E / Monolithic E2E / World Model E2E가 한 "블랙박스 구름" 안에서 각자 궤적을 낸다.

### Selector (안전 검증 + 선택)
> "The Selector receives candidate trajectories and: Safety-checks them (e.g., rule compliance, drivable area), Ranks and selects the best one"

- **Safety Gate**: 블랙박스 generator 출력의 **최소 안전성 검증**(규칙 준수, 주행가능영역, 신호·정지선). 더미 pass-through부터 HD맵 기반 검증까지 플러그인.
- **Ranking**: 복수 generator 출력을 평가·순위화해 최적 선택.

### Architecture 1.0과의 차이 (공식 문서)
- **추상화 수준 상향**: 파이프라인 전반부(센싱~로컬라이제이션)를 모듈화해, **각 generator가 필요한 컴포넌트만 골라 쓰거나 우회** 가능하게 함.
- 강조하는 이점 4가지: ① robotics와 E2E planner 통합 ② 명시적 검증으로 **블랙박스 모델을 안전하게 활용** ③ 새 계획 방법 실험 유연성 ④ 여러 궤적 후보 비교로 견고한 의사결정.

> **여기가 "하이브리드"의 정체다.** 하이브리드 = 별도 시스템이 아니라, rule-based와 E2E generator를 **Safety Gate 달린 Selector로 함께 굴리는 이 구조 자체**. 완전 E2E(블랙박스)의 출력조차 Selector를 통과해야 제어로 내려간다 → "production 안전성과 E2E의 양립" 전략의 핵심.

---

## 4. Generator 쪽 — E2E의 두 종류

(출처: [tier4 wiki](https://github.com/tier4/new_planning_framework/wiki), autoware_universe 코드, arXiv 원문)

위키는 E2E를 "Perception과 Planning을 **둘 다 ML로** 구현"으로 정의하고 2종으로 나눈다. **둘은 단계가 아니라 종류이며, 병렬 개발된다.**

| 구분 | 정의 | 장점 | 단점 | 구현체 |
|---|---|---|---|---|
| **Modular / 2-model E2E** | Perception·Planning 각각 ML, **인터페이스 명시 유지** | L4 적합, 컴포넌트 단위 테스트 용이, 빠른 반복, 높은 해석성, robotics 통합 쉬움 | 성능 상한 낮음 | **Diffusion Planner** |
| **Monolithic E2E** | 인식~계획 전체를 단일 ML | 일반적으로 고성능, L2 ADAS 성공 사례 | 컴포넌트 테스트 어려움, **블랙박스(낮은 해석성)**, robotics 통합 어려움 | **VAD, DiffusionDrive** |

<table><tr>
<td><img src="assets/npf/modular_e2e.png" width="100%"><br><sub>Modular / 2-model E2E</sub></td>
<td><img src="assets/npf/monolithic_e2e.png" width="100%"><br><sub>Monolithic E2E</sub></td>
</tr></table>

### 4.1 Monolithic E2E — VAD (`e2e/autoware_tensorrt_vad`)
- **정체**: hustvl **VAD**(Vectorized Autonomous Driving, [arXiv:2303.12077](https://arxiv.org/abs/2303.12077), ICCV 2023)를 TensorRT(NVIDIA DL4AGX)로 최적화한 ROS 2 노드. README 표현 그대로 *"Single neural network directly maps camera inputs to trajectories ... no separate detection, tracking, prediction, or planning modules."*
- **입출력**: 6개 surround-view 카메라 + odometry/accel → 선택 궤적(`Trajectory`) + 6개 후보(`CandidateTrajectories`) + 예측 객체 + 맵요소(보조 출력). 추론 ~20ms, backbone FP16/head FP32.
- **모델**: v0.1(2025-11-04), **Bench2Drive CARLA** 데이터 학습.
- **도메인 분리 설계**: `VadNode`(ROS) ↔ `VadInterface`(브리지) ↔ `VadModel`(CUDA/TensorRT)로 격리.
- **한계(README/이슈)**: ① **CARLA 시뮬레이션 데이터로만 학습** → 실차 일반화 미검증. ② **high-level command 인터페이스 부재** → 런타임에 "다음 교차로 우회전" 같은 행동 전환 불가.
- **전환의 구조적 증거**: 0.49.0(2025-12-30)에서 패키지가 `planning/` → **`e2e/` 디렉토리로 이동**. 커밋 메시지: *"to align with AWF's organization of end-to-end learning-based components."* AWF가 E2E 전용 디렉토리 체계를 신설한 것.

### 4.2 Modular E2E — Diffusion Planner (`planning/autoware_diffusion_planner`)
- **정체**: Zheng et al. **Diffusion Planner**(["Diffusion-Based Planning for Autonomous Driving with Flexible Guidance"](https://arxiv.org/abs/2501.15564), ICLR 2025 Oral)를 이식. transformer 기반으로 trajectory score function의 gradient를 학습, flexible classifier guidance로 rule-based refinement 없이 궤적 생성.
- **추론**: **ONNX Runtime**(VAD가 TensorRT인 것과 대비). 모델 v4.0.
- **입출력**: odometry/accel/**tracked objects**/traffic signals/**Lanelet2 vector map**/route → 궤적·후보·예측객체·turn indicator. 즉 **카메라 raw가 아니라 기존 perception·map 출력을 입력으로 받는 "중간 단계" E2E** = modular.
- **성숙·통합**: ROS 노드화·인터페이스 통합 완료, **일본 데이터로 재학습 완료**, Autoware 튜토리얼 동작 확인. 통합 경로는 [PR #10957](https://github.com/autowarefoundation/autoware_universe/pull/10957)로 universe에 머지.
- **한계(deprecated 위키 기록)**: 목표 지점 초과 주행(route가 goal에서 안 끝남), **proprietary Lanelet2 맵 학습→타 맵 성능 급감**, 의도적 차선변경 드묾, 회피 신뢰도 낮음, **정적 객체(콘·가드레일)는 빈 텐서로 대체**.

### 4.3 Generator 실험 — MTR (교훈적 실패)
- MTR(Motion Transformer, [arXiv:2209.13508](https://arxiv.org/abs/2209.13508))을 ego 궤적 생성기로 시험. **Selector 프레임워크 개발용 placeholder**가 명시 목적.
- 6개 mode, 80 waypoint(8초), 10Hz, ~30–40ms(RTX 3090). 합성 T4 데이터(~5000→중복 ~60000 장면), batch size 6.
- **결과**: 정량 학습은 양호했으나 **sim 성능 부진**(대부분 unsafe, 맵 이탈). route·차선·turn intention 같은 **high-level guidance 부재**가 원인. 결론: **"MTR is not a plug-and-play planner"** — 본래 예측 모델이라 planning엔 goal conditioning·semantic intention·downstream selector가 필수.

![MTR 노드 출력(노란색)](assets/npf/mtr_output.png)

---

## 5. Selector 쪽 — 파이프라인과 평가

(출처: [tier4/new_planning_framework wiki·코드](https://github.com/tier4/new_planning_framework))

`autoware_trajectory_*` 패키지들이 Selector의 실제 구현체다. 사각형=ROS 노드, 화살표=토픽:

![Selector 파이프라인](assets/npf/selector_architecture.png)

```
/candidate/trajectories
 → trajectory_concatenator    (generator별 최신 후보를 단일 메시지로 병합)
 → feasible_trajectory_filter (물리 비현실/위험 폐기: 데이터 유효성·ego 근접·차선 준수·충돌위험)
 → valid_trajectory_filter    (Traffic Rule Validator = Safety Gate: 신호·정지선 위반 차단; HD/SD맵 무관)
 → trajectory_ranker          (다기준 점수화)
 → trajectory_adaptor         (최고점수 궤적 → 단일 Trajectory, 컨트롤러 호환 포맷)
 → /planning/scenario_planning/trajectory
```

> 설계 원칙(위키): filter에 규칙을 과하게 넣으면 rule-based로 회귀해 E2E generator의 강점을 훼손하므로 **최소 설계** 유지.

### Trajectory Ranker — 5메트릭 / 6구현
| 메트릭 | 의미 | 구현 |
|---|---|---|
| Safety | 충돌 위험 최소화 | 각 점의 Time-to-Collision (TTC) |
| Comfortability | 승차감 | 횡가속도 + 종방향 jerk(+종가속도) |
| Efficiency | 추진 효율 | 시작점부터 누적 주행거리 |
| Achievability | 내비 경로 추종 | 차로 중심선 대비 횡편차(+turn 지시 준수) |
| Consistency | 결정 떨림 방지 | pure-pursuit 조향각의 이전 궤적 대비 일관성 |

![Ranker 평가 함수](assets/npf/ranker_eval_function.png)

- **시간 가중**: 시각 t 값에 decay 가중 w_t — 근미래 중시. 메트릭별 가중 W_metric으로 집계해 단일 스칼라.
- **오프라인 가중 튜닝 도구**(`autoware_offline_evaluation_tools`): 주행 로그(GT 궤적+후보)를 텐서화 → PyTorch 모델에 학습형 temporal-decay·metric-importance 가중(sigmoid 재매개변수화) → **margin/triplet ranking loss**(ADE/FDE 기반 margin 자동 확대)로 GT가 후보보다 높은 점수를 받도록 학습.

### 인터페이스 메시지 (수렴 진행 중인 지점)
- `tier4/new_planning_framework`: `autoware_new_planning_msgs/Trajectories`(= `Trajectory[]` + `TrajectoryGeneratorInfo[]`; Trajectory엔 generator_id·points·score), `EvaluationInfo`(score+metrics+weights) 등.
- `autoware_universe`(1.8.0): `autoware_internal_planning_msgs/CandidateTrajectories`(= `CandidateTrajectory[]` + `GeneratorInfo[]`), `ScoredCandidateTrajectories`.
- 둘은 유사하나 동일하지 않아 **`autoware_new_planning_msgs_converter`** 존재 → 업스트림 통합 과정에서 네이밍이 수렴 중.

---

## 6. 구현·논의 현황 타임라인

(출처: CHANGELOG, PR, Discussion — 날짜는 원문 기준)

- **2025-07-15** — TIER IV, Level 4+용 E2E 아키텍처 공개(diffusion+rule 하이브리드). "publicly available via Autoware". 2026 초 일본 50곳 실증 예고. ([보도자료](https://www.prnewswire.com/news-releases/tier-iv-unveils-end-to-end-architecture-for-level-4-autonomy-to-be-demonstrated-across-50-locations-nationwide-302506092.html))
- **2025-08** — Diffusion Planner universe 통합([PR #10957](https://github.com/autowarefoundation/autoware_universe/pull/10957)). [Discussion #6399](https://github.com/orgs/autowarefoundation/discussions/6399)(2025-08-14): batch=1 한계, multi-batch(08-15)·turn indicator(08-25) 등 개선.
- **2025-11-04** — VAD 모델 v0.1(Bench2Drive CARLA) 릴리스.
- **2025-12-30** — VAD 패키지 `planning/` → `e2e/` 이동(0.49.0).
- **2026-01-21** — [Discussion #6735](https://github.com/orgs/autowarefoundation/discussions/6735) "Challenges in Hybrid E2E + Rule-Based Architecture": vision E2E(VAD)를 rule 시스템과 통합 시 ① 외부 HLC가 정적 맵만 사용해 임시 장애물 미반영 ② ROS 2 지연+추론이 제어 데드라인 초과 ③ VAD 궤적이 컨트롤러 도달 시 현재 상태와 불일치. 메인테이너 응답은 프로파일링 요청 수준 — **아직 정형 해법 없음**.
- **2026-03** — TIER IV "AI-based Level 4" 발표: 두 모드(하이브리드/완전 E2E) 명문화, 글로벌 3허브. ([보도자료](https://www.prnewswire.com/news-releases/tier-iv-unveils-ai-based-level-4-autonomous-driving-accelerating-global-platform-expansion-across-japan-us-and-europe-302714131.html))
- **new_planning_framework 개발 상태(위키, 타임스탬프 없음)**: 협조 프레임워크는 MTR 노드로 검증 중(universe PR 9E 예정), **Modular E2E(diffusion) 일본 데이터 재학습·튜토리얼 OK**, **Monolithic E2E(VAD+DiffusionDrive) 재학습·성능 재현 확인 후 ROS 노드화 진행 중**(이후 CARLA 학습·튜토리얼 → universe PR).

**관찰된 "미배포" 지점**: ① VAD README의 `use_e2e_planning:=true`가 1.8.0 `e2e_simulator.launch.xml`에 **미배선**(grep 0건) ② diffusion 구동에 launch/param 수동 패치 필요(max_vel 4.17→22.2, validator 우회 등) ③ VAD CARLA-only·실시간 통합 미해결. → **코드는 머지됐으나 production 기본 경로 배선·실차 검증은 진행 중.**

![개발 일정(WIP)](assets/npf/schedule.png)

---

## 7. 별도 트랙 — autoware_vision_pilot (개인차량용 vision ADAS)

(출처: [autoware_vision_pilot 저장소](https://github.com/autowarefoundation/autoware_vision_pilot), [POV Work Group Discussion #6570](https://github.com/orgs/autowarefoundation/discussions/6570), [Autoware 블로그](https://autoware.org/introducing-lite-models/). **위 universe/Architecture 2.0와는 별개 저장소·별개 타깃**)

- **미션**: OEM·Tier-1 양산차 통합용 **"productionizable and safety certifiable" 오픈소스 ADAS/FSD**. 모델·데이터파싱·학습·**가중치 전부 공개**(Apache 2.0). 구명 `autoware.privately-owned-vehicles`.
- **차별점**: **HD맵 불필요**(mapless 또는 2D 내비맵), **vision-only**(전면 단일 카메라), 임베디드 엣지(README 본문 8–10 INT8 TOPS / 베이스 다이어그램 3–5 TOPS — 문서 내 불일치).
- **4단계 로드맵**(README 직접 확인): Vision Pilot(L2 단일차선, component E2E) → Plus(L2+ 고속도로) → PRO(L2++ 도심, **monolithic** E2E) → Drive(L4+ 전도로, **hybrid** E2E). 전환 철학은 universe와 동일.

<table><tr>
<td><img src="assets/vp/VisionPilot.png" width="100%"></td>
<td><img src="assets/vp/VisionPilot_Drive.png" width="100%"></td>
</tr></table>

### AutoSeg Foundation Model + 모델 라이브러리
**AutoSeg** = vision 파이프라인 코어가 되는 HydraNet(공유 backbone → 다중 head). **코드 확인 결과**: SceneSeg가 베이스(`Backbone=EfficientNet-B0 → SceneContext → Neck → Head`)이고, **Scene3D·DomainSeg는 SceneSeg의 Backbone+Context를 `requires_grad=False`로 frozen 재사용**(`Scene3DUpstream`/`DomainSegUpstream`)한 뒤 자기 head만 붙인다 → 진짜 공유-backbone HydraNet은 이 **3개(SceneSeg/Scene3D/DomainSeg)**. **EgoLanes는 자기 Backbone을 따로 가진 별도 망**(AutoSeg 헤드 아님, 조향 브랜치 소속).

> **아키텍처 분류**: 현재 VisionPilot(0.9)은 본인들 표현으로 **"component-based E2E"** — 과제별 별도 CNN을 차선마스크·깊이·bbox 같은 **명시적 중간표현**으로 잇고, 조향/속도는 homography·Kalman 등 **수작업 글루**로 엮는다. UniAD처럼 한 신경망이 궤적까지 뽑는 **monolithic이 아니다**(그건 로드맵상 PRO 단계). AutoSteer는 EgoLanes의 차선 마스크를 입력으로 받는다.

| 모델 | 과제 | 핵심(각 README) |
|---|---|---|
| **SceneSeg** | class-agnostic 전경 세그 | 미학습 객체(릭샤·넘어진 자전거·굴러가는 타이어)도 검출. cross-dataset **mIoU 90.7**(학습 ACDC/MUSES/IDDAW/Mapillary/Comma10K, 테스트 BDD100K) |
| **Scene3D** | 단안 상대 depth | DepthAnythingV2-Large **distillation**(488,535 샘플), Scale-Invariant+Edge loss |
| **DomainSeg** | 공사구역 세그 | CMU **ROADWork**(7.25K), mIoU 46.6 |
| **EgoLanes** | ego 차선 세그 | ego-left/right/기타 3클래스, 1/4 해상도 출력 |
| **AutoSteer 2.0** | 경로/조향 예측 | 명시적 차선검출 없이 전체 프레임 → 미래 waypoint, **mAP 0.955** |
| **AutoSpeed 2.0** | CIPO 검출 | YOLOv11 기반, in-path/cut-in-out 분류, mAP@50 0.74 |
| **AutoDrive 2.0** | temporal 거리+곡률+CIPO | 프레임쌍(t-1,t) 융합, 곡률오차 ~4°, CIPO presence 88% |
| **Lite models** | 임베디드 경량화 | 아래 |

### VisionPilot 0.9 런타임 (2026-03-02, production_release)
**횡+종 2병렬 스트림**, 표준 C++ 앱(IceOryx/Zenoh/ROS 2 레시피), **ONNX Runtime 1.22 + TensorRT 10**.

![VisionPilot 0.9 아키텍처](assets/vp/VisionPilot_0.9.png)

- **횡**: (t-1,t)→crop/resize→**EgoLanes**→**AutoSteer**(조향각)→이동평균→Steering Control. 별도 EgoLanes→BEV로 cross-track/yaw error.
- **종**: 현재 프레임→**AutoSpeed**(in-path 객체)→BEV 거리→**Kalman** 거리·속도 추적→Speed Control. 안전거리는 **Mobileye RSS** 준수, 거리=호모그래피 변환.

### Lite Models ([Autoware 블로그](https://autoware.org/introducing-lite-models/), 2026-03-04, 개발 AEI)
Jetson Orin Nano·TensorRT INT8 대상. SceneSeg Lite ~28×(10.2→87.6 FPS), Scene3D Lite ~28×(10.0→91.4), EgoLanes Lite ~20×(20.5→104.3).

### POV Work Group 현황 ([Discussion #6570](https://github.com/orgs/autowarefoundation/discussions/6570), 2025-11-10)
Zenoh 파이프라인 완성(ONNX/TensorRT), BrightDrive 실차 **Jetson Orin 10+ FPS**, AutoSpeed v1+CPU(OpenAD Kit), AutoSteer 이중 브랜치 재설계(~500k 샘플), ObjectFinder C++/Kalman. 마일스톤: 10월 말 sim 테스트→11월 말 AGX Orin 벤치→12월 말 실차 시연.

---

## 8. TIER IV 공식 발표·실증 계획 (회사 동향 / 보도자료)

> 이 섹션은 코드가 아니라 **TIER IV의 공식 보도자료(뉴스)** 기준이다. "이 기술을 실제로 어디서·언제·누구와 굴릴 계획인가"를 정리.

- **2025-07-15** ([보도자료](https://www.prnewswire.com/news-releases/tier-iv-unveils-end-to-end-architecture-for-level-4-autonomy-to-be-demonstrated-across-50-locations-nationwide-302506092.html)): Level 4+용 E2E 아키텍처 첫 공개. diffusion+rule 하이브리드, "publicly available via Autoware". **2026 초 일본 50개 지역** 대규모 실증. data-centric: Autoware 시뮬레이션으로 대규모 합성 데이터 자동 생성.
- **2026-03-15**(수정 03-20) ([보도자료](https://www.prnewswire.com/news-releases/tier-iv-unveils-ai-based-level-4-autonomous-driving-accelerating-global-platform-expansion-across-japan-us-and-europe-302714131.html)): "AI-based Level 4". **두 운영 모드 명문화** — ① **하이브리드 시스템**(diffusion으로 주변 시간변화를 확률적 포착 + 타 ML 인식 → 인간 운전 모방) ② **E2E 시스템**(벡터 표현 + **world model** 개념으로 인식·계획·제어를 단일 학습 프로세스로 통합). 글로벌 3허브: **도쿄**(도쿄대·Toyota JPN TAXI), **피츠버그**(CMU·Hyundai IONIQ 5), **뮌헨**(TUM·VW T7 Multivan). Shinpei Kato(CEO): "레벨 4+는 서비스 환경과 함께 자율 진화하는 기술이 필요."
- (참고, 세부 미검증) [NVIDIA reasoning-based AI / world foundation model 협력](https://www.prnewswire.com/news-releases/tier-iv-accelerates-ai-based-level-4-autonomous-driving-with-nvidias-reasoning-based-ai-and-world-foundation-models-302717091.html).

---

## 9. 관련 연구 계보 (arXiv 원문 확인)

| 모델/데이터셋 | 정식 제목 | 발표 | arXiv | Autoware 사용처 |
|---|---|---|---|---|
| **VAD** | Vectorized Scene Representation for Efficient Autonomous Driving | ICCV 2023 | [2303.12077](https://arxiv.org/abs/2303.12077) | `e2e/autoware_tensorrt_vad` |
| **Diffusion Planner** | Diffusion-Based Planning for Autonomous Driving with Flexible Guidance | ICLR 2025 Oral | [2501.15564](https://arxiv.org/abs/2501.15564) | `planning/autoware_diffusion_planner` |
| **MTR** | Motion Transformer with Global Intention Localization and Local Movement Refinement | NeurIPS 2022 | [2209.13508](https://arxiv.org/abs/2209.13508) | new_planning_framework 실험 노드 |
| **Bench2Drive** | Multi-Ability Benchmarking of Closed-Loop E2E AD | 2024 | [2406.03877](https://arxiv.org/abs/2406.03877) | VAD v0.1 학습(CARLA) |
| **BEVFormer** | BEV Representation from Multi-Camera via Spatiotemporal Transformers | 2022 | [2203.17270](https://arxiv.org/abs/2203.17270) | `perception/autoware_tensorrt_bevformer` |

수치(원문): VAD-Base 충돌률 −29.0%·2.5× 속도, VAD-Tiny 최대 9.3× 추론 속도. Diffusion Planner는 nuPlan + 200h 배송차 데이터에서 SOTA closed-loop, prediction·planning 공동 처리.

학습형 perception 패키지(E2E 전제 인프라, universe `perception/`): `autoware_tensorrt_bevformer`, `autoware_camera_streampetr`, `autoware_bevfusion`, `autoware_tensorrt_bevdet`, `autoware_lidar_frnet`, `autoware_ptv3`, `autoware_simpl_prediction`.

---

## 10. 검증되지 않았거나 불확실한 항목 (정직성 명시)

- **공식 문서 상태**: `autoware-architecture-v2`는 "Under Construction" — 상세 인터페이스·로드맵은 추후 공개 예정이라 본문 구조는 현 시점 스냅샷.
- **new_planning_framework 위키 "개발 상태"**: 타임스탬프 없음 → 확인 시점(2026-06) 스냅샷. "9E까지 PR" 등은 변동 가능.
- **`use_e2e_planning` 미배선**은 로컬 1.8.0 기준. `main` 브랜치엔 더 최신 배선이 있을 수 있음.
- **메시지 정의 분기**(new_planning_msgs vs internal_planning_msgs): 통합 진행 중이라 시점 의존.
- **vision_pilot 수치**: 저장소 README 원문 그대로 옮김. 단 SceneSeg FLOPs 표기가 README 간 복붙으로 보이는 불일치(223.43 vs 238.41), TOPS 표기 불일치(3–5 vs 8–10) 존재.
- **이미지**: `assets/npf/*`=new_planning_framework 위키 첨부 원본, `assets/vp/*`=vision_pilot `Media/` 원본을 그대로 내려받음(렌더 스크린샷 아님).
- **NVIDIA 협력**: 제목·존재만 확인, 본문 미검증.
- **DiffusionDrive**: 위키 언급 외 별도 1차 검증 안 함(arXiv/구현 추적 미수행).

---

## 11. 출처

### 공식 설계 문서 / 발표
- Autoware Architecture 2.0 설계: <https://autowarefoundation.github.io/autoware-documentation/main/design/autoware-architecture-v2/>
- TIER IV E2E 아키텍처 공개(2025-07-15): <https://www.prnewswire.com/news-releases/tier-iv-unveils-end-to-end-architecture-for-level-4-autonomy-to-be-demonstrated-across-50-locations-nationwide-302506092.html>
- TIER IV AI-based Level 4(2026-03): <https://www.prnewswire.com/news-releases/tier-iv-unveils-ai-based-level-4-autonomous-driving-accelerating-global-platform-expansion-across-japan-us-and-europe-302714131.html>
- TIER IV × NVIDIA(세부 미검증): <https://www.prnewswire.com/news-releases/tier-iv-accelerates-ai-based-level-4-autonomous-driving-with-nvidias-reasoning-based-ai-and-world-foundation-models-302717091.html>
- Lite Models 블로그(2026-03-04): <https://autoware.org/introducing-lite-models/> · SceneSeg: <https://autoware.org/sceneseg-autowares-open-source-vision-ai-engine/>

### GitHub (직접 클론·확인)
- tier4/new_planning_framework(코드·위키): <https://github.com/tier4/new_planning_framework> · wiki <https://github.com/tier4/new_planning_framework/wiki>
- diffusion planner universe 통합 PR: <https://github.com/autowarefoundation/autoware_universe/pull/10957>
- autoware_vision_pilot: <https://github.com/autowarefoundation/autoware_vision_pilot> (구 <https://github.com/autowarefoundation/autoware.privately-owned-vehicles>)
- Discussion #6735(hybrid 통합 과제, 2026-01-21): <https://github.com/orgs/autowarefoundation/discussions/6735>
- Discussion #6570(POV WG, 2025-11-10): <https://github.com/orgs/autowarefoundation/discussions/6570>
- Discussion #6399(diffusion 개선, 2025-08-14): <https://github.com/orgs/autowarefoundation/discussions/6399> · #5033(Generator-Selector 참조)
- 모델 구현: VAD <https://github.com/hustvl/VAD> · Diffusion-Planner <https://github.com/ZhengYinan-AIR/Diffusion-Planner>(tier4 fork <https://github.com/tier4/Diffusion-Planner>) · Bench2Drive <https://github.com/Thinklab-SJTU/Bench2Drive> · NVIDIA DL4AGX <https://github.com/NVIDIA/DL4AGX>

### 논문
- VAD 2303.12077 · Diffusion Planner 2501.15564 · MTR 2209.13508 · Bench2Drive 2406.03877 · BEVFormer 2203.17270 (§9 표)

### 로컬 소스 (Autoware 1.8.0, 직접 확인)
- `autoware_universe/e2e/autoware_tensorrt_vad/{README,CHANGELOG,docs/design.md}`, `planning/autoware_diffusion_planner/README.md`, `planning/autoware_trajectory_*`, `autoware_internal_planning_msgs/msg/*`, `autoware_launch/launch/e2e_simulator.launch.xml`

### 산업 매체 / Third-party (보조)
- ADAS & AV International(2025-07-22): <https://www.autonomousvehicleinternational.com/news/ai-sensor-fusion/tier-iv-unveils-end-to-end-architecture-for-level-4-autonomy-available-via-autoware.html>
- thinkautonomous(강연 해설, 4단계 로드맵은 비공식 해석): <https://www.thinkautonomous.ai/blog/autoware-end-to-end/>
