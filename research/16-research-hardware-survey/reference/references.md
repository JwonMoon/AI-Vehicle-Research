# 출처 목록 — 차량용 AI 연구 유형별 실제 사용 하드웨어 조사

> **열람일**: 2026-10-14 · ID는 [보고서](../research-hardware-survey.md)의 인용 표기와 같다.
> **등급**: 🔍 공식(벤더 제품 페이지·README·모델카드·공시·보도자료) / 📄 논문·학위논문 / 📰 언론·시장조사·2차 / 💬 개발자 포럼·커뮤니티 / ✅ 조사 환경에서 페이지를 **직접 열람**(GitHub·PyPI만 가능했음). ✅가 없는 항목은 검색 엔진 본문 발췌로 확인했다.
> **이 저장소의 기존 문서는 출처로 쓰지 않았다.**

## [N] NVIDIA (16건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| N1 | Accelerate Autonomous Vehicle Development with the NVIDIA DRIVE AGX Thor Developer Kit (NVIDIA 개발자 블로그) | https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/ | 2025-08 | 🔍 |
| N2 | NVIDIA DRIVE AGX Developer Kits (제품 페이지, Thor·Orin 사양·SKU) | https://developer.nvidia.com/drive/agx ; https://developer.nvidia.com/drive/setup ; https://developer.nvidia.com/drive/faq | — | 🔍 |
| N3 | NVIDIA DRIVE AGX Thor Platform for Developers (PDF: Thor-X 1,000 INT8/2,000 FP4, 350 W, 입력 9–16 V) | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | 2025 | 🔍 |
| N4 | NVIDIA DRIVE AGX Orin Platform for Developers (PDF: 254 INT8 TOPS, 200 W, 200 GB/s) | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-orin-platform-for-developers.pdf | — | 🔍 |
| N6 | DRIVE AGX 입수 경로: Arrow 유통 페이지("approved customers") · NVIDIA 포럼 "How to access DRIVE AGX SDK Developer" | https://www.arrow.com/en/products/030-1463-000/nvidia ; https://forums.developer.nvidia.com/t/how-to-access-drive-agx-sdk-developer/333966 | 2023– | 🔍💬 |
| N7 | NVIDIA Blackwell-Powered Jetson Thor Now Available (뉴스룸) · Hackster.io "resellers open Jetson AGX Thor orders at $3,499"(128 GB, 273 GB/s) | https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics ; https://www.hackster.io/news/nvidia-tells-resellers-to-open-jetson-agx-thor-developer-kit-orders-at-3-499-06e8cbf52441 | 2025-08-25 | 🔍📰 |
| N8 | Jetson AGX Thor Developer Kit 사양(리셀러 사양 사본: 40–130 W, QSFP28, HSB) | https://www.waveshare.com/product/jetson-agx-thor-developer-kit.htm ; https://www.generationrobots.com/en/404410-nvidia-jetson-agx-thor-developer-kit.html | 2025 | 📰 |
| N9 | Jetson AGX Thor 가격: CNBC(US$3,499) · VideoCardz "NVIDIA raises Jetson prices… AGX Thor now $5,499" · heise | https://www.cnbc.com/2025/08/25/nvidias-thor-t5000-robot-brain-chip.html ; https://videocardz.com/newz/nvidia-raises-jetson-prices-by-up-to-101-agx-thor-now-costs-5499 ; https://heise.de/-10622015 | 2025-08 / 2026-07 | 📰 |
| N10 | Jetson AGX Orin 64GB: 데이터시트 DS-10662-001(275/138 TOPS, 204.8 GB/s) · SparkFun US$1,999.95 | https://openzeka.com/wp-content/uploads/2022/03/DS-10662-001_v1.0.pdf ; https://www.sparkfun.com/nvidia-jetson-agx-orin-64gb-developer-kit.html | 2022-03 / 현재 | 🔍 |
| N11 | TensorRT-Edge-LLM Support Matrix (Jetson Thor·DRIVE Thor·DGX Spark·Jetson Orin FP16/INT8/INT4만) | https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/getting_started/support-matrix.html (GitHub 원본 https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/getting_started/support-matrix.md) | 2026-09 (v0.11.0) | 🔍 ✅ |
| N12 | TensorRT-Edge-LLM Performance Benchmarks (Thor·Orin·DGX Spark tok/s) | https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/performance/performance-benchmarks.html | 2026-09 (v0.11.0) | 🔍 ✅ |
| N13 | NVIDIA Jetson Benchmarks (vLLM, ISL/OSL 2048/128: Llama 3.1 8B 41.3/150.8 등) · ServeTheHome 재현(149.1 tok/s) | https://developer.nvidia.com/embedded/jetson-nano-dl-inference-benchmarks ; https://www.servethehome.com/nvidia-jetson-agx-thor-developer-kit-blackwell-for-robotics/3/ | 2025 | 🔍📰 |
| N14 | Streamline LLM Deployment for Autonomous Vehicle Applications with NVIDIA DriveOS LLM SDK (지원 모델·정밀도) · 포럼(Edge-LLM으로 개명) | https://developer.nvidia.com/blog/streamline-llm-deployment-for-autonomous-vehicle-applications-with-nvidia-driveos-llm-sdk/ ; https://forums.developer.nvidia.com/t/cosmos-reason-2-on-drive-agx-thor/366775 | 2025-03 | 🔍💬 |
| N15 | NVIDIA DRIVE Hyperion (Hyperion 10: 14 카메라·9 레이더·1 LiDAR·12 초음파, 2× Thor) · Hesai LiDAR 파트너 선정 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-hyperion/ ; https://www.hesaitech.com/hesai-selected-by-nvidia-as-lidar-partner-for-nvidia-drive-hyperion-10-to-enable-level-4-fleet-deployment/ | 2026-01 | 🔍 |
| N16 | Accelerating LLM and VLM Inference for Automotive and Robotics with NVIDIA TensorRT Edge-LLM (인캐빈 레퍼런스: 온보드 ASR+TTS+LLM + 클라우드 오케스트레이터) | https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/ | 2025–26 | 🔍 |

