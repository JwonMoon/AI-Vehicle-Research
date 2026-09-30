# Alpamayo 실행 하드웨어 요약 보고 — 공식 요구 사양과 후보 하드웨어 지원 범위

- 작성일: 2026-09-30 · 상태: 5판 (초판~4판 2026-09-30)
- 범위: NVIDIA가 공식 저장소·모델카드·문서에서 밝힌 요구 사양만 다룬다. 양자화·서드파티 최적화(FP8, NVFP4, W4A8, FlashDrive 등)는 별도 문서로 정리한다.
- 표기: 본문에는 출처를 달지 않았다. 검증에 쓴 자료는 6절에 항목별로 나열했다. 원화는 1 USD = 1,360원(2026-09-30 매매기준율 1,358원 반올림)으로 환산했고, 국내 유통가가 확인된 경우 함께 적었다.

---

## 1. 모델별 기본 주행 요구 사양

### 1.1 하드웨어 사양을 정할 때 필요한 항목

| 항목 | Alpamayo 1 (R1-10B) | Alpamayo 1.5 (10B) | Alpamayo 2 Super (34B) |
|---|---|---|---|
| 파라미터 | 10B (VLM 8.2B + action expert 2.3B) | 10B (구조 동일) | 34B (VLM 32B + diffusion expert 2B) |
| 가중치 파일 (BF16) | 약 22 GB | 약 22 GB | 약 72 GB |
| 공식 최소 GPU | VRAM 24 GB 이상. 16 GB는 OOM 경고 | VRAM 24 GB 이상. 16 GB는 OOM 경고 | "34B 모델에 충분한 VRAM". 모델카드 테스트는 H100 80 GB 1장 |
| 공식 테스트 GPU | RTX 3090, A100, H100 (README 예시에 RTX 4090·A5000 포함) | RTX 3090, A100, H100, B200 | H100 80 GB. "다른 GPU 아키텍처는 미검증" |
| 1샘플¹ 메모리 (공식) | 24 GB급 (테스트 스크립트가 "GPU 메모리 호환을 위해" 1샘플 고정) | 약 24 GB (H100 측정) | 72,115 MiB ≈ 75.6 GB (H100, 7카메라 × 4프레임, 1샘플, BF16, SDPA, CFG 끔, 10스텝) |
| 16샘플 메모리 (공식) | 공표 없음 | 약 40 GB (H100 측정) | 공표 없음 |
| 1샘플 + 내비 CFG² | 기능 없음 | 공표 없음 (추정 약 26 GB, 2.3절) | 공표 없음 |
| 16샘플 + 내비 CFG² | 기능 없음 | 약 60 GB (H100 측정) | 공식 예제는 H100 80 GB 2장 (VLM GPU 67 GiB + expert GPU 71 GiB), 1샘플 |
| 샘플 수 기본값 | 모델 API 6, 테스트 스크립트 1 | 모델 API 6, 테스트 스크립트 1, 내비 예제 16 | 1 |
| SW | Python 3.12, PyTorch 2.8, CUDA 12.x, flash-attn (빌드 실패 시 SDPA) | 같음 | Python 3.12, CUDA 12.x + nvcc, flash-attn 빌드 |
| 차량 배포 런타임 (TensorRT Edge-LLM³) | 공식 지원. FP16 export만. 예제 엔진은 최대 배치 6 | 미지원 (지원 요청 이슈 등록 상태) | 미지원. NVIDIA는 "DRIVE AGX Thor용으로 증류할 교사 모델"로 규정 |

### 1.2 주석

¹ **샘플(패스)**: 한 번의 추론에서 모델이 내놓는 후보 궤적의 개수다. 코드 인자 이름은 `num_traj_samples`이며, 후보 궤적마다 추론 텍스트(Chain-of-Causation)도 하나씩 생성된다. "1샘플"은 후보 궤적 하나만 뽑는 가장 가벼운 설정이고, "16샘플"은 후보 16개를 한 번에 뽑아 그중 고르거나 분포를 보는 설정이다.

² **내비 CFG(classifier-free guidance)**: "30 m 앞에서 우회전" 같은 내비게이션 문장을 궤적에 더 강하게 반영하는 방식이다. 내비 문장을 넣은 경우와 뺀 경우를 각각 계산해 그 차이를 증폭하므로, VLM의 KV 캐시가 두 벌 필요해 메모리가 늘어난다.

³ **TensorRT Edge-LLM**: NVIDIA가 Jetson·DRIVE·DGX Spark 같은 엣지 장치용으로 만든 C++ 추론 런타임이다. PyTorch 없이 모델을 ONNX로 내보내고 장치에서 TensorRT 엔진으로 빌드해 돌린다. 차량에 실을 때의 공식 경로이며, 현재 Alpamayo는 1(R1)만, 정밀도는 FP16만 지원한다.

### 1.3 보충 설명

- VQA·메타액션 같은 텍스트 과제는 expert 없이 VLM만 돌므로 궤적 1샘플보다 메모리를 더 쓰지 않는다.
- 통합 메모리 보드(Jetson·DRIVE·DGX Spark)는 CPU·OS와 메모리를 나눠 쓰므로 표기 용량 전체를 GPU가 쓸 수 없다.

## 2. 궤적 샘플(패스) 개수별 요구 메모리

### 2.1 공식 측정값

| 샘플 수 | Alpamayo 1 | Alpamayo 1.5 | Alpamayo 1.5 + 내비 CFG | Alpamayo 2 Super |
|---|---|---|---|---|
| 1 | 24 GB급 | 약 24 GB | 공표 없음 (추정 약 26 GB) | 약 75.6 GB (72,115 MiB) |
| 6 (모델 API 기본값, Edge-LLM 예제 최대 배치) | 공표 없음 | 공표 없음 | 공표 없음 | — |
| 16 | 공표 없음 | 약 40 GB | 약 60 GB | 공표 없음 |

### 2.2 1과 16 사이 개수도 되는가

된다. 세 모델 모두 `num_traj_samples`는 정수 인자이며, 코드는 이 값을 VLM 텍스트 생성의 `num_return_sequences`와 expert 배치 크기에 그대로 넣는다. 1과 16은 README가 메모리를 실측해 적어 둔 두 지점일 뿐이고, 2~15나 16 초과도 인자로 넣으면 그대로 동작한다. Alpamayo 1의 Edge-LLM 예제도 배치 6으로 엔진을 빌드한다.

### 2.3 중간 값의 메모리 추정

샘플이 늘면 가중치(약 22 GB)는 그대로이고 KV 캐시·추론 텍스트·expert 활성값만 샘플 수에 비례해 늘어난다. 1.5의 두 측정점(1샘플 24 GB, 16샘플 40 GB)을 선형으로 이으면 샘플당 약 1.07 GB다.

| 샘플 수 | 1.5 추정 메모리 |
|---|---|
| 4 | 약 27 GB |
| 6 | 약 29 GB |
| 8 | 약 31.5 GB |
| 12 | 약 36 GB |

