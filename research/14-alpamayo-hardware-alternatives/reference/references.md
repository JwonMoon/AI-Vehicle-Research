# 출처 목록 — Alpamayo를 돌릴 DRIVE Thor 대안 하드웨어

> **열람일**: 2026-09-29 · ID는 [보고서](../alpamayo-hardware-alternatives.md)의 인용 표기와 같다.
>
> **등급**: 💻 저장소 raw 파일 직접 확인 · 🔍 1차 페이지 직접 열람(GitHub 이슈·PR 등) · 📚 이 저장소의 앞선 보고서가 직접 열람해 기록(열람일 병기) · 📰 웹 검색 요약·제목만 확인 · ✅ 교차 확인 · ⚠️ 미확인
>
> **조사 환경 제약**: nvidia.com·developer.nvidia.com·forums.developer.nvidia.com·docs.nvidia.com·huggingface.co·arxiv.org·리셀러 사이트는 세션 네트워크 정책으로 원문 접근이 차단됐다. 해당 출처는 📚 또는 📰로 표시했다.

## [M] 모델·런타임 (32건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| M1 | NVlabs/alpamayo README (Alpamayo 1 / R1-10B) | https://raw.githubusercontent.com/NVlabs/alpamayo/main/README.md | main, 2026-09-29 | 💻 |
| M2 | NVlabs/alpamayo1.5 README · notebooks/inference_nav.ipynb · src/alpamayo1_5/diffusion/flow_matching.py | https://github.com/NVlabs/alpamayo1.5 | main, 2026-09-29 | 💻 |
| M3 | NVlabs/alpamayo2 README (Alpamayo 2 Super) | https://raw.githubusercontent.com/NVlabs/alpamayo2/main/README.md | main, 2026-09-29 | 💻 |
| M4 | nvidia/Alpamayo2-Super 모델카드 (34B, bf16, H100 80GB, 72,115 MiB, "other GPU architectures not yet validated") | https://huggingface.co/nvidia/Alpamayo2-Super | 2026-08-04 | 📚(Thor 배포편 2026-09-15 열람) · 📰 |
| M5 | autowarefoundation/alpamayo-autoware README — alpamayo1.5 브랜치 · alpamayo2.0-super 브랜치 | https://raw.githubusercontent.com/autowarefoundation/alpamayo-autoware/alpamayo1.5/README.md · https://raw.githubusercontent.com/autowarefoundation/alpamayo-autoware/alpamayo2.0-super/README.md | 2026-04-23 · 2026-08-06 | 💻 |
| M6 | TensorRT Edge-LLM 문서 — support-matrix.md · supported-models.md · installation.md (커밋 e8b2952, v0.10.1) | https://github.com/NVIDIA/TensorRT-Edge-LLM/tree/main/docs/source/user_guide/getting_started | 2026-09-03 | 💻 |
| M7 | TensorRT Edge-LLM 문서 — examples/vla/alpamayo.md (Alpamayo-R1-10B 워크플로, "Only FP16 is supported") | https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/examples/vla/alpamayo.md | 2026-09-03 | 💻 |
| M8 | FlashDrive 논문 (arXiv 2608.12932) — GPU별 지연표(Jetson Thor·3090·4090·5090·RTX PRO 6000), 메모리 31.6→18.3 GB | https://arxiv.org/abs/2608.12932 | 2026-08-13 | 📚(Thor 배포편·FlashDrive 분석 열람) · 📰(3090/4090 다중 샘플 행) |
| M9 | z-lab/flashdrive README (요구 사양 CC 8.0+, W4A8 Marlin, RTX PRO 6000 단계별 지연) | https://raw.githubusercontent.com/z-lab/flashdrive/main/README.md | 2026-09-29 | 💻 |
| M10 | Alpamayo-R1 논문 (arXiv 2511.00088) — RTX 6000 Pro Blackwell 99 ms / 29 ms | https://arxiv.org/abs/2511.00088 | 2025-11 | 📚(Thor 배포편) · 📰 |
| M11 | NVlabs/alpamayo-recipes — recipes/alpamayo1_5_quant/README.md (FP8 11 GB, AutoQuant 9 GB, RTX 5090/B300 테스트) | https://raw.githubusercontent.com/NVlabs/alpamayo-recipes/main/recipes/alpamayo1_5_quant/README.md | 2026-09-29 | 💻 |
| M12 | NVIDIA NIM Alpamayo 1.5 — prerequisites · support-matrix (BF16 30 GB, 양자화 20 GB, FP8 CC 8.9+, A100 미검증, x86 호스트) | https://docs.nvidia.com/nim/alpamayo/latest/prerequisites.html · https://docs.nvidia.com/nim/alpamayo/1.0.0/support-matrix.html | 2026-08-27 | 📰 |
| M13 | NVIDIA 포럼: How to perform Alpamayo1.5 fp8 quantization for Nvidia Thor (382409) — "No real-quant GEMM found", 평가 시간 424/455 s/clip, NVIDIA 답변 요지 | https://forums.developer.nvidia.com/t/how-to-perform-alpamayo1-5-fp8-quantization-for-nvidia-thor/382409 | 2026-09 | 📚(2026-09-15 열람) · 📰 |
| M14 | TensorRT Edge-LLM 이슈 #130 Alpamayo Support(1.5 요청, open, 무응답) · #134 Support for Quantized Alpamayo Export · #166 Jetson Thor export 오류(0.10.1에서 수정) · #92 action 엔진 플러그인 · Discussion #155(Orin은 양자화 호스트 불가) | https://github.com/NVIDIA/TensorRT-Edge-LLM/issues/130 · /issues/134 · /issues/166 · /issues/92 · /discussions/155 | 2026-05~09 | 🔍 |
| M15 | NVlabs/alpasim docs/ONBOARDING.md (Alpamayo1.5 프리셋 약 96 GB VRAM) | https://raw.githubusercontent.com/NVlabs/alpasim/main/docs/ONBOARDING.md | 2026-09-29 | 💻 |
| M16 | NVlabs/alpagym README (10B는 GPU 2장) · AlpaGym 블로그(RTX 6000 Ada 2장 스모크, 40 GB+ 권장) | https://raw.githubusercontent.com/NVlabs/alpagym/main/README.md · https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/ | 2026 | 💻 · 📚(03 요구사항 보고서 2026-07-15 열람) |
| M17 | Latency Analysis and Optimization of Alpamayo 1 via Efficient Trajectory Generation (arXiv 2605.08975) — DGX Spark GB10, 6궤적 13.33→4.10 s | https://arxiv.org/abs/2605.08975 | 2026-05-09 | 📰 |
| M18 | OOM-Free Alpamayo via CPU-GPU Memory Swapping (arXiv 2605.11678) — RTX 5070 Ti 16 GB, R1 21.52 GB, UVM 69.6 s, 최대 3.55×, RTX 5090 1.03 s | https://arxiv.org/abs/2605.11678 | 2026-05-12 | 📰 |
| M19 | TensorRT Edge-LLM Releases v0.10.1(2026-09-03) · v0.7.1(Alpamayo-1 추가) · CHANGELOG.md | https://github.com/NVIDIA/TensorRT-Edge-LLM/releases | 2026-09-03 | 🔍 · 💻 |
| M20 | TensorRT Edge-LLM 문서 — performance/performance-benchmarks.md v0.10.0 (Jetson AGX Thor·AGX Orin 64GB·DGX Spark, Qwen3-VL-8B INT4 AWQ/NVFP4 배치 1; Alpamayo 행 없음) | https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/performance/performance-benchmarks.md | 2026-09-03 | 💻 |
| M21 | NVIDIA Tech Blog: Build Next-Gen Physical AI with Edge-First LLMs ("On DRIVE Thor, Alpamayo 1 achieves production-viable latencies", FP8 ViT) | https://developer.nvidia.com/blog/build-next-gen-physical-ai-with-edge%E2%80%91first-llms-for-autonomous-vehicles-and-robotics/ | 2026-03-12 | 📚(Thor 배포편) · 📰 |
| M22 | NVIDIA Newsroom: Alpamayo 2 Super for Robotaxis (DRIVE AGX Thor로 증류) | https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis | 2026-05-31 | 📚 · 📰 |
| M23 | bimalmagar10/alpamayo-xavier — R1을 AGX Xavier 32GB(JetPack 5.1.7)에 TensorRT FP16/INT8로 이식, 지연 수치 없음 | https://github.com/bimalmagar10/alpamayo-xavier | 2026 | 🔍 |
| M24 | 00-YSH-E2E/YSH-Inference-Alpamayo-1.5 — Jetson AGX Thor·Orin 계측용 포크(bf16, SDPA), 수치 미공개 | https://github.com/00-YSH-E2E/YSH-Inference-Alpamayo-1.5 | 2026 | 🔍 |
| M25 | NVlabs/alpamayo 이슈 #69 Current limitations ("AGX Orin 64GB가 최소 사양인가", 무응답) | https://github.com/NVlabs/alpamayo/issues/69 | 2026-04-19 | 🔍 |
| M26 | NVIDIA/Model-Optimizer examples/alpamayo/README.md (Alpamayo 1 FP8/NVFP4/AutoQuantize) | https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/alpamayo/README.md | 2026 | 🔍 |
| M27 | NVIDIA 포럼: Spark DGX Alpamayo + Alpasim (357383) — "부분 동작, Spark 단일 노드 구조와 부정합" | https://forums.developer.nvidia.com/t/spark-dgx-alpamayo-alpasim/357383 | 2025-11~12(추정) | 📰 |
| M28 | NVIDIA 포럼: Build alpamayo1_5 native on Thor (382647) — PyTorch 소스 빌드, SDPA, jtop 14.5 GB | https://forums.developer.nvidia.com/t/build-alpamayo1-5-native-on-thor/382647 | 2026-09 | 📚(2026-09-15 열람) · 📰 |
| M29 | Dao-AILab/flash-attention 이슈 #1969 — sm_121(GB10) 휠 없음, 소스 빌드 실패, eager attention 사용 | https://github.com/Dao-AILab/flash-attention/issues/1969 | 2025-10-28 | 🔍 |
| M30 | dusty-nv/jetson-containers 이슈 #1220 — AGX Orin flash-attn "no kernel image", sm_87 미포함 PyTorch 빌드 | https://github.com/dusty-nv/jetson-containers/issues/1220 | 2025 | 🔍 |
| M31 | NVIDIA 포럼: Alpamayo-R1-10B TensorRT engine OOM on DRIVE AGX Thor (382500) · Drive AGX thor with Alpamayo (382501) — DriveOS 7.2.5.0, CUDA 13.3, TensorRT 11.0.1, 15.17 GB 요청 OOM, 미해결 | https://forums.developer.nvidia.com/t/alpamayo-r1-10b-tensorrt-engine-oom-on-drive-agx-thor/382500 · https://forums.developer.nvidia.com/t/drive-agx-thor-with-alpamayo/382501 | 2026-09-06~13 | 📚(2026-09-15 열람) · 📰 |
| M32 | pytorch/TensorRT PR #4732 Alpamayo Edge exporter support (Alpamayo 1.5 unified Edge exporter) | https://github.com/pytorch/TensorRT/pull/4732 | 2026 | 📰 |

