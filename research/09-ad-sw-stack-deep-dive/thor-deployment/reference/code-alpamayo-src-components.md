# Alpamayo 1 · 1.5 · 2 Super 소스 코드 기반 컴포넌트 근거

작성일: 2026-09-16 · 대상: 고정 커밋 클론(depth 1)의 코드 읽기. 실행 검증 아님. ROS 2·Autoware 통합(alpamayo-autoware)은 제외.

Alpamayo 1·1.5·2 Super 소스 컴포넌트 그림의 박스별 근거, 궤적 추론 호출 순서, 공식 자료 대조, 이전 버전 대비 차이를 기록한다. 공식 자료(HF 모델카드·NVIDIA 블로그·arXiv 2511.00088)는 WebFetch로 열람했으며 요약 경유 항목은 원문 재확인이 필요하다.

## 그림 읽는 법

- **종류**: `class`(클래스) · `method`(`클래스.메서드`) · `function`(모듈 최상위 함수, 필요하면 `모듈.함수`) · `attribute`(모델 객체가 가진 하위 모듈, `클래스.속성`) · `module .py`(파일 전체) · `script` · `notebook` · `pip package` · `HF Hub`(체크포인트·데이터셋) · `환경` · `코드에 없음`(grep·find로 확인).
- **이름**: 코드에 적힌 식별자 그대로.
- **설명**: 이 문서가 붙인 한국어 역할 요약.
- **정의 위치**: `src/<패키지>/` 기준 `파일:줄`. `pyproject.toml`·`README.md`·`notebooks/`·`examples/`는 저장소 루트 기준. `from_pretrained`는 transformers에서 상속한 메서드라 호출 위치를 적었다.
- **단계**: 궤적 추론 호출 순서에서 이 컴포넌트가 실행되는 단계 번호(범위).

## Alpamayo 1

- 저장소: https://github.com/NVlabs/alpamayo @ `11a0e01c13a5622377c45ee37d653351453ec43b` (2026-09-09) [K6] · 패키지 경로 `src/alpamayo_r1/`
- 그림: [04-alpamayo1-src-components.svg](../images/04-alpamayo1-src-components.svg)

### L6 Applications · 실행 진입점

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| script | `test_inference.py` | 예제 클립 1개로 궤적·CoC 추론 후 minADE 출력 (모듈 최상위 코드) | `test_inference.py:31-72` | 1–12 |  |
| notebook | `notebooks/inference.ipynb` | 추론 + 카메라·궤적 시각화 데모 | `notebooks/inference.ipynb` |  |  |
| 코드에 없음 | `학습 스크립트 (SFT·RL)` | 이 저장소는 추론 전용. 학습 코드는 alpamayo-recipes | `grep -rniE 'optimizer\|deepspeed\|backward\(' → 0건` |  |  |

### L5 Inference API

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| method | `AlpamayoR1.from_pretrained` | HF 체크포인트에서 모델 객체 생성·가중치 적재 | `상속(transformers) · 호출 test_inference.py:35` | 3 |  |
| method | `AlpamayoR1.sample_trajectories_from_data_with_vlm_rollout` | 궤적 추론 메인 API: CoC 텍스트 생성 → 궤적 샘플링 | `models/alpamayo_r1.py:150` | 5–11 |  |
| method | `AlpamayoR1.enable_diffusion_expert_cuda_graph` | 선택: expert 반복 계산을 CUDA graph로 가속 | `models/alpamayo_r1.py:130` |  |  |

### L4 Model

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `AlpamayoR1` | 최상위 모델. ReasoningVLA를 상속하고 expert·궤적 디코더를 추가 | `models/alpamayo_r1.py:80` | 3–11 |  |
| class | `ReasoningVLA` | 부모 클래스. VLM·토크나이저 생성, 궤적 토큰 삽입(TrajectoryFusionMixin) | `models/base_model.py:285` | 3·6 |  |
| attribute | `AlpamayoR1.vlm` | Qwen3VLForConditionalGeneration 객체. 이미지+프롬프트로 CoC 생성 (ReasoningVLA가 생성) | `models/base_model.py:381` | 7 |  |
| attribute | `AlpamayoR1.expert` | action expert 트랜스포머. VLM text_config 복제(AutoModel.from_config) | `models/alpamayo_r1.py:99` | 9 |  |
| attribute | `AlpamayoR1.action_in_proj` | 노이즈 action + 시간 t → expert 입력 임베딩 | `models/alpamayo_r1.py:109` | 9 |  |
| attribute | `AlpamayoR1.action_out_proj` | expert 출력 → action 속도장 (64×2). 클래스 정의는 저장소에 없음 | `models/alpamayo_r1.py:114` | 9 |  |

### L3 Model Building Blocks

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `AlpamayoR1Config` | 모델 설정. 하위 모듈 hydra cfg 보관 (ReasoningVLAConfig 상속) | `config.py:23` |  |  |
| class | `FlowMatching` | AlpamayoR1.diffusion 으로 생성. 노이즈에서 Euler 10스텝으로 action 샘플링 | `diffusion/flow_matching.py:22` | 8 |  |
| class | `UnicycleAccelCurvatureActionSpace` | AlpamayoR1.action_space 로 생성. (가속도, 곡률) → xyz·회전 적분 | `action_space/unicycle_accel_curvature.py:38` | 10 |  |
| class | `PerWaypointActionInProjV2` | action_in_proj 구현: waypoint별 Fourier 인코딩 + MLP | `models/action_in_proj.py:104` | 9 |  |
| class | `DeltaTrajectoryTokenizer` | hist_traj_tokenizer 구현: 과거 궤적 → 이산 토큰 | `models/delta_tokenizer.py:21` | 6 |  |
| class | `ExpertLogitsProcessor` | CoC 생성 중 궤적 토큰이 나오지 않게 logit 마스킹 | `models/alpamayo_r1.py:46` | 7 |  |

### L2 Data · Pre/Post-processing

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| function | `load_physical_aiavdataset` | 데이터셋 클립 → 4캠×4프레임 영상, 자차 과거·미래 궤적 | `load_physical_aiavdataset.py:27` | 1 |  |
| function | `helper.create_message` | 채팅 메시지 구성: 이미지 16장 + 궤적 자리표시 48개 | `helper.py:28` | 2 |  |
| function | `helper.get_processor` | Qwen3-VL-2B processor에 모델 토크나이저를 결합 | `helper.py:71` | 4 |  |
| method | `TrajectoryFusionMixin.fuse_traj_tokens` | 프롬프트의 궤적 자리표시를 과거 궤적 토큰으로 치환 (ReasoningVLA가 상속) | `models/base_model.py:168` | 6 |  |
| function | `extract_text_tokens` | 생성 토큰에서 cot 등 텍스트 구간 추출 | `models/token_utils.py:151` | 11 |  |
| module .py | `geometry/rotation.py` | 회전행렬·yaw 변환 유틸 | `geometry/rotation.py:25` |  |  |

### L1 Libraries · Runtime

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| pip package | `torch 2.8.0` |  | `pyproject.toml:11` |  |  |
| pip package | `transformers 4.57.1` | Qwen3-VL 모델·generate·AutoModel | `pyproject.toml:13` |  |  |
| pip package | `flash-attn 2.8.3` | VLM attention 커널 | `pyproject.toml:14 (>=) · uv.lock` |  |  |
| pip package | `hydra-core 1.3.2` | config의 _target_으로 부품 객체 생성 | `pyproject.toml:8 (>=) · uv.lock` |  |  |
| pip package | `einops 0.8.2` |  | `pyproject.toml:7 (>=) · uv.lock` |  |  |
| pip package | `physical_ai_av 0.2.0` | PhysicalAI AV 데이터셋 인터페이스 | `pyproject.toml:9 (>=) · uv.lock` |  |  |
| pip package | `scipy 1.17.1` | 회전(쿼터니언→회전행렬) | `pyproject.toml:15 · uv.lock` |  |  |
| 코드에 없음 | `TensorRT · ONNX · 양자화` | 배포용 변환·양자화 경로 없음 | `grep -rniE 'tensorrt\|onnx\|quantiz\|fp8' → 0건` |  |  |

