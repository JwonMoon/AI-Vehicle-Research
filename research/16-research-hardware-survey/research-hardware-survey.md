# 차량용 AI 연구는 어떤 장비로 하나 — 자율주행 SW · 온디바이스 AI 연구 유형별 실제 사용 하드웨어와 연구용 조합

> **작성일**: 2026-10-14 · **상태**: 초판
> **목적**: 장비 구입 전에, 비슷한 연구·업체가 **실제로 어떤 하드웨어 조합을 쓰는지**를 연구 유형별로 확인한다. 두 갈래(자율주행 SW / 온디바이스 AI) 모두 **차량에 탑재해 돌리는 것**을 전제로, 벤치 단계와 실차 단계를 함께 다룬다.
> **조사 범위**: 이 저장소의 기존 문서(research/·seminars/·news/)는 **참고하지 않았다**. 외부 공개 자료(제품 페이지·모델카드·README·논문·개발자 포럼·언론)만으로 처음부터 조사했다.
> **출처 표기 원칙**: 모든 사실 문장에 출처 ID와 등급을 붙인다. 🔍 공식(벤더 제품 페이지·모델카드·README·공시) / 📄 논문·학위논문 / 📰 언론·시장조사·2차 / 💬 개발자 포럼·커뮤니티 / ⚠️ 미확인·추정·출처 간 충돌. TOPS는 정밀도(INT8/FP4 등)를 병기하고, 벤더가 정밀도를 밝히지 않으면 "정밀도 미상"으로 적는다. 가격은 조사일 공개 표시가(USD 등 표시 통화 그대로)이며 환율 환산은 하지 않는다. 판단은 `분석` 블록에만 쓴다. 출처 목록은 [reference/references.md](reference/references.md).
> **조사 환경 제약 (2026-10-14)**: 조사 환경의 프록시가 대부분의 벤더·언론 사이트 직접 열람을 차단해, GitHub(NVlabs/alpamayo, QwenLM/Qwen-Drive-1.0, NVIDIA/TensorRT-Edge-LLM 문서, Autoware 레퍼런스 HW 문서, astuff/pacmod3, TUMFTM/edgar_digital_twin)와 PyPI(peykan)만 **직접 열람(✅)** 했다. 그 외는 검색 엔진이 돌려준 본문 발췌로 확인했으며, 출처 ID 뒤 등급은 페이지의 성격(공식/논문/언론/포럼)을 뜻한다.

출처 ID 접두어: **N** NVIDIA · **Q** Qualcomm · **X** 기타 SoC(Xpeng·Tesla·Horizon·Mobileye·Renesas·TI·Ambarella·Hailo·Huawei·comma·시장조사) · **M** 모델·벤치·논문 · **S** 센서·카메라·인터페이스·연구차량 · **V** 완성차 사례 · **O** 온디바이스·콕핏·에이전트 사례 · **P** 호스트 GPU 가격.

---

## 결론 먼저

1. **자율주행 양산은 "NVIDIA Orin-X 2개 → Thor-U 1개 또는 자체 칩"으로 가고, 연구 재현은 24 GB+ dGPU 워크스테이션에서 시작한다.** Li Auto는 AD Max를 2× Orin-X에서 1× Thor-U(700 TOPS, 정밀도 미상)로 바꾸며 VLA를 올렸고 [V1][V2] 🔍📰, Xpeng은 자체 Turing 칩 3개(2개 VLA·1개 콕핏 VLM)로 갔다 [X2][V4] 📰. 반면 공개 VLA 모델(Alpamayo 10B, Qwen-Drive 4B)의 공식 요구사항은 둘 다 "24 GB 이상 GPU"다 [M1][M7] ✅.
2. **콕핏 온디바이스 LLM의 양산 주류는 퀄컴 SA8295P(2개 묶음)이고, 10B급 이상은 Cockpit Elite(QAM8397P)·Ride Elite(QAM8797P)·자체 칩으로 넘어가는 중이다.** Lynk & Co 900·Zeekr 9X가 듀얼 8295 [Q11][V5] 📰, Li Auto 신형 콕핏이 8797(NPU 320 TOPS, 정밀도 미상) [Q19] 📰, Visteon은 Cockpit Elite 위에 Qwen 7B를 NPU로 돌렸다 [O2] 🔍.
3. **연구실이 살 수 있는 퀄컴 차량 보드는 Lantronix·Thundercomm의 ADP(SA8295P US$6,300, SA8255P/SA8775P US$4,999)지만 "퀄컴 승인 필요 + 소프트웨어 미포함"이다** [Q5][Q6][Q7] 🔍. Ride SDK는 파트너 전용이다 [Q8] 🔍. SA8255P는 퀄컴이 NPU TOPS를 공개하지 않았고 온디바이스 LLM 양산 사례도 찾지 못했다 ⚠️.
4. **"Thor"는 두 제품이다.** DRIVE AGX Thor DevKit(64 GB, GMSL 18ch, 350 W, 가격 비공개·파트너 프로그램) [N1][N2] 🔍과 Jetson AGX Thor DevKit(128 GB, HSB 카메라, 40–130 W, US$3,499→5,499) [N7][N9] 🔍📰은 메모리·카메라 인터페이스·SDK·구매 경로가 모두 다르다.
5. **실차 탑재를 가르는 것은 칩보다 카메라 인터페이스(GMSL2/3)·CAN FD·DBW·전원이다.** 대학 연구차량(UB·TUM·KIT)은 모두 x86 PC + 데스크톱 GPU + GMSL/GigE 카메라 + LiDAR + GNSS/INS + DBW 조합이고 [S8][S9][S10] 📄, Jetson/DRIVE에 GMSL 카메라를 붙이려면 별도 디시리얼라이저 보드가 필요하다 [S13] 🔍.

### 한 장 매트릭스 — 연구 유형 × 실제 사례 × 연구용 조합

