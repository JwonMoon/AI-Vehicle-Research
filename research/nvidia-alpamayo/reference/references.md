# NVIDIA Alpamayo 리서치 — 레퍼런스 기록

- **작성일(접근일)**: 2026-07-15 (KST)
- **수집 방법**: deep-research 멀티에이전트 워크플로(검색 5각도 → 19개 소스 fetch → 주장 95건 추출 → 교차검증 투표) + 핵심 수치 8건 당일 직접 재확인(WebFetch)
- **원시 기록**: [deep_research_claims_raw.json](deep_research_claims_raw.json) — 소스별 주장·원문 인용 전문
- **영상 자막**: [youtube_Alpamayo 2 Super](youtube_Alpamayo%202%20Super) — 공식 라이브스트림 자막(사용자 제공, ASR 오탈자 다수)

## 검증 등급 정의

| 등급 | 의미 |
|---|---|
| ✅ 교차검증 | 독립된 복수 소스 일치 (및/또는 워크플로 검증 투표 통과 + 직접 재확인) |
| 🔍 직접 확인 | 해당 원문 페이지를 2026-07-15에 직접 fetch해 문장 확인 |
| 📄 발췌 확보 | 워크플로 fetch 에이전트의 원문 인용만 확보 (당일 재확인 안 함) |
| 🎥 영상 발언 | 라이브스트림 자막에만 존재 (문서 소스 미확인) |

## 접근 실패·미확인 항목 (문서 앞 명시)