### L0 Platform

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| 환경 | `Python 3.12` |  | `pyproject.toml:4` |  |  |
| 환경 | `NVIDIA GPU ≥24 GB · bfloat16` | CUDA 필수, 단일 GPU | `README.md:50 · test_inference.py:35` |  |  |
| HF Hub | `nvidia/Alpamayo-R1-10B` | 가중치 약 22 GB (gated) | `test_inference.py:35 · README.md:94` |  |  |
| HF Hub | `nvidia/PhysicalAI-Autonomous-Vehicles` | 입력 클립 데이터셋 (gated, 스트리밍) | `README.md:76` |  |  |

### 궤적 추론 호출 순서 (test_inference.py 기준)

| 단계 | 위치 | 내용 |
|---|---|---|
| 1 | `test_inference.py:31` | load_physical_aiavdataset(clip_id) → 영상·자차 궤적 로드 |
| 2 | `test_inference.py:33` | helper.create_message → 채팅 메시지 |
| 3 | `test_inference.py:35` | AlpamayoR1.from_pretrained(bf16).to("cuda") → AlpamayoR1·ReasoningVLA __init__에서 vlm·expert·부품 생성 |
| 4 | `test_inference.py:36-52` | helper.get_processor → apply_chat_template → to_device |
| 5 | `test_inference.py:56` | AlpamayoR1.sample_trajectories_from_data_with_vlm_rollout 호출 |
| 6 | `models/alpamayo_r1.py:190` | self.fuse_traj_tokens: 과거 궤적 → hist_traj_tokenizer 토큰 삽입 |
| 7 | `models/alpamayo_r1.py:211-220` | self.vlm.generate (+ExpertLogitsProcessor) → CoC 텍스트 + KV 캐시 |
| 8 | `models/alpamayo_r1.py:325` | self.diffusion.sample (FlowMatching) → Euler 10스텝 시작 |
| 9 | `models/alpamayo_r1.py:292-309` | 매 스텝: action_in_proj → expert(VLM KV 캐시 조건) → action_out_proj |
| 10 | `models/alpamayo_r1.py:341` | self.action_space.action_to_traj → pred_xyz, pred_rot (64점) |
| 11 | `models/alpamayo_r1.py:355` | extract_text_tokens → extra["cot"] |
| 12 | `test_inference.py:66-72` | CoC 출력, 정답 궤적과 비교해 minADE 출력 |

### 핵심 수치

| 항목 | 값 | 근거 | 공식 자료 |
|---|---|---|---|
| 카메라 수 | 4 (cross_left_120fov, front_wide_120fov, cross_right_120fov, front_tele_30fov) | src/alpamayo_r1/load_physical_aiavdataset.py:73-79 | HF model card: 4 cameras |
| 카메라당 프레임 | 4 (t0-0.3s…t0, 0.1s 간격) | src/alpamayo_r1/load_physical_aiavdataset.py:36 · src/alpamayo_r1/load_physical_aiavdataset.py:164-168 | HF model card: 4 frames/camera |
| 이미지 픽셀 범위(processor) | min_pixels=163840, max_pixels=196608 | src/alpamayo_r1/helper.py:23-24 | HF model card: 320x576으로 downsample (320×576=184320, 범위 내) |
| processor 기반 모델 | Qwen/Qwen3-VL-2B-Instruct (tokenizer는 모델 것으로 교체) | src/alpamayo_r1/helper.py:25 · src/alpamayo_r1/helper.py:78-79 |  |
| ego 과거 궤적 | 16 points @10Hz (1.6s), xyz + 3×3 rot | src/alpamayo_r1/load_physical_aiavdataset.py:32 · src/alpamayo_r1/load_physical_aiavdataset.py:49 | HF model card: 16 waypoints at 10Hz |
| 과거 궤적 토큰 placeholder | 48개 <\|traj_history\|> | src/alpamayo_r1/helper.py:34-37 |  |
| 출력 궤적 | 64 waypoints, dt=0.1s → 6.4s; action dims (64, 2)=(accel, curvature) | src/alpamayo_r1/action_space/unicycle_accel_curvature.py:51-52 · src/alpamayo_r1/action_space/unicycle_accel_curvature.py:100-102 | HF model card / arXiv §3.2.2: 64 waypoints, 6.4s |
| flow matching 추론 step 기본값 | num_inference_steps=10, int_method=euler (코드 기본값; 체크포인트 config로 덮어쓸 수 있음) | src/alpamayo_r1/diffusion/flow_matching.py:34-36 · src/alpamayo_r1/diffusion/flow_matching.py:123 | arXiv §5.1: δt=0.1 during inference |
| 샘플링 파라미터(메서드 기본값) | top_p=0.98, temperature=0.6, top_k=None, num_traj_samples=6, num_traj_sets=1 | src/alpamayo_r1/models/alpamayo_r1.py:153-157 |  |
| 샘플링 파라미터(test_inference.py) | num_traj_samples=1, max_generation_length=256, seed 42 | src/alpamayo_r1/test_inference.py:54-62 |  |
| 궤적 이산 토큰 vocab | traj_vocab_size=768 (<i0>…<i767>), tokens_per_future_traj=64 | src/alpamayo_r1/models/base_model.py:211-213 · src/alpamayo_r1/models/base_model.py:338-341 |  |
| 파라미터 수 | 총 10B = backbone 8.2B + action expert 2.3B (코드에서 확인 불가) |  | HF model card: Model Architecture |
| 체크포인트 크기 | 약 22GB | README.md:94 | GitHub README |
| 최소 VRAM | 24GB | README.md:50 · README.md:174 | HF model card |

### 공식 자료 용어 ↔ 코드 이름

| 공식 자료 용어 | 코드 이름 | 판정 | 근거 |
|---|---|---|---|
| Chain of Causation (CoC) | cot (<\|cot_start\|>/<\|cot_end\|>, extra["cot"]) | 명칭 다름 | src/alpamayo_r1/helper.py:64 · src/alpamayo_r1/models/token_utils.py:164 · src/alpamayo_r1/test_inference.py:66 |
| Cosmos-Reason VLM backbone | vlm = Qwen3VLForConditionalGeneration (기본 vlm_name_or_path Qwen/Qwen3-VL-8B-Instruct) | 명칭 다름 | src/alpamayo_r1/models/base_model.py:207 · src/alpamayo_r1/models/base_model.py:381 |
| Action expert | expert | 일치 | src/alpamayo_r1/models/alpamayo_r1.py:99 |
| Flow matching trajectory decoder | FlowMatching / diffusion | 일치 | src/alpamayo_r1/diffusion/flow_matching.py:22 · src/alpamayo_r1/models/alpamayo_r1.py:104 |
| Unicycle dynamics (acceleration, curvature) | UnicycleAccelCurvatureActionSpace | 일치 | src/alpamayo_r1/action_space/unicycle_accel_curvature.py:38-39 |
| Discrete trajectory tokens (Action Modality Injection) | traj_vocab_size / <iN> 토큰, DiscreteTrajectoryTokenizer | 일치 | src/alpamayo_r1/models/base_model.py:338-341 · src/alpamayo_r1/action_space/discrete_action_space.py:24 |
| Egomotion history input | ego_history_xyz / ego_history_rot, fuse_traj_tokens | 명칭 다름 | src/alpamayo_r1/models/alpamayo_r1.py:180-190 |
| RL post-training (GRPO) | (없음) | 코드에 없음 | grep -rniE 'grpo\|reward' src → 0건 · README.md:27 |
| Route/navigation conditioning | route_start/route_pad/route_end 특수 토큰 이름만 정의 | 코드에 없음 | src/alpamayo_r1/models/base_model.py:67-69 · README.md:143 |
| Meta-action / VQA | meta_action, answer 추출 키만 존재 | 코드에 없음 | src/alpamayo_r1/models/token_utils.py:164 · README.md:144 |

