# [메일용] 차량용 AI 연구 장비 조사 — 결과

> 작성일 2026-10-14. 외부 공개 자료만으로 조사했습니다(저장소 기존 문서 미참고). 등급: 🔍 공식 / 📄 논문 / 📰 언론·2차 / 💬 포럼 / ⚠️ 미확인·충돌 / 💡 사례에 없는 제안. 괄호 안 ID는 맨 아래 출처 목록과 저장소의 [전체 출처 118건](reference/references.md)에 대응합니다. 가격은 조사일 공개 표시가입니다.

---

## 1. 자율주행 연구별 하드웨어

### 1-1. E2E/VLA 주행 모델

**사례**
- 공개 모델: NVIDIA **Alpamayo 1.5-10B**(백본 8.2B + 액션 전문가 2.3B, 카메라 4대 × 4프레임 입력, 6.4 s 궤적 출력) [M1][M2] 🔍, Alibaba **Qwen-Drive-1.0-4B**(Qwen3.5-4B + BEV 인식 헤드 + 플래닝 전문가, NAVSIM PDMS 90.7) [M7] 🔍.
- 논문 실차: **DriveVLM**은 Orin-X 2개를 "1번=고주파 E2E, 2번=VLM"으로 나눠 탑재, VLM 평균 410 ms [M8] 📄.
- 양산: **Li Auto i8**은 Max/Ultra에 Thor-U 1개(700 TOPS)로 VLA 배포 [V1] 🔍, **Xpeng G7 Ultra**는 자체 Turing 칩 3개(2개 VLA, 1개 콕핏) [X2] 📰. 국내 학계는 **UNIST**가 HMG 2025 E2E 챌린지에서 Jetson AGX Orin 16 Hz로 1위 [M9] 📄.

**하드웨어 — 연구와 양산 흐름이 나뉜다**
- 연구(공개 모델 실행·SFT): 두 모델 모두 공식 요구가 **"24 GB 이상 GPU"**(RTX 3090/4090, A5000, H100 예시) [M1][M7] 🔍. 워크스테이션이 1차 장비.
- 양산(차량 SoC): Orin-X 2개 → Thor-U 1개 또는 자체 칩으로 이동 중 [V2] 📰.

| 칩 | AI 연산 | 메모리·대역폭 | 정밀도 | 비고 | 출처 |
|---|---|---|---|---|---|
| NVIDIA Orin-X (DRIVE AGX Orin) | 254 INT8 TOPS | 최대 200 GB/s | FP16/INT8/INT4 (FP8·FP4 불가) | 양산 주류(2025 Q1 중국 ADAS SoC 51.8%) | N4 N11 X18 |
| Orin-X × 2 | 508 INT8 TOPS | 메모리 풀 2개(모델 분할 필요) | 동일 | NIO·Xpeng Max·Li AD Max(구) | X2 V7 |
| NVIDIA Thor-U (양산) | 700 TOPS(정밀도 미상 ⚠️) | — | Blackwell(FP8·NVFP4) | Li i8/MEGA, Zeekr 9X | V1 V6 |
| NVIDIA Thor-X (DRIVE AGX Thor DevKit) | 1,000 INT8 / 2,000 FP4 TFLOPS, 350 W | 64 GB, 273 GB/s | FP8·NVFP4 | 가격 비공개, 개발자 프로그램 승인 | N1 N3 N6 |

요약: Orin-X 2개는 연산량으로 Thor-U의 약 7할, Thor-X의 절반이고, VLA처럼 FP8/FP4와 단일 대용량 메모리가 중요한 작업은 Thor 쪽이 수치 이상으로 유리합니다.

### 1-2. 인식·데이터 수집

**사례**
- **Univ. at Buffalo** Autoware 테스트베드(IEEE IV 2026): Lincoln MKZ + Dataspeed DBW + Velodyne VLP-32 + NovAtel OEM7 + Neousys Nuvo-10108GC(350 W급 RTX 1장 탑재 x86) [S8] 📄.
- **TUM EDGAR**(VW T7): 카메라 8 + 스테레오 2, LiDAR 5, 레이더 6, NovAtel GNSS/IMU, 차량 PC + RTX A6000 [S9] 📄.
- **KIT CoCar NextGen**(Audi A6): LiDAR 12, 카메라 9, 4D 레이더 3, 서버급 다중 GPU [S10] 📄.
- 레퍼런스·로보택시: NVIDIA Hyperion 10은 카메라 14·레이더 9·LiDAR 1·초음파 12 + Thor 2개 [N15] 🔍, Pony.ai 7세대는 LiDAR 9(주 LiDAR Hesai AT128 ×4)·카메라 14 + Orin-X 4개 [S11] 📰.

