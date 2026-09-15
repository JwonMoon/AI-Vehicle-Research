# Alpamayo 1 · 1.5 · 2 Super 소스 코드 기반 컴포넌트 근거

작성일: 2026-09-16 · 대상: 고정 커밋 클론(depth 1)의 코드 읽기. 실행 검증 아님. ROS 2·Autoware 통합(alpamayo-autoware)은 제외.

그림 4~6의 박스별 파일·줄 근거, 추론 호출 순서, 공식 자료 대조, 이전 버전 대비 차이를 기록한다. 공식 자료(HF 모델카드·NVIDIA 블로그·arXiv 2511.00088) 대조는 WebFetch로 열람했으며 요약 경유 항목은 원문 재확인이 필요하다.

표기: kind=`absent`는 grep·find로 저장소에 없음을 확인한 항목. order는 궤적 추론 호출 순서 번호. 경로는 각 저장소 루트 기준.

## Alpamayo 1

- 저장소: https://github.com/NVlabs/alpamayo @ `11a0e01c13a5622377c45ee37d653351453ec43b` (2026-09-09) [K6]
- 그림: [04-alpamayo1-src-components.svg](../images/04-alpamayo1-src-components.svg)

### L6 Applications · 실행 진입점

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `test_inference.py` | script | `src/alpamayo_r1/test_inference.py` | 예제 clip 1개 추론 후 minADE 출력 |  |  | src/alpamayo_r1/test_inference.py:16-18 · src/alpamayo_r1/test_inference.py:56-72 · README.md:98-100 | GitHub README: Running Inference |
| `inference.ipynb` | notebook | `notebooks/inference.ipynb` | 추론 + 카메라/궤적 시각화 |  |  | notebooks/inference.ipynb:52 · notebooks/inference.ipynb:113 · notebooks/inference.ipynb:151 | GitHub README: Interactive notebook |
| `SFT/RL 학습 스크립트` | absent | `(alpamayo-recipes로 이전)` | 학습 코드 없음, 추론 전용 저장소 |  |  | grep -rniE 'optimizer\|deepspeed\|lora\|backward\(' → 0건 · ls docs finetune → 없음 · README.md:27 · flow_matching.py:140-173 (construct_training_data 등 손실 함수만 잔존) | GitHub README: Updates (May 2026) |

### L5 Inference API

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `AlpamayoR1.from_pretrained` | function | `src/alpamayo_r1/models/alpamayo_r1.py` | HF PreTrainedModel 상속 로더(bf16) | 3 |  | src/alpamayo_r1/test_inference.py:35 · src/alpamayo_r1/models/alpamayo_r1.py:365-366 · src/alpamayo_r1/models/base_model.py:285 | HF model card |
| `sample_trajectories_from_data_with_vlm_rollout` | function | `src/alpamayo_r1/models/alpamayo_r1.py` | CoC 생성 → flow matching 궤적 샘플링 | 5 |  | src/alpamayo_r1/models/alpamayo_r1.py:150-362 | arXiv 2511.00088 §3.2.2 · arXiv 2511.00088 §5.1 |
| `fuse_traj_tokens` | function | `src/alpamayo_r1/models/base_model.py` | 과거 궤적 토큰을 placeholder에 삽입 | 6 |  | src/alpamayo_r1/models/base_model.py:168-197 · src/alpamayo_r1/models/alpamayo_r1.py:190 |  |
| `enable_diffusion_expert_cuda_graph` | function | `src/alpamayo_r1/models/alpamayo_r1.py` | 선택: expert forward CUDA graph 재생 |  |  | src/alpamayo_r1/models/alpamayo_r1.py:130-148 · src/alpamayo_r1/models/diffusion_expert_cuda_graph.py:358-382 · README.md:109-126 | GitHub README: Optional CUDA graph acceleration |

### L4 Model

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `AlpamayoR1` | class | `src/alpamayo_r1/models/alpamayo_r1.py` | VLM + expert + 액션 헤드 최상위 모델 |  |  | src/alpamayo_r1/models/alpamayo_r1.py:80-128 | HF model card: Model Architecture · arXiv 2511.00088 §3 |
| `ReasoningVLA` | class | `src/alpamayo_r1/models/base_model.py` | 기반 클래스: VLM·tokenizer 초기화 |  |  | src/alpamayo_r1/models/base_model.py:285-401 |  |
| `vlm` | module | `src/alpamayo_r1/models/base_model.py` | Qwen3VLForConditionalGeneration | 7 |  | src/alpamayo_r1/models/base_model.py:367-381 · src/alpamayo_r1/models/alpamayo_r1.py:220-226 | arXiv 2511.00088 §3.1 (Cosmos-Reason) · HF model card: 8.2B backbone |
| `expert` | module | `src/alpamayo_r1/models/alpamayo_r1.py` | text_config 복제 action expert | 10 |  | src/alpamayo_r1/models/alpamayo_r1.py:95-101 · src/alpamayo_r1/models/alpamayo_r1.py:297-304 | HF model card: 2.3B action expert · arXiv 2511.00088 §5.1 |
| `action_in_proj` | module | `src/alpamayo_r1/models/alpamayo_r1.py` | noisy action+t → expert 임베딩 | 10 |  | src/alpamayo_r1/models/alpamayo_r1.py:109-113 · src/alpamayo_r1/models/alpamayo_r1.py:292 |  |
| `action_out_proj` | module | `src/alpamayo_r1/models/alpamayo_r1.py` | expert hidden → 속도장 (64×2) | 10 |  | src/alpamayo_r1/models/alpamayo_r1.py:114-118 · src/alpamayo_r1/models/alpamayo_r1.py:309-311 |  |

