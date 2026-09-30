# Alpamayo 실행 하드웨어 요약 보고 — 공식 요구 사양과 후보 하드웨어 지원 범위

- 작성일: 2026-09-30 · 상태: 초판
- 범위: NVIDIA가 공식 저장소·모델카드·문서에서 밝힌 요구 사양만 다룬다. 양자화·서드파티 최적화(FP8, NVFP4, W4A8, FlashDrive 등)는 이 문서에서 제외하고 별도 정리한다.
- 근거: NVlabs/alpamayo·alpamayo1.5·alpamayo2 저장소의 README와 코드, Hugging Face 모델카드, TensorRT Edge-LLM 문서, NVIDIA 개발자 포럼, 제조사·유통사 사양·가격 페이지. 문서 끝에 목록만 붙였고 본문에는 출처를 달지 않았다.

---

## 1. 모델별 기본 주행(궤적 + 추론 텍스트) 요구 사양

| 항목 | Alpamayo 1 (R1-10B) | Alpamayo 1.5 (10B) | Alpamayo 2 Super (34B) |
|---|---|---|---|
| 파라미터 | 10B (VLM 8.2B + action expert 2.3B) | 10B (구조 동일) | 34B (VLM 32B + diffusion expert 2B) |
| 가중치 파일 (BF16) | 약 22 GB | 약 22 GB | 약 72 GB |
| 입력 | 카메라 4대 × 4프레임 + 자차 이력 | 카메라 수 가변(기본 4대 × 4프레임) + 내비 텍스트(선택) | 궤적: 카메라 6대 × 4프레임 · VQA: 6대 |
| 출력 | 궤적 64점(6.4 s) + 추론 텍스트 | 같음 + VQA | 궤적 + 추론 + 메타액션 + 자동 라벨 + VQA + 2D grounding |
| 공식 최소 GPU | VRAM 24 GB 이상 (예시: RTX 3090, RTX 4090, A5000, H100). 16 GB는 OOM 경고 | VRAM 24 GB 이상. 16 GB는 OOM 경고 | "34B 모델에 충분한 VRAM". 모델카드 테스트는 H100 80 GB 1장 |
| 공식 테스트 GPU | RTX 3090, A100, H100 | RTX 3090, A100, H100, B200 | H100 80 GB ("다른 아키텍처는 미검증") |
| 1샘플 메모리 (공식) | 24 GB급 (테스트 스크립트가 "GPU 메모리 호환을 위해" 1샘플 고정) | 약 24 GB (H100 측정) | 72,115 MiB ≈ 75.6 GB (H100, 7카메라 × 4프레임, 1샘플, BF16, SDPA, CFG 끔, 10스텝) |
| 내비 CFG | 없음 | 있음 (16샘플 기준 약 60 GB) | 예제 스크립트만. H100 80 GB 2장 (VLM GPU 67 GiB + expert GPU 71 GiB) |
| SW | Python 3.12, PyTorch 2.8, CUDA 12.x, flash-attn(빌드 실패 시 SDPA) | 같음 | Python 3.12, CUDA 12.x + nvcc, flash-attn 빌드 |
| 차량 배포 런타임 | TensorRT Edge-LLM 공식 지원 (FP16 export만) | Edge-LLM 미지원 (이슈 등록 상태) | Edge-LLM 미지원. NVIDIA는 "DRIVE AGX Thor용으로 증류할 교사 모델"로 규정 |

- VQA·메타액션 같은 텍스트 과제는 expert 없이 VLM만 돌므로 궤적 1샘플보다 메모리를 더 쓰지 않는다.
- 학습·폐루프(SFT, RL, AlpaSim)는 이 문서 범위 밖이다.

## 2. 궤적 샘플(패스) 개수별 요구 메모리