**하드웨어 — 서버급이 많다는 점이 특징**
- 컴퓨트: 대학 연구차량은 예외 없이 **x86 차량 PC + 데스크톱 GPU**(RTX A6000·4080급). Autoware 레퍼런스 카탈로그도 Neousys·ADLINK·Advantech x86 PC가 중심이고 Jetson Orin/Thor 기반은 일부(MIIVII·ADLINK) [S2] 🔍.
- 센서: 카메라 6~8(GMSL2 또는 GigE; TIER IV C1/C2/C3, FLIR, Lucid), LiDAR 1~2(Hesai AT128 200 m·120°, Ouster OS1, RoboSense Helios US$1,800), 4D 레이더(Continental ARS548), GNSS/INS(Xsens MTi-680G £2,729, NovAtel PwrPak7, SBG Ellipse-D) [S3][S4][S17][S19] 🔍📰.
- 차량 신호·제어: **DBW 키트**(Dataspeed: MKZ·Fusion·Mondeo / AStuff PACMod: Polaris GEM·Lexus RX-450h·Honda CR-V) [S20] 🔍, CAN FD 어댑터(PCAN-USB FD US$347~379, Kvaser Leaf v3 US$349~407) [S21] 🔍, PTP 시간동기·10 GbE.

### 1-3. 엣지 배포·지연 최적화

**사례**
- NVIDIA **TensorRT-Edge-LLM** VLA 예제: Alpamayo 내보내기는 **FP16만 지원**, Thor에서 엔진 빌드 [M4] 🔍. 포럼에서는 DRIVE AGX Thor(DriveOS 7.2.5)에서 FP16 엔진 ~15 GB 할당 OOM 보고 [M5] 💬.
- **FlashDrive** 논문: VLA 추론 4.7× 가속(151 ms, 1.4→6.6 Hz), Jetson Thor에서 4.0×, W4A8 양자화 [M16] 📄.
- Orin vs Thor 특성화: 지연의 최대 75%가 메모리 바운드 액션 생성 단계 [M17] 📄. 비동기 fast-slow VLA(5 Hz 추론/20 Hz 제어) [M19] 📄.

**하드웨어**

| 보드 | 메모리 | 정밀도·SW | 카메라 입력 | 가격·입수 | 출처 |
|---|---|---|---|---|---|
| Jetson AGX Thor DevKit (T5000) | 128 GB LPDDR5X, 273 GB/s | FP8·NVFP4·EAGLE3, JetPack 7 | HSB(QSFP), MIPI CSI | US$3,499(2025-08) → US$5,499(2026-07) | N7 N9 N11 |
| Jetson AGX Orin 64 GB DevKit | 64 GB, 204.8 GB/s | FP16/INT8/INT4만, JetPack | MIPI CSI(GMSL은 별도 보드) | US$1,999 | N10 N11 |
| DRIVE AGX Thor DevKit (SKU 10 벤치 / SKU 12 차량) | 64 GB, 273 GB/s | DriveOS 7, ASIL-D | 16× GMSL2 + 2× GMSL3 내장 | 가격 비공개, 사전주문·프로그램 승인 | N1 N2 N6 |

벤치: Thor에서 Qwen2.5-VL-7B NVFP4 61 tok/s(EAGLE3 177), Orin 64 GB INT4 64 tok/s [N12] 🔍. Jetson Thor와 DRIVE Thor는 같은 실리콘이지만 메모리·카메라 인터페이스·SDK·구매 경로가 다른 별개 제품입니다.

---

## 2. 자율주행 — 시뮬레이터 / 실차 탑재 상황별 하드웨어

### 2-1. 시뮬레이터·녹화 데이터로 진행할 때

