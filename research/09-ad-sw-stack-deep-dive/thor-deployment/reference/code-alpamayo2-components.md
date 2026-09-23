# Alpamayo 2 Super SW 컴포넌트 (코드 기반)

기준 (src/PINS.md, 클론일 2026-09-15, depth 1, LFS 미수신):

| 디렉터리 | 저장소 | ref | 커밋 SHA | 커밋 날짜 |
|---|---|---|---|---|
| alpamayo2 | NVlabs/alpamayo2 | main | 6d05b9f2dcaa6ee45ac6e053cf18653eac23c047 | 2026-09-09 |
| alpamayo-autoware_2.0-super | autowarefoundation/alpamayo-autoware | alpamayo2.0-super | b8747df228afd0e0d40d10fcfebd7b827325d50b | 2026-08-06 |
| (대조) alpamayo-recipes | NVlabs/alpamayo-recipes | main | 670b551987280979c157c1cb70b042458dbacc99 | 2026-09-08 |
| (대조) TensorRT-Edge-LLM | NVIDIA/TensorRT-Edge-LLM | v0.10.1 | e8b29522938901f6df19ebeedd4b69bc8edbcd97 | 2026-09-03 |

표기: `a2:` = alpamayo2, `aw2:` = alpamayo-autoware_2.0-super, `rc:` = alpamayo-recipes, `edge:` = TensorRT-Edge-LLM. 경로:라인은 해당 커밋 기준.
주의: 체크포인트 `config.json`(HF `nvidia/Alpamayo2-Super`)은 클론 대상이 아니므로, VLM 층수·hidden·head 수 같은 **하이퍼파라미터 값은 코드에서 확인 불가**. 코드에 나오는 것은 "config에서 읽는다"는 사실뿐이다(아래 L4 참고). 주석/README에 적힌 값은 "문서 기재"로 구분 표기.

## 요약 (10줄)

1. 공개 코드는 **순수 PyTorch + HF transformers 추론 패키지** `alpamayo2_super` 하나(학습 forward 정의는 있으나 학습 스크립트 없음). 컨테이너·TensorRT·ONNX·양자화 경로 없음.
2. 최상위 모델 `Alpamayo2Super(PreTrainedModel)` = `vlm`(config의 `vlm_class`로 transformers에서 동적 로드) + `ExpertModel`(2B급 action expert, `AutoModel.from_config(llm_config)`에서 `embed_tokens` 삭제) + 궤적 토크나이저 2개 (a2:models/alpamayo2_super.py:106-145, models/expert.py:66-96).
3. VLM 아키텍처 이름은 코드에 하드코딩되지 않음. aw2 주석·README가 "32B Qwen3-VL backbone, 8 KV heads × 64 layers"라 기재(aw2:alpamayo2_node.py:7, nav_cfg.py:29-30); rc README는 "Cosmos 3 backbone" (rc:README.md:106,113). 이미지 README 그림은 "Cosmos 3 Super Reasoner"(a2:alpamayo2super_arch.png).
4. 추론 순서: 입력 프로필 선택(6캠×4프레임) → chat template/processor 토큰화 → 과거 궤적 이산 토큰 주입(`fuse_traj_tokens`) → 공유 prefill → CoC 샘플링 디코드(`<|traj_future_start|>`에서 정지) → KV 캐시 조건부 Flow Matching Euler 10스텝 → unicycle(accel, curvature) 적분 → 64 waypoint(0.1 s, 6.4 s) xyz+회전행렬 (a2:models/alpamayo2_super.py:273-452).
5. Expert 조건화는 cross-attn이 아니라 **VLM의 KV 캐시(past_key_values) + non-causal self-attn** (a2:models/alpamayo2_super.py:377-397, expert.py:44).
6. 텍스트 태스크(meta-action, auto-labeling JSON, VQA, 2D grounding)는 `text_tasks.generate_text`가 VLM `generate`만 사용 (a2:text_tasks.py:353-437).
7. HW 가정: CUDA 필수, bf16, 기본 `device_map="cuda:0"` 단일 GPU; 선택적 2-GPU 데모(VLM cuda:0 / expert cuda:1, H100 80GB×2 검증) (a2:inference_smoke.py:119-133, examples/two_gpu_nav_cfg_demo.py:21-22,232-247, README.md:196-224).
8. 런타임 핀: Python 3.12, torch 2.8.0, transformers 4.57.1, flash-attn ≥2.8.3(lock 2.8.3), CUDA 12.8 wheel, triton 3.4.0 (a2:pyproject.toml:4-21, uv.lock).
9. ROS 2 통합(aw2)은 벤더링된 `alpamayo2_super` + `Alpamayo2RosNode`: 6×CompressedImage + Odometry 구독 → GPU JPEG 디코드 → 동일 API 호출 → Autoware `Trajectory`, CoC `String`/`StringStamped`, RViz `MarkerArray` 발행. SDPA 강제, 1 GPU 80GB+, 추론 3.35 s 평균 → 문서상 closed-loop 불가 (aw2:alpamayo2_node.py, README.md:230-288).
10. Alpamayo 2 Super용 TensorRT/Edge-LLM/Jetson/양자화 경로는 확인된 4개 저장소 어디에도 없음 (edge의 alpamayo는 Alpamayo-R1-10B, rc 양자화는 1.5 전용).

## 저장소 지도

### alpamayo2 (NVlabs/alpamayo2)