## [Q] Qualcomm (18건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| Q1 | Snapdragon Cockpit Elite QAM8397P 제품 페이지 · Cockpit Elite/Ride Elite 제품 브리프(12× NPU, TOPS 미공개) | https://www.qualcomm.com/automotive/products/qam8397p ; https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf | 2024-10 | 🔍 |
| Q2 | Snapdragon Ride Elite QAM8797P 제품 페이지 · 2024-10 보도자료 | https://www.qualcomm.com/automotive/products/qam8797p ; https://www.qualcomm.com/news/releases/2024/10/qualcomm-races-ahead-in-the-evolution-of-software-defined-vehicl | 2024-10 | 🔍 |
| Q4 | Qualcomm Drives the Future of Mobility… (CES 2026 보도자료: Elite 채택 OEM, 7,500만 대) | https://www.qualcomm.com/news/releases/2026/01/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-di | 2026-01 | 🔍 |
| Q5 | Lantronix eStore: SA8295P Automotive Development Platform US$6,300(열 인클로저 US$6,500, SA8295PS US$5,250; "퀄컴 승인 필요") | https://estore.lantronix.com/products/sa8295p-automotive-development-platform ; https://estore.lantronix.com/products/sa8295p-automotive-development-platform-with-thermal-enclosure-configuration | 현재 | 🔍 |
| Q6 | Lantronix eStore / 제품 페이지: SA8255P and SA8775P Ride SX 4.0 Automotive Development Platforms US$4,999 | https://estore.lantronix.com/collections/development-platforms ; https://lantronix.com/products/ride-sx-4-0-automotive-development-platform | 현재 | 🔍 |
| Q7 | Thundercomm SA8295P / SA8255P+SA8775P ADP(소프트웨어 미포함, CreatePoint에서 빌드; 12 GB LPDDR5) | https://www.thundercomm.com/product/sa8295p-automotive-development-platform/ ; https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/ | 현재 | 🔍 |
| Q8 | Snapdragon Ride SDK Getting Started(Ride 플랫폼·QNX·퀄컴 라이선스 필요, 영업 문의) | https://developer.qualcomm.com/software/digital-chassis/snapdragon-ride/getting-started ; https://www.qualcomm.com/developer/software/snapdragon-ride-sdk | — | 🔍 |
| Q9 | Qualcomm AI Hub 자동차 모델 페이지(지원 디바이스: SA7255P ADP, SA8255 Proxy, SA8295P ADP, SA8650 Proxy, SA8775P ADP) · QNN 자동차 개요 | https://aihub.qualcomm.com/automotive/models/ffnet_78s ; https://docs.qualcomm.com/bundle/publicresource/80-63442-10/topics/auto_overview.md | 현재 | 🔍 |
| Q10 | Qualcomm AI Hub / HF: Llama-v3.2-1B-Instruct on SA8295P ADP 11.0 tok/s(w4, Genie) | https://huggingface.co/qualcomm/Llama-v3.2-1B-Instruct ; https://aihub.qualcomm.com/models/llama_v3_2_1b_instruct | 현재 | 🔍 |
| Q11 | TechInsights: 2025 Lynk & Co 900 Cockpit Controller with dual Qualcomm SA8295P SoCs(각 최대 60 TOPS) | https://www.techinsights.com/ko/node/60234 | 2025-08-08 | 📰 |
| Q12 | CnEVPost: Jidu 첫 모델 Snapdragon 8295(5 nm, 30 TOPS) · 42how | https://cnevpost.com/2021/11/29/jidus-first-model-to-feature-qualcomm-snapdragon-8295-chip-based-on-5nm-process ; https://en.42how.com/?p=8865 | 2021-11-29 | 📰 |
| Q13 | Gasgoo: Bosch 콕핏 도메인 컨트롤러 on SA8775P(230K DMIPS + 72 TOPS NPU) 및 QC8255 콕핏 양산 | https://autonews.gasgoo.com/articles/icv/70037655 | 2025 | 📰 |
| Q14 | Qualcomm Unveils Snapdragon Ride Flex(보도자료 재게시) | https://www.edge-ai-vision.com/2023/01/qualcomm-unveils-snapdragon-ride-flex-the-automotive-industrys-first-scalable-family-of-socs-to-simultaneously-support-digital-cockpit-and-advanced-driver-assistance-systems/ | 2023-01 | 🔍 |
| Q15 | Momenta: SA8620P/SA8650P 36–100 밀집 TOPS | https://momenta.ai/en/article/165.html | 2024-04 | 🔍 |
| Q16 | Li Auto Inc. Form 6-K(2026 L9/L8에 Snapdragon 8797 채택) | https://www.sec.gov/Archives/edgar/data/0001791706/000110465926105658/tm2624872d2_ex99-1.pdf | 2026 | 🔍 |
| Q17 | Qualcomm and Hyundai Mobis to Power Next-Generation ADAS and Digital Cockpit(Ride Flex) | https://www.qualcomm.com/news/releases/2025/01/qualcomm-and-hyundai-mobis-to-power-next-generation-adas-and-dig | 2025-01 | 🔍 |
| Q18 | MarkLines 검색 "8255"(Chery Zongheng G700, Ford Bronco New Energy 등 채택차) | https://www.marklines.com/en/search/1?q=8255 | 2025 | 📰 |
| Q19 | Gasgoo: Li Auto launches new-gen cockpit platform… Qualcomm 8797, NPU 320 TOPS | https://autonews.gasgoo.com/articles/news/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217 | 2026 | 📰 |