공식 수치가 아니므로 실제 장비에서 확인이 필요하다. Alpamayo 1은 1.5와 구조가 같아 비슷하게 볼 수 있고, 2 Super는 1샘플 외 공표가 없다.

**1샘플 + 내비 CFG의 추정.** 코드는 내비 문장을 뺀 프롬프트를 한 번 더 prefill해 unguided KV 캐시를 만들고, 이를 샘플 수만큼 복제(`batch_repeat_interleave`)한 뒤 expert를 guided·unguided 두 번 돌린다. 16샘플에서 CFG가 +20 GB(40→60 GB)이므로 샘플당 약 1.25 GB가 CFG 몫이다. 1샘플이면 unguided 캐시 한 벌과 expert 활성값 한 벌만 더해지므로 약 26 GB로 추정한다. 공식 수치는 없으며, 32 GB 이상 GPU를 권장하고 24 GB GPU는 경계선으로 본다.

### 2.4 주의할 점

- 1.5·2 Super는 CUDA graph 옵션을 켤 때 `max_batch_size`를 `batch × num_traj_samples × num_traj_sets` 이상으로 잡아야 하며, 이 정적 버퍼가 메모리를 더 쓴다.
- 내비 CFG는 unguided KV 캐시를 한 벌 더 만들어 16샘플 기준 +20 GB가 붙는다.

## 3. 학습·폐루프 요구 사양 (공식 문서 기준)

| 작업 | 모델 | 공식 하드웨어 조건 | 비고 |
|---|---|---|---|
| SFT (지도 미세조정) | Alpamayo 1 | 8× H100 80 GB에서 검증. DeepSpeed ZeRO-2, `torchrun --nproc_per_node 8` | Stage 1(VLM 전체) → Stage 2(궤적 expert) |
| SFT | Alpamayo 1.5 | 같은 스크립트 계열, 8 GPU 실행 예시 | 내비 조건·VQA(LingoQA) 추가 학습 |
| RL 후처리 (Cosmos-RL, GRPO) | Alpamayo 1 / 1.5 | 로컬 테스트: GPU 5장 이상, 각 80 GB 이상 (정책 4장 FSDP + 롤아웃 1장). 8× H100 노드에서 약 10분(동작 보상), 8× A100 노드에서 약 1.1시간(추론+동작 보상) | 대규모 예시: 80노드 640 GPU (정책 512 + 롤아웃 128) |
| 폐루프 RL (AlpaGym + AlpaSim) | Alpamayo 1.5 | GPU 2장, 각 40 GB 이상 (2× RTX 6000 Ada 50 GB에서 테스트). "10B 모델은 GPU 2장 필요". 디스크 100~150 GB + NuRec 씬당 1.5 GB (전체 1.5 TB) | 1장에서 돌 2B 증류 스크립트는 계획만 공지 |
| 폐루프 평가 (AlpaSim 단독) | Alpamayo 1.5 | FlashDreams 렌더러 + 1.5 단일 카메라 프리셋: 약 96 GB VRAM. 경량 공개 드라이버 프리셋: 약 48 GB | 렌더러와 드라이버를 같은 GPU에 둘 때 |
| 양자화 레시피 | Alpamayo 1.5 | RTX 5090 + CUDA 12 / B300 + CUDA 13에서 테스트 | 내용은 별도 문서 |

- 학습은 모두 x86 서버·워크스테이션 전제이며, 어떤 문서도 Jetson·DRIVE에서의 학습을 다루지 않는다.
- 2 Super의 SFT·RL 레시피는 공개되지 않았다.

## 4. 후보 하드웨어별 지원 범위

### 4.1 비교 항목이 요구하는 것

| 비교 항목 | 필요한 GPU 메모리 | 그 밖의 조건 |
|---|---|---|
| 1 / 1.5 1샘플 | 24 GB 이상 | Ampere 이상, PyTorch 2.8 + CUDA 12.x 동작 |
| 1.5 1샘플 + 내비 CFG | 공식 수치 없음. 추정 약 26 GB (1샘플 24 GB + unguided KV 캐시 + expert 2회). 32 GB 이상 권장, 24 GB는 경계선 | 같음 |
| 1.5 16샘플 | 40 GB 이상 | 같음 |
| 1.5 16샘플 + 내비 CFG | 60 GB 이상 | 같음 |
| 2 Super 1샘플 | 75.6 GB 이상 (실질 80 GB급) | 공식 검증은 H100뿐 |
| 2 Super 내비 CFG | 80 GB GPU 2장 (67 GiB + 71 GiB) | 공식 예제가 2장 수동 배치 |
| 차량 배포 런타임 | Edge-LLM 공식 플랫폼 (Jetson Thor, DRIVE Thor, DGX Spark, Jetson Orin) | Alpamayo 1 FP16만 |

### 4.2 판정 기호

- ✔ 공식 테스트 GPU이거나 공개 실행 사례 있음
- ○ 메모리·세대 조건은 충족하나 공개 실측 없음
- △ 경계선이거나 미해결 문제 있음
- ✖ 불가

### 4.3 지원 범위 표

