# Alpamayo 활용에 필요한 SW·HW 정리 — 목적별 요구사항

- 작성일: 2026-07-15 · 출처 접근일 동일 · 자매 문서: [alpamayo_1_vs_2_비교보고서.md](alpamayo_1_vs_2_비교보고서.md) · 발췌 기록: [reference/references.md](reference/references.md)
- 전제: **범용 기준** — 공식 문서의 최소/권장 사양 그대로, 특정 보유 장비 가정 없음
- 검증 등급: ✅ 교차검증 / 🔍 원문 직접 확인(2026-07-15) / 📄 발췌 확보 / 🎥 영상 발언만
- ⚠️ Alpamayo 2 Super는 미공개(여름 예정)라 아래는 전부 **1.5(현행 공개판) 기준**. 2 Super 공개 시 갱신 필요.

---

## 0. 한눈 요약

| 목적 | 최소 HW 한 줄 | 핵심 SW | 난이도 체감 |
|---|---|---|---|
| ① 추론 체험 | NVIDIA GPU **24GB VRAM** 1장 + 디스크 ~30GB | uv + PyTorch + HF gated 승인 | 낮음 — 노트북 따라하기 |
| ② 파인튜닝(SFT) | 다GPU 권장(수치 미공표 — recipe별 README 확인 필요) | alpamayo-recipes (HF Trainer + DeepSpeed) | 중간 |
| ③ closed-loop RL | **GPU 2장(각 ≥40–50GB)** 스모크 / 실전은 노드 단위 + 씬 데이터 ~1.5TB | AlpaGym = AlpaSim + Cosmos-RL(GRPO) | 높음 — 분산 인프라 |
| ④ 차량 배포 | 타깃: DRIVE AGX Thor (Blackwell, 2,000 FP4 TFLOPS) | quantization recipe(FP8/NVFP4) + distillation(공식 recipe 미출시) | 높음 — 파트너 트랙 |

