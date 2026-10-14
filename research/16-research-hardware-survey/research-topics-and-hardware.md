# 차량용 AI — 무엇을 연구할 것인가, 그 연구에 무엇이 필요한가

> **작성일**: 2026-10-14 · **상태**: 2판(연구 후보 → 장비). 1판 [장비 카탈로그](research-hardware-survey.md)는 칩·주변장비 스펙과 가격의 상세 표로 함께 쓴다.
> **목적**: ① 차량에서 지금 진행되는 AI 연구를 a) 자율주행 / b) 온디바이스 AI로 나눠 **사례 → 카테고리**로 정리하고, ② 각 카테고리의 연구(또는 그것을 변형한 연구)에 **필요한 하드웨어·부자재 조합**을 제시한다. 자율주행은 **(i) 시뮬레이터·녹화 데이터**와 **(ii) 실차 탑재·주행 테스트** 두 갈래로 나눈다.
> **조사 범위**: 이 저장소의 기존 문서는 참고하지 않았다. 외부 공개 자료만 썼다.
> **표기**: 사실 문장마다 출처 ID와 등급 — 🔍 공식 / 📄 논문 / 📰 언론·2차 / 💬 포럼 / ⚠️ 미확인·충돌. **💡 제안** = 조사된 사례에는 없지만 실제 차량 적용을 감안해 우리가 제안하는 구성(출처 없음, 판단). TOPS는 정밀도 병기, 가격은 조사일 공개 표시가. 출처 목록은 [reference/references.md](reference/references.md). 조사 환경 제약(GitHub·PyPI만 직접 열람, 나머지는 검색 발췌)은 1판 헤더와 같다.

---

## 결론 먼저 — 연구 후보 6개와 장비 세트

| # | 연구 후보 | 왜 이 연구인가(사례의 빈틈) | 장비 세트 | 근거 |
|---|---|---|---|---|
| R1 | **공개 VLA(Qwen-Drive 4B·Alpamayo 10B)를 차량 SoC에 올리는 양자화·지연 연구** | 두 모델 다 공식 요구가 "24 GB GPU"뿐, 차량 SoC 배포 수치 없음. Alpamayo 엣지 내보내기는 FP16만 지원, Thor에서 OOM 포럼 사례. FlashDrive는 Thor에서 4.0× 가속·W4A8로 가능성 제시 | 벤치: 24 GB+ dGPU → 엣지: Jetson AGX Thor(128 GB, NVFP4) · Orin 64 GB(INT4) | M1 M7 M4 M5 M16 |
| R2 | **시뮬·녹화 데이터 기반 E2E 평가 파이프라인(개루프↔폐루프 상관)** | 개루프 ADE/FDE는 폐루프 주행 점수와 상관이 없다는 2026 교차 연구; NAVSIM v2·Bench2Drive가 새 표준 | 워크스테이션 GPU 1~2장 + NAVSIM/Bench2Drive/MORAI | M13 M14 M9 |
| R3 | **콕핏 SLM/VLM을 실제 차량 콕핏 SoC(퀄컴 NPU)에 올리는 연구** 💡 | 양산 콕핏은 퀄컴 8295(2개)가 주류이고 Visteon은 Cockpit Elite NPU에 Qwen 7B를 올렸지만, 공개 연구는 거의 Jetson 위주 | Lantronix SA8295P/SA8775P ADP(US$4,999–6,300, 승인) + Qualcomm AI Hub/QNN · 비교군 Jetson Orin 64 GB | Q5 Q6 Q9 Q10 O2 |
| R4 | **엣지↔클라우드 분할 추론(투기 디코딩·시맨틱 라우팅)의 차량 실측** | 업계는 하이브리드(Li Mind GPT-3o, Cerence, FEV, AWS 가이드)로 가는데 차량 하드웨어를 명시한 실측 논문은 못 찾음 | 엣지 보드 + 호스트 GPU(RTX PRO 6000/DGX Spark) + 5G 모듈 | O5 O6 O7 M12 |
| R5 | **온디바이스 SLM + 차량 버스(CAN/VSS) 툴 사용 에이전트 하네스** | MCP-CAN 서버(Peykan)·KUKSA 같은 부품은 있으나 둘을 묶은 2025 논문은 없음 | 엣지 LLM 보드 + 가상 CAN → CAN FD 인터페이스 + OBD-II | O9 O11 S21 |
| R6 | **콕핏+AD 도메인 간 컴퓨트 공유 실험** 💡 | NIO는 4× Orin-X 중 256 TOPS를 콕핏 모델에 공유, MediaTek은 콕핏 SoC와 DRIVE AGX를 DriveOS로 묶음 — 연구실 재현 사례 없음 | Jetson(AD 역할) + 퀄컴 ADP(콕핏 역할) 2보드 + 10 GbE/T1 | V7 X18 Q14 |