### L3 Model Building Blocks

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `AlpamayoR1Config` | config | `src/alpamayo_r1/config.py` | 하위 모듈 hydra cfg 보관 |  |  | src/alpamayo_r1/config.py:23-50 · src/alpamayo_r1/models/base_model.py:200-239 |  |
| `FlowMatching` | class | `src/alpamayo_r1/diffusion/flow_matching.py` | Euler 적분 샘플러 (BaseDiffusion) | 9 |  | src/alpamayo_r1/diffusion/flow_matching.py:22-138 · src/alpamayo_r1/diffusion/base.py:45 | arXiv 2511.00088 §5.1 |
| `UnicycleAccelCurvatureActionSpace` | class | `src/alpamayo_r1/action_space/unicycle_accel_curvature.py` | 가속도·곡률 → 궤적 적분 | 11 |  | src/alpamayo_r1/action_space/unicycle_accel_curvature.py:38-102 · src/alpamayo_r1/action_space/unicycle_accel_curvature.py:307-389 | arXiv 2511.00088 §3.2.2 |
| `PerWaypointActionInProjV2` | class | `src/alpamayo_r1/models/action_in_proj.py` | Fourier 인코딩+MLP 입력 projection |  |  | src/alpamayo_r1/models/action_in_proj.py:104-169 |  |
| `DeltaTrajectoryTokenizer` | class | `src/alpamayo_r1/models/delta_tokenizer.py` | 과거 궤적 → 이산 delta 토큰(추정) |  |  | src/alpamayo_r1/models/delta_tokenizer.py:21-98 · src/alpamayo_r1/models/base_model.py:396-401 |  |
| `ExpertLogitsProcessor` | class | `src/alpamayo_r1/models/alpamayo_r1.py` | 생성 중 궤적 토큰 logit을 -inf 마스킹 | 7 |  | src/alpamayo_r1/models/alpamayo_r1.py:46-77 · src/alpamayo_r1/models/alpamayo_r1.py:212-219 |  |

### L2 Data · Pre/Post-processing

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `load_physical_aiavdataset` | function | `src/alpamayo_r1/load_physical_aiavdataset.py` | 4카메라×4프레임, ego 좌표계 변환(scipy) | 1 |  | src/alpamayo_r1/load_physical_aiavdataset.py:27-222 | HF model card: Input |
| `create_message` | function | `src/alpamayo_r1/helper.py` | system/user/assistant 채팅 메시지 구성 | 2 |  | src/alpamayo_r1/helper.py:28-68 |  |
| `get_processor` | function | `src/alpamayo_r1/helper.py` | Qwen3-VL-2B processor 구성 | 4 |  | src/alpamayo_r1/helper.py:23-25 · src/alpamayo_r1/helper.py:71-80 · src/alpamayo_r1/test_inference.py:36-45 |  |
| `token_utils` | module | `src/alpamayo_r1/models/token_utils.py` | StopAfterEOS·extract_text_tokens 등 | 12 |  | src/alpamayo_r1/models/token_utils.py:151-169 · src/alpamayo_r1/models/token_utils.py:172-209 · src/alpamayo_r1/models/token_utils.py:212-253 |  |
| `geometry/rotation.py` | module | `src/alpamayo_r1/geometry/rotation.py` | 2D/3D 회전행렬·yaw 변환 |  |  | src/alpamayo_r1/geometry/rotation.py:109 · src/alpamayo_r1/geometry/rotation.py:197 · src/alpamayo_r1/action_space/unicycle_accel_curvature.py:387 |  |

### L1 Libraries · Runtime

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `torch 2.8.0` | external | `external` |  |  |  | pyproject.toml:11 · uv.lock:1165-1166 | HF model card: Runtime (PyTorch ≥2.8) |
| `transformers 4.57.1` | external | `external` | Qwen3-VL, generate, AutoModel |  |  | pyproject.toml:13 · uv.lock:1254-1255 | HF model card: Runtime (Transformers ≥4.57.1) |
| `flash-attn 2.8.3` | external | `external` | 기본 attn_implementation |  |  | pyproject.toml:14 · uv.lock:265-266 · src/alpamayo_r1/models/base_model.py:215 | GitHub README: Troubleshooting |
| `hydra-core 1.3.2` | external | `external` | cfg dict로 하위 모듈 instantiate |  |  | pyproject.toml:8 · uv.lock:336-337 · src/alpamayo_r1/models/alpamayo_r1.py:103-118 |  |
| `einops 0.8.2` | external | `external` |  |  |  | pyproject.toml:7 · uv.lock:238-239 |  |
| `physical-ai-av 0.2.0` | external | `external` | PhysicalAI AV 데이터셋 인터페이스 |  |  | pyproject.toml:9 · uv.lock:828-829 · src/alpamayo_r1/load_physical_aiavdataset.py:21 |  |
| `scipy 1.17.1` | external | `external` | Rotation(쿼터니언→회전행렬) |  |  | pyproject.toml:15 · uv.lock:1074-1075 · src/alpamayo_r1/load_physical_aiavdataset.py:22 |  |
| `TensorRT / ONNX / 양자화` | absent | `(없음)` | 배포용 export·양자화 코드 없음 |  |  | grep -rniE 'tensorrt\|onnx\|quantiz\|int8\|fp8\|vllm' (*.py,*.toml,*.ipynb) → delta_tokenizer.py:91 주석(이산화)만 매칭 |  |