## [J] Jetson (13건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| J1 | Jetson Thor Series Modules Data Sheet DS-11945-001 v1.5 (T5000·T4000 사양) | https://developer.nvidia.com/downloads/assets/embedded/secure/jetson/thor/docs/jetson-thor-series-modules-datasheet_ds-11945-001.pdf | 2026-06-01 | 📚(Thor 배포편 2026-09-15 열람) |
| J2 | JetPack 7.0 / 7.2 / 7.2.1 발표(포럼·다운로드 페이지) — CUDA·TensorRT 버전, MIG 프리뷰 | https://forums.developer.nvidia.com/t/jetpack-7-2-jetson-software-goes-agentic-with-jetson-linux-39-2/372056 · https://developer.nvidia.com/embedded/jetpack/downloads | 2025-08~2026-08 | 📚 |
| J3 | Jetson AGX Thor 개발킷 $3,499 (NVIDIA 뉴스룸·CNX Software·Hackster) | https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics · https://www.cnx-software.com/2025/08/19/3499-nvidia-jetson-agx-thor-developer-kit-2070-tops-jetson-t5000-som-for-robotics-and-edge-ai/ · https://www.hackster.io/news/nvidia-tells-resellers-to-open-jetson-agx-thor-developer-kit-orders-at-3-499-06e8cbf52441 | 2025-08-25 | ✅(📚·📰) |
| J4 | Autoware PR #7108 Support NVIDIA Thor (Jetson + DRIVE) — Jetson Thor에서만 검증 | https://github.com/autowarefoundation/autoware/pull/7108 | 2026-05-15 | 📚 |
| J5 | Jetson AGX Orin 제품 페이지·기술 브리프 (2,048 CUDA 코어, 275 TOPS, 204.8 GB/s, NVDLA 2.0 ×2, 15~60 W) | https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/ · https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf | — | 📰 |
| J6 | JetPack 6.2 / 6.2.2 (CUDA 12.6, TensorRT 10.3, Ubuntu 22.04) | https://developer.nvidia.com/embedded/jetpack-sdk-62 · https://developer.nvidia.com/embedded/jetpack-sdk-622 | 2025 | 📰 |
| J7 | JetPack 7.2의 Orin 지원 (Seeed 블로그, Connect Tech, 포럼 "Orin AGX, JP 7.2, Pytorch and sm_87 support?") | https://www.seeedstudio.com/blog/2026/07/09/jetpack-7-2-platform-level-reset-and-the-new-era-of-agentic-ai/ · https://forums.developer.nvidia.com/t/orin-agx-jp-7-2-pytorch-and-sm-87-support/378368 | 2026-07 | 📰 |
| J8 | Jetson T4000 사양 — NVIDIA Tech Blog(T4000·JetPack 7.1) · EDOM · OpenZeka | https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ · https://www.edomtech.com/en/product-detail/nvidia-jetson-t4000-module/ | 2026-01 | 📚(Thor 배포편) · 📰 |
| J9 | T4000용 파트너 캐리어 — Seeed reComputer J601 · Forecr DSBOARD-THRMAX · AVerMedia D331 · Axiomtek AIE015-AT | https://www.seeedstudio.com/reComputer-J601-Carrier-Board-for-Jetson-AGX-Thortm-T5000-T4000.html · https://www.forecr.io/products/nvidia-jetson-thor-carrier-board-dsboard-thrmax · https://linuxgizmos.com/axiomtek-previews-jetson-thor-t5000-t4000-developer-kit-for-robotics-systems/ | 2026 | 📰 |
| J10 | Jetson Orin Nano Super(8 GB, 102 GB/s, 67 TOPS) · Orin NX 16GB(102.4 GB/s, 157 TOPS) | https://developer.nvidia.com/blog/nvidia-jetson-orin-nano-developer-kit-gets-a-super-boost/ · https://developer.nvidia.com/blog/nvidia-jetpack-6-2-brings-super-mode-to-nvidia-jetson-orin-nano-and-jetson-orin-nx-modules/ | 2024-12 · 2025-01 | 📰 |
| J11 | Jetson AGX Thor vLLM 벤치마크(Llama 3.1 8B 41.3 tok/s) · Jetson AI Lab 벤치마크 | https://developer.nvidia.com/embedded/jetson-benchmarks · https://developer.nvidia.com/blog/unlock-faster-smarter-edge-models-with-7x-gen-ai-performance-on-nvidia-jetson-agx-thor/ | 2025-10 | 📚(Thor 배포편) · 📰 |
| J12 | PyTorch 2.8 wheel for JetPack 6.2 (포럼) · pypi.jetson-ai-lab.io/jp6/cu126 | https://forums.developer.nvidia.com/t/pytorch-2-8-wheel-for-jetpack-6-2/341339 | 2025 | 📰 |
| J13 | NVIDIA, LPDDR4 Jetson 모듈(TX2·Xavier) EOL 공지 (CNX Software) | https://www.cnx-software.com/2026/04/30/nvidia-phases-out-several-jetson-modules-due-to-high-lpddr4-ram-prices-and-tight-supplies/ | 2026-04-30 | 📰 |