| 연구 유형 | 실제 사례의 하드웨어 | 연구용 벤치 조합 | 연구용 실차 조합 | 근거 |
|---|---|---|---|---|
| **A1** E2E/VLA 주행(Qwen-Drive·Alpamayo) | Li i8: 1× Thor-U 700 TOPS + LiDAR · Xpeng G7 Ultra: 3× Turing 2,250 TOPS · DriveVLM: 2× Orin-X(E2E 1 + VLM 1, 410 ms) | 24 GB+ dGPU(RTX 4090/5090·RTX PRO 6000) + 공개 데이터셋 | Jetson AGX Thor(128 GB) 또는 DRIVE AGX Thor/Orin DevKit + GMSL 카메라 4~7 | V1 X2 M8 M1 M7 M4 |
| **A2** 인식(BEV·3D)·데이터 수집 | UB: MKZ + Dataspeed + VLP-32 + OEM7 + Nuvo-10108GC · TUM EDGAR: 8 cam + 5 LiDAR + 6 radar + RTX A6000 · Hyperion 10: 14 cam/9 radar/1 LiDAR | x86 PC + RTX GPU + GigE/USB 카메라 1~2 | x86 차량 PC(Neousys/ADLINK) + GMSL/GigE 카메라 6~8 + LiDAR 1~2 + GNSS/INS + DBW | S8 S9 N15 S2 |
| **A3** L2/L2+ ADAS 양산급·저전력 | Horizon J6E/J6M(80/128 TOPS) · Orin-N · EyeQ6H(34 TOPS INT8) · R-Car V4H(34 TOPS) · TDA4VH(32 TOPS) · comma 3X(Snapdragon 845) | TI SK-TDA4VM(US$199) · Hailo-10H M.2(US$260) · D-Robotics RDK S100(US$439–499) | comma 3X/four(US$999) + 차량 하네스(US$99) | X4 X7 X9 X10 X12 X14 X6 |
| **A4** 차량 통합·인터페이스 | DBW(Dataspeed·PACMod) · CAN FD(PCAN·Kvaser) · 100/1000BASE-T1 변환기 · 12 V DC-DC | PCAN-USB FD(US$347–379) 또는 Kvaser Leaf v3(US$349–407) + 가상 CAN | DBW 키트(견적) + CAN FD 2ch + T1 미디어 컨버터(€400) + DC-DC 350 W급 | S20 S21 S22 N3 |
| **B1** 콕핏 온디바이스 LLM/VLM | Lynk & Co 900·Zeekr 9X: 2× SA8295P · NIO: 1× 8295 + 4× Orin-X 공유 · Li: 8797(NPU 320 TOPS) · Xpeng: Turing(30B 로컬) · Visteon: Cockpit Elite + Qwen 7B | Jetson AGX Orin 64 GB(US$1,999) 또는 Lantronix SA8295P ADP(US$6,300, 승인 필요) | 같은 보드를 12 V 전원·CAN으로 차량 연결 | Q11 V5 V7 Q19 O3 O2 Q5 |
| **B2** LLM/VLM 동작구조 분석·프로파일링 | Jetson Thor: Qwen2.5-VL-7B NVFP4 61 tok/s(EAGLE3 177) · Orin 64 GB: INT4 64 tok/s · SA8295P ADP: Llama 3.2 1B 11 tok/s | Jetson AGX Orin 64 GB(FP16/INT8/INT4) → 필요 시 Jetson AGX Thor(FP8/NVFP4) · jtop/INA3221 전력 측정 | 동일 | N12 N11 Q10 S26 |
| **B3** 온디바이스↔클라우드 확장 | Cerence xUI(Orin 온보드 + 클라우드) · Li Mind GPT-3o(엣지 NPU + 클라우드) · FEV: Phi-4-mini on DRIVE AGX 오프라인 + 클라우드 폴백 · AWS 가이드(온보드 SLM + 클라우드 LLM 시맨틱 라우팅) | 엣지 보드 + 호스트 GPU(RTX PRO 6000 96 GB 또는 DGX Spark 128 GB) + 유선 10 GbE | 엣지 보드 + 5G 모듈(Quectel RM520N-GL, US$276–327) | O6 O5 O7 M12 P1 P2 S25 |
| **B4** AI 에이전트·하네스 PoC(차량 데이터) | Peykan(MCP over CAN/OBD/UDS/J1939, 가상 CAN 내장) · Pi + CAN HAT 테스트베드 · KUKSA Databroker(VSS gRPC) | 엣지 LLM 보드 + 가상 CAN(SocketCAN vcan) | 엣지 LLM 보드 + CAN HAT/USB-CAN + OBD-II 커넥터(읽기 전용) | O9 O10 O11 S24 |

---

## 1. 연구 유형별 — 실제로 무엇을 쓰나

### A1. E2E / VLA 주행 (Qwen-Drive·Alpamayo 통합)

**연구 내용**: 멀티카메라 입력 → VLM 백본 → 궤적 출력 모델을 올리고, 실차에서 지연·주행 품질을 본다.