### 각주

- 정의 위치 경로는 src/<패키지>/ 기준이다. pyproject.toml·README.md·notebooks/·examples/는 저장소 루트 기준이다.
- from_pretrained는 transformers PreTrainedModel에서 상속한 메서드라 저장소에 정의가 없어, 호출 위치를 적었다.
- L3 부품(diffusion·action_space·action_in/out_proj·궤적 토크나이저)은 체크포인트 config.json의 hydra _target_으로 주입된다. 저장소에 구현이 하나뿐인 클래스를 적었으며 실제 체크포인트 값은 확인하지 않았다(출처 미확인).
- 코드 읽기 기반이며 실행 검증이 아니다. 근거: reference/code-alpamayo-src-components.md
- get_processor는 Qwen/Qwen3-VL-2B-Instruct processor를 불러오지만(helper.py:25) config 기본 백본 경로는 Qwen/Qwen3-VL-8B-Instruct다(models/base_model.py:207).
- 파라미터 수(백본 8.2B + expert 2.3B)는 HF 모델카드 기재이며 코드로 확인되지 않는다.

## Alpamayo 1.5

- 저장소: https://github.com/NVlabs/alpamayo1.5 @ `36aeb4c5938cbc2eb2aed33b22434773da4ab639` (2026-09-09) [K7] · 패키지 경로 `src/alpamayo1_5/`
- 그림: [05-alpamayo1_5-src-components.svg](../images/05-alpamayo1_5-src-components.svg)

### L6 Applications · 실행 진입점

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| script | `test_inference.py` | 예제 클립 궤적·CoC 추론 후 minADE 출력 | `test_inference.py:29 (main)` | 1–12 |  |
| notebook | `notebooks/inference.ipynb` | 기본 궤적 + CoC 추론 데모 | `notebooks/inference.ipynb` |  |  |
| notebook | `notebooks/inference_nav.ipynb` | 내비 지시문 조건·CFG 비교 데모 | `notebooks/inference_nav.ipynb` |  | ✓ |
| notebook | `notebooks/inference_cam_num.ipynb` | 카메라 1·2·4대 입력 비교 데모 | `notebooks/inference_cam_num.ipynb` |  | ✓ |
| notebook | `notebooks/inference_vqa.ipynb` | 영상 질의응답(VQA) 데모 | `notebooks/inference_vqa.ipynb` |  | ✓ |
| 코드에 없음 | `학습 스크립트 · TensorRT/ONNX` | 학습(SFT·RL)은 alpamayo-recipes, 배포 변환 없음 | `grep 'optimizer\|backward\|tensorrt\|onnx' → 0건` |  |  |

### L5 Inference API

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| method | `Alpamayo1_5.from_pretrained` | HF 체크포인트에서 모델 객체 생성·가중치 적재 | `상속(transformers) · 호출 test_inference.py:39` | 3 |  |
| method | `Alpamayo1_5.sample_trajectories_from_data_with_vlm_rollout` | 궤적 추론 메인 API: CoC 생성 → 궤적 샘플링 | `models/alpamayo1_5.py:244` | 5–12 |  |
| method | `Alpamayo1_5.sample_trajectories_from_data_with_vlm_rollout_cfg_nav` | 내비 CFG: 내비 문장을 뺀 입력의 KV 캐시를 하나 더 만들어 궤적을 보정 | `models/alpamayo1_5.py:440` |  | ✓ |
| method | `ReasoningVLA.generate_text` | VLM으로 텍스트만 생성 (VQA) | `models/base_model.py:456` |  | ✓ |
| function | `nav_utils.compare_nav_conditions` | 내비 있음·없음·반대 방향 3조건 궤적 비교 | `nav_utils.py:69` |  | ✓ |

### L4 Model

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `Alpamayo1_5` | 최상위 모델. ReasoningVLA를 상속하고 expert·궤적 디코더를 추가 | `models/alpamayo1_5.py:87` | 3–12 |  |
| class | `ReasoningVLA` | 부모 클래스. VLM·토크나이저 생성, 궤적 토큰 삽입, generate_text | `models/base_model.py:292` | 3·6 |  |
| attribute | `Alpamayo1_5.vlm` | Qwen3VLForConditionalGeneration 객체. CoC 생성 (ReasoningVLA가 생성) | `models/base_model.py:390` | 7 |  |
| attribute | `Alpamayo1_5.expert` | action expert 트랜스포머. VLM이 flash_attention_2면 expert만 sdpa 강제 | `models/alpamayo1_5.py:110` | 10 | ✓ |
| attribute | `Alpamayo1_5.action_in_proj` | 노이즈 action + 시간 t → expert 입력 임베딩 | `models/alpamayo1_5.py:120` | 10 |  |
| attribute | `Alpamayo1_5.action_out_proj` | expert 출력 → action 속도장. 클래스 정의는 저장소에 없음 | `models/alpamayo1_5.py:125` | 10 |  |

### L3 Model Building Blocks

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `Alpamayo1_5Config` | 모델 설정. 하위 모듈 hydra cfg 보관 (ReasoningVLAConfig 상속) | `config.py:23` |  |  |
| class | `FlowMatching` | Alpamayo1_5.diffusion. Euler 10스텝 샘플링 + CFG 합성(_guided_v) | `diffusion/flow_matching.py:22` | 9 | ✓ |
| class | `UnicycleAccelCurvatureActionSpace` | Alpamayo1_5.action_space. (가속도, 곡률) → xyz·회전 적분 | `action_space/unicycle_accel_curvature.py:38` | 11 |  |
| class | `PerWaypointActionInProjV2` | action_in_proj 구현: waypoint별 Fourier 인코딩 + MLP | `models/action_in_proj.py:104` | 10 |  |
| class | `DeltaTrajectoryTokenizer` | hist_traj_tokenizer 구현: 과거 궤적 → 이산 토큰 | `models/delta_tokenizer.py:21` | 6 |  |
| class | `ExpertLogitsProcessor` | CoC 생성 중 궤적 토큰 logit 마스킹 | `models/alpamayo1_5.py:53` | 7 |  |

### L2 Data · Pre/Post-processing

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| function | `load_physical_aiavdataset` | 클립 → 카메라×4프레임 영상, 자차 궤적 (카메라 부분집합 가능) | `load_physical_aiavdataset.py:27` | 1 |  |
| function | `helper.create_message` | 채팅 메시지: 카메라 이름·프레임 번호, 내비 문장(route) 포함 | `helper.py:77` | 2 | ✓ |
| function | `helper.create_vqa_message` | 질문을 넣은 VQA 메시지 | `helper.py:145` |  | ✓ |
| function | `helper.get_processor` | Qwen3-VL-2B processor + 모델 토크나이저 | `helper.py:190` | 4 |  |
| method | `TrajectoryFusionMixin.fuse_traj_tokens` | 궤적 자리표시를 과거 궤적 토큰으로 치환 (ReasoningVLA가 상속) | `models/base_model.py:172` | 6 |  |
| function | `extract_text_tokens` | 생성 토큰에서 cot·answer 등 텍스트 추출 | `models/token_utils.py:151` | 12 |  |
| module .py | `nav_utils.py` | 내비 문장 조작: swap_direction, remove_nav_text | `nav_utils.py:199` |  | ✓ |
| module .py | `viz_utils.py` | BEV 궤적 비교·카메라 그리드 그림 | `viz_utils.py:97` |  | ✓ |