### L0 Platform

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Python 3.12.*` | config | `pyproject.toml` |  |  |  | pyproject.toml:4 · uv.lock:3 | GitHub README: Requirements |
| `NVIDIA CUDA GPU ≥24GB · bfloat16` | config | `src/alpamayo_r1/test_inference.py` | Linux 테스트, autocast bf16 |  |  | src/alpamayo_r1/test_inference.py:35 · src/alpamayo_r1/test_inference.py:55 · src/alpamayo_r1/models/base_model.py:214 · README.md:47-51 | HF model card: Precision BF16, ≥24GB VRAM |
| `nvidia/Alpamayo-R1-10B` | config | `src/alpamayo_r1/test_inference.py` | HF 체크포인트 약 22GB (gated) |  |  | src/alpamayo_r1/test_inference.py:35 · README.md:94 · README.md:77 | HF model card: 10B params |
| `nvidia/PhysicalAI-Autonomous-Vehicles` | config | `src/alpamayo_r1/load_physical_aiavdataset.py` | HF 데이터셋 스트리밍 (gated) |  |  | README.md:76 · src/alpamayo_r1/load_physical_aiavdataset.py:31 · src/alpamayo_r1/load_physical_aiavdataset.py:71 | GitHub README: Authenticate with HuggingFace |

### 궤적 추론 호출 순서

1. test_inference.py → load_physical_aiavdataset(clip_id)
2. create_message: 이미지 16장+traj_history×48+cot_start
3. AlpamayoR1.from_pretrained(bfloat16).to("cuda")
4. get_processor → apply_chat_template → helper.to_device
5. sample_trajectories_from_data_with_vlm_rollout 호출
6. fuse_traj_tokens: hist_traj_tokenizer로 placeholder 치환
7. vlm.generate: ExpertLogitsProcessor·StopAfterEOS로 CoC
8. traj_future_start 기준 KV cache·position_ids·mask 구성
9. FlowMatching.sample: 노이즈 x에서 Euler 적분(기본 10 step)
10. step_fn: action_in_proj → expert(KV cache) → action_out_proj
11. UnicycleAccelCurvatureActionSpace.action_to_traj → xyz/rot
12. token_utils.extract_text_tokens → extra["cot"]
13. test_inference.py: ego_future_xyz와 비교해 minADE 출력

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

- diffusion_cfg·action_space_cfg·action_in_proj_cfg·action_out_proj_cfg·traj/hist_traj_tokenizer_cfg의 실제 값은 HF 체크포인트 config.json에 있으며 저장소에 없음. L3의 클래스-속성 대응(action_in_proj=PerWaypointActionInProjV2, hist_traj_tokenizer=DeltaTrajectoryTokenizer 등)은 코드 내 유일 구현체 기준 추정 (출처 미확인).
- action_out_proj의 구체 클래스는 저장소에 정의가 없음 (in_features/out_features 인자로 보아 nn.Linear 계열 추정, 출처 미확인).
- 헬퍼 to_device(helper.py:83-100), 로깅(common/logging.py), geometry/coordinates.py, action_space/utils.py는 사소한 유틸로 박스에서 생략.
- DiffusionExpertCudaGraph 클래스(models/diffusion_expert_cuda_graph.py:104)는 박스 수 제한으로 L5 enable_diffusion_expert_cuda_graph에 병합.
- tests/test_diffusion_expert_cuda_graph.py는 CUDA graph 경로의 GPU 단위 테스트(pytest)로 L6에서 생략.
- dev 그룹: matplotlib 3.10.8, mediapy 1.2.6 (노트북 시각화 전용); 노트북은 pandas 3.0.1(uv.lock:786-787)도 사용하나 pyproject 직접 의존성에는 없음.
- README는 이 저장소를 유지보수 모드로 표기하고 후속 버전(Alpamayo 1.5, alpamayo-recipes)을 안내함 (README.md:1-11, 29).
- 파라미터 수(8.2B+2.3B)는 HF 모델 카드 기준이며 코드로 검증하지 않음.

## Alpamayo 1.5

- 저장소: https://github.com/NVlabs/alpamayo1.5 @ `36aeb4c5938cbc2eb2aed33b22434773da4ab639` (2026-09-09) [K7]
- 그림: [05-alpamayo1_5-src-components.svg](../images/05-alpamayo1_5-src-components.svg)

### L6 Applications · 실행 진입점

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `test_inference.py` | script | `src/alpamayo1_5/test_inference.py` | 예제 클립 추론 후 minADE 출력 |  |  | src/alpamayo1_5/test_inference.py:29 · src/alpamayo1_5/test_inference.py:80 · README.md:88 | README Test script |
| `inference.ipynb` | notebook | `notebooks/inference.ipynb` | 기본 궤적+CoC 추론 데모 |  |  | notebooks/inference.ipynb:cell8 · README.md:138 | README Project Structure |
| `inference_nav.ipynb` | notebook | `notebooks/inference_nav.ipynb` | 내비 지시 조건화·CFG 비교 데모 |  | ✓ | notebooks/inference_nav.ipynb:cell11 · notebooks/inference_nav.ipynb:cell14 · README.md:140 | README FAQ Navigation |
| `inference_cam_num.ipynb` | notebook | `notebooks/inference_cam_num.ipynb` | 카메라 1/2/4대 비교 데모 |  | ✓ | notebooks/inference_cam_num.ipynb:cell6 · README.md:139 | README FAQ cameras |
| `inference_vqa.ipynb` | notebook | `notebooks/inference_vqa.ipynb` | 시각 질의응답(VQA) 데모 |  | ✓ | notebooks/inference_vqa.ipynb:cell12 · README.md:141 | README FAQ VQA |
| `TensorRT/ONNX export · training scripts` | absent | `external` | 저장소에 없음(SFT/RL은 alpamayo-recipes) |  |  | grep -rnEi 'tensorrt\|onnx\|torch\.export\|quantiz\|fp8' src tests notebooks pyproject.toml README.md → 해당 없음(주석 2건만) · grep -rnE 'optimizer\|\.backward\(\|training_step\|compute_loss' src → 0건 · README.md:14 · README.md:128 | README Fine-tuning and Post-training Recipes |

### L5 Inference API

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Alpamayo1_5.from_pretrained` | function | `transformers PreTrainedModel (상속)` | HF 체크포인트 로드 | 2 |  | src/alpamayo1_5/test_inference.py:39 · src/alpamayo1_5/models/alpamayo1_5.py:736 · README.md:178 | HF model card nvidia/Alpamayo-1.5-10B |
| `sample_trajectories_from_data_with_vlm_rollout` | function | `src/alpamayo1_5/models/alpamayo1_5.py` | CoC 생성 후 궤적 샘플링(주 경로) | 6 |  | src/alpamayo1_5/models/alpamayo1_5.py:244 · README.md:102 | README Inference methods |
| `sample_trajectories_from_data_with_vlm_rollout_cfg_nav` | function | `src/alpamayo1_5/models/alpamayo1_5.py` | 내비 CFG: 내비 제거 KV캐시 추가 구축 |  | ✓ | src/alpamayo1_5/models/alpamayo1_5.py:440 · src/alpamayo1_5/models/alpamayo1_5.py:553 · src/alpamayo1_5/models/alpamayo1_5.py:693 | README Hardware requirements (CFG ~60GB) |
| `generate_text` | function | `src/alpamayo1_5/models/base_model.py` | 텍스트 전용 생성(VQA) |  | ✓ | src/alpamayo1_5/models/base_model.py:456 · README.md:104 | README Inference methods |
| `compare_nav_conditions` | function | `src/alpamayo1_5/nav_utils.py` | 내비 유/무/반대방향 3조건 일괄 추론 |  | ✓ | src/alpamayo1_5/nav_utils.py:69 · src/alpamayo1_5/nav_utils.py:179 |  |

