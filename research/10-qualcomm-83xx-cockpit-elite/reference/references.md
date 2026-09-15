# 출처·검증 기록 — 퀄컴 83xx(SA8397P · Snapdragon Cockpit Elite)

- 조사일: 2026-09-16
- 대상 보고서: [`qualcomm-83xx-cockpit-elite.md`](../qualcomm-83xx-cockpit-elite.md)

## 0. 수집 방법

1. "83xx" 품번을 공개 출처에서 역추적. 결과: SA8397P = Snapdragon Cockpit Elite(座舱平台至尊版) 하나로 수렴. 다른 83xx 품번은 검색되지 않음.
2. 퀄컴 공식 문서(제품 브리프 PDF, 보도자료)는 절대 수치가 없어 배수(3×·12×)만 공식으로 채택. 절대 수치는 Tier-1 제품 사양(Thundersoft)과 중국 기술 블로그·언론에서 수집하고 등급을 표기.
3. 82xx(SA8295P·SA8255P)는 Lantronix·Thundercomm 개발 플랫폼 사양서(퀄컴 승인 배포)로 확인.
4. 양산 사례는 OEM/Tier-1 보도자료 또는 복수 언론 교차 확인.
5. 퀄컴 qualcomm.com 보도자료 페이지는 WebFetch 시 제목만 반환되는 경우가 많아, 동일 본문을 전재한 Nasdaq/The Fly·MarketScreener·telematicswire를 사용.

## 1. 검증 등급

| 등급 | 의미 |
|---|---|
| 🔍 공식 | 퀄컴 제품 브리프·보도자료, OEM/Tier-1 보도자료 원문 |
| 🧰 벤더 | Lantronix·Thundercomm 등 개발 플랫폼 사양서 |
| 📰 서드파티 | 언론·분석기관·기술 블로그 |
| 🧮 추정 | 출처 자체가 추정으로 명시했거나 보고서가 해석한 내용 |
| ❓ 미확인 | 검색 요약에만 등장하거나 원문 확인 실패 |

## 2. 출처별 확인 내용