### L1 Libraries · Runtime

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| pip package | `torch 2.8.0` |  | `pyproject.toml:14` |  |  |
| pip package | `transformers 4.57.1` | Qwen3-VL 모델·generate·AutoModel | `pyproject.toml:16` |  |  |
| pip package | `flash-attn 2.8.3` | VLM attention 커널 | `pyproject.toml:17 (>=) · uv.lock` |  |  |
| pip package | `hydra-core 1.3.2` | config의 _target_으로 부품 객체 생성 | `pyproject.toml:10 (>=) · uv.lock` |  |  |
| pip package | `einops 0.8.1` |  | `pyproject.toml:8 (>=) · uv.lock` |  |  |
| pip package | `physical-ai-av 0.2.0` | PhysicalAI AV 데이터셋 인터페이스 | `pyproject.toml:12` |  |  |
| 코드에 없음 | `TensorRT · ONNX · 양자화` | 배포용 변환·양자화 경로 없음 | `grep -rniE 'tensorrt\|onnx\|quantiz\|fp8' → 0건` |  |  |

### L0 Platform

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| 환경 | `Python 3.12` |  | `pyproject.toml:4` |  |  |
| 환경 | `NVIDIA GPU ≥24 GB` | VRAM(H100): 샘플 1개 ~24 · 16개 ~40 · 16개+CFG ~60 GB | `README.md:37-41` |  | ✓ |
| 환경 | `bfloat16 · flash_attention_2 / sdpa` | VLM FA2 기본, expert는 sdpa | `models/base_model.py:218,226` |  |  |
| HF Hub | `nvidia/Alpamayo-1.5-10B` | 가중치 약 22 GB (gated) | `test_inference.py:39 · README.md:83` |  | ✓ |
| HF Hub | `nvidia/PhysicalAI-Autonomous-Vehicles` | 입력 클립 데이터셋 (gated) | `README.md:66` |  |  |

### 궤적 추론 호출 순서 (test_inference.py main() 기준)

| 단계 | 위치 | 내용 |
|---|---|---|
| 1 | `test_inference.py:33` | load_physical_aiavdataset(clip_id) → 영상·자차 궤적 로드 |
| 2 | `test_inference.py:35` | helper.create_message(frames, camera_indices) → 채팅 메시지 |
| 3 | `test_inference.py:39` | Alpamayo1_5.from_pretrained(bf16).to("cuda") → vlm·expert·부품 생성 |
| 4 | `test_inference.py:40-56` | helper.get_processor → apply_chat_template → to_device |
| 5 | `test_inference.py:60` | Alpamayo1_5.sample_trajectories_from_data_with_vlm_rollout 호출 |
| 6 | `models/alpamayo1_5.py:285` | self.fuse_traj_tokens: 과거 궤적 토큰 삽입 |
| 7 | `models/alpamayo1_5.py:306-315` | self.vlm.generate (+ExpertLogitsProcessor) → CoC 텍스트 + KV 캐시 |
| 8 | `models/alpamayo1_5.py:343` | _build_expert_pos_ids_and_attn_mask → expert 위치·마스크 |
| 9 | `models/alpamayo1_5.py:400` | self.diffusion.sample (FlowMatching) → Euler 10스텝 시작 |
| 10 | `models/alpamayo1_5.py:367-384` | 매 스텝: action_in_proj → expert(KV 캐시 조건) → action_out_proj |
| 11 | `models/alpamayo1_5.py:416` | self.action_space.action_to_traj → pred_xyz, pred_rot |
| 12 | `models/alpamayo1_5.py:430 · test_inference.py:69-75` | extract_text_tokens → extra["cot"], minADE 출력 |

### 핵심 수치

| 항목 | 값 | 근거 | 공식 자료 |
|---|---|---|---|
| 기본 카메라 수 | 4 (CROSS_LEFT_120FOV, FRONT_WIDE_120FOV, CROSS_RIGHT_120FOV, FRONT_TELE_30FOV) | src/alpamayo1_5/load_physical_aiavdataset.py:73-79 | HF model card: 4 cameras by default |
| 가변 카메라 | camera_features 인자로 임의 부분집합; 인덱스 0~6 총 7종 매핑, 프롬프트에 CAMERA_DISPLAY_NAMES 삽입. 노트북에서 1/2/4대 시연 | src/alpamayo1_5/load_physical_aiavdataset.py:81-89 · src/alpamayo1_5/helper.py:27-35 · notebooks/inference_cam_num.ipynb:cell6 | README FAQ |
| 카메라당 프레임 | 4 (t0-0.3s…t0, 0.1s 간격) | src/alpamayo1_5/load_physical_aiavdataset.py:36 · src/alpamayo1_5/load_physical_aiavdataset.py:162-165 | HF model card: 4 frames per camera |
| 이미지 픽셀 범위 | MIN_PIXELS=163840, MAX_PIXELS=196608 (프로세서 리사이즈 범위) | src/alpamayo1_5/helper.py:23-24 | HF model card: 320x576(=184320px), 범위 내 |
| ego 이력 | num_history_steps=16, time_step=0.1s (1.6s); 프롬프트 <\|traj_history\|> 48개 | src/alpamayo1_5/load_physical_aiavdataset.py:32-34 · src/alpamayo1_5/helper.py:106-109 | HF model card는 0.4s history로 기재 → 코드 기본값과 불일치 |
| 출력 궤적 | n_waypoints=64, dt=0.1 (6.4s), action dims (64,2) | src/alpamayo1_5/action_space/unicycle_accel_curvature.py:49-50 · src/alpamayo1_5/action_space/unicycle_accel_curvature.py:102 · src/alpamayo1_5/load_physical_aiavdataset.py:33 | README.md:205, HF model card: 64 waypoints at 10Hz |
| flow matching 스텝 | num_inference_steps 기본 10, int_method euler (실제 값은 HF config diffusion_cfg가 결정, 저장소 코드로 확인 불가) | src/alpamayo1_5/diffusion/flow_matching.py:34-35 | HF model card: 출처 미확인(명시 없음) |
| VLM 샘플링 | top_p=0.98, temperature=0.6, top_k=None; num_traj_samples 메서드 기본 6, test_inference 1, 노트북 16; max_generation_length=256 | src/alpamayo1_5/models/alpamayo1_5.py:247-250 · src/alpamayo1_5/test_inference.py:62-65 · notebooks/inference_cam_num.ipynb:cell8 |  |
| 궤적 토큰 어휘 | traj_vocab_size=768 (<i0>…<i767>), tokens_per_future_traj=64 기본 | src/alpamayo1_5/models/base_model.py:215-217 · src/alpamayo1_5/models/base_model.py:271 |  |
| CFG | v = (1-α)·unguided + α·guided; inference_guidance_weight 기본 1.0, 노트북 1.5; use_classifier_free_guidance 기본 False; unguided는 <\|route_start\|>…<\|route_end\|> 제거 입력 | src/alpamayo1_5/diffusion/flow_matching.py:136 · src/alpamayo1_5/diffusion/flow_matching.py:36 · src/alpamayo1_5/diffusion/base.py:51 · src/alpamayo1_5/models/alpamayo1_5.py:552-555 · notebooks/inference_nav.ipynb:cell14 | Guided Flows arXiv 2311.13443 eq.6 (코드 주석) |
| 초기 노이즈 temperature | diffusion_kwargs temperature 기본 1.0, 내비 노트북 0.6 | src/alpamayo1_5/diffusion/flow_matching.py:64 · src/alpamayo1_5/diffusion/flow_matching.py:171 · notebooks/inference_nav.ipynb:cell11 |  |
| VRAM (README, H100 측정) | num_traj_samples=1 ~24GB / 16 ~40GB / 16+CFG ~60GB | README.md:35-41 | README Hardware requirements |
| 체크포인트 | nvidia/Alpamayo-1.5-10B, 가중치 다운로드 22GB | README.md:83 · src/alpamayo1_5/test_inference.py:39 | HF model card: Backbone 8.2B + Action Expert 2.3B |
| 백본 기본 경로 | vlm_name_or_path='Qwen/Qwen3-VL-8B-Instruct', vlm_backend='qwenvl3'; 프로세서는 Qwen/Qwen3-VL-2B-Instruct | src/alpamayo1_5/models/base_model.py:211-212 · src/alpamayo1_5/helper.py:25 | HF model card: Cosmos-Reason2 / Qwen3-VL-8B-Instruct 기반 |
| CUDA graph (선택) | enable_diffusion_expert_cuda_graph(max_batch_size, max_graphs=4), eval·CUDA 필수 | src/alpamayo1_5/models/alpamayo1_5.py:141-152 · src/alpamayo1_5/models/diffusion_expert_cuda_graph.py:115-123 | README Optional CUDA graph acceleration |