## [D] DRIVE (14건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| D1 | NVIDIA DRIVE AGX Thor Development Platform (PDF) — SKU10/12, 64 GB, I/O, 안전 MCU, Developer Program | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | 2025-12 | 📚(Thor 배포편) |
| D2 | DriveOS 7.2.5 Now Available (포럼) — CUDA 13.3, TensorRT 11, Edge-LLM 포함 | https://forums.developer.nvidia.com/t/announcement-from-nvidia-nvidia-driveos-7-2-5-now-available/379371 | 2026-08-06 | 📚 |
| D3 | 포럼: Alpamayo-R1-10B TensorRT engine OOM on DRIVE AGX Thor (382500) | https://forums.developer.nvidia.com/t/alpamayo-r1-10b-tensorrt-engine-oom-on-drive-agx-thor/382500 | 2026-09-06~13 | 📚 · 📰 |
| D4 | 포럼: Drive AGX thor with Alpamayo (382501) — CUDA 가용 6.0 GiB · NVidia Drive Detailed Specs (352616) — 15,018 MB | https://forums.developer.nvidia.com/t/drive-agx-thor-with-alpamayo/382501 · https://forums.developer.nvidia.com/t/nvidia-drive-detailed-specs/352616 | 2026-09 · 2025-11 | 📚 · 📰 |
| D5 | DRIVE AGX Orin 개발킷 — developer.nvidia.com/drive/agx · Arrow 제품 브리프 · 포럼 "Drive AGX Orin Development Kit Specifications" | https://developer.nvidia.com/drive/agx · https://forums.developer.nvidia.com/t/drive-agx-orin-development-kit-specifications/237226 | — | 📰 |
| D6 | Arrow: NVIDIA DRIVE AGX Orin Developer Kit 940-63710-0010-300 (MSRP $7,500) | https://www.arrow.com/en/products/940-63710-0010-300/nvidia.html | 2026-09-29 확인 | 📰 |
| D7 | 포럼: DRIVE OS 6.0.10.0 is now available (CUDA 11.4, TensorRT 8.6.13, cuDNN 8.9.2) | https://forums.developer.nvidia.com/t/announcement-from-nvidia-drive-os-6-0-10-0-is-now-available/303314 | 2024~2025 | 📰 |
| D8 | 포럼: PyTorch with GPU on DRIVE AGX Orin (253407) · DRIVE AGX Orin upgraded to 6.0.10 but no CUDA PyTorch (305928) · Installation of PyTorch with CUDA on DRIVE Orin (346369) — "PyTorch is not officially supported on DRIVE" | https://forums.developer.nvidia.com/t/pytorch-with-gpu-on-drive-agx-orin/253407 · https://forums.developer.nvidia.com/t/installation-of-pytorch-with-cuda-support-on-drive-orin/346369 | 2023~2025 | 📰 |
| D9 | 포럼: ETA for DriveOS 7.x supporting Drive AGX Orin (356123) · Drive OS 7 for Orin (354068) | https://forums.developer.nvidia.com/t/eta-for-driveos-7-x-supporting-drive-agx-orin/356123 | 2026-01 | 📰 |
| D10 | 포럼: Where to find DriveOS release documentation for TensorRT Edge-LLM on DRIVE Thor (364838) — "DriveOS LLM SDK는 TensorRT 8.6 미지원, Orin·DriveOS 6 불가" | https://forums.developer.nvidia.com/t/where-to-find-the-driveos-release-documentation-for-tensorrt-edge-llm-on-drive-thor/364838 | 2026 | 📰 |
| D11 | NVIDIA DRIVE FAQ — DRIVE AGX SDK Developer Program은 계약·초청 기반 | https://developer.nvidia.com/drive/faq | — | 📰 |
| D12 | NVIDIA Blog: DRIVE AGX Thor Developer Kit GA — Tier-1(Continental·Desay SV·Lenovo·Magna·Quanta) 양산 시스템 | https://blogs.nvidia.com/blog/drive-agx-developer-kit-general-availability | 2025-08-25 | 📚 · 📰 |
| D13 | NVIDIA Newsroom: Uber 로보택시 — Hyperion 10, DRIVE AGX Thor SoC 2개, 2,000 FP4 TFLOPS | https://nvidianews.nvidia.com/news/nvidia-uber-robotaxi | 2025-10 | 📰 |
| D14 | Lenovo AD1 on DRIVE AGX Thor (Lenovo 뉴스룸) · Desay SV IPU14 (Thor-U) | https://news.lenovo.com/pressroom/press-releases/lenovo-works-with-swm-to-develop-next-generation-robotaxi-on-nvidia-drive-agx-thor/ | 2026-03-04 | 📰 |