| 사례 | 컴퓨트 | 카메라·센서 | 지연·메모리 | 근거 |
|---|---|---|---|---|
| NVIDIA Alpamayo 1.5-10B(공개 모델) | 공식 요구: **NVIDIA GPU ≥24 GB VRAM**(RTX 3090/4090·A5000·H100 예시), 16 GB는 OOM 가능 | 기본 4개 카메라(cross-left/front-wide/cross-right 120° + front-tele 30°) × 4 프레임(0.1 s 간격), 출력 6.4 s 궤적 @10 Hz | 가중치 22 GB; 백본 8.2B + 액션 전문가 2.3B; TensorRT-Edge-LLM 내보내기는 **FP16만** 지원, Thor에서 엔진 빌드(maxKVCache 4096, batch 6) | M1 ✅ M3 ✅ M2 🔍 M4 ✅ |
| Alpamayo on DRIVE AGX Thor(포럼) | DRIVE AGX Thor, DriveOS 7.2.5 | — | FP16 엔진 직렬화에서 ~15.17 GB 할당 실패(OOM), batch 1·KV 2048에서도 발생; INT8 경로 질문 미답 | M5 💬 |
| Alpamayo-R1 지연(언론) | RTX PRO 6000 | 4 카메라 × 2 s | 99 ms | M6 📰 |
| Qwen-Drive-1.0-4B(공개 모델) | README: **24 GB+ GPU 권장** | 데이터셋 nuScenes·NAVSIM·Waymo E2E·NVIDIA PhysicalAI(카메라 수 README 미기재) | VLM 9.1 GB + 플래너 2.1 GB + 인식 헤드 0.5 GB; 출력 5 s @10 Hz; NAVSIM PDMS 90.7(RL) | M7 ✅ |
| DriveVLM(논문, 실차) | **2× Orin-X**: 1번에 고주파 E2E, 2번에 VLM, 비동기 협업 | 차량 카메라 | VLM 평균 410 ms on Orin-X; 차량 제약으로 모델 <4B | M8 📄 |
| Li Auto i8(양산) | Max/Ultra: **1× Thor-U 700 TOPS(정밀도 미상)** · Pro: Horizon J6M 128 TOPS | 전 트림 LiDAR 기본(Hesai ATL) | VLA 드라이버를 Orin-X·Thor-U AD Max에 배포 | V1 🔍 V2 📰 |
| Xpeng G7 Ultra / P7(양산) | **3× Turing(2,250 TOPS "유효", 정밀도 미상)**: 2개 로컬 VLA, 1개 콕핏 VLM; Max 트림은 2× Orin-X 508 TOPS | LiDAR 없음(G7) | Turing 단일 칩 750 TOPS, 30B 모델까지 지원(제조사 주장) | X1 🔍 X2 📰 V4 📰 |
| UNIST(학위논문, HMG 2025 E2E 챌린지 1위) | **Jetson AGX Orin, 16 Hz** | 시뮬레이터(MORAI) | 챌린지 2라운드는 Orin-X 기반 PC 환경 | M9 📄 |

`분석` — 공개 VLA 두 모델 모두 "24 GB GPU"가 1차 요구이고, 엣지 배포는 FP16 기준 ~15 GB급 엔진이라 Thor(64/128 GB)에서도 메모리 여유가 관건이다(포럼 OOM 사례). 양산은 Thor-U·Turing처럼 700 TOPS급 단일 칩에 VLA를 올리는 흐름이며, 연구에서 그 경로를 흉내 내려면 **Jetson AGX Thor(128 GB, NVFP4 지원)** 가 메모리·정밀도 면에서 가장 가깝고, DRIVE AGX Thor는 파트너 프로그램을 통해야 한다 [N6] 💬.

**연구용 조합**: 벤치 = RTX 4090(24 GB)/RTX 5090(32 GB)/RTX PRO 6000(96 GB) 워크스테이션 + 공개 데이터셋 → 엣지 = Jetson AGX Thor DevKit(또는 Orin 64 GB에서 INT4로 축소) → 실차 = 같은 보드 + GMSL 카메라 4~7 + 디시리얼라이저 + 12 V 전원.

### A2. 인식(BEV·3D 검출·점유)·데이터 수집

**연구 내용**: 멀티카메라·LiDAR·GNSS 동기 수집, BEV/3D 모델 학습·평가.

| 사례 | 컴퓨트 | 센서 | 차량·인터페이스 | 근거 |
|---|---|---|---|---|
| Univ. at Buffalo Autoware 테스트베드(IEEE IV 2026) | Neousys Nuvo-10108GC(350 W급 RTX 1장 지원 x86) | Velodyne VLP-32, NovAtel OEM7 GNSS+INS | Lincoln MKZ + Dataspeed DBW | S8 📄 🔍 |
| TUM EDGAR(VW T7) | InoNet 차량 PC + RTX A6000 | 8× Basler 모노 + 2× Framos 스테레오 카메라, 5 LiDAR(Ouster 2·Seyond 2·Aeva 1), 6 Continental 레이더, NovAtel GNSS/IMU | CAN-FD·Ethernet·USB | S9 📄 ✅ |
| KIT CoCar NextGen(Audi A6) | 서버급 PC, 다중 GPU | 12 LiDAR(4D 6 + 360° 6), 9 Full-HD 카메라, 3× 4D 레이더, 이중 안테나 GNSS, 5G V2X | — | S10 📄 |
| Autoware 레퍼런스 HW 카탈로그 | ADLINK·Neousys·Advantech·NXP·Crystal Rugged·MIIVII(Jetson Orin/Thor 기반) 21종 | LiDAR 37종(Hesai·Ouster·Velodyne·RoboSense·Livox), 카메라(TIER IV C1/C2/C3 GMSL2, FLIR·Lucid GigE), GNSS/INS(NovAtel·Xsens·SBG·Applanix) | DBW: Dataspeed·AStuff PACMod·Schaeffler-Paravan | S1–S7 ✅ |
| NVIDIA DRIVE Hyperion 10(레퍼런스) | 2× DRIVE AGX Thor | 14 카메라, 9 레이더, 1 LiDAR(Hesai), 12 초음파, 실내 카메라 4 | — | N15 🔍 |
| Pony.ai 7세대 로보택시 | 4× Orin-X(1,016 TOPS) | 9 LiDAR(주 LiDAR Hesai AT128 ×4), 14 카메라, 4 레이더 | — | S11 📰 |
| Waymo 6세대 드라이버 | — | 13 카메라, 4 LiDAR, 6 레이더 | — | S12 🔍 |

`분석` — 대학 연구차량은 예외 없이 **x86 + 데스크톱 GPU** 이고 임베디드 SoC는 양산·로보택시 쪽이다. 데이터 수집이 목적이면 GigE/USB 카메라와 x86 PC가 드라이버·시간동기 면에서 가장 수월하고, GMSL은 양산 카메라 재현이 필요할 때 선택한다.

