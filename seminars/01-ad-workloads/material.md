# 1회차 — 자율주행/ADAS 워크로드의 이해: SW 스택이 컴퓨팅에 요구하는 것

> **대상**: 차량용 HPC 아키텍처 설계 팀 | **형식**: 세미나 발표 정리본 (발표 대본 수준)
> **한 줄 요약**: 자율주행 워크로드는 CNN 중심의 compute-bound에서 Transformer/VLA 중심의 **memory-bandwidth-bound**로 이동 중이며, 이것이 차세대 HPC 설계의 1차 결정 변수다.

---

## 0. 발표 흐름 안내 (5분)

이번 세미나는 "우리가 설계하는 HPC 위에서 실제로 무엇이 돌아가는가"를 다룹니다. 알고리즘 자체보다, **각 워크로드가 하드웨어 자원(연산기, 메모리, I/O)을 어떻게 압박하는지**의 관점으로 정리했습니다.

1. 왜 HPC가 필수가 됐나 (배경)
2. 고전적 AD 파이프라인 — 모듈별 연산 특성
3. 최신 AI 모델 트렌드 — BEV/Occupancy, End-to-End, VLA, World Model
4. 온보드 최적화 연구 동향 — 큰 모델을 차량 SoC에 올리는 기법들
5. 워크로드 정량화 — 숫자로 보는 요구사항
6. HPC 설계 시사점 종합

---

## 1. 왜 HPC가 필수가 됐나 (10분)

### 자율화 레벨별 컴퓨트 요구의 계단식 증가

업계 통용 추정치 기준 (공식 표준 아님, 필요조건의 감각치로만 사용):

| 레벨 | AI 연산 요구 (업계 통용치) | 비고 |
|---|---|---|
| L2 | < 10 TOPS | 실질 2–2.5 TOPS 사례도 |
| L3 | 20–30 TOPS | eyes-off 진입 |
| L4 | 200–320+ TOPS | 도심 무인 주행 |
| 2025+ 플래그십 (도심 NOA + E2E/VLA) | **500–2,000+ TOPS** | 소프트웨어 성장 헤드룸 포함 |