---

## Part A. 자율주행

### A-1. 지금 진행되는 연구 — 사례와 카테고리

| 카테고리 | 연구 내용 | 대표 사례 | 사례가 쓴 하드웨어 | 근거 |
|---|---|---|---|---|
| **A1 E2E/VLA 주행 모델** | 멀티카메라 → VLM 백본 → 궤적(+추론 텍스트) | Alpamayo 1.5-10B(4 cam × 4 frame, 6.4 s 궤적) · Qwen-Drive-1.0-4B(BEV 헤드 + 플래닝 전문가, NAVSIM PDMS 90.7) · DriveVLM(실차 2× Orin-X, 410 ms) · Li i8(Thor-U 700 TOPS에 VLA) · Xpeng G7 Ultra(3× Turing, 2개 VLA) · UNIST(HMG 2025 챌린지 1위, Orin 16 Hz) | 연구: GPU ≥24 GB · 양산: Orin-X 2개 → Thor-U/Turing 단일 칩 | M1 M3 M7 M8 V1 X2 M9 |
| **A2 인식·데이터 수집** | BEV/3D 검출·점유, 멀티센서 동기 수집 | Qwen-Drive BEV 헤드(nuScenes·OpenScene) · UB Autoware 테스트베드 · TUM EDGAR(8 cam·5 LiDAR·6 radar) · KIT CoCar NextGen(12 LiDAR·9 cam) · Hyperion 10(14 cam·9 radar·1 LiDAR) · Pony 7세대(4× Orin-X, AT128 ×4) | 연구차량: x86 PC + RTX A6000/4080급 + GMSL/GigE 카메라 + LiDAR + GNSS/INS + DBW | M7 S8 S9 S10 N15 S11 |
| **A3 폐루프 평가·시뮬·월드모델** | 시뮬레이터 폐루프 점수, 개루프 지표의 타당성, 생성형 월드모델로 시나리오 생성 | Bench2Drive(CARLA, 220 루트·44 시나리오) · NAVSIM v2 안전 인지 개루프 지표 vs 폐루프 교차 연구(2026) · HMG 챌린지(MORAI) · NVIDIA Cosmos(2025-01, 데이터센터 GPU 최적화) · Wayve GAIA-2(5 카메라 비디오 생성) | 워크스테이션/서버 GPU; 월드모델 학습은 데이터센터급 | M13 M14 M9 M15 |
| **A4 엣지 배포·지연 최적화** | 양자화·투기 디코딩·커널로 차량 SoC에서 Hz 확보 | TensorRT-Edge-LLM VLA 예제(FP16만, Thor 빌드) · Thor OOM 포럼 · FlashDrive(4.7× 가속, 1.4→6.6 Hz, Jetson Thor 4.0×, W4A8) · Orin vs Thor 특성화(지연의 75%가 메모리 바운드 액션 생성) · 비동기 fast-slow VLA(5 Hz 추론/20 Hz 제어) | Jetson AGX Thor / Orin, DRIVE AGX Thor | M4 M5 M16 M17 M19 |
| **A5 저전력 양산급 ADAS** | 수십 TOPS SoC에서 L2/L2+ 스택 | Horizon J6E/M/P(BYD·Li i8 Pro) · EyeQ6H 34 INT8 TOPS · R-Car V4H 34 TOPS · TDA4VH 32 TOPS · comma openpilot(Snapdragon 845, tinygrad) | 양산 SoC(파트너) / 공개 보드: SK-TDA4VM US$199, comma 3X US$999 | X4 X7 X9 X10 X14 X15 |

`분석` — 연구 사례의 무게중심은 A1·A4(VLA를 어떻게 차량 SoC에 올리나)와 A3(평가의 타당성)에 있다. A2는 연구차량을 가진 대학의 인프라형 연구이고, A5는 산업 쪽이라 연구실 진입점이 좁다.