- **학습·추론 서버**: GPU ≥24 GB 1장(RTX 4090 24 GB MSRP US$1,599 / RTX 5090 32 GB US$1,999)으로 공개 VLA 추론·소규모 SFT 가능 [M1][M7][P3]. 대규모 SFT·RL은 RTX PRO 6000(96 GB, 1,792 GB/s, US$8,435~) 또는 DGX Spark(128 GB, 273 GB/s, US$4,699~6,950) [P1][P2]. LMSYS 벤치에서 디코딩은 RTX PRO 6000이 DGX Spark의 약 4배 [M11] 📰.
- **시뮬레이터·벤치마크**: Bench2Drive(CARLA, 220 루트·44 시나리오, 2M 프레임) [M13] 📄, NAVSIM v2(로그 재생, 안전 인지 개루프) [M14] 📄, MORAI(HMG 챌린지) [M9]. 2026년 교차 연구는 ADE/FDE 같은 개루프 지표가 폐루프 주행 점수와 상관이 없다고 보고 [M14] 📄. 월드모델(NVIDIA Cosmos, Wayve GAIA-2)은 데이터센터급 GPU 영역 [M15] 🔍📰.
- **엣지 배포 검증 보드 1대**: Jetson AGX Thor(FP8/NVFP4) 또는 Orin 64 GB(INT4까지) + 녹화 데이터 재생 + jtop 전력 계측 [N11][S26].

### 2-2. 실차에 탑재해 주행할 때 (VLA 기준)

| 항목 | 구성 | 공개가 | 출처 |
|---|---|---|---|
| 카메라·센서 | GMSL2 카메라 4~7대(Alpamayo 기본 4: 좌·전방광각·우 120° + 전방망원 30°), HDR 120 dB+ (Leopard LI-AR0233 US$429~499, e-con STURDeCAM 견적, 양산 센서 Sony IMX490/IMX728) | US$429~/대 | M3 S15 S14 S16 |
| 인터페이스 | GMSL 디시리얼라이저(Connect Tech JCB002, Jetson용 8ch, US$540; DRIVE Thor는 내장) · CAN FD 어댑터(PCAN/Kvaser US$347~407) · DBW 키트(Dataspeed·PACMod, 견적) · 100/1000BASE-T1 변환기(€400, 양산 ECU 연결 시) | US$540 / US$347~407 / 견적 / €400 | S13 S21 S20 S22 |
| 전원 | 12 V → 보드 DC-DC. DRIVE AGX Thor TDP 350 W(입력 9–16 V, SKU 12 차량 직결) · Jetson AGX Thor 40–130 W(28 V 5 A, 240 W USB-C PSU 동봉) · 400 W급 DC-DC(Vicor US$460) | — | N3 S23 S27 |
| 기타 | 마운트·냉각, GNSS 안테나 2개(이중 안테나 INS), 5G 모듈(Quectel RM520N-GL US$276~327), 전력계·온도 로거, 대용량 NVMe | — | S25 S26 |
| 가장 싼 실차 E2E | **comma 3X/four**(Snapdragon 845, 3× 1080p 140 dB 카메라·LTE·CAN FD 내장, 325+ 차종 하네스) | US$999 + 하네스 US$99 | X14 |

---

## 3. 온디바이스 AI 연구별 하드웨어

### 3-1. 콕핏 어시스턴트 SLM/VLM

**사례**
- Cerence **CaLLM Edge**: Phi-3 3.8B, 4-bit, 헤드유닛 임베디드 [O6] 🔍. Visteon: Snapdragon Cockpit Elite 위에 **Qwen 7B**를 QNN으로 양자화해 Hexagon NPU 실행(CES 2026) [O2] 🔍. Banma AutoOmni 2.0: 23B-A3B MoE, 8397 대상 [O4] 📰. Xpeng×Banma: Turing 칩(750 TOPS)에 30B급 로컬, "온디바이스 우선·클라우드 보조" [O3] 📰. FEV×Microsoft: Phi-4-mini on DRIVE AGX 오프라인 음성 [O7] 🔍.
- 양산 콕핏 SoC: Lynk & Co 900·Zeekr 9X가 **SA8295P 2개**(각 "최대 60 TOPS", 2021 보도는 30 TOPS ⚠️) [Q11][V5] 📰, Li Auto 신형 콕핏은 **8797 Elite**(NPU 320 TOPS, 정밀도 미상) [Q19] 📰.