### L4 Model

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Alpamayo1_5` | class | `src/alpamayo1_5/models/alpamayo1_5.py` | VLM + expert + 확산 조립 최상위 모델 |  |  | src/alpamayo1_5/models/alpamayo1_5.py:87 · src/alpamayo1_5/models/alpamayo1_5.py:110 · src/alpamayo1_5/models/alpamayo1_5.py:114 | HF model card: 10B |
| `ReasoningVLA` | class | `src/alpamayo1_5/models/base_model.py` | VLM·토크나이저·궤적 토크나이저 기반 클래스 |  |  | src/alpamayo1_5/models/base_model.py:292 · src/alpamayo1_5/models/base_model.py:318 |  |
| `Qwen3VLForConditionalGeneration` | class | `external (transformers) · self.vlm` | VLM 백본(카드상 Cosmos-Reason2) |  |  | src/alpamayo1_5/models/base_model.py:31 · src/alpamayo1_5/models/base_model.py:211 · src/alpamayo1_5/models/base_model.py:390 | HF model card: Backbone 8.2B, Cosmos-Reason2, Qwen3-VL-8B-Instruct 기반 |
| `expert` | module | `src/alpamayo1_5/models/alpamayo1_5.py (AutoModel.from_config)` | VLM text_config 복제 action expert |  |  | src/alpamayo1_5/models/alpamayo1_5.py:102 · src/alpamayo1_5/models/alpamayo1_5.py:110 · src/alpamayo1_5/models/alpamayo1_5.py:112 | HF model card: Action Expert 2.3B |

### L3 Model Building Blocks

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Alpamayo1_5Config` | config | `src/alpamayo1_5/config.py` | ReasoningVLAConfig 상속·hydra cfg |  |  | src/alpamayo1_5/config.py:23 · src/alpamayo1_5/models/base_model.py:204 |  |
| `FlowMatching` | class | `src/alpamayo1_5/diffusion/flow_matching.py` | Euler 적분 샘플러, CFG _guided_v | 10 | ✓ | src/alpamayo1_5/diffusion/flow_matching.py:22 · src/alpamayo1_5/diffusion/flow_matching.py:115 · src/alpamayo1_5/diffusion/flow_matching.py:138 | arXiv 2511.00088 (diffusion-based trajectory decoder) |
| `UnicycleAccelCurvatureActionSpace` | class | `src/alpamayo1_5/action_space/unicycle_accel_curvature.py` | 가속도·곡률 action ↔ xyz/rot 궤적 | 11 |  | src/alpamayo1_5/action_space/unicycle_accel_curvature.py:38 · src/alpamayo1_5/action_space/unicycle_accel_curvature.py:102 · src/alpamayo1_5/action_space/unicycle_accel_curvature.py:307 |  |
| `PerWaypointActionInProjV2` | class | `src/alpamayo1_5/models/action_in_proj.py` | noisy action+t → expert 임베딩 |  |  | src/alpamayo1_5/models/action_in_proj.py:104 · src/alpamayo1_5/models/alpamayo1_5.py:120 |  |

### L2 Data · Pre/Post-processing

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `load_physical_aiavdataset` | function | `src/alpamayo1_5/load_physical_aiavdataset.py` | 클립→영상 프레임·ego 이력/미래 | 1 |  | src/alpamayo1_5/load_physical_aiavdataset.py:27 · src/alpamayo1_5/load_physical_aiavdataset.py:208 | HF dataset nvidia/PhysicalAI-Autonomous-Vehicles |
| `create_message` | function | `src/alpamayo1_5/helper.py` | 채팅 메시지(카메라명·route 구간 포함) | 4 | ✓ | src/alpamayo1_5/helper.py:77 · src/alpamayo1_5/helper.py:113 · src/alpamayo1_5/helper.py:38 |  |
| `create_vqa_message` | function | `src/alpamayo1_5/helper.py` | <\|question_start\|> 질의 메시지 |  | ✓ | src/alpamayo1_5/helper.py:145 · src/alpamayo1_5/helper.py:165 |  |
| `get_processor` | function | `src/alpamayo1_5/helper.py` | Qwen3-VL-2B 프로세서+모델 토크나이저 | 3 |  | src/alpamayo1_5/helper.py:190 · src/alpamayo1_5/helper.py:25 |  |
| `nav_utils` | module | `src/alpamayo1_5/nav_utils.py` | swap_direction·remove_nav_text |  | ✓ | src/alpamayo1_5/nav_utils.py:199 · src/alpamayo1_5/nav_utils.py:225 · src/alpamayo1_5/nav_utils.py:251 |  |
| `extract_text_tokens` | function | `src/alpamayo1_5/models/token_utils.py` | 출력에서 cot/meta_action/answer 추출 | 12 |  | src/alpamayo1_5/models/token_utils.py:151 · src/alpamayo1_5/models/token_utils.py:166 · src/alpamayo1_5/models/alpamayo1_5.py:430 |  |
| `viz_utils` | module | `src/alpamayo1_5/viz_utils.py` | BEV 궤적 비교·카메라 그리드 그림 |  | ✓ | src/alpamayo1_5/viz_utils.py:97 · src/alpamayo1_5/viz_utils.py:190 |  |