### A-2. 연구별 필요 하드웨어·부자재

#### (i) 시뮬레이터·녹화 데이터로 진행할 때

| 카테고리 | 컴퓨트 | 데이터·시뮬레이터 | 부자재 | 공개가 | 근거 |
|---|---|---|---|---|---|
| A1 VLA 추론·SFT | GPU ≥24 GB 1장(RTX 4090 24 GB / 5090 32 GB), 대규모 SFT·RL은 RTX PRO 6000 96 GB 또는 DGX Spark 128 GB | nuScenes·NAVSIM·Waymo E2E·NVIDIA PhysicalAI AV(Alpamayo 로더 내장) | NVMe 2 TB+(Alpamayo 가중치 22 GB, 데이터셋 수백 GB) | GPU US$1,599–1,999 / PRO 6000 US$8,435~ / Spark US$4,699~6,950 | M1 M7 P1 P2 P3 |
| A2 인식 학습 | 위와 동일; BEV 학습은 멀티 GPU 유리 | nuScenes·OpenScene | — | — | M7 |
| A3 폐루프 평가 | CARLA/Bench2Drive·MORAI는 GPU 워크스테이션 1대로 가능; NAVSIM은 로그 재생 | Bench2Drive(2M 프레임), NAVSIM v2, MORAI(HMG 챌린지) | — | 소프트웨어 무료(MORAI 라이선스 ⚠️ 미확인) | M13 M14 M9 |
| A4 엣지 배포 | **엣지 보드 1대**: Jetson AGX Thor(128 GB, FP8/NVFP4, EAGLE3) 또는 Jetson AGX Orin 64 GB(FP16/INT8/INT4만) + 내보내기용 x86 호스트 | 녹화 데이터 재생(ROS bag / 데이터셋) | 240 W USB-C PSU(Thor 동봉), NVMe, jtop 전력 계측 | Thor US$3,499→5,499 / Orin US$1,999 | N7 N9 N10 N11 S23 S26 |
| A5 양산급 | TI SK-TDA4VM(8 TOPS) · Hailo-10H M.2(20 INT8 TOPS, x86에 장착) · comma 3X(벤치에서도 openpilot 실행 가능) | 녹화 데이터 | — | US$199 / US$260 / US$999 | X10 X12 X14 |
| 💡 제안 | **Qualcomm SA8775P(Ride Flex) ADP**에 인식 모델을 QNN으로 올려 "콕핏+ADAS 통합 SoC"에서의 NPU 배포를 벤치에서 먼저 검증. AI Hub가 SA8775P ADP를 공식 타깃으로 지원하므로 모델 변환 경로는 열려 있음 | AI Hub 사전 변환 모델(FFNet 등) | — | ADP US$4,999(승인 필요, SW 자체 빌드) | Q6 Q9 |

#### (ii) 실차에 탑재해 주행·테스트할 때

| 카테고리 | 차량 컴퓨트 | 카메라·센서 | 인터페이스 | 전원·기타 | 공개가 | 근거 |
|---|---|---|---|---|---|---|
| A1 VLA 실차 | Jetson AGX Thor(연구) / DRIVE AGX Thor DevKit SKU 12(양산 경로, 가격 비공개·프로그램 승인) / x86 차량 PC + RTX GPU(대학 방식) | GMSL2 카메라 4~7(Alpamayo 기본 4: 좌·전방광각·우 120° + 전방망원 30°), HDR 120 dB+ | GMSL 디시리얼라이저(Connect Tech JCB002, Jetson용) 또는 DRIVE 내장 16× GMSL2; CAN FD(PCAN/Kvaser); DBW 키트 | DC-DC 12 V→보드(Thor DRIVE 350 W, Jetson Thor ≤130 W), 마운트·냉각 | 카메라 US$429~/개, JCB002 US$540, CAN US$347~407, DBW 견적 | M3 N1 S13 S15 S21 S20 N3 |
| A2 데이터 수집 | x86 차량 PC(Neousys Nuvo-10108GC: 350 W RTX 1장) 또는 ADLINK/MIIVII(Jetson Orin·Thor 탑재) | 카메라 6~8(GMSL2 또는 GigE), LiDAR 1~2(Hesai AT128 / Ouster OS1 / RoboSense Helios), 4D 레이더(선택), GNSS/INS(Xsens MTi-680G / NovAtel PwrPak7) | PTP 시간동기, 10 GbE 스위치, DBW(Dataspeed·PACMod) | 대용량 NVMe(카메라 8대 수집), DC-DC, 랙 | Helios US$1,800, MTi-680G £2,729, 나머지 견적 | S2 S8 S17 S19 S20 |
| A3 시뮬→실차 전이 | A1과 동일 보드 | A1과 동일 | 시뮬 시나리오를 실차 로그로 재현하려면 GNSS/INS 필수 | — | — | M9 M14 |
| A4 지연 실측 | Jetson Orin/Thor 또는 DRIVE Thor | 카메라 4(실시간 입력) | CAN FD로 차량 속도·조향 수신 | jtop/INA3221 전력, 온도 로깅 | — | S26 S23 |
| A5 양산급 실차 | **comma 3X/four**(카메라·LTE·CAN FD 내장, 325+ 차종 하네스) — 가장 싼 실차 E2E | 내장 3× 1080p 140 dB | 차량 하네스 US$99 | — | US$999 + 99 | X14 |
| 💡 제안 | **Hailo-10H M.2를 x86 차량 PC에 추가**해 메인 GPU는 주행 모델, Hailo는 저전력 VLM/보조 인식 담당으로 분리 실험(2.5 W, 20 INT8 TOPS). 사례 없음, 제안 | — | PCIe Gen3 x4 M.2 | — | US$260 | X12 |