### 공식 자료 용어 ↔ 코드 이름

| 공식 자료 용어 | 코드 이름 | 판정 | 근거 |
|---|---|---|---|
| Cosmos-Reason (VLM backbone) | Qwen3VLForConditionalGeneration (self.vlm) | 명칭 다름 | src/alpamayo1_5/models/base_model.py:390; 모델 카드는 Cosmos-Reason2(Qwen3-VL-8B-Instruct 기반) |
| action expert | expert | 일치 | src/alpamayo1_5/models/alpamayo1_5.py:110 |
| diffusion-based trajectory decoder (flow matching) | FlowMatching | 명칭 다름 | src/alpamayo1_5/diffusion/flow_matching.py:22; 초록은 diffusion-based로 표기, flow matching 명칭은 논문 본문 미확인 |
| Chain of Causation (CoC) | cot (<\|cot_start\|>, extra["cot"]) | 명칭 다름 | src/alpamayo1_5/helper.py:140; src/alpamayo1_5/models/token_utils.py:166 |
| unicycle(가속도·곡률) action 표현 | UnicycleAccelCurvatureActionSpace | 일치 | src/alpamayo1_5/action_space/unicycle_accel_curvature.py:38; 논문 본문 대조는 출처 미확인 |
| discrete trajectory tokens | traj_vocab_size / ExpertLogitsProcessor(추론 시 마스킹) | 명칭 다름 | src/alpamayo1_5/models/base_model.py:271; src/alpamayo1_5/models/alpamayo1_5.py:53 |
| RL post-training | — | 코드에 없음 | README.md:14, 206 (alpamayo-recipes에 존재) |
| meta action | extract_text_tokens의 'meta_action' 키 | 코드에 없음 | 1.5 SPECIAL_TOKENS_KEYS에서 meta_action_start/end가 _padding_2/3으로 대체(base_model.py:59-60), 추출 키만 잔존(token_utils.py:166) |
| real-time latency 99ms | — | 코드에 없음 | arXiv 2511.00088 초록; 저장소에 벤치마크 코드 없음 |

### Alpamayo 1 대비 차이

| 항목 | 내용 | 근거 |
|---|---|---|
| 패키지·클래스·체크포인트 이름 | alpamayo_r1.AlpamayoR1 / nvidia/Alpamayo-R1-10B → alpamayo1_5.Alpamayo1_5 / nvidia/Alpamayo-1.5-10B | alpamayo:src/alpamayo_r1/test_inference.py:35 · alpamayo1.5:src/alpamayo1_5/test_inference.py:39 |
| 내비게이션 조건화 | create_message(nav_text) → <\|route_start\|>…<\|route_end\|>; nav_utils(compare_nav_conditions, swap_direction, remove_nav_text) 신규 | src/alpamayo1_5/helper.py:113 · src/alpamayo1_5/models/base_model.py:71-73 · src/alpamayo1_5/nav_utils.py:69 |
| CFG(Classifier-Free Guidance) | sample_trajectories_from_data_with_vlm_rollout_cfg_nav 신규, BaseDiffusion.use_classifier_free_guidance, FlowMatching._guided_v·unguided_step_fn 추가 | src/alpamayo1_5/models/alpamayo1_5.py:440 · src/alpamayo1_5/diffusion/base.py:51 · src/alpamayo1_5/diffusion/flow_matching.py:115 |
| VQA | ReasoningVLA.generate_text, helper.create_vqa_message, question/answer 특수 토큰 신규 | src/alpamayo1_5/models/base_model.py:456 · src/alpamayo1_5/helper.py:145 · src/alpamayo1_5/models/base_model.py:74-77 |
| 가변 카메라 수 | 로더의 camera_features 인자는 1에도 있음. 1.5는 프롬프트에 카메라명·frame 번호를 넣는 _build_image_content, CAMERA_DISPLAY_NAMES와 데모 노트북 추가 | alpamayo:src/alpamayo_r1/load_physical_aiavdataset.py:35 · alpamayo:src/alpamayo_r1/helper.py:28 · src/alpamayo1_5/helper.py:38 |
| 특수 토큰 정리 | meta_action_start/end, vectorized_wm*, *_pre_tkn 제거 → _padding_N으로 교체 | alpamayo:src/alpamayo_r1/models/base_model.py:55 · alpamayo:src/alpamayo_r1/models/base_model.py:63 · src/alpamayo1_5/models/base_model.py:52 |
| expert 어텐션·마스크 | FA2면 expert만 sdpa 강제; 좌측 패딩 prefix_mask를 expert 4D 마스크에 반영(_build_expert_pos_ids_and_attn_mask) | src/alpamayo1_5/models/alpamayo1_5.py:108 · src/alpamayo1_5/models/alpamayo1_5.py:189 |
| 학습용 잔재 제거 | FlowMatching의 train_timestep_sampler·train_ignore_guidance_rate 삭제, 초기 노이즈 temperature 추가; common/logging.py·geometry/coordinates.py 삭제 | alpamayo:src/alpamayo_r1/diffusion/flow_matching.py:35 · src/alpamayo1_5/diffusion/flow_matching.py:64 |
| 버퍼·dtype | action space·Fourier 버퍼 persistent=False; PerWaypointActionInProjV2의 x.float() 캐스트 제거 | src/alpamayo1_5/action_space/unicycle_accel_curvature.py:83-86 · alpamayo:src/alpamayo_r1/models/action_in_proj.py:162 |
| 시각화·문서 | viz_utils.py 신규; README에 VRAM 표(24/40/60GB), B200 테스트 추가; test_inference는 main() 래핑+minADE 경고 | src/alpamayo1_5/viz_utils.py:97 · README.md:35-41 · src/alpamayo1_5/test_inference.py:76 |
| 변경 없음 | diffusion_expert_cuda_graph.py·tests·delta_tokenizer·action_space/utils 로직 동일(라이선스 연도·로거만 차이), 백본 Qwen3VL 동일 | diff alpamayo_r1 vs alpamayo1_5 (이름 치환 후) · alpamayo:src/alpamayo_r1/models/base_model.py:381 |