**연구용 조합**: 벤치 = x86 PC + RTX GPU + GigE 카메라 1~2 → 실차 = Neousys/ADLINK 차량 PC + 카메라 6~8(GMSL2 또는 GigE) + LiDAR 1(Hesai AT128/Ouster OS1/RoboSense Helios) + GNSS/INS(Xsens MTi-680G 또는 NovAtel) + DBW.

### A3. L2/L2+ ADAS 양산급·저전력

**연구 내용**: 수십 TOPS급 양산 SoC에서 인식·주행 스택을 돌리고 전력·비용을 본다.

| 칩 | AI 연산 | 양산 채택 | 연구용 입수 | 근거 |
|---|---|---|---|---|
| Horizon Journey 6E/6M/6P | 6E ~80 · 6M 128 · 6P 560 TOPS(정밀도 미상) | BYD God's Eye C(J6), 100+ 모델; Li i8 Pro(J6M); Chery Exlantix E05(J6P) | 공개 개발보드 없음. 근접: D-Robotics RDK S100(BPU Nash 80 TOPS, 12 GB) US$439–499 ⚠️(J6와 동일 다이 여부 미확인) | X4 📰 X5 📰 V1 🔍 X6 📰 |
| NVIDIA Orin-N / Orin-X | Orin-X 254 INT8 TOPS | 2025 Q1 중국 ADAS SoC 51.8%(Orin-X+N) | DRIVE AGX Orin DevKit(파트너) / Jetson AGX Orin 64 GB US$1,999 | N4 🔍 X18 📰 N10 🔍 |
| Mobileye EyeQ6 High / Lite | 34 / 5 DL TOPS(INT8) | EyeQ6L 4,600만 대 수주; EyeQ6H SOP 2025 | EyeQ Kit SDK는 완성차 전용(파트너) | X7 🔍 X8 📰 |
| Renesas R-Car V4H | 34 TOPS(정밀도 미상) | 양산 차종 미확인 ⚠️ | White Hawk 평가보드(2× CSI-2, 8× CAN) 가격 미공개 | X9 🔍 |
| TI TDA4VM / TDA4VH | 8 / 32 TOPS(INT8) | — | SK-TDA4VM US$199(출시가); J784S4XEVM 가격 미공개 | X10 🔍 |
| Ambarella CV3-AD685 | 패밀리 최대 500 eTOPS | Continental SOP 2027 | 파트너 전용 | X11 🔍 |
| Hailo-10H / Hailo-8 (M.2 가속기) | 40 INT4 / 20 INT8 TOPS, 2.5 W · 26 INT8 TOPS | — | ASUS UGen300(Hailo-10H 8 GB) US$259.99; Hailo-8 M.2 US$179.99 | X12 🔍📰 |
| comma 3X / comma four | Snapdragon 845(GPU에서 tinygrad로 주행 모델 실행) | openpilot 지원 325+ 차종 | comma 3X US$999(출시 US$1,250), four US$999, 하네스 US$99; 3× 1080p 140 dB 카메라, CAN FD, LTE | X14 🔍 X15 🔍 |

`분석` — 양산 ADAS SoC는 대부분 파트너·NDA 경로라 연구실 입수가 어렵다. 저전력 양산급을 체험할 현실적 경로는 **TI SK-TDA4VM(US$199), Hailo M.2 가속기, comma 3X(실차 E2E 오픈소스)** 세 가지다.

### A4. 차량 통합·인터페이스 (두 갈래 공통)

| 항목 | 대표 제품 | 공개가 | 근거 |
|---|---|---|---|
| DBW(조향·제동·가속 제어) | Dataspeed ADAS Kit(Lincoln MKZ·Ford Fusion/Mondeo) · AStuff PACMod(Polaris GEM, Lexus RX-450h, Honda CR-V 등) | 견적(비공개) | S20 🔍 ✅ |
| CAN FD 인터페이스 | PEAK PCAN-USB FD · Kvaser Leaf v3(CAN FD 8 Mbit/s) | US$347–379 · US$349–407 | S21 🔍 |
| 자동차 이더넷 변환 | Intrepid RAD-Moon 2(100/1000BASE-T1↔1000BASE-T, H-MTD/MATEnet) · MACH Systems T1 컨버터 | 견적 · €400–410 | S22 🔍 |
| 전원 | DRIVE AGX Thor: TDP 350 W, 입력 9–16 V(과도 7–32 V), SKU 12는 차량 배터리 직결 · Jetson AGX Thor: 40–130 W, 28 V 5 A(피크 7.5 A) · 400 W급 12 V DC-DC(Vicor V24A12C400BL US$460) | — | N3 🔍 S23 💬 S27 🔍 |
| 소형 CAN(라즈베리파이) | PiCAN2(MCP2515) €44.95 · Waveshare 2-CH CAN FD HAT | — | S24 🔍 |

### B1. 콕핏 온디바이스 LLM/VLM (양산 사례)