출처: [Huawei MDC 기고](https://www.huawei.com/en/huaweitech/publication/86/driverless-vehicles-with-MDC), [ersa electronics](https://www.ersaelectronics.com/blog/autonomous-driving-levels), [Nevsemi Top-20 AD chips 2025](https://www.nevsemi.com/blog/top-20-most-advanced-autonomous-driving-chips-2025)

> ⚠️ **TOPS는 필요조건이지 충분조건이 아님** — Mobileye EyeQ6H는 34 DL TOPS(INT8) 칩 2개로 hands-off 시스템(SuperVision) 전체 스택을 구동한다. 아키텍처 효율과 실사용률(utilization)이 실성능을 결정한다. 출처: [Mobileye EyeQ6 블로그](https://www.mobileye.com/blog/the-fast-lane-to-higher-levels-of-autonomy-with-the-eyeq6-soc/), [Mobileye 벤치마크](https://www.mobileye.com/technology/eyeq-chip/benchmark/)

### 중앙집중형 HPC로의 수렴 이유

1. **컴퓨트 스케일링**: 레벨당 요구 연산이 ~10배씩 증가 — 분산 ECU 수십 개로는 담을 수 없는 밀도.
2. **데이터 중력**: E2E/BEV 모델은 전 센서의 raw/저레벨 데이터를 **한 곳에서 시간 동기화해 융합**해야 성능이 나온다. 레이더 raw 데이터를 중앙 처리하면 레이더 5대 합산 ~540MB/s(≈4.3Gbps)로 커지지만 L4급 인지 성능이 확보된다 ([NVIDIA Centralized Radar Processing, 2025](https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy/)).
3. **E2E 모델의 단일성**: 단일 신경망은 기능 분산이 불가능 — 모델 하나가 하나의 큰 NPU/GPU 메모리 공간을 요구한다 (Tesla FSD v13 주행 모델 추정 ~7.5GB, §3 참조).
4. **L3의 법적 책임 → 이중화**: eyes-off부터 제동·조향·전원·컴퓨트의 물리적+기능적 이중화가 인증 요건. "고성능 컴퓨터 2계통" 구조에서만 비용이 성립 ([Mercedes-Benz redundancy](https://group.mercedes-benz.com/technology/autonomous-driving/driving/redundancy-drive-pilot.html)).
5. **E/E 아키텍처 경제성**: zonal + central HPC 전환으로 와이어링 하네스 30–40% 감축 전망 ([GMI](https://www.gminsights.com/industry-analysis/automotive-zonal-architecture-domain-controller-market)).

시장 전망: 중앙집중형 E/E 아키텍처 차량 2035년 4,781만 대(Yano Research), zonal/domain controller 시장 2025년 $4.9B → 2035년 $20.7B (CAGR 16.1%, GMI).

---

## 2. 고전적 AD 파이프라인 — 모듈별 연산 특성 (15분)

**Sensing → Perception → Localization → Prediction → Planning → Control**

### 모듈별 연산 내용과 하드웨어 친화성

| 모듈 | 대표 연산 | 연산 특성 / 바운드 |
|---|---|---|
| Sensing (ISP/전처리) | debayering, HDR merge, lens correction, point cloud 조립 | 고정 기능 ISP/DSP, **스트리밍 I/O 대역폭 바운드** |
| Perception | CNN inference (최근 BEV Transformer), voxelization/clustering | **GPU/NPU 바운드** (dense MAC), 해상도에 연산량 급증 |
| Tracking / Fusion | Kalman filter (EKF/UKF), Hungarian matching | 소규모 행렬·분기 많음 → **CPU/DSP**, latency-critical |
| Localization | LiDAR scan matching (ICP/NDT), particle filter, GNSS/IMU EKF | CPU 병목 심함 — **가속기 이득이 가장 큰 모듈** |
| Prediction | GNN/Transformer 기반 trajectory prediction | GPU/NPU (소형 모델, 저지연) |
| Planning | behavior planning, QP/NLP 최적화, MPC, sampling(A*, lattice) | **CPU 바운드** (분기·반복·희소 선형대수), 병렬화 어려움 |
| Control | PID/MPC, 액추에이터 명령 | CPU, 100Hz+ 고주기, **ASIL-D 결정성** 요구 |

### 정량 근거 — ASPLOS 2018 (U. Michigan)

자율주행 워크로드 아키텍처 분석의 고전 레퍼런스 ([ACM ASPLOS 2018](https://dl.acm.org/doi/10.1145/3173162.3173191)):

- End-to-end 지연 제약 **~100ms** (사람 반응속도보다 빨라야 한다는 논리)
- **localization, detection, tracking 3개 모듈이 E2E latency를 지배** — 멀티코어 CPU만으로는 실시간 불가를 실측으로 입증
- 가속기 적용 시 tail latency 개선: localization **169×**(FPGA/ASIC), detection **10×**(GPU), tracking **93×**
- GPU는 지연을 만족시키지만 **전력+냉각 부하가 주행거리를 잠식**
- Full HD까지는 실시간 가능, **Quad HD는 어떤 조합도 실시간 미달** — "카메라 해상도 향상을 컴퓨트가 막는다"

### Latency 예산

- 업계 표준 perception–planning 스택: **10–12Hz 주기 → 사이클당 80–100ms** 예산. Mobileye도 100ms 예산 사용 인용 ([arXiv:2207.08930](https://arxiv.org/pdf/2207.08930), [arXiv:2112.14947](https://arxiv.org/pdf/2112.14947))
- **평균이 아닌 p99 tail latency가 안전성 결정 요인** ([COLA, arXiv:2305.07147](https://arxiv.org/pdf/2305.07147))

> 💡 **HPC 설계 시사점**: 모듈형 스택은 "GPU/NPU(perception) + 실시간 CPU 클러스터(planning/control) + lockstep 안전 코어(ASIL-D)"의 **이기종(heterogeneous) 구성을 강제**하며, 모듈 간 데이터 이동(카메라 프레임, BEV feature, point cloud)이 온칩 fabric/메모리 대역폭을 소모한다.

---

## 3. 최신 AI 모델 트렌드와 컴퓨트 수요 (20분)

### 3.1 BEV + Transformer / Occupancy

- **BEVFormer** ([arXiv:2203.17270](https://arxiv.org/pdf/2203.17270)): multi-camera 이미지를 spatiotemporal deformable attention으로 통합 BEV 표현으로 변환. 기본 구성 inference ~130ms, TensorRT FP16 최적화 후 **~90ms**, 경량화 구성 25ms ([MulticoreWare 최적화 사례](https://multicorewareinc.com/optimized-bev-models-for-real-time-autonomous-perception-bevdet-bevformer/)). 병목은 multi-view 입력 탓에 **backbone(CNN) 연산**.
- **하드웨어 관점 문제**: deformable attention의 불규칙 메모리 접근은 NPU 비친화적 — 하드웨어 지향 BEV 설계 연구가 별도로 존재 ([HotBEV, NeurIPS 2023](https://openreview.net/forum?id=3Cj67k38st), [Fast-BEV](https://arxiv.org/pdf/2301.12511)).
- **Occupancy Network**: Tesla가 CVPR 2022 워크숍에서 공개 — FSD 컴퓨터에서 **~10ms 저지연 실시간 추론**. 비정형 장애물을 3D voxel 점유로 표현 → dense 3D 출력이라 **메모리 사용량이 큼** ([arXiv:2303.01212](https://arxiv.org/pdf/2303.01212)).

### 3.2 End-to-End 주행

- **UniAD** (CVPR 2023 Best Paper, [arXiv:2212.10156](https://arxiv.org/abs/2212.10156)): detection·tracking·mapping·prediction·planning을 **단일 query 기반 Transformer**로 통합한 planning-oriented 설계.
- **Tesla FSD v12** (2024): 카메라→제어를 단일 신경망으로 대체, **~30만 줄 rule-based C++ 제거** ([분석](https://www.fredpope.com/blog/machine-learning/tesla-fsd-12)).
- **Tesla FSD v13** (2024말~2025): Temporal Transformer 기반. 공식 릴리스 노트 기준 **모델 크기·context 3×, 데이터 4.2×, 학습 컴퓨트 5×**. 커뮤니티 분석 기준 주행 네트워크 메모리 footprint **v12 ~2.3GB → v13 ~7.5GB** (estimated — 리버스엔지니어링 기반), HW4에서 FP16 native 실행, HW3 실행 불가 격차 발생 ([Creative Strategies](https://creativestrategies.com/research/tesla-ai-autonomy-fsd-v13-update/), [shop4tesla](https://www.shop4tesla.com/en/blogs/news/tesla-fsd-v13-hw4-hw3-limit)).
- **중국 OEM은 E2E 전면 전환 단계**: Momenta가 중국 city-NOA 솔루션 60% 공급(2024), 서드파티 urban NOA 점유율 65%(2025–26), BMW 차세대 iX3(2026)에 E2E 대모델 탑재 예정 ([Recode China AI](https://www.recodechinaai.com/p/tesla-fsds-toughest-competition-comes), [CarNewsChina](https://carnewschina.com/2025/11/17/bmw-and-one-of-chinas-top-autonomous-driving-companies-momenta-partner-to-debut-its-next-gen-bmw-ix3-in-2026/)).

### 3.3 VLM/VLA 기반 주행 — "fast + slow" 이중 시스템

- **DriveVLM-Dual** (Tsinghua × Li Auto, [arXiv:2402.12289](https://arxiv.org/abs/2402.12289)): 느린 VLM(long-tail 상황 추론) + 빠른 E2E의 dual-system. 실차에서 **OrinX 2개에 분산** — OrinX-1에 고주기 E2E, OrinX-2에 VLM. VLM 추론 **평균 410ms on OrinX** (speculative decoding으로 decode 2.7× 가속). → **"VLM은 10Hz 제어 루프에 못 들어가므로 slow-path로 격리"가 현재 표준 패턴.**
- **Li Auto MindVLA** (GTC 2025): 자체 설계 base LLM — MoE 8-expert + sparse attention. Orin/Thor에서 **약 2,000개 모델 구성을 정확도-지연 트레이드오프로 탐색**해 배포 구성 결정. 2025년 L-시리즈에 Thor-U(730 TOPS) 채택 ([Automotive World](https://www.automotiveworld.com/articles/gtc-li-auto-unveils-mindvla-autonomous-driving-architecture/)).
- **XPeng VLA 2.0** (2025-11): 언어 토큰 단계를 제거한 "Vision-Implicit Token-Action". **30B 파라미터 VLA를 차량 로컬 실행** — 자체 Turing 칩 3개(2,250 TOPS, 2개 VLA + 1개 cockpit). **Volkswagen이 라이선스 파트너** ([XPeng 공식](https://www.xpeng.com/pressroom/news/019a56f54fe99a2a0a8d8a0282e402b7), [VW 채택](https://eletric-vehicles.com/xpeng/volkswagen-to-adopt-xpengs-autonomous-driving-solution-vla-2-0/)).
- **Waymo EMMA** (2024-10): Gemini 기반 E2E multimodal — 단 Waymo 스스로 "소수 프레임 처리, LiDAR 미통합, 연산 비용 과다"를 명시한 **연구 단계** ([Waymo Blog](https://waymo.com/blog/2024/10/introducing-emma/), [arXiv:2410.23262](https://arxiv.org/abs/2410.23262)).
- **노선 분화 (2025 중국)**: VLA 노선(XPeng, Li Auto) vs **World Model 노선(Huawei ADS 4.0 — WEWA 아키텍처, MoE 기반 World Action 모델, MDC 1000/1,000 TOPS)** ([EEWorld](https://en.eeworld.com.cn/news/qcdz/eic695593.html), [36Kr](https://eu.36kr.com/en/p/3730949951091202)).

### 3.4 World Model (주로 학습/시뮬레이션 인프라 측)

- **Wayve GAIA-1**(9B+ 파라미터, 2023) → **GAIA-2**(latent diffusion, 2025) → **GAIA-3**(15B, 오프라인 안전 평가용) ([Wayve](https://wayve.ai/thinking/gaia-3/))
- **NVIDIA Cosmos** (CES 2025): World Foundation Model 플랫폼, 4B~13B 변형, 2,000만 시간 영상(9,000조 토큰) 학습 ([arXiv:2501.03575](https://arxiv.org/abs/2501.03575))
- world model은 기본적으로 **데이터센터 워크로드**이나, Huawei WA처럼 차량측 추론으로 내려오는 흐름이 있음.

### 3.5 ★ 핵심 논점: 왜 Transformer/VLA는 TOPS보다 메모리 대역폭을 압박하는가

- CNN perception: conv 커널의 **재사용률이 높아 arithmetic intensity(OPS/byte)가 높음** → MAC array(TOPS)가 병목.
- 차량 내 LLM/VLA 추론: **batch-1 autoregressive decode** — 매 토큰마다 전체 weight + KV cache를 DRAM에서 스트리밍 → arithmetic intensity가 machine balance point 아래로 떨어져 **연산기가 놀고 step time이 메모리 대역폭으로 결정됨** ([arXiv:2605.30571](https://arxiv.org/abs/2605.30571)). Attention 레이어는 matrix-vector 위주로 본질적으로 memory-bound ([SparQ, arXiv:2312.04985](https://arxiv.org/pdf/2312.04985)).
- **정량 근거**: 2019→2026 사이 차량 SoC TOPS는 ~30 → 2,000+ (약 70×) 증가했으나, 온보드 메모리 대역폭은 ~68 → 273 GB/s (약 4×) 증가에 그침. **대역폭이 스케일링 병목.**
- 실리콘 방증: Tesla AI5는 GDDR6/7 12패키지로 **768GB/s~1.5TB/s 추정 대역폭** 확보 설계 ([Tom's Hardware, 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-demonstrates-first-sample-of-tesla-ai5-processor-accidentally-thanks-tsc-rather-than-tsmc-claims-40x-performance-boost-over-the-predecessor)).

---

## 4. 차량 탑재(온보드) 최적화 연구 동향 (20분)

> 큰 모델을 차량용 SoC에 올리기 위한 기법들 — 각 기법이 **하드웨어에 무엇을 요구하는지**에 주목.

### 4.1 양자화 (Quantization)

**PTQ vs QAT**: PTQ(post-training)는 calibration 데이터만으로 수 분~수 시간 내 변환 — 산업 주류. 공격적 저정밀(W4A8 등)은 대부분 QAT(재학습) 필요 ([LLM 양자화 종합평가, arXiv:2507.17417](https://arxiv.org/html/2507.17417)).

자율주행 인지 모델 사례:
- **LiDAR-PTQ** (ICLR 2024): CenterPoint INT8 PTQ에서 FP32 동급 정확도 + **3× 추론 가속**, QAT 대비 **30× 빠른 양자화** ([arXiv:2401.15865](https://arxiv.org/pdf/2401.15865))
- **Q-PETR**: multi-view 3D detection 8-bit PTQ에서 <1% 열화, 2× 속도, 3× 메모리 절감 ([논문](https://www.researchgate.net/publication/389750123_Q-PETR_Quant-aware_Position_Embedding_Transformation_for_Multi-View_3D_Object_Detection))

**저정밀 포맷 전쟁 — INT8 vs FP8 vs FP4**:
- Qualcomm AI Research의 반론: 전용 하드웨어에서 **FP8 MAC은 INT8 대비 면적/에너지 효율이 50~180% 나쁨** ([arXiv:2303.17951](https://arxiv.org/pdf/2303.17951)) — NPU 진영(Qualcomm, Horizon)이 INT 중심, GPU 진영(NVIDIA)이 FP 중심인 구도의 이론적 배경.
- **NVFP4** (Blackwell): block-scaled 4-bit float. FP8→NVFP4 변환 시 **<1% 정확도 손실**, FP8 대비 **~3× 처리량, 메모리 트래픽 절반**. INT4와 달리 dequantization 병목 없이 하드웨어 네이티브 가속 ([NVIDIA](https://build.nvidia.com/spark/nvfp4-quantization)).
- **W4A8**: 처리량 최상위이나 대형 모델에서 최대 22% 품질 손실 사례 — 태스크별 검증 필수 ([arXiv:2508.16712](https://arxiv.org/html/2508.16712v1)).
- 하드웨어 지원: NVIDIA DRIVE Thor **2,000 FP4 TFLOPS** (FP4/FP8 Transformer Engine), DriveOS LLM SDK는 weight/GEMM에 FP8·NVFP4, LayerNorm·KV cache·attention은 FP16 유지하는 mixed-precision 레시피 ([DriveOS LLM SDK](https://developer.nvidia.com/blog/streamline-llm-deployment-for-autonomous-vehicle-applications-with-nvidia-driveos-llm-sdk/)).

> 💡 "INT8은 인지 모델의 안전한 기본값, FP8/FP4는 Transformer/LLM 워크로드의 새 기본값"으로 이원화 진행 중. **포맷 선택이 곧 실리콘 벤더 선택이 되는 lock-in** 문제도 논의 필요.

### 4.2 프루닝 · 구조적 희소성 · 지식 증류

**2:4 Structured Sparsity**:
- NVIDIA Ampere 이후 Sparse Tensor Core: 이론상 GEMM 2× — 실측은 LLM 기준 **1.40–1.44×** ([LLMCBench](https://arxiv.org/pdf/2410.21352)), sparse+INT8 CNN 워크플로우 **~1.7×** ([NVIDIA](https://developer.nvidia.com/blog/sparsity-in-int8-training-workflow-and-best-practices-for-tensorrt-acceleration)).
- **Orin DLA도 channel 2:4 sparsity를 하드웨어 지원** — DLA 합산 105 TOPS(INT8 sparse) ([NVIDIA DLA SW](https://github.com/NVIDIA/Deep-Learning-Accelerator-SW/blob/main/README.md)). 고정기능 가속기에도 sparsity가 전력 효율에 유효함이 입증됨.

**지식 증류 (Knowledge Distillation)**:
- **Cross-modal BEV 증류 (LiDAR teacher → camera student)**: 값비싼 LiDAR의 기하 지식을 카메라 전용 모델에 이식 → **센서 BOM 절감**이 산업적 동기. DistillBEV +3.9% mAP ([ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_DistillBEV_Boosting_Multi-Camera_3D_Object_Detection_with_Cross-Modal_Knowledge_Distillation_ICCV_2023_paper.pdf)), SimDistill +4.8% mAP ([AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/28577/29122)).
- **DistillDrive** (ICCV 2025): planning teacher → E2E student 다단계 증류 ([arXiv:2508.05402](https://arxiv.org/abs/2508.05402)).
- **NVIDIA Minitron**: 15B→8B/4B structured pruning + 증류, 처음부터 학습 대비 **40× 적은 학습 토큰** — 온디바이스용 소형 LLM 확보의 대표 레시피 ([arXiv:2407.14679](https://arxiv.org/abs/2407.14679)).
- **산업 침투 사례 (2025)**: DeepSeek-R1 증류 모델이 Geely(StarRui dual-brain)·BYD·Zeekr·Leapmotor 등 cockpit에 오프라인 동작 가능한 소형 모델로 탑재 ([Inside China Auto](https://insidechinaauto.com/2025/02/08/chinese-carmakers-integrate-deepseek-into-infotainment-systems/)).

### 4.3 효율적 아키텍처 설계

- **Fast-BEV++**: custom CUDA plugin을 제거한 view transformation — **TensorRT-native, zero custom plugin**, NDS 0.478 @ ~90ms FP16 ([arXiv:2512.08237](https://arxiv.org/html/2512.08237)). → **"deployable by design"**: 배포 스택(지원 연산자, 커널)이 아키텍처 설계의 1차 제약.
- **BEVFusion** (MIT): BEV pooling 최적화로 view transformation 지연 40×+ 감소, TensorRT ~20Hz ([GitHub](https://github.com/mit-han-lab/bevfusion)).
- **NAS**: hardware-aware NAS(지연·에너지·메모리 동시 최적화) 활발 — 단 실무는 full NAS보다 "**타깃 NPU의 지원 연산자 집합 안에서의 설계**"가 지배적.
- **Token pruning/merging**: ToMe는 ViT throughput ~2× (손실 0.2–0.3%) ([arXiv:2210.09461](https://arxiv.org/abs/2210.09461)). 주행 특화로는 **FastDriveVLA** (XPeng×북경대, AAAI 2026): visual token 3,249→812로 **연산 ~7.5× 절감**, nuScenes planning SOTA 유지 ([arXiv:2507.23318](https://arxiv.org/abs/2507.23318)) — 일반 VLM용 pruning이 주행 시나리오에서 성능이 나쁘다는 발견이 출발점.

### 4.4 온디바이스 LLM/VLM 추론 최적화

- **DriveOS LLM SDK** (DriveOS 7): TensorRT 기반 순수 C++ 경량 LLM 런타임. FP16/FP8/INT4(AWQ)/NVFP4 + **speculative decoding, KV caching, LoRA, dynamic batching**, Llama·Qwen 네이티브 지원 ([NVIDIA](https://developer.nvidia.com/blog/streamline-llm-deployment-for-autonomous-vehicle-applications-with-nvidia-driveos-llm-sdk/)).
- **Speculative decoding**: TensorRT-LLM에서 Llama-3.3-70B ~3×, EAGLE-3 최대 4.79× ([NVIDIA](https://developer.nvidia.com/blog/boost-llama-3-3-70b-inference-throughput-3x-with-nvidia-tensorrt-llm-speculative-decoding), [Red Hat](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding)). Li Auto 실차에서는 OrinX용 최적화로 EAGLE 2.7× decode 가속 ([DriveVLM](https://arxiv.org/html/2402.12289v4)).
- **cabin + ADAS 동시 수용**: Thor는 **MIG(Multi-Instance GPU)로 graphics/compute 도메인 격리** — time-critical ADAS와 cockpit 워크로드 동시 실행을 하드웨어 수준 보장, Linux+QNX+Android 동시 구동 ([NVIDIA](https://blogs.nvidia.com/blog/drive-thor/)).

### 4.5 컴파일러·런타임 스택

- **ONNX Runtime + 벤더 Execution Provider**가 사실상 공통 배포 계층 — 그래프 자동 partitioning, NPU 미지원 연산자는 CPU fallback ([Qualcomm docs](https://docs.qualcomm.com/doc/80-70029-15B/topic/run-an-onnx-model-using-ort.html)).
- Qualcomm: SNPE → **QNN/QAIRT** 세대교체. NVIDIA: TensorRT (DLA는 INT8/FP16만, calibration 필수). Horizon: **BPU Nash + 자체 컴파일러 + 알고리즘의 3축** ([Horizon](https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6)). XPeng은 자체 칩에 **자체 컴파일러를 재개발**.
- 시장: automotive NPU $2.2B(2024) → $17.1B(2034) 전망 ([GM Insights](https://www.gminsights.com/industry-analysis/automotive-neural-npu-market)).

> 💡 **"모델 최적화 기법의 절반은 컴파일러 문제"** — custom plugin 없는 TensorRT-native 설계, NPU 연산자 커버리지, CPU fallback 비용이 실제 latency를 좌우한다. **연산자 커버리지·양자화 툴체인 없는 NPU TOPS는 무의미.**

---

## 5. 워크로드 정량화 — 숫자로 보는 요구사항 (15분)

### 5.1 센서 스위트와 raw 대역폭

| 시스템 | 구성 | 출처 |
|---|---|---|
| Tesla HW4 (L2+) | 카메라 8대, 1.2MP→~5MP 업그레이드 | [AutoPilot Review](https://www.autopilotreview.com/tesla-hardware-4-rolling-out-to-new-vehicles/) |
| Waymo 6세대 (L4) | 카메라 13대(17MP) + LiDAR 4 + radar 6 — 5세대 대비 센서 42% 감축 | [Waymo Blog](https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/) |
| Mercedes DRIVE PILOT (인증 L3) | 35개+ 센서 (카메라·radar·초음파·LiDAR), 제동/조향/전원 이중화, 95km/h 승인 | [Mercedes 공식](https://group.mercedes-benz.com/technology/autonomous-driving/driving/drive-pilot-95-kmh.html) |

raw 대역폭:
- 카메라 1대: **479 Mbps ~ 1.8 Gbps** (실측 기반, [arXiv:2301.06422](https://arxiv.org/pdf/2301.06422)) → 11카메라급이면 카메라만 수~수십 Gbps
- LiDAR: Ouster OS2 ~240Mbps, 128ch 최대 ~250Mbps ([arXiv:1912.01080](https://arxiv.org/pdf/1912.01080), [Ouster](https://ouster.com/insights/blog/the-anatomy-of-an-autonomous-vehicle))
- 4D radar: point cloud면 ~4.8MB/s에 불과하나 **raw ADC 중앙 처리 시 5대 합산 ~540MB/s(≈4.3Gbps)** ([NVIDIA](https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy/))
- 차량 1대당 수집 데이터 ~4,000GB/day 규모 ([Label Your Data](https://labelyourdata.com/articles/autonomous-vehicle-data-collection))

### 5.2 주요 SoC — TOPS와 메모리 대역폭

| 칩 | AI 성능 (precision 주의) | 메모리 대역폭 | 시점 |
|---|---|---|---|
| NVIDIA Orin | 254 TOPS (INT8 sparse) | LPDDR5 **204.8 GB/s** | 2022 양산 |
| NVIDIA Thor | **1,000 TOPS INT8 = 2,000 TFLOPS FP4** | LPDDR5X **273 GB/s** | 2025 양산 |
| Tesla HW4 | ~243 TOPS (추정) | GDDR6 **224 GB/s** | 2023 |
| Tesla AI5 | AI4 대비 실질 5–8× | **768GB/s–1.5TB/s 추정** | 2027 목표 |
| XPeng Turing | 750 TOPS/칩 × 3칩 = 2,250 TOPS | 미공개 | 2025 |
| NIO NX9031 | 1,000+ TOPS (자체 발표) | 미공개 | 2025 |
| Horizon J6P | 560 TOPS | 미공개 | 2025 |
| Mobileye EyeQ6H | **34 TOPS** (2칩으로 SuperVision 구동) | LPDDR5 | 2025 |
| (메모리 산업) automotive LPDDR5X | — | 256-bit 기준 **307.2 GB/s** 공급 가능 ([Samsung](https://semiconductor.samsung.com/us/news-events/tech-blog/samsungs-12nm-class-automotive-lpddr5x-dram-for-safety-critical-centralized-automotive-systems)) | — |

> ⚠️ 벤더 TOPS는 precision(INT8/FP8/FP4, dense/sparse) 기준이 제각각 — 비교 시 반드시 precision 병기. 중국 벤더·Tesla 수치는 자체 발표/추정 기반.

### 5.3 Latency 정량 요약

| 워크로드 | 지연 | 출처 |
|---|---|---|
| E2E(sensing→actuation) 예산 | ~100ms (10–12Hz) | ASPLOS 2018, arXiv:2207.08930 |
| BEVFormer류 perception (배포 최적화) | 25–90ms | arXiv:2203.17270, MulticoreWare |
| Tesla occupancy network | ~10ms | arXiv:2303.01212 |
| 온보드 VLM (slow path) | ~410ms on OrinX | DriveVLM, arXiv:2402.12289 |
| LLM decode 상한 | 대역폭/모델크기로 결정 (273 GB/s ÷ 1GB 모델 ≈ 273 tok/s) | Memory Bandwidth Ladder |

---

## 6. HPC 설계 시사점 종합 (10분 + 토론)

1. **워크로드가 compute-bound에서 memory-bound로 이동** — 차기 플랫폼의 1차 차별화 요소는 TOPS가 아니라 **DRAM 대역폭, 온칩 SRAM, KV cache 처리 능력, FP8/FP4 datapath**. 메모리 티어링(용량 = 모델 상주, 대역폭 = decode, 연산 = prefill)의 3축 균형으로 사양을 정할 것.
2. **저정밀 포맷 로드맵을 워크로드 믹스로 결정**: CNN 인지 중심이면 INT8+INT4, VLA/LLM 중심이면 FP8/FP4 필수. per-block scaling(NVFP4류) 지원 여부가 정확도-효율의 관건. FP4 네이티브 가속이 없으면 dequant 오버헤드로 4-bit 이득이 사라짐.
3. **Sparsity는 "이론 2×, 실측 1.3–1.7×"로 보수적으로 계획** — metadata 오버헤드와 sparse GEMM 메모리 접근 패턴까지 포함해 검증.
4. **이중 시간 스케일 아키텍처가 표준**: 10Hz+ fast path (E2E/BEV, deterministic) + 1–2Hz slow path (VLM ~410ms) — 컴퓨트 파티셔닝·QoS·격리 설계가 필요. speculative decoding은 "작은 모델 + 큰 모델 동시 상주"를, token pruning은 동적 텐서 shape 지원을 요구.
5. **I/O 프런트엔드가 새 병목**: 카메라 10대+ × ~2Gbps + radar raw 4Gbps급 인입을 SerDes/이더넷 백본과 ISP가 흡수해야 함.
6. **tail latency와 mixed-criticality**: 평균이 아닌 p99 결정성. LLM의 대역폭 폭식이 인지 파이프라인 deadline을 침해하지 않도록 **메모리 QoS/대역폭 파티셔닝** 필수 (→ 2회차에서 상세).
7. **컴파일러 생태계가 실리콘의 가치를 결정**: 신규 가속기 설계 시 ONNX Runtime EP 등 표준 계층과의 접점을 1일차부터 계획.

### 토론 주제 제안

- 우리 타깃 워크로드 믹스(인지 vs VLA/LLM 비중)에서 저정밀 포맷 우선순위는?
- 273 GB/s급 대역폭으로 어느 규모의 온보드 모델까지 감당 가능한가? 차기 세대 목표 대역폭은?
- fast/slow path 분리를 단일 SoC 파티셔닝으로 할 것인가, 별도 칩으로 할 것인가?

---

## 부록: 전체 출처

**파이프라인/지연**: [ASPLOS 2018](https://dl.acm.org/doi/10.1145/3173162.3173191) · [arXiv:2207.08930](https://arxiv.org/pdf/2207.08930) · [arXiv:2112.14947](https://arxiv.org/pdf/2112.14947) · [COLA arXiv:2305.07147](https://arxiv.org/pdf/2305.07147) · [arXiv:2504.12813](https://arxiv.org/pdf/2504.12813)

**BEV/E2E/VLA/World Model**: [BEVFormer](https://arxiv.org/pdf/2203.17270) · [MulticoreWare](https://multicorewareinc.com/optimized-bev-models-for-real-time-autonomous-perception-bevdet-bevformer/) · [HotBEV](https://openreview.net/forum?id=3Cj67k38st) · [Fast-BEV](https://arxiv.org/pdf/2301.12511) · [Occupancy survey](https://arxiv.org/pdf/2303.01212) · [UniAD](https://arxiv.org/abs/2212.10156) · [FSD v13 분석](https://creativestrategies.com/research/tesla-ai-autonomy-fsd-v13-update/) · [DriveVLM](https://arxiv.org/abs/2402.12289) · [OpenDriveVLA](https://arxiv.org/abs/2503.23463) · [Waymo EMMA](https://waymo.com/blog/2024/10/introducing-emma/) · [MindVLA](https://www.automotiveworld.com/articles/gtc-li-auto-unveils-mindvla-autonomous-driving-architecture/) · [XPeng VLA 2.0](https://www.xpeng.com/pressroom/news/019a56f54fe99a2a0a8d8a0282e402b7) · [Huawei ADS 4.0](https://en.eeworld.com.cn/news/qcdz/eic695593.html) · [Wayve GAIA-3](https://wayve.ai/thinking/gaia-3/) · [NVIDIA Cosmos](https://arxiv.org/abs/2501.03575)

**Memory-bound 논거**: [arXiv:2605.30571](https://arxiv.org/abs/2605.30571) · [SparQ](https://arxiv.org/pdf/2312.04985) · [Tesla AI5](https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-demonstrates-first-sample-of-tesla-ai5-processor-accidentally-thanks-tsc-rather-than-tsmc-claims-40x-performance-boost-over-the-predecessor)

**최적화**: [LiDAR-PTQ](https://arxiv.org/pdf/2401.15865) · [FP8vsINT8](https://arxiv.org/pdf/2303.17951) · [NVFP4](https://build.nvidia.com/spark/nvfp4-quantization) · [W4A8 특성화](https://arxiv.org/html/2508.16712v1) · [LLMCBench](https://arxiv.org/pdf/2410.21352) · [Orin DLA](https://github.com/NVIDIA/Deep-Learning-Accelerator-SW/blob/main/README.md) · [DistillBEV](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_DistillBEV_Boosting_Multi-Camera_3D_Object_Detection_with_Cross-Modal_Knowledge_Distillation_ICCV_2023_paper.pdf) · [Minitron](https://arxiv.org/abs/2407.14679) · [DeepSeek 차량 침투](https://insidechinaauto.com/2025/02/08/chinese-carmakers-integrate-deepseek-into-infotainment-systems/) · [Fast-BEV++](https://arxiv.org/html/2512.08237) · [BEVFusion](https://github.com/mit-han-lab/bevfusion) · [ToMe](https://arxiv.org/abs/2210.09461) · [FastDriveVLA](https://arxiv.org/abs/2507.23318) · [DriveOS LLM SDK](https://developer.nvidia.com/blog/streamline-llm-deployment-for-autonomous-vehicle-applications-with-nvidia-driveos-llm-sdk/) · [Speculative decoding](https://developer.nvidia.com/blog/boost-llama-3-3-70b-inference-throughput-3x-with-nvidia-tensorrt-llm-speculative-decoding) · [EAGLE-3](https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding) · [EDGE-LLM](https://arxiv.org/abs/2406.15758) · [Thor MIG](https://blogs.nvidia.com/blog/drive-thor/) · [QNN/QAIRT](https://docs.qualcomm.com/doc/80-70029-15B/topic/run-an-onnx-model-using-ort.html) · [Horizon J6](https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6) · [NPU 시장](https://www.gminsights.com/industry-analysis/automotive-neural-npu-market)

**센서/대역폭/SoC**: [arXiv:2301.06422](https://arxiv.org/pdf/2301.06422) · [arXiv:1912.01080](https://arxiv.org/pdf/1912.01080) · [Ouster](https://ouster.com/insights/blog/the-anatomy-of-an-autonomous-vehicle) · [NVIDIA radar 중앙화](https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy/) · [Waymo 6세대](https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/) · [Mercedes DRIVE PILOT](https://group.mercedes-benz.com/technology/autonomous-driving/driving/drive-pilot-95-kmh.html) · [Orin Brief](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf) · [Thor 개발자 문서](https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf) · [Tesla HW4](https://grokipedia.com/page/Tesla_Hardware_4) · [Samsung automotive LPDDR5X](https://semiconductor.samsung.com/us/news-events/tech-blog/samsungs-12nm-class-automotive-lpddr5x-dram-for-safety-critical-centralized-automotive-systems) · [Mobileye EyeQ6](https://www.mobileye.com/blog/the-fast-lane-to-higher-levels-of-autonomy-with-the-eyeq6-soc/) · [Huawei MDC](https://www.huawei.com/en/huaweitech/publication/86/driverless-vehicles-with-MDC) · [Yano Research](https://www.yanoresearch.com/press/press.php/3969) · [GMI zonal](https://www.gminsights.com/industry-analysis/automotive-zonal-architecture-domain-controller-market)