| 하드웨어 | 분류 | GPU 메모리 · 대역폭 · 세대 | 1 / 1.5 1샘플 | 1.5 1샘플 + CFG | 1.5 16샘플 | 1.5 16샘플 + CFG | 2 Super 1샘플 | 2 Super CFG | Edge-LLM | 공개 실행 사례 | 가격 (원, 2026-09) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **DRIVE AGX Thor 개발킷** | 차량용 SoC 개발킷 | 64 GB 통합 · 273 GB/s · Blackwell | △ | △ | △ | ✖ | ✖ | ✖ | 공식 (DriveOS 7.2) | R1 FP16 엔진 빌드가 CUDA 가용 메모리 부족(6 GB 보고, 15 GB 요청)으로 실패한 포럼 보고 2건, 미해결 | 비공개. DRIVE 개발자 프로그램 경유 |
| **Jetson AGX Thor 개발킷 (T5000)** | 임베디드 개발킷 | 128 GB 통합 · 273 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ○ | ✖ | 공식 (JetPack 7) | 1.5 BF16을 PyTorch + SDPA로 실행한 포럼 사례 | 약 748만 ($5,499, 2026-07 인상). 출시가 약 476만 ($3,499). 국내 유통 540만(VAT 별도) |
| **Jetson T4000 모듈** | 임베디드 모듈 | 64 GB 통합 · 273 GB/s · Blackwell | ○ | ○ | ○ | △ | ✖ | ✖ | 공식 (Jetson Thor 계열) | 없음 | 모듈 약 408만 ($2,999, 1천 개 단가). NVIDIA 개발킷 없음 |
| **Jetson AGX Orin 64GB 개발킷** | 임베디드 개발킷 | 64 GB 통합 · 204.8 GB/s · Ampere | ○ | ○ | ○ | △ | ✖ | ✖ | 공식 (JetPack 7.2, FP16만) | 없음 (포럼에 요구사양 질문만) | 약 476만 ($3,499, 2026-07 인상). 구가 약 272만 ($1,999). 국내 유통 462만(VAT 별도)~560만 |
| **DRIVE AGX Orin 개발킷** | 차량용 SoC 개발킷 | Orin-X · Ampere (메모리 용량 공식 표기 미확인) | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | 없음 (DriveOS 6 = CUDA 11.4, PyTorch 미지원) | 없음 | 약 1,020만 ($7,500, Arrow) |
| **Jetson Orin NX 16GB / Nano 8GB** | 임베디드 모듈·개발킷 | 16 / 8 GB 통합 · Ampere | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | — | — | 약 54만~ ($399~) |
| **DGX Spark (GB10)** | AI 미니 PC | 128 GB 통합 · 273 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ○ | ✖ | 공식 | Alpamayo 1(6샘플) 실행·지연 분석 논문 | 약 639만 ($4,699, 2026-02 인상). 파트너 약 558만~ ($4,100~). 국내 700만~ |
| **RTX 5090** | 데스크톱 GPU | 32 GB · 1,792 GB/s · Blackwell | ✔ | ○ | ✖ | ✖ | ✖ | ✖ | x86 개발용 | Alpamayo 1 실행 논문 (1샘플 1.03 s) | 시세 약 585만~680만 ($4,300~5,000). MSRP 약 272만 ($1,999). 국내 다나와 550만~650만 |
| **RTX 4090** | 데스크톱 GPU | 24 GB · 1,008 GB/s · Ada | ✔ (README 예시 GPU) | △ (24 GB 경계) | ✖ | ✖ | ✖ | ✖ | x86 개발용 | — | 단종. 중고 약 340만~408만 ($2,500~3,000) |
| **RTX 3090** | 데스크톱 GPU | 24 GB · 936 GB/s · Ampere | ✔ (공식 테스트 GPU) | △ (24 GB 경계) | ✖ | ✖ | ✖ | ✖ | x86 개발용 | — | 단종. 중고 약 143만~190만 ($1,050~1,400) |
| **RTX 5080 / 5070 Ti / 4080 Super** | 데스크톱 GPU | 16 GB | ✖ (README OOM 명시) | ✖ | ✖ | ✖ | ✖ | ✖ | — | — | 약 143만~218만 ($1,050~1,600) |
| **RTX PRO 6000 Blackwell** | 워크스테이션 GPU | 96 GB · 1,792 GB/s · Blackwell | ✔ | ○ | ○ | ○ | ○ | ✖ | x86 개발용 | 1.5·2 Super ROS 2 노드 실행 사례 (TIER IV) | MSRP 약 2,176만 ($16,000, 2026-08 인상). 시세 약 1,904만~2,448만 ($14,000~18,000) |
| **RTX PRO 5000 Blackwell 72 GB** | 워크스테이션 GPU | 72 GB · 1,344 GB/s · Blackwell | ○ | ○ | ○ | ○ | ✖ (75.6 GB > 72 GB) | ✖ | x86 개발용 | 없음 | 공식가 미발표. 추정 약 680만~857만 ($5,000~6,300) |
| **RTX PRO 5000 48 GB / RTX 6000 Ada / RTX A6000** | 워크스테이션 GPU | 48 GB | ○ | ○ | ○ | ✖ | ✖ | ✖ | x86 개발용 | AlpaGym 스모크 (RTX 6000 Ada 2장) | 약 585만~952만 ($4,300~7,000). A6000 중고 약 354만~680만 |
| **L40S** | 서버 GPU | 48 GB · 864 GB/s · Ada | ○ | ○ | ○ | ✖ | ✖ | ✖ | x86 개발용 | — | 약 816만~1,034만 ($6,000~7,600). 임대 시간당 약 1,500~2,500원 ($1.1~1.9) |
| **A100 80 GB** | 서버 GPU | 80 GB HBM2e · Ampere | ✔ (공식 테스트 GPU) | ○ | ○ | ○ | ○ (메모리 충족, 아키텍처 미검증) | ✖ 1장 / ○ 2장 | x86 개발용 | — | 신품 약 952만~2,040만 ($7,000~15,000). 임대 시간당 약 1,500~2,200원 ($1.1~1.6) |
| **H100 80 GB** | 서버 GPU | 80 GB HBM3 · Hopper | ✔ (1.5 측정 GPU) | ✔ (16샘플+CFG 측정 GPU) | ✔ | ✔ | ✔ (모델카드 테스트 GPU) | ✔ (2장, 공식 예제) | x86 개발용 | 공식 측정 환경 | 약 3,400만~4,080만 ($25,000~30,000). 임대 시간당 약 2,700~5,400원 ($2~4) |
| **H200 141 GB** | 서버 GPU | 141 GB HBM3e · Hopper | ✔ | ○ | ○ | ○ | ○ | ✖ 공식 예제 기준 2장 (합 138 GB는 1장에 경계선) | x86 개발용 | — | 약 4,080만~5,440만 ($30,000~40,000). 임대 시간당 약 6,100~8,200원 ($4.5~6) |

### 4.4 한 줄 판정

- **DRIVE AGX Thor**: 공식 배포 타깃이지만 개발킷에서는 CUDA 가용 메모리 문제로 R1 FP16 엔진조차 아직 못 만든 상태다. 2 Super는 64 GB에 들어가지 않는다.
- **Thor보다 더 되는 것**: Jetson AGX Thor·DGX Spark(128 GB)는 2 Super 1샘플까지 메모리상 들어간다. 단, 세 보드 모두 Thor와 같은 273 GB/s라 속도는 데스크톱 GPU보다 훨씬 느리다.
- **가장 싸게 1·1.5 1샘플을 확인**: 중고 RTX 3090/4090(24 GB). 1샘플 + CFG는 약 26 GB 추정이라 24 GB 카드는 경계선이고 32 GB(RTX 5090)부터 여유가 있다. 16샘플·CFG는 40·60 GB가 필요해 48 GB 이상 카드로 올라가야 한다.
- **2 Super를 한 장으로**: 80 GB 이상(H100, A100, RTX PRO 6000). 72 GB 카드는 모델카드 피크(75.6 GB)에 못 미친다.
- **2 Super 내비 CFG**: 공식 경로는 80 GB GPU 2장뿐이다.
- **학습·폐루프**: SFT는 8× H100급, RL 로컬 테스트는 80 GB GPU 5장, AlpaGym 스모크는 40 GB GPU 2장이다. 어느 것도 임베디드 보드에서는 하지 않는다.
- **비NVIDIA·DRIVE Orin·16 GB급**: 공식 코드가 CUDA·PyTorch 2.8·flash-attn에 묶여 있어 후보가 아니다.

