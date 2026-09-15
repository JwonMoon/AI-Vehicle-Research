# 퀄컴 83xx 계열(SA8397P · Snapdragon Cockpit Elite) 리서치 — 82xx(SA8255P/SA8295P)와 무엇이 다른가

> **작성일**: 2026-09-16
> **배경**: IPCU 성능형 SoC 후보 검토. IVI에는 지금까지 82xx(주로 SA8255P)를 써 왔다. 83xx는 무엇이고, 무엇이 달라지는가.
> **출처 표기 원칙**: 모든 사실 주장에 출처를 병기한다. **공식**(퀄컴 보도자료·제품 브리프·OEM/Tier-1 보도자료) / **개발 플랫폼 벤더**(Lantronix·Thundercomm 사양서, 퀄컴 승인 하 배포) / **서드파티**(언론·분석기관·기술 블로그) / **추정**을 구분한다. 확인하지 못한 항목은 **"출처 미확인"**, 출처 간 상충은 **"상충"**으로 명시한다. 퀄컴 공식 문서는 배수(3×·12×)만 제시하고 절대 수치를 내지 않으므로, TOPS·코어 수·대역폭 같은 절대 수치는 **거의 전부 서드파티 값**이다.

---

## 0. 세 줄 요약

1. **"83xx"는 사실상 SA8397P 한 품번이며, 퀄컴 브랜드로는 Snapdragon Cockpit Elite(중국명 骁龙座舱平台至尊版)다.** 2024-10-22 Snapdragon Summit에서 Ride Elite(SA8797P)와 함께 발표된 5세대 콕핏 플랫폼으로, 82xx(4세대 Snapdragon Cockpit Platform, 2021-01 발표·5nm)의 직계 후속이다. ([Nasdaq/The Fly 2024-10-22](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms) · [Thundersoft CES 2026](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [车联天下×퀄컴](https://www.newsfcar.com/14736/))
2. **핵심 차이는 CPU 아키텍처 교체(Arm Cortex 기반 Kryo → 퀄컴 자체 설계 Oryon)와 NPU의 세대 도약이다.** 퀄컴 공식 목표치는 전 세대 콕핏 대비 CPU 3×, GPU 3×, NPU 12×("preliminary internal testing" 기준). 서드파티 수치로는 8295P 30 TOPS → 8397P 320 TOPS(dense), 메모리 LPDDR4X → 256-bit LPDDR5X 약 273 GB/s. 이 조합이 "차내에서 14B급 LLM을 돌리는 콕핏"이라는 세일즈 포인트를 만든다. ([퀄컴 제품 브리프](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf) · [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [IT之家 2026-03-31](https://m.ithome.com/html/934657.htm))
3. **양산 시점은 "지금"이다.** 2025년 샘플링 → 2026년 JLR×체리 Freelander·Exeed(星途) 신차·Zeekr 등에 8397P 탑재, Leapmotor D19·Li Auto L9/L8에 형제 칩 8797P 탑재가 시작됐고, 퀄컴은 2026년 중 Elite 탑재 신차 15종 이상을 예고했다. 한국에서는 LG전자가 CES 2026에서 Cockpit Elite 기반 AI 캐빈 플랫폼을 공개했다. 다만 **퀄컴 AI Hub·ExecuTorch 등 공개 SW 툴체인에는 아직 SA8397P가 정식 등재되지 않았다**(2026-09-16 확인). ([Qualcomm CES 2026 PR](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026) · [Nakul Duggal 인터뷰 2026-04-28](https://chejiahao.autohome.com.cn/info/25366884) · [Qualcomm AI Hub Automotive](https://aihub.qualcomm.com/automotive/models) · [ExecuTorch #16535](https://github.com/pytorch/executorch/issues/16535))

---

## 1. 퀄컴 차량용 SoC 계보 — 83xx가 어디에 놓이는가

### 1.1 명명 규칙 (본 보고서 해석)

퀄컴은 품번 규칙을 공식 문서로 설명하지 않는다. 그러나 공개된 품번과 브랜드 대응을 놓고 보면 다음 패턴이 일관된다. (**본 보고서 해석** — 출처 미확인. 대응 관계 자체는 각 행의 출처로 확인)

| 품번 | 브랜드 | 세대/계층 | 용도 | 근거 |
|---|---|---|---|---|
| SA8155P / SA8195P | Snapdragon Cockpit Platform 3세대 | 7nm | 콕핏 | [퀄컴 SA8155P 제품 브리프](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/qul7413_sa8155_productbrief_r4.pdf) |
| **SA8295P** | Snapdragon Cockpit Platform **4세대**, 최상위 | 5nm | 콕핏 | [Lantronix ADP 사양서](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf) · [퀄컴 4세대 발표 2021-01-27](https://telematicswire.net/qualcomm-introduces-gen4-snapdragon-automotive-cockpit-platform/) |
| **SA8255P** | Snapdragon Cockpit Platform 4세대, 중간 등급 | 5nm(서드파티) | 콕핏 | [Thundercomm Ride SX 4.0](https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/) |
| SA8775P | Snapdragon Ride Flex | — | 콕핏+ADAS 통합(ASIL D) | [Thundercomm Ride SX 4.0](https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/) |
| SA8650P / SA8620P | Snapdragon Ride | — | ADAS | [QAIRT Auto 개요](https://docs.qualcomm.com/nav/home/auto_overview.html?product=1601111740009302) |
| **SA8397P** | **Snapdragon Cockpit Elite**(座舱平台至尊版) | **5세대**, Oryon | 콕핏 | [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [车联天下](https://www.newsfcar.com/14736/) |
| **SA8797P** | **Snapdragon Ride Elite**(Ride平台至尊版; 서드파티는 "Ride Flex Elite"로도 부름) | 5세대, Oryon | ADAS 또는 콕핏+ADAS 융합 | [车联天下](https://www.newsfcar.com/14736/) · [vision-mobility 2026-01](https://vision-mobility.de/en/news/ces-2026-leapmotor-becomes-the-first-oem-to-use-qualcomms-dual-chipset-sa8797p-389375.html) |

읽는 법(해석): `SA8` 다음 첫 자리가 **도메인**(1·2·3 = 콕핏 세대, 6 = Ride, 7 = Ride Flex/융합), 뒤 두 자리가 **등급**(97 = Elite 최상위, 95 = 4세대 최상위, 55 = 4세대 중간). 따라서 사용자가 말한 "82xx"는 4세대 콕핏(8295P·8255P), "83xx"는 5세대 콕핏 Elite(8397P)에 해당한다. **8397P 외의 83xx 품번(예: 8355P·8375P 등)은 2026-09-16 기준 공개 출처에서 확인되지 않았다**(출처 미확인).

### 1.2 시간축

| 시점 | 사건 | 출처 |
|---|---|---|
| 2021-01-27 | 4세대 Snapdragon Cockpit Platform 발표(5nm), 2022 양산 예고 | [telematicswire](https://telematicswire.net/qualcomm-introduces-gen4-snapdragon-automotive-cockpit-platform/) (퀄컴 PR 인용) |
| 2024-10-22 | Snapdragon Summit(Maui)에서 Cockpit Elite·Ride Elite 발표. Oryon CPU, CPU 3×·AI 12×, 2025 샘플링, Li Auto·Mercedes-Benz 협력 | [Nasdaq/The Fly](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms) · [Futurride 2024-10-22](https://futurride.com/2024/10/22/qualcomm-ups-snapdragon-tech-with-cockpit-and-ride-elite-platforms/) |
| 2025-01-07 | Panasonic Automotive, Cockpit Elite 기반 CDC/HPC 개발 발표. "차세대 Cockpit Platform 탑재차 2026 초, Elite는 그 직후" | [Panasonic PR](https://news.panasonic.com/global/press/en250107-5) |
| 2025-07-22 | Li Auto i8 콕핏은 8295P(8397 아님) — 8397 양산 전 | [腾讯新闻](https://news.qq.com/rain/a/20250722A089YJ00) |
| 2025-09 | Mercedes-Benz CLA(MB.OS) — "Snapdragon Cockpit Platforms" 탑재(품번 미기재) | [퀄컴 PR 2025-09](https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a) |
| 2025-12-11 | LG전자, CES 2026에서 Cockpit Elite 기반 'AI 캐빈 플랫폼' 공개 예고 | [한국경제 via Nate](https://news.nate.com/view/20251211n35389) |
| 2025-12-22 | Exeed(星途) 브랜드 나이트: 2026년 Carmind 2.0 + 8397 콕핏 | [腾讯新闻 2025-12-23](https://news.qq.com/rain/a/20251223A05T4R00) |
| 2026-01-05 | CES 2026: Cockpit/Ride Elite 디자인윈 10건, Leapmotor D19 듀얼 Elite 중앙 컴퓨터, Visteon·Garmin·Thundersoft 솔루션 | [퀄컴 PR via MarketScreener](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026) |
| 2026-01-12 | ExecuTorch에 SA8397 지원 요청 이슈 등록 | [pytorch/executorch #16535](https://github.com/pytorch/executorch/issues/16535) |
| 2026-03-31 | JLR×체리 Freelander — "세계 최초 8397 탑재 차종 그룹" | [IT之家](https://m.ithome.com/html/934657.htm) · [快科技](https://news.mydrivers.com/1/1112/1112866.htm) |
| 2026-04-28 | 퀄컴 Nakul Duggal(베이징 모터쇼): 2026년 Elite 탑재 신차 15종 이상 | [汽车之家 车家号](https://chejiahao.autohome.com.cn/info/25366884) |
| 2026-06-05 | 퀄컴 중국 자동차 기술 서밋(우시): Cockpit Elite SA8397P 4nm, Ride Elite 720 TOPS | [网易 2026-06](https://www.163.com/dy/article/KUP4MPM60511DTVV.html) |
| 2026-06-15 | Li Auto 차세대 콕핏 — 8797 Elite 세계 최초 양산 적용 | [Gasgoo 2026-06-16](https://autonews.gasgoo.com/articles/icv/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217) |

---

## 2. 82xx — 지금까지 써 온 것 (SA8295P · SA8255P)

### 2.1 SA8295P (4세대 최상위)

Lantronix ADP 사양서(퀄컴 파트너 공식 문서, 2023)에 명기된 구성:

- **CPU**: Qualcomm Kryo 695 (Arm v8 Cortex 기반)
- **GPU**: Adreno 695
- **AI**: Dual Hexagon Tensor Processor — Hexagon DSP + quad HVX(벡터) + dual HMX(행렬)
- **ISP**: Spectra 395 · **VPU**: Adreno 665 · **DPU**: Adreno 1199
- **안전**: 전용 Safety Manager 서브시스템(dual ARC HS46 lock-step), SEooC로 ASIL B 상정
- **메모리(ADP 기준)**: 8채널 LPDDR4X-2133 (8×16-bit), 16 GB
- **디스플레이(ADP)**: DP 3 + eDP 1.4b 4 + MIPI DSI 2 · **카메라**: 4-lane MIPI CSI ×4

([Lantronix SA8295P ADP 사양서](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf))

서드파티 수치: 5nm, CPU 8코어(고성능 4 + 중급 4), AI 약 30 TOPS. ([pcauto](https://www.pcauto.com/my/news/30tops-a-deep-analysis-of-the-qualcomm-8295-chip-intelligent-driving-under-5nm-process-14039) · [腾讯新闻 2025-07-22](https://news.qq.com/rain/a/20250722A089YJ00)) — 절대 TOPS 값은 퀄컴 공식 문서에 없다.

### 2.2 SA8255P (4세대 중간 등급 — 현재 IVI 주력)

Lantronix/Thundercomm Ride SX 4.0 사양서(SA8255P·SA8775P 공용 보드):

- **CPU**: Kryo Gen-6 (Arm v8.2 Cortex 기반), "Quad Kryo Gold Prime" 표기. PassMark 등재는 8코어/8스레드(Multithread 6,337 · Single 1,625, 2025 Q3 최초 등재)
- **GPU**: Adreno 663 (safe GP-GPU compute 지원)
- **AI**: Hexagon Tensor Processor — Hexagon DSP + quad HVX + dual HMX
- **ISP**: Spectra 690 · MIPI-CSI ×4 (D-PHY/C-PHY)
- **메모리(ADP)**: LPDDR5 3채널 3200 MHz, 3×12 GB · UFS 3.1 ×2
- **비디오**: AV1/HEVC/H.264/VP9 디코드 최대 4×4K60, 인코드 2×4K60
- **안전**: Safety Island(quad Cortex-R52), SEooC로 **ASIL B**. 같은 보드의 SA8775P는 **ASIL D**
- **패키지**: FCBGA1723 (Arrow 품번 `SA-8255P-0-FCBGA1723`)

([Lantronix Ride SX 4.0](https://www.lantronix.com/products/ride-sx-4-0-automotive-development-platform/) · [Thundercomm](https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/) · [PassMark](https://www.cpubenchmark.net/cpu.php?cpu=Qualcomm+SA8255P&id=6866) · [Arrow](https://www.arrow.com/en/products/sa-8255p-0-fcbga1723hs-tr-01-0-ab/qualcomm))

**AI 성능 — 상충**: ResearchInChina는 8255P를 "230K DMIPS, NPU 24 TOPS"로([ResearchInChina 2024-07](http://www.researchinchina.com/UpLoads/ArticleFreePartPath/20240723085131.pdf)), EEWORLD는 "Hexagon V73, 최대 48 TOPS"로([EEWORLD](https://en.eeworld.com.cn/news/qcdz/eic657301.html)) 적는다. 정밀도(INT8 dense/sparse) 기준이 명시되지 않아 단순 비교 불가. 퀄컴 공식 절대치 없음.

**82xx의 위치**: 8255P는 CPU가 8295P와 비슷하거나 고클럭에서 약간 앞서지만 GPU(Adreno 663 vs 695)가 낮은 "IVI 가성비" 칩이라는 것이 업계 평가다([EEWORLD](https://en.eeworld.com.cn/news/qcdz/eic657301.html), 서드파티). 8295P·8255P 합산 중국 시장 연 100만 대 규모로 4세대가 주류가 됐다([CSDN/高工智能汽车 2024-06](https://blog.csdn.net/GGAI_AI/article/details/139519069), 서드파티).

---

## 3. 83xx — SA8397P · Snapdragon Cockpit Elite

### 3.1 퀄컴이 공식적으로 말하는 것

퀄컴 제품 브리프(Cockpit Elite·Ride Elite 공용, 각주: "모든 성능 목표는 전 세대 대비, 예비 내부 테스트 기준, 최종 검증 시 변경 가능")의 주장:

| 항목 | 공식 주장 |
|---|---|
| CPU | **Qualcomm Oryon** — 퀄컴 최고 성능 CPU를 차량용으로 맞춤. 전 세대 대비 **3×**(퀄컴 보도자료·X 게시물) |
| GPU | 개선된 Adreno, **3×** 성능. 고급 렌더링·게이밍·멀티미디어 |
| NPU | 멀티모달 AI 전용 Hexagon NPU, 전 세대 콕핏 대비 **12×**. 트랜스포머 가속기·벡터 엔진·혼합 정밀도 |
| 카메라·센서 | **40개 이상 멀티모달 센서, 최대 20대 고해상도 카메라**(360° + 캐빈 모니터링). 고급 ISP |
| 가상화 | **Type-1 하이퍼바이저**, 멀티 OS. 클러스터·IVI·다중 승객 인스턴스를 앱 중심 멀티유저 VM으로 분리. 장기 API 호환 지원 |
| AI 실행 환경 | 온디바이스 AI + 통합 **edge orchestrator**(Qualcomm AI Orchestrator), AI Hub 연동 |
| 안전 | **ASIL-D 시스템 대응 설계, 전용 safety island 컨트롤러**, 격리·무간섭 HW 구조(Elite 계열 공통 서술) |
| 전력 | "업계 선도 전력 효율" — HW/SW 전력 관리로 코어 사용률·런타임 균형 (절대치 없음) |
| 아키텍처 | 콕핏과 자율주행 기능을 **같은 SoC에 결합 가능한 유연 구조** |

([퀄컴 제품 브리프 PDF](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf) · [퀄컴 X 2024-10-22](https://x.com/Qualcomm/status/1848811003225473177) · [Nasdaq/The Fly](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms))

분석기관 Counterpoint는 발표 브리핑을 근거로 "전·후석 **4K 디스플레이 16개 이상** 구동, 실시간 레이 트레이싱, 전용 DPU, Dolby Atmos 오디오 서브시스템"을 추가한다([Counterpoint 2024-10](https://counterpointresearch.com/en/insights/qualcomm-snapdragon-cockpit-elite-powering-premium-visual-intelligent-cockpit-automotive-experiences), 서드파티·발표 인용). 퀄컴 중국 서밋(2026-06-05, 우시) 보도는 SA8397P를 **4nm**, "수백억 파라미터급 엔드사이드 생성형 AI"로 소개한다([网易](https://www.163.com/dy/article/KUP4MPM60511DTVV.html), 서드파티·퀄컴 발표 인용). 퀄컴 중국 부사장 盛况은 Freelander 발표에서 "Adreno GPU 3배 — **120만 폴리곤 고정밀 3D 모델 실시간 렌더링**"을 언급했다([快科技 2026-03-31](https://news.mydrivers.com/1/1112/1112866.htm)).

### 3.2 서드파티가 말하는 절대 수치

| 항목 | 값 | 출처 | 신뢰도 |
|---|---|---|---|
| NPU | **320 TOPS(dense)** | [Thundersoft RazorDCX Sylvania(SA8397P 도메인 컨트롤러)](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [IT之家 "300 TOPS 이상"](https://m.ithome.com/html/934657.htm) | Tier-1 제품 사양. 정밀도(INT8 추정) 미기재 |
| CPU | **SPECint2017 rate 80** | [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) | Tier-1 제품 사양 |
| 메모리 대역폭 | **272 GB/s(raw)** / 256-bit LPDDR5X 273 GB/s | [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500) | 두 출처 일치 |
| 메모리 용량(도메인 컨트롤러 기준) | LPDDR5X 24–36 GB, UFS 4.0 | [CSDN 2025-11](https://blog.csdn.net/m0_72165397/article/details/155090743) | 블로그 |
| 온디바이스 LLM | **약 14B 파라미터** | [IT之家](https://m.ithome.com/html/934657.htm) · [腾讯新闻 2025-07-22](https://news.qq.com/rain/a/20250722A089YJ00) | 언론 |
| 공정 | 4nm | [网易(퀄컴 서밋 보도)](https://www.163.com/dy/article/KUP4MPM60511DTVV.html) · [腾讯新闻 2024-10-25](https://news.qq.com/rain/a/20241025A09PRM00) | 퀄컴 발표 인용 + 추정 |
| NPU 아키텍처 | Hexagon **V83/V85** — 차량 전용 설계, NPU 자체가 ASIL-B | [腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500) | 기술 블로그, 업계 소식통 인용 |
| Oryon 코어 수 | "12 또는 16코어"(8797P는 18코어 = 12+6) | [腾讯新闻 2024-12-21](https://news.qq.com/rain/a/20241221A042RT00) 등 | **추정**. 해당 글 자체가 "참고용"으로 면책 |
| 소비 전력 | 15–20 W | 검색 요약에만 등장 | **출처 미확인** |

### 3.3 8397P vs 8797P — 같은 세대, 다른 역할

두 칩은 같은 Oryon·Adreno·Hexagon 세대다. 차이는 규모와 대상 도메인이다.

- **8397P = 콕핏 전용.** 320 TOPS급, 콕핏 워크로드(다중 디스플레이·오디오·캐빈 AI)에 초점. ([Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/))
- **8797P = ADAS 또는 콕핏+ADAS 융합.** Oryon 18코어(12+6) 추정, dense 320 / sparse 640 TOPS, 560K DMIPS, GPU 8.1 TFLOPS(서드파티). Leapmotor D19는 8797P **2개**(1개 콕핏, 1개 ADAS)로 합계 1,280 TOPS. 퀄컴 Nakul Duggal은 2026-04 인터뷰에서 "칩당 700 TOPS sparse, 듀얼 1,400 TOPS, 온디바이스 30B MoE"라 말해 **수치가 상충**한다(640 vs 700). 소비 전력 70–80 W 추정. ([新出行](https://www.xchuxing.com/article/154818) · [vision-mobility](https://vision-mobility.de/en/news/ces-2026-leapmotor-becomes-the-first-oem-to-use-qualcomms-dual-chipset-sa8797p-389375.html) · [汽车之家 인터뷰](https://chejiahao.autohome.com.cn/info/25366884) · [腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500))
- Li Auto 차세대 콕핏(2026-06-15)은 콕핏임에도 **8797**을 썼다 — "504K CPU, GPU 8.1 TFLOPS, NPU 320 TOPS". 즉 OEM은 콕핏에도 상위 8797을 선택할 수 있다. ([Gasgoo](https://autonews.gasgoo.com/articles/icv/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217))
- 반대로 SAIC-GM은 8397/8797 병행, JLR×체리·Exeed·Zeekr은 8397 채택 보도. ([新出行](https://www.xchuxing.com/article/154818) · [IT之家](https://m.ithome.com/html/934657.htm))

---

## 4. 비교표 — 8255P · 8295P · 8397P (참고: 8797P)

| 항목 | SA8255P (82xx 중간) | SA8295P (82xx 최상위) | **SA8397P (83xx, Cockpit Elite)** | SA8797P (Ride Elite, 참고) |
|---|---|---|---|---|
| 세대·발표 | 4세대 콕핏 | 4세대 콕핏, 2021-01 | **5세대 콕핏, 2024-10-22** | 5세대, 2024-10-22 |
| 공정 | 5nm(서드파티) | 5nm(퀄컴 4세대 발표) | **4nm**(퀄컴 서밋 보도) | 4nm(추정) |
| CPU | Kryo Gen-6, Arm v8.2 Cortex 기반, 8코어 | Kryo 695, Arm v8 Cortex 기반, 8코어 | **Oryon(퀄컴 자체 설계)**, 3×; 코어 수 미확인(12~16 추정) | Oryon 18코어(12+6 추정), 560K DMIPS |
| CPU 지표 | PassMark MT 6,337 | — | SPECint2017 rate 80(Thundersoft) | — |
| GPU | Adreno 663 | Adreno 695 | 신형 Adreno, **3×**, 실시간 레이 트레이싱, 120만 폴리곤 | 8.1 TFLOPS |
| NPU | Hexagon HTP(HVX×4 + HMX×2); 24 또는 48 TOPS(**상충**) | Dual Hexagon HTP; ~30 TOPS(서드파티) | Hexagon V83/V85(서드파티), **12×**, **320 TOPS dense** | 320 dense / 640~700 sparse(**상충**) |
| 온디바이스 LLM | — | — | ~14B | 30B MoE(퀄컴 발언) |
| 메모리 | LPDDR5 3ch 3200 (ADP 3×12 GB) | LPDDR4X-2133 8×16-bit (ADP 16 GB) | **256-bit LPDDR5X, ~273 GB/s**; 도메인 컨트롤러 24–36 GB | 256-bit LPDDR5X(추정) |
| 센서/카메라 | MIPI-CSI ×4 | MIPI-CSI ×4 | **40+ 센서, 카메라 최대 20** | 동일 |
| 디스플레이 | eDP ×4(ADP) | DP 3 + eDP 4 + DSI 2(ADP) | **4K 16+**(Counterpoint) | — |
| 가상화 | 하이퍼바이저(퀄컴 GVM: LA/LV) | 동일 | **Type-1 하이퍼바이저, 멀티유저 VM, 장기 API 호환** 명시 | QC Linux PVM 툴체인 등재 |
| 안전 | SEooC **ASIL B**, Safety Island(Cortex-R52 ×4) | SEooC **ASIL B**, Safety Manager(ARC HS46 lock-step) | **ASIL-D 시스템 대응 safety island**(Elite 브리프 공통 서술; 8397P 단독 등급은 미확인) | 동일 |
| 전력 | — | — | 15–20 W(**출처 미확인**) | 70–80 W(추정) |
| 양산 | 2023~ (중국 연 100만 대 규모) | 2022~ | **2026** (Freelander·Exeed·Zeekr) | 2026 (Leapmotor D19·Li L9/L8) |
| 공개 툴체인 | AI Hub 등재 | AI Hub 등재 | **AI Hub 미등재, ExecuTorch 요청 중** | QAIRT 문서 등재 |

출처: 2장·3장 각 항목 참조. 퀄컴 공식 절대 수치는 없으며 "3×/12×"만 공식이다.

---

## 5. 그래서 무엇이 다른가 — 아키텍처 관점 6가지

### 5.1 CPU: Arm 설계 코어(Kryo) → 퀄컴 자체 설계 코어(Oryon)

82xx의 Kryo는 Arm Cortex(v8/v8.2) 기반의 커스텀 튜닝이다([Lantronix](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf)). 83xx의 Oryon은 퀄컴이 Nuvia 인수 후 자체 설계한 코어로, PC(Snapdragon X Elite)·모바일(8 Elite)에 먼저 들어간 것을 차량용으로 맞춘 것이다([Futurum](https://futurumgroup.com/insights/qualcomm-launches-new-elite-snapdragon-automotive-platforms/) · [腾讯新闻 2024-10-25](https://news.qq.com/rain/a/20241025A09PRM00)). 공식 목표 3×. **실무적 의미**: ISA는 여전히 AArch64이므로 앱 바이너리 호환은 유지되나, 코어 수·클러스터 구성·캐시 계층이 바뀌므로 CPU 어피니티·실시간 스케줄링 튜닝은 재검증 대상이다(본 보고서 해석).

### 5.2 NPU: "보조 가속기" → "LLM 실행 엔진"

82xx의 Hexagon HTP는 스마트폰과 공유하는 범용 세대(HVX+HMX)다. 83xx는 트랜스포머 가속기·혼합 정밀도가 명시된 12× NPU이고([제품 브리프](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf)), 서드파티는 차량 전용 Hexagon V83/V85로 NPU 자체가 ASIL-B라고 전한다([腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500)). 결과적으로 Tier-1 데모가 "Qwen 7B 온디바이스 컨시어지"(Visteon), "14B급 LLM"(JLR Freelander), "VLM+LLM+이미지 생성 온디바이스"(LG전자)로 바뀌었다. ([Visteon 2026-01-08](https://www.visteon.com/investors/investor-news/news-details/2026/Visteon-Showcases-Production-Ready-High-Performance-Compute-Solution-on-Snapdragon-Cockpit-Elite-Platform/default.aspx) · [IT之家](https://m.ithome.com/html/934657.htm) · [한국경제 via Nate](https://news.nate.com/view/20251211n35389))

### 5.3 메모리: LPDDR4X/LPDDR5 → 256-bit LPDDR5X ~273 GB/s

8295P ADP는 LPDDR4X-2133 8×16-bit(=128-bit), 8255P ADP는 LPDDR5 3채널이다. 8397P는 256-bit LPDDR5X로 약 273 GB/s(Thundersoft "272 GB/s raw")다. LLM 디코딩은 메모리 대역폭에 묶이므로, 12× NPU보다 이 대역폭 도약이 온디바이스 LLM 체감 속도에 더 직접적이다(본 보고서 해석; 근거: [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) · [腾讯新闻 2025-07-07](https://news.qq.com/rain/a/20250707A07U3500) · [Lantronix 8295P](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf) · [Lantronix 8255P](https://www.lantronix.com/products/ride-sx-4-0-automotive-development-platform/)). 도메인 컨트롤러 실장 용량도 24–36 GB LPDDR5X·UFS 4.0으로 올라간다는 보도가 있다([CSDN](https://blog.csdn.net/m0_72165397/article/details/155090743), 블로그).

### 5.4 GPU·디스플레이: 레이 트레이싱, 4K 16화면, 120만 폴리곤

공식 3×, 실시간 레이 트레이싱, 4K 디스플레이 16개 이상(Counterpoint), 120만 폴리곤 실시간 3D(퀄컴 중국 부사장 발언). 82xx 세대의 "11개 디스플레이"(8295P, 서드파티) 대비 화면 수·해상도·렌더링 품질이 한 단계 올라간다. ([Counterpoint](https://counterpointresearch.com/en/insights/qualcomm-snapdragon-cockpit-elite-powering-premium-visual-intelligent-cockpit-automotive-experiences) · [快科技](https://news.mydrivers.com/1/1112/1112866.htm) · [腾讯新闻 2025-07-22](https://news.qq.com/rain/a/20250722A089YJ00))

### 5.5 안전·통합: ASIL B 콕핏 → ASIL-D 대응 safety island, 콕핏+ADAS 동일 SoC 옵션

82xx는 SEooC로 ASIL B를 상정한 순수 IVI 칩이다. Elite 브리프는 계열 공통으로 "ASIL-D 시스템 대응, 전용 safety island, 무간섭 격리"를 서술하고, 콕핏과 자율주행을 같은 SoC에 결합할 수 있다고 한다. 다만 **8397P 단독의 ASIL 등급은 공식 문서에서 분리 명시되지 않았다**(출처 미확인). 40+ 센서·20 카메라 입력은 콕핏 칩이 서라운드뷰·DMS/OMS·주차 보조까지 흡수하는 "콕핏-주차 통합(舱泊一体)" 구성을 염두에 둔 것이다. ([제품 브리프](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf) · [Lantronix Ride SX 4.0](https://www.lantronix.com/products/ride-sx-4-0-automotive-development-platform/))

### 5.6 소프트웨어 플랫폼: Type-1 하이퍼바이저·멀티유저 VM·edge orchestrator·장기 API 호환

브리프가 SW 스택을 사양 수준으로 명시한 점이 82xx 세대 문서와 다르다. 클러스터/IVI/승객 인스턴스를 앱 중심 멀티유저 VM으로 분리하고, 온디바이스 AI를 AI Orchestrator가 조율하며, AI Hub로 모델을 온보딩하는 흐름이 제품의 일부로 정의된다. ([제품 브리프](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf)) — 단, 2026-09-16 현재 AI Hub Automotive 모델 페이지의 칩셋 필터는 SA7255P/SA8255P/SA8295P/SA8650P/SA8775P뿐이고 SA8397P는 없다([Qualcomm AI Hub](https://aihub.qualcomm.com/automotive/models)). ExecuTorch Qualcomm 백엔드도 "SA8397은 `-m SA8397` 실패, SA8295 기본값 미러링으로 우선 지원" 요청 단계다([#16535, 2026-01-12](https://github.com/pytorch/executorch/issues/16535)). QAIRT 자동차 개요 문서는 SA8797(QC Linux PVM)은 열거하나 SA8397은 열거하지 않는다([QAIRT Auto 개요](https://docs.qualcomm.com/nav/home/auto_overview.html?product=1601111740009302)). **즉 공개 툴체인 성숙도는 82xx가 앞선다.**

---

## 6. 양산·생태계 현황 (2026-09 기준)

### 6.1 OEM

| OEM | 칩 | 상태 | 출처 |
|---|---|---|---|
| Leapmotor D19 | 8797P ×2 (콕핏 1 + ADAS 1) | 세계 최초 듀얼 Elite 중앙 컴퓨터 양산, CES 2026 공개, 2026-04 출시 | [퀄컴 PR 2026-01](https://www.qualcomm.com/news/releases/2026/01/leapmotor-and-qualcomm-debuts-world-s-first-automotive-central-c) · [CarNewsChina](https://carnewschina.com/2026/01/06/leapmotor-partners-with-qualcomm-to-launch-worlds-first-central-computing-platform-with-dual-snapdragon-automotive-platforms/) · [汽车之家 인터뷰](https://chejiahao.autohome.com.cn/info/25366884) |
| Li Auto L9/L8·차세대 콕핏 | 8797 | 2026 H1 출시, 5·6월 인도. 콕핏 8797 세계 최초 | [Gasgoo](https://autonews.gasgoo.com/articles/icv/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217) · [MarkLines](https://www.marklines.com/en/news/346249) |
| JLR × 체리 Freelander | **8397** | 2026-03-31 발표, "세계 최초 8397 탑재군" | [IT之家](https://m.ithome.com/html/934657.htm) |
| 체리 Exeed(星途) 신차 | **8397** | 2026년 Carmind 2.0 + 8397 | [腾讯新闻 2025-12-23](https://news.qq.com/rain/a/20251223A05T4R00) |
| Zeekr, GWM, NIO, Chery | Elite(세부 미상) | 퀄컴 CES 2026 디자인윈 10건에 포함 | [퀄컴 PR via MarketScreener](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026) |
| SAIC-GM | 8397/8797 | 2026 양산 계획(보도) | [新出行](https://www.xchuxing.com/article/154818) |
| Mercedes-Benz | Cockpit/Ride Elite | 2024-10 협력 발표. 2026 CLA는 4세대 계열 "Snapdragon Cockpit Platforms"(품번 미기재) | [Nasdaq](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms) · [퀄컴 PR 2025-09](https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a) |
| 기타(Nakul 인터뷰 언급) | Elite | VW·Geely·Audi·BYD·동풍닛산 등 "2026년 15종 이상" | [汽车之家 인터뷰](https://chejiahao.autohome.com.cn/info/25366884) |

### 6.2 Tier-1·플랫폼

| 회사 | 내용 | 출처 |
|---|---|---|
| **LG전자** | CES 2026, Cockpit Elite 기반 'AI 캐빈 플랫폼'(VLM·LLM·이미지 생성 온디바이스), 퀄컴 협업 HPC | [한국경제 via Nate 2025-12-11](https://news.nate.com/view/20251211n35389) |
| Visteon | Cockpit Elite 기반 양산 사양 HPC, Qwen 7B 컨시어지, 24+ 스피커 Dolby | [Visteon 2026-01-08](https://www.visteon.com/investors/investor-news/news-details/2026/Visteon-Showcases-Production-Ready-High-Performance-Compute-Solution-on-Snapdragon-Cockpit-Elite-Platform/default.aspx) |
| Panasonic Automotive | Cockpit Elite 기반 CDC/HPC | [Panasonic 2025-01-07](https://news.panasonic.com/global/press/en250107-5) |
| Garmin | Nexus 컴퓨팅 플랫폼에 Elite 채택 | [Garmin](https://www.garmin.com/en-US/newsroom/press-release/corporate/garmin-and-qualcomm-reveal-next-gen-digital-cockpit-solution-powered-by-snapdragon-cockpit-elite-platform/) |
| Thundersoft(中科创达) | RazorDCX Sylvania — SA8397P 도메인 컨트롤러(320 TOPS, SPECint2017 rate 80, 272 GB/s) | [Thundersoft](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/) |
| 车联天下 | SA8397P 콕핏 + SA8797P 융합 컨트롤러(2026 양산) | [汽车之讯](https://www.newsfcar.com/14736/) |

### 6.3 규모 지표(퀄컴 공식, CES 2026)

Snapdragon Cockpit Platform 누적 탑재 7,500만 대 이상(2025-06 기준), Snapdragon Ride SoC 약 100만 개 출하, Cockpit/Ride Elite 디자인윈 10건, Ride Flex 양산 프로그램 8건. ([퀄컴 PR via MarketScreener](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026))

---

## 7. IPCU 성능형 SoC 관점 시사점 (본 보고서 해석)

1. **"83xx = 8397P 하나"다.** 82xx처럼 최상위(8295P)·중간(8255P) 2단이 아니라, 콕핏 Elite는 현재 단일 품번이다. 성능·가격 계층을 나누려면 위로는 8797P, 아래로는 8255P/8295P와 조합해야 한다. 8397P 하위 파생 품번은 공개 출처에 없다(출처 미확인).
2. **CPU·NPU·메모리 모두 계단이 아니라 도약이다.** 공식 3×/3×/12×, 서드파티 30→320 TOPS, 128-bit LPDDR4X→256-bit LPDDR5X. IPCU가 "성능형"을 요구한다면 8397P는 콕핏 도메인에서 현재 퀄컴 최상위 선택지다.
3. **열·전력 예산은 재산정 필요.** 8397P 절대 전력은 공개 출처가 없다(15–20 W 설은 출처 미확인). 8797P는 70–80 W 추정. 도메인 컨트롤러 메모리도 24–36 GB LPDDR5X로 커진다. 하우징·방열 설계가 8255P 기준과 다를 가능성이 높다.
4. **SW 이식 비용의 핵심은 CPU 아키텍처와 하이퍼바이저다.** Oryon은 AArch64 호환이나 코어 토폴로지가 다르고, Elite 스택은 Type-1 하이퍼바이저·멀티유저 VM을 전제로 한다. 안전 파티션(클러스터)과 IVI 파티션 분리 설계를 8397P의 safety island 구조에 맞춰 다시 잡아야 한다.
5. **AI 툴체인은 아직 82xx가 성숙하다.** AI Hub·ExecuTorch·QAIRT 공개 문서에 SA8397P가 없다(2026-09-16). 양산 OEM들은 퀄컴 직접 지원(NDA SDK)으로 진행 중으로 보인다. 공개 자료 의존 개발이라면 시차를 감안해야 한다.
6. **8397P vs 8797P 선택.** 콕핏만이면 8397P, 콕핏+주차/ADAS 융합 또는 30B급 모델을 염두에 두면 8797P. Li Auto는 콕핏에도 8797을, JLR·Exeed·Zeekr은 8397을 택했다. 두 칩은 같은 세대라 SW 자산 공유가 가능하다는 점이 퀄컴의 "유연 아키텍처" 주장이다.
7. **공급·시점.** 2025 샘플링, 2026 양산 개시. 한국 Tier-1(LG전자)이 이미 Elite 기반 플랫폼을 공개했다. 2027~2028 SOP 프로그램이라면 83xx가 표준 후보다.

---

## 8. 미확인·상충 항목

| 항목 | 상태 |
|---|---|
| SA8397P Oryon 코어 수·클럭·캐시 | 출처 미확인(12~16코어 추정만 존재) |
| SA8397P 소비 전력 | 출처 미확인(15–20 W는 검색 요약 수준) |
| SA8397P 단독 ASIL 등급 | 출처 미확인(Elite 브리프는 계열 공통으로 ASIL-D 대응 서술) |
| SA8397P 공정 | 4nm — 퀄컴 서밋 보도 인용, 공식 문서 미확인 |
| SA8255P NPU TOPS | 상충: 24 TOPS(ResearchInChina) vs 48 TOPS(EEWORLD) |
| SA8797P sparse TOPS | 상충: 640(新出行·Leapmotor 1,280/2) vs 700(Nakul 인터뷰) |
| Ride Flex SA8775P NPU | 상충: 72 TOPS dense(新出行) vs 144 TOPS(퀄컴 서밋 보도; sparse 추정) |
| 8397P 외 83xx 품번 존재 여부 | 출처 미확인 |
| Mercedes-Benz Elite 양산 차종·시점 | 출처 미확인(협력 발표만) |
| 퀄컴 공식 절대 수치(TOPS·대역폭) | 공식 문서 없음. 배수만 공식 |

---

## 9. 출처

상세 수집·검증 기록: [`reference/references.md`](reference/references.md)

**공식(퀄컴·OEM·Tier-1)**
- [Snapdragon Cockpit Elite / Ride Elite 제품 브리프 (PDF)](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Cockpit-Elite-Snapdragon-Ride-Elite-Product-Brief.pdf)
- [퀄컴 X 게시물 2024-10-22](https://x.com/Qualcomm/status/1848811003225473177)
- [퀄컴 PR 2026-01: Leapmotor 듀얼 Elite 중앙 컴퓨터](https://www.qualcomm.com/news/releases/2026/01/leapmotor-and-qualcomm-debuts-world-s-first-automotive-central-c)
- [퀄컴 PR 2026-01: Digital Chassis 모멘텀 (MarketScreener 전재)](https://www.marketscreener.com/news/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-digital-chassis-momentum-and-agentic-ce7e59deda80f026)
- [퀄컴 PR 2025-09: Mercedes-Benz CLA](https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a)
- [퀄컴 4세대 콕핏 발표 2021-01 (telematicswire 전재)](https://telematicswire.net/qualcomm-introduces-gen4-snapdragon-automotive-cockpit-platform/)
- [Qualcomm AI Hub — Automotive](https://aihub.qualcomm.com/automotive/models) · [QAIRT Auto Platform Overview](https://docs.qualcomm.com/nav/home/auto_overview.html?product=1601111740009302)
- [Panasonic PR 2025-01-07](https://news.panasonic.com/global/press/en250107-5) · [Visteon PR 2026-01-08](https://www.visteon.com/investors/investor-news/news-details/2026/Visteon-Showcases-Production-Ready-High-Performance-Compute-Solution-on-Snapdragon-Cockpit-Elite-Platform/default.aspx) · [Garmin PR](https://www.garmin.com/en-US/newsroom/press-release/corporate/garmin-and-qualcomm-reveal-next-gen-digital-cockpit-solution-powered-by-snapdragon-cockpit-elite-platform/) · [Thundersoft CES 2026](https://www.thundersoft.com/thundersoft-new-gen-ai-domain-control-released-at-ces-2026/)

**개발 플랫폼 벤더**
- [Lantronix SA8295P ADP 사양서 (PDF)](https://cdn.lantronix.com/wp-content/uploads/pdf/MPB-00130-RevB-SA8295P-US.pdf)
- [Lantronix Ride SX 4.0 (SA8255P/SA8775P)](https://www.lantronix.com/products/ride-sx-4-0-automotive-development-platform/) · [Thundercomm Ride SX 4.0](https://www.thundercomm.com/product/sa8255p-sa8775p-automotive-development-platform/)
- [Arrow SA-8255P 품번](https://www.arrow.com/en/products/sa-8255p-0-fcbga1723hs-tr-01-0-ab/qualcomm)

**서드파티(언론·분석·블로그)**
- [Nasdaq/The Fly 2024-10-22](https://www.nasdaq.com/articles/qualcomm-debuts-snapdragon-cockpit-elite-and-snapdragon-ride-elite-platforms) · [Futurride 2024-10-22](https://futurride.com/2024/10/22/qualcomm-ups-snapdragon-tech-with-cockpit-and-ride-elite-platforms/) · [Futurum](https://futurumgroup.com/insights/qualcomm-launches-new-elite-snapdragon-automotive-platforms/) · [Counterpoint](https://counterpointresearch.com/en/insights/qualcomm-snapdragon-cockpit-elite-powering-premium-visual-intelligent-cockpit-automotive-experiences)
- [Gasgoo 2026-06-16 Li Auto](https://autonews.gasgoo.com/articles/icv/li-auto-launches-new-gen-cockpit-platform-powered-by-proprietary-os-qualcomms-latest-chip-2066711041814409217) · [CarNewsChina 2026-01-06](https://carnewschina.com/2026/01/06/leapmotor-partners-with-qualcomm-to-launch-worlds-first-central-computing-platform-with-dual-snapdragon-automotive-platforms/) · [vision-mobility 2026-01](https://vision-mobility.de/en/news/ces-2026-leapmotor-becomes-the-first-oem-to-use-qualcomms-dual-chipset-sa8797p-389375.html)
- [汽车之家 车家号 Nakul Duggal 인터뷰 2026-04-28](https://chejiahao.autohome.com.cn/info/25366884) · [网易 퀄컴 중국 서밋 2026-06](https://www.163.com/dy/article/KUP4MPM60511DTVV.html) · [IT之家 2026-03-31](https://m.ithome.com/html/934657.htm) · [快科技 2026-03-31](https://news.mydrivers.com/1/1112/1112866.htm) · [新浪 2026-03-31](https://www.sina.cn/news/detail/5282621412351047.html)
- [新出行 8797 三杀](https://www.xchuxing.com/article/154818) · [腾讯新闻 2025-07-07 (Hexagon V83/V85)](https://news.qq.com/rain/a/20250707A07U3500) · [腾讯新闻 2025-07-22 (Li i8 8295P)](https://news.qq.com/rain/a/20250722A089YJ00) · [腾讯新闻 2024-12-21 (SA8797/8799 추정)](https://news.qq.com/rain/a/20241221A042RT00) · [腾讯新闻 2024-10-25](https://news.qq.com/rain/a/20241025A09PRM00) · [腾讯新闻 2025-12-23 Exeed](https://news.qq.com/rain/a/20251223A05T4R00)
- [汽车之讯 车联天下×퀄컴](https://www.newsfcar.com/14736/) · [CSDN 8397 vs 8295](https://blog.csdn.net/m0_72165397/article/details/155090743) · [CSDN/高工智能汽车 2024-06](https://blog.csdn.net/GGAI_AI/article/details/139519069) · [EEWORLD 콕핏 SoC 순위](https://en.eeworld.com.cn/news/qcdz/eic657301.html) · [ResearchInChina 2024-07 (PDF)](http://www.researchinchina.com/UpLoads/ArticleFreePartPath/20240723085131.pdf) · [pcauto 8295](https://www.pcauto.com/my/news/30tops-a-deep-analysis-of-the-qualcomm-8295-chip-intelligent-driving-under-5nm-process-14039) · [PassMark SA8255P](https://www.cpubenchmark.net/cpu.php?cpu=Qualcomm+SA8255P&id=6866)
- [한국경제 via Nate 2025-12-11 (LG전자)](https://news.nate.com/view/20251211n35389)
- [pytorch/executorch #16535](https://github.com/pytorch/executorch/issues/16535)
