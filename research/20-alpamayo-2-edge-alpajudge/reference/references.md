# 출처 기록 — NVIDIA Alpamayo 2 Edge · AlpaJudge

> **작성일(접근일)**: 2026-11-12 (KST), 2판  
> **등급**: 📄 기사 본문(직접 열람) · 🔍 기사가 링크한 1차 자료를 직접 열어 확인 · 🔗 URL만 기록(미열람)  
> 번호는 본 보고서 [`../alpamayo-2-edge-alpajudge.md`](../alpamayo-2-edge-alpajudge.md)의 인라인 인용 번호와 일치한다.

## 수집 방법

기사 1건의 HTML 원문을 2026-11-12에 내려받아 본문·표·코드·캡션을 추출했다. 2판에서는 기사가 링크한 1차 자료 중 Alpamayo 2 Edge 모델 카드와 GitHub README, Alpamayo 2 Super 모델 카드와 소개 블로그, AlpaJudge 모델 카드와 GitHub README, DFlash GitHub README, alpamayo-recipes의 허브 README와 Thor 배포 레시피 README를 직접 열어 교차 확인했다. 용어 풀이·Super 대비 비교·하네스 구성·지연 단계별 수치는 이들 1차 자료에서 가져왔다. 기사 안의 파트너 3사(PORT·Niulinx·Embedl) 수치는 각 사의 자체 평가 인용이다. 기사 상단의 NVIDIA Nemotron 생성 요약은 본문과 대조해 보조 참고로만 썼다.

## 그림

`../images/`의 5장은 기사 원본 도식이며 저작권은 NVIDIA에 있다(인용 목적). 원본 URL:

| 파일 | 기사 그림 | 원본 URL |
|---|---|---|
| fig1-architecture.webp | Figure 1. Alpamayo 2 Edge 아키텍처 | https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image7-3.webp |
| fig2-benchmarks.webp | Figure 2. Alpamayo 2 Edge vs Qwen-Drive-1.0 벤치마크 | https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image3-8.webp |
| fig3-notebook-frames.webp | Figure 3. 예제 노트북 클립 카메라 프레임 | https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-2.webp |
| fig4-data-curation.webp | Figure 4. 점수 기반 데이터 큐레이션 루프 | https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image8-4.webp |
| fig5-rl-reward.webp | Figure 5. AlpaJudge 보상 효과 | https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image2-6.webp |

기사에 포함된 영상 2편(Niulinx 실차 시연, Embedl 최적화 전후 비교)은 저장하지 않았다.

## 출처 목록


1. 📄 NVIDIA Technical Blog — Running AV Reasoning Models Within Onboard Compute and Latency Limits (Marco Pavone, Boris Ivanovic) — 2026-11-10 — https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/
2. 🔍 Hugging Face — nvidia/Alpamayo2-Edge 모델 카드 (파라미터 구성·입출력·벤치마크·메모리·라이선스) — 2026-11-10 공개 — https://huggingface.co/nvidia/Alpamayo2-Edge
3. 🔍 GitHub NVlabs/alpamayo2-edge — README (추론 코드, 입력 프로필, 가속 옵션) — https://github.com/NVlabs/alpamayo2-edge
4. 🔍 Hugging Face — nvidia/Alpamayo2-Super 모델 카드 (34B 구성·입출력·평가) — 2026-08-04 공개 — https://huggingface.co/nvidia/Alpamayo2-Super
5. 🔍 NVIDIA Technical Blog — Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super — https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/
6. 🔍 GitHub NVlabs/alpajudge — README (RB·RF 입력 계약, 점수 공식, 한계) — https://github.com/NVlabs/alpajudge
7. 🔍 Hugging Face — nvidia/alpajudge 모델 카드 (체크포인트 2종, 라이선스) — https://huggingface.co/nvidia/alpajudge
8. 🔍 GitHub z-lab/dflash — README (DFlash·DFlash 2 개요, 지원 모델) — https://github.com/z-lab/dflash
9. 🔗 arXiv 2602.06036 — DFlash: Block Diffusion for Flash Speculative Decoding (Chen, Liang, Liu) — 2026 — https://arxiv.org/abs/2602.06036
10. 🔍 GitHub NVlabs/alpamayo-recipes — README (Alpamayo Developer Hub, 모델 가족·레시피 목록) — https://github.com/NVlabs/alpamayo-recipes
11. 🔍 GitHub NVlabs/alpamayo-recipes — recipes/alpamayo2edge_edgellm/README.md (Thor 배포 레시피, 단계별 지연, 하네스 구성) — https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo2edge_edgellm/README.md
12. 🔗 GitHub NVlabs/alpagym — AlpaGym 폐루프 RL 프레임워크 — https://github.com/NVlabs/alpagym
13. 🔗 GitHub NVlabs/alpamayo-recipes — recipes/alpamayo1_x_rl/README.md (GRPO RL 레시피) — https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_x_rl/README.md
14. 🔗 NVIDIA Developer Forums — Alpamayo 포럼 — https://forums.developer.nvidia.com/c/autonomous-vehicles/alpamayo/766
15. 🔗 NVIDIA — Cosmos 소개 페이지 — https://www.nvidia.com/en-us/ai/cosmos/