| # | 출처 | 등급 | 확인 내용 |
|---|---|---|---|
| 1 | [Cockpit Elite/Ride Elite 제품 브리프 PDF](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf) | 🔍 | NPU 12×, GPU 3×, 40+ 센서·카메라 최대 20, Type-1 하이퍼바이저·멀티유저 VM·장기 API 호환, edge orchestrator, ASIL-D 대응 safety island, 트랜스포머 가속기·혼합 정밀도. 각주 "전 세대 대비, 예비 내부 테스트" |
| 2 | [Nasdaq/The Fly 2024-10-22](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms) · [Futurride](https://futurride.com/2024/10/22/qualcomm-ups-snapdragon-tech-with-cockpit-and-ride-elite-platforms/) | 🔍(전재) | 발표일·Oryon·CPU 3×·AI 12×·2025 샘플링·Li Auto/Mercedes |
| 3 | [퀄컴 X 2024-10-22](https://x.com/Qualcomm/status/1848811003225473177) | 🔍 | "3x faster CPU, up to 12x AI" |
| 4 | [퀄컴 CES 2026 PR (MarketScreener)](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026) | 🔍(전재) | 디자인윈 10건(Li Auto·Leapmotor·Zeekr·GWM·NIO·Chery), Ride Flex 8건, 7,500만 대, Ride SoC ~100만, Toyota RAV4·Garmin |
| 5 | [퀄컴 PR Leapmotor 2026-01](https://www.qualcomm.com/news/releases/2026/01/leapmotor-and-qualcomm-debuts-world-s-first-automotive-central-c) · [CarNewsChina](https://carnewschina.com/2026/01/06/leapmotor-partners-with-qualcomm-to-launch-worlds-first-central-computing-platform-with-dual-snapdragon-automotive-platforms/) · [vision-mobility](https://vision-mobility.de/en/news/ces-2026-leapmotor-becomes-the-first-oem-to-use-qualcomms-dual-chipset-sa8797p-389375.html) | 🔍/📰 | D19 듀얼 SA8797P, 1,280 TOPS, 콕핏·ADAS·바디·게이트웨이 통합 |
| 6 | [Panasonic PR 2025-01-07](https://news.panasonic.com/global/press/en250107-5) | 🔍 | Cockpit Elite CDC/HPC, "차세대 Cockpit 2026 초, Elite 직후" |
| 7 | [Visteon PR 2026-01-08](https://www.visteon.com/investors/investor-news/news-details/2026/Visteon-Showcases-Production-Ready-High-Performance-Compute-Solution-on-Snapdragon-Cockpit-Elite-Platform/default.aspx) | 🔍 | 양산 사양 HPC, Qwen 7B, 24+ 스피커 |
| 8 | [Thundersoft CES 2026](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) | 🔍 | RazorDCX Sylvania: SA8397P, 320 TOPS dense, SPECint2017 rate 80, 272 GB/s raw |
| 9 | [汽车之讯 车联天下](https://www.newsfcar.com/14736/) | 📰 | "座舱平台至尊版(SA8397P)·Ride平台至尊版(SA8797P)" 품번-브랜드 대응 |
| 10 | [Lantronix SA8295P ADP PDF](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf) | 🧰 | Kryo 695·Adreno 695·dual HTP·Spectra 395·DPU 1199·ARC HS46 lock-step·LPDDR4X-2133 8×16-bit·ASIL B SEooC |
| 11 | [Lantronix Ride SX 4.0](https://www.lantronix.com/products/ride-sx-4-0-automotive-development-platform/) · [Thundercomm](https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/) | 🧰 | SA8255P: Kryo Gen-6 v8.2·Adreno 663·HTP(HVX×4+HMX×2)·Spectra 690·LPDDR5 3ch 3200·Cortex-R52×4 safety island·ASIL B; SA8775P ASIL D |
| 12 | [PassMark SA8255P](https://www.cpubenchmark.net/cpu.php?cpu=Qualcomm+SA8255P&id=6866) | 📰 | 8코어/8스레드, MT 6,337·ST 1,625 |
| 13 | [Arrow SA-8255P](https://www.arrow.com/en/products/sa-8255p-0-fcbga1723hs-tr-01-0-ab/qualcomm) | 🧰 | FCBGA1723 |
| 14 | [telematicswire 2021-01-27](https://telematicswire.net/qualcomm-introduces-gen4-snapdragon-automotive-cockpit-platform/) | 🔍(전재) | 4세대 5nm, 2022 양산 |
| 15 | [Counterpoint](https://counterpointresearch.com/en/insights/qualcomm-snapdragon-cockpit-elite-powering-premium-visual-intelligent-cockpit-automotive-experiences) | 📰 | 4K 16+ 디스플레이, 레이 트레이싱, DPU, Dolby Atmos |
| 16 | [网易 퀄컴 중국 서밋 2026-06-05](https://www.163.com/dy/article/KUP4MPM60511DTVV.html) | 📰 | SA8397P 4nm, Ride Elite 720 TOPS, Ride Flex 144 TOPS, 채택 차종 |
| 17 | [IT之家 2026-03-31](https://m.ithome.com/html/934657.htm) · [快科技](https://news.mydrivers.com/1/1112/1112866.htm) · [新浪](https://www.sina.cn/news/detail/5282621412351047.html) | 📰 | Freelander 8397 최초군, 300+ TOPS, 14B LLM, 120만 폴리곤(퀄컴 부사장 발언) |
| 18 | [汽车之家 Nakul 인터뷰 2026-04-28](https://chejiahao.autohome.com.cn/info/25366884) | 📰(퀄컴 발언) | 2026 신차 15+, 8797 700 TOPS sparse/1,400 듀얼, 30B MoE |
| 19 | [Gasgoo 2026-06-16](https://autonews.gasgoo.com/articles/icv/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217) · [MarkLines](https://www.marklines.com/en/news/346249) | 📰 | Li Auto 8797 콕핏, 504K CPU·8.1 TFLOPS·320 TOPS, L9/L8 5·6월 인도 |
| 20 | [新出行 8797 三杀](https://www.xchuxing.com/article/154818) | 📰 | 8797 320 dense/640 sparse, 560K DMIPS, 8.1 TFLOPS; 8397 하위; SAIC-GM; 8775 72 TOPS |
| 21 | [腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500) | 📰 | Hexagon V83/V85 차량 전용·ASIL-B, 256-bit LPDDR5X 273 GB/s, 8797 70–80 W |
| 22 | [腾讯新闻 2024-12-21](https://news.qq.com/rain/a/20241221A042RT00) | 🧮 | 8797 18코어(12+6) 추정. 글 자체 "참고용" 면책 |
| 23 | [腾讯新闻 2024-10-25](https://news.qq.com/rain/a/20241025A09PRM00) | 🧮 | 4nm 추정, 8397 360T/8797 720T 계산 |
| 24 | [腾讯新闻 2025-07-22](https://news.qq.com/rain/a/20250722A089YJ00) | 📰 | Li i8 = 8295P; 8295P 5nm·8코어·30 TOPS·11 디스플레이; 8397 320 TOPS·14B |
| 25 | [腾讯新闻 2025-12-23](https://news.qq.com/rain/a/20251223A05T4R00) | 📰 | Exeed 2026 Carmind 2.0 + 8397 |
| 26 | [CSDN 8397 vs 8295](https://blog.csdn.net/m0_72165397/article/details/155090743) | 📰 | 24–36 GB LPDDR5X·UFS 4.0, 레이 트레이싱 |
| 27 | [EEWORLD](https://en.eeworld.com.cn/news/qcdz/eic657301.html) · [ResearchInChina](http://www.researchinchina.com/UpLoads/ArticleFreePartPath/20240723085131.pdf) | 📰 | 8255P NPU 48 vs 24 TOPS(상충) |
| 28 | [Qualcomm AI Hub Automotive](https://aihub.qualcomm.com/automotive/models) | 🔍 | 칩셋 필터: SA7255P/SA8255P/SA8295P/SA8650P/SA8775P — SA8397P 없음 (2026-09-16) |
| 29 | [ExecuTorch #16535](https://github.com/pytorch/executorch/issues/16535) | 🔍 | 2026-01-12, SA8397 지원 요청 |
| 30 | [QAIRT Auto 개요](https://docs.qualcomm.com/nav/home/auto_overview.html?product=1601111740009302) | 🔍 | SA8295/8540/8620/8650/8775/8797 열거, 8397 미열거 |
| 31 | [한국경제 via Nate 2025-12-11](https://news.nate.com/view/20251211n35389) | 📰 | LG전자 AI 캐빈 플랫폼, Cockpit Elite |
| 32 | [퀄컴 PR 2025-09 Mercedes CLA](https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a) | 🔍(제목만 확인) | "Snapdragon Cockpit Platforms" — 품번 미기재 |

## 3. 폐기·불채택 출처

- [difans.cn 8155/8255/8295 비교](https://www.difans.cn/post_byd_car/643.html): SA8295P를 "Cortex-X2 + Adreno 750 + LPDDR4X 32GB"로 기술 — Lantronix 공식 사양(Kryo 695/Adreno 695)과 상충. 불채택.
- Zeekr 관련 검색 요약의 "SA8397P 15–20 W, 8K@60, 2025-12 ET9 최초 탑재": 원문 페이지 미확인. 전력은 ❓로 표기, ET9 시점은 腾讯新闻(2026년 탑재)으로 대체.
- MarketScreener 전재문의 "SA8297P" 표기: 오기로 판단(다른 출처 모두 SA8797P).
- 접근 실패(403/521/타임아웃): qualcomm.com 보도자료 본문, edge-ai-vision 전재, Zhihu 2건, CSDN 3건, Torque News, sohu. 동일 내용의 대체 출처로 보완.