## 5. 가격 환산 기준

- 환율: 1 USD = 1,360원 (2026-09-30 매매기준율 1,358.34원 반올림). 환산액에는 관세·부가세·유통 마진이 들어 있지 않으므로 국내 실구매가는 더 높다.
- 국내 유통가는 검색으로 확인한 유통사 표시가이며(Jetson AGX Thor·AGX Orin: ICBanq, RTX 5090: 다나와), 2026-07 NVIDIA 인상 전 재고인지 확인하지 못했다.
- 2026년은 메모리 수급난으로 NVIDIA가 Jetson(7월, 최대 101%), RTX PRO 6000(6·8월), DGX Spark(2월) 가격을 올렸고 RTX 5090 소매가는 MSRP의 2배를 넘었다. 구매 시점에 다시 확인해야 한다.

---

## 6. 근거 자료

### 6.1 모델 저장소·모델카드 (요구 사양, 샘플 수, 학습)

| 자료 | URL | 이 문서에서 뒷받침하는 내용 |
|---|---|---|
| NVlabs/alpamayo README | https://github.com/NVlabs/alpamayo | 최소 VRAM 24 GB, 예시 GPU(RTX 3090·4090·A5000·H100), 테스트 GPU(3090·A100·H100), 16 GB OOM 경고, 가중치 22 GB, Python 3.12·flash-attn·SDPA |
| NVlabs/alpamayo `src/alpamayo_r1/models/alpamayo_r1.py` | https://github.com/NVlabs/alpamayo/blob/main/src/alpamayo_r1/models/alpamayo_r1.py | `num_traj_samples: int = 6`, `generation_config.num_return_sequences = num_traj_samples` |
| NVlabs/alpamayo `src/alpamayo_r1/test_inference.py` | https://github.com/NVlabs/alpamayo/blob/main/src/alpamayo_r1/test_inference.py | 테스트 스크립트 `num_traj_samples=1` ("set for GPU memory compatibility") |
| NVlabs/alpamayo1.5 README | https://github.com/NVlabs/alpamayo1.5 | 1샘플 24 GB·16샘플 40 GB·16샘플+CFG 60 GB(H100), 테스트 GPU(3090·A100·H100·B200), CUDA graph `max_batch_size` 규칙, 가변 카메라 |
| NVlabs/alpamayo1.5 `src/alpamayo1_5/models/alpamayo1_5.py` | https://github.com/NVlabs/alpamayo1.5/blob/main/src/alpamayo1_5/models/alpamayo1_5.py | `num_traj_samples: int = 6`, `num_return_sequences` 전달 |
| NVlabs/alpamayo1.5 `src/alpamayo1_5/nav_utils.py`, `notebooks/inference_nav.ipynb` | https://github.com/NVlabs/alpamayo1.5/tree/main/src/alpamayo1_5 · https://github.com/NVlabs/alpamayo1.5/blob/main/notebooks/inference_nav.ipynb | 내비 예제 기본 16샘플, "CFG 추론은 60 GB+ 필요" |
| NVlabs/alpamayo1.5 `src/alpamayo1_5/diffusion/flow_matching.py` | https://github.com/NVlabs/alpamayo1.5/blob/main/src/alpamayo1_5/diffusion/flow_matching.py | CFG가 guided·unguided 두 경로를 따로 계산, `num_inference_steps=10` |
| NVlabs/alpamayo2 README | https://github.com/NVlabs/alpamayo2 | 34B = 32B VLM + 2B expert, CUDA 12.x + nvcc·flash-attn, 2-GPU 내비 CFG 예제(H100 80 GB 2장, 67 GiB + 71 GiB, 1샘플·10스텝), 카메라 6대(궤적)·VQA 6대 |
| NVlabs/alpamayo2 `src/alpamayo2_super/models/alpamayo2_super.py`, `inference_smoke.py` | https://github.com/NVlabs/alpamayo2/tree/main/src/alpamayo2_super | `num_traj_samples: int = 1` 기본값 |
| Hugging Face nvidia/Alpamayo2-Super 모델카드 | https://huggingface.co/nvidia/Alpamayo2-Super | H100 80 GB 1장 테스트, 피크 72,115 MiB, 측정 조건(7카메라·4프레임·배치 1·1샘플·BF16·SDPA·CFG 끔·10스텝), "다른 아키텍처 미검증" |
| Hugging Face nvidia/Alpamayo-1.5-10B 모델카드 | https://huggingface.co/nvidia/Alpamayo-1.5-10B | 최소 24 GB VRAM, flash-attn/SDPA |
| Hugging Face nvidia/Alpamayo-R1-10B 모델카드 | https://huggingface.co/nvidia/Alpamayo-R1-10B | 가중치·최소 사양 |
| NVlabs/alpamayo-recipes README | https://github.com/NVlabs/alpamayo-recipes | 레시피 목록(SFT 1·1.5, RL, 양자화), 2 Super를 "DRIVE AGX Thor용 증류 교사 모델"로 규정 |
| alpamayo-recipes `recipes/alpamayo1_sft/README.md` | https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_sft/README.md | "8× H100 80 GB에서 검증", DeepSpeed ZeRO-2, `--nproc_per_node 8` |
| alpamayo-recipes `recipes/alpamayo1_5_sft/README.md` | https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_5_sft/README.md | 1.5 SFT(내비·VQA), 8 GPU 실행 예시 |
| alpamayo-recipes `recipes/alpamayo1_x_rl/README.md` | https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_x_rl/README.md | RL 로컬 테스트 "GPU 5장 이상, 각 80 GB 이상", 8× H100 약 10분 / 8× A100 약 1.1시간, 대규모 640 GPU 예시 |
| alpamayo-recipes `recipes/alpamayo1_5_quant/README.md` | https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_5_quant/README.md | 양자화 레시피 테스트 환경(RTX 5090 + CUDA 12, B300 + CUDA 13) |
| NVlabs/alpagym README · `docs/ONBOARDING.md` | https://github.com/NVlabs/alpagym · https://github.com/NVlabs/alpagym/blob/main/docs/ONBOARDING.md | "10B 모델은 GPU 2장 필요", 40 GB 이상 GPU 2장(2× RTX 6000 Ada 50 GB 테스트), 디스크 100~150 GB, NuRec 씬 1.5 GB·전체 1.5 TB, 2B 증류 계획 |
| NVlabs/alpasim `docs/ONBOARDING.md` | https://github.com/NVlabs/alpasim/blob/main/docs/ONBOARDING.md | FlashDreams + 1.5 단일 카메라 프리셋 약 96 GB, 경량 드라이버 약 48 GB |
| NVIDIA Tech Blog: How to Post-Train AV Models in Closed-Loop with NVIDIA Alpamayo (2026-05-31) | https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/ | AlpaGym 구조, 단일 GPU → 멀티노드 확장 |

### 6.2 차량 배포 런타임 (TensorRT Edge-LLM)