| 샘플 수 | Alpamayo 1 | Alpamayo 1.5 | Alpamayo 1.5 + 내비 CFG | Alpamayo 2 Super |
|---|---|---|---|---|
| 1 | 24 GB급 | 약 24 GB | 공표 없음 | 약 75.6 GB (72,115 MiB) |
| 6 (모델 API 기본값, 1·1.5) | 공표 없음 | 공표 없음 | 공표 없음 | — |
| 16 | 공표 없음 | 약 40 GB | 약 60 GB | 공표 없음 |

**1과 16 사이 개수는 되는가.** 된다. 세 모델 모두 `num_traj_samples`는 정수 인자이며, 코드는 이 값을 VLM 텍스트 생성의 `num_return_sequences`와 expert 배치 크기에 그대로 넣는다. 1과 16은 README가 메모리를 실측해 적어 둔 두 지점일 뿐이고, 2~15나 16 초과도 인자로 넣으면 그대로 동작한다. 기본값을 보면 모델 API는 6, 테스트 스크립트는 1(메모리 호환 목적), 2 Super는 1이다.

**중간 값의 메모리는 어떻게 보나.** 샘플이 늘면 가중치(약 22 GB)는 그대로이고 KV 캐시·추론 텍스트·expert 활성값만 샘플 수에 비례해 늘어난다. 1.5의 두 측정점(1샘플 24 GB, 16샘플 40 GB)을 선형으로 이으면 샘플당 약 1.07 GB다. 이 추정으로 6샘플은 약 29 GB, 8샘플은 약 31.5 GB다. 공식 수치가 아니므로 실제 장비에서 확인이 필요하다.

**두 가지 주의.** ① 1.5는 CUDA graph 옵션을 켤 때 `max_batch_size`를 `batch × num_traj_samples × num_traj_sets` 이상으로 잡아야 하고, 이 버퍼가 메모리를 더 쓴다. ② 내비 CFG는 unguided KV 캐시를 하나 더 만들어 16샘플 기준 +20 GB가 붙는다.

## 3. 후보 하드웨어별 지원 범위

읽는 법: ✔ 공식 테스트 GPU이거나 공개 실행 사례 있음 · ○ 메모리·세대 조건은 충족하나 공개 실측 없음 · △ 경계선·미해결 문제 있음 · ✖ 불가 · 메모리 판정 기준은 2절 공식 수치(1샘플 24 GB / 16샘플 40 GB / 16샘플+CFG 60 GB / 2 Super 1샘플 75.6 GB / 2 Super CFG는 공식 데모가 GPU 2장). 통합 메모리 보드는 OS·CPU와 메모리를 나눠 쓰므로 표기 용량보다 가용치가 작다.

