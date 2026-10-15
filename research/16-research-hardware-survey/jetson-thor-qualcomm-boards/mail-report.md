# [메일용] Jetson AGX Thor 활용 사례·부자재 / 퀄컴 보유 보드 대비 상위 보드 조사 — 결과

> 작성일 2026-10-15. 외부 공개 자료만으로 조사(저장소 기존 문서 미참고). 등급: 🔍 공식 / 📄 논문 / 📰 언론·2차 / 💬 포럼 / 🏷️ 리셀러·벤더 / ⚠️ 미확인·충돌. 괄호 ID는 [전체 출처 88건](reference/references.md)에 대응. 가격은 조사일 공개 표시가.

## 0. 한 줄 결론

- **Jetson AGX Thor**: 실제 도로 차량에 올린 공개 논문은 아직 없고, 차량 관련 사례는 ① 주행 VLA 추론 가속·특성화 논문 ② 멀티카메라 BEV 벤치 ③ **Thor 모듈 기반 차량용 박스 PC·캐리어(8~16× GMSL2 + CAN FD)** 다. 데브킷에 양산급 카메라를 붙이려면 **HSB(QSFP) 경로 + GMSL2 디시리얼라이저** 또는 **GMSL2 캐리어/박스**가 필요하다 [J1][J19][J43] 📄🔍🏷️.
- **퀄컴**: 보드는 차량용 ADP / Dragonwing IQ·QCS EVK / Snapdragon X / 모바일 HDK 네 갈래이고, 보유 중인 **IQ-9075(QCS9075, NPU 최대 100 INT8 TOPS, 36 GB)** 가 이미 LLM에 가장 강하다. 차량과 같은 칩으로 올라가려면 **SA8775P Ride Flex ADP(US$4,999)**, LLM 공개 수치가 많은 쪽은 **Snapdragon 8 Elite HDK(US$1,499)** 다 [K35][K4][K55] 🔍🏷️.

## 1. Jetson AGX Thor — 활용 사례

### 1-1. 연구 사례 (차량 관련만)
- **FlashDrive**(Z Lab, 2026-08): 주행 VLA Alpamayo 1.5-10B 추론 가속(KV 캐시 재사용·투기 추론·W4A8). RTX PRO 6000 716.9→151.4 ms(4.7×), **Jetson Thor 4.0× 가속**(절대값 미공개 ⚠️). 시뮬 폐루프만, 실차 없음. 카메라 전용 VLA라 센서 HW 기재 없음 [J1] 📄.
- **VLA-Perf**(NVlabs, 2026-02): Thor LPDDR ~270 GB/s라 비전 인코더·VLM 백본까지 메모리 바운드 → 주행 VLA도 메모리 대역폭이 한계 [J5] 📄. Orin vs Thor 특성화: 지연의 최대 75%가 메모리 바운드 액션 생성 [J3] 📄.
- RidgeRun **멀티카메라 BEV** 스티칭 벤치 Thor vs Orin [J9] 🏷️. 포럼: Thor는 INT8보다 FP8/FP4 유리 — 기존 INT8 인식 모델 이식 시 주의 [J12] 💬.

### 1-2. 차량 산업 사례 — Thor 기반 차량용 컴퓨터·캐리어
- 업계는 Thor를 데브킷이 아니라 **"T5000 모듈 + 8~16 GMSL2 + CAN FD 박스"** 로 쓴다:
  - **MIIVII APEX THOR**(Autoware 레퍼런스 HW 등재): 128 GB, GMSL, CAN, SIM, 9–36 V [J18] 🔍 · **Advantech MIC-742-AT**: **8× GMSL2 + 4× CAN FD**, Sensing Tech 차량용 GMSL 카메라 통합 [J19] 🔍
  - **Syslogic RML A5AGX**(러기드 차량 PC): 8× GMSL2(PoC), CAN FD, IP67 [J22] 📰 · Firefly EC-ThorT5000: 8× GMSL2, 4×10 GbE [J23] 📰
  - ASUS PE3000N: 최대 16× GMSL, 2× CAN, 12–60 V [J24] 🔍 · EverFocus EAR-100T: 12× GMSL2, €7,498(예비) [J25] 🏷️
  - **Leopard LI-THOR-BOX-GM2B**: MAX96712 내장, 8× GMSL2, **US$8,500** [J26] 🏷️ · **Seeed reComputer J601 캐리어**: 8× GMSL2, CAN FD, M.2 B-key(5G), 19–48 V [J28] 🏷️ · Connect Tech AGX301: GMSL2/3 브레이크아웃, 캐리어 US$2,054 [J21] 📰