### 각주

- 정의 위치 경로는 src/<패키지>/ 기준이다. pyproject.toml·README.md·notebooks/·examples/는 저장소 루트 기준이다.
- from_pretrained는 transformers PreTrainedModel에서 상속한 메서드라 저장소에 정의가 없어, 호출 위치를 적었다.
- L3 부품(diffusion·action_space·action_in/out_proj·궤적 토크나이저)은 체크포인트 config.json의 hydra _target_으로 주입된다. 저장소에 구현이 하나뿐인 클래스를 적었으며 실제 체크포인트 값은 확인하지 않았다(출처 미확인).
- 코드 읽기 기반이며 실행 검증이 아니다. 근거: reference/code-alpamayo-src-components.md
- HF 모델카드는 자차 이력을 0.4 s로 적지만 로더 기본값은 16스텝(1.6 s)이다(load_physical_aiavdataset.py:32-34).
- compare_nav_conditions는 inference_fn 인자를 받지만 실제로는 sample_trajectories_from_data_with_vlm_rollout으로 덮어쓴다(nav_utils.py:119).

## Alpamayo 2 Super

- 저장소: https://github.com/NVlabs/alpamayo2 @ `6d05b9f2dcaa6ee45ac6e053cf18653eac23c047` (2026-09-09) [K8] · 패키지 경로 `src/alpamayo2_super/`
- 그림: [06-alpamayo2-src-components.svg](../images/06-alpamayo2-src-components.svg)

### L6 Applications · 실행 진입점

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| script | `inference_smoke.py` | CLI: python -m alpamayo2_super.inference_smoke. 궤적·CoC 추론, PNG/JSON 저장 | `inference_smoke.py:92 (run_smoke)` | 1–13 | ✓ |
| script | `examples/two_gpu_nav_cfg_demo.py` | VLM cuda:0 / expert cuda:1 분할 + 내비 CFG 데모 | `examples/two_gpu_nav_cfg_demo.py` |  | ✓ |
| notebook | `notebooks/ inference · meta_actions · autolabeling · vqa .ipynb` | 궤적, meta-action, auto-label, VQA 데모 | `notebooks/` |  | ✓ |
| 코드에 없음 | `학습 스크립트 · TensorRT/ONNX/양자화 · Dockerfile` | forward()의 손실 계산만 있고 학습 루프·배포 변환 없음 | `find 'train*.py' · grep 'tensorrt\|onnx\|quantiz' → 0건` |  |  |

### L5 Inference API

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| function | `input_profiles.select_task_input` | 과제별 입력 선택: 궤적은 카메라 (0,1,2,3,5,6) × 4프레임 | `input_profiles.py:198` | 2 | ✓ |
| method | `Alpamayo2Super.from_pretrained` | HF 체크포인트에서 모델 객체 생성·가중치 적재 (device_map="cuda:0") | `상속(transformers) · 호출 inference_smoke.py:133` | 3 |  |
| function | `helper.prepare_model_inputs` | 메시지 구성 → processor 토큰화 → 모델 입력 dict | `helper.py:68` | 4 | ✓ |
| method | `Alpamayo2Super.sample_trajectories_from_data` | 궤적 추론 메인 API: CoC 생성 → 궤적 샘플링 | `models/alpamayo2_super.py:274` | 5–12 | ✓ |
| function | `text_tasks.generate_text` | 텍스트 과제(meta-action·auto-label·VQA·grounding). model을 인자로 받음 | `text_tasks.py:353` |  | ✓ |
| method | `Alpamayo2Super.enable_diffusion_expert_cuda_graph` | 선택: expert 반복 계산을 CUDA graph로 가속 | `models/alpamayo2_super.py:147` |  |  |

### L4 Model

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `Alpamayo2Super` | 최상위 모델. vlm·tokenizer·궤적 토크나이저·expert를 직접 조립 (ReasoningVLA 없음) | `models/alpamayo2_super.py:106` | 3–12 | ✓ |
| attribute | `Alpamayo2Super.vlm` | VLM 객체. 클래스는 config.vlm_class 문자열로 transformers에서 찾음 | `models/alpamayo2_super.py:124` | 7 | ✓ |
| method | `Alpamayo2Super._generate_with_shared_prefill` | prefill 1회 후 샘플 수만큼 KV 캐시 복제해 CoC 디코드 | `models/alpamayo2_super.py:182` | 7 | ✓ |
| class | `ExpertModel` | Alpamayo2Super.expert 로 생성. action 디코더 묶음(expert·proj·diffusion·action_space) | `models/expert.py:66 · 생성 alpamayo2_super.py:143` | 9–11 | ✓ |
| attribute | `ExpertModel.expert` | action expert 트랜스포머 (AutoModel.from_config) | `models/expert.py:76` | 10 |  |
| attribute | `ExpertModel.action_in_proj / action_out_proj` | action ↔ expert 임베딩 변환 | `models/expert.py:87,92` | 10 |  |

### L3 Model Building Blocks

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| class | `Alpamayo2SuperConfig` | 모델 설정: vlm_class, 궤적 vocab 1000+3000, 토큰 48/128 | `config.py:52` |  | ✓ |
| class | `ExpertModelConfig` | expert·부품 hydra cfg 보관 | `models/expert.py:31` |  | ✓ |
| class | `DeltaTrajectoryTokenizer` | history_traj_tokenizer 구현: 과거 궤적 → 이산 토큰 48개 | `models/delta_tokenizer.py:21` | 6 |  |
| class | `MaskDiscreteTrajectoryLogitsProcessor` | CoC 생성 중 궤적 토큰 logit 마스킹 | `models/alpamayo2_super.py:61` | 7 | ✓ |
| class | `FlowMatching` | ExpertModel.diffusion. 노이즈에서 Euler 10스텝 action 샘플링 | `diffusion/flow_matching.py:25` | 9 |  |
| class | `PerWaypointActionInProjV2` | action_in_proj 구현: waypoint별 Fourier 인코딩 + MLP | `models/action_in_proj.py:94` | 10 |  |
| class | `UnicycleAccelCurvatureActionSpace` | ExpertModel.action_space. (가속도, 곡률) → xyz·회전 적분 | `action_space/unicycle_accel_curvature.py:38` | 11 |  |
| class | `DiffusionExpertCudaGraph` | expert forward CUDA graph 캡처·재생 | `models/diffusion_expert_cuda_graph.py:104` |  |  |

### L2 Data · Pre/Post-processing

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| function | `load_physical_aiavdataset` | 클립 → 7캠×4프레임 영상, 자차 과거 16·미래 64점 | `load_physical_aiavdataset.py:32` | 1 | ✓ |
| class | `input_profiles.InputProfile` | 과제별 카메라·프레임 조합 정의 (DRIVING_SIX_CAMERA_FOUR_FRAME 등) | `input_profiles.py:24` | 2 | ✓ |
| function | `chat_template.conversation.build_conversation` | 시스템 프롬프트·이미지·궤적 자리표시로 대화 구성 | `chat_template/conversation.py:332` | 4 | ✓ |
| function | `models.utils.fuse_traj_tokens` | 궤적 자리표시를 과거 궤적 토큰으로 치환 (1.5의 메서드 → 모듈 함수) | `models/utils.py:154` | 6 |  |
| function | `expert_utils.build_expert_pos_ids_and_attn_mask` | expert 위치 id·attention 마스크 구성 | `models/expert_utils.py:92` | 8 | ✓ |
| function | `extract_text_tokens` | 생성 토큰에서 cot·meta_action 등 텍스트 추출 | `models/token_utils.py:134` | 12 |  |
| function | `viz_utils.plot_inference_result` | 카메라·궤적·CoC 그림 PNG + JSON | `viz_utils.py:1329` | 13 | ✓ |