| 사례 | 콕핏 SoC | 온디바이스 모델 | 분담 구조 | 근거 |
|---|---|---|---|---|
| Lynk & Co 900 (2025) | **2× SA8295P**(각 "최대 60 TOPS", 정밀도 미상; 2021 출시 보도는 30 TOPS ⚠️ 충돌) + 후석용 1개 | 모델 크기 미공개 | 주행은 NVIDIA Thor 별도 | Q11 📰 Q12 📰 |
| Zeekr 9X (2025) | 2× Snapdragon 8295 | 미공개 | 주행 2× Thor-U | V5 📰 |
| NIO 2024 라인업 | 1× 8295 + 4× Orin-X(1,016 TOPS) | NOMI GPT: 온디바이스 멀티모달 인식(오프라인) | Orin-X 중 최대 256 TOPS를 콕핏에 공유 | V7 📰 |
| Li Auto 신형 콕핏 (2026) | Snapdragon 8797 Elite, NPU 320 TOPS(정밀도 미상) | Mind GPT-3o: 엣지 NPU + 클라우드 분담 | 2026 L9/L8 공시 | Q19 📰 O5 📰 Q16 🔍 |
| Visteon on Cockpit Elite (CES 2026) | QAM8397P(NPU 12× 성능 주장, TOPS 미공개) | **Qwen 7B**, QNN으로 양자화해 Hexagon NPU 실행 | — | O2 🔍 Q1 🔍 |
| Xpeng × Banma (2026 윈치) | Xpeng Turing 750 TOPS | **30B급 로컬** 모델; Banma AutoOmni 2.0 23B-A3B MoE는 8397 대상 | "온디바이스 우선, 클라우드 보조" | O3 📰 O4 📰 |
| SemiDrive X10 (2026 양산) | 4 nm, NPU 40 TOPS, 154 GB/s | 7B 멀티모달 | 소·중·대 모델 하이브리드 | X17 📰 |
| Cerence CaLLM Edge | DRIVE AGX Orin 등 | Phi-3 3.8B, 4-bit | 임베디드 단독 또는 하이브리드 폴백 | O6 🔍 |
| Mercedes CLA MBUX | Snapdragon Cockpit + 5G 모뎀 | — | 대화 에이전트는 Google Gemini(클라우드) | O8 📰 🔍 |
| SA8255P 채택차(Chery G700, Ford Bronco NE 등) | SA8255P(NPU TOPS 비공개) | Desay SV·ModelBest 1.2B 음성 모델 사례 외 LLM 양산 미확인 ⚠️ | — | Q18 📰 Q13 📰 |

`분석` — 양산 콕핏 LLM은 **8295 2개(10B 미만)** 와 **Elite/자체 칩(7~30B)** 으로 나뉜다. 퀄컴 쪽은 모델 크기·TOPS를 거의 밝히지 않아, 연구에서 "양산 콕핏 수준"을 재현하려면 SA8295P ADP(US$6,300, 승인 필요)가 유일한 직접 경로이고, 성능 비교·프로파일링은 Jetson 쪽이 자료가 훨씬 많다.

### B2. LLM/VLM 동작구조 분석·프로파일링

| 플랫폼 | 공식 벤치 | 정밀도 지원 | 입수 | 근거 |
|---|---|---|---|---|
| Jetson AGX Thor (T5000, 128 GB, 273 GB/s) | TensorRT-Edge-LLM v0.10: Qwen2.5-VL-7B NVFP4 61.0 tok/s(batch 1), EAGLE3 투기 디코딩 177.3 tok/s; Llama-3.1-8B NVFP4 54.9(EAGLE3 189.2) · vLLM: Llama 3.1 8B 41.3/150.8 tok/s(동시 1/8) | FP16·FP8·NVFP4·INT4 | US$3,499(2025-08) → US$5,499(2026-07) | N12 ✅ N13 🔍 N9 📰 |
| Jetson AGX Orin 64 GB (204.8 GB/s) | Edge-LLM v0.9: Qwen2.5-VL-7B INT4 AWQ EAGLE3 64.4 tok/s(12.1 GB) | **FP16·INT8·INT4만**(FP8/FP4 불가) | US$1,999 | N12 ✅ N11 ✅ N10 🔍 |
| DGX Spark (GB10, 128 GB, 273 GB/s) | Qwen2.5-VL-7B NVFP4 55.6 tok/s(EAGLE3 154.9); LMSYS: GPT-OSS 20B 49.7 tok/s vs RTX PRO 6000 215 tok/s | FP4 | US$3,999 → 4,699(2026-02) → 6,950(2026-10) | N12 ✅ M11 📰 P2 💬📰 |
| Qualcomm SA8295P ADP | AI Hub: Llama 3.2 1B(w4, Genie) 11.0 tok/s | QNN(Hexagon NPU) | US$6,300(승인 필요) | Q10 🔍 Q5 🔍 |
| DRIVE AGX Orin/Thor | DriveOS LLM SDK(현 TensorRT-Edge-LLM): Llama 3/3.1 8B·3.2 3B, Qwen2.5 7B, Qwen2-VL; FP16/FP8/NVFP4(Thor)/INT4 | — | 파트너 프로그램 | N14 🔍 N11 ✅ |
| 학술 사례 | Jetson Orin AGX에서 2.7B–32.8B LLM을 전력 모드별 측정(arXiv 2506.09554) · LLaMA 3.2 on AGX Orin 평균 응답 5.07 s(AI-CDA4All) · VLA 모델을 Orin 15/30/50 W 모드 vs 클라우드 GPU 비교(arXiv 2509.11480) | — | — | M10 📄 |
| 계측 | Jetson 온보드 INA3221 레일(GPU·CPU·SoC·5 V) + jtop | — | 무료 | S26 💬📰 |

`분석` — 동작구조 분석(KV 캐시, 투기 디코딩, 정밀도별 거동)은 **Orin 64 GB로 시작해도 충분**하나, FP8/NVFP4와 EAGLE3를 보려면 Thor가 필요하다. Edge-LLM 공식 표에서 Thor와 Orin이 같은 모델로 비교돼 있어 세대 간 분석에 쓸 수 있다.

### B3. 온디바이스 ↔ 클라우드 확장 구조