| 경로 | 내용 | 근거 |
|---|---|---|
| `pyproject.toml`, `uv.lock` | uv 프로젝트, 의존성 핀 | a2:pyproject.toml:1-47 |
| `src/alpamayo2_super/models/` | `alpamayo2_super.py`(최상위 모델), `expert.py`, `action_in_proj.py`, `expert_utils.py`, `delta_tokenizer.py`, `token_utils.py`, `utils.py`, `diffusion_expert_cuda_graph.py` | find 결과 |
| `src/alpamayo2_super/config.py` | `Alpamayo2SuperConfig`, 토크나이저 빌더 | a2:config.py:31-203 |
| `src/alpamayo2_super/diffusion/` | `BaseDiffusion`, `FlowMatching` | a2:diffusion/flow_matching.py:25 |
| `src/alpamayo2_super/action_space/` | `UnicycleAccelCurvatureActionSpace`, `DiscreteTrajectoryTokenizer`, 수치 유틸 | a2:action_space/unicycle_accel_curvature.py:38 |
| `src/alpamayo2_super/chat_template/conversation.py` | 프롬프트/대화 구성 | a2:chat_template/conversation.py:51-411 |
| `src/alpamayo2_super/input_profiles.py` | 태스크별 카메라·프레임 프로필 | a2:input_profiles.py:36-51 |
| `src/alpamayo2_super/helper.py` | processor 로드·입력 토큰화 | a2:helper.py:49-102 |
| `src/alpamayo2_super/text_tasks.py` | meta-action / auto-labeling / VQA(+grounding) 생성·파싱 | a2:text_tasks.py:39-437 |
| `src/alpamayo2_super/load_physical_aiavdataset.py` | PhysicalAI-AV 데이터 로더 | a2:load_physical_aiavdataset.py:32 |
| `src/alpamayo2_super/viz_utils.py`, `visualization.py` | matplotlib 그림·JSON 사이드카·MP4 | a2:viz_utils.py:1215-1722 |
| `src/alpamayo2_super/common/` | 상수(카메라명), 로깅, distributed 헬퍼, config 저장 | a2:common/constants.py:18-54 |
| `src/alpamayo2_super/geometry/` | 회전·좌표 유틸 | a2:geometry/rotation.py |
| 엔트리포인트 CLI | `python -m alpamayo2_super.inference_smoke` (argparse `main`), `test_inference.py`(호환 엔트리) | a2:inference_smoke.py:184-268, README.md:313-320 |
| `examples/two_gpu_nav_cfg_demo.py` | 2-GPU 내비 CFG 데모 | a2:examples/two_gpu_nav_cfg_demo.py:16-24 |
| `examples/*.json` | 검증 샘플 manifest (clip_id, t0_us) 3종 | a2:inference_smoke.py:82-89 |
| `notebooks/` | `inference.ipynb`, `meta_actions.ipynb`, `autolabeling.ipynb`, `vqa.ipynb`, `clip_ids.parquet` | a2:README.md:226-294 |
| `tests/test_diffusion_expert_cuda_graph.py` | CUDA graph 단위 테스트(CUDA 없으면 skip) | a2:tests/test_diffusion_expert_cuda_graph.py:21,122 |
| config 파일 | yaml/hydra 설정 파일 **없음** (hydra는 `hyu.instantiate`로 체크포인트 config.json 내 `_target_` dict를 인스턴스화) | find `*.yaml` 0건; a2:models/expert.py:79-96 |
| Dockerfile | **없음** | find `Dockerfile*` 0건 |

### alpamayo-autoware (branch alpamayo2.0-super)

| 경로 | 내용 | 근거 |
|---|---|---|
| `src/alpamayo_ros/` | ament_python 패키지 `alpamayo_ros` (노드 2개: `alpamayo_node`(1.5), `alpamayo2_node`) | aw2:src/alpamayo_ros/setup.py:27-31, package.xml:1-27 |
| `src/alpamayo_ros/alpamayo_ros/alpamayo2_node.py` | `Alpamayo2RosNode` | aw2:alpamayo2_node.py:71 |
| `.../conversions.py` | 오도메트리→ego history, 검사, Autoware Trajectory/Marker 변환 | aw2:conversions.py:38-419 |
| `.../nav_cfg.py`, `nav_text.py` | 단일 GPU 내비 CFG, lanelet2 경로→지시문 | aw2:nav_cfg.py:4-33, nav_text.py:4-117 |
| `src/alpamayo_ros/launch/alpamayo2.launch.py` | 런치(파라미터 선언) | aw2:launch/alpamayo2.launch.py:12-95 |
| `run_alpamayo2_node.sh` | 소스트리 직접 실행 스크립트(PYTHONPATH, use_sim_time=true) | aw2:run_alpamayo2_node.sh:19-46 |
| `src/alpamayo2_super/` | 업스트림 벤더링 사본 (commit 9596749e, 2026-08-03) | aw2:src/alpamayo2_super/UPSTREAM.md:7-9 |
| `src/alpamayo1_5/` | 1.5 모델 패키지(대조용) | find |
| `pyproject.toml` | 이름은 `alpamayo1_5`, Python ≥3.10, torch 2.8.0, transformers 4.57.1, flash-attn ≥2.8.3, opencv-python | aw2:pyproject.toml:2-20 |
| RViz config / Dockerfile / yaml | **없음** ("No RViz config ships with this branch") | aw2:README.md:268; find 0건 |

벤더링 사본 vs 현 업스트림 차이(diff -rq): aw2에는 `load_physical_aiavdataset.py` 제거(의도적, UPSTREAM.md:19-24), `models/diffusion_expert_cuda_graph.py` 없음(업스트림이 벤더링 이후 추가), `unicycle_accel_curvature.py`의 curvature bounds (-0.2,0.2) vs 업스트림 (-0.33,0.33)+저속 곡률 0 처리(a2:action_space/unicycle_accel_curvature.py:35,48,197-212).

## 층별 인벤토리 (L0~L8)

### L0 HW

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| NVIDIA CUDA GPU (필수) | CUDA 없으면 즉시 RuntimeError | a2:inference_smoke.py:119-123 |
| 단일 GPU `cuda:0` 기본 배치 | `from_pretrained(..., dtype=bfloat16, device_map="cuda:0")` | a2:inference_smoke.py:133; notebooks 4종 동일(a2:notebooks/inference.ipynb:112 등) |
| 2-GPU 분할(선택, 데모) | VLM+prefill cuda:0, expert+guided/unguided KV cache cuda:1; 서로 다른 CUDA 인덱스 강제 | a2:examples/two_gpu_nav_cfg_demo.py:21-22,91-115,232-247,442-448 |
| 메모리 (문서 기재) | 2×H100 80GB에서 VLM GPU ~67 GiB, expert GPU ~71 GiB 피크; 호스트 RAM도 전체 모델 적재 필요 | a2:README.md:196-224 |
| ROS 노드 GPU (문서 기재) | 1 GPU 80GB+, RTX PRO 6000 Blackwell 96GB에서 피크 69.1 GiB; 가중치 ~72 GB bf16 | aw2:README.md:218,230,278-284 |
| GPU JPEG 디코드 | `torchvision.io.decode_jpeg(device="cuda")` — CPU 경로 없음 | aw2:alpamayo2_node.py:425; README.md:231 |
| CPU/호스트 | Linux 호스트 가정, 명시적 CPU 추론 경로 없음 | a2:README.md:39 |
| dtype | bfloat16 기본 (config `dtype="bfloat16"`, autocast bf16) | a2:config.py:65,187-200; inference_smoke.py:138 |