**하드웨어**
- 연구 보드: Jetson AGX Orin 64 GB(3~8B INT4) 또는 Jetson AGX Thor(7~30B NVFP4) [N10][N7].
- 💡 제안: 양산과 같은 칩으로 하려면 **Lantronix SA8295P ADP**(US$6,300) 또는 **SA8255P/SA8775P Ride SX ADP**(US$4,999) + Qualcomm AI Hub/QNN. AI Hub가 8295/8775 ADP를 공식 타깃으로 지원하고 Llama 3.2 1B(w4) 11 tok/s 수치 공개 [Q5][Q6][Q9][Q10] 🔍. 단 퀄컴 승인·소프트웨어 자체 빌드 필요, NPU TOPS 비공개 [Q7] 🔍.
- 부자재: 마이크 어레이·스피커, 디스플레이, 실내 IR 카메라(운전자 모니터링 겸용), LTE/5G 모듈, 12 V DC-DC, CAN FD(차량 상태 수신). 이 부자재의 공개가는 별도 조사하지 않았습니다 ⚠️.

### 3-2. 엣지 LLM/VLM 최적화

**사례**
- TensorRT-Edge-LLM 공식 벤치: Thor Qwen2.5-VL-7B NVFP4 61 tok/s(EAGLE3 투기 디코딩 177), Llama-3.1-8B NVFP4 54.9(EAGLE3 189); Orin 64 GB Qwen2.5-VL-7B INT4 64 tok/s; DGX Spark 55.6 [N12] 🔍. vLLM 기준 Thor Llama 3.1 8B 41.3 tok/s(동시 1) [N13] 🔍.
- 논문: Jetson Orin AGX에서 2.7B–32.8B LLM을 전력 모드별로 측정 [M10] 📄. Qualcomm AI Hub: SA8295P ADP Llama 3.2 1B 11 tok/s [Q10] 🔍.

**하드웨어**
- 세대 기준선 Orin 64 GB(FP16/INT8/INT4) + Thor(FP8/NVFP4·EAGLE3) + 비교군 호스트 GPU. 전력은 Jetson 내장 INA3221 레일 + jtop [S26] 💬📰.
- 💡 제안: SA8295P ADP를 세 번째 비교군으로 두면 "GPU(Jetson) vs NPU(Hexagon)" 정밀도·전력 비교가 가능. 공개 수치가 거의 없어 측정 자체가 기여.

### 3-3. 엣지 ↔ 클라우드 하이브리드

**사례**
- Li Auto Mind GPT-3o: 추론을 엣지 NPU와 클라우드 GPT로 분할 [O5] 📰. Cerence xUI: DRIVE AGX Orin 온보드 + 클라우드 [O6] 🔍. FEV: 온보드 SLM이 클라우드 폴백 [O7] 🔍. AWS 인-비히클 어시스턴트 가이드: 온보드 SLM + 클라우드 LLM 시맨틱 라우팅, OTA 재학습 [M12] 🔍. 엣지-클라우드 투기 디코딩(TMLR 2025): 지연 최대 35% 감소, 로봇 실험 [M12] 📄. NVIDIA 인캐빈 레퍼런스: 온보드 ASR+TTS+LLM + 클라우드 오케스트레이터 [N16] 🔍.
- 차량 하드웨어를 명시한 실측 논문은 찾지 못했습니다 ⚠️.

**하드웨어**
- 엣지 보드(Orin/Thor) + 호스트 GPU(RTX PRO 6000 96 GB / DGX Spark 128 GB) + 벤치는 유선 10 GbE, 실차는 5G 모듈(Quectel RM520N-GL US$276~327) + 네트워크 지연 주입 도구 [P1][P2][S25].

### 3-4. 에이전트·툴 사용(차량 데이터)

**사례**
- **Peykan 0.2.1**(2026-10-07): MCP 서버로 CAN·OBD-II·UDS·J1939를 LLM에 노출, 가상 CAN + ECU 시뮬레이터 내장, cantools DBC 디코딩, SocketCAN/PCAN/Kvaser/Vector 지원, 실차는 읽기 전용 기본 [O9] 🔍.
- 신호 추상화: Eclipse KUKSA Databroker(COVESA VSS, gRPC), Android Automotive VHAL [O11] 🔍. 저가 테스트베드: Raspberry Pi + CAN HAT(Pro-CHASER, CANLP) [O10] 📄. 차량 내 LLM 실측: AI-CDA4All, LLaMA 3.2 on AGX Orin 응답 5.07 s [M10] 📄.
- "온디바이스 SLM + CAN 툴 사용"을 묶은 2025 논문은 없음 ⚠️.