| 사례 | 차량 측 | 클라우드 측 | 분담 방식 | 근거 |
|---|---|---|---|---|
| NVIDIA TensorRT-Edge-LLM 인캐빈 레퍼런스 | DRIVE AGX Thor / Jetson Thor에 ASR+TTS+LLM 온보드 | 대형 모델 | 오케스트레이터가 협업 | N16 🔍 |
| Cerence xUI | DRIVE AGX Orin(우선 최적화)에 CaLLM Edge | 클라우드 LLM | 하이브리드, 오프라인 폴백 | O6 🔍 |
| Li Auto Mind GPT-3o | 엣지 NPU | 클라우드 GPT | 추론 분할 | O5 📰 |
| FEV × Microsoft × NVIDIA (2026-07) | Phi-4-mini on DRIVE AGX(오프라인 음성 제어) | 클라우드 LLM | 온보드 SLM이 폴백 | O7 🔍 |
| AWS In-Vehicle AI Assistant 가이드 | 온보드 SLM + 툴 레지스트리·시맨틱 캐시 | Bedrock/SageMaker | 시맨틱 라우팅, OTA 재학습 | M12 🔍 |
| 엣지-클라우드 투기 디코딩(TMLR 2025) | 엣지 드래프트 모델 | 클라우드 타깃(early exit) | 지연 최대 35% 감소 | M12 📄 |

**연구용 조합**: 엣지(Jetson Orin/Thor) + 호스트 GPU 서버(RTX PRO 6000 96 GB/1,792 GB/s US$8,435~ 또는 DGX Spark 128 GB) + 유선 10 GbE(벤치) / Quectel RM520N-GL 5G 모듈(US$276–327, 실차) [P1][P2][S25] 🔍📰.

### B4. AI 에이전트·하네스 PoC (차량 데이터 접근)

| 구성요소 | 사례 | 근거 |
|---|---|---|
| 에이전트 ↔ 차량 버스 | **Peykan 0.2.1(2026-10-07)**: MCP 서버로 CAN·OBD-II·UDS·J1939를 LLM에 노출, **가상 CAN + ECU 시뮬레이터 내장**(7종 고장 시나리오), cantools DBC 디코딩, SocketCAN/PCAN/Kvaser/Vector/slcan 지원, 실차는 읽기 전용 기본 | O9 ✅ |
| 저가 테스트베드 | Raspberry Pi + CAN HAT(Pro-CHASER; CANLP는 Pi 3/4 + PiCAN2 Duo) | O10 📄 |
| 신호 추상화 | COVESA VSS + Eclipse KUKSA Databroker(gRPC) · Android Automotive VHAL(AIDL) | O11 🔍 |
| 엣지 LLM | B2의 Jetson/SA8295P 보드, 또는 Hailo-10H M.2(생성 AI 가속, 2.5 W) | X12 🔍 |

`분석` — 하네스 PoC는 **가상 CAN(vcan)만으로도 시작**할 수 있고, 실차 단계는 CAN FD 인터페이스 하나와 OBD-II 커넥터면 된다. 쓰기(TX)는 안전 문제라 Peykan도 기본 차단한다.

---

## 2. 칩 한눈 비교표

| 칩 / 보드 | AI 연산(정밀도) | 메모리·대역폭 | 카메라 입력 | 주 용도 | 양산 채택 예 | **연구용 입수 경로** | 근거 |
|---|---|---|---|---|---|---|---|
| NVIDIA DRIVE AGX Thor DevKit(Thor-X) | 1,000 INT8 / 2,000 FP4 TFLOPS, 350 W | 64 GB LPDDR5X, 273 GB/s | 16× GMSL2 + 2× GMSL3 | AD/ADAS 중앙 컴퓨트 | Hyperion 10(2개) | 사전주문·2025-09 출고, 가격 비공개, DRIVE 개발자 프로그램 승인 필요 | N1 N2 N3 N6 |
| NVIDIA DRIVE Thor-U(양산 변종) | 700 TOPS(Li Auto·Zeekr 공시/보도) ⚠️ 730·750 보도 혼재 | — | — | AD | Li i8/MEGA, Zeekr 9X, Lynk & Co 900 | 차량 전용 | V1 V5 V6 X16 |
| NVIDIA DRIVE AGX Orin DevKit | 254 INT8 TOPS, 200 W | 최대 200 GB/s | 16× GMSL | AD | NIO(4개), Pony 7세대(4개), Mercedes CLA | 유통사(승인 고객), SDK 프로그램 | N4 N2 N6 V7 S11 V8 |
| NVIDIA Jetson AGX Thor DevKit(T5000) | 2,070 FP4 TFLOPS(희소), 40–130 W | 128 GB LPDDR5X, 273 GB/s | HSB(QSFP) 카메라, MIPI CSI | 로보틱스·엣지(JetPack) | — | US$3,499(2025-08) → US$5,499(2026-07) | N7 N8 N9 |
| NVIDIA Jetson AGX Orin 64 GB DevKit | 275 희소 / 138 밀집 INT8 TOPS, 15–60 W | 64 GB LPDDR5, 204.8 GB/s | MIPI CSI(GMSL은 별도 보드) | 엣지·연구 | TIER IV·MIIVII 차량 PC | US$1,999 | N10 S2 |
| Qualcomm SA8295P(Cockpit Gen 4) | "최대 60 TOPS"(TechInsights) / 30 TOPS(2021 보도), 정밀도 미상 ⚠️ | — | — | 콕핏 | Lynk & Co 900, Zeekr 9X/001/007, NIO, Mercedes E-Class LWB | Lantronix/Thundercomm ADP US$6,300(퀄컴 승인, SW 미포함) | Q11 Q12 Q5 Q7 |
| Qualcomm SA8255P | NPU TOPS 비공개 ⚠️ | 6ch LPDDR5(ADP 12 GB) | — | 인포테인먼트 | Chery G700, Ford Bronco NE, Bosch 콕핏(2025) | Ride SX 4.0 ADP(SA8255P+SA8775P) US$4,999(승인) | Q6 Q18 Q13 |
| Qualcomm SA8775P(Ride Flex) | 72 TOPS NPU(Bosch 컨트롤러, 정밀도 미상) | — | — | 콕핏+ADAS 통합 | NETA, SAIC-GM Buick, Arcfox; Hyundai Mobis 개발 | 위 ADP 공용; AI Hub 지원 | Q13 Q14 Q17 Q9 |
| Qualcomm SA8650P(Ride) | 패밀리 36–100 밀집 TOPS(Momenta) | — | — | ADAS | Momenta 2024 | AI Hub "Proxy"만, 보드 비공개 | Q15 Q9 |
| Qualcomm QAM8797P(Ride Elite) | TOPS 비공개; NPU 320 TOPS(Li Auto 보도, 정밀도 미상) | — | — | 콕핏+AD | Li L9/L8(2026) | 파트너 | Q2 Q19 Q16 |
| Qualcomm QAM8397P(Cockpit Elite) | "12× AI" 주장, TOPS 비공개; 10B 온디바이스(언론) | — | — | 콕핏 | NIO·Zeekr·Li·GWM·Leapmotor·Chery 10개 프로그램 | 파트너 | Q1 Q4 O1 |
| Xpeng Turing | 750 TOPS(유효, 정밀도 미상), 30B 모델 | — | — | AD+콕핏 | G7 Ultra, P7(3개) | 차량 전용 | X1 X2 |
| Tesla HW4/AI4 | ~500 TOPS(추정 ⚠️) | 16 GB/SoC × 2 | 카메라 커넥터 12, ~5 MP | AD | Model S/3/X/Y·Cybertruck | 차량 전용 | X3 |
| Horizon Journey 6P / 6M / 6E | 560 / 128 / ~80 TOPS(정밀도 미상) | — | 6P: 18 MP 전방 | ADAS | BYD, Li i8 Pro, Chery | 공개 보드 없음(RDK S100 근접 ⚠️) | X4 X5 X6 |
| Mobileye EyeQ6 High | 34 INT8 TOPS, 7 nm | — | — | L2+ | VW 그룹(보도), Porsche | 파트너 | X7 |
| Renesas R-Car V4H | 34 TOPS | LPDDR5-6400 | 2× CSI-2 | L2+/L3 | 미확인 | White Hawk 보드(가격 미공개) | X9 |
| TI TDA4VH / TDA4VM | 32 / 8 TOPS(INT8) | — | 최대 8 카메라(VM, 애드온) | ADAS | — | SK-TDA4VM US$199 | X10 |
| Hailo-10H M.2 | 40 INT4 / 20 INT8 TOPS, 2.5 W | 4/8 GB | PCIe Gen3 x4 | 생성 AI 가속 | — | US$259.99(ASUS UGen300) | X12 |
| comma 3X / four | Snapdragon 845 | 128 GB 저장 | 3× 1080p 140 dB 내장 | L2 오픈소스 | 325+ 지원 차종 | US$999 + 하네스 US$99 | X14 |
| Huawei MDC 810 | 400+ TOPS | — | 16 카메라 | AD | Arcfox 등 | 파트너 | X13 |