## [G] 데스크톱·워크스테이션 GPU·DGX Spark (13건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| G1 | RTX 3090 사양 (24 GB GDDR6X 936 GB/s, 350 W, $1,499, Ampere FP8 없음) | https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/ · https://wccftech.com/nvidia-geforce-rtx-3090-24-gb-official-launch-price-specs-performance/ | 2020-09 | 📰 |
| G2 | RTX 4090 사양·단종 (24 GB 1,008 GB/s, 450 W, $1,599; 2024-10 공급 종료) | https://en.wikipedia.org/wiki/GeForce_RTX_40_series · https://www.tweaktown.com/news/100896/nvidia-is-discontinuing-the-geforce-rtx-4080-and-4090-to-make-way-for-50-series/index.html | 2022~2024 | 📰 |
| G3 | RTX 4080 Super 사양 (16 GB, 736 GB/s, 320 W, $999) | https://www.techpowerup.com/review/nvidia-geforce-rtx-4080-super-founders-edition/ | 2024-01 | 📰 |
| G4 | RTX 5090 / 5080 / 5070 Ti 사양 (32/16/16 GB GDDR7, 1,792/960/896 GB/s, 575/360/300 W, $1,999/$999/$749) | https://gamersnexus.net/gpus/nvidia-rtx-5090-575-watts-rtx-5080-5070-ti-5070-specs | 2025-01 | 📰 |
| G5 | RTX 6000 Ada 사양 (48 GB GDDR6 ECC 960 GB/s, 300 W, MSRP 약 $6,800) | https://www.thundercompute.com/blog/nvidia-rtx-6000-ada-pricing · https://gpucost.org/gpu/rtx-6000-ada | 2026 | 📰 |
| G6 | RTX PRO 4500 Blackwell 사양 (32 GB GDDR7 ECC 896 GB/s, 200 W) | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-4500/ · https://www.spheron.network/blog/nvidia-rtx-pro-4500-blackwell-specs-and-cloud-pricing-2026/ | 2025~2026 | 📰 |
| G7 | RTX PRO 5000 Blackwell 48 GB / 72 GB (1,344 GB/s, 300 W; 72 GB 2025-12 조용히 출시, 공식가 미발표) | https://videocardz.com/newz/nvidia-quietly-launches-rtx-pro-5000-blackwell-workstation-card-with-72gb-of-memory · https://www.cgchannel.com/2025/12/nvidia-launches-new-72gb-rtx-pro-5000-blackwell-gpu/ | 2025-12 | 📰 |
| G8 | RTX PRO 6000 Blackwell Workstation / Max-Q 데이터시트 (96 GB GDDR7 ECC 1,792 GB/s, 600/300 W) | https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/rtx-pro-6000-blackwell-workstation-edition/workstation-blackwell-rtx-pro-6000-workstation-edition-nvidia-us-3519208-web.pdf | 2025 | 📰 |
| G9 | DGX Spark 제품 페이지·리뷰 (GB10, 6,144 CUDA 코어, 128 GB LPDDR5X 273 GB/s, 1 PFLOP NVFP4, SM121) | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ · https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/ · https://hothardware.com/reviews/nvidia-dgx-spark-hands-on | 2025-10 | 📰 |
| G10 | DGX Spark 파트너 시스템 (ASUS Ascent GX10, Gigabyte AI TOP Atom, Lenovo ThinkStation PGX, HP ZGX Nano, Dell Pro Max GB10) | https://eshop.asus.com/us/ascent-gx10.html · https://www.servethehome.com/lenovo-thinkstation-pgx-review-the-nvidia-gb10-128gb-ai-workstation-goes-corporate/4/ · https://www.hp.com/us-en/workstations/zgx-nano-ai-station.html | 2026 | 📰 |
| G11 | jethac/dgx-spark-hijinks — PYTORCH_SM121_SUPPORT.md (PyTorch 2.9+ sm_121 기준, sm_120 바이너리 호환) · 포럼 "Request for sm_121-tuned kernels" | https://github.com/jethac/dgx-spark-hijinks/blob/main/docs/PYTORCH_SM121_SUPPORT.md · https://forums.developer.nvidia.com/t/request-for-sm-121-tuned-kernels-in-cudnn-cublas-dgx-spark-training-throughput-gap/371094 | 2026 | 🔍 · 📰 |
| G12 | flash-attention 이슈 #1969 sm_121 (= M29) · vLLM SM121 빌드 PR #31740 | https://github.com/Dao-AILab/flash-attention/issues/1969 · https://github.com/vllm-project/vllm/pull/31740 | 2025-10~2026 | 🔍 · 📰 |
| G13 | vLLM Marlin W4A8 PR #24722 · avesed/vllm-ampere-optimized ("vLLM은 W4A8을 Hopper로 게이팅, Ampere는 W4A16") | https://github.com/vllm-project/vllm/pull/24722 · https://github.com/avesed/vllm-ampere-optimized | 2025~2026 | 📰 |