- YouTube 영상 페이지의 **라이브 방송 날짜**: fetch 시 제목만 노출, 날짜 확인 불가. 제목 확인됨: "Alpamayo 2 Super: The Open Reasoning Model for Robotaxis"
- **LingoQA 리더보드**(Alpamayo 1.5 "1위" 주장): 리더보드 자체 미접근 — 영상 발언 + 모델카드 점수(74.2)만 확인
- **nvidia/Cosmos3-Super-Reasoner** HF repo: HF 블로그 내 링크로만 확인, repo 직접 미접근
- **aibusiness Mercedes CLA 기사**(https://aibusiness.com/intelligent-automation/nvidia-s-ai-driving-tech-debuts-in-mercedes-cla-by-2026): HTTP 403 — Alpamayo 명시 여부 확인 불가, 보고서에서 인용 보류 처리
- deep-research 워크플로가 세션 한도로 검증 투표 25건 중 19건 중단 → 해당 주장은 당일 직접 재확인으로 보완(위 등급 표기)

---

## 1. NVIDIA 공식 — 제품/보도

### 1.1 NVIDIA Alpamayo 솔루션 페이지 ✅
- URL: https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/
- 유형: 공식 제품 허브(날짜 미표기, CES 2026 영상·GTC Taipei 2026 뉴스 링크 포함)
- 확인 사실:
  - "It's available in 10 B parameters with Alpamayo 1 Nano and 1.5 Nano, and scales to 32 B with Alpamayo 2 Super." (검증 투표 2-0)
  - "Alpamayo 2 Super is a 32 billion-parameter reasoning-based vision language action (VLA) model. It extends the NVIDIA Alpamayo family ... for safe robotaxi (Level 4) development." (2-0)
  - "built on NVIDIA Cosmos™ and processes multi-camera video, navigation inputs, and driving context to generate trajectories and Chain-of-Causation reasoning traces." (3-0)
  - AlpaGym = "high-throughput closed-loop RL training framework", AlpaSim = "open-source closed-loop AV simulation framework" (3-0)
  - ⚠️ 이 페이지는 "32 B"로 표기 — 보도자료(34B)와 충돌. §미확인 참조.

### 1.2 CES 2026 보도자료 — Alpamayo 플랫폼 발표 📄
- URL: https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development
- 날짜: 2026-01-05
- 확인 사실(발췌):
  - "With a 10-billion-parameter architecture, Alpamayo 1 uses video input to generate trajectories alongside reasoning traces"
  - 공개 범위: "open model weights and open-source inferencing scripts"
  - 예고: "Future models in the family will feature larger parameter counts, more detailed reasoning capabilities, more input and output flexibility, and options for commercial usage."
  - AlpaSim 공개(GitHub), 1,700+시간 오픈 데이터셋, 관심 파트너: Lucid, JLR, Uber, Berkeley DeepDrive

### 1.3 GTC Taipei 보도자료 — Alpamayo 2 Super 발표 🔍
- URL: https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis
- 날짜: 2026-05-31
- 직접 확인(2026-07-15):
  - **"34-billion-parameter reasoning-based vision language action (VLA) model"** — 본문 2회 명시
  - 이전 세대 명칭: "NVIDIA Alpamayo 1 Nano and NVIDIA Alpamayo 1.5 Nano" (10B)
  - Meta-Action: "Adds Meta-Action output — including macro actions such as yield, lane change and stop — so the model predicts high-level driving decisions"
  - Auto-labeling: "reasoning auto-labeling with 2D grounding so the 34-billion-parameter foundation model can provide high-quality reasoning labels, compressing annotation cycles from months to days"
  - 릴리스: "expected to be available this summer on GitHub for inference code and Hugging Face for model weights"
  - 누적 다운로드: "downloaded close to 400,000 times"
  - teacher 모델 → distill → NVIDIA DRIVE AGX Thor 차량 탑재 구도 (발췌)
  - AlpaGym(AlpaSim 내 closed-loop) + OmniDreams(포토리얼 시나리오 생성) 소개 (발췌)

### 1.4 GTC Taipei / COMPUTEX 2026 뉴스 블로그 📄
- URL: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
- 날짜: 2026-05-21 시작, 섹션별 타임스탬프 ~05-31
- 확인 사실(발췌):
  - 05-31 8:00pm PT 섹션: "NVIDIA introduced Alpamayo 2 Super, an open AV reasoning model..."
  - "Alpamayo 2 is paired with AlpaGym ... and OmniDreams, which can generate photorealistic driving scenarios"
  - 05-21 섹션: **COMPUTEX 2026 Best Choice Awards — "NVIDIA Alpamayo won the Vehicle Technology and Smart Cockpit Category Award"**
  - 발표 직전까지 플랫폼 구성 = Alpamayo 1/1.5(10B) + AlpaSim + Physical AI Open Datasets(1,700+시간)

### 1.5 NeurIPS 2025 블로그 — Alpamayo-R1 최초 공개 📄
- URL: https://blogs.nvidia.com/blog/neurips-open-source-digital-physical-ai/
- 날짜: 2025-12-01
- 확인 사실(발췌):
  - "NVIDIA DRIVE Alpamayo-R1 (AR1), the world's first open reasoning VLA model for AV research"
  - 기반: "AR1's open foundation, based on NVIDIA Cosmos Reason"
  - GitHub·Hugging Face 공개 + Physical AI Open Datasets 일부 데이터 공개
  - AlpaSim도 AR1 평가용으로 함께 공개 → **AlpaSim은 CES 이전, NeurIPS 2025 시점부터 존재**

## 2. NVIDIA 공식 — 기술 블로그/모델카드/코드

### 2.1 developer blog: "Building Autonomous Vehicles That Reason" ✅
- URL: https://developer.nvidia.com/blog/building-autonomous-vehicles-that-reason-with-nvidia-alpamayo/
- 날짜: 2026-01-05 (저자 Marco Pavone, 태그 CES26)
- 확인 사실:
  - Alpamayo 1 = "an open, 10B reasoning VLA model" (검증 3-0)
  - 가중치 HF nvidia/Alpamayo-R1-10B + 코드 GitHub NVlabs/alpamayo (3-0)
  - Physical AI AV Dataset: "1,727 hours ... 25 countries and over 2,500 cities ... 310,895 clips ... 20 seconds ... multi-camera and LiDAR coverage for all clips, radar coverage for 163,850 clips" (발췌 📄)
  - AlpaSim 마이크로서비스 구조(Driver/Renderer/TrafficSim/Controller/Physics), ~900 NuRec 재구성 씬, DrivingScore 지표 (발췌 📄)

### 2.2 developer blog: "How to Post-Train AV Models in Closed Loop" (AlpaGym) 📄
- URL: https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/
- 날짜: 2026-06-01 UTC 게시(페이지 표기 May 31, 2026), 2026-06-22 수정
- 확인 사실(발췌):
  - AlpaGym = AlpaSim 마이크로서비스 + Physical AI Open Datasets + Cosmos-RL 결합한 closed-loop RL post-training 파이프라인
  - 지원 모델: Alpamayo 1.5 10B(현재 유일), 변환 툴 경로 `packages/policies/alpamayo_r1/` (R1 코드베이스 기반 증거)
  - 자원: GPU ≥40GB VRAM 권장, 디스크 100–150GB(가중치 ~21GB 포함), NuRec 씬당 ~1.5GB, public_2601 전체 ~1.5TB, 10B 학습은 GPU 2장(스모크 테스트 "2x 50GB RTX 6000 Ada" 표기), distillation 스크립트 예정
  - CVPR 2026 챌린지 2종: AlpaSim Closed-Loop E2E Driving Challenge / Physical AI AV Reasoning Challenge (HF Spaces 리더보드)

### 2.3 HF 블로그(Marco Pavone): "NVIDIA Alpamayo" (플랫폼 런치) 📄
- URL: https://huggingface.co/blog/drmapavone/nvidia-alpamayo
- 날짜: 2026-01-05
- 확인 사실(발췌): 오픈 생태계(모델+시뮬레이션+데이터셋) 발표문. Alpamayo 1 = 10B CoT reasoning VLA, Cosmos-Reason 백본. 데이터셋 1,727시간/300,000+클립/25개국/2,500+도시, 전 클립 카메라+LiDAR, 절반 이상 radar. AlpaSim 900+ 재구성 시나리오.

### 2.4 HF 블로그(Marco Pavone): "NVIDIA Alpamayo 2" 🔍
- URL: https://huggingface.co/blog/drmapavone/nvidia-alpamayo-2
- 날짜: 2026-06-01
- 직접 확인(2026-07-15):
  - **"built on the Cosmos 3 Super Reasoner 32-billion parameter VLM backbone"** — 32B는 **백본** 수치. 전체 파라미터 수는 이 글에 미명시
  - "3x the number of parameters as prior Alpamayo models"
  - 카메라: "Expands from front-focused cameras to 360-degree situational awareness across front, side and rear views" — **카메라 개수 미명시**
  - Meta-Action outputs(yield, lane change, stop), reasoning auto-labeling with 2D grounding
  - AlpaGym = open source, high-throughput, closed-loop RL framework
  - 가중치·추론 코드 "coming summer 2026"
  - (워크플로 발췌) Computex 2026 Best Choice Award, 다운로드 400,000+, 링크: nvidia/PhysicalAI-Autonomous-Vehicles, nvidia/PhysicalAI-Autonomous-Vehicles-NuRec, nvidia/Cosmos3-Super-Reasoner

### 2.5 HF 모델카드: nvidia/Alpamayo-R1-10B (= Alpamayo 1) 🔍
- URL: https://huggingface.co/nvidia/Alpamayo-R1-10B
- HF 릴리스: 2025-12-03
- 직접 확인(2026-07-15):
  - "Following the release of NVIDIA Alpamayo at CES 2026, Alpamayo-R1 has been renamed to Alpamayo 1."
  - 구성: Backbone 8.2B + Action Expert 2.3B (Cosmos-Reason 백본 + diffusion 기반 trajectory decoder)
  - 입력: 4카메라(front-wide, front-tele, cross-left, cross-right), 10Hz 0.4초 히스토리(카메라당 4프레임), 다운샘플 후 320×576, egomotion 히스토리
  - 출력: CoC reasoning + 6.4초 미래 궤적(64 waypoints @10Hz, 위치+회전)
  - 학습 데이터: 80,000시간 멀티카메라 영상, 700,000 CoC reasoning traces (hybrid: 인간 구조화 CoC + VLM auto-labeling)
  - 벤치마크: AlpaSim Score 0.73±0.01 (PhysicalAI-AV-NuRec 910 시나리오), minADE_6@6.4s 1.22m (937 샘플)
  - 라이선스: 가중치 non-commercial(상업은 별도 요청), 추론 코드 Apache 2.0
  - new_version 프론트매터: nvidia/Alpamayo-1.5-10B (발췌 📄)

### 2.6 HF 모델카드: nvidia/Alpamayo-1.5-10B 🔍
- URL: https://huggingface.co/nvidia/Alpamayo-1.5-10B
- HF 릴리스: 2026-03-19
- 직접 확인(2026-07-15):
  - 백본: **Cosmos-Reason2** + diffusion 기반 action decoder. Backbone 8.2B + Action Expert 2.3B
  - 신규: "support for navigation guidance, flexible camera counts, and user question answering", RL post-trained
  - 학습 데이터: 80,000시간(10억+ 이미지), **CoC traces 3,000,000개** (1.0의 700K 대비 약 4.3배)
  - 벤치마크: LingoQA Lingo-Judge 74.2, AlpaSim Score 0.81±0.01, minADE_6@6.4s 1.11m
  - 라이선스: 가중치 non-commercial + 코드 Apache 2.0 (1.0과 동일 구조)
  - 코드: github.com/NVlabs/alpamayo1.5 (발췌 📄)

### 2.7 GitHub: NVlabs/alpamayo (Alpamayo 1 추론 코드) 🔍
- URL: https://github.com/NVlabs/alpamayo
- repo 생성 2025-11-19, 마지막 push 2026-05-29 (GitHub API, 발췌)
- 직접 확인(2026-07-15):
  - Updates: [January 2026] CES 2026 후 Alpamayo-R1 → Alpamayo 1 개명 / [March 2026] Alpamayo 1.5 릴리스 / [May 2026] fine-tuning·post-training 스크립트 → NVlabs/alpamayo-recipes 이동
  - **공개 10B 모델은 RL post-training 미적용** ("the current 10B model release has not undergone RL post-training"), RL 가중치 미공개
  - 공개 모델에 navigation/route 입력 없음
  - 요구사항: NVIDIA GPU ≥24GB VRAM (RTX 3090/4090, A5000, H100 예시)
  - 라이선스: 코드 Apache 2.0, 가중치 non-commercial
  - (발췌 📄) 가중치 다운로드 ~22GB, gated (Physical AI AV Dataset도 gated)

### 2.8 GitHub: NVlabs/alpagym 📄
- URL: https://github.com/NVlabs/alpagym
- repo 생성 2026-05-19 (GitHub API), 마지막 push 2026-07-08. 라이선스 Apache-2.0
- 확인 사실(발췌):
  - "AlpaGym is a reinforcement-learning framework for end-to-end autonomous-driving policies" — 시뮬레이터 내 closed-loop 실행→채점→학습
  - 구조: AlpaSim = 환경(closed-loop simulator), Cosmos-RL = 트레이너(분산 rollout·학습 오케스트레이션)
  - 알고리즘: GRPO (rollout 아티팩트로 GRPO step → 가중치 rollout worker에 sync)
  - 지원 모델: **Alpamayo 1.5 10B만** (GPU 2장 필요). 1/R1, 2, 2 Super 미지원 명시
  - 상태: "early but active development", 로드맵 = throughput/스케일링, 모델·알고리즘 추가

### 2.9 NVIDIA Research 논문 페이지 📄
- URL: https://research.nvidia.com/labs/avg/publication/wang.luo.etal.arxiv2025/
- 표기: arXiv Preprint, December 2025
- 확인 사실(발췌): 아키텍처·성능 수치 arXiv와 동일 + **off-road rate 35% 감소, close encounter rate 25% 감소** 표기(arXiv 초록의 "close encounter 35%"와 수치 배치 상이 — §미확인 참조), 99ms 실차 레이턴시, 코드 링크

## 3. 논문

### 3.1 arXiv 2511.00088 — Alpamayo-R1 논문 🔍
- URL: https://arxiv.org/abs/2511.00088 (HTML v2: https://arxiv.org/html/2511.00088v2)
- v1: 2025-10-30, v2: 2026-01-07
- 제목: "Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail"
- 직접 확인(2026-07-15, 초록):
  - CoC dataset: "built through a hybrid auto-labeling and human-in-the-loop pipeline"
  - 아키텍처: "modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder"
  - 학습: "supervised fine-tuning to elicit reasoning and reinforcement learning (RL)"
  - 성능: planning accuracy +12%(어려운 케이스), close encounter rate -35%(closed-loop), RL로 reasoning quality +45%·consistency +37%, 0.5B→7B 스케일링 일관 향상, 실차 99ms
  - 공개: HF nvidia/Alpamayo-R1-10B + GitHub NVlabs/alpamayo
  - v2 추가 문구(발췌 📄): "Following the release of NVIDIA Alpamayo at CES 2026, Alpamayo-R1 is also referred to as Alpamayo 1."
  - 3단계 학습 상세(발췌 📄, alphaXiv 경유): Stage 1 Action Modality Injection(이산 궤적 토큰+conditional flow matching action expert) → Stage 2 SFT → Stage 3 GRPO 기반 RL

## 4. 서드파티 (교차검증용)

### 4.1 TechCrunch 📄
- URL: https://techcrunch.com/2026/01/05/nvidia-launches-alpamayo-open-ai-models-that-allow-autonomous-vehicles-to-think-like-a-human/
- 날짜: 2026-01-05
- 교차 확인: CES 2026 런칭, Alpamayo 1 = 10B CoT reasoning VLA, 1,700+시간 데이터셋, AlpaSim GitHub 공개 — 공식 발표와 일치

### 4.2 The Decoder 📄
- URL: https://the-decoder.com/nvidia-bets-big-on-physical-ai-at-gtc-taipei-with-a-new-world-model-driving-brain-and-open-humanoid-robot/
- 날짜: 2026-06-01
- 교차 확인: Alpamayo 2 Super가 1 Nano/1.5 Nano(각 10B) 대체, meta-action(lane change/stop/yield) → downstream planner 전달, CoC를 안전 문서화·규제 검토 용도로 포지셔닝, AlpaGym+OmniDreams 동시 발표, 코드·가중치 여름 공개 예정. ⚠️ 파라미터는 "32 billion"으로 보도(보도자료 34B와 상이)

### 4.3 alphaXiv 요약 📄 (참고용 — AI 생성 요약 포함)
- URL: https://www.alphaxiv.org/overview/2511.00088v2
- 교차 확인: 3단계 학습 구조, GRPO. 세부 수치(10B vs 0.5B: at-fault close encounter 4% vs 9%, AlpaSim score 0.72 vs 0.35)는 AI 요약 유래 — **논문 원문 표와 대조 전 인용 금지**

## 5. 영상

### 5.1 NVIDIA 라이브스트림: "Alpamayo 2 Super: The Open Reasoning Model for Robotaxis" 🎥
- URL: https://www.youtube.com/watch?v=kJRVwaYwvt0 (자막 사본: 본 폴더 `youtube_Alpamayo 2 Super`)
- 방송 날짜: 페이지에서 확인 불가. 내용상 GTC Taipei(5/31) 이후·AlpaGym 공개 당일·CVPR 2026 챌린지 발표 이후 → 2026년 6월 추정 (추정 표시)
- 영상에서만 나온 발언(문서 미확인 → 보고서에 🎥 표기):
  - "7+ 카메라" 360° 서라운드 (문서들은 카메라 수 미명시)
  - Alpamayo 1.5 "LingoQA 1위(number one)", "HF 로보틱스 모델 다운로드 2위"
  - "Alpamayo 2 = Alpamayo 2 Super(모델) + AlpaGym(프레임워크)" 구성 정의
  - 추론 주기: 10Hz reasoning 가능(최적화+템플릿화된 trace 전제), adaptive thinking(CVPR highlight 논문 "counterfactual VLA(발음상)" — 단순 상황은 reasoning 생략)
  - 추론 효율화: speculative decoding, quantization, "DFlash", UCSD 랩 최적화 사례(→ HF의 z-lab/*-DFlash 모델과 부합, 팀 명시 문서 미확인)
  - 배포 옵션: distillation으로 DRIVE Thor 탑재 크기로 축소, distillation recipe "올여름 말" 예정
  - AlpaSim 실행 스택: UV(Python), Rust(cargo, 가속 모듈), Docker, gRPC 서비스, Hydra 설정, Slurm/n-node 배포, ~900 공개 씬
  - AlpaGym 명령 예시: 10B 학습 GPU 2장(학습 1+rollout/sim 1), 향후 2B distill로 단일 GPU 목표
  - Alpamayo 1.5 quantization: FP8/auto-quant PTQ recipe PR 진행 중

## 6. 기타 확인

- HF 모델 검색(2026-07-15 직접 확인 🔍): **Alpamayo-2 / Alpamayo-2-Super 모델 미존재** → 가중치 미공개 상태 확정. nvidia/Alpamayo-R1-10B 다운로드 20.1k, nvidia/Alpamayo-1.5-10B 58.2k (HF 표기 기준 최근 30일 수치). 서드파티 최적화판: z-lab/Alpamayo-1.5-10B, z-lab/Alpamayo-R1-10B-DFlash, z-lab/Alpamayo-1.5-10B-DFlash

## 7. 활용 동향 소스 (2차 조사 추가, 2026-07-15)

### 7.1 PlusAI 채택 발표 🔍
- URL: https://www.plus.ai/news-and-insights/2026-03-16-nvidia-alpamayo
- 날짜: 2026-03-16
- 직접 확인:
  - "Alpamayo foundation model specifically for heavy duty trucking" 적응 진행
  - "A large 10-billion-parameter reasoning Vision-Language-Action (VLA) model is trained using reinforcement learning against safety constraints and traffic rules."
  - teacher→student: 대형 모델이 **500M 파라미터 엣지 모델** 학습 — "reason about complex, novel driving situations without requiring a data center on wheels"
  - 3축 결합: "AI reasoning through the NVIDIA Alpamayo foundation model, hardware-level integration through NVIDIA DRIVE Hyperion and safety through NVIDIA Halos"
  - 협력사: International Motors, Scania, MAN(TRATON), Hyundai Motor Company, Iveco 등

## 8. 타 VLA 비교 소스 (2차 조사 추가, 2026-07-15)

### 8.1 Waymo EMMA 🔍
- URL: https://waymo.com/blog/2024/10/introducing-emma (2024-10)
- "Powered by Gemini". 카메라+텍스트 → "planner trajectories, perception objects, and road graph elements". 오픈소스 언급 없음(논문만). 한계 자인: "EMMA's current limitations in processing long-term video sequences", "not leveraging LiDAR and radar inputs"

### 8.2 Wayve LINGO-2 🔍
- URL: https://wayve.ai/thinking/lingo-2-driving-with-language/ (2024-04-17)
- "첫 closed-loop 공도 테스트 VLAM" 주장. 비전 모델+자기회귀 언어 모델. 입력: 카메라·경로·속도. 출력: 궤적+설명 텍스트/VQA. 가중치 비공개

### 8.3 Li Auto MindVLA 🔍
- URL: https://cnevpost.com/2025/03/18/li-auto-unveils-mindvla-autonomous-driving-architecture/ (2025-03-18)
- NVIDIA GTC 2025에서 공개(발표자 Jia Peng). 자체 개발 LLM(MoE+Sparse Attention, from scratch), 3D 공간 인코더, diffusion으로 액션 토큰→궤적 디코딩, 자체 월드 모델. Li i8(2025-07 출시 예정 시점 기준)부터 적용 계획. 오픈소스 여부 명시 없음(비공개 추정)
- CEO 발언: "MindVLA will redefine autonomous driving in the same way the iPhone 4 redefined smartphones"

### 8.4 OpenEMMA 🔍
- URL: https://github.com/taco-group/OpenEMMA · arXiv 2412.15208 (2024-12)
- "an open-source implementation of Waymo's EMMA". 사용 VLM: GPT-4o, LLaVA-1.6-Mistral-7B, Llama-3.2-11B-Vision-Instruct, Qwen2-VL-7B-Instruct. Apache-2.0. TAMU 주도(저자 이메일 기준 추정)

### 8.5 OpenDriveVLA 🔍
- URL: https://github.com/DriveVLA/OpenDriveVLA (AAAI 2026) · https://ojs.aaai.org/index.php/AAAI/article/view/38386
- "[AAAI 2026] OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model". 0.5B 체크포인트 HF 공개(2025-11-14), Apache-2.0

### 8.6 AutoVLA 📄
- URL: https://arxiv.org/abs/2506.13757
- "AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning" — 제목·초록 수준만 확인, 본문 미검토

## 9. 이미지 출처 기록 (images/ 폴더)

| 파일 | 내용 | 출처 | 다운로드일 |
|---|---|---|---|
| images/ar1_fig1_architecture.png | Alpamayo-R1 아키텍처 개요 (Figure 1) | https://arxiv.org/html/2511.00088v2/x1.png (NVIDIA 논문) | 2026-07-15 |
| images/ar1_fig5_training_pipeline.png | 3단계 학습 파이프라인 (Figure 5) | https://arxiv.org/html/2511.00088v2/figs/train_pipeline.png | 2026-07-15 |
| images/ar1_fig6_rl_posttraining.png | RL post-training 보상 구조 (Figure 6) | https://arxiv.org/html/2511.00088v2/x5.png | 2026-07-15 |
| images/alpagym_closedloop_diagram.png | AlpaGym closed-loop 순환 구조 | https://huggingface.co/blog/drmapavone/nvidia-alpamayo-2 본문 이미지 (https://cdn-uploads.huggingface.co/production/uploads/6954c60c2fcf065716941a7a/ZaVBZtx8fMa7Sbmdlj9vo.png) | 2026-07-15 |
| images/stack_dev_learning.svg | 개발·학습 SW 스택 계층도 (자체 제작 — SW/HW 문서 §4B-A 표 근거 시각화, 실선=확인/점선=추정) | 원출처 없음(자작). 근거: §10.8-0 의존성 파일들 | 2026-07-15 제작 |
| images/stack_vehicle.svg | 차량 탑재 참조 스택 계층도 (자체 제작 — §4B-B 표 근거 시각화, Alpamayo 결합부 점선=추론) | 원출처 없음(자작). 근거: DriveOS·DriveWorks·in-vehicle computing·Thor 블로그·PlusAI | 2026-07-15 제작 |

용도: 개인 리서치 노트 인용(출처 명기). 재배포 시 원 저작권(NVIDIA) 확인 필요.

## 10. SW/HW 요구사항 조사 소스 (3차 조사, 2026-07-15 — 전부 🔍 직접 확인)

### 10.1 GitHub: NVlabs/alpamayo1.5
- URL: https://github.com/NVlabs/alpamayo1.5
- 확인: uv 설치 절차, CUDA Toolkit 12.x + nvcc, Python 3.12, "Tested on an NVIDIA H100 80GB GPU"
- VRAM: 단일 샘플 ~24GB / 16샘플 ~40GB / 16샘플+CFG ~60GB. 가중치 22GB 자동 다운로드
- gated 2건 필요(모델+PhysicalAI 데이터셋), `hf auth login`
- 노트북: 표준 추론/navigation/멀티카메라/VQA. flash-attn 실패 시 `attn_implementation="sdpa"`
- "not a fully fledged driving stack" — 연구·평가 전용 고지. 코드 Apache 2.0/가중치 non-commercial

### 10.2 GitHub: NVlabs/alpamayo-recipes
- URL: https://github.com/NVlabs/alpamayo-recipes
- recipe 4계열: `alpamayo1_sft`·`alpamayo1_5_sft`(HF Trainer+DeepSpeed) / `alpamayo1_x_rl`(Cosmos-RL/GRPO) / `alpamayo1_5_quant`(Model Optimizer Toolkit, FP8, NVFP4+FP8 혼합)
- 유틸: 1↔1.5 체크포인트 변환, PAI 서브셋 큐레이션. GPU 요구는 개별 recipe README로 위임(총괄 수치 없음)
- **distillation recipe 목록에 없음** (2026-07-15 기준)

### 10.3 GitHub: NVlabs/alpasim
- URL: https://github.com/NVlabs/alpasim
- gRPC 마이크로서비스("swap out components"), Python 94.5%+Rust 4%, Docker/UV, `.python-version` 지정
- 렌더러: NuRec(기본, pluggable) + **OmniDreams "FlashDreams" 비디오모델 렌더링**(동적 객체 충실도)
- 배포: Docker Compose 로컬 / `src/tools/run-on-slurm` 멀티노드. Manual Driver(키보드 조작) 가이드 존재
- 씬: HF PhysicalAI-Autonomous-Vehicles-NuRec + repo Git LFS 샘플. Apache 2.0
- GPU 최소 사양 README 명시 없음

### 10.4 GitHub: NVlabs/alpagym
- URL: https://github.com/NVlabs/alpagym
- 패키지: `host`(CLI·config·AlpaSim 셋업)/`runtime`(GPU 컨테이너, rollout+추론)/`policies`/`alpasim_configs`
- "The default 10B Alpamayo model requires two GPUs". 지원: Alpamayo 1.5 10B만. GRPO
- 실행 예: `uv run ... alpagym_host.cli experiment=alpamayo_1_5_local_2gpu_smoke ... reward=progress_safety`
- 로컬/Slurm 배포, 설정 `packages/host/src/alpagym_host/conf/default.yaml`. Apache-2.0

### 10.5 GitHub: nvidia-cosmos/cosmos-rl
- URL: https://github.com/nvidia-cosmos/cosmos-rl
- Physical AI용 RL 프레임워크. 병렬화: tensor/sequence/context/FSDP/pipeline. FP8 학습·FP8/FP4 rollout. 단일 컨트롤러 메시징(가중치 sync·rollout·평가)
- ⚠️ **"활발한 개발 종료, 제한 유지보수 — Cosmos 3 이동 권장"** 표기. 코드 Apache 2.0, 모델은 NVIDIA Open Model License

### 10.6 HF 데이터셋 카드: nvidia/PhysicalAI-Autonomous-Vehicles
- URL: https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles
- 1,700시간 / 306,152클립(20초) / **133TB** / 25개국·2,500+도시
- **카메라 7개**: front wide 120°, front tele 30°, cross left/right 120°, rear left/right 70°, rear tele 30°
- LiDAR: 상단 360° 회전식 1기(298,326클립) / Radar: 최대 10기(160,761클립)
- 라벨: egomotion, 캘리브레이션, 기계생성 장애물, OOD reasoning 라벨
- 라이선스: NVIDIA AV Dataset License(AV 용도 한정, 상업 가능, 감시·생체·재배포 금지), gated. 최근 한 달 다운로드 207,246
- ⚠️ 2026-01 dev blog 수치(1,727h/310,895클립/radar 163,850)와 소폭 상이 — 버전 갱신 추정(확증 없음)

### 10.7 DRIVE AGX Thor
- URL: https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/ (2025-09-03)
- "Up to 1,000 INT8 TFLOPS; 2,000 FP4 TFLOPS" (Blackwell GPU), 14x Arm Neoverse V3AE, LPDDR5X 273GB/s
- ISO 26262 ASIL-D + ISO 21434 설계. 개발킷 페이지: https://developer.nvidia.com/drive/agx (Thor SKU 10 벤치/SKU 12 차량)

### 10.8-0 스택 계층 조사 추가분 (4차, 2026-07-15 — 전부 🔍 직접 확인)

**의존성 파일 (pyproject.toml raw)**
- alpamayo1.5: requires-python ==3.12.*; torch==2.8.0, transformers==4.57.1, flash-attn>=2.8.3, accelerate>=1.12.0, hydra-core>=1.3.2, hydra-colorlog, einops>=0.8.1, av>=16.0.1, pandas, pillow, matplotlib, seaborn, **physical-ai-av==0.2.0**
- alpagym: ==3.12.*; workspace 5패키지(host, plugins, runtime, alpasim_configs, **policies/alpamayo_r1**); uv≥0.10; **Linux x86_64(CUDA) 제한**; PyTorch CUDA 12.8 wheel 인덱스; **xformers 의도적 비활성**(cosmos-rl 체인과 flash-attn 충돌 회피); flash-attn·grouped-gemm 커스텀 빌드; pytest에서 alpasim_e2e·**nccl_e2e** 기본 제외(NCCL 사용 근거)
- alpasim: >=3.11,<3.13; 기본 deps 비움, 전부 optional extras — 모듈 11종: plugins, controller, eval, **grpc**, runtime, utils, physics, tools, driver, wizard, trafficsim
- cosmos-rl: transformers>=4.51.1(4.52/4.53 제외)<5; **vllm>=0.8.5는 `[rl]` extra** — rollout 추론 서빙 근거

**차량 스택 공식 문서**
- DriveOS(https://developer.nvidia.com/drive/os): hypervisor("manages resources and provides abstraction"), 게스트 Linux/QNX, NvMedia("camera frames are directly loaded into GPU memory"), NvStreams(zero-copy), **CUDA·cuDNN·TensorRT 포함**, ASPICE·ISO 26262·ISO/SAE 21434 준수, DRIVE AGX SDK Developer Program 필요
- DriveWorks(https://developer.nvidia.com/drive/driveworks): DriveOS 위 미들웨어. **SAL**("abstraction between physical sensor models and software applications"), 이미지/포인트클라우드 처리, 동적 캘리브레이션(런타임 재추정), egomotion 모듈
- in-vehicle computing(https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/): **DRIVE Hyperion = "two NVIDIA DRIVE AGX Thor systems-on-a-chip on a single board" + DriveOS + 센서 셋 "14 high-definition cameras, nine radars, one lidar, and 12 ultrasonics"**, DRIVE AV software("purpose-built for L4 autonomy")

## 11. 신규 종합 보고서용 소스 (5차 조사, 2026-07-28)

### 11.1 CES 2026 Jensen 키노트 자막 🎥→🔍 (사용자 제공)
- 파일: `youtube_alpamayo_summut_2026.txt.txt` (파일명은 Summit이지만 내용 = CES 2026 키노트, "Hello, Las Vegas. Happy New Year." · "The Chat GPT moment for physical AI is nearly here" 문구 포함 — NVIDIA On-Demand "Alpamayo Summit 2026" 세션과의 관계 미확인)
- ASR 표기: Alpha Mylo/Alpha Miao/ElpaMayo = Alpamayo
- 핵심 발언:
  - "Alpha Mylo, the world's first thinking, reasoning autonomous vehicle AI ... trained end to end, literally from camera in to actuation out" — 학습 데이터: 인간 시연 주행 + "lots and lots of miles that are generated by Cosmos" + "hundreds of thousands of examples labeled very carefully"
  - 롱테일 논리: "long tails will be decomposed into quite normal circumstances that the car knows how to deal with. It just needs to reason about it."
  - 5-layer cake: car → chips → infrastructure(Omniverse·Cosmos) → **model(Alpamayo)** → **application(Mercedes-Benz)**
  - **Mercedes**: "Mercedes agreed to partner with us 5 years ago" · "the application above that is the Mercedes-Benz" · "first AV car from NVIDIA is going to be on the road in Q1, Europe in Q2, Asia in Q3 and Q4" · "keep on updating it with next versions of Alpha Miao" · 파트너 "Ola"(문맥상 Ola Källenius 추정)
  - Mercedes CLA: "just rated by NCAP the world's safest car"(미검증 주장) · "dual Orions, the next generation dual Thors"
  - **이중 스택 안전 구조**: Alpamayo(학습 기반) + "another software stack, an entire AV stack underneath ... fully traceable"(6-7년 개발) + "policy and safety evaluator"가 상황별로 Alpamayo↔classical stack 전환 — "the only car in the world with both of these AV stacks running"
  - 사업 구조: "We're going to deploy the car. We're going to operate the stack. We're going to maintain the stack."
  - Cosmos: "turns compute into data", 합성데이터로 롱테일 학습, 수백만 다운로드 주장
- ⚠️ 이 자막에 현대·BYD·지리·닛산 언급 **없음** (grep 확인)

### 11.2 GTC 2026 보도자료: DRIVE Hyperion L4 채택 🔍
- URL: https://nvidianews.nvidia.com/news/drive-hyperion-level-4 (2026-03-16)
- **BYD, Geely, Isuzu, Nissan이 채택한 것은 DRIVE Hyperion(HW·센서 플랫폼)** — Alpamayo 모델 채택이 아님
- **Hyundai는 이 보도자료에 없음** ([electrive 기사](https://www.electrive.com/2026/03/17/nvidia-partners-with-byd-geely-hyundai-isuzu-nissan-and-uber/) 제목엔 포함 — 별도 발표 여부 확인 필요, 미검증)
- **Nissan: "powered by Wayve software"** — Hyperion 위에서 Wayve SW 사용(Alpamayo 아님)
- Alpamayo 언급: "Alpamayo 1.5, a major upgrade ... an interactive, steerable reasoning model" · "downloaded by more than 100,000 automotive developers worldwide"(3월 시점)
- Uber: "fleet of autonomous vehicles entirely powered by the full-stack NVIDIA DRIVE AV software across 28 cities and four continents by 2028", LA·SF 2027 상반기 시작

### 11.3 HF 재확인 (2026-07-28) 🔍
- `alpamayo-2` 검색: 공식 Alpamayo-2/2-Super **여전히 미존재** — "여름 공개" 약속 미이행 상태(여름 기간은 아직 진행 중)
- 커뮤니티 파생 발견: `chenfunvidia/Alpamayo-R1-2B-step80000`(**2B 축소 체크포인트** — distillation 흐름 증거), `sasa2000/Alpamayo-R1-10B-Text-Only`, `lingkang2024/OneVL_AlpamayoR1`

## 12. Phase C — 한계·비판 조사 (6차, 2026-07-28)

### 12.1 Alpamayo-R1 논문 본문 정독 🔍 (PDF p.18–34 직접 열람, /tmp/ar1_paper.pdf)
- **수치 충돌 해소**: 초록 "close encounter -35%" = Table 8 (내부 75개 챌린지 시나리오, baseline 17.0±3.0% → AR1 11.0±2.0%). **off-road는 오히려 3.0%→4.0%로 소폭 증가**("comparable"로 표현) → NVIDIA Research 페이지의 "off-road -35%, close encounter -25%" 표기는 본문과 불일치 = **오기로 판정**
- Table 10 (공개 벤치마크, at-fault): 10B minADE 0.849 / close encounter 4.0±0.0% / off-road 16.0±1.0% / AlpaSim Score 0.72±0.02 ↔ 0.5B 0.913 / 9.0 / 19.0 / 0.35 (모델카드 0.73±0.01·910 시나리오와 근사, 논문은 920 시나리오 표기)
- "12% improvement" = Table 7, **0.5B 모델** 챌린지셋: trajectory-only 0.994m → CoC 0.868m (route 있음)
- Table 9 (RL, 0.5B): SFT→풀리워드: ADE 2.12→1.94m, reasoning 3.1→4.5(+45%), consistency 0.62→0.85(+37%), close encounter 6.9→3.7%. **reasoning 리워드만 쓰면 ADE 2.19m·consistency 0.53으로 악화** — 원문: "optimizing for reasoning quality alone can lead to ungrounded or overconfident reasoning ... fluent but causally disconnected explanations"
- **SFT 4대 한계 자인**(Sec 5.2): data bias/annotation noise, limited generalization, **weak visual grounding("may hallucinate causal factors not present in the scene", Fig 10)**, reasoning-action inconsistency(Fig 11)
- **Table 14 (99ms 분해, RTX 6000 Pro Blackwell)**: vision 3.43 + prefill 16.54 + **reasoning 70ms(40 tokens)** + trajectory(flow matching 5 steps) 8.75 = 99ms. trajectory-only 29ms / 자동회귀 궤적이면 312ms. "typically 100ms" 기준 턱걸이 — **reasoning이 지연의 70%, 40토큰 제한 전제**
- 백본 확정: "our final Alpamayo-R1 models adopt Cosmos-Reason as their backbone" (ablation은 DINOv2+Qwen2.5-0.5B / Qwen2.5-VL-3B/7B로 수행). Cosmos-Reason-7B LingoQA zero-shot 66.2 (GPT-4V 59.6, Qwen2.5-VL-7B 62.2 대비)
- Flow matching ablation (Table 12): AR 대비 minADE 0.6811→0.6440, AlpaSim(at-fault) 0.59→1.27, Comfort 44%→97%, 속도 1.16×
- 데이터 스케일링: 100k→2M 세그먼트 +14% (Fig 13). 내부 학습 데이터 = 미국·EU 수집(공개 데이터셋과 별개)
- Future Work 자인: **reasoning on demand 미구현**(모든 입력에 reasoning 생성), world model 통합 미착수
- 저자: core contributor에 **Zhijian Liu** 포함(→z-lab 겹침), Program Architect = Marco Pavone

### 12.2 CoC 신뢰성 직접 검증 논문 2편 🔍
- **arXiv 2605.17268 "Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation..."** (CVPR 2026 DriveX 채택, 중남대·Wollongong Dubai — 서드파티): Alpamayo-R1-10B 직접 실험(PhysicalAI-AV 100클립×3시드). 반사실 교란(블러·폐색)+정보이론 기준. **결과: 전체 reasoning faithfulness 42.5%, hallucination 8.9%, 보행자 미탐 33.3%, "정지 선언 후 미정지" 37.9%, silent failure 14.3%, 종방향 제어 실패 64.1%(정지 62.1%·감속 69.0% 실패 vs 차선유지 100%)**. 결론 원문: "Chain-of-Causation 추론을 현재 VLA 모델의 안전 보증으로 의존할 수 없다". 대응책 SafeDriveX(독립 VLM 모니터+RSS 폴백) 제안. ⚠️ 논문이 백본을 "Qwen3-VL-8B"로 기술 — NVIDIA 원논문(Cosmos-Reason)과 불일치, 논문측 부정확 추정
- **arXiv 2607.04681 "Do VLA Models Mean What They Say?"** (**Stanford+NVIDIA Research — Marco Pavone 공저!**): functional(성능 개선) vs faithful(내부 판단 반영) 구분 공식화. "RL improves trajectories even when reasoning remains unchanged or degrades"(결합 약함). Pinocchio critic 제안(균형정확도 0.87), 훈련 후 일관성 61.4%(baseline 43.4%). OOD 합성 위험 시나리오에서 "1.6× improvement over Alpamayo on causal alignment" = Alpamayo 자체의 causal alignment 약점을 개발 리드 본인 연구가 정량 인정

### 12.3 CoT faithfulness 일반 문헌 (배경) 📄
- [arXiv 2307.13702](https://arxiv.org/abs/2307.13702) "Measuring Faithfulness in Chain-of-Thought Reasoning" (Anthropic)
- [arXiv 2503.08679](https://arxiv.org/abs/2503.08679) "CoT Reasoning In The Wild Is Not Always Faithful"
- [Oxford "Chain-of-Thought Is Not Explainability"](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf)

### 12.4 경량화 계보 (z-lab) 🔍
- **DFlash**: [arXiv 2602.06036](https://arxiv.org/abs/2602.06036) "DFlash: Block Diffusion for Flash Speculative Decoding" (Jian Chen, Yesheng Liang, Zhijian Liu — ICML 2026 poster). block diffusion 드래프터로 6×+ 무손실 가속, EAGLE-3 대비 최대 2.5×
- **FlashDrive**: https://z-lab.ai/projects/flashdrive/ — **Alpamayo 1.5 지연 716ms→159ms(4.5×, RTX PRO 6000)**. 기법: 스트리밍 추론(비전 인코딩 75% 제거)+DFlash 투기 추론+적응형 flow matching+W4A8 양자화(ParoQuant)+CUDA graph/커널 퓨전. 논문 preview 단계
- ⚠️ **레이턴시 갭 주목**: NVIDIA 논문 99ms(40토큰·최적 구성) vs z-lab 실측 기본 716ms — 측정 조건 차이가 §7 레이턴시 절 핵심 소재
- 인물 연결: Zhijian Liu = AR1 core contributor 겸 z-lab(라이브스트림 "UCSD 랩" 발언과 부합, 소속 문서 직접 확인은 안 됨 — 추정 표기)

### 12.5 독립 평가 현황 📄
- 독립 재현·실측 평가는 사실상 부재 — 12.2의 faithfulness 논문 2편이 실질적 첫 외부 검증. 언론 논평 수준: "certified evidence 필요, independent labs must verify" ([AI CERTs](https://www.aicerts.ai/news/nvidias-alpamayo-sets-new-benchmark-for-autonomous-vehicle-ai/))
- 모델카드/repo 자체 한계 고지(기확보): "not a fully fledged driving stack", 센서 제한, 자동차급 검증 미실시

## 13. Phase A(대안 흐름) + Phase B 잔여 (7차, 2026-07-28)

### 13.1 주행 VLA 서베이 정독 🔍
- URL: https://arxiv.org/html/2512.16760v1 ("VLA Models for AD: Past, Present, and Future")
- 분류: modular → e2e Vision-Action(VA) → VLA. VLA 하위: **End-to-End VLA**(단일 모델) vs **Dual-System VLA**("slow deliberation (via VLMs) from fast, safety-critical execution (via planners)" 분리)
- VA 4대 한계(=VLA 등장 이유): 블랙박스 해석 불가 / long-tail 일반화 취약 / CoT 부재 / 자연어 지시 통합 불가
- **World model = VA의 병렬 진화 갈래**(image/occupancy/latent 3종) — "action consequence simulation" 최적화 vs VLA는 "linguistic reasoning and interpretability" — **직교·상보 관계**로 정리
- VLA 계보: ALVINN·ChauffeurNet → TransFuser·UniAD·VAD → DriveMLM·GPT-Driver·DriveLM·DriveGPT4(2023-24 전환) → AutoVLA·SimLingo·LINGO-2·OmniDrive·Drive-R1
- 남은 과제: robustness·interpretability·instruction fidelity, 효율·실시간 레이턴시, 안전 검증

### 13.2 Wayve GAIA-2 🔍
- URL: https://wayve.ai/thinking/gaia-2/ · arXiv 2503.20523 (기술보고서만 공개)
- 주행 특화 **비디오 생성 world model** — 용도: 정책이 아니라 **합성 데이터 생성·검증**("training, testing and validation"), 안전-중요 시나리오 생성
- 구조적 발견: **Wayve = LINGO(VLA)+GAIA(WM) 투트랙 — NVIDIA(Alpamayo+Cosmos)와 동일 구조**

### 13.3 Tesla pure e2e 노선 📄 (서드파티 종합 — 공식 1차 소스 아님 주의)
- FSD V12(2024)부터 카메라→작동 단일 신경망, rule 기반 C++ 제거, 언어 추론 없음
- 자체 neural world simulator 운용(Tesla AI VP Ashok Elluswamy 2025-11 발언 인용 보도) — FSD·Optimus 공용
- 참고 서베이: [arXiv 2603.16050](https://arxiv.org/html/2603.16050v1) "The Era of End-to-End Autonomy"

### 13.4 검색 부산물 — 학술 후속 흐름 📄 (제목·초록 수준)
- [arXiv 2605.08975](https://arxiv.org/pdf/2605.08975) "Latency Analysis and Optimization of **Alpamayo 1** via Efficient Trajectory Generation" — 레이턴시 절 보강 후보
- [arXiv 2606.23938](https://arxiv.org/pdf/2606.23938) "Neuro-Symbolic Drive: Rule-Grounded **Faithful** Reasoning for Driving VLAs" — faithfulness 후속
- [arXiv 2606.14010](https://arxiv.org/pdf/2606.14010) RT-VLA(distillation) · [arXiv 2603.11219](https://arxiv.org/pdf/2603.11219) Senna-2(VLM↔e2e 정합)

### 13.5 MindVLA-o1 실존 확인 🔍(보도 다수 교차)
- Li Auto, **GTC 2026(2026-03-17) 발표** — [Pandaily](https://pandaily.com/li-auto-unveils-next-gen-autonomous-driving-foundation-model-mind-vla-o1) 등
- 5대 요소: 3D 공간이해(native 3D ViT) · 멀티모달 추론 · 통합 액션 생성 · closed-loop RL · HW-SW 공동설계. 카메라+**LiDAR** 입력, **latent world model 내장**(단기 미래 시뮬), 로보틱스 확장 비전(Li Xiang: "자율주행은 Physical AI의 시작점")
- → VLA+WM 하이브리드의 양산 지향 실례

### 13.6 "엠비 드라이브 어시스트 프로" 정체 = **MB.DRIVE ASSIST PRO** 🔍
- **Mercedes-Benz 제품명**("엠비"=MB), NVIDIA 제품 아님 — [Mercedes 공식](https://group.mercedes-benz.com/innovations/product-innovation/autonomous-driving/mb-drive-assist-pro.html)
- 신형 CLA의 **SAE Level 2** 도심 point-to-point 지원(내비+주행보조 통합), 센서 30개(카메라 10·레이더 5·초음파 12 포함)
- 기반: NVIDIA 풀스택 DRIVE AV + DRIVE AGX — [NVIDIA Korea 블로그](https://blogs.nvidia.co.kr/blog/drive-av-software-mercedes-benz-cla/)
- 출시: 중국 2025말 → 미국 2026 → 독일 도심 기능 2026말(슈투트가르트·뮌헨), 2027초 전국 — [Electrek](https://electrek.co/2026/01/05/nvidia-unveils-open-source-ai-for-autonomous-driving-ships-in-mercedes-benz-cla-in-q1-2026/) 교차

### 13.7 CLA Euro NCAP 검증 🔍
- [Mercedes 공식](https://group.mercedes-benz.com/innovations/product-innovation/technology/cla-euro-ncap.html): 신형 전기 CLA = Euro NCAP 5성 + **"Best Performer"(2025년 테스트 전 모델 중 1위)**. Adult 94% / Child 89% / VRU 93% / Safety Assist 85%
- → Jensen 키노트 "world's safest car" 발언 = Euro NCAP 2025 Best Performer에 근거한 표현으로 판정(과장 아님, 단 "2025 테스트 차 중" 한정)

### 13.8 현대차 검증 🔍 (The Elec 원문, 2026-03-13 게재·07-28 업데이트)
- URL: https://www.thelec.net/news/articleView.html?idxno=5760
- 상태: **확정 아님 — "is moving to adopt" 추진 단계.** AVP본부 신임 총괄 **박민우(전 NVIDIA 부사장)**, 취임 2주 내 NVIDIA와 정례 미팅
- 발언: "we will be able to utilize data collected by other companies participating in the Hyperion ecosystem"
- **로열티 구조(§7 종속성 리스크 핵심)**: 가중치는 공개지만 **"validation-related source code" 비공개 — 양산 적용 시 NVIDIA와 로열티 협상 필요**
- 배경: 2025-10 현대, Blackwell GPU 50,000장 확보 발표 · CES 2026 정의선-젠슨 회동 보도([digitimes](https://www.digitimes.com/news/a20260108PD244/hyundai-nvidia-autonomous-driving-ces-2026.html)) · Hyundai/Kia DRIVE Hyperion 채택([WardsAuto](https://www.wardsauto.com/news/hyundai-kia-expanding-partnership-nvidia-drive-hyperion-sdv-adas/814989/))

### 10.8 배경지식 참고 논문 ID 검증
- 🔍 arXiv 2501.03575 = "Cosmos World Foundation Model Platform for Physical AI" (NVIDIA) — 제목 직접 확인
- 🔍 arXiv 2503.15558 = "Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning" (NVIDIA) — 제목 직접 확인
- 서베이 존재 확인(본문 미검토): arXiv 2506.24044, arXiv 2512.16760
- 고전(ID 안정, 재검증 생략): 1706.03762(Transformer), 2201.11903(CoT), 2103.00020(CLIP), 2307.15818(RT-2), 2212.10156(UniAD), 2006.11239(DDPM), 2203.02155(InstructGPT), 2402.03300(DeepSeekMath/GRPO), 1503.02531(Distillation)