---

## 3. 주변 장비 표

| 분류 | 대표 제품 | 핵심 사양 | 공개가 | 근거 |
|---|---|---|---|---|
| GMSL2 카메라 | Leopard Imaging LI-AR0233-GMSL2(2.6 MP, HDR+LFM) · e-con STURDeCAM31(3 MP, 120 dB, IP69K) · TIER IV C1/C2/C3(2.5/5.4/8.3 MP) | 양산급 센서: Sony IMX490(5.4 MP, 120–140 dB), IMX728(8.3 MP, 120 dB) | Leopard US$429–499(카메라), 키트 US$609; e-con 견적 | S15 S14 S4 S16 |
| GMSL 디시리얼라이저 | Connect Tech JCB002(Jetson AGX Orin용, 8× GMSL2) · Neousys PCIe-GL26 그래버 | DevKit 캐리어 미지원(Connect Tech 캐리어 전용) | US$519–540 | S13 S4 |
| LiDAR | Hesai AT128(128ch, 200 m@10%, 120°×25.4°, 1.5 M pts/s) · Ouster OS1-128(400 m) · RoboSense Helios 32 · Velodyne VLP-32 | — | Helios US$1,800; OS1-128 US$18,000(2019 정가) / OS1-32 US$8,000(대학 US$6,000) ⚠️ 현재가 미확인 | S17 S3 |
| 4D 레이더 | Continental ARS548 RDI(300 m, ±60°) · Arbe Phoenix(2,304 가상채널) | — | 견적 | S18 |
| GNSS/INS | Xsens MTi-680G(RTK, 2 kHz) · NovAtel PwrPak7D-E2(200 Hz INS) · SBG Ellipse-D(1 cm RTK, 0.05° 롤/피치) | — | MTi-680G £2,729 / €3,212–3,275; NovAtel·SBG 견적 | S19 S5 |
| DBW | Dataspeed(MKZ·Fusion·Mondeo) · AStuff PACMod(GEM·RX-450h·CR-V) | ROS 2 드라이버 공개 | 견적 | S20 |
| CAN / 이더넷 | PCAN-USB FD · Kvaser Leaf v3 · Intrepid RAD-Moon 2 · MACH T1 컨버터 | CAN FD 8 Mbit/s; 100/1000BASE-T1 | US$347–407; €400–410 | S21 S22 |
| 무선 | Quectel RM520N-GL 5G(Jetson Orin용 캐리어 번들) | 5G NSA/SA + GNSS | US$276–327 | S25 |
| 전원 | 400 W급 12 V DC-DC(Vicor) · Jetson Thor 240 W USB-C PSU 동봉 | — | Vicor US$460 | S27 S23 |
| 계측 | Jetson INA3221 + jtop(레일별 전력) | 무료 | — | S26 |

---

## 4. 연구용 구매 조합 (3단계, 공개 표시가 기준)

