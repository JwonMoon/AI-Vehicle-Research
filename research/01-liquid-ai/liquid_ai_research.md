# Liquid AI 기업 조사 보고서

> 작성일: 2026-06-19
> 모든 사실 주장에 출처(URL)를 병기함. 공식 발표와 서드파티/언론 보도를 구분함.

---

## 1. 회사 개요

| 항목 | 내용 | 출처 |
|------|------|------|
| 회사명 | Liquid AI, Inc. | [Liquid AI – About](https://www.liquid.ai/company/about) |
| 설립 | MIT CSAIL(컴퓨터과학·인공지능연구소)에서 스핀오프. 2023년 설립 | [TechCrunch (2023.12.6)](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/) |
| 본사 | 미국 매사추세츠주 케임브리지, 314 Main St, Cambridge, MA 02142 | [Liquid AI – About](https://www.liquid.ai/company/about) |
| 창업자 | Ramin Hasani, Mathias Lechner, Alexander Amini, Daniela Rus (4인) | [Liquid AI – About](https://www.liquid.ai/company/about) |
| CEO | Ramin Hasani | [Mercedes-Benz 보도자료 (2026.4.23)](https://www.liquid.ai/press/liquid-ai-and-mercedes-benz-partner-to-scale-embedded-in-car-intelligence) |
| 주요 임원 | Mathias Lechner(CTO), Alexander Amini(Chief Scientific Officer로 보도됨) | [WebSearch 종합 / cbinsights](https://www.cbinsights.com/company/liquid-ai/people) — *직함은 서드파티 출처, 공식 확정 필요* |
| 미션 | "We build efficient general-purpose AI at every scale" — 모든 규모에서 효율적인 범용 AI 구축 | [Liquid AI – About](https://www.liquid.ai/company/about) |
| 주요 제품 | Liquid Foundation Models(LFM), LEAP(엣지 배포 플랫폼), Liquid Apollo(온디바이스 앱) | [Liquid AI – About](https://www.liquid.ai/company/about) |

> **창업진 배경 참고:** Daniela Rus는 MIT CSAIL 디렉터, Ramin Hasani·Mathias Lechner·Alexander Amini는 해당 연구실에서 Liquid Neural Network 연구를 수행한 연구진. (MIT 스핀오프 — [TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/))

### 회사 규모 / 인원 / 매출
- **인원, 매출은 공식 비공개.** 비상장 스타트업으로 정확한 직원 수·매출은 공식 출처에서 확인 불가. (출처 미확인)
- LFM 상용 라이선스 조건상 "연 매출 1,000만 달러 초과 기업"은 별도 상용 라이선스 필요 → 매출 규모 기업을 고객으로 상정. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))

### 자금 조달
| 항목 | 내용 | 출처 |
|------|------|------|
| 시드 | 3,750만 달러 | [TechCrunch (2023.12.6)](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/) |
| Series A | 2억 5,000만 달러 (공식 발표 2024.12.13) | [Liquid AI 공식 블로그](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai) |
| 주도 투자자 | AMD Ventures가 라운드 리드 (언론 보도) — *공식 블로그는 리드 투자자/밸류에이션 미명시, AMD를 협력사로만 언급* | [The Information](https://www.theinformation.com/briefings/liquid-ai-raises-250-million-in-round-led-by-amd), [TechFundingNews](https://techfundingnews.com/liquid-ai-closes-250m-hits-2b-valuation-with-amd-led-funding/) |
| 밸류에이션 | 약 23억 5,000만 달러(유니콘) — **언론 보도 기준**, 공식 미공개 | [TechFundingNews](https://techfundingnews.com/liquid-ai-closes-250m-hits-2b-valuation-with-amd-led-funding/) |

> ⚠️ **출처 구분:** Liquid AI 공식 블로그는 2.5억 달러 조달은 명시하나, "리드 투자자=AMD", "밸류에이션 23.5억 달러"는 공식 문서에 없음. 이 두 수치는 The Information·TechFundingNews 등 **언론 보도** 기반.

자금 사용처(공식): LFM 개발·확장·배포 가속, 컴퓨팅 인프라 확장, 엣지/온프레미스 추론·파인튜닝 스택 제품화, 가전·통신·금융·이커머스·바이오 분야 배포 확대. ([공식 블로그](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai))

---

## 2. 핵심 기술

구성: **(A) 기반 기술 → (B) 모델 → (C) 플랫폼** 3층 구조.

| 층 | 정체 | 항목 |
|----|------|------|
| A. 기반 기술 | 아키텍처/연구 | Liquid Neural Network (LNN) |
| B. 모델 | 출하 제품군 (Liquid Foundation Models) | LFM2 / LFM2.5 (엣지 소형), 멀티모달·오디오 LFM, Nanos |
| C. 플랫폼 | 배포 도구 | LEAP(엣지 배포), Apollo(모바일 앱) |

> **LNN vs LFM 핵심:** LNN은 *기반 기술/아키텍처*(연구 산물, 제품 아님). LFM은 그 원리를 범용 생성형 모델로 확장한 *상용 모델군*. 단, 실제 출하 LFM(LFM2 등)은 순수 LNN이 아닌 **컨볼루션+GQA 하이브리드**. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))

---

### A. 기반 기술 — Liquid Neural Networks (LNN)
창업 토대. MIT CSAIL 연구 산물. 제품이 아닌 아키텍처 원리.
- **개념:** 예쁜꼬마선충(roundworm) 뇌에서 영감 받은 구조. 시간에 따른 개별 뉴런 거동을 미분방정식으로 모델링하고, 데이터를 처리하며 파라미터를 동적으로 조정하는 "유동적(liquid)" 아키텍처. ([TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/))
- **트랜스포머와의 차이:** 매우 컴팩트. 예시로 GPT-3가 약 1,750억 파라미터인 데 반해, 드론 항법용 LNN은 약 2만 파라미터·뉴런 20개 미만으로 동작 가능 — 이론상 "라즈베리파이에서 자율주행 알고리즘 구동" 수준. ([TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/))
- **핵심 혁신:** 고립된 데이터 스냅샷이 아닌 "데이터 시퀀스"를 고려, 뉴런 간 신호 교환을 동적으로 조정 → 학습하지 않은 환경 변화(예: 날씨 변화)에도 적응. ([TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/))

#### 왜 트랜스포머보다 컴팩트한가
핵심 차이 = **"뉴런 한 개가 얼마나 똑똑하냐"**.

| 구분 | 트랜스포머 (GPT 등) | LNN |
|------|---------------------|-----|
| 뉴런 성격 | 정적(static). 가중치 곱·합, 학습 후 숫자 고정 | 뉴런 자체가 작은 동역학 시스템. 미분방정식으로 시간에 따라 내부 상태가 계속 진화 |
| 똑똑함의 출처 | 뉴런을 **엄청 많이 쌓아서** 확보 → 파라미터 수십억~수천억 | 복잡도를 **뉴런 내부 방정식**에 담음 → 적은 뉴런으로 같은 패턴 표현 |
| 비유 | 계산기 수억 개 배선 | 출렁이는 아날로그 회로 몇 개 |

적은 수로 되는 두 이유:
1. **연속 시간(continuous-time):** 트랜스포머는 시점마다 별도 처리. LNN은 시간을 연속 흐름으로 모델링 → 시퀀스/동역학을 적은 파라미터로 자연스럽게 표현. ([LNN 논문 arXiv:2006.04439](https://arxiv.org/abs/2006.04439))
2. **표현력 집중:** 복잡도를 "뉴런 수(폭)"가 아닌 "뉴런 내부 방정식(질)"에 배치 → 폭 대신 깊이로 표현력 확보.

수치 예: 드론 항법용 LNN 약 2만 파라미터·뉴런 20개 미만 vs GPT-3 약 1,750억 파라미터. ([TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/))

> ⚠️ **비교 주의(공정성):**
> - 위 "2만 vs 1,750억"은 **동일 작업 비교 아님**. LNN 2만은 드론 항법(좁은 제어 문제), GPT-3는 범용 언어. 1:1 비교 불가.
> - 범용 언어/대화로 가면 LNN도 작지 않음. 실제 출하 모델 LFM2는 **순수 LNN이 아니라 컨볼루션+어텐션 하이브리드**, 크기 0.35B~1.2B (뉴런 20개 수준 아님). ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))
> - 메커니즘(연속시간·표현력 집중)은 LNN 논문·Liquid AI 주장 기반. 트랜스포머 대비 우위는 작업에 따라 다름 — 만능 아님.
> - 참고: GPT = **G**enerative **P**re-trained **T**ransformer, 즉 트랜스포머 구조. ([Transformer 원논문 arXiv:1706.03762](https://arxiv.org/abs/1706.03762))

---

### B. 모델 — Liquid Foundation Models (LFM)
LNN 연구를 범용 생성형 모델로 확장한 출하 제품군. 트랜스포머 일변도가 아닌 하이브리드 아키텍처 채택, **온디바이스/엣지 효율**에 집중.

> **중요:** LFM2/LFM2.5는 단일 모델이 아니라 **크기(350M~24B)·용도(텍스트·비전·오디오·검색·추론)·아키텍처(dense / MoE)별 패밀리**. 아래 벤치마크에 쓰인 LFM2.5-1.2B-Instruct는 그중 대표 소형 멤버 하나.

#### B-0. 모델 패밀리 전체 (2024.9~2026.6)
| 모델 | 크기 | 종류/용도 | 공개 |
|------|------|-----------|------|
| LFM v1 | 1.3B/3B/40B-MoE | 1세대 범용 (초기 라인) | 2024.9.30 |
| LFM2 | 0.35B/0.7B/1.2B | 2세대 엣지 소형 텍스트 | 2025.7.10 |
| Nanos | 350M/1.2B (6종) | 작업 특화(번역·추출·수학·RAG·도구) | 2025.9.25 |
| LFM2-8B-A1B | 8B(활성 1B) | **MoE** 온디바이스 | 2025.10.7 |
| LFM2-VL-3B | 3B | 비전언어 | 2025.10.22 |
| LFM2-ColBERT-350M | 350M | 검색(임베딩) | 2025.10.28 |
| LFM2.5 | 1.2B 등 | 3세대 (텍스트·비전·오디오) | 2026.1.5 |
| LFM2.5-1.2B-Thinking | 1.2B | 추론 특화(1GB 미만) | 2026.1.20 |
| LFM2-24B-A2B | 24B(활성 2B) | **MoE** 최대 모델, AI PC | 2026.2.24 |
| LFM2.5-350M | 350M | 초소형 | 2026.3.31 |
| LFM2.5-VL-450M | 450M | 비전언어(엣지~클라우드) | 2026.4.8 |
| LFM2.5-8B-A1B | 8B(활성 1B) | **MoE** 개선판 | 2026.5.28 |
| LFM2.5 Retrievers | 350M×2 | 검색(ColBERT/Embedding), 첫 양방향 | 2026.6.18 |

출처: [Liquid AI 블로그 목록](https://www.liquid.ai/company/blog?category=All)

##### 용어: 모델 변종(variant) — Base / Instruct / Thinking
같은 모델의 훈련 단계 차이.
- **Base:** 사전학습만 한 원본. 다음 토큰 예측만. 명령 잘 못 따름.
- **Instruct:** Base에 지시 튜닝(SFT/RLHF) 추가 → 사용자 명령·대화 수행. **실사용 형태.** (벤치마크의 "1.2B-Instruct" = 이 버전)
- **Thinking:** 추론 특화(사고 과정 생성). 수학·논리 강화.
- 그 외 `-JP`(일본어), `-Extract`/`-RAG`/`-Tool`(작업 특화) 등.

##### 용어: MoE 와 "A1B / A2B"
- **MoE(Mixture of Experts):** 모델 전체는 크지만 **토큰당 일부 전문가만 활성화**.
- `8B-A1B` = 총 **8B** 파라미터, **A**ctive(활성) **1B**(토큰마다 1B만 작동). `24B-A2B` = 총 24B, 활성 2B.
- 효과: **큰 모델 품질 + 작은 모델 속도/메모리** → 온디바이스에 큰 모델 올리는 방법.

#### B-1. LFM2 (2025.7.10 공개) — 엣지 소형
| 항목 | 내용 | 출처 |
|------|------|------|
| 아키텍처 | 하이브리드 Liquid 모델 (multiplicative gates + short convolutions). **총 16블록 = double-gated short-range convolution 10블록 + grouped query attention 6블록** | [LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models) |
| 모델 크기 | 0.35B / 0.7B / 1.2B (dense) | 동일 |
| 속도 | CPU에서 Qwen3 대비 **디코드·프리필 2배 빠름** | 동일 |
| 효율 | LFM2-1.2B가 파라미터 47% 적으면서 Qwen3-1.7B와 경쟁력 / 학습 효율 이전 세대 대비 3배 | 동일 |
| 학습 | 10조 토큰 (영어 75%, 다국어 20%, 코드 5%), 32k 컨텍스트, LFM1-7B 지식증류 활용 | 동일 |
| 라이선스 | Apache 2.0 기반 오픈 라이선스 (연 매출 1,000만 달러 초과 기업은 상용 라이선스 필요) | 동일 |
| 배포처 | Hugging Face, OpenRouter, Liquid Playground | [BusinessWire (2025.7.10)](https://www.businesswire.com/news/home/20250710527694/en/Liquid-AI-Releases-Worlds-Fastest-and-Best-Performing-Open-Source-Small-Foundation-Models) |

##### "컨볼루션 + GQA 하이브리드"란?
한 모델 안에 **두 종류 블록을 섞은** 구조. 16블록 = 컨볼루션 10 + GQA 6.

**1. (단거리) 컨볼루션 블록 — 10개**
- 컨볼루션(convolution) = 토큰을 볼 때 **바로 옆 몇 개만** 슬라이딩 윈도로 훑는 연산. 지역 패턴(이웃 단어 관계) 포착. 연산량 길이에 **선형 O(n)** → 빠르고 가벼움.
- LFM2는 여기에 **게이트(gate)**를 붙여 신호 흐름을 곱셈으로 조절(중요한 것만 통과). 정식 명칭 "double-gated short-range convolution". LNN 계열의 동적 조절 아이디어가 들어간 부분. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))

**2. GQA 블록 — 6개**
- 어텐션(attention) = 토큰이 **문장 전체 어디든** 골라 참조하는 연산. 장거리 관계 포착. 트랜스포머 핵심. 단 길이에 **제곱 O(n²)** → 무겁고 메모리 많이 씀.
- **GQA(Grouped Query Attention)** = 어텐션 변형. 여러 query가 key/value를 **묶어서 공유** → 메모리·속도 개선하면서 성능 거의 유지. ([GQA 논문 arXiv:2305.13245](https://arxiv.org/abs/2305.13245))

**왜 섞나 (하이브리드 이유)**

| | 컨볼루션 | 어텐션(GQA) |
|---|---|---|
| 잘함 | 지역 패턴, 빠름·가벼움 | 장거리 관계 |
| 약점 | 먼 관계 못봄 | 무거움(O(n²)) |

→ **가벼운 컨볼루션 많이(10) + 비싼 어텐션은 필요한 만큼만(6)** 배치. 순수 트랜스포머보다 빠르고 메모리 적음 → 온디바이스/엣지 적합. "CPU서 Qwen3 대비 2배" 주장의 구조적 근거. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))

> 요약: **싼 일은 컨볼루션, 비싼 일은 어텐션 — 역할 분담한 16블록(10+6) 혼합 모델.**

#### B-2. LFM2.5 (2026.1.5 공개) — 최신 세대, 엣지 소형 + 멀티모달·오디오
| 항목 | 내용 | 출처 |
|------|------|------|
| 라인업 | LFM2.5-1.2B-Base / -Instruct, 일본어용 -JP, 비전언어 LFM2.5-VL-1.6B, 오디오언어 LFM2.5-Audio-1.5B | [LFM2.5 블로그 (2026.1.5)](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai) |
| 학습 확대 | 사전학습 토큰 10T → **28T**, 강화학습(RL) 파이프라인 대폭 확장 | 동일 |
| 텍스트 | 온디바이스 에이전트형 AI에 최적화된 instruction following | 동일 |
| 비전 | 다중 이미지·다국어 비전 이해 (아랍어·중국어·프랑스어·독일어·일본어·한국어·스페인어 지원) | 동일 |

출처: [LFM2.5 블로그 (2026.1.5)](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai)

##### "텍스트: 온디바이스 에이전트형 AI에 최적화된 instruction following"이란?
- **instruction following(지시 따르기):** 사용자 명령("3문장으로 요약", "JSON으로 출력")을 정확히 알아듣고 그대로 수행하는 능력. -Instruct 모델의 핵심 훈련 목표.
- **에이전트형(agentic):** 단순 답변 넘어 **도구 호출·다단계 작업**을 스스로 수행하는 AI. 도구 이름·인자를 안 틀리게 *구조적으로 정확히* 따라야 함.
- **온디바이스:** 클라우드 안 거치고 기기 내부 구동.
- → 합치면: "클라우드 없이 기기에서 도는, 도구 쓰고 다단계 작업하는 에이전트가 명령을 정확히 따르도록 특화 훈련됨." 작은 모델의 약점(지시 따르기 부족)을 겨냥한 자랑.

##### 멀티모달·오디오 LFM
LFM2.5 세대부터 텍스트 외 **비전언어(LFM2.5-VL-1.6B)**, **오디오언어(LFM2.5-Audio-1.5B)** 모델 별도 제공.
- **오디오 "이전 세대 대비 8배 빠름"의 정확한 의미:** 모델 전체가 아니라 **detokenizer(숫자 출력→실제 음성 파형 변환 부품)**가 LFM2 세대의 "Mimi" detokenizer 대비 모바일 CPU에서 8배 빠름(동일 precision). INT4 저정밀(QAT) 학습으로 품질 손실 거의 없이 경량 배포. → 실시간 음성 응답 가능. ([LFM2.5 블로그](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai))

##### 벤치마크 해석 (LFM2.5-1.2B-Instruct)
형식: `벤치마크 = LFM2.5 점수 (경쟁모델 점수)`, **높을수록 좋음**.

| 벤치마크 | 측정 능력 | LFM2.5-1.2B | 비교 모델 |
|----------|-----------|-------------|-----------|
| MMLU-Pro | 다분야 지식·추론 (어려운 객관식) | **44.35** | Llama 3.2 1B = 20.80 |
| IFEval | 지시 따르기 정확도 | **86.23** | Gemma 3 1B = 63.25 |

- 해석: 비슷한 크기(~1B) 소형 모델 대비 지식·추론, 지시 따르기 둘 다 크게 앞섬 = "작은데 잘한다" 주장.
- ⚠️ 주의: (1) **벤더 자체 발표 수치** — 독립 평가 확인 권장. (2) MMLU-Pro는 Llama, IFEval은 Gemma로 **시험마다 비교 상대가 다름** → 유리한 매칭일 수 있음. (3) 절대 점수는 소형 한계(MMLU-Pro 44점은 대형 모델 70~80점대 대비 낮음) — "소형 치고 잘함"이지 대형 대체 아님.

##### 기기별 추론 속도 벤치마크 (LFM2.5-1.2B-Instruct)
조건: **4-bit 양자화, 4k 토큰 입력 컨텍스트, CPU 기준.** 비교 대상 Granite-4.0-h-1b, Qwen3-1.7B.

**AMD Ryzen AI Max+ 395**
| 지표 | LFM2.5-1.2B | Granite-4.0-h-1b | Qwen3-1.7B |
|------|-------------|------------------|------------|
| Prefill (tok/s, ↑좋음) | **5,049** | 3,994 | 3,092 |
| Decode (tok/s, ↑좋음) | **239** | 146 | 141 |
| Memory (MB, ↓좋음) | **896** | 1,129 | 1,804 |

**Qualcomm Snapdragon Gen4 (Samsung Galaxy S25 Ultra)**
| 지표 | LFM2.5-1.2B | Granite-4.0-h-1b | Qwen3-1.7B |
|------|-------------|------------------|------------|
| Prefill (tok/s, ↑좋음) | **244** | 195 | 104 |
| Decode (tok/s, ↑좋음) | **71** | 47 | 42 |
| Memory (MB, ↓좋음) | **799** | 1,055 | 1,985 |

- 용어: **Prefill** = 입력 프롬프트 처리(초기 한 번) 속도, **Decode** = 토큰 생성(응답 출력) 속도, **Memory** = 구동 메모리 사용량.
- 해석: 두 기기 모두에서 LFM2.5가 속도(Prefill·Decode) **가장 빠르고** 메모리 **가장 적게** 씀. 특히 Decode에서 Qwen3 대비 큰 격차(AMD 239 vs 141, Snapdragon 71 vs 42). 폰(Snapdragon)에서도 동급 최상 = 온디바이스 적합성 입증 의도.
- ⚠️ 벤더 자체 발표 수치, 4-bit 양자화·4k 컨텍스트 특정 조건 기준. 조건 다르면 결과 다를 수 있음. ([LFM2.5 블로그](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai))

##### 배포 호환성 (NPU / 하드웨어 / 런타임)
"어디서·어떻게 돌릴 수 있나" = 배포 유연성.
- **NPU 최적화:** AMD·Nexa AI가 LFM2.5를 NPU(폰·노트북·차량 칩의 AI 전용 가속기)에서 잘 돌게 다듬은 버전 제공 → 엣지에서 더 빠르고 저전력.
- **런타임 지원:** llama.cpp(가벼운 로컬 추론)·MLX(애플 실리콘)·vLLM(서버 고속)·ONNX(범용 교환 포맷) 등 인기 실행 도구에서 그대로 사용 가능.
- **하드웨어 대응:** Apple·AMD·Qualcomm·Nvidia 4대 칩 모두 지원 → 벤더 비종속.
- → 종합: 특정 칩·도구에 묶이지 않고 폰/맥/서버/차량 어디든, 인기 도구로, NPU까지 최적화해 구동. 온디바이스 전략의 핵심. ([LFM2.5 블로그](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai))

#### B-3. Nanos — 극소형, 작업 특화 (2025.9.25 공개)
"프론티어급 품질을 일상 기기에서 직접 구동하는 극소형(extremely small) 파운데이션 모델". 범용 모델이 아니라 **한 작업만 잘하도록 특화**한 초소형 모델 묶음. ([Liquid AI – Nanos 보도자료](https://www.liquid.ai/press/liquid-unveils-nanos-extremely-small-foundation-models-that-match-frontier-model-quality--running-directly-on-everyday-devices))

**핵심 발상:** 범용 대형 모델 대신, 특정 작업에 맞춘 350M~1.2B 초소형 모델을 써서 **GPT-4o급 품질을 기기에서 직접** 내겠다는 것. (전체 라인 350M~2.6B 파라미터)

**출시 6종 (작업 특화):**
| 모델 | 크기 | 작업 |
|------|------|------|
| LFM2-350M-ENJP-MT | 350M | 영↔일 양방향 번역 |
| LFM2-350M-Extract | 350M | 비정형 데이터 → 구조화 추출(예: 청구서 → JSON) |
| LFM2-350M-Math | 350M | 수학 추론 |
| LFM2-1.2B-Extract | 1.2B | 데이터 추출 (상위 버전) |
| LFM2-1.2B-RAG | 1.2B | 긴 문맥 기반 질의응답(RAG) |
| LFM2-1.2B-Tool | 1.2B | 함수/도구 호출(에이전트용) |

**성능 주장 (크기 대비):**
- LFM2-350M-ENJP-MT: 자기보다 10배 이상 큰 범용 오픈모델 능가. 번역 품질이 **약 500배 크다고 추정되는 GPT-4o와 경쟁력**.
- LFM2-350M-Extract: 11배 큰 Gemma 3 4B 능가.
- LFM2-1.2B-Extract: **22.5배 큰 Gemma 3 27B 능가**, 약 160배 큰 GPT-4o와 경쟁력.

**효율 주장:** 클라우드 배포 대비 연간 비용 최대 **50배 절감**, 에너지 사용 **100배 감소**.

**용도:** 온디바이스(폰·노트북·임베디드), 빅데이터용 클라우드 GPU 확장, 가전·자동차·이커머스·금융 기업 배포.

출처: [Liquid AI – Nanos 보도자료 (2025.9.25)](https://www.liquid.ai/press/liquid-unveils-nanos-extremely-small-foundation-models-that-match-frontier-model-quality--running-directly-on-everyday-devices)

> ⚠️ "GPT-4o급" "500배 작은데 경쟁력"은 **특정 단일 작업(번역·추출 등) 한정** + 벤더 자체 주장. 범용 능력에서 GPT-4o 대체 아님. 작업 특화 모델의 강점은 좁은 범위에 국한됨.

#### B-4. LFM2.5 Retrievers — 검색(retrieval) 모델 (2026.6.18 공개)
검색 전용 모델 2종, 각 350M. LFM2.5-350M-Base를 **causal decoder → bidirectional encoder로 개조**. LFM 계열 **첫 양방향(bidirectional) 모델**. RAG 파이프라인의 "찾기" 단계 담당(생성이 아니라 검색).

| 모델 | 방식 | 특징 |
|------|------|------|
| LFM2.5-Embedding-350M | 문서당 dense 벡터 1개 | 인덱스 가장 작고 빠름 |
| LFM2.5-ColBERT-350M | 토큰별 벡터(단어 단위 매칭) | 정확도 높음, 인덱스 큼 |

- **언어:** 11개 다국어·교차언어 검색 (아랍·독일·영·스페인·프랑스·이탈리아·일본·**한국**·노르웨이·포르투갈·스웨덴어). 단문맥(상품 카탈로그·FAQ·지원 문서) 대상.
- **벤치마크(↑좋음):** NanoBEIR Multilingual NDCG@10 — ColBERT 0.605 / Embedding 0.577 > Qwen3-Embedding-0.6B 0.556 > GTE-multilingual-base 0.528. MKQA-11 Recall@20 — ColBERT 0.694 / Embedding 0.691 > GTE 0.675.
- **속도:** MacBook M4 Max 쿼리 임베딩 7.3ms(p50), H100 GPU 1.3~2.8ms.

출처: [LFM2.5 Retrievers 블로그 (2026.6.18)](https://www.liquid.ai/blog/lfm2-5-retrievers)

> ⚠️ 벤더 자체 수치. 단문맥 검색 특화(긴 문서 검색 아님). 참고: 이전에 ColBERT 계열은 LFM2-ColBERT-350M(2025.10.28)으로 먼저 나왔고, 이번이 LFM2.5 세대 업데이트.

---

### C. 플랫폼 — 배포 도구 (2025.7.15 출시)
모델을 실제 기기에 올리는 도구 계층.

#### C-1. LEAP (Liquid Edge AI Platform) — 엣지 배포
**"풀스택 온디바이스 AI 플랫폼"** — 모델 선택부터 추론까지 하나의 통합 툴체인. 슬로건 "Intelligence everywhere. For everyone", "어떤 기기에든 몇 분 만에 배포", "No cloud, no guesswork". ([LEAP](https://leap.liquid.ai/), [LEAP Platform](https://leap.liquid.ai/platform), [공식 보도자료](https://www.liquid.ai/press/liquid-ai-launches-leap-and-apollo-a-new-era-for-edge-ai-deployment-begins))

**4단계 워크플로우:**
1. **Find** — 용도·제약에 맞는 모델 검색 (사전학습 번들 라이브러리 탐색·다운로드)
2. **Test** — Apollo·Workbench로 온디바이스 또는 클라우드에서 비교
3. **Customize** — GPU 최적화 스크립트로 LFM2 등 파인튜닝 → 배포용 모델 번들 생성
4. **Deploy** — 앱에 통합해 완전 온디바이스 실행

**구성 도구:**
- **Edge SDK** — 로컬 모델 로드·쿼리를 "클라우드 API 호출하듯" 처리
- **Model bundling 서비스** — 배포 최적화 패키징
- **Workbench** — 모델 비교·테스트
- **Liquid Apollo** — 온디바이스 테스트용 모바일 앱
- **CLI 파인튜닝** — GPU 최적화 학습 스크립트
- **Function calling** — 외부 시스템 연동(에이전트)

**제공 모델:** 텍스트·오디오·비전 350M~1.6B (LFM2-1.2B, LFM2-Audio-1.5B, LFM2-VL-1.6B, 다국어·RAG·번역 특화 변종 등). 비전 모델은 iOS·Android·노트북 지원.
**임베드:** 앱에 클라우드 API 호출하듯 **약 10줄 코드**로 직접 삽입. CPU·GPU 가속 Apple·AMD·Qualcomm·Nvidia 전반, NPU는 AMD·Qualcomm·Nexa AI 협력.
**플랫폼:** iOS·Android·노트북·데스크톱. PC/노트북은 **llama.cpp 경유, AMD Ryzen 최적화**(2025.8.18 노트북 확장).
**활용 예:** AR/VR 장면 이해, 게임 대사, 사기 탐지, 오프라인 지식 비서, 기업 문서 처리, 웨어러블 헬스 분석.

출처: [LEAP](https://leap.liquid.ai/), [LEAP Platform](https://leap.liquid.ai/platform), [VentureBeat](https://venturebeat.com/ai/finally-a-dev-kit-for-designing-on-device-mobile-ai-apps-is-here-liquid-ais-leap), [LFM2.5 블로그](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai)

> 가격 정보는 공식 페이지에 미명시(출처 미확인).

#### C-2. Liquid Apollo — 소비자용 모바일 앱 (iOS + Android)
일반 사용자가 온디바이스 AI를 직접 체험하는 앱. "주머니 속 저지연·클라우드 프리 플레이그라운드, 진입 장벽 없음". AI를 즉시·안전하게·로컬로 사용. **iOS·Android 양쪽 제공**(앱스토어 다운로드). LEAP의 Test 단계에서 모델 비교 용도로도 쓰임. ([Liquid Apollo](https://www.liquid.ai/apollo))

> 정정: 이전 버전 문서가 Apollo를 "iOS 앱"으로 적었으나, 공식 페이지 기준 **iOS·Android 둘 다 지원**. 구동 모델명은 페이지에 미명시(출처 미확인).

#### C-3. 개발자 접근 경로 / 생태계
공식 docs(LFM2)가 안내하는 개발자 진입점:
- **모델 배포처:** Liquid Playground, HuggingFace Collections, OpenRouter API, LEAP Model Library
- **개발 단계 지원:** 모델 탐색 → 플랫폼별 추론 가이드 → 파인튜닝 커스터마이즈 → 모바일·노트북·웹 end-to-end 코드 예제
- **문서 강조 특징:** 학습 3배 빠름, SOTA급 품질, 메모리 효율, "Deploy Anywhere"(주요 추론 프레임워크 호환)
- **커뮤니티:** GitHub, Discord, 문서 포털(docs.liquid.ai)

출처: [LFM Docs – Welcome](https://docs.liquid.ai/lfm/getting-started/welcome)

#### C-4. LFM 사용 조건·요구사항 (공식 문서 기준)
"기존 칩에서 부품 없이 구동"은 **조건부**다. 공식 docs가 명시한 요구사항·제약:

**메모리 (가장 중요):**
- LEAP SDK 데스크톱/네이티브 기준 **"디스크상 모델 크기 + 1 GiB 여유 RAM 확보"** 권장. 메모리 매핑(mmap)으로 가중치를 지연 로드. ([Desktop & Native Platforms](https://docs.liquid.ai/deployment/on-device/sdk/desktop-platforms.md))
- 즉 1.2B 4-bit(디스크 ~0.7GB)면 대략 **~1.7GB+ 여유 RAM** 필요. 모델 크면 비례 증가.

**양자화(필수 압축):**
- GGUF: Q4_0·Q4_K_M·Q5_K_M·Q6_K·Q8_0·BF16·F16 — **Q4_K_M 권장**(크기/품질 균형)
- MLX(애플): 3~8bit·BF16 — **8bit 권장**
- ONNX: FP32·FP16·Q4·Q8 — **Q4 권장**
- ([Complete Library](https://docs.liquid.ai/lfm/models/complete-library))

**컨텍스트 길이:** 대부분 **32K 토큰**, LFM2.5-8B-A1B만 **128K**. ([Complete Library](https://docs.liquid.ai/lfm/models/complete-library))

**배포 포맷·백엔드:**
- GPU 추론: Transformers, vLLM, SGLang / 서비스 Baseten·Fal·Modal
- 온디바이스: llama.cpp, LM Studio, MLX(애플 실리콘), Ollama, ONNX, LEAP SDK
- ([docs 인덱스](https://docs.liquid.ai/llms.txt))

**데스크톱/네이티브 최소 OS (LEAP SDK):**
| 플랫폼 | 아키텍처 | 최소 OS |
|--------|----------|---------|
| JVM Desktop | macOS ARM64, Linux x86_64/aarch64, Windows x86_64/aarch64 | JDK 11 |
| Linux Native | x86_64, aarch64 | glibc 2.34+ (Ubuntu 22.04/Debian 12/RHEL 9) |
| Windows Native | x86_64 | Windows 10+ |
| macOS | ARM64(Apple Silicon) | macOS 15 |

출처: [Desktop & Native Platforms](https://docs.liquid.ai/deployment/on-device/sdk/desktop-platforms.md)

> ⚠️ **조건 요약 (차량 HPC 도입 관점):**
> 1. **모델 체급 ↔ 칩 매칭 필수** — 350M~1.2B는 일반 CPU 가능, 8B/24B는 더 큰 메모리·연산 필요(임의 칩 아님).
> 2. **양자화 전제** — 4-bit 등 압축이 기본. 칩이 해당 정밀도 지원해야 하고 품질 손실 일부 감수.
> 3. **여유 RAM = 모델 크기 + 1GiB** — 차량 SoC는 메모리 공유 환경이라 실측 확보 필요.
> 4. **per-모델 정확 RAM·차량 SoC 최소사양은 공식 표로 미공개** — 개별 모델 카드/PoC로 확인해야 함(출처 미확인). 서드파티(InsiderLLM 등)는 LFM2 최소 ~220MB~700MB 언급하나 비공식.

---

## 3. 차별점

1. **트랜스포머 대안 아키텍처:** 표준 트랜스포머가 아닌 LNN 기반 하이브리드(컨볼루션 + GQA). 동급 모델 대비 적은 파라미터로 경쟁력 확보. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))
2. **온디바이스/엣지 우선:** 클라우드 의존 없이 로컬 기기에서 저지연·프라이빗 구동을 핵심 가치로 제시. ([공식 보도자료](https://www.liquid.ai/press/liquid-ai-launches-leap-and-apollo-a-new-era-for-edge-ai-deployment-begins))
3. **효율성:** CPU에서 Qwen3 대비 2배 속도, 학습 효율 3배 개선 주장. ([LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models))
4. **하드웨어 중립 + AMD 동맹:** AMD Instinct GPU 학습/배포 협력, NPU는 AMD·Qualcomm·Nexa AI 협력. NVIDIA 종속에서 벗어난 추론 옵션 지향. ([공식 블로그](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai), [TechFundingNews](https://techfundingnews.com/liquid-ai-closes-250m-hits-2b-valuation-with-amd-led-funding/))

---

## 4. 협력·파트너십 및 적용 사례

### [차량] 4.0 차량용 솔루션 개요
Liquid AI는 차량 **기존 CPU·NPU에서 직접 구동**되는 소형 멀티모달 AI를 제공, 차내 AI 비서의 클라우드 의존 제거를 표방.
- Edge-first SLM: CPU·NPU 저메모리 환경 최적화, **1초 미만 응답**.
- 멀티모달: 오디오 + 비전언어로 의도·감정·차내(cabin) 상황 이해.
- 하이브리드: 제조사 판단에 따라 엣지/클라우드 선택 구동.
- 신규 부품 없이 표준 차량용 SoC에서 동작.

출처: [Liquid AI – Automotive](https://www.liquid.ai/automotive)

### 4.1 Mercedes-Benz (대표 사례)
| 항목 | 내용 |
|------|------|
| 발표일 | 2026년 4월 23일 |
| 형태 | 다년간(multi-year) 파트너십. 북미 시장 Mercedes 차량에 임베디드 온디바이스 AI 통합 |
| 적용 대상 | 3세대 및 4세대 MBUX. (3세대: MY24+ E-Class·CLE, MY25-26 C-Class ICE, MY25-27 GLC ICE, MY26-27 GT 2-door·SL / 4세대: MY26+ CLA BEV, MY27 CLA·C-Class·GLB·GLC·EQS·GLE/GLS·S-Class·AMG GT 등) |
| 기술 범위 | LFM 기반 온디바이스 음성인식·언어이해·추론. MBUX Virtual Assistant 강화. MB.OS와 통합. 저지연·프라이빗·클라우드 비의존 |
| 일정 | 초기 양산 배포 목표 2026년 하반기 |

출처: [Liquid AI 공식 보도자료](https://www.liquid.ai/press/liquid-ai-and-mercedes-benz-partner-to-scale-embedded-in-car-intelligence), [BusinessWire (2026.4.23)](https://www.businesswire.com/news/home/20260423009970/en/Mercedes-Benz-and-Liquid-AI-Partner-to-Scale-Embedded-In-Car-Intelligence-in-North-America), [Mercedes-Benz Group 공식](https://group.mercedes-benz.com/technology/innovation/collaboration/liquid-ai.html)

**경영진 코멘트:**
- Jörg Burzer (Mercedes-Benz CTO): "Liquid AI와 온디바이스 음성·언어이해·추론을 발전시켜 직관적 차내 경험의 기반을 닦고 있다." ([공식 보도자료](https://www.liquid.ai/press/liquid-ai-and-mercedes-benz-partner-to-scale-embedded-in-car-intelligence))
- Ramin Hasani (Liquid AI CEO): "Liquid 모델은 클라우드 의존 없이 빠르고, 프라이빗하며, 자주적인(sovereign) 지능을 제공한다." (동일 출처)

### 4.2 글로벌 완성차 VLM 배포 사례 연구
> 고객명 미공개. 원문은 **"a global automaker(글로벌 완성차 업체)"**로만 지칭.

| 항목 | 내용 |
|------|------|
| 고객 | 글로벌 완성차 업체 (이름 미공개) |
| 문제 | 차내 실시간 음성·비전 AI 필요. 그러나 **중급(mid-tier) CPU**가 기존 VLM 추론 속도 못 따라감. 자체적으로 **llama.cpp**로 수개월 최적화 시도했으나 추론 느리고 first-token 지연 과다 → UX 악화. 하드웨어 업그레이드 불가 |
| 해결 | Liquid **Edge SDK**로 하드웨어 최적화 커스텀 VLM 제작. 신규 HW 없이 모델 압축·CPU 효율에 집중 |
| 결과 | first-token **10배 빠름**, 모델 크기 **50% 축소(정확도 유지)**, 기존 CPU 배포 성공 |
| 기간 | 양산 가능 솔루션 **1주 만에** 배포 (기존엔 수개월) |

출처: [Liquid AI – Automotive VLM 사례](https://www.liquid.ai/use-cases/accelerating-vision-language-model-deployment-for-automotive-ai)

> 참고: **llama.cpp** = CPU·노트북 등에서 AI 모델을 돌리는 오픈소스 추론 엔진. 고객이 먼저 시도했다 실패한 범용 도구이며, Liquid Edge SDK는 그 대안으로 제시됨. ([llama.cpp GitHub](https://github.com/ggml-org/llama.cpp))

### 4.3 SOAFEE 가입 (차량 생태계 진입)
- Liquid AI가 **SOAFEE Special Interest Group 회원 가입**. ([SOAFEE 발표](https://www.soafee.io/news/2026/liquid-ai-announcement/))
- **SOAFEE** = Scalable Open Architecture for Embedded Edge. ARM 주도, 클라우드 네이티브 개발 방식을 차량 임베디드로 가져오는 SDV(소프트웨어 정의 차량) 표준 이니셔티브.
- 목표: 효율적·확장 가능한 AI로 SDV 개발 가속. **Tier 1·OEM이 클라우드 네이티브 개발 ↔ 임베디드 하드웨어 간극을 메우도록** 기여.

> ⚠️ SOAFEE 발표 페이지는 직접 접근 시 HTTP 403 차단. 위 내용은 WebSearch가 반환한 페이지 요약 기반 — 인용문·정확 날짜는 원문 직접 재확인 필요(본문 미검증).

> **Tier 1 종합:** Tier 1 부품사와의 *개별 명시 협력*은 공식 확인 불가(출처 미확인). 단 SOAFEE 가입으로 Tier 1·OEM 대상 생태계 접근은 공식화. 현재 공개된 OEM 직접 협력 대표 사례는 Mercedes-Benz.

### [비차량] 4.4 기타 파트너십
- **Shopify (이커머스):** 다년(multi-year) 파트너십 발표(2025.11.13). ([블로그 목록](https://www.liquid.ai/company/blog?category=All)) — *세부 내용 본문 미확인, 제목 기준.*
- **AMD + Robotec.ai (로보틱스):** 엣지 에이전틱 로보틱스 — LFM2-VL-3B 시연(2025.10.23). AMD 하드웨어 협력 연장선. ([블로그 목록](https://www.liquid.ai/company/blog?category=All)) — *세부 본문 미확인.*
- **AMD:** Series A 투자 + Instinct GPU 학습/배포, NPU 협력(앞 섹션 참조).

### [적용] 4.5 케이스 스터디 (2025.12.17 공개 묶음)
차량 외 산업 적용 사례. 모두 온디바이스 효율 강조.
- 자동차 VLM 가속 (위 4.2)
- 사기 방지(fraud prevention) — 실시간 속도·정밀
- 상품 카탈로깅용 VLM 최적화
- 스마트폰용 커스텀 번역 모델
- 클라우드 병목 없는 합성 비디오 생성

출처: [Liquid AI 블로그 목록 – Case Studies](https://www.liquid.ai/company/blog?category=All)

> ⚠️ 4.4·4.5는 블로그 *목록의 제목·날짜* 기반. 각 기사 본문은 미열람 — 세부 수치·조건은 원문 재확인 필요.

---

## 5. 최신 기술 동향 요약 (타임라인)

| 시점 | 이벤트 | 출처 |
|------|--------|------|
| 2023.12 | MIT CSAIL 스핀오프 설립, 시드 3,750만 달러 | [TechCrunch](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/) |
| 2024.12 | Series A 2.5억 달러 (AMD 주도 보도, 유니콘 진입 보도) | [공식 블로그](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai) |
| 2024.9.30 | LFM v1 공개 (1세대, 1.3B/3B/40B-MoE) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.7.10 | LFM2 공개 (온디바이스 소형 모델) | [LFM2 블로그](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models) |
| 2025.7.15 | LEAP + Apollo 출시 | [공식 보도자료](https://www.liquid.ai/press/liquid-ai-launches-leap-and-apollo-a-new-era-for-edge-ai-deployment-begins) |
| 2025.8.18 | LEAP 노트북 확장 (AMD Ryzen) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.9.25 | Nanos 공개 (작업 특화 극소형 6종, 350M~1.2B) | [Nanos 보도자료](https://www.liquid.ai/press/liquid-unveils-nanos-extremely-small-foundation-models-that-match-frontier-model-quality--running-directly-on-everyday-devices) |
| 2025.10.7 | LFM2-8B-A1B 공개 (온디바이스 MoE) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.10.22 | LFM2-VL-3B (비전언어), ExecuTorch 통합 | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.10.23 | AMD·Robotec.ai 엣지 로보틱스 시연 (LFM2-VL-3B) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.10.28 | LFM2-ColBERT-350M (검색) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.11.13 | Shopify 다년 파트너십 | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.12.4 | Liquid Labs 출범 | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2025.12.17 | 케이스 스터디 5종 공개 (차량·사기방지·카탈로그·번역·비디오) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.1.5 | LFM2.5 공개 (28T 토큰, 텍스트·비전·오디오, 온디바이스 에이전트) | [LFM2.5 블로그](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai) |
| 2026.1.20 | LFM2.5-1.2B-Thinking (추론 특화, 1GB 미만) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.2.24 | LFM2-24B-A2B 공개 (최대 모델, MoE, AI PC) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.3.31 | LFM2.5-350M (초소형) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.4.8 | LFM2.5-VL-450M (비전언어) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.4.23 | Mercedes-Benz 다년 파트너십 (북미 차내 온디바이스 AI) | [공식 보도자료](https://www.liquid.ai/press/liquid-ai-and-mercedes-benz-partner-to-scale-embedded-in-car-intelligence) |
| 2026.5.28 | LFM2.5-8B-A1B (MoE 개선판) | [블로그 목록](https://www.liquid.ai/company/blog?category=All) |
| 2026.6.18 | LFM2.5 Retrievers (검색, 첫 양방향 LFM) | [Retrievers 블로그](https://www.liquid.ai/blog/lfm2-5-retrievers) |
| 2026 (시기 미확인) | SOAFEE 가입 (차량 SDV 생태계) | [SOAFEE 발표](https://www.soafee.io/news/2026/liquid-ai-announcement/) — *본문 미검증* |

---

## 6. 확인 불가 / 주의 항목
- **직원 수·매출:** 공식 비공개. (출처 미확인)
- **밸류에이션 23.5억 달러, 리드 투자자 AMD:** 언론 보도 기반이며 Liquid AI 공식 문서에는 미명시.
- **임원 직함(CTO/CSO):** 서드파티(cbinsights 등) 기반. 공식 확정 권장.
- **Tier 1 부품사 협력:** 공식 확인된 사례 없음. 현재 확인된 차량 협력은 OEM Mercedes-Benz 중심.