## [X] 기타 SoC·가속기·오픈소스 장치·시장 (18건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| X1 | XPENG Turing AI Chip 공식 페이지(750 TOPS, 40코어, 30B 모델) | https://www.xpeng.com/technology/Turing_AI_Chip | — | 🔍 |
| X2 | CnEVPost: Xpeng debuts G7(3× Turing 2,250 TOPS; 2개 VLA·1개 VLM; Max는 2× Orin-X 508 TOPS) · InsideChinaAuto | https://cnevpost.com/2025/06/11/xpeng-debuts-g7-suv/ ; https://insidechinaauto.com/2025/06/12/xpeng-g7-debuts-with-three-turing-ai-chips-claiming-global-deployment-of-xngp/ | 2025-06 | 📰 |
| X3 | Tesla HW4: NotATeslaApp "How Tesla's FSD Hardware Has Changed"(~500 TOPS 추정, 16 GB/SoC) · Drive Tesla Canada 티어다운(카메라 커넥터 12) · TechInsights | https://www.notateslaapp.com/news/3521/how-teslas-fsd-hardware-has-changed-over-the-years ; https://driveteslacanada.ca/news/tesla-hw4-gets-first-teardown-revealing-additional-camera-inputs-and-more/ ; https://www.techinsights.com/ko/node/53315 | 2023–26 | 📰 |
| X4 | Horizon Journey 6 사양: Gasgoo(J6B 18 TOPS) · 42how(J6P 560 TOPS, 18× A78AE) | https://autonews.gasgoo.com/articles/market-industry/70038233 ; https://en.42how.com/2025/04/19/what-makes-horizons-journey-6p-chip-a-game-changer/ | 2025-04 | 📰 |
| X5 | Horizon J6 채택: Gasgoo(100+ 모델) · Horizon 뉴스(BYD, 출하량) · CarNewsChina(Exeed E05 J6P) | https://autonews.gasgoo.com/articles/ICV/horizon-robotics-journey-6-series-products-to-be-deployed-onto-over-100-vehicle-models-70035597 ; https://www.horizon.auto/en/news/horizon-news/478 ; https://carnewschina.com/2025/07/15/chery-teases-exeed-exlantix-e05-suv-with-chinese-developed-horizon-journey-6p-chip/ | 2025 | 📰🔍 |
| X6 | D-Robotics RDK S100(BPU Nash 80 TOPS, 12 GB) US$499 Switch Science / US$439 Spotpear | https://www.switch-science.com/products/10854 ; https://spotpear.com/index.php/shop/D-Robotics-RDK-S100-Robotics-Development-Kit.html | 현재 | 📰 |
| X7 | Mobileye EyeQ 칩 페이지 · EyeQ6 블로그(EyeQ6H 34 INT8 TOPS) | https://www.mobileye.com/technology/eyeq-chip/ ; https://www.mobileye.com/blog/eyeq6-system-on-chip/ | — | 🔍 |
| X8 | Mobileye EyeQ6 Lite launches(5 TOPS, 4,600만 대) · Globes(VW EyeQ6H) · AIwire EyeQ Kit | https://www.mobileye.com/news/mobileye-eyeq6-lite-launches-to-speed-adas-upgrades-worldwide/ ; https://en.globes.co.il/en/article-1001467280 ; https://aiwire.net/2022/07/05/mobileye-launches-eyeq-kit-new-sdk-for-driver-assistance-systems | 2024 | 🔍📰 |
| X9 | Renesas R-Car V4H 제품 페이지(34 TOPS) · White Hawk 평가보드 RTP8A779G0ASKB0FS0SA000 | https://www.renesas.com/en/products/r-car-v4h ; https://www.renesas.com/en/design-resources/boards-kits/rtp8a779g0askb0fs0sa000 | — | 🔍 |
| X10 | TI SK-TDA4VM(8 TOPS, US$199) · TDA4VH EVM J784S4XEVM(32 TOPS) | https://www.mouser.lu/new/texas-instruments/ti-sk-tda4vm-kit/ ; https://www.ti.com/tool/J784S4XEVM | 2021– | 🔍 |
| X11 | Ambarella CV3-AD685 보도자료(최대 500 eTOPS 패밀리) · Continental 파트너십(SOP 2027) | https://www.businesswire.com/news/home/20230724604370/en/ ; https://www.continental.com/en/press/press-releases/20230105-ambarella-strategic-partnership/ | 2023 | 🔍 |
| X12 | Hailo-10H M.2 제품 페이지(40 INT4/20 INT8 TOPS, 2.5 W) · ASUS UGen300 US$259.99 · Hailo-8 M.2 US$179.99 | https://hailo.ai/products/ai-accelerators/hailo-10h-m-2-generative-ai-acceleration-module/ ; https://www.neweggbusiness.com/asus-ugen300-8gld4-m2-ai-module/p/9B-00-949-002 ; https://www.waveshare.com/product/ai/boards-kits/raspberry-pi/hailo-8.htm | 현재 | 🔍📰 |
| X13 | Huawei MDC 810/610(42how, CnEVPost) | https://en.42how.com/?p=8581 ; https://cnevpost.com/2021/04/18/huawei-didnt-say-all-in-in-their-self-driving-efforts-they-came-straight-out-with-an-ace-in-the-hole | 2021 | 📰 |
| X14 | comma 3X 블로그(Snapdragon 845, 3× 1080p 140 dB, US$1,250) · comma compare/shop(US$999, comma four) · 하네스 US$99(Slickdeals) | https://blog.comma.ai/comma3X/ ; https://comma.ai/compare ; https://www.comma.ai/shop/comma-3x ; https://slickdeals.net/f/18416992-comma-3x-799-july-4th-sale-99-for-vehicle-harness-open-source-driver-assist-device | 2023–25 | 🔍📰 |
| X15 | openpilot 0.9.8 / 0.9.9 릴리스 블로그(tinygrad QCOM GPU 런타임, USB 외부 GPU) | https://blog.comma.ai/098release/ ; https://blog.comma.ai/099release/ | 2025 | 🔍 |
| X16 | Global and China Autonomous Driving SoC Research Report 2025(ResearchInChina via BusinessWire: Thor-U 730T, 주류 L2.5 SoC) | https://www.businesswire.com/news/home/20250911741155/en | 2025-09-11 | 📰 |
| X17 | SemiDrive X10(4 nm, 40 TOPS NPU, 154 GB/s, 7B 온디바이스; 상하이시 Auto Shanghai 2025 보도) | https://english.shanghai.gov.cn/en-AutoShanghai2025/20250425/81f820dcc0ec4fdfa35465853ca883ae.html | 2025-04-25 | 📰 |
| X18 | Q1 2025 China ADAS SoC 점유율(Orin-X+N 51.8%) · GGII 2025(NVIDIA 49.36%, Huawei 23.07%; Horizon 47.66%, Mobileye 27.81%) | https://news.metal.com/newscontent/103359135/Q1-2025-ADAS-component-supplier-rankings%3A-China%E2%80%99s-local-suppliers-lead-new-trend-in-technology-integration/ ; https://carnewschina.com/2026/02/01/horizon-robotics-and-nvidia-are-key-players-in-chinas-advanced-driving-chip-market-share-rankings-in-2025/ | 2025 / 2026-02 | 📰 |