## [C] 데이터센터 GPU·클라우드 (12건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| C1 | H100 PCIe vs SXM 사양 (80 GB, 2.0/3.35 TB/s, 350/700 W, FP8) | https://www.hyperstack.cloud/technical-resources/performance-benchmarks/comparing-nvidia-h100-pcie-vs-sxm-performance-use-cases-and-more | 2025~2026 | 📰 |
| C2 | H200 사양·가격 (141 GB HBM3e 4.8 TB/s; $30~40k; RunPod $4.59, Nebius $4.50, AWS p5e $39.8/h) | https://jarvislabs.ai/blog/h200-price · https://www.runpod.io/articles/guides/nvidia-h200-gpu | 2026-08 | 📰 |
| C3 | A100 80 GB 사양·가격 (HBM2e, FP8 없음; 신품 $7~15k, 중고 $4~9k; RunPod $1.59, Vast $1.09) | https://jarvislabs.ai/blog/a100-price · https://www.spheron.network/blog/l40s-vs-a100/ | 2026 | 📰 |
| C4 | L40S 사양·가격 (48 GB GDDR6 864 GB/s, 350 W, FP8; $5,999~7,569) | https://www.nvidia.com/en-us/data-center/l40s/ · https://gpudojo.com/l40s | 2026 | 📰 |
| C5 | RTX PRO 6000 Blackwell Server Edition (96 GB, 1.6 TB/s, 600 W) | https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/ · https://lenovopress.lenovo.com/lp2263-thinksystem-nvidia-rtx-pro-6000-blackwell-server-edition-pcie-gen5-gpu | 2025 | 📰 |
| C6 | AWS EC2 G7e (RTX PRO 6000 Server) g7e.2xlarge $3.3631/h · B200/B300 시세(Lambda $6.69, getdeploying 중앙값 $6.49) | https://aws.amazon.com/ec2/instance-types/g7e/ · https://instances.vantage.sh/aws/ec2/g7e.2xlarge · https://getdeploying.com/gpus/nvidia-b200 | 2026-09 | 📰 |
| C7 | AWS p5.48xlarge (8× H100) $55.04/h · GCP a3-highgpu-8g $87.8~88.5/h · Azure ND96isr H100 v5 $98.32/h | https://instances.vantage.sh/aws/ec2/p5.48xlarge · https://instances.vantage.sh/gcp/a3-highgpu-8g · https://instances.vantage.sh/azure/vm/nd96isrh100-v5 | 2026 | 📰 |
| C8 | AWS g6e.xlarge (1× L40S) $1.861/h | https://instances.vantage.sh/aws/ec2/g6e.xlarge | 2026 | 📰 |
| C9 | Lambda 가격 (H100 SXM $3.99, PCIe $3.29, B200 $6.69) | https://lambda.ai/pricing · https://www.spheron.network/blog/lambda-cloud-h100-pricing-2026/ | 2026 | 📰 |
| C10 | RunPod 가격 (H100 PCIe $2.89 / SXM $3.49, A100 $1.59, L40S $1.09, RTX PRO 6000 $2.09) | https://www.runpod.io/pricing · https://gpuperhour.com/providers/runpod | 2026 | 📰 |
| C11 | Vast.ai 시세 (H100 SXM 중앙값 $2.25, RTX PRO 6000 $0.93~1.40) | https://computeprices.com/providers/vast | 2026-09 | 📰 |
| C12 | RTX A6000 중고가 ($2,600~3,800 / eBay $4,500~4,999 / gpudojo $4,400~) | https://gpudojo.com/a6000 · https://electronics.alibaba.com/product/used-a6000-gpu | 2026-09 | 📰 |