### L1 Libraries · Runtime

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| pip package | `torch 2.8.0` |  | `pyproject.toml:18` |  |  |
| pip package | `transformers 4.57.1` | VLM 클래스·generate·AutoModel | `pyproject.toml:20` |  |  |
| pip package | `flash-attn 2.8.3` | attention 커널 | `pyproject.toml:21 (>=) · uv.lock` |  |  |
| pip package | `hydra-core 1.3.2` | config의 _target_으로 부품 객체 생성 | `pyproject.toml:10 (>=) · uv.lock` |  |  |
| pip package | `einops 0.8.2` |  | `pyproject.toml:8 (>=) · uv.lock` |  |  |
| pip package | `physical-ai-av 0.2.2` | PhysicalAI AV 데이터셋 인터페이스 | `pyproject.toml:15 (>=) · uv.lock` |  |  |
| pip package | `scipy 1.17.1` |  | `pyproject.toml:17 (>=) · uv.lock` |  |  |
| 코드에 없음 | `TensorRT · ONNX · 양자화` | 배포용 변환·양자화 경로 없음 | `grep -rniE 'tensorrt\|onnx\|quantiz\|fp8\|nvfp4' → 0건` |  |  |

### L0 Platform

| 종류 | 이름 (코드 식별자) | 설명 | 정의 위치 | 단계 | 신규 |
|---|---|---|---|---|---|
| 환경 | `Python 3.12` |  | `pyproject.toml:4` |  |  |
| 환경 | `NVIDIA CUDA GPU` | CUDA 필수. CUDA 12.8 wheel. 2-GPU 예제는 H100 80 GB × 2 | `inference_smoke.py:119-123` |  |  |
| 환경 | `torch.bfloat16 · device_map="cuda:0"` | 단일 GPU 기본 적재 | `inference_smoke.py:133` |  | ✓ |
| HF Hub | `nvidia/Alpamayo2-Super` | 가중치 (gated). 모델카드 기재 34B | `common/constants.py:18` |  | ✓ |
| HF Hub | `nvidia/PhysicalAI-Autonomous-Vehicles` | 입력 클립 데이터셋 (gated) | `README.md:43-45` |  |  |

### 궤적 추론 호출 순서 (inference_smoke.run_smoke() 기준)

| 단계 | 위치 | 내용 |
|---|---|---|
| 1 | `inference_smoke.py:126` | load_physical_aiavdataset → 7캠 영상·자차 궤적 로드 |
| 2 | `inference_smoke.py:130` | select_task_input(data, "trajectory") → 6캠 × 4프레임 선택 |
| 3 | `inference_smoke.py:133` | Alpamayo2Super.from_pretrained(bf16, device_map="cuda:0") → __init__에서 vlm·tokenizer·ExpertModel 생성 |
| 4 | `inference_smoke.py:134` | helper.prepare_model_inputs → create_messages → build_conversation → apply_chat_template |
| 5 | `inference_smoke.py:139` | Alpamayo2Super.sample_trajectories_from_data 호출 |
| 6 | `models/alpamayo2_super.py:300` | fuse_traj_tokens: 과거 궤적 → 토큰 48개 삽입 |
| 7 | `models/alpamayo2_super.py:324-340` | MaskDiscreteTrajectoryLogitsProcessor + self._generate_with_shared_prefill → vlm.generate: CoC + KV 캐시 |
| 8 | `models/alpamayo2_super.py:367` | build_expert_pos_ids_and_attn_mask → expert 위치·마스크 |
| 9 | `models/alpamayo2_super.py:406` | self.expert.diffusion.sample (FlowMatching) → Euler 10스텝 시작 |
| 10 | `models/alpamayo2_super.py:383-396` | 매 스텝: expert.action_in_proj → expert.expert(KV 캐시 조건) → expert.action_out_proj |
| 11 | `models/alpamayo2_super.py:424` | self.expert.action_space.action_to_traj → pred_xyz, pred_rot |
| 12 | `models/alpamayo2_super.py:447` | extract_text_tokens → extra["cot"] |
| 13 | `inference_smoke.py:149-158` | CoC·minADE 출력, plot_inference_result로 PNG/JSON 저장 |

### 핵심 수치

| 항목 | 값 | 근거 | 공식 자료 |
|---|---|---|---|
|  |  | src/alpamayo2_super/common/constants.py:20-37 · src/alpamayo2_super/load_physical_aiavdataset.py:85-92 |  |
|  |  | src/alpamayo2_super/input_profiles.py:36-51 |  |
|  |  | src/alpamayo2_super/load_physical_aiavdataset.py:176-180 |  |
|  |  | src/alpamayo2_super/config.py:67-68 · src/alpamayo2_super/helper.py:57-60 · src/alpamayo2_super/helper.py:84-95 |  |
|  |  | src/alpamayo2_super/load_physical_aiavdataset.py:37 · src/alpamayo2_super/config.py:72 · src/alpamayo2_super/config.py:113-130 · src/alpamayo2_super/models/delta_tokenizer.py:24-32 |  |
|  |  | src/alpamayo2_super/action_space/unicycle_accel_curvature.py:49-50 · src/alpamayo2_super/models/alpamayo2_super.py:424-445 · src/alpamayo2_super/load_physical_aiavdataset.py:38 |  |
|  |  | src/alpamayo2_super/diffusion/flow_matching.py:32 · src/alpamayo2_super/diffusion/flow_matching.py:123-124 · src/alpamayo2_super/inference_smoke.py:222-227 |  |
|  |  | src/alpamayo2_super/models/alpamayo2_super.py:277-279 · src/alpamayo2_super/models/alpamayo2_super.py:310-320 · src/alpamayo2_super/config.py:73 |  |
|  |  | src/alpamayo2_super/text_tasks.py:388-389 |  |
|  |  | src/alpamayo2_super/config.py:31-41 · src/alpamayo2_super/config.py:63-64 · src/alpamayo2_super/models/utils.py:26-57 · src/alpamayo2_super/config.py:146 |  |
|  |  | README.md:196-198 · README.md:220-224 |  |
|  |  | https://huggingface.co/nvidia/Alpamayo2-Super |  |
|  |  | README.md:12-13 · src/alpamayo2_super/models/alpamayo2_super.py:123-124 · src/alpamayo2_super/models/expert.py:75 |  |

### 공식 자료 용어 ↔ 코드 이름

