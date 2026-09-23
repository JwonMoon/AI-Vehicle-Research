# Alpamayo 코드 대조 노트

기준 (클론일 2026-09-15, depth 1, LFS 미수신):

| 디렉터리 | 저장소 | ref | 커밋 SHA | 커밋 날짜 |
|---|---|---|---|---|
| alpamayo | NVlabs/alpamayo | main | 11a0e01c13a5622377c45ee37d653351453ec43b | 2026-09-09 |
| alpamayo1.5 | NVlabs/alpamayo1.5 | main | 36aeb4c5938cbc2eb2aed33b22434773da4ab639 | 2026-09-09 |
| alpamayo2 | NVlabs/alpamayo2 | main | 6d05b9f2dcaa6ee45ac6e053cf18653eac23c047 | 2026-09-09 |
| alpamayo-recipes | NVlabs/alpamayo-recipes | main | 670b551987280979c157c1cb70b042458dbacc99 | 2026-09-08 |
| alpamayo-autoware_1.5 | autowarefoundation/alpamayo-autoware | alpamayo1.5 | 65eda63b70460fc806a3dd1c619475e1d3bdbe28 | 2026-04-23 |
| alpamayo-autoware_2.0-super | autowarefoundation/alpamayo-autoware | alpamayo2.0-super | b8747df228afd0e0d40d10fcfebd7b827325d50b | 2026-08-06 |
| alpamayo-autoware_main | autowarefoundation/alpamayo-autoware | main | 4e1c3874a0d58c48369592d5ee6dad9e2ea14a01 | 2026-03-23 |
| TensorRT-Edge-LLM | NVIDIA/TensorRT-Edge-LLM | v0.10.1 | e8b29522938901f6df19ebeedd4b69bc8edbcd97 | 2026-09-03 |

약칭: `A1`=alpamayo@11a0e01, `A15`=alpamayo1.5@36aeb4c, `A2`=alpamayo2@6d05b9f, `REC`=alpamayo-recipes@670b551, `AW15`=alpamayo-autoware@alpamayo1.5(65eda63), `AW2S`=alpamayo-autoware@alpamayo2.0-super(b8747df), `AWM`=alpamayo-autoware@main(4e1c387), `EDGE`=TensorRT-Edge-LLM@v0.10.1(e8b2952).
보고서 약칭: `TD`=thor-deployment.md, `DD`=ad-sw-stack-deep-dive.md, `ART`=article.md.
`(web)` 표시는 저장소 밖 HF `config.json`을 WebFetch(요약 모델 경유)로 본 것 — 2차 근거로 취급.

## 요약