## [P] 가격·시세 (21건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| P1 | ICBanq: NVIDIA Jetson AGX Thor Developer Kit 국내 정품 (540만 원, VAT 포함 594만 원) | https://www.icbanq.com/P016786968 | 2026-09-29 확인 | 📰 |
| P2 | NVIDIA, Jetson 모듈·개발킷 가격 최대 101% 인상 (CNX Software · VideoCardz · Hackster · JetsonHacks) — AGX Orin 개발킷 $1,999→$3,499, AGX Orin 64GB 모듈 $2,999, 32GB $899→$1,799, AGX Thor 개발킷 $3,499→$5,499, T4000 $2,999, Orin Nano Super $249→$399 | https://www.cnx-software.com/2026/07/22/nvidia-increases-the-price-of-jetson-modules-and-devkits-by-up-to-101/ · https://videocardz.com/newz/nvidia-raises-jetson-prices-by-up-to-101-agx-thor-now-costs-5499 · https://www.hackster.io/news/nvidia-hikes-jetson-pricing-by-up-to-101-as-the-company-gets-caught-out-by-its-own-ai-bubble-91701d7c5783 | 2026-07-22 | 📰 |
| P3 | Hackster: Jetson AGX Orin Developer Kit $1,999 출시 | https://www.hackster.io/news/nvidia-launches-275-tops-jetson-agx-orin-developer-s-kit-at-1-999-bbb5ff80e050 | 2022-03 | 📰 |
| P4 | ICBanq: Jetson AGX Orin 64GB Developer Kit 국내가 (462만 원 VAT 별도 / 560만 원) | https://www.icbanq.com/P015243419 · https://www.icbanq.com/P015198223 | 2026-09-29 확인 | 📰 |
| P5 | RTX 5090 2026-09 시세 — ThinkComputers(소매 $5,000 돌파), Tech Insider($4,329, 중고 $3,999), videocardprices($6,996 9/27), bestvaluegpu($4,899 신품/$3,822 중고), shattered.io | https://thinkcomputers.org/rtx-5090-shortage-deepens-as-ai-buyers-push-retail-cards-above-5000 · https://tech-insider.org/rtx-5090-price-4329-rtx-60-delay-2028-2026/ · https://videocardprices.com/card/nvidia-rtx-5090/ · https://bestvaluegpu.com/history/new-and-used-rtx-5090-price-history-and-specs/ | 2026-09 | 📰 |
| P6 | 다나와 RTX 5090 (GIGABYTE GAMING OC 6,489,770원, 현금 5,500,000원) · 글로벌이코노믹 "美 RTX 5090 품귀, 암시장 호가 1,280만 원" | https://prod.danawa.com/info/?pcode=75184280 · https://www.g-enews.com/article/Global-Biz/2026/09/20260915092807623fbbec65dfb_1 | 2026-09-15 | 📰 |
| P7 | Tom's Hardware: NVIDIA, RTX PRO 6000 Blackwell MSRP를 $16,000으로 인상 (2025-03 $8,565 → 2026-06 $13,250 → 2026-08 $16,000) | https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year · https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time | 2026-06~08 | 📰 |
| P8 | RTX PRO 6000 시세 — videocardprices($17,987 9/28, 범위 $12,380~19,999) · Thunder Compute(B&H $15,499, Newegg $13,998, Max-Q $8,900) | https://videocardprices.com/card/nvidia-rtx-pro-6000-blackwell/ · https://www.thundercompute.com/blog/nvidia-rtx-pro-6000-pricing | 2026-09 | 📰 |
| P9 | Tom's Hardware: DGX Spark $700 인상, Founders $3,999→$4,699 (메모리 수급) | https://www.tomshardware.com/desktops/mini-pcs/nvidia-dgx-spark-gets-18-percent-price-increase-as-memory-shortages-bite-founders-edition-now-usd4-699-up-from-usd3-999 | 2026-02 | 📰 |
| P10 | pi3g: DGX Spark 가격 (Q4 2026, NVIDIA $4,699, Newegg $4,399, Best Buy $5,404, OEM $5,400~8,200) · TechRadar/서드파티 파트너가 | https://pi3g.com/nvidia-dgx-spark-price/ · https://intuitionlabs.ai/articles/nvidia-dgx-spark-review | 2026-09 | 📰 |
| P11 | DGX Spark 국내가 (나무위키·클리앙: 700만 원대~, Dell 약 1,000만 원) | https://namu.wiki/w/NVIDIA%20RTX%20Spark%20%C2%B7%20DGX%20Spark · https://www.clien.net/service/board/news/19077958 | 2026 | 📰 |
| P12 | RTX 4090 중고가 — GetPCParts(eBay 체결가 $3,010 9/12, 30일 평균 $2,527) · bestvaluegpu($2,499) | https://www.getpcparts.com/market-prices/gpu-graphics-cards/rtx-4090 · https://bestvaluegpu.com/history/new-and-used-rtx-4090-price-history-and-specs/ | 2026-09 | 📰 |
| P13 | RTX 3090 중고가 — ResalePrices(평균 $1,343) · bestvaluegpu($1,413) · Alibaba 가이드($1,050) | https://resaleprices.com/gpu/nvidia-rtx-3090 · https://bestvaluegpu.com/history/new-and-used-rtx-3090-price-history-and-specs/ | 2026-09 | 📰 |
| P14 | RTX 5080 $1,579(Tom's 9월 추적) · 5070 Ti 약 $1,050 · 4080 Super 약 $1,500 (gpuprix) | https://www.tomshardware.com/pc-components/gpus/lowest-gpu-prices-tracking · https://thepcenthusiast.com/gpu-prices-2026-rtx-50-rx-9000-price-increase/ · https://gpuprix.com/us/gpus/geforce-rtx-4080-super | 2026-09 | 📰 |
| P15 | RTX PRO 5000 48 GB $4,250~4,600(VideoCardz 2025-10) · 72 GB 추정 $5,000~6,300, Newegg 마켓플레이스 $13,136 · RTX PRO 4500 약 $2,268 | https://videocardz.com/newz/nvidia-quietly-launches-rtx-pro-5000-blackwell-workstation-card-with-72gb-of-memory · https://www.newegg.com/nvidia-pro-5000-blackwell-72-gb-rtx-pro-5000-72gb-video-cards-workstation/p/2VV-000H-000N6 | 2025-10~2026-09 | 📰 |
| P16 | RTX 6000 Ada 시세 약 $7,000 (gpucost.org) · Newegg/B&H 판매 중 | https://gpucost.org/gpu/rtx-6000-ada · https://www.bhphotovideo.com/c/product/1753962-REG/pny_vcnrtx6000ada_pb_rtx_6000_ada_generation.html | 2026-09 | 📰 |
| P17 | H100 시세 (jarvislabs $25~30k PCIe, compute.exchange, cloudzero 중고 $15~28k) | https://jarvislabs.ai/blog/h100-price · https://compute.exchange/blogs/h100-gpu-price-2026 · https://www.cloudzero.com/blog/h100-gpu-cost/ | 2026-09 | 📰 |
| P18 | 클라우드 시세 집계 (gpuperhour · computeprices · getdeploying · gpus.io) | https://gpuperhour.com/ · https://computeprices.com/ · https://getdeploying.com/gpus/nvidia-rtx-pro-6000 | 2026-09 | 📰 |
| P19 | Jetson AGX Thor — Arrow 리드타임 24주 · Amazon 특가 $2,799 (Slickdeals) | https://www.arrow.com/en/products/945-14070-0080-000/nvidia.html · https://slickdeals.net/f/18875800-2799-nvidia-jetson-agx-thor-developer-kit-at-amazon | 2026 | 📰 |
| P20 | Arrow: DRIVE AGX Orin Developer Kit MSRP $7,500 (= D6) | https://www.arrow.com/en/products/940-63710-0010-300/nvidia.html | 2026-09-29 확인 | 📰 |
| P21 | 워크스테이션 완성품 — Petronella(RTX 5090 조립 $8,500~9,500, 2026-08) · BIZON($5,126~) · Lambda Vector(듀얼 5090 $14,999~) | https://petronellatech.com/blog/how-to-build-custom-ai-workstation-2026/ · https://bizon-tech.com/deep-learning-ai-workstation · https://shop.lambda.ai/gpu-workstations/vector/customize | 2026 | 📰 |