**공통 부자재 체크리스트(실차)**: GMSL 디시리얼라이저 + FAKRA 케이블 · CAN FD 인터페이스 2ch · OBD-II/차량 하네스 · 100/1000BASE-T1 미디어 컨버터(양산 센서·ECU 연결 시, €400) · 12 V DC-DC(보드 피크 전력 기준) · GNSS 안테나 2개(이중 안테나 INS) · 5G/LTE 모듈(Quectel RM520N-GL, US$276~327) · 전력계·온도 로거 · 마운트/냉각 [S22][S25][S26] 🔍📰.

---

## Part B. 온디바이스 AI

### B-1. 지금 진행되는 연구 — 사례와 카테고리

| 카테고리 | 연구 내용 | 대표 사례 | 사례가 쓴 하드웨어 | 근거 |
|---|---|---|---|---|
| **B1 콕핏 어시스턴트 SLM/VLM** | 3~30B 모델을 콕핏 SoC에 올려 음성·시각 대화 | Cerence CaLLM Edge(Phi-3 3.8B, 4-bit) · Visteon(Qwen 7B, QNN→Hexagon NPU) · Banma AutoOmni 2.0(23B-A3B MoE, 8397 대상) · Xpeng×Banma(30B급 로컬) · FEV×Microsoft(Phi-4-mini on DRIVE AGX, 오프라인) · Lynk & Co 900·Zeekr 9X(2× SA8295P) | 퀄컴 8295 2개 / Cockpit Elite 8397 / Xpeng Turing / DRIVE AGX Orin | O6 O2 O4 O3 O7 Q11 V5 |
| **B2 엣지 LLM/VLM 구조·성능 분석** | 정밀도·KV 캐시·투기 디코딩·전력 모드별 거동 | TensorRT-Edge-LLM 공식 벤치(Thor Qwen2.5-VL-7B NVFP4 61 tok/s, EAGLE3 177; Orin INT4 64) · arXiv 2506.09554(Orin AGX, 2.7B–32.8B, 전력 모드) · Qualcomm AI Hub(SA8295P ADP, Llama 3.2 1B 11 tok/s) · 엣지 LLM 서베이 | Jetson Thor/Orin, DGX Spark, SA8295P ADP | N12 M10 Q10 M18 |
| **B3 엣지↔클라우드 하이브리드** | 온보드 SLM + 클라우드 LLM 분담·라우팅·투기 디코딩 | Li Mind GPT-3o(엣지 NPU + 클라우드) · Cerence xUI(Orin 온보드 + 클라우드) · AWS 가이드(시맨틱 라우팅, OTA 재학습) · TensorRT-Edge-LLM 인캐빈 레퍼런스(오케스트레이터) · 엣지-클라우드 투기 디코딩(지연 −35%, 로봇 실험) | DRIVE AGX Orin/Thor + 클라우드 | O5 O6 M12 N16 |
| **B4 에이전트·툴 사용(차량 데이터)** | LLM이 CAN/OBD/VSS 신호를 읽고(쓰고) 행동 | Peykan(MCP over CAN/OBD/UDS/J1939, 가상 CAN+ECU 시뮬) · KUKSA Databroker(VSS gRPC) · AAOS VHAL · AI-CDA4All(LLaMA 3.2 on AGX Orin, 응답 5.07 s) | Jetson AGX Orin, Raspberry Pi + CAN HAT | O9 O11 M10 O10 |
| **B5 도메인 간 컴퓨트 공유·통합** | AD 칩 여유 연산을 콕핏 모델에, 또는 한 SoC에 콕핏+ADAS | NIO(4× Orin-X 중 256 TOPS를 NOMI GPT에) · MediaTek C-X1 + DRIVE AGX(DriveOS 공유) · Snapdragon Ride Flex 8775P(콕핏+ADAS 단일 SoC, Hyundai Mobis·Bosch) | Orin-X 4개 / C-X1+Thor / 8775P | V7 X18 Q14 Q13 |