- 완성차·L4 프로그램(TIER IV·Isuzu 버스 등)은 **DRIVE AGX Thor**(별개 제품) [J37] 📰. Ouster REV8 LiDAR는 Orin·Thor 드라이버 튜닝 발표 [J39] 🔍.

### 1-3. 데브킷 사양과 붙일 부자재
- 데브킷(T5000): 128 GB LPDDR5X(~270 GB/s), 2,070 FP4 TFLOPS, 40–130 W; **QSFP28 → HSB 카메라 최대 20대, 16-lane MIPI CSI-2 → 6대**; RJ45 5 GbE; M.2 M(NVMe 1 TB)+E(Wi-Fi), **B-key 없음**; CAN 헤더(J47) 2채널 [J58][J40][J50] 🔍. 가격 US$3,499 → **US$5,499(2026-07)** [J59] 📰. INT8보다 FP8/FP4 유리 [J12] 💬.
- 카메라 경로 ①: QSFP 브레이크아웃 → **Lattice CertusPro-NX HSB 보드(US$350)** → MIPI 카메라(Leopard 듀얼 IMX274 US$329, Thor 호환 표기 N/A ⚠️) [J41][J42] 💬🏷️
- 카메라 경로 ②: HSB에 **Leopard GMSL2 디시리얼라이저(US$388)** 결합 → 양산급 GMSL2 카메라(IMX728 등) — 데브킷을 바꾸지 않고 GMSL2를 쓰는 유일한 경로 [J43] 🏷️
- 카메라 경로 ③: e-con 10 GbE Holoscan 카메라(ISX031 120 dB HDR, IMX900 GS), 샘플가 요청 [J44] 🏷️
- CAN: J47 헤더 + SN65HVD230 트랜시버 보드, CAN FD 지원 [J50] 🔍 · 5G: 데브킷은 B-key 없음 → J601 등 캐리어의 B-key에 Quectel RM520N-GL(JetPack 7 검증 미확인 ⚠️) [J52] 🏷️
- 전원: 240 W USB-C PD 동봉, 대체 PSU 28 V 5 A 연속·7.5 A 피크; **차량 12 V→28 V PD 어댑터는 확인된 해법 없음**, 캐리어 직입력(19–48 V)이 현실적 [J51][J28] 💬🏷️ · 마운트 홀 없음, 커뮤니티 STL 인클로저·Seeed 히트싱크+팬 [J55] 💬
- SW: JetPack 7.0(CUDA 13) → 7.1(TensorRT-Edge-LLM) → 7.2(CUDA 13.2, MIG 프리뷰); Isaac ROS 4.x(Jazzy); Holoscan 3.9 [J56][J57] 🔍

## 2. 퀄컴 — 라인업 설명과 상위 보드

### 2-1. 라인업 사전 설명
| 라인업 | 칩 | 보드·판매처 | 용도 | 출처 |
|---|---|---|---|---|
| 차량용 Digital Chassis | SA8155P·SA8255P·SA8295P(콕핏), SA8775P(Ride Flex), QAM8797P/8397P(Elite) | **ADP** — Lantronix·Thundercomm, **퀄컴 승인 필요·SW 미포함** | 콕핏·ADAS 양산 | K4 K9 🏷️ |
| IoT·로보틱스 Dragonwing | IQ9(QCS9075)·IQ8(QCS8275)·IQ6, QCS6490(RB3 Gen 2), QRB5165(RB5), QCS8550 | **EVK** — 퀄컴·DigiKey·Lantronix; TurboX·Open-Q 키트 | 로봇·엣지 AI 박스 | K35 K44 K46 🔍🏷️ |
| PC Snapdragon X | X Elite(45 TOPS)·X2 Elite(80 TOPS) | 데브킷 **2024-10 취소**, Copilot+ 노트북이 타깃 | AI PC | K49 K50 K51 📰 |
| 모바일 | 8 Elite / 8 Elite Gen 5 | **HDK**(Lantronix US$1,499) | 레퍼런스 폰 | K55 🏷️ |
| 공통 SW | — | AI Hub(사전 변환 모델·벤치) + QNN/QAIRT + **Genie→GenieX**(2026-06 프리뷰) | — | K38 🔍 |

"온디바이스 LLM 특화 장치" 라인은 따로 없고, NPU·메모리가 큰 **IQ9·QCS8550·X·8 Elite**가 그 역할이다.