### L1 Libraries · Runtime

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `torch==2.8.0` | external | `external` |  |  |  | pyproject.toml:14 · uv.lock (torch 2.8.0) | HF model card: PyTorch min 2.8 |
| `transformers==4.57.1` | external | `external` | Qwen3VL·generate·AutoModel |  |  | pyproject.toml:16 · src/alpamayo1_5/models/base_model.py:26 | HF model card: Transformers min 4.57.1 |
| `flash-attn 2.8.3` | external | `external` | VLM 기본 어텐션(선택, SDPA 대체) |  |  | pyproject.toml:17 · uv.lock (flash-attn 2.8.3) · README.md:165 |  |
| `hydra-core 1.3.2` | external | `external` | hyu.instantiate로 하위모듈 생성 |  |  | pyproject.toml:10 · src/alpamayo1_5/models/alpamayo1_5.py:23 · src/alpamayo1_5/models/alpamayo1_5.py:114 |  |
| `physical-ai-av==0.2.0` | external | `external` | 데이터셋 HF 스트리밍 인터페이스 |  |  | pyproject.toml:12 · src/alpamayo1_5/load_physical_aiavdataset.py:21 | README.md:77 |

### L0 Platform

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Python 3.12` | external | `external` |  |  |  | pyproject.toml:4 · README.md:31 |  |
| `NVIDIA GPU · CUDA 12.x` | external | `external` | 24GB+ VRAM, .to("cuda") 고정 |  |  | README.md:29-41 · README.md:244 · src/alpamayo1_5/nav_utils.py:155 | HF model card: 1 GPU 24GB+, tested H100 |
| `bfloat16 · flash_attention_2/sdpa` | config | `external` | expert는 FA2 대신 sdpa 강제 |  | ✓ | src/alpamayo1_5/models/base_model.py:218 · src/alpamayo1_5/models/base_model.py:226 · src/alpamayo1_5/models/alpamayo1_5.py:108 · src/alpamayo1_5/test_inference.py:59 | HF model card: BF16 |
| `nvidia/Alpamayo-1.5-10B` | external | `external (HF Hub, gated)` | 가중치 약 22GB |  | ✓ | src/alpamayo1_5/test_inference.py:39 · README.md:83 | HF model card (8.2B+2.3B, OpenMDW-1.1, 2026-03-19) |
| `nvidia/PhysicalAI-Autonomous-Vehicles` | external | `external (HF dataset, gated)` |  |  |  | README.md:66 · src/alpamayo1_5/load_physical_aiavdataset.py:71 | HF dataset card |

### 궤적 추론 호출 순서

1. load_physical_aiavdataset: 4카메라×4프레임, ego 이력 16스텝 로드
2. Alpamayo1_5.from_pretrained(dtype=bfloat16).to("cuda")
3. helper.get_processor(model.tokenizer): Qwen3-VL-2B 프로세서
4. helper.create_message: 카메라명·frame 텍스트+이미지+48 history 자리표시
5. apply_chat_template → tokenized_data, to_device(cuda)
6. sample_trajectories_from_data_with_vlm_rollout 호출
7. fuse_traj_tokens: ego 이력을 <|traj_history|> 자리에 토큰 치환
8. vlm.generate(StopAfterEOS 등) → CoC 텍스트 + KV캐시
9. _find_eos_offset·_build_expert_pos_ids_and_attn_mask
10. FlowMatching._euler: action_in_proj→expert→action_out_proj
11. action_space.action_to_traj → pred_xyz, pred_rot
12. extract_text_tokens → extra["cot"] (return_extra=True)

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

- 하위모듈(diffusion, action_space, action_in_proj, action_out_proj, traj_tokenizer, hist_traj_tokenizer)은 HF config.json의 hydra _target_으로 주입됨(alpamayo1_5.py:114-129, base_model.py:392-410). 저장소 코드만으로 실제 클래스를 확정할 수 없음. FlowMatching·UnicycleAccelCurvatureActionSpace·PerWaypointActionInProjV2는 저장소 안에 하나뿐인 구현체라 채택으로 추정함. action_out_proj 클래스, DeltaTrajectoryTokenizer/DiscreteTrajectoryTokenizer 중 무엇이 쓰이는지는 출처 미확인.
- 박스 수 제한 때문에 생략한 식별자: StopAfterEOS(token_utils.py:172, <\|traj_future_start\|> 다음 1토큰에서 생성 중단, call_order 8단계), ExpertLogitsProcessor(궤적 토큰 logits -inf),fuse_traj_tokens/TrajectoryFusionMixin, DiffusionExpertCudaGraph·enable_diffusion_expert_cuda_graph(1과 동일), DeltaTrajectoryTokenizer, geometry/rotation.py, to_device, einops 0.8.1, scipy 1.16.3(uv.lock 전이 의존), matplotlib 3.10.7·seaborn 0.13.2, mediapy(dev).
- alpamayo1_5.py:212, 216의 주석은 'Qwen2.5-VL RoPE'라고 되어 있지만 실제 백본 클래스는 Qwen3VLForConditionalGeneration임(base_model.py:390). 주석이 갱신되지 않은 것으로 보임.
- HF 모델 카드의 ego history '0.4 second'와 로더 기본 num_history_steps=16(1.6s)이 서로 다름. 체크포인트 config의 tokens_per_history_traj 등은 확인 불가.
- compare_nav_conditions는 inference_fn 인자를 받지만 곧바로 model.sample_trajectories_from_data_with_vlm_rollout으로 덮어씀(nav_utils.py:119). no-nav 조건에는 항상 기본 메서드를 씀.
- create_message의 use_nav_prompt 인자는 docstring에만 설명되고 본문에서는 쓰이지 않음. 프롬프트 문자열이 항상 같음(helper.py:115-120).
- 공식 자료: HF 모델 카드 https://huggingface.co/nvidia/Alpamayo-1.5-10B (2026-09-16 조회), arXiv 2511.00088 초록. NVIDIA HF 블로그는 조회하지 않음.

## Alpamayo 2 Super

- 저장소: https://github.com/NVlabs/alpamayo2 @ `6d05b9f2dcaa6ee45ac6e053cf18653eac23c047` (2026-09-09) [K8]
- 그림: [06-alpamayo2-src-components.svg](../images/06-alpamayo2-src-components.svg)

### L6 Applications · 실행 진입점

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `inference_smoke` | script | `python -m alpamayo2_super.inference_smoke · test_inference.py(호환)` | 1클립 궤적 추론 CLI, PNG/JSON 저장 | 1 | ✓ | src/alpamayo2_super/inference_smoke.py:92 · src/alpamayo2_super/inference_smoke.py:184 · src/alpamayo2_super/test_inference.py:17 · README.md:120-144 | README CLI Inference |
| `two_gpu_nav_cfg_demo.py` | script | `examples/ · sample_with_nav_cfg · load_model_on_two_gpus` | VLM cuda:0·expert cuda:1 내비 CFG |  | ✓ | examples/two_gpu_nav_cfg_demo.py:232 · examples/two_gpu_nav_cfg_demo.py:257 · examples/two_gpu_nav_cfg_demo.py:503-510 · examples/two_gpu_nav_cfg_demo.py:641 | README Two-GPU Navigation CFG Demo |
| `notebooks` | notebook | `inference.ipynb · meta_actions.ipynb · autolabeling.ipynb · vqa.ipynb` | 궤적/메타액션/오토라벨/VQA·그라운딩 |  | ✓ | notebooks/inference.ipynb:112 · notebooks/meta_actions.ipynb:110 · notebooks/autolabeling.ipynb:122 · notebooks/vqa.ipynb:122 | README Notebook/Text Task Notebooks |
| `training scripts (없음)` | absent | `forward() 손실 정의만 존재, 학습 루프·DeepSpeed 없음` | 학습/RL 후학습 코드 미공개 |  |  | find alpamayo2 -iname 'train*.py' → 0건 · src/alpamayo2_super/models/alpamayo2_super.py:225-271 · grep -i deepspeed pyproject.toml uv.lock → 0건 | HF blog nvidia-alpamayo-2: RL post-trained |

### L5 Inference API

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `select_task_input` | function | `input_profiles.TASK_INPUT_PROFILES` | 태스크별 6캠×4프레임 선택 | 3 | ✓ | src/alpamayo2_super/input_profiles.py:198-206 · src/alpamayo2_super/input_profiles.py:45-51 | HF model card nvidia/Alpamayo2-Super: six cameras, four frames |
| `prepare_model_inputs` | function | `helper · create_messages · get_processor · to_device` | chat template+processor 토큰화(배치 1) | 4 |  | src/alpamayo2_super/helper.py:68-102 · src/alpamayo2_super/helper.py:28 · src/alpamayo2_super/helper.py:49 · src/alpamayo2_super/helper.py:105 |  |
| `sample_trajectories_from_data` | function | `Alpamayo2Super · top_p=0.98, temperature=0.6` | CoC 생성→expert 디퓨전→궤적 64점 | 5 | ✓ | src/alpamayo2_super/models/alpamayo2_super.py:273-452 | NVIDIA Tech Blog 2026-08-06: trajectories + CoC |
| `generate_text` | function | `text_tasks · prepare_text_generation_inputs · prepare_vqa_inputs` | VLM generate만 쓰는 텍스트 태스크 |  | ✓ | src/alpamayo2_super/text_tasks.py:353-437 · src/alpamayo2_super/text_tasks.py:238 · src/alpamayo2_super/text_tasks.py:308 · src/alpamayo2_super/text_tasks.py:418 | NVIDIA Tech Blog 2026-08-06: meta-actions, VQA, auto-labels |
| `enable_diffusion_expert_cuda_graph` | function | `Alpamayo2Super · max_batch_size, max_graphs=4` | expert forward CUDA graph 선택 가속 |  |  | src/alpamayo2_super/models/alpamayo2_super.py:147-167 · README.md:146-163 |  |

### L4 Model

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Alpamayo2Super` | class | `PreTrainedModel · model_type alpamayo2_super` | vlm+tokenizer+traj 토크나이저+expert |  | ✓ | src/alpamayo2_super/models/alpamayo2_super.py:106-145 · src/alpamayo2_super/models/alpamayo2_super.py:455 · src/alpamayo2_super/config.py:55 | HF model card nvidia/Alpamayo2-Super: 34B VLA |
| `vlm` | module | `getattr(transformers, config.vlm_class)._from_config` | VLM 백본(클래스명은 체크포인트 config) | 6 | ✓ | src/alpamayo2_super/models/alpamayo2_super.py:123-124 · src/alpamayo2_super/config.py:147 · src/alpamayo2_super/config.py:162 | NVIDIA Tech Blog 2026-08-06: 32B Cosmos 3 Super Reasoner |
| `_generate_with_shared_prefill` | function | `vlm.model prefill → batch_repeat_interleave → vlm.generate` | 공유 prefill 후 샘플 수만큼 CoC 디코드 | 6 | ✓ | src/alpamayo2_super/models/alpamayo2_super.py:182-223 |  |
| `ExpertModel` | class | `expert=AutoModel.from_config(llm_config) · action_in_proj · diffusion · action_space · action_out_proj · expert_utils.build_expert_pos_ids_and_attn_mask` | VLM KV캐시 조건 non-causal 액션 디노이저 | 7 | ✓ | src/alpamayo2_super/models/expert.py:66-96 · src/alpamayo2_super/models/expert.py:31-56 · src/alpamayo2_super/models/alpamayo2_super.py:143 · src/alpamayo2_super/models/expert_utils.py:92-123 · src/alpamayo2_super/models/alpamayo2_super.py:359-397 | NVIDIA Tech Blog 2026-08-06: 2B diffusion-based Action Expert · HF model card nvidia/Alpamayo2-Super: 2.3B action expert |