`분석` — 공개 연구(B2·B4)는 거의 Jetson 위주이고, 양산(B1·B5)은 퀄컴 위주다. 이 간극 자체가 연구 기회다(R3·R6).

### B-2. 연구별 필요 하드웨어·부자재

| 카테고리 | 벤치 구성 | 실차 구성 | 부자재 | 공개가 | 근거 |
|---|---|---|---|---|---|
| B1 콕핏 SLM/VLM | Jetson AGX Orin 64 GB(3~8B INT4) 또는 Jetson AGX Thor(7~30B NVFP4) + USB 마이크/스피커/카메라 | 같은 보드를 12 V DC-DC로 차량 전원에, CAN FD로 차량 상태 수신 | 마이크 어레이, 디스플레이, LTE/5G | Orin US$1,999 / Thor US$3,499~5,499 | N10 N9 |
| B1 💡 제안(퀄컴) | **Lantronix SA8295P ADP**(양산 콕핏과 같은 칩) 또는 **SA8255P/SA8775P Ride SX ADP** + Qualcomm AI Hub/QNN으로 Llama/Qwen 양자화 모델을 Hexagon NPU에 배포. 사례: Visteon(8397+Qwen 7B), AI Hub(8295+Llama 1B). 제약: 퀄컴 승인, SW 미포함(CreatePoint 빌드), TOPS 비공개 | ADP는 차량 전원 규격 보드이므로 그대로 탑재 가능(⚠️ 미확인) | — | US$6,300 / US$4,999 | Q5 Q6 Q7 Q9 Q10 O2 |
| B2 구조·성능 분석 | Orin 64 GB(세대 기준선) + Thor(FP8/NVFP4·EAGLE3) + 호스트 GPU(비교군); jtop/INA3221 전력 | 차량 전원·온도 조건에서 동일 측정 | 전력계, 온도 로거 | — | N11 N12 S26 |
| B2 💡 제안(퀄컴) | SA8295P ADP를 세 번째 비교군으로 두면 "GPU(Jetson) vs NPU(Hexagon)" 정밀도·전력 비교가 가능. 공개 수치는 Llama 3.2 1B 11 tok/s뿐이라 측정 자체가 기여 | — | — | US$6,300 | Q10 |
| B3 하이브리드 | 엣지 보드 + 호스트 GPU(RTX PRO 6000 96 GB / DGX Spark 128 GB) + 10 GbE | 엣지 보드 + 5G 모듈(RM520N-GL) + 클라우드 GPU | 네트워크 지연 주입 도구 | PRO 6000 US$8,435~ / Spark US$4,699~ / 5G US$276~327 | P1 P2 S25 |
| B4 에이전트 하네스 | 엣지 LLM 보드 + **가상 CAN(SocketCAN vcan) + Peykan**(ECU 시뮬레이터 내장) | 엣지 보드 + CAN FD 인터페이스(PCAN/Kvaser) + OBD-II 커넥터(읽기 전용) 또는 Raspberry Pi + PiCAN2 | DBC 파일(차종별), KUKSA Databroker | CAN US$347~407 / PiCAN2 €45 | O9 S21 S24 O11 |
| B5 도메인 공유 | Jetson(AD 역할) + 퀄컴 ADP 또는 2번째 Jetson(콕핏 역할), 10 GbE/T1로 연결 | 두 보드를 차량에 탑재, T1 컨버터로 양산 ECU와 연결 | T1 미디어 컨버터(€400), PTP | — | S22 |
| B5 💡 제안 | NIO식 "AD 칩 여유분을 콕핏 모델에" 실험을 **Jetson Thor 1대에서 MIG/프로세스 분리**로 먼저 흉내 낸 뒤 2보드로 확장. 사례 없음 | — | — | — | V7 |