| 하드웨어 | GPU 메모리 · 대역폭 · 세대 | 1 / 1.5 1샘플 | 1.5 16샘플 | 1.5 16샘플 + CFG | 2 Super 1샘플 | 2 Super 내비 CFG | 공식 런타임 지원 | 공개 실행 사례 | 가격 (2026-09) |
|---|---|---|---|---|---|---|---|---|---|
| **DRIVE AGX Thor 개발킷** | 64 GB 통합 · 273 GB/s · Blackwell | △ | △ | ✖ | ✖ | ✖ | Edge-LLM 공식 (DriveOS 7.2, R1 FP16) | R1 FP16 엔진 빌드가 CUDA 가용 메모리 부족(6 GB 보고, 15 GB 요청)으로 실패한 포럼 보고 2건, 미해결 | 비공개. DRIVE 개발자 프로그램 경유 |
| **Jetson AGX Thor 개발킷 (T5000)** | 128 GB 통합 · 273 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ✖ (공식 데모 2장) | Edge-LLM 공식 (JetPack 7.x, R1 FP16 튜토리얼) | 1.5 BF16을 PyTorch+SDPA로 실행한 포럼 사례 | $3,499 (2025-08) → $5,499 (2026-07 인상) |
| **Jetson T4000 모듈** | 64 GB 통합 · 273 GB/s · Blackwell | ○ | ○ | △ | ✖ | ✖ | Edge-LLM 공식 (Jetson Thor 계열) | 없음 | 모듈 $2,999 (1천 개 단가). NVIDIA 개발킷 없음, 파트너 캐리어 |
| **Jetson AGX Orin 64GB** | 64 GB 통합 · 204.8 GB/s · Ampere | ○ | ○ | △ | ✖ | ✖ | Edge-LLM 공식 (JetPack 7.2, FP16만) · JetPack 6.2용 PyTorch 2.8 휠 제공 | 없음 (포럼에 요구사양 질문만) | 개발킷 $1,999 → $3,499 (2026-07). 모듈 $2,999 |
| **DRIVE AGX Orin 개발킷** | Orin-X · Ampere (메모리 용량 공식 표기 미확인) | ✖ | ✖ | ✖ | ✖ | ✖ | 없음. DriveOS 6 = CUDA 11.4, PyTorch 미지원, Edge-LLM 미지원 | 없음 | $7,500 (Arrow) |
| **Jetson Orin NX 16GB / Nano 8GB** | 16 / 8 GB 통합 · Ampere | ✖ | ✖ | ✖ | ✖ | ✖ | — | — | $399~ |
| **DGX Spark (GB10)** | 128 GB 통합 · 273 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ✖ (공식 데모 2장) | Edge-LLM 공식 | Alpamayo 1(6샘플) 실행·지연 분석 논문 | $3,999 → $4,699 (2026-02). 파트너 $4,100~ |
| **RTX 5090** | 32 GB · 1,792 GB/s · Blackwell | ✔ | ✖ | ✖ | ✖ | ✖ | x86 개발용 (Edge-LLM "Developer" 등급) | Alpamayo 1 실행 논문 (1.03 s) | MSRP $1,999 → 시세 약 $4,300~5,000 |
| **RTX 4090** | 24 GB · 1,008 GB/s · Ada | ✔ (README 예시 GPU) | ✖ | ✖ | ✖ | ✖ | x86 개발용 | — | 단종. 중고 $2,500~3,000 |
| **RTX 3090** | 24 GB · 936 GB/s · Ampere | ✔ (공식 테스트 GPU) | ✖ | ✖ | ✖ | ✖ | x86 개발용 | — | 단종. 중고 $1,050~1,400 |
| **RTX 5080 / 5070 Ti / 4080 Super** | 16 GB | ✖ (README OOM 명시) | ✖ | ✖ | ✖ | ✖ | — | — | $1,050~1,600 |
| **RTX PRO 6000 Blackwell** | 96 GB · 1,792 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ✖ (공식 데모 2장) | x86 개발용 | 1.5·2 Super ROS 2 노드 실행 사례 (TIER IV) | MSRP $16,000 (2026-08). 시세 $14,000~18,000 |
| **RTX PRO 5000 72 GB** | 72 GB · 1,344 GB/s · Blackwell | ○ | ○ | ○ | ✖ (75.6 GB > 72 GB) | ✖ | x86 개발용 | 없음 | 공식가 미발표, 추정 $5,000~6,300 |
| **RTX PRO 5000 48 GB / RTX 6000 Ada / L40S / RTX A6000** | 48 GB | ○ | ○ | ✖ | ✖ | ✖ | x86 개발용 | AlpaGym 스모크(RTX 6000 Ada 2장) | $4,300~7,600 (A6000 중고 $2,600~5,000) |
| **A100 80 GB** | 80 GB HBM2e · Ampere | ✔ (공식 테스트 GPU) | ○ | ○ | ○ (메모리 충족, 아키텍처 미검증) | ✖ (1장) / ○ (2장) | x86 개발용 | — | 신품 $7,000~15,000. 임대 $1.1~1.6/h |
| **H100 80 GB** | 80 GB HBM3 · Hopper | ✔ (1.5 측정 GPU) | ✔ | ✔ | ✔ (모델카드 테스트 GPU) | ✔ (2장, 공식 데모) | x86 개발용 | 공식 측정 환경 | $25,000~30,000. 임대 $2~4/h |
| **H200 141 GB** | 141 GB HBM3e · Hopper | ✔ | ○ | ○ | ○ | ✖ 공식 데모 기준 2장 (합 138 GB는 1장에 경계선) | x86 개발용 | — | $30,000~40,000. 임대 $4.5~6/h |