### L1 OS·드라이버·컨테이너

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| Linux + CUDA 드라이버/런타임, CUDA Toolkit 12.x + nvcc | flash-attn 소스 빌드용 | a2:README.md:39-41,82-84 |
| CUDA 12.8 런타임 wheel | `nvidia-cuda-runtime-cu12 12.8.90`, cuDNN 9.10.2.21, NCCL 2.27.3 | a2:uv.lock:1231-1232,1239-1240,1309-1310 |
| Python 3.12 (업스트림) | `requires-python = "==3.12.*"` | a2:pyproject.toml:4 |
| Python 3.10 (ROS 통합) | ROS 2 Humble 호환 위해 3.10에서 무수정 임포트 | aw2:UPSTREAM.md:26-30, README.md:15 |
| ROS 2 Humble (+ Jazzy 파라미터 호환 주석) | 노드 실행 환경 | aw2:README.md:16, alpamayo2_node.py:86 |
| Autoware 워크스페이스 (필수) | `autoware_planning_msgs`, `autoware_internal_debug_msgs` 임포트 | aw2:alpamayo2_node.py:43-44, README.md:232 |
| 컨테이너 | Dockerfile/베이스 이미지 **없음** (uv venv 방식) | find 0건; a2:README.md:55-64 |

### L2 런타임·라이브러리

| 컴포넌트 | 버전(선언 / lock) | 역할 | 코드 근거 |
|---|---|---|---|
| torch | ==2.8.0 / 2.8.0 | 텐서·autocast·CUDA graph | a2:pyproject.toml:18; uv.lock:1939 |
| torchvision | ≥0.23.0 / 0.23.0 | (aw2) GPU JPEG 디코드 | a2:pyproject.toml:19; aw2:alpamayo2_node.py:42,425 |
| transformers | ==4.57.1 / 4.57.1 | PreTrainedModel, AutoModel/AutoConfig/AutoProcessor, generate, DynamicCache | a2:pyproject.toml:20; models/alpamayo2_super.py:27-31 |
| flash-attn | ≥2.8.3 / 2.8.3 (sdist 빌드) | attention 커널 | a2:pyproject.toml:21,40; uv.lock:453-460 |
| attention 구현 | 모델이 `_supports_flash_attn`/`_supports_sdpa` 선언; 업스트림은 `attn_implementation` 미지정(HF 기본 선택), aw2는 `"sdpa"` 강제(flash-attn 2.8.3에 Blackwell sm_120 커널 없음) | a2:models/alpamayo2_super.py:111-112, expert.py:71-72; aw2:alpamayo2_node.py:321-330 |
| triton | lock 3.4.0 (torch 의존) | — | a2:uv.lock:2049 |
| accelerate | ≥1.12.0 / 1.13.0 | device_map 적재 | a2:pyproject.toml:6; uv.lock:11 |
| safetensors | lock 0.7.0 (transformers 경유) | `*.safetensors` 샤드 존재 검사 | a2:uv.lock:1782; inference_smoke.py:78 |
| huggingface-hub | lock 0.36.2 | HF 다운로드/인증 | a2:uv.lock:551 |
| hydra-core (+hydra-colorlog) | ≥1.3.2 / 1.3.2 | `hydra.utils.instantiate`로 토크나이저/액션스페이스/디퓨전/프로젝터 생성 | a2:pyproject.toml:9-10; models/expert.py:79-96 |
| einops | ≥0.8.1 / 0.8.2 | reshape | a2:models/alpamayo2_super.py:414-441 |
| av (PyAV) | ≥16.0.1 / 17.0.1 | 비디오(데이터셋/MP4) | a2:pyproject.toml:7 |
| physical-ai-av | ≥0.2.0 / 0.2.2 | PhysicalAI-AV 데이터셋 리더 | a2:pyproject.toml:15; load_physical_aiavdataset.py |
| numpy, scipy, pandas, pillow, matplotlib, mediapy | — | 수치·시각화 | a2:pyproject.toml:11-17 |
| rclpy, lanelet2, autoware_lanelet2_extension_python | (시스템/Autoware) | ROS·내비 텍스트 | aw2:alpamayo2_node.py:40; nav_text.py:21-22 |
| deepspeed, decord, opencv | a2에는 **없음** (aw2 pyproject에 opencv-python은 1.5용으로 존재) | — | grep 0건(a2); aw2:pyproject.toml:20 |

### L3 모델 로딩·체크포인트

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| HF Hub ID `nvidia/Alpamayo2-Super` 또는 로컬 디렉터리 | `PUBLIC_MODEL_ID`, env `ALPAMAYO2_SUPER_MODEL_ID` | a2:common/constants.py:18; inference_smoke.py:187-190 |
| 로컬 체크포인트 레이아웃 검사 | `config.json`, `tokenizer.json`, `tokenizer_config.json`, `preprocessor_config.json`, `*.safetensors` 필수 | a2:inference_smoke.py:32-37,53-79 |
| `AutoConfig/AutoModel.register` | `model_type="alpamayo2_super"`, `"alpamayo2_super_expert"` 등록 | a2:config.py:55,203; models/alpamayo2_super.py:455; expert.py:164-165 |
| `Alpamayo2Super.from_pretrained(dtype=bf16, device_map="cuda:0")` | 단일 GPU 직접 적재(aw2 주석: `.to()` 재호출 시 72GB 이중 적재 위험) | a2:inference_smoke.py:133; aw2:alpamayo2_node.py:321-330 |
| 샤딩 (문서 기재) | ~71.6 GB, bf16, 32 files; `model.safetensors.index.json` 해시 기록 | aw2:UPSTREAM.md:10; a2:viz_utils.py:216-221 |
| 로드 시 무시 키 | Fourier freqs 버퍼, action space 정규화 통계 | a2:models/alpamayo2_super.py:113-117 |
| 2-GPU 수동 배치 | `from_pretrained`(CPU) → `vlm.to(cuda:0)`, `expert.to(cuda:1)`; `device_map="auto"/"balanced"` 비권장 | a2:examples/two_gpu_nav_cfg_demo.py:24,232-247 |
| CUDA graph (선택) | `enable_diffusion_expert_cuda_graph(max_batch_size, max_graphs=4)` — expert forward exact-shape 캡처/리플레이 | a2:models/alpamayo2_super.py:147-167; diffusion_expert_cuda_graph.py:104-375 |
| 모델 로드 시간 (문서 기재) | 28.6 s (RTX PRO 6000) | aw2:README.md:282 |