판정별 개수 (대조표 72행, 행별 주 판정 기준. "일치(보강)"은 일치로 셈):
- 일치: 52
- 수정 필요: 10 (#7, 15, 17, 20, 29, 46, 48, 49, 51, 64)
- 코드와 반대: 1 (#14)
- 코드로 확인 불가: 9 (#1, 8, 28, 43, 52, 53, 60, 68, 70)

가장 중요한 수정 5개
1. **레시피 출력은 기본값이 fake quantization이 아니다 (코드와 반대).** `quantize.py`는 기본으로 `mtq.compress()`를 불러 실제 FP8/NVFP4 가중치로 저장한다. Q/DQ만 넣고 원본 가중치를 유지하는 체크포인트는 `--fake_quant`를 줘야 나온다. (TD 2.0, 2.3)
2. **R1 저장소 요구 버전은 "이상"이 아니라 고정이다.** `torch==2.8.0`, `transformers==4.57.1`, `requires-python==3.12.*`, `flash-attn>=2.8.3`. (TD 2.1)
3. **입력 이력 표현 오류.** 카메라 프레임 4장은 t0−0.3 s…t0로 폭이 0.3 s다. 자차 운동 이력은 별도로 16스텝(1.6 s @10 Hz), xyz와 3×3 회전이다. DD 2.2.5의 "0.4 s 이력 @10 Hz, 자차 운동"은 두 입력을 섞어 쓴 표현이다. (TD 2.1, DD 2.2.5)
4. **1.5 ROS 노드 성능표에서 README의 한 행이 빠졌다.** 빠진 행은 "GPU preproc + greedy + TRT expert + 5-step = 0.660 s / 1.52 FPS / ~1.8%"다. 행 순서도 README와 다르다. (TD 2.5)
5. **백본 표기 보강.** 코드상 R1과 1.5의 VLM 클래스는 `Qwen3VLForConditionalGeneration`이고 기본값은 `Qwen/Qwen3-VL-8B-Instruct`다. 1.5의 HF config는 `nvidia/Cosmos-Reason2-8B`를 가리킨다(web). 2 Super VLM은 `qwen3_vl_text` 계열로 64 layers, hidden 5120이다(web). AW2S README는 "32B Qwen3-VL backbone + 2B flow-matching expert"라고 적는다. "Cosmos 3 Super Reasoner"라는 이름은 코드에 없다. 공식 문서 표기는 "Cosmos 3 backbone"이다. 1.5 KV 캐시 가정(36 layers / KV head 8 / head_dim 128)은 Qwen3-VL-8B config로 해소된다(web). 따라서 ⚠️를 떼고 근거를 달 수 있다.

## 대조표

| # | 보고서 | 위치 | 주장 요지 | 판정 | 코드 근거 | 수정 문안 |
|---|---|---|---|---|---|---|
| 1 | TD | 결론 1 | NVIDIA 직원 "not available for AGX Thor"; Edge-LLM은 Alpamayo 1 FP16만 | 코드로 확인 불가(포럼) / 후반부 일치 | `EDGE:docs/source/user_guide/examples/vla/alpamayo.md:48` "Only FP16 is supported for Alpamayo export" | 포럼 인용은 유지. 뒤에 "Edge-LLM v0.10.1 문서도 FP16만 명시"를 덧붙일 수 있음 |
| 2 | TD | 결론 2 / 2.2 / 4.2 | 공식 온보드 경로는 Edge-LLM, 대상은 R1-10B, FP16뿐 | 일치 | `EDGE:docs/.../supported-models.md:214` "Alpamayo: nvidia/Alpamayo-R1-10B"만 있음; `EDGE:experimental/builder/models/registry.py:540-554` `"alpamayo_r1"` 한 종류 | — |
| 3 | TD | 결론 2 / 2.2 / 2.7 | 1.5 지원은 요청 단계 | 일치(코드상 미지원) | `EDGE:tensorrt_edgellm/checkpoint/checkpoint_utils.py:260` `if root.get("model_type") == "alpamayo_r1"`; `A15:src/alpamayo1_5/config.py:26` `model_type = "alpamayo1_5"`; EDGE 전체에 alpamayo1_5/alpamayo2 문자열 없음 | "v0.10.1 코드에는 `alpamayo_r1` model_type만 분기되어 1.5·2 Super 경로가 없다" 추가 가능 |
| 4 | TD | 결론 6 | Autoware 노드 추론 주기 기본값 0.1 s | 일치(1.5·main 노드) / 보강 | `AW15:src/alpamayo_ros/alpamayo_ros/alpamayo_node.py:60` `declare_parameter("inference_period_sec", 0.1)`; `AW2S:.../alpamayo2_node.py:84` `("inference_period_sec", 2.0)` | "1.5 노드 0.1 s, 2 Super 노드 2.0 s" |
| 5 | TD | 1.3 표 | Jetson Thor JP7.0/7.1+CUDA13.0, JP7.2+CUDA13.2(기기에서 빌드); DRIVE Thor DriveOS 7.2+CUDA13.3(SDK 컨테이너) | 일치 | `EDGE:docs/.../support-matrix.md:15-17` | — |
| 6 | TD | 1.3 | DriveOS 7.0.3(CUDA 12.8)에서는 빌드 안 됨 | 일치(간접) | 같은 표에 DriveOS는 7.2만 있음 (`support-matrix.md:17,43`) | — |
| 7 | TD | 1.3 / 2.3 | FP8·NVFP4는 Blackwell 계열에서만 | 수정 필요 | `EDGE:docs/.../supported-models.md:24` "MXFP8 and FP4/NVFP4 require Blackwell-class hardware"; `:18` Orin은 FP8·FP4 불가 | "MXFP8·NVFP4는 Blackwell급 필요, FP8은 Orin에서 불가"로 정정 |
| 8 | TD | 1.3 | Edge-LLM 최신 릴리스 0.10.1 | 코드로 확인 불가 | 핀은 v0.10.1 태그(2026-09-03). 이후 릴리스 여부는 저장소로 판단 불가 | — |
| 9 | TD | 2.0 | R1은 Alpamayo 1의 원래 이름 | 일치 | `A1:README.md:30` "Alpamayo-R1 has been renamed to Alpamayo 1" | — |
| 10 | TD | 2.0 | 제품명 "Alpamayo 1 Nano", "1.5 Nano" | 일치 | `REC:README.md:104-105` | — |
| 11 | TD | 2.0 / 2.1 | 가중치 22.2 GB(R1·1.5), 약 71.6 GB(2 Super), BF16 | 일치 | `A1:README.md:94`·`A15:README.md:83` "model weights (22 GB)"; `AW2S:src/alpamayo2_super/UPSTREAM.md` "~71.6 GB, bf16, 32 files"; `A1:src/alpamayo_r1/test_inference.py:35` `dtype=torch.bfloat16` | — |
| 12 | TD | 2.0 / 2.2 / 2.7 | Edge-LLM에서 Alpamayo는 FP16 원본 방식만 지원 | 일치 | `EDGE:.../vla/alpamayo.md:48`; `EDGE:tensorrt_edgellm/onnx/export_encoder.py:514` `dtype: torch.dtype = torch.float16` | — |
| 13 | TD | 2.0 / 2.3 | 레시피로 1.5를 양자화하면 FP8 약 11 GB, AutoQuant 약 9 GB | 일치 | `REC:recipes/alpamayo1_5_quant/README.md:16-20` "FP8 ~11 GB", "Autoquant 6.5BPE ~9 GB" | — |
| 14 | TD | 2.0 / 2.3 | 레시피 출력은 downstream SDK용 "fake quantization"(Q/DQ) 체크포인트 | **코드와 반대** | `REC:recipes/alpamayo1_5_quant/quantize.py:253-258` `--fake_quant` "By default the model is compressed with mtq.compress() so the saved weights are real FP8/NVFP4"; `:323-327` `if not args.fake_quant: mtq.compress(model)` | "기본 출력은 `mtq.compress()`로 압축한 실제 FP8/NVFP4 가중치다. `--fake_quant`를 주면 원본 가중치에 Q/DQ만 배치한 TensorRT 등 downstream용 체크포인트가 된다" |
| 15 | TD | 2.1 | R1 구성 Cosmos-Reason 8.2B + action expert 2.3B | 수정 필요(보강) | `REC:README.md:154` "Cosmos-Reason backbone (8.2B) with a diffusion-based action expert (2.3B)" 문서는 일치. 그러나 코드 `A1:src/alpamayo_r1/models/base_model.py:207` `vlm_name_or_path: str = "Qwen/Qwen3-VL-8B-Instruct"`, `:381` `Qwen3VLForConditionalGeneration`; HF config `vlm_backend: "qwenvl3"`(web) | "Cosmos-Reason 8.2B(코드상 Qwen3-VL-8B 아키텍처) + flow-matching action expert 2.3B" |
| 16 | TD | 2.1 | 1.5 구성 Cosmos-Reason2 8.2B + expert 2.3B | 일치(보강 가능) | HF `Alpamayo-1.5-10B/config.json` `vlm_name_or_path: "nvidia/Cosmos-Reason2-8B"`(web); expert = VLM text config 복제 후 덮어씀 `A15:src/alpamayo1_5/models/alpamayo1_5.py:101-105`; expert_cfg hidden 2048 / inter 8256 / heads 16 / head_dim 128(web) → 36층 기준 약 2.28B(계산) | "(계산: expert 36층×약 63M ≈ 2.3B)" 병기 가능 |
| 17 | TD | 2.1 / DD 2.2.5 | 2 Super = Cosmos 3 Super Reasoner 32B + expert 2.3B | 수정 필요 | `A2:README.md:13` "32B VLM backbone with a 2B diffusion expert"; `REC:README.md:106,113` "Cosmos 3 backbone"; `AW2S:README.md:208` "32B Qwen3-VL backbone + 2B flow-matching action expert"; VLM 클래스는 config의 `vlm_class`로 동적 결정 `A2:src/alpamayo2_super/models/alpamayo2_super.py:122-123`; HF config text `model_type: qwen3_vl_text`, 64 layers, hidden 5120, KV 8(web) | "Cosmos 3 기반 32B VLM(Qwen3-VL 계열 아키텍처, 64층) + 약 2B(모델카드 2.3B) flow-matching expert". "Super Reasoner"라는 명칭은 출처를 따로 확인할 것 |
| 18 | TD | 2.1 | R1 카메라 4대 | 일치 | `A1:src/alpamayo_r1/load_physical_aiavdataset.py:52` "If None, uses 4 cameras" | — |
| 19 | TD | 2.1 | 1080×1920을 320×576으로 | 일치(간접) | `A1:src/alpamayo_r1/helper.py:23-24` `MIN_PIXELS = 163840`, `MAX_PIXELS = 196608` (320×576=184,320이 이 범위 안, 32의 배수); 1080×1920 원본은 `AW15:README.md:51` | "코드상 프레임당 163,840~196,608 px로 리사이즈" 병기 권장 |
| 20 | TD | 2.1 | 카메라당 4프레임(0.4 s @10 Hz) | 수정 필요 | `A1:.../load_physical_aiavdataset.py:164` "if num_frames=4, load at [t0-0.3s, t0-0.2s, t0-0.1s, t0]" | "카메라당 4프레임(t0−0.3 s~t0, 10 Hz 간격)" |
| 21 | TD | 2.1 | 1.5 카메라 수 가변, 내비게이션 명령 | 일치 | `A15:README.md:207,209`; `notebooks/inference_nav.ipynb`, `inference_cam_num.ipynb` | — |
| 22 | TD | 2.1 | 2 Super 6대 검증, 카메라당 과거 4프레임 | 일치 | `A2:src/alpamayo2_super/input_profiles.py:36-51` `camera_ids=(0,1,2,3,5,6)`(궤적), VQA는 `(0,1,2,3,4,5)`, `frame_indices=(0,1,2,3)` | "궤적 과제는 ID (0,1,2,3,5,6), VQA는 (0–5)" 추가 가능 |
| 23 | TD | 2.1 | 출력 64 waypoints / 6.4 s | 일치 | `A1:src/alpamayo_r1/action_space/unicycle_accel_curvature.py:50` `n_waypoints: int = 64`; `load_physical_aiavdataset.py:50` "64 for 6.4s at 10Hz"; `A1:README.md:138` | — |
| 24 | TD | 2.1 | R1 출력에 인과 추론 텍스트 | 일치 | `A1:src/alpamayo_r1/test_inference.py:66` `extra["cot"]` | — |
| 25 | TD | 2.1 | 1.5 = 같음 + QA | 일치 | `A15:README.md:104` `generate_text` for VQA | — |
| 26 | TD | 2.1 | 2 Super 출력 궤적+추론+메타액션+VQA+2D grounding+자동 라벨 | 일치 | `A2:src/alpamayo2_super/text_tasks.py:39` `TextTask = Literal["meta_action", "auto_labeling", "vqa"]`; `input_profiles.py:50` `"grounding"`; `A2:README.md:256-263` | — |
| 27 | TD | 2.1 / 4.3 | R1·1.5 24 GB+ VRAM, H100에서 테스트 | 일치 | `A1:README.md:50,174` "≥24 GB… Tested RTX 3090, A100, and H100"; `A15:README.md:37` "~24 GB" | 1.5 "16샘플 ~40 GB, CFG ~60 GB"(`A15:README.md:38-39`) 추가 가능 |
| 28 | TD | 2.1 | 2 Super H100 80 GB, 피크 72,115 MiB | 코드로 확인 불가 | 저장소에는 없음(모델카드 수치). 2-GPU 데모 피크 67/71 GiB(`A2:README.md:222-223`), AW2S 노드 69.1 GiB만 있음 | — |
| 29 | TD | 2.1 | R1 저장소 요구는 PyTorch 2.8 이상, transformers 4.57.1 이상 | 수정 필요 | `A1:pyproject.toml` `requires-python = "==3.12.*"`, `"torch==2.8.0"`, `"transformers==4.57.1"`, `"flash-attn>=2.8.3"` | "Python 3.12, torch==2.8.0, transformers==4.57.1 고정, flash-attn≥2.8.3" |
| 30 | TD | 2.1 | 2 Super 저장소는 Python 3.12와 flash-attn 빌드 전제 | 일치 | `A2:pyproject.toml` `requires-python = "==3.12.*"`, `flash-attn>=2.8.3`; `A2:README.md:40` "CUDA Toolkit 12.x with nvcc; flash-attn builds during installation" | — |
| 31 | TD | 2.2 | 2 Super NVFP4는 변환·실행 도구 없음 | 일치 | 레시피 양자화는 1.5 전용 `REC:recipes/alpamayo1_5_quant/quantize.py:228` `default="nvidia/Alpamayo-1.5-10B"`; EDGE에 alpamayo2 없음 | — |
| 32 | TD | 2.2 | R1 Jetson Thor: Edge-LLM 공식 경로 | 일치 | `EDGE:.../vla/alpamayo.md:57,91` "Build Engines (Thor Device)", "Run Inference (Thor Device)" | — |
| 33 | TD | 2.3 | student 가중치·distillation 레시피 없음 | 일치 | `REC:README.md:73-78` 레시피는 SFT×2, RL, 1.5 quant뿐. "distill"은 목적 설명(`:58`)과 2 Super 소개(`:126`)에만 등장 | — |
| 34 | TD | 2.3 | 레시피: 1·1.5 SFT, RL(GRPO), 1.5 양자화(ModelOpt); distillation·ONNX export·TensorRT 변환·Thor 지침 없음 | 일치 | `REC:README.md:75-78`; `grep -ri "onnx\|jetson\|thor"` 결과는 README 설명과 `utils.py:30` `torch.ops.tensorrt.quantize_op`(ModelOpt Q/DQ 연산자 확인용)뿐 | — |
| 35 | TD | 2.3 | 양자화 환경 RTX 5090+CUDA 12 / B300+CUDA 13, PyTorch 2.8.0, ModelOpt 0.43.0 | 일치 | `REC:recipes/alpamayo1_5_quant/README.md:9-12`; `pyproject.toml` `"nvidia-modelopt==0.43.0"`, `"torch==2.8.0"` | — |
| 36 | TD | 2.3 | AutoQuant 6.5 bit | 일치(보강) | README 예시 `--auto_quantize_bits=6.5`(`README.md:142`), 코드 기본값은 `default=4.8`(`quantize.py:240-244`) | "6.5 bit는 README 예시값(기본값 4.8)" |
| 37 | TD | 2.8 | 보정 클립 100개 | 일치 | `quantize.py:251` `--num_of_calib_clips … default=100`; 보정 알고리즘 기본 `max`(`:246`) | — |
| 38 | TD | 2.3 | 워크플로 HF → ONNX → TRT 엔진 → C++ 런타임 | 일치 | `EDGE:.../vla/alpamayo.md:27-43`(export), `:57-85`(llm_build/visual_build/action_build), `:175` `action_inference` | — |
| 39 | TD | 2.3 | "must be built on the device" | 일치(간접) | `EDGE:support-matrix.md:15-17` Jetson Build location "Device", DRIVE "SDK container" | DRIVE는 SDK 컨테이너 빌드임을 병기 |
| 40 | TD | 2.3 | action expert는 별도 엔진, `max_kv_cache_capacity`가 LLM 엔진 값과 같아야 | 일치 | `EDGE:docs/source/developer_guide/customization/customization-guide.md:68,72-73`; `EDGE:.../vla/alpamayo.md:48,81`; `export_encoder.py:512` "Fixed KV cache capacity (must match LLM engine)" | — |
| 41 | TD | 2.3 | 1.5 넣으면 `KeyError: 'hidden_size'` | 일치(원인 정황) | 1.5는 `model_type="alpamayo1_5"`라 `checkpoint_utils.py:257-261`의 VLM config 승격 분기를 타지 않음. 루트 config에는 hidden_size가 없음(web) | "원인: v0.10.1은 `alpamayo_r1`만 VLM text config를 승격" 추가 가능 |
| 42 | TD | 2.3 | student 후보 Cosmos-Reason2 2B/8B 등 | 일치(부분 확인) | `EDGE:supported-models.md:122` Cosmos-Reason2-2B/8B | 나머지 모델 목록은 대조하지 않음 |
| 43 | TD | 2.4 | R1 99 ms, flow-matching 5스텝 | 코드로 확인 불가(논문) / 참고 | 코드 기본 스텝은 10 `A1:src/alpamayo_r1/diffusion/flow_matching.py:36` `num_inference_steps: int = 10` | "코드 기본값은 10스텝(논문 측정은 5스텝)" 병기 권장 |
| 44 | TD | 2.4 | 1.5 ROS 노드: GPU 전처리 + TRT INT8 expert + 5스텝 0.600 s | 일치 | `AW15:README.md:70`; INT8 근거 `AW15:scripts/build_trt_expert_engine.py:156-171` `quantize_expert_denoiser_int8`, `enable_int8=True, enable_fp16=True`. README 다이어그램(`:21`)은 "TRT FP16"으로 적혀 서로 다름 | "TRT expert(INT8 QDQ + FP16 혼합, ONNX Runtime TensorRT EP)" |
| 45 | TD | 2.4 / 2.5 / 3.8 | 2 Super 노드 평균 3.35 s / p90 3.97 s, 피크 69.1 GiB, 로딩 28.6 s, "not usable closed-loop" | 일치 | `AW2S:README.md:282-286` | median 3.29 s, max 6.24 s, 304회 측정 추가 가능 |
| 46 | TD | 2.5 | 1.5 노드 성능표 5행 | 수정 필요 | `AW15:README.md:63-70` 6행. 누락 행 "GPU preproc + greedy + TRT expert + 5-step \| 0.660s \| 1.52 \| ~1.8%". README 순서는 native 10 → native 5 → TRT 10 → TRT 5 → Full | 누락 행 추가, 순서 README대로 |
| 47 | TD | 2.5 | 조건: RTX PRO 6000 96 GB, 카메라 4대×4프레임, 1080×1920 | 일치 | `AW15:README.md:51` | "rate=0.5, max_generation_length=16, 120 s warmup" 조건 병기 권장 |
| 48 | TD | 2.5 | H100 80 GB×2 공식 데모: VLM GPU 0, expert GPU 1 | 수정 필요(표현) | `A2:README.md:196-200` "VLM generation on cuda:0, then expert denoising plus guided/unguided KV caches on cuda:1. This is an advanced demo, not the default public API"; `A2:examples/two_gpu_nav_cfg_demo.py:21-22`; 기본 CLI는 단일 GPU `inference_smoke.py:133` `device_map="cuda:0"` | "내비게이션 CFG용 고급 2-GPU 데모(기본 경로는 단일 GPU), 피크 VLM GPU 약 67 GiB / expert GPU 약 71 GiB" |
| 49 | TD | 2.5 | R1 24 GB+ GPU(3090·3090 Ti·4090·A5000) 호환 | 수정 필요(경미) | `A1:README.md:50` "RTX 3090, RTX 4090, A5000, H100" — 3090 Ti는 저장소에 없음(모델카드 표기일 수 있음) | 출처가 모델카드면 유지, 저장소 기준이면 3090 Ti 삭제 |
| 50 | TD | 2.6 | R1/1.5 10.5B (8.2B+2.3B) | 일치(계산) | expert 파라미터 계산: q/o 2048² ×2, k/v 2048×1024 ×2, MLP 3×2048×8256 → 층당 약 63M × 36층 ≈ 2.28B | — |
| 51 | TD | 2.6 | 1.5 KV 가정 36 layers, KV head 8, head_dim 128은 원문 미확인 | 수정 필요(해소) | 코드 기본 VLM `A15:src/alpamayo1_5/models/base_model.py:211` `Qwen/Qwen3-VL-8B-Instruct`; Qwen3-VL-8B text_config: num_hidden_layers 36, num_key_value_heads 8, head_dim 128, hidden 4096(web); 1.5 HF config vlm=Cosmos-Reason2-8B(web). 토큰 수 가정도 `EDGE:.../vla/alpamayo.md:69,78` `--maxInputLen 3424`, `--maxImageTokensPerImage 192`(16장×192=3,072)와 부합 | "백본(Qwen3-VL-8B 구조: 36층, KV head 8, head_dim 128)은 HF config로 확인" — ⚠️ 제거. 0.44 GB 계산은 그대로 유효 |
| 52 | TD | 2.7 | flash-attn 2.8.3에 SM 110(Thor) 없음 → SDPA 대체 | 코드로 확인 불가(부분 방증) | 저장소에는 SM110 언급 없음. 방증 `AW2S:README.md:236-237` "flash-attn 2.8.3 ships no sm_120 (Blackwell) kernels". SDPA 대체 경로는 존재 `A15:README.md:167-182` | — |
| 53 | TD | 2.7 | PyTorch 휠 ABI 문제로 소스 빌드 | 코드로 확인 불가 | 포럼 사례 | — |
| 54 | TD | 2.8 | flash-attn 생략, `attn_implementation='sdpa'` 지정 | 일치(가능함 확인) | `A15:README.md:170-182`; `A15:src/alpamayo1_5/models/base_model.py:225-227` 기본 `flash_attention_2`, 인자로 덮어쓰기 가능 | — |
| 55 | TD | 3.8 | 1.5 브랜치: 24 GB+ VRAM, Humble, Python 3.10, TRT expert 엔진은 Py3.12 venv | 일치 | `AW15:README.md:76-78,128`; `AW15:scripts/requirements-trt-build.txt` 머리말 "calibration step requires physical_ai_av which needs Python >= 3.11"; `AW15:pyproject.toml` `requires-python = ">=3.10"` | — |
| 56 | TD | 3.8 | 2.0-super: 80 GB+ VRAM, TensorRT 미사용 | 일치 | `AW2S:README.md:223,230` | — |
| 57 | TD | 3.8 | 입력 토픽 CompressedImage 4개, `/localization/kinematic_state`, `/planning/mission_planning/route` | 일치(보강) | `AW15:.../alpamayo_node.py:58-59,151-152,167,186` (CompressedImage, Odometry, LaneletRoute). 카메라 수는 `camera_topics` 파라미터로 가변이고 README 예시가 4개. 2 Super 노드는 정확히 6개 강제 `AW2S:.../alpamayo2_node.py:307-310` | "1.5 노드는 예시 4대(가변), 2 Super 노드는 ID [0,1,2,3,5,6] 6대 고정" |
| 58 | TD | 3.8 | 출력 `/alpamayo/predicted_trajectory`(Autoware Trajectory), `/alpamayo/reasoning` 등 | 일치 | `AW15:.../alpamayo_node.py:54-57`; `AW15:README.md:186-190` (+`reasoning_stamped`, `nav_text`, `_markers`) | — |
| 59 | TD | 3.8 | 세 README 어디에도 Thor/Jetson/aarch64/Jazzy 언급 없음 | 일치(README 한정) / 보강 | README에는 없음. 코드 주석에는 Jazzy가 있음 `AW15:.../alpamayo_node.py:62`, `AWM:.../alpamayo_node.py:58`, `AW2S:.../alpamayo2_node.py:86` "ROS 2 Jazzy: non-empty defaults so … array parameter types are inferred" | "README에는 없으나, 노드 코드에 Jazzy 파라미터 호환 주석이 있다(Jazzy 포팅 부담이 일부 줄었을 가능성)" |
| 60 | TD | 3.8 | 브랜치 `alpamayo1.0`, `alpamayo1.5`, `alpamayo2.0-super`, `main` | 코드로 확인 불가(부분) | alpamayo1.0은 클론하지 않음. 나머지 3개는 PINS에 있음 | — |
| 61 | TD | 4.1 / 4.3 | x86 기준선 RTX PRO 6000 약 0.6~0.7 s, 24 GB+, 2 Super 노드 80 GB+ | 일치 | `AW15:README.md:68-70`; `AW2S:README.md:230` | — |
| 62 | DD | 1.6 | R1 구조 = Cosmos-Reason VLM + diffusion(flow-matching) 궤적 디코더 | 일치(보강) | `A1:src/alpamayo_r1/diffusion/flow_matching.py`(FlowMatching, Euler — HF config `int_method: euler`(web)); VLM 클래스 Qwen3-VL(#15) | "(코드상 VLM은 Qwen3-VL-8B 아키텍처)" 병기 가능 |
| 63 | DD | 1.6 / 2.2.5 표 | 2 Super 34B; GitHub "34B = 32B + 2B" | 일치 | `A2:README.md:5,12-13` | — |
| 64 | DD | 2.2.5 R1 행 | 입력: 카메라 4대, 0.4 s 이력 @10 Hz, 자차 운동, 텍스트 | 수정 필요 | 이미지 4프레임 t0−0.3~t0 `A1:load_physical_aiavdataset.py:164`; 자차 이력 `num_history_steps: int = 16` "1.6s at 10Hz" `:32,49`; `ego_history_xyz (…,16,3)`, `ego_history_rot (…,16,3,3)` `:61-62` | "카메라 4대×4프레임(0.3 s 구간), 자차 이력 16포인트(1.6 s @10 Hz, 위치+회전), 텍스트" |
| 65 | DD | 2.2.5 R1 행 | 출력 6.4 s 궤적(64점) + 인과 추론 텍스트 | 일치 | #23, #24 | — |
| 66 | DD | 2.2.5 1.5 행 | Cosmos-Reason2 + diffusion 디코더, RL 후학습, 카메라 가변, 내비, 궤적+추론 또는 VQA | 일치 | `A15:README.md:102-104,206-209`; `A15:src/alpamayo1_5/diffusion/flow_matching.py` | — |
| 67 | DD | 2.2.5 2 Super 행 | 카메라 6대, 4프레임; 출력 궤적+추론+메타액션+2D grounding+자동 라벨 | 일치(누락 보강) | #22, #26 — VQA가 출력 목록에서 빠짐 | 출력에 "VQA" 추가 |
| 68 | DD | 2.2.5 2 Super 행 | "상업 이용 가능" | 코드로 확인 불가 / 상충 | `A2:README.md:378` 가중치 OpenMDW-1.1(상업 조건 명시 없음); `AW2S:README.md:379` "Model weights: Non-commercial license" | TD 라이선스 상충 표에 AW2S README 표기 추가 권장 |
| 69 | DD | 2.2.5 | Recipes는 1.5용 "FP8 and NVFP4 + FP8 Mixed Precision" 제공 | 일치(보강) | `REC:README.md:78`; 코드 선택지 `quantize.py:238` `choices=["fp8", "nvfp4", "w4a8_nvfp4_fp8", "auto"]` | "포맷 선택지: fp8 / nvfp4 / w4a8_nvfp4_fp8 / auto" |
| 70 | DD / ART | 2.2.5, 5.1, ART | 99 ms 중 70 ms 디코딩, FlashDrive 717→151 ms, "not available for AGX Thor", "months to days", "cloud-to-car" | 코드로 확인 불가 | 논문·포럼·블로그 수치 | — |
| 71 | ART | 1문단 | Alpamayo 10B → 34B | 일치 | `REC:README.md:102-106` | — |
| 72 | ART | 라벨링 | 2 Super 추론 자동 라벨 | 일치(기능 존재) | `A2:notebooks/autolabeling.ipynb`; `text_tasks.py:56` `"auto_labeling": ["cot_auto_labeling"]` | "months to days" 효과는 확인 불가 |

(집계는 요약 절 참조: 일치 52 / 수정 필요 10 / 코드와 반대 1 / 코드로 확인 불가 9.)

## 코드에서 새로 확인한 사실

| # | 사실 | 근거 |
|---|---|---|
| 1 | R1·1.5의 VLM은 `Qwen3VLForConditionalGeneration`, 기본 `vlm_name_or_path="Qwen/Qwen3-VL-8B-Instruct"`. 전처리 processor는 Qwen3-VL-2B-Instruct를 쓰고, 프레임당 163,840~196,608 px | `A1:src/alpamayo_r1/models/base_model.py:207,381`; `A1:src/alpamayo_r1/helper.py:23-25`; `A15:.../base_model.py:211` |
| 2 | action expert는 VLM text config를 복제해 hidden 2048 / inter 8256 / heads 16으로 덮어쓴 Transformer(층 수는 VLM과 동일). VLM KV 캐시를 소비함. 2 Super expert는 hidden 1536 / inter 6144(web) | `A15:src/alpamayo1_5/models/alpamayo1_5.py:101-112`; HF configs(web) |
| 3 | 1.5는 VLM이 flash_attention_2여도 expert는 강제로 sdpa("The diffusion expert does not support FlashAttention 2") | `A15:src/alpamayo1_5/models/alpamayo1_5.py:106-109` |
| 4 | Flow matching 기본 추론 스텝은 R1·1.5·2 Super 모두 10(Euler). AW15 노드 기본 5, AW2S 노드 기본 10 | `A1:.../flow_matching.py:36`; `A15:.../flow_matching.py:35`; `A2:.../flow_matching.py:32`; `AW15:.../alpamayo_node.py:75`; `AW2S:.../alpamayo2_node.py:98` |
| 5 | Edge-LLM Alpamayo 런타임 I/O: 입력 궤적은 `[x,y,z]` 16점, 출력 `output_trajectory`는 (accel, kappa) 쌍(웨이포인트 좌표 아님). 예시 빌드값 maxInputLen 3424, maxKVCacheCapacity 4096, maxImageTokensPerImage 192, maxBatchSize 6 | `EDGE:docs/.../vla/alpamayo.md:21-23,65-84,182` |
| 6 | Edge-LLM은 Alpamayo에 speculative decoding을 거부. Alpamayo-1 지원은 0.7.1에서 추가됨 | `EDGE:experimental/builder/models/alpamayo/configuration.py:88-91`; `EDGE:CHANGELOG.md:86` |
| 7 | Edge-LLM은 R1 root config에 VLM 구조가 없어 `Qwen/Qwen3-VL-8B-Instruct` config를 HF에서 받아 승격(오프라인 환경이면 `vlm_config.json` 필요) | `EDGE:tensorrt_edgellm/checkpoint/checkpoint_utils.py:168-199`; `EDGE:experimental/builder/models/alpamayo/configuration.py:22,53-59` |
| 8 | AW15 TRT expert 경로의 실체: FP32 ONNX export → neural-compressor SmoothQuant(α=0.6) INT8 QDQ → ONNX Runtime `TensorrtExecutionProvider`(int8+fp16). 보정 샘플 기본 8개. 순수 TensorRT API가 아니며, 스크립트 `--model-id` 기본값이 `nvidia/Alpamayo-R1-10B`로 남아 있음 | `AW15:scripts/build_trt_expert_engine.py:68,73,79,156-171`; `AW15:src/alpamayo1_5/trt/expert_runtime.py:46-53`; `AW15:scripts/requirements-trt-build.txt` (`onnxruntime-gpu`, `neural-compressor==3.0`) |
| 9 | 2 Super 노드: 카메라 ID [0,1,2,3,5,6] 오름차순 강제, `inference_period_sec` 2.0, `max_generation_length` 256, `attn_implementation="sdpa"` 고정. 내비 CFG를 켜면 3.35 → 5.2 s, 69.4 → 70.9 GiB | `AW2S:.../alpamayo2_node.py:84,96,307-310,329`; `AW2S:README.md:340` |
| 10 | AW2S는 upstream이 Python 3.12로 고정한 alpamayo2_super를 Python 3.10에서 수정 없이 vendoring해 실행(`load_physical_aiavdataset.py`만 제거) | `AW2S:src/alpamayo2_super/UPSTREAM.md` |
| 11 | 2 Super VLM text config: 64층, KV head 8, head_dim 128, hidden 5120(web). AW2S README도 "8 KV heads over 64 layers", 5k 토큰 캐시 약 1.2 GiB로 적음 | HF `Alpamayo2-Super/config.json`(web); `AW2S:README.md:341-342` |
| 12 | AW2S README는 1.5 노드 궤적을 "20 points / 2.0 s"라고 적지만, 노드 코드는 `pred_xyz[0,0,0]` 전체(`n_waypoints=64`)를 dt 0.1로 발행 — README와 코드가 불일치 | `AW2S:README.md:221`; `AW2S:.../alpamayo_node.py:393-395,438-468`; `AW15:README.md:186` "64-waypoint trajectory" |
| 13 | 1.5 VRAM: 단일 샘플 ~24 GB, 16샘플 ~40 GB, 16샘플+CFG ~60 GB(H100 측정) | `A15:README.md:35-41` |
| 14 | 2 Super 공식 2-GPU 데모는 내비 CFG용 고급 예제. 10스텝, 피크 VLM GPU ~67 GiB / expert GPU ~71 GiB. 모델을 먼저 호스트 메모리에 로드하므로 호스트 RAM도 필요 | `A2:README.md:194-224` |
| 15 | 버전 고정: 추론 저장소와 레시피 모두 torch==2.8.0 / transformers==4.57.1. SFT 레시피는 DeepSpeed 0.18.2(Alpamayo 1), 0.19.1(1.5). 양자화 기본 보정 알고리즘 `max`(smoothquant 선택 가능), AutoQuant 기본 비트 4.8 | `REC:recipes/alpamayo1_sft/pyproject.toml:25`; `REC:recipes/alpamayo1_5_sft/pyproject.toml:25`; `REC:recipes/alpamayo1_5_quant/quantize.py:240-246` |

## 확인 불가 목록

| 항목 | 이유 |
|---|---|
| NVIDIA 직원 포럼 답변("not available for AGX Thor", NIM/TRT-LLM Jetson 미지원) | 포럼 출처, 코드 밖. 참고로 Edge-LLM 문서는 R1 엔진 빌드·추론을 "Thor Device"에서 하도록 안내함 |
| 2 Super H100 피크 72,115 MiB, R1 모델카드 3090 Ti 호환 | HF 모델카드 수치, 저장소에 없음 |
| flash-attn 2.8.3에 SM110 커널 없음 | 저장소에는 sm_120 부재 언급(AW2S README)만 있음 |
| Thor용 PyTorch 휠 ABI 문제, 커뮤니티 절차의 PyTorch 버전 | 포럼 사례 |
| 논문 지연(99/70/29 ms), FlashDrive 수치, Jetson Thor 3,770→943.6 ms | 논문 출처, 코드 무관 |
| Edge-LLM 최신 릴리스가 0.10.1인지 | 태그 핀으로는 이후 릴리스 여부를 판단할 수 없음 |
| `alpamayo1.0` 브랜치 존재·내용 | 클론 대상 아님 |
| "Cosmos 3 Super Reasoner" 명칭, 2 Super "상업 이용 가능" | 코드에는 명칭 없음. 라이선스는 A2(OpenMDW-1.1)와 AW2S README(Non-commercial)가 상충 |
| DRIVE Thor 개발킷 FP16 엔진 빌드 OOM, CUDA 가용 6 GB | 포럼 사례. Edge-LLM `limitations.md:21`에 DriveOS 대형 모델 cudaMallocAsync 이슈와 hugepage 권고만 있음 |
| 2 Super expert 층 수·정확한 파라미터 수 | HF config 요약(web)에서 층 수가 확인되지 않음. 64층 상속 가정 시 약 2.4B(계산) |