---

## 연구 주제 후보 → 장비 세트 매핑

| 후보 | 시작 세트 | 확장 세트 | 1판 구매 단계 |
|---|---|---|---|
| R1 VLA 양자화·지연 | RTX 4090/5090 + Jetson AGX Orin 64 GB | + Jetson AGX Thor, GMSL 카메라 4 + JCB002 | A → B |
| R2 개루프↔폐루프 평가 | RTX 4090/5090 1~2장 + NAVSIM·Bench2Drive | + MORAI, 실차 로그(A2 수집 차량) | A |
| R3 퀄컴 NPU 콕핏 SLM 💡 | SA8295P ADP + AI Hub/QNN + Orin 비교군 | + SA8775P ADP(콕핏+ADAS) | B(+ADP) |
| R4 엣지↔클라우드 분할 | Orin/Thor + RTX PRO 6000/DGX Spark + 10 GbE | + 5G 모듈, 실차 | B |
| R5 SLM + CAN 에이전트 | Orin + vcan + Peykan | + PCAN/Kvaser + OBD-II, comma 3X 차량 하네스 | A → B |
| R6 도메인 공유 💡 | Jetson Thor 1대(MIG/프로세스 분리) | + 퀄컴 ADP 2보드, T1 컨버터 | B |

1판 구매 단계: **A** 벤치 최소(GPU + Orin + CAN) · **B** 공용(호스트 GPU + Jetson Thor + GMSL 카메라 + comma 3X + 선택 ADP) · **C** 실차 확장(차량 PC/DRIVE + 멀티카메라 + LiDAR + GNSS/INS + DBW). 상세는 [1판 §4](research-hardware-survey.md#4-연구용-구매-조합-3단계-공개-표시가-기준).

---

## 미확인·주의

- 퀄컴 제안(R3·R6)은 **사례가 아니라 제안**이다. SA8255P·8397P·8797P의 NPU TOPS는 비공개, 8295P는 30/60 TOPS 보도 충돌, ADP는 승인·SW 자체 빌드가 필요하다 ⚠️ [Q5][Q7][Q11].
- Thor-U TOPS는 700/730/750 보도가 섞여 있고 NVIDIA 공식은 Thor-X만 명시한다 ⚠️ [V1][V6][N3]. Jetson Thor(128 GB, HSB)와 DRIVE Thor(64 GB, GMSL)는 다른 제품이다 [N7][N1].
- GAIA-2 파라미터(8.4B)·GAIA-3는 2차 위키 출처라 미확인 ⚠️ [M15]. MORAI 라이선스 조건 미확인 ⚠️.
- 가격은 2025–2026에 크게 변동했다(Jetson Thor US$3,499→5,499, DGX Spark US$3,999→6,950) [N9][P2].
- 대부분의 벤더 페이지는 검색 발췌로 확인했다(1판 헤더 참조).

## 용어

| 용어 | 뜻 |
|---|---|
| 개루프 / 폐루프 | 로그 재생으로 궤적 오차를 재는 평가 / 시뮬레이터에서 모델이 실제로 주행하며 점수를 받는 평가 |
| VLA | Vision-Language-Action. 카메라 입력을 언어 모델 백본으로 처리해 궤적을 내는 모델 |
| ADP | Qualcomm Automotive Development Platform. 차량 SoC 레퍼런스 보드 |
| QNN / AI Hub | 퀄컴 AI Engine Direct SDK / 사전 변환 모델·디바이스 벤치 포털 |
| GMSL2 · HSB | 양산 차량 카메라 직렬 링크(디시리얼라이저 필요) · Jetson Thor의 QSFP 카메라 입력 |
| EAGLE3 / NVFP4 | 투기 디코딩 기법 / Blackwell 4-bit 부동소수점(Thor·DGX Spark만) |
| vcan / DBC | 리눅스 가상 CAN 인터페이스 / CAN 신호 정의 파일 |