### L4 모델 컴포넌트

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| `Alpamayo2Super` | 최상위 HF 래퍼; `vlm`, `tokenizer`, `history_traj_tokenizer`, `future_traj_tokenizer`, `expert` | a2:models/alpamayo2_super.py:106-145 |
| VLM 백본 `self.vlm` | `getattr(transformers, config.vlm_class)._from_config(vlm_config)`; `vlm_class = vlm_config.architectures[0]` → 클래스명은 체크포인트 config에 있음(코드엔 없음). 층/hidden/head 값: **코드에서 확인 불가**. 문서 기재: "32B Qwen3-VL backbone", "8 KV heads over 64 layers" (aw2), "Cosmos 3 backbone" (rc) | a2:models/alpamayo2_super.py:123-124; config.py:145-147,161-162; aw2:alpamayo2_node.py:7, nav_cfg.py:29-30; rc:README.md:106,113 |
| 비전 인코더/이미지 토크나이저 | 별도 클래스 없음 — VLM 내부 vision tower + HF `AutoProcessor`(min_pixels=163840, max_pixels=196608); `pixel_values`, `image_grid_thw`를 VLM에 전달 | a2:config.py:67-68; helper.py:49-65; models/alpamayo2_super.py:195-202 |
| 텍스트 토크나이저 | `AutoTokenizer.from_pretrained(fix_mistral_regex=True)` + 이산 궤적 토큰 `<i0>..<i3999>`(history 1000 + future 3000) + 특수 토큰 29종 `<|key|>` | a2:config.py:31-41,63-64; models/utils.py:26-57 |
| vocab 확장 | `text_config.vocab_size`를 128 배수로 올림 | a2:config.py:146 |
| 특수 토큰(발췌) | `image_start/end`, `traj_history_start/end`, `cot_start/end`, `meta_action_start/end`, `traj_future_start/end`, `route_start/pad/end`, `question_start/end`, `answer_start/end`, `vectorized_wm*` | a2:models/utils.py:26-56 |
| 과거 궤적 토크나이저 | `DeltaTrajectoryTokenizer`(delta xyz 1000 bins, ±4 m xy/±10 m z, 선택적 yaw) — hydra로 인스턴스화; 16 waypoint→48 토큰(3축×16) 검증 | a2:models/delta_tokenizer.py:21-60; config.py:28,113-130 |
| 궤적 토큰 주입 `fuse_traj_tokens` | `<|traj_history|>` 패드 자리를 이산 토큰으로 치환 (future는 auto-label 입력시만) | a2:models/utils.py:103-177 |
| 궤적 토큰 로짓 마스킹 | CoC 생성 중 이산 궤적 토큰 span `-inf` (`MaskDiscreteTrajectoryLogitsProcessor`), 텍스트 EOS 마스킹 | a2:models/alpamayo2_super.py:61-103,322-338 |
| Action expert `ExpertModel` | `AutoModel.from_config(llm_config)` 트랜스포머(임베딩 삭제), `expert_non_causal_attention=True`; 파라미터 규모는 문서 기재 "2B" | a2:models/expert.py:31-96; a2:README.md:12-14 |
| Expert 조건화 | **VLM KV 캐시 공유**: `past_key_values=prompt_cache`, MRoPE position(`rope_deltas + offset`), 생성 CoC 이후~expert 토큰 사이 마스킹, 매 스텝 `prompt_cache.crop(prefill_seq_len)` | a2:models/alpamayo2_super.py:353-397; expert_utils.py:92-123 |
| `PerWaypointActionInProjV2` | 액션(64×2) 각 축 Fourier(20) + timestep Fourier → MLP(4층, 1024) → LayerNorm → expert hidden | a2:models/action_in_proj.py:94-143 |
| `action_out_proj` | hydra 인스턴스(hidden→2) — 구체 클래스는 체크포인트 config | a2:models/expert.py:92-96 |
| `FlowMatching` | Euler 적분, 기본 `num_inference_steps=10`, x0~N(0,I), t: 0→1 linspace; CFG 옵션(`unguided_step_fn`) 있으나 config에서 켜면 ValueError | a2:diffusion/flow_matching.py:25-149; models/expert.py:84-85 |
| `UnicycleAccelCurvatureActionSpace` | 액션 = (accel, curvature)×64, dt=0.1; `action_to_traj`로 t0 상태(과거 궤적 미분으로 v0 추정)에서 적분 → xyz, rot | a2:action_space/unicycle_accel_curvature.py:38-102,216-389 |
| Meta-action "헤드" | 별도 헤드 없음 — VLM 텍스트 출력 `Longitudinal:/Lateral:/Lane:` 정규식 분리 | a2:models/token_utils.py:121-131 |
| Grounding / auto-label 출력 | 별도 모듈 없음 — 텍스트 JSON(bbox_2d 등)·4필드 JSON 파싱 | a2:models/token_utils.py:182-191; text_tasks.py:41-46,324-351 |
| 학습 forward | 이산 future 토큰 CE + 기타 CE, expert flow-matching MSE (학습 루프는 없음) | a2:models/alpamayo2_super.py:225-271; expert.py:123-161 |

### L5 데이터·전/후처리

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| 카메라 정규 링(7) | 0 cross_left_120fov, 1 front_wide_120fov, 2 cross_right_120fov, 3 rear_left_70fov, 4 rear_tele_30fov, 5 rear_right_70fov, 6 front_tele_30fov | a2:common/constants.py:20-37 |
| 입력 프로필 | trajectory/meta_action/auto_labeling/grounding: 캠 (0,1,2,3,5,6); VQA: (0,1,2,3,4,5); 4프레임 | a2:input_profiles.py:36-51 |
| 프레임 시점 | t0-0.3, -0.2, -0.1, t0 (10 Hz) | a2:load_physical_aiavdataset.py:176-180 |
| Ego history | 16 poses @10 Hz(1.6 s), t0 로컬 프레임 xyz + 3×3 rot | a2:load_physical_aiavdataset.py:37-39,118-141,248-249 |
| GT future | 64 poses @10 Hz (6.4 s) | a2:load_physical_aiavdataset.py:38,251-252 |
| 이미지 전처리 | uint8→float/255, processor(`do_rescale=False`)가 min/max_pixels로 리사이즈 | a2:helper.py:84-95; config.py:67-68 |
| 대화 구성 | system "You are a driving assistant that generates safe and accurate actions." → user: [카메라ID 텍스트 + `frame i` + image]×6×4, traj_history 패드, 지시문 "output the chain-of-thought reasoning of the driving process, then output the future trajectory." | a2:chat_template/conversation.py:51-95,98-155; helper.py:28-46 |
| 카메라 ID 오름차순 assert | 템플릿 내부 | a2:chat_template/conversation.py:115-116 |
| 태스크 프롬프트 | meta_action: cot→meta_action→traj_future; auto_labeling: "comprehensive analysis ... in JSON format"; VQA: 질문 텍스트만 | a2:text_tasks.py:54-58; conversation.py:78-83 |
| 내비 지시문 | 구조 토큰 없는 raw text(`construct_nav_instruction`) | a2:chat_template/conversation.py:247-271 |
| 출력 파싱 | assistant 텍스트를 `<|traj_future_start|>`/`<|im_end|>`에서 절단 → `cot`, `meta_action`, `answer`, `box`, `cot_auto_labeling` | a2:models/token_utils.py:134-179 |
| 궤적 출력 형식 | `pred_xyz [B, sets, samples, 64, 3]`, `pred_rot [...,64,3,3]`, `logprob`=0 placeholder | a2:models/alpamayo2_super.py:424-445; aw2:alpamayo2_node.py:14-15 |
| Auto-label JSON | 4 키: critical_components_analysis, ego_vehicle_motion_analysis, trajectory_analysis, chain_of_causation | a2:text_tasks.py:41-46,338-351 |
| 2D grounding | bbox JSON 텍스트 파싱·스케일·오버레이 | a2:viz_utils.py:667-790 |