| 단계 | 구성 | 공개가(조사일) | 어떤 연구를 덮나 | 근거 사례 |
|---|---|---|---|---|
| **A. 벤치 최소** | 24 GB+ dGPU 워크스테이션(RTX 4090 24 GB MSRP US$1,599 / RTX 5090 32 GB MSRP US$1,999) + **Jetson AGX Orin 64 GB**(US$1,999) + USB/GigE 카메라 1~2 + PCAN-USB FD(US$347~) + 가상 CAN(무료) | GPU US$1,599–1,999 + Orin US$1,999 + CAN US$347 | A1 벤치(Alpamayo·Qwen-Drive 추론·SFT 소규모), B2(FP16/INT8/INT4 프로파일링), B4(가상 CAN 하네스) | M1 M7 N10 N12 O9 P3 |
| **B. 양 갈래 공용(실차 PoC 가능)** | 호스트 GPU: RTX PRO 6000 96 GB(US$8,435~, 시세 변동) 또는 DGX Spark 128 GB(US$4,699~6,950) + **Jetson AGX Thor DevKit**(US$3,499~5,499) + GMSL2 카메라 세트(Leopard US$429×4 + 디시리얼라이저 US$540, Connect Tech 캐리어 필요) + Kvaser Leaf v3(US$349~407) + 5G 모듈(US$276~327) + **comma 3X/four**(US$999 + US$99) + (선택) Lantronix SA8295P ADP US$6,300(승인) | 약 US$20,000 내외(ADP 제외) | A1 엣지(NVFP4·EAGLE3), A3(comma 실차 E2E), B1(8295 재현은 ADP 추가 시), B2 세대 비교, B3 엣지↔호스트, B4 실차 CAN | N7 N9 P1 P2 S15 S13 S21 S25 X14 Q5 |
| **C. 실차 확장** | DRIVE AGX Thor DevKit SKU 12(가격 비공개·프로그램 승인) 또는 Neousys Nuvo-10108GC급 x86 차량 PC + RTX GPU + GMSL/GigE 카메라 6~8 + LiDAR 1(RoboSense Helios US$1,800 ~ Hesai AT128 견적) + GNSS/INS(Xsens MTi-680G €3,200대) + DBW(Dataspeed/PACMod 견적) + 400 W DC-DC + T1 컨버터(€400) | 대부분 견적 | A2 데이터 수집·인식, A1 실차 폐루프, A4 통합 | N1 N6 S8 S17 S19 S20 S22 S27 |

`분석` — A단계만으로 공개 VLA 모델 추론과 온디바이스 프로파일링·하네스 PoC가 모두 가능하다. B단계의 핵심 추가는 Jetson AGX Thor(정밀도·메모리)와 comma 3X(실차 E2E를 가장 싸게)이며, 퀄컴 재현이 꼭 필요할 때만 ADP를 더한다. C단계는 차량·DBW·LiDAR가 비용의 대부분이고 대학 사례처럼 x86 PC가 현실적이다.

---

## 5. 미확인·주의 사항

- **퀄컴 TOPS 비공개**: SA8255P·QAM8397P·QAM8797P의 NPU TOPS는 퀄컴 공식 자료에 없다. SA8295P는 30 TOPS(2021) vs 60 TOPS(2025 티어다운) 충돌, 8797 "320 TOPS"·8397 "10B 온디바이스"는 언론 수치다 ⚠️ [Q11][Q19][O1].
- **Thor-U TOPS 충돌**: 700(Li Auto 공시·Zeekr) / 730(ResearchInChina) / 750(36Kr) ⚠️ [V1][X16][V6]. NVIDIA 공식 자료는 Thor-X(1,000 INT8 / 2,000 FP4)만 명시한다 [N3].
- **Jetson Thor ≠ DRIVE Thor**: 같은 실리콘이지만 메모리(128 vs 64 GB)·카메라(HSB vs GMSL)·SDK(JetPack vs DriveOS)·입수 경로가 다르다 [N7][N1].
- **INT8/FP4/희소 TOPS는 직접 비교 불가**: Jetson Thor 2,070은 FP4 희소, Orin 275는 INT8 희소(138 밀집)다 [N7][N10].
- **Qwen-Drive 엣지 배포 사례 없음**: README·논문 모두 GPU 24 GB 권장만 있고 차량 SoC 배포·지연 수치는 없다 [M7].
- **Alpamayo 라이선스·배포**: 1.5는 OpenMDW-1.1, R1은 비상업 표기 보도 ⚠️; README는 "차량 등급 검증 미완"을 명시한다 [M1][M2].
- **가격 변동**: Jetson AGX Thor(US$3,499→5,499)·DGX Spark(US$3,999→6,950)·RTX PRO 6000(US$8,435→13,250 표시 사례)은 2025–2026 사이 크게 올랐다 [N9][P2][P1].
- **직접 열람 못 한 페이지**: 퀄컴·Lantronix·NVIDIA 제품 페이지 등은 검색 발췌 기준이다(헤더 참조).

## 6. 용어

| 용어 | 뜻 |
|---|---|
| VLA | Vision-Language-Action. 카메라 입력을 언어 모델 백본으로 처리해 궤적·행동을 내는 모델 |
| GMSL2/3 | Gigabit Multimedia Serial Link. 동축 케이블로 양산 차량 카메라를 연결하는 직렬 링크(Analog Devices). 보드 쪽에 디시리얼라이저 필요 |
| HSB | Holoscan Sensor Bridge. Jetson Thor가 QSFP로 카메라를 받는 NVIDIA 방식 |
| ADP | Automotive Development Platform. 퀄컴 차량 SoC 레퍼런스 보드 |
| DBW | Drive-by-Wire. 조향·제동·가속을 전자 신호로 제어하는 키트 |
| NVFP4 / EAGLE3 | Blackwell 세대 4-bit 부동소수점 / 투기 디코딩 기법. TensorRT-Edge-LLM에서 Thor·DGX Spark만 지원 |
| 100/1000BASE-T1 | 단일 꼬임선 자동차 이더넷. 일반 RJ45와 연결하려면 미디어 컨버터 필요 |
| SKU 10 / SKU 12 | DRIVE AGX Thor DevKit의 벤치용(AC 전원) / 차량 탑재용(DC 전원·하네스) 구성 |