| 자료 | URL | 뒷받침하는 내용 |
|---|---|---|
| TensorRT Edge-LLM 지원 매트릭스 | https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/getting_started/support-matrix.html (원문: https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/getting_started/support-matrix.md) | 공식 플랫폼: Jetson Thor(JetPack 7.0~7.2), DRIVE Thor(DriveOS 7.2), DGX Spark, Jetson Orin(JetPack 7.2, FP16·INT8·INT4만). x86는 "Developer" 등급 |
| TensorRT Edge-LLM 지원 모델 | https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/getting_started/supported-models.md | Alpamayo는 `nvidia/Alpamayo-R1-10B`만 등재 |
| TensorRT Edge-LLM Alpamayo 예제 | https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/examples/vla/alpamayo.md | "Only FP16 is supported for Alpamayo export", 엔진 빌드 `--maxBatchSize 6`, 4카메라 × 4프레임 |
| TensorRT Edge-LLM 이슈 #130 "Alpamayo Support" | https://github.com/NVIDIA/TensorRT-Edge-LLM/issues/130 | 1.5 지원 요청, 2026-07-08 등록, 라벨 "New Model / Roadmap", 무응답 |
| TensorRT Edge-LLM 이슈 #134 | https://github.com/NVIDIA/TensorRT-Edge-LLM/issues/134 | 양자화 Alpamayo export 요청, "FP16만 지원" 재확인 |
| TensorRT Edge-LLM Discussion #155 | https://github.com/NVIDIA/TensorRT-Edge-LLM/discussions/155 | Jetson Orin은 양자화·export 호스트 불가, 배포 타깃으로는 지원 |
| Jetson AI Lab: TensorRT Edge-LLM on Jetson | https://www.jetson-ai-lab.com/tutorials/tensorrt-edge-llm/ | Alpamayo R1 튜토리얼 "FP16 only", 엔진은 장치에서 빌드 |

### 6.3 실행 사례·포럼

| 자료 | URL | 뒷받침하는 내용 |
|---|---|---|
| NVIDIA 포럼: Alpamayo-R1-10B TensorRT engine OOM on DRIVE AGX Thor | https://forums.developer.nvidia.com/t/alpamayo-r1-10b-tensorrt-engine-oom-on-drive-agx-thor/382500 | DriveOS 7.2.5, 엔진 직렬화 시 15.17 GB 요청 OOM, 미해결 |
| NVIDIA 포럼: Drive AGX thor with Alpamayo | https://forums.developer.nvidia.com/t/drive-agx-thor-with-alpamayo/382501 | 같은 배포, CUDA 가용 메모리 6.0 GiB 보고 |
| NVIDIA 포럼: Build alpamayo1_5 native on Thor | https://forums.developer.nvidia.com/t/build-alpamayo1-5-native-on-thor/382647 | Jetson Thor에서 1.5를 PyTorch(소스 빌드) + SDPA로 실행 |
| NVIDIA 포럼: Spark DGX Alpamayo + Alpasim | https://forums.developer.nvidia.com/t/spark-dgx-alpamayo-alpasim/357383 | DGX Spark에서 Alpamayo·AlpaSim 부분 동작 보고 |
| NVlabs/alpamayo 이슈 #69 | https://github.com/NVlabs/alpamayo/issues/69 | "Jetson AGX Orin 64GB가 최소 사양인가" 질문, 무응답 |
| arXiv 2605.08975 Latency Analysis and Optimization of Alpamayo 1 | https://arxiv.org/abs/2605.08975 | DGX Spark(GB10)에서 Alpamayo 1 6궤적 실행 |
| arXiv 2605.11678 OOM-Free Alpamayo via CPU-GPU Memory Swapping | https://arxiv.org/abs/2605.11678 | RTX 5090에서 R1 1샘플 1.03 s, R1 BF16 21.52 GB, 16 GB 카드는 스와핑 없이는 불가 |
| arXiv 2511.00088 Alpamayo-R1 논문 | https://arxiv.org/abs/2511.00088 | RTX 6000 Pro Blackwell에서 99 ms(추론 40토큰·flow 5스텝) / 29 ms(궤적만) |
| arXiv 2608.12932 FlashDrive 논문 · z-lab/flashdrive README | https://arxiv.org/abs/2608.12932 · https://github.com/z-lab/flashdrive | RTX PRO 6000·Jetson Thor·RTX 3090/4090/5090에서 Alpamayo 1·1.5 기준 지연과 최적화 후 지연 |
| NVIDIA Tech Blog: Build Next-Gen Physical AI with Edge-First LLMs (2026-03-12) | https://developer.nvidia.com/blog/build-next-gen-physical-ai-with-edge%E2%80%91first-llms-for-autonomous-vehicles-and-robotics/ | "DRIVE Thor에서 Alpamayo 1이 production-viable latency", ViT FP8 (수치 없음) |
| NVIDIA NIM Alpamayo 1.5 문서 (prerequisites · support-matrix) | https://docs.nvidia.com/nim/alpamayo/latest/prerequisites.html · https://docs.nvidia.com/nim/alpamayo/1.0.0/support-matrix.html | x86 호스트, GPU 1장/컨테이너, BF16 30 GB 이상·양자화 프로파일 20 GB 이상 |
| autowarefoundation/alpamayo-autoware (alpamayo1.5 · alpamayo2.0-super 브랜치) | https://github.com/autowarefoundation/alpamayo-autoware | RTX PRO 6000 96 GB에서 1.5·2 Super 노드 실행, 2 Super 피크 69.1 GiB |

### 6.4 하드웨어 사양