| 공식 자료 용어 | 코드 이름 | 판정 | 근거 |
|---|---|---|---|
| Cosmos 3 Super Reasoner (32B) | Alpamayo2Super.vlm = getattr(transformers, config.vlm_class) | partial | src/alpamayo2_super/models/alpamayo2_super.py:123-124 · src/alpamayo2_super/config.py:147 |
| 2B diffusion-based Action Expert (모델 카드 2.3B) | ExpertModel (expert=AutoModel.from_config) | yes | src/alpamayo2_super/models/expert.py:66-96 · README.md:13 |
| diffusion-based action decoder | FlowMatching (BaseDiffusion, Euler) | yes | src/alpamayo2_super/diffusion/flow_matching.py:25 |
| Chain-of-Causation reasoning traces | extra["cot"], <\|cot_start\|>, construct_cot | yes | src/alpamayo2_super/models/token_utils.py:134-179 · src/alpamayo2_super/chat_template/conversation.py:183 · src/alpamayo2_super/inference_smoke.py:147 |
| Meta-actions (yield, lane change, stop) | split_cot_and_meta_action, task meta_action | yes | src/alpamayo2_super/models/token_utils.py:124-131 · src/alpamayo2_super/text_tasks.py:54-58 |
| Structured reasoning auto-labels | parse_auto_labeling_json, COT_AUTO_LABELING_KEYS | yes | src/alpamayo2_super/text_tasks.py:41-46 · src/alpamayo2_super/text_tasks.py:338-351 |
| VQA with 2D grounding | prepare_vqa_inputs, TASK_INPUT_PROFILES["grounding"], plot_grounding_result | yes | src/alpamayo2_super/text_tasks.py:308 · src/alpamayo2_super/input_profiles.py:50 · src/alpamayo2_super/viz_utils.py:1546 |
| up to seven cameras, 4 temporal frames per camera | load_physical_aiavdataset(7캠) → select_task_input(6캠) | partial | src/alpamayo2_super/load_physical_aiavdataset.py:85-92 · src/alpamayo2_super/input_profiles.py:36-51 |
| 64 waypoints, 0.1–6.4 s | UnicycleAccelCurvatureActionSpace(n_waypoints=64, dt=0.1) | yes | src/alpamayo2_super/action_space/unicycle_accel_curvature.py:49-50 |
| RL post-trained | (없음) | absent | grep -rniE 'reinforce\|grpo\|ppo\|reward' (*.py/*.md/*.ipynb) → 0건; find train*.py → 0건 |
| DeepSpeed ≥0.17.4 (모델 카드 런타임) | (없음) | no | pyproject.toml:5-22 · grep -ci deepspeed uv.lock → 0 |
| minADE_6 0.911 m | inference_smoke minADE (num_traj_samples=1) | partial | src/alpamayo2_super/inference_smoke.py:149-152 |

### Alpamayo 1.5 대비 차이

| 항목 | 내용 | 근거 |
|---|---|---|
| VLM 백본 결합 | 1.5: Qwen3VLForConditionalGeneration 하드코딩(기본 Qwen/Qwen3-VL-8B-Instruct) → 2: getattr(transformers, vlm_class) 동적 | a15 models/base_model.py:211 · a15 models/base_model.py:390 · src/alpamayo2_super/models/alpamayo2_super.py:123-124 |
| 클래스 구조 | 1.5: Alpamayo1_5(ReasoningVLA+TrajectoryFusionMixin), expert를 __init__ 안에서 구성 → 2: Alpamayo2Super(PreTrainedModel) + 독립 ExpertModel/ExpertModelConfig | a15 models/alpamayo1_5.py:87-140 · a15 models/base_model.py:292 · src/alpamayo2_super/models/expert.py:31-96 |
| 궤적 API 이름·기본값 | sample_trajectories_from_data_with_vlm_rollout(num_traj_samples=6) → sample_trajectories_from_data(num_traj_samples=1) + 공유 prefill | a15 models/alpamayo1_5.py:244-251 · src/alpamayo2_super/models/alpamayo2_super.py:273-281 · src/alpamayo2_super/models/alpamayo2_super.py:182 |
| 내비 CFG | 1.5: 모델 메서드 ..._cfg_nav + nav_utils.py → 2: 공개 API에서 제거(CFG 설정 시 ValueError), examples 2-GPU 데모로만 | a15 models/alpamayo1_5.py:440 · a15 nav_utils.py · src/alpamayo2_super/models/expert.py:84-85 · examples/two_gpu_nav_cfg_demo.py:257 |
| 카메라 입력 | 1.5 로더 기본 4캠(전방·크로스) → 2: 7캠 링 로드 + input_profiles 태스크별 6캠×4프레임 | a15 load_physical_aiavdataset.py:74-79 · src/alpamayo2_super/load_physical_aiavdataset.py:85-92 · src/alpamayo2_super/input_profiles.py:36-51 |
| 궤적 토큰 | 1.5: traj_vocab_size 768, history 16/future 64 토큰 → 2: vocab 1000+3000, history 48/future 128 토큰 | a15 models/base_model.py:213-215 · src/alpamayo2_super/config.py:63-64 · src/alpamayo2_super/config.py:72-73 |
| 텍스트 태스크 | 1.5: ReasoningVLA.generate_text(VQA) → 2: text_tasks 모듈(meta_action/auto_labeling/vqa+grounding, JSON 파싱) | a15 models/base_model.py:456 · src/alpamayo2_super/text_tasks.py:39-58 · src/alpamayo2_super/text_tasks.py:353 |
| 프롬프트 구성 | 1.5 helper.create_message/create_vqa_message → 2 chat_template/conversation.py; include_camera_ids 기본 False→True | a15 helper.py:77 · a15 config.py:37 · src/alpamayo2_super/chat_template/conversation.py:332 · src/alpamayo2_super/config.py:69 |
| attention 구현 | 1.5: 기본 flash_attention_2 강제, expert는 sdpa 강제 → 2: 강제 없음(HF 기본 선택) | a15 models/base_model.py:225-226 · a15 models/alpamayo1_5.py:107-109 · src/alpamayo2_super/models/alpamayo2_super.py:111-112 |
| 로딩·엔트리 | 1.5 test_inference: from_pretrained(...).to("cuda") → 2: device_map="cuda:0", inference_smoke CLI + visualization 공개 API 신규 | a15 test_inference.py:39 · src/alpamayo2_super/inference_smoke.py:133 · src/alpamayo2_super/visualization.py:17 |
| 체크포인트 | nvidia/Alpamayo-1.5-10B → nvidia/Alpamayo2-Super (34B) | a15 test_inference.py:39 · src/alpamayo2_super/common/constants.py:18 · README.md:12 |
| 노트북 | inference/inference_nav/inference_cam_num/inference_vqa → inference/meta_actions/autolabeling/vqa | a15 README.md:138-141 · README.md:226-294 |
| 유지된 블록 | UnicycleAccelCurvatureActionSpace(import만 변경), DiffusionExpertCudaGraph(382행 동일 크기), PerWaypointActionInProjV2, FlowMatching steps 10, top_p 0.98/T 0.6, torch 2.8.0/transformers 4.57.1/flash-attn 2.8.3 | diff a15/a2 action_space/unicycle_accel_curvature.py · a15 diffusion/flow_matching.py:35 · src/alpamayo2_super/diffusion/flow_matching.py:32 · a15 pyproject.toml:13-16 |
| 의존성 | physical-ai-av ==0.2.0 → >=0.2.0(lock 0.2.2); numpy·scipy·mediapy 추가, seaborn 제거 | a15 pyproject.toml:12 · pyproject.toml:11-17 · uv.lock:1407 |

### 각주

- 정의 위치 경로는 src/<패키지>/ 기준이다. pyproject.toml·README.md·notebooks/·examples/는 저장소 루트 기준이다.
- from_pretrained는 transformers PreTrainedModel에서 상속한 메서드라 저장소에 정의가 없어, 호출 위치를 적었다.
- L3 부품(diffusion·action_space·action_in/out_proj·궤적 토크나이저)은 체크포인트 config.json의 hydra _target_으로 주입된다. 저장소에 구현이 하나뿐인 클래스를 적었으며 실제 체크포인트 값은 확인하지 않았다(출처 미확인).
- 코드 읽기 기반이며 실행 검증이 아니다. 근거: reference/code-alpamayo-src-components.md
- VLM 클래스·층·hidden·head 수는 코드에 없고 체크포인트 config.json에서 읽는다(models/alpamayo2_super.py:123-124).
- 파라미터 규모: 저장소 README는 32B VLM + 2B diffusion expert(README.md:13), 모델카드는 expert 2.3B로 적는다(WebFetch 요약 경유).