### L3 Model Building Blocks

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Alpamayo2SuperConfig` | config | `ExpertModelConfig · build_alpamayo2_super_tokenizer · SPECIAL_TOKENS` | vocab 1000+3000, 48/128 토큰, bf16 |  | ✓ | src/alpamayo2_super/config.py:52-73 · src/alpamayo2_super/config.py:31-41 · src/alpamayo2_super/models/expert.py:31 · src/alpamayo2_super/models/utils.py:26-57 |  |
| `DeltaTrajectoryTokenizer` | class | `history_traj_tokenizer / future_traj_tokenizer (hydra instantiate)` | ego 16점 delta xyz → 이산 토큰 48개 | 5 |  | src/alpamayo2_super/models/delta_tokenizer.py:21-57 · src/alpamayo2_super/models/alpamayo2_super.py:133-140 · src/alpamayo2_super/config.py:113-130 |  |
| `MaskDiscreteTrajectoryLogitsProcessor` | class | `MaskTokenIdsLogitsProcessor · StopAfterEOS` | CoC 중 궤적토큰 차단·future_start 정지 | 6 | ✓ | src/alpamayo2_super/models/alpamayo2_super.py:61-103 · src/alpamayo2_super/models/alpamayo2_super.py:322-339 · src/alpamayo2_super/models/expert_utils.py:27 |  |
| `PerWaypointActionInProjV2` | class | `FourierEncoderV2 · MLPEncoder · LayerNorm` | 액션·timestep Fourier→MLP→expert 토큰 | 8 |  | src/alpamayo2_super/models/action_in_proj.py:94-143 |  |
| `FlowMatching` | class | `BaseDiffusion · _euler · num_inference_steps=10` | Euler 적분 10스텝 액션 샘플링 | 8 |  | src/alpamayo2_super/diffusion/flow_matching.py:25-60 · src/alpamayo2_super/diffusion/flow_matching.py:106-149 · src/alpamayo2_super/diffusion/base.py:33 | HF model card nvidia/Alpamayo2-Super: diffusion-based action decoder |
| `UnicycleAccelCurvatureActionSpace` | class | `ActionSpace · action_to_traj · dt=0.1, n_waypoints=64` | (accel,curvature) 적분→xyz·회전 | 9 |  | src/alpamayo2_super/action_space/unicycle_accel_curvature.py:38-60 · src/alpamayo2_super/action_space/unicycle_accel_curvature.py:307 | HF model card nvidia/Alpamayo2-Super: 64 waypoints 0.1–6.4 s |
| `DiffusionExpertCudaGraph` | class | `diffusion_expert_cuda_graph · _ReadOnlyPromptCacheLayer` | exact-shape CUDA graph 캡처/리플레이 |  |  | src/alpamayo2_super/models/diffusion_expert_cuda_graph.py:104 · src/alpamayo2_super/models/diffusion_expert_cuda_graph.py:358 |  |

### L2 Data · Pre/Post-processing

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `load_physical_aiavdataset` | function | `physical_ai_av.PhysicalAIAVDatasetInterface` | 7캠×4프레임, ego 과거16/미래64 | 2 |  | src/alpamayo2_super/load_physical_aiavdataset.py:32-43 · src/alpamayo2_super/load_physical_aiavdataset.py:85-92 · src/alpamayo2_super/load_physical_aiavdataset.py:176-180 | NVIDIA Tech Blog 2026-08-06: up to seven cameras |
| `input_profiles` | module | `InputProfile · DRIVING_SIX_CAMERA_FOUR_FRAME · VQA_SIX_CAMERA_FOUR_FRAME · common.constants` | 카메라 ID 링·태스크별 프로필 | 3 | ✓ | src/alpamayo2_super/input_profiles.py:24-51 · src/alpamayo2_super/common/constants.py:20-37 | HF model card nvidia/Alpamayo2-Super: validated camera IDs |
| `build_conversation` | function | `chat_template.conversation · construct_system_prompt · construct_image · construct_traj_history` | system/user 메시지·이미지·traj 패드 구성 | 4 | ✓ | src/alpamayo2_super/chat_template/conversation.py:332 · src/alpamayo2_super/chat_template/conversation.py:51-95 · src/alpamayo2_super/chat_template/conversation.py:98-155 |  |
| `fuse_traj_tokens` | function | `models.utils · tokenize_history_trajectory · replace_pad_token` | traj_history 패드를 <i*> 토큰으로 치환 | 5 |  | src/alpamayo2_super/models/utils.py:154-177 · src/alpamayo2_super/models/utils.py:103 · src/alpamayo2_super/models/alpamayo2_super.py:300-306 |  |
| `extract_text_tokens` | function | `token_utils.split_cot_and_meta_action · text_tasks.parse_auto_labeling_json` | cot/meta_action/answer/box/JSON 파싱 | 10 |  | src/alpamayo2_super/models/token_utils.py:134-179 · src/alpamayo2_super/models/token_utils.py:124 · src/alpamayo2_super/text_tasks.py:338-351 · src/alpamayo2_super/text_tasks.py:41-46 | NVIDIA Tech Blog 2026-08-06: structured auto-labels |
| `viz_utils` | module | `visualization.plot_inference_result · plot_compact_inference_result · plot_*_result · geometry.rotation/coordinates` | PNG+JSON 사이드카, MP4, 좌표 변환 | 11 |  | src/alpamayo2_super/viz_utils.py:1215 · src/alpamayo2_super/viz_utils.py:1329 · src/alpamayo2_super/visualization.py:17-26 · src/alpamayo2_super/geometry/rotation.py · src/alpamayo2_super/geometry/coordinates.py | README Visualization API |

### L1 Libraries · Runtime

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `torch 2.8.0` | external | `torchvision 0.23.0 · triton 3.4.0 (lock)` | autocast bf16·CUDA graph |  |  | pyproject.toml:18-19 · uv.lock:1940 · uv.lock:1975 · uv.lock:2050 | HF model card nvidia/Alpamayo2-Super: PyTorch ≥2.8 |
| `transformers 4.57.1` | external | `PreTrainedModel · AutoModel/AutoConfig/AutoProcessor · generate · huggingface-hub 0.36.2` | 모델 래퍼·생성·프로세서 |  |  | pyproject.toml:20 · uv.lock:2029 · uv.lock:552 · src/alpamayo2_super/models/alpamayo2_super.py:27-31 | HF model card nvidia/Alpamayo2-Super: Transformers ≥4.57.1 |
| `flash-attn 2.8.3` | external | `no-build-isolation 소스 빌드 · _supports_flash_attn/_supports_sdpa` | attention 커널(구현 미강제) |  |  | pyproject.toml:21 · pyproject.toml:40 · uv.lock:454 · src/alpamayo2_super/models/alpamayo2_super.py:111-112 |  |
| `hydra-core 1.3.2 · physical-ai-av 0.2.2` | external | `hydra.utils.instantiate · einops 0.8.2 · accelerate 1.13.0 · av 17.0.1 · matplotlib · mediapy` | 서브모듈 생성·데이터셋 리더·시각화 |  |  | pyproject.toml:6-17 · uv.lock:584 · uv.lock:418 · uv.lock:12 · uv.lock:1407 · uv.lock:196 · src/alpamayo2_super/models/expert.py:79-96 |  |
| `TensorRT / ONNX / quantization / Dockerfile (없음)` | absent | `grep -iE 'tensorrt\|onnx\|quantiz\|fp8\|nvfp4' → 0건; find Dockerfile* → 0건` | 배포 최적화·컨테이너 경로 없음 |  |  | grep -rniE 'tensorrt\|onnx\|quantiz\|fp8\|nvfp4' --include=*.py/*.toml/*.md/*.ipynb → 0건 · find -iname 'Dockerfile*' -o -iname '*.yaml' → 0건 |  |

### L0 Platform

| 이름 (코드 식별자) | 종류 | 위치 | 설명 | 순서 | 신규 | 근거 | 공식 자료 |
|---|---|---|---|---|---|---|---|
| `Python 3.12` | external | `uv sync --locked · Linux` | requires-python ==3.12.* |  |  | pyproject.toml:4 · README.md:39-42 |  |
| `NVIDIA CUDA GPU` | external | `CUDA 12.8 wheel (nvidia-cuda-runtime-cu12 12.8.90, cuDNN 9.10.2.21) · nvcc 12.x` | CUDA 필수, 2×H100 80GB 검증(데모) |  |  | src/alpamayo2_super/inference_smoke.py:119-123 · uv.lock:1232 · uv.lock:1240 · README.md:39-40 · README.md:196-198 | HF model card nvidia/Alpamayo2-Super: tested H100 80GB |
| `torch.bfloat16 · device_map="cuda:0"` | config | `2-GPU: vlm.to(cuda:0), expert.to(cuda:1)` | 단일 GPU 기본, bf16 적재·autocast |  |  | src/alpamayo2_super/inference_smoke.py:133 · src/alpamayo2_super/inference_smoke.py:138 · src/alpamayo2_super/config.py:65 · examples/two_gpu_nav_cfg_demo.py:239-245 |  |
| `nvidia/Alpamayo2-Super` | external | `PUBLIC_MODEL_ID · config.json/tokenizer/preprocessor/*.safetensors · 34B` | HF 게이트 체크포인트(크기 코드 미기재) |  | ✓ | src/alpamayo2_super/common/constants.py:18 · src/alpamayo2_super/inference_smoke.py:32-37 · README.md:12-13 · README.md:112-113 | HF model card nvidia/Alpamayo2-Super: 36B BF16 safetensors · HF model card nvidia/Alpamayo2-Super: peak 72,115 MiB |
| `nvidia/PhysicalAI-Autonomous-Vehicles` | external | `HF dataset · examples/validation_samples.json (clip_id, t0_us)` | 입력 클립 소스(스트리밍) |  |  | README.md:43-45 · README.md:115-118 · src/alpamayo2_super/load_physical_aiavdataset.py:34-35 |  |

### 궤적 추론 호출 순서

1. inference_smoke.run_smoke: CUDA 확인, 체크포인트 레이아웃 검사
2. load_physical_aiavdataset: 7캠×4프레임·ego 과거16/미래64 로드
3. select_task_input("trajectory"): 캠 (0,1,2,3,5,6)×4프레임 선택
4. from_pretrained(bf16, cuda:0) → prepare_model_inputs
5. sample_trajectories_from_data: history 48토큰 주입
6. _generate_with_shared_prefill: prefill 1회→CoC 샘플링(궤적토큰 마스크)
7. traj_future_start 정지 → expert 위치·마스크 구성
8. FlowMatching 10스텝: in_proj→expert(KV캐시)→out_proj
9. action_to_traj: (accel,curvature)×64 적분 → pred_xyz/pred_rot
10. extract_text_tokens → extra["cot"] 등, minADE 출력
11. plot_inference_result → PNG + JSON 사이드카

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

- evidence 경로는 alpamayo2 저장소 루트 기준(src/alpamayo2_super/...), 'a15 '는 alpamayo1.5 src/alpamayo1_5 기준(README/pyproject/test_inference는 해당 위치).
- ROS 2 / Autoware(alpamayo-autoware) 통합은 범위에서 제외.
- VLM 층·hidden·head 수, 체크포인트 파일 크기는 코드 미기재(체크포인트 config.json 의존). 모델 카드는 36B BF16, 피크 72,115 MiB 기재.
- 공식 자료: https://huggingface.co/nvidia/Alpamayo2-Super · https://huggingface.co/blog/nvidia/nvidia-alpamayo-2 · https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/ (WebFetch 요약으로 확인, 수치는 원문 재확인 권장).
- order는 inference_smoke 기본 궤적 경로 call_order 단계 번호. new_in_2는 alpamayo1.5 대비 파일/클래스/함수 신규 또는 역할이 크게 바뀐 경우 true.