| 자료 | URL | 뒷받침하는 내용 |
|---|---|---|
| NVIDIA DRIVE AGX Thor Development Platform (PDF, 2025-12) | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | 64 GB LPDDR5X 273 GB/s, 1,000 INT8 TOPS, SKU10/12, 개발자 프로그램 |
| NVIDIA Tech Blog: Accelerate AV Development with the DRIVE AGX Thor Developer Kit | https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/ | 64 GB LPDDR5X @ 4266 MHz, DriveOS 7 |
| NVIDIA Jetson Thor 제품 페이지 | https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ | T5000 128 GB LPDDR5X 273 GB/s, 2,070 FP4 TFLOPS |
| NVIDIA Tech Blog: Jetson T4000 and JetPack 7.1 | https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ | T4000 64 GB, 1,200 FP4 TFLOPS |
| NVIDIA Jetson AGX Orin 제품 페이지·기술 브리프 | https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/ · https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf | 64 GB LPDDR5 204.8 GB/s, Ampere 2,048 CUDA 코어, 275 TOPS |
| NVIDIA DRIVE AGX (Orin 개발킷 페이지) | https://developer.nvidia.com/drive/agx | 단일 Orin SoC, 254 TOPS |
| NVIDIA 포럼: DRIVE OS 6.0.10.0 is now available | https://forums.developer.nvidia.com/t/announcement-from-nvidia-drive-os-6-0-10-0-is-now-available/303314 | DriveOS 6.0.10 = CUDA 11.4, TensorRT 8.6.13 |
| NVIDIA 포럼: PyTorch with GPU on DRIVE AGX Orin · Installation of PyTorch on DRIVE Orin | https://forums.developer.nvidia.com/t/pytorch-with-gpu-on-drive-agx-orin/253407 · https://forums.developer.nvidia.com/t/installation-of-pytorch-with-cuda-support-on-drive-orin/346369 | "PyTorch는 DRIVE에서 공식 지원하지 않음" |
| NVIDIA 포럼: PyTorch 2.8 wheel for JetPack 6.2 | https://forums.developer.nvidia.com/t/pytorch-2-8-wheel-for-jetpack-6-2/341339 | Orin용 PyTorch 2.8 휠 |
| NVIDIA DGX Spark 제품 페이지 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | GB10, 128 GB LPDDR5X 273 GB/s, 1 PFLOP NVFP4 |
| GeForce RTX 50 사양 (GamersNexus) · RTX 40 사양 (Wikipedia) · RTX 3090 (NVIDIA) | https://gamersnexus.net/gpus/nvidia-rtx-5090-575-watts-rtx-5080-5070-ti-5070-specs · https://en.wikipedia.org/wiki/GeForce_RTX_40_series · https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/ | VRAM·대역폭·세대 |
| RTX PRO 6000 Blackwell 데이터시트 · RTX PRO 5000 72 GB (VideoCardz) · RTX 6000 Ada | https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/rtx-pro-6000-blackwell-workstation-edition/workstation-blackwell-rtx-pro-6000-workstation-edition-nvidia-us-3519208-web.pdf · https://videocardz.com/newz/nvidia-quietly-launches-rtx-pro-5000-blackwell-workstation-card-with-72gb-of-memory · https://www.thundercompute.com/blog/nvidia-rtx-6000-ada-pricing | 96 GB / 72 GB / 48 GB 사양 |
| NVIDIA L40S · H100 · H200 사양 | https://www.nvidia.com/en-us/data-center/l40s/ · https://www.hyperstack.cloud/technical-resources/performance-benchmarks/comparing-nvidia-h100-pcie-vs-sxm-performance-use-cases-and-more · https://www.runpod.io/articles/guides/nvidia-h200-gpu | 메모리·대역폭 |

### 6.5 가격