### L6 추론 파이프라인

`Alpamayo2Super.sample_trajectories_from_data` (a2:models/alpamayo2_super.py:273-452) 호출 순서:

| 단계 | 내용 | 근거 |
|---|---|---|
| 0 | `select_task_input(data,"trajectory")` → `helper.prepare_model_inputs` → `to_device("cuda")` | a2:inference_smoke.py:130-135 |
| 1 | `fuse_traj_tokens`로 history 토큰 주입 | :300-307 |
| 2 | generation config: `do_sample=True, top_p=0.98, temperature=0.6, top_k=None, max_new_tokens=max(256, tokens_per_future_traj=128)` | :310-320; config.py:73 |
| 3 | 공유 prefill: `vlm.model(input_ids[:, :-1], pixel_values...)` → 캐시 `batch_repeat_interleave(num_traj_samples×num_traj_sets)` | :182-205 |
| 4 | CoC 디코드: `vlm.generate(past_key_values=prompt_cache)` + 궤적토큰 마스킹 + `StopAfterEOS(<|traj_future_start|>)` | :207-217,322-346 |
| 5 | EOS 이후 패딩, offset·MRoPE position·attention mask 구성 | :348-375 |
| 6 | Flow Matching Euler (`inference_step` 기본 10): step_fn = action_in_proj → expert(KV cache, non-causal) → crop → action_out_proj; 선택적 CUDA graph 컨텍스트 | :381-412 |
| 7 | `action_space.action_to_traj`(마지막 history pose 기준) → reshape | :414-441 |
| 8 | `extract_text_tokens` → `extra["cot"]` 등 | :447-452 |
| 멀티샘플 | `num_traj_samples × num_traj_sets` 배치 복제; 입력 batch는 1 샘플만(`prepare_model_inputs`) | :309; helper.py:96-97 |
| 텍스트 태스크 | `text_tasks.generate_text`: VLM generate만, max_new_tokens 기본 1024(auto_label/VQA)/512(meta) | a2:text_tasks.py:353-437 |
| 2-GPU CFG | guided/unguided 2회 prefill(cuda:0) → 캐시를 cuda:1로 이동 → `diffusion.sample(use_classifier_free_guidance=True, unguided_step_fn)` | a2:examples/two_gpu_nav_cfg_demo.py:257-530 |
| 시각화 | `plot_inference_result`/`plot_compact_inference_result` → PNG+JSON, minADE 출력 | a2:inference_smoke.py:151-181 |

### L7 통합 (alpamayo-autoware 2.0-super)

노드: `Alpamayo2RosNode(rclpy.node.Node)`, 노드명 `alpamayo2_node`, console script `alpamayo2_node = alpamayo_ros.alpamayo2_node:main` (aw2:alpamayo2_node.py:71-75; setup.py:30).

구독:

| 토픽 (기본) | 타입 | QoS | 근거 |
|---|---|---|---|
| `camera_topics` 6개 (런치 기본 `/sensing/camera/camera{5,1,6,9,10,2}/image_raw/compressed` → ID 0,1,2,3,5,6) | sensor_msgs/CompressedImage | BEST_EFFORT, KEEP_LAST 10; 버퍼 deque(12) | aw2:launch/alpamayo2.launch.py:18-37; alpamayo2_node.py:199-213 |
| `/localization/kinematic_state` | nav_msgs/Odometry | BEST_EFFORT, depth 50; 50 Hz→10 Hz 5개마다 샘플 | aw2:alpamayo2_node.py:141-143,215-222,405-407 |
| `/planning/mission_planning/route` (nav_cfg_enabled 시) | autoware_planning_msgs/LaneletRoute | RELIABLE, TRANSIENT_LOCAL, depth 1 | aw2:alpamayo2_node.py:248-255 |

발행:

| 토픽 | 타입 | 근거 |
|---|---|---|
| `/alpamayo/predicted_trajectory` | autoware_planning_msgs/Trajectory (frame `base_link`, 헤더 stamp = 입력 t0, time_from_start=(i+1)×0.1 s, 속도는 차분) | aw2:alpamayo2_node.py:166-167,585-592; conversions.py:186-248 |
| `/alpamayo/predicted_trajectory_markers` | visualization_msgs/MarkerArray (LINE_STRIP 궤적, ego footprint, TEXT_VIEW_FACING CoC) | aw2:alpamayo2_node.py:178-179,594-604; conversions.py:273-397 |
| `/alpamayo/reasoning` | std_msgs/String | aw2:alpamayo2_node.py:170-171,606-609 |
| `/alpamayo/reasoning_stamped` | autoware_internal_debug_msgs/StringStamped | aw2:alpamayo2_node.py:174-175,611-614 |
| `/alpamayo/nav_text` | std_msgs/String | aw2:alpamayo2_node.py:133,232-234,527-529 |

파라미터(기본값, aw2:alpamayo2_node.py:77-136): `model_name=nvidia/Alpamayo2-Super`, `inference_period_sec=2.0`, `camera_indices=[0,1,2,3,5,6]`(정확히 일치 강제, :290-311), `max_generation_length=256`, `num_diffusion_steps=10`, `top_p=0.98`, `temperature=0.6`, `max_image_long_side=1280`, `marker_line_width=1.2`, `marker_z_offset=0.4`, `ego_footprint=[4.77,1.73,1.03]`, `max_frame_age_sec=3.0`, `skip_on_bad_history=true`, `drop_bad_trajectory=true`, `seed=0`, `nav_cfg_enabled=false`, `lanelet2_map_path=""`, `route_topic`, `nav_text_topic`, `nav_guidance_weight=-1.0`(체크포인트 값 3.0 사용).

실행·스레딩: `create_timer(inference_period)` → in-flight면 tick 드롭 → `ThreadPoolExecutor(max_workers=1)`에서 `_run_inference` (aw2:alpamayo2_node.py:182-183,263,353-361).

전처리: 콜백은 JPEG 바이트만 저장 → 준비 조건 검사(프레임 수, 오도메트리 16×5, 프레임 age, ego history 불변식) → GPU `decode_jpeg` → bicubic 다운스케일(long side 1280) → `[6,4,3,H,W]` → 캐시된 processor로 GPU 토큰화(`device=cuda`) (aw2:alpamayo2_node.py:363-505). Ego history 변환 `xyz_local = R_t0^-1(xyz - xyz_t0)` (aw2:conversions.py:38-79); 출력 검사 `check_trajectory`(시작점 오차 2 m 등) (conversions.py:144-160).