공통 관문: **Hugging Face gated 승인 2건** — 모델 가중치([Alpamayo-1.5-10B](https://huggingface.co/nvidia/Alpamayo-1.5-10B))와 데이터셋([PhysicalAI-Autonomous-Vehicles](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles)) 모두 계정+약관 동의 필요. (🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) · [데이터셋 카드](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles))

라이선스 요약: 추론·시뮬·RL **코드는 전부 Apache 2.0**, **모델 가중치는 non-commercial**(상업은 별도 요청), **데이터셋은 NVIDIA AV Dataset License**(AV 용도 한정, 상업 사용 가능하되 재배포·감시용 금지). (🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) · [alpasim](https://github.com/NVlabs/alpasim) · [alpagym](https://github.com/NVlabs/alpagym) · [데이터셋 카드](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles))

---

## 1. 공통 준비물 (모든 단계)

| 항목 | 내용 | 근거 |
|---|---|---|
| OS/드라이버 | Linux + CUDA Toolkit **12.x** (nvcc 포함) | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |
| Python | **3.12** | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |
| 패키지 관리 | **uv** (`uv venv` → `uv sync`) — Alpamayo/AlpaSim/AlpaGym 공통 | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) · [alpagym](https://github.com/NVlabs/alpagym) |
| 계정 | HF 계정 + `hf auth login` + gated 승인(모델·데이터셋 각각) | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |
| 컨테이너 | Docker (AlpaSim/AlpaGym 서비스 실행) | 🔍 [alpasim](https://github.com/NVlabs/alpasim) 📄 |
| 참고 | flash-attention 빌드 실패 시 `attn_implementation="sdpa"` 대체 가능 | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |

---

## 2. ① 추론 체험 — "모델이 뭘 하는지 눈으로 확인"

### SW
- repo: [NVlabs/alpamayo1.5](https://github.com/NVlabs/alpamayo1.5) (Apache 2.0). 테스트 스크립트 `src/alpamayo1_5/test_inference.py` — 예제 데이터+가중치(**22GB**) 자동 다운로드. (🔍)
- 노트북 4종: 표준 추론 / **navigation guidance** / 멀티카메라 변형 / **VQA**. (🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5))
- 구모델(Alpamayo 1)은 [NVlabs/alpamayo](https://github.com/NVlabs/alpamayo) — 단 navigation 입력·RL 미적용 구버전이므로 신규 시작은 1.5 권장(공식도 1.5 권장 🔍).

### HW (공식 수치, H100 80GB에서 테스트됨)
| 작업 | VRAM | 근거 |
|---|---|---|
| 단일 샘플 추론 | **~24 GB** | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |
| 16샘플 배치 추론 | ~40 GB | 🔍 동일 |
| 16샘플 + CFG(navigation 증폭) | ~60 GB | 🔍 동일 |
| 디스크 | 가중치 22GB + 예제 데이터 → 여유 ~30GB+ | 🔍 동일 |

해석: RTX 3090/4090(24GB)로 단일 샘플 데모 가능(Alpamayo 1 repo가 명시한 최소선과 일치 — "≥24 GB VRAM (e.g., RTX 3090, RTX 4090, A5000, H100)" 🔍 [GitHub alpamayo](https://github.com/NVlabs/alpamayo)). 배치·CFG 실험은 40GB+급(A100/H100/RTX 6000 계열) 필요.

### 절차 요약
1. HF에서 모델·데이터셋 gated 접근 신청 → 2. `uv` 환경 구성(CUDA 12.x, Python 3.12) → 3. `hf auth login` → 4. `test_inference.py` 실행 → 5. 노트북으로 CoC·navigation·VQA 확인.

---

## 3. ② 파인튜닝(SFT) — "내 데이터로 적응"

### SW
- repo: [NVlabs/alpamayo-recipes](https://github.com/NVlabs/alpamayo-recipes) — recipe 4계열 (🔍):
  - `recipes/alpamayo1_sft/` — Alpamayo 1 SFT (**HuggingFace Trainer + DeepSpeed**)
  - `recipes/alpamayo1_5_sft/` — Alpamayo 1.5 SFT (동일 스택)
  - `recipes/alpamayo1_x_rl/` — 1/1.5 RL post-training (**Cosmos-RL / GRPO**) → §4
  - `recipes/alpamayo1_5_quant/` — quantization → §5
- 유틸: 1↔1.5 체크포인트 변환, PAI 데이터셋 서브셋 큐레이션 도구. (🔍)
- 커스텀 데이터: Physical AI 데이터셋과 유사한 포맷으로 변환 후 데이터 로더 참고 — 공식 권장 방식. (🎥 [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0), 문서 표현은 recipes README 참조)

### 데이터
- 기준 데이터셋: [nvidia/PhysicalAI-Autonomous-Vehicles](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles) — 1,700시간 / 306,152클립(20초) / **전체 133TB** / 25개국·2,500+도시. 서브셋 큐레이션 도구로 일부만 받는 것이 현실적. (🔍 데이터셋 카드)
- 자체 reasoning 라벨 제작: 공개된 reasoning auto-labeling 파이프라인 활용(플랫폼 구성요소 📄 [HF 런치 블로그](https://huggingface.co/blog/drmapavone/nvidia-alpamayo)). 2 Super 공개 시 auto-labeling 모델 겸용 예정(🔍 [보도자료](https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis)).

### HW
- **공식 총괄 수치 미공표** — recipes 메인 README는 개별 recipe README로 위임. (🔍 [recipes](https://github.com/NVlabs/alpamayo-recipes)) DeepSpeed 채택 자체가 다GPU 전제 신호. 최소 참고선: 10B 모델은 추론만 24GB, **학습은 단일 GPU에 안 들어감**(AlpaGym 문서 "10B 학습은 GPU 1장 불가, 2장 스모크" 📄 [AlpaGym 블로그](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/)). → **미확인: SFT 정확 GPU 수/VRAM은 개별 recipe README에서 확인 필요.**

---

## 4. ③ closed-loop RL 학습 — "시뮬레이터 안에서 자기 행동으로 배우기"

### SW 스택 (3층 구조)
| 층 | 컴포넌트 | 역할 | 근거 |
|---|---|---|---|
| 환경 | [AlpaSim](https://github.com/NVlabs/alpasim) (Apache 2.0) | closed-loop 시뮬레이터. **gRPC 마이크로서비스**(Driver/Renderer/TrafficSim/Controller/Physics 분리, GPU별 배치 가능). 렌더러: **NuRec**(기본) + **OmniDreams/FlashDreams**(생성형, 동적 객체 충실도↑). Python 94.5%+Rust 4%(가속 모듈), Docker Compose(로컬)/Slurm(멀티노드) | 🔍 [alpasim](https://github.com/NVlabs/alpasim) · 📄 [developer blog](https://developer.nvidia.com/blog/building-autonomous-vehicles-that-reason-with-nvidia-alpamayo/) |
| 하네스 | [AlpaGym](https://github.com/NVlabs/alpagym) (Apache 2.0) | 패키지 4개: `host`(CLI·config·AlpaSim 셋업) / `runtime`(GPU 컨테이너, rollout+추론) / `policies`(정책 구현) / `alpasim_configs`(시뮬 토폴로지). 리워드 교체형(`reward=progress_safety` 예시) | 🔍 [alpagym](https://github.com/NVlabs/alpagym) |
| 트레이너 | [Cosmos-RL](https://github.com/nvidia-cosmos/cosmos-rl) (코드 Apache 2.0) | 분산 rollout·학습 오케스트레이션. 병렬화: tensor/sequence/context/FSDP/pipeline. FP8 학습·FP8/FP4 rollout 지원. **GRPO** 기본 | 🔍 [cosmos-rl](https://github.com/nvidia-cosmos/cosmos-rl) · [alpagym](https://github.com/NVlabs/alpagym) |

⚠️ 스택 세대 교체 주의: Cosmos-RL repo는 "활발한 개발 종료, 제한 유지보수 — **Cosmos 3로 이동 권장**" 표기. (🔍 [cosmos-rl](https://github.com/nvidia-cosmos/cosmos-rl)) Alpamayo 2 Super(Cosmos 3 백본) 공개 시 RL 스택도 Cosmos 3 계열로 옮겨갈 가능성 — 신규 구축 시 버전 확인 필수.

실행 예 (🔍 [alpagym](https://github.com/NVlabs/alpagym)):
```bash
uv run --no-sync --all-packages python -m alpagym_host.cli \
  experiment=alpamayo_1_5_local_2gpu_smoke \
  policy.model.path="$(pwd)/tmp/checkpoints/alpamayo-1.5-10B_alpagym_ckpt" \
  reward=progress_safety
```

### HW
| 항목 | 수치 | 근거 |
|---|---|---|
| 스모크 테스트 | **GPU 2장** (학습 1 + rollout/시뮬 1) — "tested on 2x 50GB RTX 6000 Ada" | 🔍 [alpagym](https://github.com/NVlabs/alpagym) · 📄 [AlpaGym 블로그](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/) |
| GPU VRAM | **≥40GB 권장** | 📄 [AlpaGym 블로그](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/) |
| 디스크(기본) | 환경+컨테이너+가중치(~21GB) 합쳐 **~100–150GB** | 📄 동일 |
| 씬 데이터 | NuRec 씬당 **~1.5GB**, `public_2601` 전체 **~1.5TB** (공개 씬 ~900개는 [NuRec 데이터셋](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-NuRec)) | 📄 동일 · 📄 [HF 런치 블로그](https://huggingface.co/blog/drmapavone/nvidia-alpamayo) |
| 실전 학습 | 노드 단위 이상, Slurm 배포 지원. 수백 GPU 스케일링은 선형 관계 주장(초기 단계) | 🔍 [alpagym](https://github.com/NVlabs/alpagym) · 🎥 [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0) |
| 지원 모델 | **Alpamayo 1.5 10B만** — 2 Super 미지원 (2026-07-15 기준) | 🔍 [alpagym](https://github.com/NVlabs/alpagym) |

---

## 4B. SW 스택 계층 상세 — "BSP부터 앱까지"

두 스택을 구분해야 한다: **(A) 개발·학습 스택**(워크스테이션/클러스터 — 공개 repo로 전부 사실 확인 가능)과 **(B) 차량 탑재 스택**(NVIDIA DRIVE 계열 — 각 층은 공식 문서로 확인되나, **Alpamayo가 이 스택에 실제로 어떻게 꽂히는지는 NVIDIA가 문서로 공개한 적 없음** → 결합 부분은 추론 표기).

### A. 개발·학습 스택 (사실 기반 — repo 의존성 파일 직접 확인)

![Alpamayo 개발·학습 SW 스택 계층도 — L0 HW부터 L5 앱까지](images/stack_dev_learning.svg)

> 그림: 자체 제작(본 절 근거 기반). 실선 = 공식 repo/문서 직접 확인, 점선 = 추정(근거 병기). 아래 표가 그림의 근거 원본.

| 계층 | 구성요소 | 근거 |
|---|---|---|
| **L5 앱/워크로드** | 추론 노트북 4종·`test_inference.py` / SFT·quant recipe 실행 / AlpaGym experiment CLI / CVPR 챌린지 제출 | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) · [recipes](https://github.com/NVlabs/alpamayo-recipes) · [alpagym](https://github.com/NVlabs/alpagym) |
| **L4 도메인 프레임워크** | `alpamayo1.5`(모델 코드) · `alpamayo-recipes`(SFT/RL/quant) · **AlpaGym** 워크스페이스 5패키지(`host`·`plugins`·`runtime`·`alpasim_configs`·`policies/alpamayo_r1`) · **AlpaSim** 모듈 11종(`driver`·`renderer`(NuRec/OmniDreams)·`trafficsim`·`controller`·`physics`·`eval`·`grpc`·`runtime`·`utils`·`tools`·`wizard` — 전부 옵션 설치형 extras) | 🔍 각 repo pyproject.toml 직접 확인 |
| **L3 ML 프레임워크·라이브러리** | **PyTorch 2.8.0**(CUDA 12.8 wheel 인덱스 고정) · **transformers 4.57.1** · **flash-attn ≥2.8.3**(빌드 실패 시 SDPA 폴백) · accelerate ≥1.12 · **DeepSpeed**(SFT recipe) · **Cosmos-RL**(RL 트레이너, rollout 추론은 **vLLM ≥0.8.5** — `[rl]` extra) · grouped-gemm · einops · hydra-core/colorlog(설정) · av(PyAV, 비디오 디코딩) · pandas/pillow/matplotlib/seaborn · `physical-ai-av==0.2.0`(이름상 PAI-AV 데이터셋 SDK — **역할은 이름 기반 추정**, 패키지 문서 미확인) | 🔍 [1.5 pyproject](https://raw.githubusercontent.com/NVlabs/alpamayo1.5/main/pyproject.toml) · [alpagym pyproject](https://raw.githubusercontent.com/NVlabs/alpagym/main/pyproject.toml) · [cosmos-rl pyproject](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-rl/main/pyproject.toml) · [recipes README](https://github.com/NVlabs/alpamayo-recipes) |
| **L2 런타임·시스템 SW** | Python **3.12**(1.5·AlpaGym 고정, AlpaSim은 3.11–3.12) · **uv ≥0.10**(전 repo 공통) · **Docker**(서비스 컨테이너) · **gRPC**(AlpaSim 서비스 간 통신 — `alpasim_grpc` 패키지 실존) · **NCCL**(분산 통신 — AlpaGym에 `nccl_e2e` 테스트 실존; 영상에서 대용량 rollout 전송용 튜닝 언급 🎥) · **Rust/cargo**(AlpaSim 가속 모듈, 코드베이스 4%) · **Slurm**(멀티노드 — `run-on-slurm` 도구 실존) | 🔍 각 pyproject·README |
| **L1 OS·드라이버** | **Linux x86_64 전용**(AlpaGym이 플랫폼 제약 명시) + NVIDIA 드라이버 + **CUDA Toolkit 12.x**(nvcc 필요) | 🔍 [alpagym pyproject](https://raw.githubusercontent.com/NVlabs/alpagym/main/pyproject.toml) · [1.5 repo](https://github.com/NVlabs/alpamayo1.5) |
| **L0 HW** | GPU(§2·§4 사양) · 디스크(§2·§4) · 다GPU/다노드 시 고속 인터커넥트 — NCCL 병렬 스케일링 전제(🎥 수백 GPU 선형 주장) | §2·§4 참조 |

주목할 사실 2개:
- AlpaGym은 **xformers를 의도적으로 비활성화** — cosmos-rl 의존성 체인과 flash-attn 버전 충돌 회피 목적 명시. 스택 결합이 민감하다는 신호. (🔍 [alpagym pyproject](https://raw.githubusercontent.com/NVlabs/alpagym/main/pyproject.toml))
- AlpaGym 정책 패키지 경로가 `policies/alpamayo_r1` — 1.5 지원도 R1 코드베이스 위에서 돌아감(비교보고서 §의 "R1 코드베이스 기반" 증거와 일치). (🔍 동일)

### B. 차량 탑재 스택 (NVIDIA DRIVE 참조 아키텍처)

⚠️ **주의**: 아래 각 층은 NVIDIA 공식 문서로 확인된 사실. 단 **"Alpamayo distilled 모델이 이 스택의 어느 자리에 어떻게 통합되는지"는 공개 문서 없음** — 최상층 배치는 보도자료 발언(teacher→distill→Thor 탑재 🔍)에서 유추한 것이며 추론임을 명시.

![차량 탑재 참조 스택 — DriveOS(BSP)부터 DRIVE AV(앱)까지, Alpamayo 결합부는 점선(추론)](images/stack_vehicle.svg)

> 그림: 자체 제작(본 절 근거 기반). 실선 = 공식 문서 원문 확인, 점선 = 추론(Alpamayo 통합 위치 미공개). 아래 표가 그림의 근거 원본.

| 계층 | 구성요소 | 근거 |
|---|---|---|
| **앱/AV 스택** | **DRIVE AV software** — "purpose-built for L4 autonomy". Alpamayo 관점: distilled student 모델이 주행 정책으로, meta-action을 소비하는 downstream planner와 결합하는 구조가 **시사됨(추론)** — 보도자료 "downstream AV stack built on Alpamayo", "distilled compact models run on NVIDIA DRIVE AGX Thor" 발언 기반, 실제 통합 아키텍처 미공개 | 🔍 [in-vehicle computing 페이지](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/) · [보도자료 5/31](https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis) |
| **AI 런타임** | DriveOS가 **CUDA·cuDNN·TensorRT** 포함. Alpamayo quant recipe(FP8/NVFP4, Model Optimizer Toolkit)의 산출물이 Thor의 FP4 native 가속과 정합 — **"차량 추론이 TensorRT 계열 런타임"이라는 직접 명시는 없음(추론)**, 근거: DriveOS 구성(사실)+NVFP4 recipe(사실)+Thor FP4 스펙(사실) | 🔍 [DriveOS 페이지](https://developer.nvidia.com/drive/os) · [recipes](https://github.com/NVlabs/alpamayo-recipes) · [Thor 블로그](https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/) |
| **미들웨어** | **DriveWorks SDK** — DriveOS 위 계층. **SAL(Sensor Abstraction Layer)**: "abstraction between physical sensor models and software applications" / 이미지·포인트클라우드 처리 / **동적 캘리브레이션**(런타임 재추정) / **egomotion 모듈**(차량 자세 추적·예측 — Alpamayo 입력의 egomotion 히스토리와 개념적으로 대응, 직접 연결 문서는 없음) | 🔍 [DriveWorks 페이지](https://developer.nvidia.com/drive/driveworks) |
| **OS/BSP** | **DriveOS** — "hypervisor manages resources and provides abstraction between underlying hardware and OS" / 게스트 OS **Linux 또는 QNX** / **NvMedia**: "camera frames are directly loaded into GPU memory" / **NvStreams**: zero-copy 데이터 전송 / 준수: **ASPICE, ISO 26262, ISO/SAE 21434** / DRIVE AGX SDK Developer Program 가입 필요(gated) | 🔍 [DriveOS 페이지](https://developer.nvidia.com/drive/os) |
| **HW 플랫폼** | **DRIVE AGX Thor** 칩(Blackwell, 1,000 INT8 TOPS/2,000 FP4 TFLOPS, ASIL-D 설계) — 플랫폼 단위로는 **DRIVE Hyperion**: "two NVIDIA DRIVE AGX Thor systems-on-a-chip on a single board, the safety-certified NVIDIA DriveOS operating system, and a fully qualified multimodal sensor suite that includes **14 high-definition cameras, nine radars, one lidar, and 12 ultrasonics**" | 🔍 [in-vehicle computing](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/) · [Thor 블로그](https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/) |
| **안전 프레임워크** | **NVIDIA Halos** — PlusAI가 "safety through NVIDIA Halos"로 3축(모델=Alpamayo, HW=Hyperion, 안전=Halos) 중 하나로 명시. Halos 자체 상세는 본 조사 범위 밖(미조사 표기) | 🔍 [PlusAI 발표](https://www.plus.ai/news-and-insights/2026-03-16-nvidia-alpamayo) |

참고 정합성: Hyperion 카메라 14개 ⊃ 데이터셋 카메라 7개 구성(§6) — 데이터셋은 Hyperion 센서 셋의 부분집합 형태로 보이나 **공식 매핑 문서는 없음(추론)**.

### C. 스택에 들어있는 AI 기술 요소 목록

| 기술 | 어디에 | 근거 |
|---|---|---|
| Transformer 기반 VLM 백본 (Cosmos-Reason2 / Cosmos 3 Super Reasoner) | 모델 본체 | 🔍 [1.5 카드](https://huggingface.co/nvidia/Alpamayo-1.5-10B) · [HF 블로그 2](https://huggingface.co/blog/drmapavone/nvidia-alpamayo-2) |
| Diffusion 기반 action decoder + conditional flow matching (Stage 1 학습) | 궤적 생성(action expert 2.3B) | 🔍 [1.5 카드](https://huggingface.co/nvidia/Alpamayo-1.5-10B) · 📄 [arXiv v2](https://arxiv.org/html/2511.00088v2) |
| Chain-of-Causation SFT (구조화 인과 추론 라벨 학습) | Stage 2 | 🔍 [arXiv](https://arxiv.org/abs/2511.00088) |
| GRPO 기반 RL post-training (open-loop→closed-loop) | Stage 3 · AlpaGym | 🔍 [arXiv](https://arxiv.org/abs/2511.00088) · [alpagym](https://github.com/NVlabs/alpagym) |
| FlashAttention (효율 어텐션 커널) | 추론·학습 공통 필수 의존성 | 🔍 [1.5 pyproject](https://raw.githubusercontent.com/NVlabs/alpamayo1.5/main/pyproject.toml) |
| Classifier-Free Guidance (navigation 조건 증폭) | 추론(내비 조건부 궤적) | 🔍 [1.5 repo](https://github.com/NVlabs/alpamayo1.5) VRAM 표 "+CFG" · 🎥 [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0) |
| vLLM (rollout 추론 서빙) | Cosmos-RL `[rl]` extra | 🔍 [cosmos-rl pyproject](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-rl/main/pyproject.toml) |
| PTQ 양자화 FP8 / NVFP4+FP8 혼합 (Model Optimizer Toolkit) | 배포 전 압축 | 🔍 [recipes](https://github.com/NVlabs/alpamayo-recipes) |
| Knowledge distillation (teacher→student) | 차량 배포 경로 (공식 recipe 미출시) | 🔍 [보도자료](https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis) · [PlusAI](https://www.plus.ai/news-and-insights/2026-03-16-nvidia-alpamayo) |
| NuRec 재구성 렌더링 (실주행 데이터→시뮬 씬; 영상에선 3DGS 기법 언급) | AlpaSim 기본 렌더러 | 🔍 [alpasim](https://github.com/NVlabs/alpasim) · 🎥(3DGS 언급) |
| OmniDreams/FlashDreams 생성형(비디오 모델) 렌더링 | AlpaSim 대체 렌더러 | 🔍 [alpasim](https://github.com/NVlabs/alpasim) |
| Speculative decoding·DFlash (추론 가속) | 10Hz reasoning 달성 수단 언급 | 🎥 [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0) · 🔍 [z-lab HF](https://huggingface.co/z-lab/Alpamayo-1.5-10B-DFlash) |
| Adaptive thinking (단순 상황은 reasoning 생략) | 향후/연구 단계 — CVPR highlight 논문 발언 | 🎥 [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0) — 논문 실체 미확인 |

---

## 5. ④ 차량 배포 — "엣지 크기로 줄여 싣기"

### SW 경로
| 수단 | 상태 | 근거 |
|---|---|---|
| **Quantization** | 공식 recipe 존재: `alpamayo1_5_quant` — Model Optimizer Toolkit, **FP8**, **NVFP4+FP8 혼합 정밀도** | 🔍 [recipes](https://github.com/NVlabs/alpamayo-recipes) |
| **Distillation** | 공식 recipe **아직 없음**(recipes 목록에 부재 🔍). "여름 말 릴리스 예정" 발언 🎥 + "single-GPU용 2B distill 스크립트 계획" 📄 [AlpaGym 블로그](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/) | — |
| 추론 가속(참고) | 서드파티 z-lab **DFlash**판([R1](https://huggingface.co/z-lab/Alpamayo-R1-10B-DFlash)·[1.5](https://huggingface.co/z-lab/Alpamayo-1.5-10B-DFlash)) + 영상 언급: speculative decoding, 템플릿화 CoC로 10Hz reasoning 가능 | 🔍 HF · 🎥 |
| 실증 사례 | PlusAI: 10B teacher → **500M student** distill로 트럭 엣지 탑재 ("without requiring a data center on wheels") | 🔍 [PlusAI](https://www.plus.ai/news-and-insights/2026-03-16-nvidia-alpamayo) |

### 타깃 HW: NVIDIA DRIVE AGX Thor
| 항목 | 수치 | 근거 |
|---|---|---|
| 연산 | "Up to **1,000 INT8 TFLOPS; 2,000 FP4 TFLOPS**" (Blackwell GPU) | 🔍 [Thor 개발킷 블로그 2025-09-03](https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/) |
| CPU/메모리 | 14x Arm Neoverse V3AE, LPDDR5X 273GB/s | 🔍 동일 |
| 안전 | ISO 26262 **ASIL-D** + ISO 21434 설계 | 🔍 동일 |
| 개발킷 | [DRIVE AGX 개발자 페이지](https://developer.nvidia.com/drive/agx) — Thor SKU 10(벤치)/SKU 12(차량) | 🔍 |

NVFP4 quantization recipe(위)와 Thor의 FP4 native 가속이 짝을 이루는 구조 — 보도자료의 "distill → DRIVE AGX Thor 탑재" 경로와 일치. (🔍 [보도자료 5/31](https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis))

---

## 6. 데이터셋·센서 스펙 (모델 학습·평가의 물리적 전제)

[nvidia/PhysicalAI-Autonomous-Vehicles](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles) 카드 직접 확인(2026-07-15 🔍):

| 항목 | 수치 |
|---|---|
| 규모 | 1,700시간 / 306,152클립(각 20초) / **133TB** / 25개국·2,500+도시 |
| 카메라 | **7개**: 전방 광각 120° · 전방 망원 30° · 크로스 좌/우 120° · 후방 좌/우 70° · 후방 망원 30° |
| LiDAR | 상단 360° 회전식 1기 — 298,326클립 커버 |
| Radar | 최대 10기 — 160,761클립 커버 |
| 부가 라벨 | egomotion, 캘리브레이션, 기계생성 장애물 라벨, OOD reasoning 라벨 |
| 라이선스 | NVIDIA AV Dataset License — **AV 용도 한정**(상업 가능), 감시·생체인식·재배포 금지, gated |
| 인기 | 최근 한 달 다운로드 207,246회(HF 표기) |

주의: 2026-01 developer blog 수치(1,727h/310,895클립/radar 163,850 📄)와 현재 카드 수치가 소폭 다름 — 데이터셋 버전 갱신 추정(확증 없음). 본 문서는 카드(최신 직접 확인) 기준.

시사점: 데이터셋 카메라 7개 구성은 Alpamayo 2 Super의 360° 인지("7+ 카메라" 영상 발언)와 정합 — 1/1.5는 이 중 전방 4개만 사용했고, 2 Super가 데이터셋의 전체 카메라 셋을 쓰는 방향으로 해석 가능(추정 — 2 Super 입력 스펙 문서 미공개).

---

## 7. 미확인 항목

| 항목 | 상태 |
|---|---|
| SFT recipe별 정확한 GPU 수/VRAM | 개별 recipe README 미확인 — 실행 전 확인 필요 |
| Alpamayo 2 Super 추론/학습 HW 요구 | 모델 미공개. 34B급이므로 1.5(24GB) 대비 대폭 상승 예상(추정) |
| distillation recipe 시점 | "여름 말" 🎥 영상 발언만 |
| AlpaSim 렌더링 GPU 최소 사양 | README에 명시 없음 🔍 |
| Cosmos 3 기반 RL 스택 전환 일정 | Cosmos-RL 이관 권고만 확인, Alpamayo 적용 시점 미공표 |
| 2 Super 라이선스(상업 옵션 여부) | 미발표 — CES 예고("options for commercial usage" 📄)만 |

---

## 8. 레퍼런스 (이 문서 신규 소스)

- [NVlabs/alpamayo1.5](https://github.com/NVlabs/alpamayo1.5) 🔍 · [NVlabs/alpamayo-recipes](https://github.com/NVlabs/alpamayo-recipes) 🔍 · [NVlabs/alpasim](https://github.com/NVlabs/alpasim) 🔍 · [NVlabs/alpagym](https://github.com/NVlabs/alpagym) 🔍
- [nvidia-cosmos/cosmos-rl](https://github.com/nvidia-cosmos/cosmos-rl) 🔍
- [nvidia/PhysicalAI-Autonomous-Vehicles 데이터셋 카드](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles) 🔍 · [PhysicalAI-Autonomous-Vehicles-NuRec](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-NuRec)
- [DRIVE AGX Thor 개발킷 블로그](https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/) 2025-09-03 🔍 · [DRIVE AGX 개발자 페이지](https://developer.nvidia.com/drive/agx) 🔍
- [PlusAI 발표](https://www.plus.ai/news-and-insights/2026-03-16-nvidia-alpamayo) 2026-03-16 🔍
- 의존성 파일(§4B): [alpamayo1.5 pyproject](https://raw.githubusercontent.com/NVlabs/alpamayo1.5/main/pyproject.toml) · [alpagym pyproject](https://raw.githubusercontent.com/NVlabs/alpagym/main/pyproject.toml) · [alpasim pyproject](https://raw.githubusercontent.com/NVlabs/alpasim/main/pyproject.toml) · [cosmos-rl pyproject](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-rl/main/pyproject.toml) — 전부 🔍
- 차량 스택(§4B): [DriveOS](https://developer.nvidia.com/drive/os) 🔍 · [DriveWorks](https://developer.nvidia.com/drive/driveworks) 🔍 · [in-vehicle computing(Hyperion)](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/) 🔍
- 기존 소스(비교보고서와 공유): [AlpaGym 블로그](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/) · [보도자료 5/31](https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis) · [라이브스트림](https://www.youtube.com/watch?v=kJRVwaYwvt0) 등 — [reference/references.md](reference/references.md)