**하드웨어 — CAN 접근이 특징**
- 벤치: 엣지 LLM 보드 + 가상 CAN(SocketCAN vcan) + Peykan. 실차: CAN FD 어댑터(US$347~407) + OBD-II 커넥터, 또는 Raspberry Pi + PiCAN2(€45) [S21][S24] 🔍. 쓰기(TX)는 안전상 차단이 기본.

### 3-5. AD와 컴퓨트 공유·통합

**사례**
- NIO 2024: 콕핏 8295 1개 + Orin-X 4개(1,016 TOPS) 중 최대 256 TOPS를 NOMI GPT 온디바이스 모델에 공유 [V7] 📰. MediaTek Dimensity Auto C-X1(NVIDIA GPU 내장) + DRIVE AGX Thor를 DriveOS로 묶어 자원 공유 [X18] 🔍. Qualcomm Ride Flex SA8775P: 콕핏+ADAS 단일 SoC(Hyundai Mobis·Bosch 적용) [Q14][Q13] 🔍📰.
- 연구실 재현 사례는 없음 ⚠️.

**하드웨어**
- 💡 제안: 1단계는 Jetson Thor 1대에서 프로세스/MIG 분리로 "AD 여유 연산을 콕핏 모델에" 실험, 2단계는 Jetson(AD 역할) + 퀄컴 ADP(콕핏 역할) 2보드를 10 GbE/T1 컨버터(€400)로 연결 [S22].

---

## 핵심 출처 (전체 118건은 reference/references.md)

- N1 DRIVE AGX Thor DevKit 블로그 https://developer.nvidia.com/blog/accelerate-autonomous-vehicle-development-with-the-nvidia-drive-agx-thor-developer-kit/
- N3 DRIVE AGX Thor 플랫폼 PDF https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf
- N4 DRIVE AGX Orin 플랫폼 PDF https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-orin-platform-for-developers.pdf
- N7/N9 Jetson Thor 출시·가격 https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics · https://videocardz.com/newz/nvidia-raises-jetson-prices-by-up-to-101-agx-thor-now-costs-5499
- N11/N12 TensorRT-Edge-LLM 지원 매트릭스·벤치 https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/getting_started/support-matrix.html · https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/performance/performance-benchmarks.html
- M1 Alpamayo README https://github.com/NVlabs/alpamayo · M7 Qwen-Drive README https://github.com/QwenLM/Qwen-Drive-1.0 · M8 DriveVLM https://arxiv.org/abs/2402.12289v5 · M16 FlashDrive https://arxiv.org/abs/2608.12932
- V1 Li Auto i8 (Thor-U 700 TOPS) https://www.sec.gov/Archives/edgar/data/1791706/000110465925071734/tm2521968d1_ex99-1.htm · X2 Xpeng G7 https://cnevpost.com/2025/06/11/xpeng-debuts-g7-suv/
- S2–S7 Autoware 레퍼런스 HW https://docs.autoware.org/main/reference-design/reference-hw/ · S8 UB IV 2026 https://www.acsu.buffalo.edu/~chaozheh/Papers/2026_IV_Meka_Gutha_Krozelius_He_Sadek_Qiao.pdf · S9 TUM EDGAR https://arxiv.org/pdf/2309.15492
- Q5/Q6 Lantronix ADP 가격 https://estore.lantronix.com/products/sa8295p-automotive-development-platform · https://lantronix.com/products/ride-sx-4-0-automotive-development-platform · Q9/Q10 Qualcomm AI Hub https://aihub.qualcomm.com/automotive/models/ffnet_78s · https://aihub.qualcomm.com/models/llama_v3_2_1b_instruct
- O2 Visteon Qwen 7B https://www.nasdaq.com/press-release/visteon-showcases-production-ready-high-performance-compute-solution-snapdragonr · O6 Cerence https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive · O9 Peykan https://pypi.org/project/peykan/ · V7 NIO https://autonews.gasgoo.com/articles/news/nio-begins-pre-sale-for-2024-vehicle-models-70031474