추론: 기본 경로는 업스트림 `sample_trajectories_from_data` 그대로(num_traj_samples=1), 내비 활성 시 `nav_cfg.tokenize_nav_prompts` + `nav_cfg.sample_with_nav_cfg`(단일 GPU, guided/unguided 캐시, 동일 디바이스 assert) (aw2:alpamayo2_node.py:532-566; nav_cfg.py:180-419, 230-237). 내비 지시문은 lanelet2 맵(MGRSProjector)+route에서 "Turn left in 30m" 등 생성 (aw2:nav_text.py:32-117).

런치/재생: `alpamayo2.launch.py`(파라미터 전부 launch arg), `run_alpamayo2_node.sh`(use_sim_time=true, rosbag 재생 전제); rosbag route QoS override 예시 (aw2:launch/alpamayo2.launch.py:39-95; run_alpamayo2_node.sh:37-46; README.md:359-374).

성능(문서 기재, RTX PRO 6000 96GB, 304회): 추론 평균 3.35 s / p90 3.97 s, 피크 VRAM 69.1 GiB; 내비 CFG 시 5.2 s/70.9 GiB; "not usable closed-loop" (aw2:README.md:278-288,340-344).

### L8 API / HMI / 도구

| 컴포넌트 | 역할 | 코드 근거 |
|---|---|---|
| Python 공개 API | `Alpamayo2Super.from_pretrained`, `sample_trajectories_from_data`, `helper.prepare_model_inputs`, `input_profiles.select_task_input`, `text_tasks.prepare_text_generation_inputs/prepare_vqa_inputs/generate_text/parse_auto_labeling_json` | a2:models/alpamayo2_super.py:273; helper.py:68; input_profiles.py:198; text_tasks.py:238-447 |
| CLI | `inference_smoke` (--model-id, --manifest, --sample-index, --save-viz, --save-json, --figure-style blog/compact, --diffusion-steps 10, --seed 42, --require-camera-projection) | a2:inference_smoke.py:184-237 |
| 2-GPU 데모 CLI | `examples/two_gpu_nav_cfg_demo.py` (--vlm-device, --expert-device) | a2:examples/two_gpu_nav_cfg_demo.py:641-720 |
| Jupyter 노트북 4종 | inference / meta_actions / autolabeling / vqa(+grounding) | a2:notebooks/*.ipynb; README.md:226-294 |
| 시각화 API | `plot_inference_result`, `plot_compact_inference_result`, `plot_meta_action_result`, `plot_vqa_result`, `plot_grounding_result`, `plot_auto_labeling_result`(+MP4) | a2:visualization.py; viz_utils.py:1215-1722 |
| 산출물 | PNG + JSON 사이드카(체크포인트 해시·입력 프로필 메타) | a2:viz_utils.py:203-227,1005-1021 |
| RViz (HMI) | MarkerArray(궤적·footprint·CoC 텍스트); rviz 설정 파일 미동봉 | aw2:conversions.py:320-397; README.md:266-274 |
| ROS 토픽 텍스트 | reasoning / reasoning_stamped / nav_text | L7 표 |
| 테스트 | CUDA graph pytest | a2:tests/test_diffusion_expert_cuda_graph.py |
| 웹 UI(gradio/streamlit/fastapi), AlpaSim/closed-loop 훅, 벤치마크 스크립트 | **없음** | grep 0건 |

## 데이터·제어 흐름 (엣지 목록)

### 업스트림 추론 경로 (a2)

1. PhysicalAI-AV (HF dataset) → `load_physical_aiavdataset` (7캠 × 4프레임 uint8, egomotion 16 past/64 future, calib) [a2:load_physical_aiavdataset.py:32-252]
2. `load_physical_aiavdataset` → `select_task_input("trajectory")` (6캠 (0,1,2,3,5,6) × 4프레임, 상대 timestamps) [a2:input_profiles.py:120-206]
3. `select_task_input` → `helper.create_messages`/`build_conversation` (system+user 메시지: 이미지, traj_history 패드 48, 지시문) [a2:helper.py:28-46]
4. messages + images → HF `AutoProcessor` (`input_ids`, `attention_mask`, `pixel_values`, `image_grid_thw`) [a2:helper.py:77-95]
5. `input_ids` + ego_history_xyz/rot → `DeltaTrajectoryTokenizer` via `fuse_traj_tokens` (이산 `<i*>` 토큰 치환) [a2:models/utils.py:154-177]
6. tokenized_data → VLM `vlm.model` prefill (KV cache, rope_deltas) [a2:models/alpamayo2_super.py:197-205]
7. KV cache → VLM `generate` (CoC 텍스트 토큰, `<|traj_future_start|>`까지) [:207-217]
8. VLM KV cache(prefill+CoC) + offset/MRoPE/mask → `ExpertModel.expert` [:353-397]
9. `FlowMatching` 노이즈 x_t, t → `PerWaypointActionInProjV2` → expert → `action_out_proj` → 속도장 v (×10 Euler) [:381-412; diffusion/flow_matching.py:106-149]
10. 샘플 액션 (64×[accel, curvature]) + 마지막 history pose → `UnicycleAccelCurvatureActionSpace.action_to_traj` → `pred_xyz(64,3)`, `pred_rot(64,3,3)` [:414-428]
11. 생성 시퀀스 → `extract_text_tokens` → `extra{cot, meta_action, answer, box, cot_auto_labeling}` [:447-452]
12. pred_xyz + extra + data → `viz_utils.plot_*` → PNG/JSON [a2:inference_smoke.py:156-181]
13. (텍스트 태스크) tokenized_data → `vlm.generate` → `extract_text_tokens` → meta-action 분리 / auto-label JSON / bbox [a2:text_tasks.py:353-437]
14. (선택) guided/unguided prompt → 2× prefill (cuda:0) → 캐시 이동 → expert CFG (cuda:1) [a2:examples/two_gpu_nav_cfg_demo.py:257-530]

### ROS 2 경로 (aw2)

1. Autoware 카메라 드라이버/rosbag → `/sensing/camera/cameraN/image_raw/compressed` (CompressedImage) → `_image_callback` (JPEG 바이트 버퍼) [aw2:alpamayo2_node.py:363-366]
2. Autoware localization → `/localization/kinematic_state` (Odometry) → `_odometry_callback` [:368-369]
3. timer(2.0 s) → `_prepare_inference_payload` (준비·신선도 검사) [:353-450]
4. odometry 16×(10 Hz) → `conversions.build_ego_history`/`check_ego_history` (t0 로컬 xyz/rot) [conversions.py:38-143]
5. JPEG → `torchvision.io.decode_jpeg(cuda)` → `_downscale` → image_frames [6,4,3,H,W] [:425-436]
6. payload → `_tokenize` (upstream `helper.create_messages` + 캐시 processor, GPU) [:468-505]
7. (opt) `/planning/mission_planning/route` (LaneletRoute) + lanelet2 map → `nav_text.compute_nav_text` → 지시문 → `/alpamayo/nav_text` [:507-530]
8. model_inputs → `Alpamayo2Super.sample_trajectories_from_data` (또는 `nav_cfg.sample_with_nav_cfg`) → pred_xyz/rot, extra.cot [:532-566]
9. pred_xyz → `conversions.check_trajectory` → (통과 시) `to_autoware_trajectory` → `/alpamayo/predicted_trajectory` (Trajectory, base_link, stamp=t0) [:568-592]
10. pred_xyz + cot → `trajectory_to_markers` → `/alpamayo/predicted_trajectory_markers` (MarkerArray) → RViz [:594-604]
11. cot → `/alpamayo/reasoning` (String), `/alpamayo/reasoning_stamped` (StringStamped) [:606-614]
12. (코드상 소비자 없음) Trajectory → Autoware planning/control: 이 브랜치에서 연결 코드·런치 없음; README가 closed-loop 불가라 명시 [aw2:README.md:286-288]

## 코드에 없는 것 (확인 방법)

| 부재 항목 | 확인 방법 | 결과 |
|---|---|---|
| Alpamayo 2 Super용 TensorRT / ONNX 경로 | `grep -rniE "tensorrt\|onnx\|trtllm"` in a2(py/toml/md/ipynb), aw2(alpamayo_ros, alpamayo2_super, sh) | a2 0건; aw2 1건 = "The TensorRT expert engine is unavailable for this generation" (aw2:alpamayo2_node.py:21); README 표 "TensorRT expert: No" (aw2:README.md:223) |
| Jetson / aarch64 / Thor / Orin 처리 | `grep -rniE "jetson\|aarch64\|arm64\|thor"` | a2·aw2 코드 0건. ("orin" 매치는 "origin"의 부분문자열). 단 uv.lock에는 PyPI wheel 목록의 aarch64 항목 49건 존재(플랫폼별 wheel 메타데이터일 뿐 처리 코드 아님; resolution-markers는 win32/emscripten/기타만) |
| 양자화 (FP8/NVFP4/INT4/AWQ/GPTQ) | `grep -rniE "quantiz\|fp8\|nvfp4\|int4\|awq\|gptq"` | 0건 (delta_tokenizer.py:112 "quantize delta yaw" 주석은 bin 이산화) ; rc의 양자화 레시피는 `recipes/alpamayo1_5_quant`만 (rc:README.md:78) |
| alpamayo-recipes의 2 Super 학습/후처리 레시피 | `ls rc/recipes`; grep "alpamayo2" | recipes = alpamayo1_sft, alpamayo1_5_sft, alpamayo1_x_rl, alpamayo1_5_quant. 2 Super는 README 소개·링크만 (rc:README.md:28,106-128) |
| TensorRT-Edge-LLM의 Alpamayo 2 지원 | `grep -rniE "alpamayo2\|alpamayo 2\|alpamayo-2\|alpamayo2_super"` in edge | 0건. edge의 alpamayo 모델은 `alpamayo_r1` / Alpamayo-R1-10B (edge:experimental/builder/models/registry.py:540-553; docs/source/user_guide/examples/vla/alpamayo.md:1-3; CHANGELOG.md:86 "Added Alpamayo-1 support") |
| vLLM/Triton 서버, 웹 UI (gradio/streamlit/fastapi/flask) | grep 동일 키워드 | 0건 (lock의 triton 3.4.0은 torch 의존 커널 컴파일러) |
| Dockerfile / 컨테이너 / yaml·hydra 설정 파일 / RViz 설정 | `find -iname 'Dockerfile*' -o -iname '*.yaml' -o -iname '*.yml' -o -iname '*.rviz'` | 0건 (JSON은 examples manifest 3개뿐); aw2:README.md:268 "No RViz config ships" |
| 학습 스크립트/DeepSpeed | grep deepspeed, find train*.py | 0건 (forward 손실 정의만 존재) |
| AlpaSim / closed-loop 시뮬 훅 | grep "alpasim\|closed.loop" | a2 0건; aw2는 README에서 closed-loop 불가 명시만 |
| VLM 하이퍼파라미터(층/hidden/heads)·VLM 클래스명 하드코딩 | grep "Qwen3VL\|num_hidden_layers\|num_key_value_heads" | a2 0건 (체크포인트 config.json에서 동적 결정); aw2 주석에 "Qwen3-VL", "8 KV heads over 64 layers" 서술 2건 |
| CPU 추론 경로 | inference_smoke CUDA 검사, aw2 README | 없음 (a2:inference_smoke.py:119-123; aw2:README.md:231) |
| 다중 입력 배치 | `prepare_model_inputs`가 batch≠1이면 에러 | 샘플 복제(num_traj_samples)만 지원 (a2:helper.py:96-97) |
| 업스트림 공개 API의 CFG | `ExpertModel`이 config CFG 시 raise; `sample_trajectories_from_data`는 unguided_step_fn 미전달 | 데모/aw2 nav_cfg에서만 우회 구현 (a2:models/expert.py:84-85; aw2:nav_cfg.py:18-25) |
| 벤더링 사본의 CUDA graph 가속 | diff -rq | aw2에는 `diffusion_expert_cuda_graph.py` 없음 |

## 그림 설계안 (층별 박스 목록 + 화살표 목록 + 범례)

캔버스 1500×1000 px, 9개 가로 밴드(아래 L0 → 위 L8), 각 밴드 높이 ~105 px, 좌측 70 px 폭 층 라벨 열. 오른쪽 1/3 영역(x≈1000-1480)은 ROS 2 통합 컬럼으로 L1~L8에 걸쳐 배치해 "업스트림 추론 스택(좌) / Autoware 통합(우)"를 시각적으로 분리.

### 범례 (4종 스타일)

| 스타일 | 의미 |
|---|---|
| 초록 실선 채움 (#76B900 계열) | alpamayo2 저장소 코드 (NVlabs/alpamayo2) |
| 파랑 실선 채움 | alpamayo-autoware 2.0-super 코드 (벤더링된 alpamayo2_super는 초록 박스에 "vendored in aw2" 뱃지) |
| 회색 실선 테두리(흰 채움) | 외부 의존성 (HW, OS, 라이브러리, HF 체크포인트, Autoware) |
| 회색 점선 테두리 + 옅은 글자 | 코드에 없음 (not present) |
| 굵은 실선 화살표 | 메인 추론 데이터 흐름 |
| 가는 점선 화살표 | 선택/실험 경로 (2-GPU CFG, nav CFG) |

### 박스 목록 (29개)

| # | 층 | 라벨 (≤30자) | 서브라벨 (파일/클래스) | 스타일 |
|---|---|---|---|---|
| B1 | L0 | NVIDIA GPU (CUDA, bf16) | cuda:0 기본 · 80GB+ (문서) | 외부 |
| B2 | L0 | 2nd GPU (optional) | cuda:1 expert, two_gpu_nav_cfg_demo.py | 외부 |
| B3 | L0 | Jetson/DRIVE Thor (aarch64) | 코드 없음 | 부재(점선) |
| B4 | L1 | Linux + CUDA 12.8 / Driver | nvcc 12.x (flash-attn build) | 외부 |
| B5 | L1 | Python 3.12 · uv venv | pyproject.toml / uv.lock | 외부 |
| B6 | L1 | ROS 2 Humble · Py3.10 | + Autoware workspace (msgs) | 외부 |
| B7 | L1 | Docker image | 없음 | 부재(점선) |
| B8 | L2 | torch 2.8 · transformers 4.57.1 | AutoModel/generate/DynamicCache | 외부 |
| B9 | L2 | flash-attn 2.8.3 / SDPA | aw2는 sdpa 강제(Blackwell) | 외부 |
| B10 | L2 | hydra · einops · av · physical-ai-av | hyu.instantiate | 외부 |
| B11 | L2 | TensorRT / Edge-LLM / quant | Alpamayo 2 미지원 | 부재(점선) |
| B12 | L3 | HF checkpoint (~72GB bf16) | nvidia/Alpamayo2-Super, safetensors | 외부 |
| B13 | L3 | Alpamayo2SuperConfig + loader | config.py · from_pretrained(device_map) | 초록 |
| B14 | L4 | Tokenizer + traj tokens | build_alpamayo2_super_tokenizer, <i0..3999> | 초록 |
| B15 | L4 | DeltaTrajectoryTokenizer | models/delta_tokenizer.py (history 48 tok) | 초록 |
| B16 | L4 | VLM backbone (32B, vision+LLM) | self.vlm = transformers[vlm_class] | 외부(HF 클래스)+초록 테두리 래퍼 표시 |
| B17 | L4 | Action Expert (2B) | ExpertModel · PerWaypointActionInProjV2 | 초록 |
| B18 | L4 | FlowMatching + Unicycle AS | flow_matching.py · unicycle_accel_curvature.py | 초록 |
| B19 | L5 | Input profiles (6 cam×4 fr) | input_profiles.py · constants.py | 초록 |
| B20 | L5 | Chat template / Processor | conversation.py · helper.py | 초록 |
| B21 | L5 | Output parsing | token_utils.py · text_tasks.py | 초록 |
| B22 | L6 | sample_trajectories_from_data | alpamayo2_super.py:273 (prefill→CoC→10 Euler) | 초록 |
| B23 | L6 | generate_text (text tasks) | text_tasks.py:353 | 초록 |
| B24 | L6 | nav CFG sampler (optional) | two_gpu_nav_cfg_demo.py / aw2 nav_cfg.py | 초록+파랑 분할, 점선 테두리 아님(존재) |
| B25 | L7 | Alpamayo2RosNode | alpamayo2_node.py (timer 2.0s, 1 worker) | 파랑 |
| B26 | L7 | conversions / nav_text | conversions.py · nav_text.py (lanelet2) | 파랑 |
| B27 | L7 | Autoware sensing/localization | CompressedImage×6 · Odometry · Route | 외부 |
| B28 | L8 | CLI · Notebooks · Viz API | inference_smoke.py · notebooks/*.ipynb · viz_utils.py | 초록 |
| B29 | L8 | RViz / ROS topics | Trajectory · MarkerArray · reasoning(String) | 파랑(발행)+외부(RViz) |

(선택 추가 1개 가능, 30개 한도: B30 L8 "Autoware planning closed-loop" / "README: not usable closed-loop" / 부재 점선)

배치 힌트: 좌측 컬럼(x 90-980)에 B1-B5, B7-B24, B28; 우측 컬럼(x 1000-1480)에 B6, B25-B27, B29(B30). B16은 L4에서 가장 넓게(≈300 px), B17·B18을 오른쪽에 붙여 "KV cache" 화살표가 짧게 보이도록.

### 화살표 목록

메인(굵은 실선):
1. B12 → B13 "weights / config.json"
2. B13 → B16, B13 → B17 "instantiate (hydra, bf16, cuda:0)"
3. B19 → B20 "6×4 frames, ego history 16"
4. B20 → B14 → B15 "input_ids + traj pad → <i*> tokens"
5. B20 → B22 "tokenized_data (pixel_values, input_ids)"
6. B22 → B16 "prefill + CoC decode (top_p 0.98, T 0.6)"
7. B16 → B17 "KV cache (prefix+CoC), MRoPE pos"
8. B17 ↔ B18 "v(x,t) ×10 Euler → accel/curvature"
9. B18 → B21 "pred_xyz 64×3, pred_rot 64×3×3 (0.1s)"
10. B16 → B21 "CoC / meta-action / JSON / bbox text"
11. B21 → B28 "PNG + JSON, minADE"
12. B27 → B25 "CompressedImage×6, Odometry"
13. B25 → B26 "ego history (t0 local), checks"
14. B25 → B20 "GPU JPEG decode → processor(device=cuda)" (aw2 경로가 업스트림 B20/B22 재사용함을 표시)
15. B22 → B25 "pred_xyz/rot, extra.cot"
16. B26 → B29 "Trajectory(base_link, stamp=t0), MarkerArray, String"
17. 수직 스택 의존(가는 회색 실선, 라벨 없음): B8/B9 → B1, B5 → B4, B6 → B4

선택(가는 점선):
18. B23 → B16 "VLM generate only (meta/auto-label/VQA/grounding)"
19. B24 → B17 "guided + unguided caches, w=3.0 (ckpt)"
20. B27(Route) → B26 → B24 "lanelet2 → 'Turn left in 30m'"
21. B24 → B2 "expert on cuda:1 (demo)"
22. B11 ⇢ B22, B3 ⇢ B1, B30 ⇠ B29: 점선 회색 "not present"

각주(그림 하단 1줄): "VLM 층/헤드 수는 체크포인트 config.json에서 로드(코드 미기재); '32B Qwen3-VL, 8 KV heads×64 layers'는 alpamayo-autoware 주석 기재, 'Cosmos 3'는 NVIDIA 문서 기재. 기준 커밋 a2 6d05b9f / aw2 b8747df."