| 자료 | URL | 뒷받침하는 내용 |
|---|---|---|
| CNX Software: NVIDIA increases the price of Jetson modules and devkits by up to 101% (2026-07-22) · VideoCardz | https://www.cnx-software.com/2026/07/22/nvidia-increases-the-price-of-jetson-modules-and-devkits-by-up-to-101/ · https://videocardz.com/newz/nvidia-raises-jetson-prices-by-up-to-101-agx-thor-now-costs-5499 | AGX Thor 개발킷 $5,499, AGX Orin 개발킷 $3,499, 64GB 모듈 $2,999, T4000 $2,999, Orin Nano Super $399 |
| CNX Software: $3499 Jetson AGX Thor Developer Kit (2025-08) · NVIDIA 뉴스룸 | https://www.cnx-software.com/2025/08/19/3499-nvidia-jetson-agx-thor-developer-kit-2070-tops-jetson-t5000-som-for-robotics-and-edge-ai/ · https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics | 출시가 $3,499 |
| Hackster: Jetson AGX Orin Developer Kit at $1,999 (2022) | https://www.hackster.io/news/nvidia-launches-275-tops-jetson-agx-orin-developer-s-kit-at-1-999-bbb5ff80e050 | 구가 $1,999 |
| Arrow: DRIVE AGX Orin Developer Kit 940-63710-0010-300 | https://www.arrow.com/en/products/940-63710-0010-300/nvidia.html | MSRP $7,500 |
| ICBanq: Jetson AGX Thor 개발킷 · Jetson AGX Orin 64GB 개발킷 | https://www.icbanq.com/P016786968 · https://www.icbanq.com/P015243419 | 국내 유통가 540만 / 462만~560만 |
| Tom's Hardware: DGX Spark gets $700 price hike (2026-02) · pi3g DGX Spark 가격 정리 | https://www.tomshardware.com/desktops/mini-pcs/nvidia-dgx-spark-gets-18-percent-price-increase-as-memory-shortages-bite-founders-edition-now-usd4-699-up-from-usd3-999 · https://pi3g.com/nvidia-dgx-spark-price/ | $3,999 → $4,699, 파트너 $4,100~ |
| 나무위키·클리앙 DGX Spark 국내가 | https://namu.wiki/w/NVIDIA%20RTX%20Spark%20%C2%B7%20DGX%20Spark · https://www.clien.net/service/board/news/19077958 | 국내 700만 원대~ |
| RTX 5090 시세: ThinkComputers · Tech Insider · videocardprices · 다나와 | https://thinkcomputers.org/rtx-5090-shortage-deepens-as-ai-buyers-push-retail-cards-above-5000 · https://tech-insider.org/rtx-5090-price-4329-rtx-60-delay-2028-2026/ · https://videocardprices.com/card/nvidia-rtx-5090/ · https://prod.danawa.com/info/?pcode=75184280 | 소매 $4,300~5,000, 국내 550만~650만 |
| RTX 4090 중고 (GetPCParts) · RTX 3090 중고 (ResalePrices) · RTX 5080/5070 Ti/4080 Super (Tom's Hardware 추적·gpuprix) | https://www.getpcparts.com/market-prices/gpu-graphics-cards/rtx-4090 · https://resaleprices.com/gpu/nvidia-rtx-3090 · https://www.tomshardware.com/pc-components/gpus/lowest-gpu-prices-tracking · https://gpuprix.com/us/gpus/geforce-rtx-4080-super | 중고·소매 시세 |
| Tom's Hardware: NVIDIA doubles RTX PRO 6000 Blackwell MSRP to $16,000 · videocardprices RTX PRO 6000 | https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year · https://videocardprices.com/card/nvidia-rtx-pro-6000-blackwell/ | MSRP $16,000, 시세 $14,000~18,000 |
| RTX PRO 5000 (VideoCardz) · RTX 6000 Ada (gpucost) · A6000 중고 (gpudojo) | https://videocardz.com/newz/nvidia-quietly-launches-rtx-pro-5000-blackwell-workstation-card-with-72gb-of-memory · https://gpucost.org/gpu/rtx-6000-ada · https://gpudojo.com/a6000 | 워크스테이션 GPU 가격 |
| L40S (gpudojo) · A100 (jarvislabs) · H100 (jarvislabs·compute.exchange) · H200 (jarvislabs) | https://gpudojo.com/l40s · https://jarvislabs.ai/blog/a100-price · https://jarvislabs.ai/blog/h100-price · https://compute.exchange/blogs/h100-gpu-price-2026 · https://jarvislabs.ai/blog/h200-price | 서버 GPU 구매가 |
| 클라우드 임대: Lambda · RunPod · Vast(computeprices) · AWS(vantage) | https://lambda.ai/pricing · https://www.runpod.io/pricing · https://computeprices.com/providers/vast · https://instances.vantage.sh/aws/ec2/p5.48xlarge · https://instances.vantage.sh/aws/ec2/g6e.xlarge | 시간당 임대가 |
| 환율 (2026-09-30 매매기준율 1,358.34원) | https://github.com/seotaiji0324/Daily_Finance_Briefing/issues/44 · https://kr.investing.com/currencies/usd-krw | 원화 환산 기준 |

---

## 7. 공식·논문·벤치마크의 실행 환경 한눈에 보기

### 7.1 읽는 법

- "성격" 열: **공식** = NVIDIA 저장소·모델카드·문서·블로그, **논문** = arXiv 학술 논문, **서드파티** = 외부 기관의 공개 저장소, **커뮤니티** = NVIDIA 포럼 사용자 보고.
- 최적화·양자화가 들어간 결과는 "실행 방식" 열에 그렇게 적었다. 그 기법 자체는 별도 문서에서 다룬다.
- 지연은 모두 궤적 1회 추론 기준이며, 측정 범위(전처리 포함 여부 등)가 자료마다 달라 행 사이 직접 비교는 조건을 확인한 뒤 해야 한다.

### 7.2 추론 실행 환경

"실행 방식" 열 맨 앞의 【 】 안은 4.1절 비교 항목 중 어디에 해당하는지를 뜻한다. 【—】는 비교 항목과 직접 대응하지 않는 경우다.

| 자료 | 모델 | 하드웨어 | 실행 방식 | 결과 | 성격 · 출처 |
|---|---|---|---|---|---|
| NVlabs/alpamayo README | 1 (R1) | RTX 3090 · A100 · H100 (예시에 RTX 4090·A5000) | 【1샘플】 PyTorch 2.8, BF16, flash-attn(또는 SDPA), `test_inference.py` 1샘플 | 동작 확인용. 지연·메모리 수치 없음 (최소 VRAM 24 GB) | 공식 · [README](https://github.com/NVlabs/alpamayo) |
| Alpamayo-R1 논문 | 1 (R1) | RTX 6000 Pro Blackwell (워크스테이션 GPU) | 【1샘플】 추론 텍스트 40토큰, flow 5스텝 | 1회 99 ms (궤적만 29 ms). 시험 차량 공로 주행도 보고, 차량 컴퓨터 사양은 미기재 | 논문(NVIDIA) · [arXiv 2511.00088](https://arxiv.org/abs/2511.00088) |
| NVlabs/alpamayo1.5 README | 1.5 | H100 80 GB (테스트 GPU: RTX 3090 · A100 · H100 · B200) | 【1샘플】【16샘플】【16샘플+CFG】 PyTorch 2.8, BF16 | 1샘플 약 24 GB, 16샘플 약 40 GB, 16샘플 + CFG 약 60 GB. 지연 수치 없음 | 공식 · [README](https://github.com/NVlabs/alpamayo1.5) · [내비 노트북](https://github.com/NVlabs/alpamayo1.5/blob/main/notebooks/inference_nav.ipynb) |
| Alpamayo 2 Super 모델카드 · NVlabs/alpamayo2 README | 2 Super | H100 80 GB 1장 · 내비 CFG는 H100 80 GB 2장 | 【2 Super 1샘플】 BF16, SDPA, 7카메라 × 4프레임, 1샘플, CFG 끔, 10스텝 · 【2 Super CFG】 VLM/expert를 GPU 2장에 수동 배치, 1샘플 | 피크 72,115 MiB · CFG 예제 67 GiB + 71 GiB. 지연 수치 없음 | 공식 · [모델카드](https://huggingface.co/nvidia/Alpamayo2-Super) · [README](https://github.com/NVlabs/alpamayo2) |
| NVIDIA NIM Alpamayo 1.5 | 1.5 | x86 서버, GPU 1장/컨테이너 (CC 8.0 이상) | 【1샘플】 컨테이너 배포, BF16 · FP8 · W4A16 프로파일 자동 선택 (기본 궤적 1개) | BF16은 30 GB 이상, 양자화 프로파일은 20 GB 이상. 지연 수치 없음 | 공식 · [prerequisites](https://docs.nvidia.com/nim/alpamayo/latest/prerequisites.html) · [support matrix](https://docs.nvidia.com/nim/alpamayo/1.0.0/support-matrix.html) |
| TensorRT Edge-LLM Alpamayo 예제 | 1 (R1) | Jetson AGX Thor (JetPack 7) · DRIVE Thor (DriveOS 7.2) · DGX Spark · Jetson Orin (JetPack 7.2) | 【Edge-LLM】 x86에서 ONNX export(FP16만) → 장치에서 TensorRT 엔진 빌드(LLM·visual·action 3개, 최대 배치 6) → C++ 런타임 | 지연·메모리 수치 없음 | 공식 · [예제 문서](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/examples/vla/alpamayo.md) · [지원 매트릭스](https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/getting_started/support-matrix.md) |
| NVIDIA 블로그: Edge-First LLMs (2026-03) | 1 (R1) | DRIVE Thor | 【Edge-LLM】 ViT에 FP8 가속 | "production-viable latencies" 표현만, 수치 없음 | 공식 · [블로그](https://developer.nvidia.com/blog/build-next-gen-physical-ai-with-edge%E2%80%91first-llms-for-autonomous-vehicles-and-robotics/) |
| 지연 분석 논문 | 1 (R1) | DGX Spark (GB10, 128 GB) | 【—】 PyTorch, 6샘플. 다중 추론 → 단일 추론 재설계, expert 커널 정리, CUDA graph + 정적 KV 캐시 | 13.33 s → 4.10 s (69% 감소) | 논문 · [arXiv 2605.08975](https://arxiv.org/abs/2605.08975) |
| OOM-Free Alpamayo 논문 | 1 (R1) | RTX 5070 Ti 16 GB (기준 비교: RTX 5090 32 GB) | 【1샘플】 BF16 유지, 층 단위 CPU-GPU 스와핑 | RTX 5090 전량 적재 시 1.03 s. 5070 Ti는 UVM 기준 69.6 s/추론에서 오프로드 대비 최대 3.55배 개선 | 논문 · [arXiv 2605.11678](https://arxiv.org/abs/2605.11678) |
| FlashDrive 논문 · z-lab/flashdrive | 1 (R1) · 1.5 | RTX PRO 6000 · RTX 5090 · RTX 4090 · RTX 3090 · Jetson AGX Thor | 【1샘플】 PyTorch. 기준(BF16) 대비 W4A8 양자화 + 추측 디코딩 + 스트리밍 KV 캐시 + CUDA graph 적용 | 기준 → 최적화: RTX PRO 6000 716.9 → 151.4 ms, RTX 5090 878.1 → 183.7 ms, RTX 4090 1,307.1 → 217.2 ms, RTX 3090 1,891.9 → 382.3 ms, Jetson Thor 3,770.3 → 943.6 ms. 메모리 FP16 약 31.6 GB → W4A8 약 18.3 GB | 논문(UCSD Z Lab, 서드파티) · [arXiv 2608.12932](https://arxiv.org/abs/2608.12932) · [GitHub](https://github.com/z-lab/flashdrive) · [프로젝트 페이지](https://z-lab.ai/projects/flashdrive/) |
| alpamayo-autoware `alpamayo1.5` 브랜치 | 1.5 | RTX PRO 6000 Blackwell 96 GB | 【1샘플】 ROS 2 Humble 노드, 카메라 4대 × 4프레임 1080×1920, greedy 디코딩, flow 5스텝, expert만 TensorRT INT8/FP16 | 1회 0.60~0.82 s (구성별) | 서드파티(TIER IV) · [README](https://github.com/autowarefoundation/alpamayo-autoware/blob/alpamayo1.5/README.md) |
| alpamayo-autoware `alpamayo2.0-super` 브랜치 | 2 Super | RTX PRO 6000 Blackwell 96 GB | 【2 Super 1샘플】 ROS 2 노드, 카메라 6대, BF16, SDPA, 304회 측정 · 【2 Super CFG】 VLM 2회 prefill로 1장에서 구현(공식 2장 예제와 다름) | 평균 3.35 s(p90 3.97 s), 피크 69.1 GiB · CFG 켜면 5.2 s, 70.9 GiB. "폐루프 사용 불가" 명시 | 서드파티(TIER IV) · [README](https://github.com/autowarefoundation/alpamayo-autoware/blob/alpamayo2.0-super/README.md) |
| NVIDIA 포럼 "Build alpamayo1_5 native on Thor" | 1.5 | Jetson AGX Thor | 【1샘플】 PyTorch 소스 빌드, flash-attn 없이 SDPA | 실행 성공 보고. 지연 수치 없음 | 커뮤니티 · [포럼 382647](https://forums.developer.nvidia.com/t/build-alpamayo1-5-native-on-thor/382647) |
| NVIDIA 포럼 "Alpamayo-R1-10B TensorRT engine OOM on DRIVE AGX Thor" 외 1건 | 1 (R1) | DRIVE AGX Thor 개발킷 (DriveOS 7.2.5, CUDA 13.3, TensorRT 11.0.1) | 【Edge-LLM】 FP16 엔진 빌드 | 엔진 직렬화 중 15.17 GB 요청 OOM (CUDA 가용 6.0 GiB 보고). 미해결 | 커뮤니티 · [포럼 382500](https://forums.developer.nvidia.com/t/alpamayo-r1-10b-tensorrt-engine-oom-on-drive-agx-thor/382500) · [포럼 382501](https://forums.developer.nvidia.com/t/drive-agx-thor-with-alpamayo/382501) |
| NVIDIA 포럼 "Spark DGX Alpamayo + Alpasim" | 1.x + AlpaSim | DGX Spark | 【—】 로컬 설치 시도 | "부분적으로 동작하나 Spark 단일 노드 구조와 맞지 않음". 수치 없음 | 커뮤니티 · [포럼 357383](https://forums.developer.nvidia.com/t/spark-dgx-alpamayo-alpasim/357383) |

### 7.3 학습·폐루프·양자화 실행 환경

| 자료 | 작업 | 하드웨어 | 실행 방식 | 결과 | 성격 |
|---|---|---|---|---|---|
| alpamayo-recipes `alpamayo1_sft` | SFT | 8× H100 80 GB | HF Trainer + DeepSpeed ZeRO-2, `torchrun --nproc_per_node 8`, Stage 1(VLM) → Stage 2(expert) | 검증 완료 표기. 소요 시간 미기재 | 공식 |
| alpamayo-recipes `alpamayo1_5_sft` | SFT (내비·VQA) | 8 GPU 실행 예시 | 같은 스택 | — | 공식 |
| alpamayo-recipes `alpamayo1_x_rl` | RL (GRPO) | 로컬 테스트 GPU 5장(각 80 GB 이상) · 8× H100 노드 · 8× A100 노드 · 대규모 640 GPU | Cosmos-RL, 정책 4장 FSDP + 롤아웃 1장 | 8× H100 약 10분(동작 보상), 8× A100 약 1.1시간(추론+동작 보상) | 공식 |
| NVlabs/alpagym | 폐루프 RL 스모크 | 2× RTX 6000 Ada 50 GB (40 GB 이상 2장 권장) | AlpaSim + Cosmos-RL, 정책·롤아웃 GPU 분리 | 동작 확인용 | 공식 |
| NVlabs/alpasim ONBOARDING | 폐루프 평가 | GPU 1장 96 GB (1.5 단일 카메라 프리셋) / 48 GB (경량 드라이버) | FlashDreams 렌더러 + 드라이버 동일 GPU | — | 공식 |
| alpamayo-recipes `alpamayo1_5_quant` | 양자화 (FP8 · AutoQuant) | RTX 5090 + CUDA 12 · B300 + CUDA 13 | ModelOpt 0.43, 보정 클립 100개 | FP8 약 11 GB, AutoQuant 6.5 bit 약 9 GB (정확도·지연 미기재) | 공식 |

### 7.4 한눈에 보는 요점

- **NVIDIA가 지연을 숫자로 공개한 것은 R1 논문의 99 ms(RTX 6000 Pro Blackwell) 하나뿐이다.** 차량용 Thor에서의 공식 지연 수치는 없고 "production-viable"이라는 표현만 있다.
- **메모리를 숫자로 공개한 것은 1.5 README(H100, 24/40/60 GB)와 2 Super 모델카드(H100, 72,115 MiB)다.**
- **임베디드 보드에서의 실측은 전부 논문·커뮤니티 몫이다.** Jetson Thor(FlashDrive, 포럼), DGX Spark(지연 분석 논문, 포럼), DRIVE Thor(포럼, 실패)뿐이고 Jetson Orin 실측은 없다.
- **DRIVE AGX Thor에서 Alpamayo가 실제로 돌았다는 공개 사례는 없다.** 공개된 "Thor" 실행 사례(FlashDrive 논문, 포럼 네이티브 빌드)는 모두 Jetson AGX Thor다. DRIVE Thor 쪽은 NVIDIA 블로그의 "production-viable latency" 서술(수치·재현 자료 없음)과 커뮤니티의 엔진 빌드 실패 보고 2건뿐이다.
- **공식 학습 환경은 H100 8장 노드가 기준이며**, 폐루프 RL 스모크만 48 GB급 2장으로 내려온다.