## [M] 모델·벤치·논문 (12건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| M1 | NVlabs/alpamayo README(≥24 GB VRAM, 가중치 22 GB, 6.4 s 궤적, 라이선스·변경 이력) | https://github.com/NVlabs/alpamayo | 2026-05 | 🔍 ✅ |
| M2 | NGC: Alpamayo 1.5-10B 모델카드(백본 8.2B + 액션 전문가 2.3B, Cosmos-Reason2, OpenMDW-1.1) · NVIDIA Alpamayo LLM Info(80,000 h) | https://catalog.ngc.nvidia.com/orgs/nim/nvidia/models/alpamayo-1-5-10b ; https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/llm-info/ | 2026-03 | 🔍 |
| M3 | alpamayo 데이터 로더 소스(기본 4 카메라, 4 프레임 0.1 s, 64 스텝 10 Hz) | https://github.com/NVlabs/alpamayo/blob/main/src/alpamayo_r1/load_physical_aiavdataset.py | 2026 | 🔍 ✅ |
| M4 | TensorRT-Edge-LLM Alpamayo-R1-10B (VLA) 예제("Only FP16 is supported", Thor 빌드 파라미터, 4 cam × 4 timestep) | https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/examples/vla/alpamayo.html (GitHub 원본 https://github.com/NVIDIA/TensorRT-Edge-LLM/blob/main/docs/source/user_guide/examples/vla/alpamayo.md) | 2026 | 🔍 ✅ |
| M5 | NVIDIA 포럼: Alpamayo-R1-10B TensorRT engine OOM on DRIVE AGX Thor(15.17 GB, DriveOS 7.2.5) · Drive AGX Thor with Alpamayo | https://forums.developer.nvidia.com/t/alpamayo-r1-10b-tensorrt-engine-oom-on-drive-agx-thor/382500 ; https://forums.developer.nvidia.com/t/drive-agx-thor-with-alpamayo/382501 | 2026 | 💬 |
| M6 | The Batch(deeplearning.ai): NVIDIA's Alpamayo-R1… 99 ms on RTX Pro 6000 | https://www.deeplearning.ai/the-batch/nvidias-alpamayo-r1-is-a-robotics-style-reasoning-model-for-autonomous-vehicles | 2025–26 | 📰 |
| M7 | QwenLM/Qwen-Drive-1.0 README(Qwen3.5-4B, BEV 헤드, 플래닝 전문가, 24 GB+ GPU 권장, 파일 크기, NAVSIM PDMS) · arXiv 2609.00111 | https://github.com/QwenLM/Qwen-Drive-1.0 ; https://arxiv.org/abs/2609.00111 | 2026-08/09 | 🔍 ✅ 📄 |
| M8 | DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models(arXiv 2402.12289; 2× Orin-X, 410 ms) | https://arxiv.org/abs/2402.12289v5 | 2024-06 | 📄 |
| M9 | UNIST 학위논문(E2E 모델 16 Hz on Jetson AGX Orin, HMG 2025 E2E 챌린지 1위) · UNIST 뉴스(2라운드 Orin-X PC 환경) | https://scholarworks.unist.ac.kr/handle/201301/91051 ; https://news.unist.ac.kr/?p=38120 | 2026-02 / 2025-10 | 📄🔍 |
| M10 | 엣지 LLM/VLA 논문: arXiv 2506.09554(Orin AGX 2.7B–32.8B 전력 모드) · AI-CDA4All arXiv 2505.06749(LLaMA 3.2 on AGX Orin 5.07 s) · arXiv 2509.11480(VLA 엣지-클라우드 스케일링) | https://www.arxiv.org/abs/2506.09554 ; https://arxiv.org/pdf/2505.06749 ; https://arxiv.org/html/2509.11480v2 | 2025 | 📄 |
| M11 | LMSYS: NVIDIA DGX Spark In-Depth Review(GPT-OSS 20B 49.7 vs RTX PRO 6000 215 tok/s) | https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/ | 2025-10-13 | 📰 |
| M12 | AWS Guidance for In-Vehicle AI Assistant(온보드 SLM + 클라우드 LLM 시맨틱 라우팅) · Venkatesha et al., TMLR 2025 엣지-클라우드 투기 디코딩(지연 −35%) | https://aws.amazon.com/solutions/guidance/in-vehicle-ai-assistant-on-aws/ ; https://mlanthology.org/tmlr/2025/venkatesha2025tmlr-fast | 2025 | 🔍📄 |

## [S] 센서·카메라·인터페이스·연구차량 (27건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| S1 | Autoware Reference HW 색인(벤더 분류·면책) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/index.md (렌더: https://docs.autoware.org/main/reference-design/reference-hw/) | — | 🔍 ✅ |
| S2 | Autoware Reference HW: AD Computers(Neousys·ADLINK·MIIVII Jetson Orin/Thor 등 21종) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/ad-computers.md | — | 🔍 ✅ |
| S3 | Autoware Reference HW: LiDARs(37종; AT128 200 m 120°×25.4°, OS1 등) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/lidars.md | — | 🔍 ✅ |
| S4 | Autoware Reference HW: Cameras(TIER IV C1/C2/C3 GMSL2, FLIR, Lucid, Neousys PCIe-GL26) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/cameras.md | — | 🔍 ✅ |
| S5 | Autoware Reference HW: IMU/AHRS/GNSS-INS(NovAtel PwrPak7D-E2, Xsens MTi-680G, SBG Ellipse-D 등) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/imu_ahrs_gnss_ins.md | — | 🔍 ✅ |
| S6 | Autoware Reference HW: Radars(Smartmicro, Aptiv, Continental ARS404/408) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/radars.md | — | 🔍 ✅ |
| S7 | Autoware Reference HW: DBW 공급사 · 센서 키트 공급사(LEO Drive, TIER IV ADK, RoboSense) | https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/vehicle_drive_by_wire_suppliers.md ; https://github.com/autowarefoundation/autoware-documentation/blob/main/docs/reference-design/reference-hw/ad_sensor_kit_suppliers.md | — | 🔍 ✅ |
| S8 | Meka et al., "Driving On: Taking Our Autoware AV Testbed Further," IEEE IV 2026(MKZ·Dataspeed·VLP-32·OEM7·Nuvo-10108GC) · Neousys Nuvo-10108GC 데이터시트(350 W RTX 1장) | https://www.acsu.buffalo.edu/~chaozheh/Papers/2026_IV_Meka_Gutha_Krozelius_He_Sadek_Qiao.pdf ; https://coastipc.com/media/productattach/n/u/nuvo-10108gc_data_sheet_112024.pdf | 2026-06 / 2024-11 | 📄🔍 |
| S9 | TUM EDGAR: arXiv 2309.15492(센서 구성) · TUMFTM/edgar_digital_twin URDF(8 카메라·5 LiDAR·6 레이더) · ATTI(InoNet PC + RTX A6000) | https://arxiv.org/pdf/2309.15492 ; https://github.com/TUMFTM/edgar_digital_twin/blob/main/source/sensor_parameter/edgar.urdf ; https://www.automotivetestingtechnologyinternational.com/?p=61030 | 2023–26 | 📄 ✅ 📰 |
| S10 | KIT CoCar NextGen(arXiv 2404.17550: 12 LiDAR, 9 카메라, 3× 4D 레이더) | https://arxiv.org/pdf/2404.17550 | 2024-04 | 📄 |
| S11 | Pony.ai 7세대 로보택시: Hesai 보도자료(AT128 ×4) · Gasgoo(9 LiDAR·14 카메라·4 레이더, 4× Orin-X 1,016 TOPS) | https://hesaitech.com/?p=7711 ; https://autonews.gasgoo.com/articles/news/ponyai-unveils-seventh-generation-robotaxis-at-auto-shanghai-2025-70037142 | 2025-04 | 📰 |
| S12 | Waymo: Meet the 6th-generation Waymo Driver(13 카메라·4 LiDAR·6 레이더) | https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/ | 2024-08 | 🔍 |
| S13 | Connect Tech JCB002 GMSL Camera Platform(8× GMSL2, Rogue/Forge 캐리어 전용) · WDL Systems US$539.74 | https://connecttech.com/product/xavier-gmsl-camera-platform/ ; https://www.wdlsystems.com/CTI-Xavier-GMSL-Camera-Platform | 2024–25 | 🔍📰 |
| S14 | e-con Systems STURDeCAM12/31/34(GMSL2, 120–140 dB HDR, 가격 견적) | https://www.e-consystems.com/gmsl-cameras/1mp-ox01g10-120db-hdr-ip69k-gmsl2-camera.asp | 2023–25 | 🔍 |
| S15 | Leopard Imaging LI-AR0233-GMSL2(US$429–499, 키트 US$609) | https://leopardimaging.com/product/automotive-cameras/cameras-by-interface/adi-gmsl2-cameras/li-ar0233-gmsl2/li-ar0233-gmsl2-065h-2/ | 2025 | 🔍 |
| S16 | Sony 차량용 이미지 센서(IMX490 5.4 MP 120–140 dB, IMX728 8.3 MP 120 dB; EDOM 라인업 · Leopard IMX728 데이터시트) | https://www.edomtech.com/en/product-detail/automotive-cmos-image-sensor-solution/ ; https://leopardimaging.com/wp-content/uploads/2026/01/LI-IMX728-APHY-120H_Datasheet.pdf | 2018 / 2026-01 | 🔍 |
| S17 | LiDAR 사양·가격: Hesai AT128 제품 페이지(128 ch, 200 m@10%, 1.5 M pts/s) · Ouster OS1-32 US$8,000(대학 US$6,000) / OS1-128 US$18,000(GeoWeek 2018–19) · RoboSense Helios US$1,800(공식 스토어) | https://www.hesaitech.com/?p=5030 ; https://www.geoweeknews.com/articles/32-channel-lidar-for-8k-ousters-newest-lidar-finds-a-sweet-spot/ ; https://geoweeknews.com/news/ouster-starts-2019-with-a-new-18k-128-channel-lidar-and-big-benefits-for-mapping ; https://store.robosense.ai/products/helios-series | 2018–25 | 🔍📰 |
| S18 | 4D 레이더: Continental ARS548 RDI 데이터시트(300 m, ±60°) · Arbe Phoenix(2,304 가상채널, VentureBeat) | https://conti-engineering.com/wp-content/uploads/2023/01/RadarSensors_ARS548RDI.pdf ; https://venturebeat.com/business/qamcom-will-bring-arbes-4d-imaging-radar-to-trucks-mines-and-farms | 2021–23 | 🔍📰 |
| S19 | GNSS/INS 가격: Xsens MTi-680G RS Components £2,729 · Generation Robots €3,562(VAT 포함) · SBG Ellipse-D 사양 · NovAtel PwrPak7 | https://uk.rs-online.com/web/p/multi-function-sensors/2614490 ; https://www.generationrobots.com/en/404361-xsens-mti-680g-rtk-gnss-ins.html ; https://sbg-systems.com/high-performance-ins-gnss ; https://novatel.com/products/receivers/enclosures/pwrpak7 | 2025 | 🔍📰 |
| S20 | DBW: Dataspeed ADAS Development Vehicle Kit(ROS wiki) · astuff/pacmod3(지원 차종, DBC v3–12) · AStuff Honda CR-V 키트 | https://robots.ros.org/adas-development-vehicle-kit/ ; https://github.com/astuff/pacmod3 ; https://autonomoustuff.com/news/new-honda-cr-v-by-wire-kit-hexagon-autonomoustuff-accelerates-rd-for-autonomy-programs-worldwide | 2026-02 / 2022 | 🔍 ✅ |
| S21 | CAN 인터페이스 가격: PEAK PCAN-USB FD(DigiKey US$379, Gridconnect US$347) · Kvaser Leaf v3(US$407 공식, US$349 리셀러) | https://azcus.digikey.com/en/products/detail/peak-system/IPEH-004022/12326289 ; https://gridconnect.com/can-usb-fd-adapter.html ; https://www2.kvaser.com/product/leaf-v3 | 2025 | 🔍📰 |
| S22 | 자동차 이더넷 변환기: Intrepid RAD-Moon 2(100/1000BASE-T1↔1000BASE-T) · MACH Systems T1 컨버터 €400–410 | https://store.intrepidcs.com/product/RAD-MOON2 ; https://shop.machsystems.cz/?p=774 | 2025 | 🔍 |
| S23 | NVIDIA 포럼: Jetson Thor Developer Kit USB-C 전원(240 W 동봉, 28 V 5 A/7.5 A 피크) · DRIVE AGX Thor 전원 사양 스레드 | https://forums.developer.nvidia.com/t/updated-7-2-2026-nvidia-jetson-thor-developer-kit-usb-c-power-supply/358753 ; https://forums.developer.nvidia.com/t/drive-agx-thor-power-supply-specification/368616 | 2026 | 💬 |
| S24 | PiCAN 2(MCP2515, Elektor €44.95) · Waveshare 2-CH CAN FD HAT | https://www.elektor.com/products/pican-2-can-bus-board-for-raspberry-pi-2-3 ; https://www.pishop.us/product/2-channel-isolated-can-fd-expansion-hat-for-raspberry-pi-multi-protections/ | 현재 | 🔍 |
| S25 | Quectel RM520N-GL 5G 모듈(Jetson Orin 캐리어 번들 US$276–327) | https://spotpear.com/shop/Jetson-Orin-5G-4G-3G-RM520N-GL-GPS-GNSS/RM520N-GL-5G-for-Jetson-Orin.html ; https://cdwg.com/product/quectel-rm520n-gl-wireless-cellular-modem-5g/8257146 | 2025 | 📰 |
| S26 | Jetson AGX Orin INA3221 전력 레일(NVIDIA 포럼) · jtop(JetsonHacks) | https://forums.developer.nvidia.com/t/jetson-agx-orin-ina3221-power-monitor-layout/223111 ; https://jetsonhacks.com/2023/02/07/jtop-the-ultimate-tool-for-monitoring-nvidia-jetson-devices/amp/ | 2022–23 | 💬📰 |
| S27 | 400 W급 12 V DC-DC: Vicor V24A12C400BL US$460(산업용) | https://thepartsdirect.com/part/v24a12c400bl~vicor | 2025 | 📰 |

## [V] 완성차 사례 (7건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| V1 | Li Auto Launches Li i8(보도자료: Pro J6M 128 TOPS, Max/Ultra Thor-U 700 TOPS, VLA 배포) · Li Auto 6-K 2025-07(Thor-U 700 TOPS) | https://finviz.com/news/118723/li-auto-inc-launches-li-i8-a-six-seat-battery-electric-family-suv ; https://www.sec.gov/Archives/edgar/data/1791706/000110465925071734/tm2521968d1_ex99-1.htm | 2025-07 | 🔍 |
| V2 | CnEVPost: Li Auto to update existing models(AD Max 2× Orin-X → 1× Thor-U, Hesai ATL) · Li MEGA Home on Thor-U "will support VLA" | https://cnevpost.com/2025/02/28/li-auto-to-update-existing-models-may/ ; https://cnevpost.com/2025/05/20/li-auto-mega-home-rolls-off-line/ | 2025 | 📰 |
| V4 | Electrek: Xpeng VLA 2.0 test drive(Turing 2,250 TOPS, P7 2+1 칩) | https://electrek.co/2026/04/29/xpeng-vla-2-test-drive-tesla-not-alone-full-self-driving/ | 2026-04-29 | 📰 |
| V5 | Zeekr 9X Technology Unveiled(듀얼 8295 콕핏, 듀얼 Thor-U 주행) | https://chinaevhome.com/2025/07/10/zeekr9xtechnologyunveiledfullybenchmarkingthecullinan1/ | 2025-07-10 | 📰 |
| V6 | CarNewsChina: Zeekr launches cross-generation ADAS upgrade… moving to 700 TOPS(Thor-U) · CnEVPost 2024-12(Thor X/U/S/Z, 750 TOPS 버전) | https://carnewschina.com/2025/11/25/zeekr-launches-cross-generation-adas-upgrade-for-older-001-and-009-models-moving-to-700-tops-system/ ; https://cnevpost.com/2024/12/16/xpeng-considering-shelving-plans-adopt-nvidia-thor-report/ | 2025-11 / 2024-12 | 📰 |
| V7 | Gasgoo: NIO begins pre-sale for 2024 models(1× 8295 + 4× Orin-X, 256 TOPS 콕핏 공유) · NIO launches NOMI GPT | https://autonews.gasgoo.com/articles/news/nio-begins-pre-sale-for-2024-vehicle-models-70031474 ; https://autonews.gasgoo.com/articles/market-industry/nio-launches-nomi-gpt-large-model-70032446 | 2024 | 📰 |
| V8 | KrASIA: Mercedes-Benz CLA… DRIVE Orin + Momenta | https://kr-asia.com/mercedes-benz-to-rev-up-intelligent-driving-with-new-all-electric-cla | 2025 | 📰 |

## [O] 온디바이스·콕핏·에이전트 사례 (11건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| O1 | Gasgoo: Cockpit-Driving Fusion, Qualcomm Unveils Another Major Move(8397 "10B 온디바이스") | https://autonews.gasgoo.com/articles/market-industry/cockpit-driving-fusion-qualcomm-unveils-another-major-move-2064710943249113089 | 2025 | 📰 |
| O2 | Visteon: Production-Ready HPC on Snapdragon Cockpit Elite(CES 2026, Qwen 7B) · Visteon×Qualcomm 2025(QNN 양자화, Hexagon NPU) | https://www.nasdaq.com/press-release/visteon-showcases-production-ready-high-performance-compute-solution-snapdragonr ; https://s205.q4cdn.com/875277771/files/doc_news/Visteon-and-Qualcomm-Redefine-Next-Generation-AI-based-Intelligent-Cockpit-Experience-2025.pdf | 2026-01 / 2025-04 | 🔍 |
| O3 | Gasgoo: XPENG, Banma unveil automotive-grade AI cockpit solution at 2026 Yunqi Conference(Turing 750 TOPS, 30B 로컬, 온디바이스 우선) | https://autonews.gasgoo.com/articles/news/xpeng-banma-unveil-automotive-grade-ai-cockpit-solution-at-2026-yunqi-conference-2105184460592340993 | 2026-09 | 📰 |
| O4 | Banma AutoOmni 2.0-23B-A3B(MoE, 8397 대상) | https://www.thailand-business-news.com/?p=330518 | 2026-09 | 📰 |
| O5 | ResearchAndMarkets(GlobeNewswire): Li Auto… Mind GPT-3o(엣지 NPU + 클라우드 추론 분할) | https://www.globenewswire.com/news-release/2025/04/07/3056503/28124/en/li-auto-layout-in-electrification-connectivity-intelligence-and-sharing-analysis-report-2024-2025-mind-gpt-cockpit-evolution-multimodal-end-to-end-architecture-complex-task-process.html | 2025-04-07 | 📰 |
| O6 | Cerence xUI 보도자료(하이브리드, DRIVE AGX Orin 우선 최적화) · CaLLM Edge(Phi-3 3.8B, 4-bit) | https://investors.cerence.com/news-events/press-releases/detail/104/cerence-ai-debuts-xui-its-hybrid-llm-based-platform-advancing-the-fully-agentic-in-car-experience ; https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive | 2025-01 / 2024-11 | 🔍 |
| O7 | FEV × Microsoft × NVIDIA 보도자료(Phi-4-mini on DRIVE AGX, 오프라인 음성, 클라우드 폴백) | https://www.fev.com/app/uploads/2026/07/PR_FEV_MS_NVIDIA.pdf ; https://autotechinsight.spglobal.com/news/5289456/fev-partners-with-microsoft-on-in-car-ai-using-small-language-models-on-nvidia-platform | 2026-07 | 🔍📰 |
| O8 | Mercedes CLA MBUX Virtual Assistant(Gemini, 클라우드; WhichCar) · Qualcomm 2025-09 보도자료(Snapdragon Cockpit + 5G) | https://whichcar.com.au/news/mercedes-benz-cla-mbux-virtual-assistant ; https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a | 2025 | 📰🔍 |
| O9 | peykan 0.2.1 · PyPI(MCP over CAN/OBD-II/UDS/J1939, 가상 CAN+ECU 시뮬레이터, cantools, 읽기 전용 기본) | https://pypi.org/project/peykan/ | 2026-10-07 | 🔍 ✅ |
| O10 | Pro-CHASER(Raspberry Pi + CAN-HAT 테스트베드) · CANLP(UW, Pi + PiCAN2 Duo) | https://researcher.manipal.edu/en/publications/pro-chaser-a-prototype-testbed-for-car-hacking-attack-simulation-/ ; https://digital.lib.washington.edu/researchworks/bitstreams/3cd53d33-bd6a-4b2c-9af6-e5b293b3dfad/download | — | 📄 |
| O11 | Eclipse KUKSA Databroker(VSS, gRPC) · Android Automotive VHAL 인터페이스 | https://sdv.eclipse.org/sdv-contribution-day-sept-2022/slides/07-eclipse-kuksa.pdf ; https://source.android.com/docs/automotive/vhal/vhal-interface | 2022 / 현재 | 🔍 |

## [P] 호스트 GPU 가격·사양 (3건)

| ID | 제목 | URL | 날짜 | 등급 |
|---|---|---|---|---|
| P1 | RTX PRO 6000 Blackwell WS 사양(96 GB GDDR7, 1,792 GB/s, 600 W; Puget) · 가격 추이(US$8,435 → 13,250 표시; Digital Citizen) | https://www.pugetsystems.com/parts/Video-Card/NVIDIA-RTX-PRO-6000-Blackwell-Workstation-Edition-96GB-PCI-E-16221/ ; https://www.digitalcitizen.life/nvidia-rtx-pro-6000-blackwell-prices-climb-past-10000-as-ai-demand-keeps-rising/ | 2025–26 | 🔍📰 |
| P2 | DGX Spark 사양(GB10, 128 GB, 273 GB/s; The Register) · 가격: NVIDIA 포럼 2026-02-23 인상(US$4,699) · implicator.ai(US$6,950, 64 GB US$4,999) | https://theregister.com/2025/10/13/nvidia_gb10_spark ; https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713 ; https://www.implicator.ai/nvidia-adds-64gb-dgx-spark-at-4-999-as-128gb-model-climbs-to-6-950/ | 2025-10 / 2026 | 📰💬 |
| P3 | RTX 5090(32 GB, 1,792 GB/s, MSRP US$1,999) · RTX 4090(24 GB, 1,008 GB/s, MSRP US$1,599) | https://www.corsair.com/explorer/gamer/gaming-pcs/rtx-5090-vs-4090-whats-the-difference/ | 2025 | 📰 |