### 2-2. 보유 보드 기준선
- SA8155P ADP: Kryo 8코어, Adreno 640, Hexagon 696, **TOPS 비공개**(역산 ≈4 ⚠️), 12 GB, 8 GMSL [K1][K2] 🏷️
- SA8255P ADP(Ride SX 4.0): Kryo Gen-6, Adreno 663, Hexagon HTP, **TOPS 비공개**, 36 GB LPDDR5, 4× CSI; SA8775P와 같은 보드 [K3][K4] 🏷️
- SA7255P: **공개 사양 없음** ⚠️ [K5]
- **IQ-9075 EVK**: QCS9075, **NPU 50/100 INT8 TOPS**, 36 GB LPDDR5(ECC), Ubuntu; 브리프 "13B 모델 12 tok/s"; Radxa QCS9075 보드 Llama 3.2 3B ≈19.4 tok/s; GenieX 원격 테스트 대상 [K35][K36][K37][K38] 🔍🏷️

### 2-3. 상위 후보와 사례
| 보드 | NPU·사양 | 사례 | LLM 수치 | 가격 | 출처 |
|---|---|---|---|---|---|
| **SA8775P Ride Flex ADP** | 공식 TOPS 없음, 변종 72–192 TOPS 보도 ⚠️, ASIL-D | Neta·Buick·Arcfox·Nissan N6 양산; **Hyundai Mobis·HL Klemove** 채택 | AI Hub에 **Qwen3-8B·Qwen3-VL-8B w4a16** 빌드 등록 | **US$4,999** | K17 K18 K22 K21 K19 K4 |
| **SA8295P ADP** | 30(2021) vs 60 TOPS(2025 티어다운) ⚠️ | Mercedes E-Class·Lynk & Co 900 듀얼; Nexa AutoNeural VLM | Llama 3.2 1B 11 tok/s | US$6,300(+카메라 키트 US$799) | K7 K8 K13 K12 K10 K9 |
| QAM8397P Cockpit Elite / 8797P | 공식 TOPS 없음(보도 320/1,280 ⚠️) | **Visteon Qwen 7B 온디바이스**, Banma, Garmin, Mercedes·Li | — | **ADP 미출시** | K24 K26 K27 K28 |
| QCS8550 키트(TurboX C8550 / Open-Q 8550CS) | 48 INT8 / 12 FP16 TOPS, 16 GB | 엣지 AI 박스 | — | €1,490 / US$1,500 | K46 K47 |
| **Snapdragon 8 Elite HDK** | 플래그십 NPU(TOPS 비공개) | AI Hub Llama 3 8B·Qwen3-8B 등록 | Llama 3.2 3B ≈10 tok/s | US$1,499 | K55 K56 K57 |
| Snapdragon X2 Elite | NPU 80 TOPS | X Elite NPU 온디바이스 RAG 논문(에너지 12.3× 절감) | — | 노트북 | K51 K52 |
| (참고) SA8255P 위 사례 | — | **Desay SV + ModelBest 1.2B** 음성, 첫 응답 <300 ms | — | 보유 보드로 재현 가능 | K29 |

## 3. 제안
- Thor: 데브킷 + Lattice HSB + Leopard GMSL2 디시리얼라이저 + GMSL2 카메라 4대 + J47 CAN 트랜시버로 시작 → 실차 단계에서 Seeed J601 캐리어 또는 Leopard Thor 박스로 이전. 연구는 FlashDrive 식 Alpamayo 가속을 Thor에서 재현해 **미공개 절대 지연값을 확보**하는 것이 기여 [J43][J50][J28][J1].
- 퀄컴: 1순위 **SA8775P ADP**(차량 ASIL-D, Qwen3-8B 빌드, 국내 Tier-1 채택) → 2순위 **8 Elite HDK**(LLM 공개 수치 多) → SA8295P ADP는 양산 콕핏 재현 목적일 때만. 당장은 보유 IQ-9075에 GenieX/AI Hub로 Qwen3-8B·Llama 3.2 3B tok/s·전력 측정, SA8255P ADP에는 1.2B급 음성 모델 재현 [K19][K22][K55][K36][K29].

## 4. 미확인·주의
- Thor 실차 논문 없음; FlashDrive Thor 절대 지연·MIIVII APEX THOR 사양·다수 캐리어 가격 미확인 ⚠️. Leopard HSB 카메라 Thor 호환 표기 N/A, 5G·GNSS·LiDAR의 JetPack 7 검증 보고 없음 ⚠️.
- 퀄컴 차량용 칩은 모두 공식 TOPS 비공개; SA7255P·SA8650P 사양, Elite ADP, AI Hub 8775/9075 tok/s 미확보 ⚠️. 가격 변동 큼(Thor 데브킷 +57%).