### 한 줄 판정

- **DRIVE AGX Thor**: 공식 배포 타깃이지만 개발킷에서는 CUDA 가용 메모리 문제로 R1 FP16 엔진조차 아직 못 만든 상태. 2 Super는 64 GB에 안 들어간다.
- **Thor보다 더 되는 것**: Jetson AGX Thor·DGX Spark(128 GB)는 2 Super 1샘플까지 메모리상 들어간다. 단, 세 보드 모두 Thor와 같은 273 GB/s라 속도는 데스크톱 GPU보다 훨씬 느리다.
- **가장 싸게 1·1.5 1샘플을 확인**: 중고 RTX 3090/4090(24 GB). 16샘플·CFG는 40·60 GB가 필요해 48 GB 이상 카드로 올라가야 한다.
- **2 Super를 한 장으로**: 80 GB 이상(H100, A100, RTX PRO 6000). 72 GB 카드는 모델카드 피크(75.6 GB)에 못 미친다.
- **2 Super 내비 CFG**: 공식 경로는 80 GB GPU 2장뿐이다.
- **비NVIDIA·DRIVE Orin·16 GB급**: 공식 코드가 CUDA·PyTorch 2.8·flash-attn에 묶여 있어 후보가 아니다.

---

## 근거 자료 (검증에 사용, 본문 미표기)

- NVlabs/alpamayo README·`models/alpamayo_r1.py`·`test_inference.py` — 최소 VRAM 24 GB, 테스트 GPU, `num_traj_samples` 기본값 6/1, `num_return_sequences` 전달
- NVlabs/alpamayo1.5 README·`models/alpamayo1_5.py`·`nav_utils.py` — 1/16샘플·CFG 메모리, 테스트 GPU, CUDA graph `max_batch_size` 규칙
- NVlabs/alpamayo2 README·`models/alpamayo2_super.py`·`inference_smoke.py` — 34B 구성, 2-GPU CFG 데모 67/71 GiB, 기본 샘플 1
- Hugging Face nvidia/Alpamayo2-Super 모델카드 — H100 80 GB, 72,115 MiB, 측정 조건(7카메라·4프레임·1샘플·BF16·SDPA·CFG 끔·10스텝)
- NVIDIA/TensorRT-Edge-LLM 문서 support-matrix·supported-models·examples/vla/alpamayo.md, 이슈 #130 — 플랫폼별 공식 지원, Alpamayo R1 FP16 전용, 1.5 미지원
- NVIDIA 개발자 포럼 — DRIVE AGX Thor R1 엔진 OOM(382500·382501), Jetson Thor 1.5 네이티브 빌드(382647), 저장소 이슈 NVlabs/alpamayo #69
- arXiv 2605.08975(DGX Spark에서 Alpamayo 1 지연 분석), arXiv 2605.11678(RTX 5090 1.03 s), autowarefoundation/alpamayo-autoware(RTX PRO 6000 실행), NVlabs/alpagym·alpasim 문서
- 사양·가격: NVIDIA DRIVE AGX Thor 플랫폼 문서·Jetson Thor/Orin 제품 페이지, DGX Spark 제품 페이지, Arrow(DRIVE AGX Orin $7,500), 2026-07 Jetson 가격 인상 보도(CNX Software·VideoCardz), Tom's Hardware(RTX PRO 6000 $16,000·DGX Spark $4,699), GPU 시세 추적 사이트(videocardprices·bestvaluegpu·getpcparts), 클라우드 가격표(Lambda·RunPod·AWS)
