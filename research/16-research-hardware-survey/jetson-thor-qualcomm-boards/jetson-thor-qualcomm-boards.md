# Jetson AGX Thor 사용 사례·부자재 / 퀄컴 보유 보드 대비 상위 보드 조사

> **작성일**: 2026-10-15 · **상태**: 초판 · 16번 주제의 후속편(보드 특정)
> **전제**: 자율주행은 **Jetson AGX Thor Developer Kit(T5000)** 을 구매한다. 온디바이스는 현재 **퀄컴 SA8155P·SA8255P·SA7255P 프로젝트 개발보드 + SA8255P ADP + SA8155P ADP + Dragonwing IQ-9075 EVK** 를 보유한다.
> **목적**: ① Jetson AGX Thor를 쓴 **차량 관련** 연구·산업 사례와, 그 사례가 함께 쓴 부자재(카메라·인터페이스·CAN·전원 등)를 정리한다(로봇·산업 장비 사례는 제외). ② 퀄컴 보드 라인업이 어떻게 나뉘는지 설명하고, 보유 보드보다 상위인 보드와 그 사례를 정리한다.
> **표기**: 🔍 공식 / 📄 논문 / 📰 언론·2차 / 💬 포럼 / 🏷️ 리셀러·벤더 제품 페이지 / ⚠️ 미확인·충돌. 출처 ID는 [reference/references.md](reference/references.md). 저장소 기존 문서는 참고하지 않았고, 조사 환경 제약으로 GitHub·PyPI 외 페이지는 검색 발췌로 확인했다. 가격은 조사일 공개 표시가.

---

## 결론 먼저

1. **Jetson AGX Thor를 "실제 도로 차량"에 올린 공개 논문은 아직 없다.** 차량 관련 Thor 사례는 ① 주행 VLA 추론 가속·특성화 논문(FlashDrive, VLA-Perf) ② 멀티카메라 BEV 벤치 ③ **Thor 모듈 기반 차량용 박스 PC·캐리어(8~16× GMSL2 + CAN FD; Advantech·Syslogic·Leopard·Seeed·MIIVII)** 다 [J1][J5][J9][J19][J18] 📄🏷️🔍. Autoware·TIER IV의 공식 차량 프로그램은 DRIVE AGX Thor 쪽이다 [J37] 📰.
2. **Thor 데브킷에 양산급 카메라를 붙이는 정석은 HSB(Holoscan Sensor Bridge)와 16-lane MIPI CSI-2이고, GMSL2는 ① HSB용 GMSL2 디시리얼라이저(Leopard, US$388) ② Thor용 캐리어/박스(Connect Tech·Seeed·Advantech·Leopard US$8,500) 중 하나가 필요하다** [J40][J43][J21][J26] 🔍🏷️. CAN은 데브킷 헤더(J47)에 트랜시버만 달면 된다 [J50] 🔍.
3. **퀄컴 보드는 크게 네 라인업이다.** 차량용(SA/QAM ADP, Lantronix·Thundercomm 판매, 승인 필요) / IoT·로보틱스 Dragonwing(IQ6·IQ8·IQ9 EVK, RB3·RB5, QCS8550 키트) / PC(Snapdragon X 계열, 데브킷은 2024-10 취소) / 모바일(HDK·QRD). 소프트웨어는 공통으로 AI Hub + QNN/QAIRT + Genie→GenieX [K38][K49][K50] 🔍📰.
4. **보유 보드 대비 상위 후보는 세 축이다.** 차량용 같은 칩으로 가려면 **SA8295P ADP(US$6,300)·SA8775P Ride Flex ADP(US$4,999)**, 생성 AI 성능으로 가려면 **IQ-9075(QCS9075, NPU 최대 100 INT8 TOPS, 36 GB, EVK €825)** 가 이미 보유 중인 가장 강한 NPU이고, 그 위는 **Snapdragon 8 Elite HDK(US$1,499)** 와 Cockpit/Ride Elite(ADP 미출시)다 [K9][K4][K35][K36][K55][K24] 🏷️🔍.
5. **퀄컴 NPU 위 LLM 공개 수치는 적다.** 확인된 것은 SA8295P ADP Llama 3.2 1B 11 tok/s, QCS9075 Llama 3.2 3B ≈19.4 tok/s, IQ-9075 브리프 "13B 모델 12 tok/s", 8 Elite Llama 3.2 3B ≈10 tok/s뿐이다 [K10][K37][K36][K56] 🔍🏷️📰. SA8775P에는 Qwen3-8B·Qwen3-VL-8B w4a16 빌드가 AI Hub에 올라와 있다 [K19] 🔍.

---

## Part 1. Jetson AGX Thor — 사례와 부자재

### 1-1. 데브킷 사양 요약 (무엇을 갖고 시작하나)

| 항목 | 사양 | 출처 |
|---|---|---|
| 모듈 | T5000: Blackwell GPU 2,560 CUDA / 96 Tensor, 14× Arm Neoverse-V3AE, **128 GB LPDDR5X(~270 GB/s)**, 최대 2,070 FP4 희소 TFLOPS, 40–130 W | J58 🔍 |
| 카메라 입력 | **QSFP28(4×25 GbE) → HSB 카메라 최대 20대**, **16-lane MIPI CSI-2 커넥터 → 최대 6대(가상 채널 시 32)**, USB 카메라 | J40 🔍 |
| 네트워크·확장 | RJ45 5 GbE, M.2 Key M(NVMe 1 TB 동봉) + Key E(Wi-Fi 6E) — Key B(LTE/5G)는 없음 | J58 🔍 |
| CAN | 2×13 헤더(J47)에 CAN 컨트롤러 2채널, CAN FD 지원, **외부 트랜시버(SN65HVD230 등) 필요** | J50 🔍 |
| 전원 | 240 W USB-C PD(Delta ADP-240LB) 동봉, 대체 PSU는 28 V 5 A 연속·7.5 A 피크; Micro-Fit DC 잭도 있으나 피크 보장 안 됨 | J51 💬 |
| 소프트웨어 | JetPack 7.0(CUDA 13, TRT 10.13, HSB 통합) → 7.1(TensorRT-Edge-LLM) → 7.2(CUDA 13.2, TRT 10.16, MIG 프리뷰); ROS 2 Jazzy(Isaac ROS 4.x); Holoscan 3.9 | J56 J15 J57 🔍 |
| 가격 | US$3,499(2025-08) → **US$5,499(2026-07)**; T4000 모듈(64 GB, 1,200 TFLOPS) US$1,999, T3000/T2000은 2027 Q1 예고 | J59 J60 📰 |
| 주의 | DRIVE AGX Thor(DriveOS, GMSL 내장)와 별개 제품; Thor는 INT8보다 FP8/FP4가 유리(포럼 INT8 성능 불만) | J61 J12 💬 |

### 1-2. 연구 사례 — 무엇을 했고 무엇을 붙였나 (차량 관련만)

| 사례 | 연구 내용 | Thor에서의 결과 | 함께 쓴 부자재 | 출처 |
|---|---|---|---|---|
| **FlashDrive**(Z Lab, 2026-08) | 주행 VLA **Alpamayo 1.5-10B** 추론 가속: KV 캐시 재사용, 투기 추론, W4A8 양자화, CUDA Graph | RTX PRO 6000 716.9→151.4 ms(4.7×, 1.4→6.6 Hz); **Jetson Thor 4.0× 가속**(절대값 미확인 ⚠️); 시뮬 폐루프만, 실차 없음 | 카메라 전용 VLA(Alpamayo 입력), 센서 HW 미기재 | J1 📄 |
| **VLA-Perf**(NVlabs, 2026-02) | 루프라인 기반 VLA 성능 모델(주행·로봇 VLA 공통) | Thor LPDDR ~270 GB/s라 비전 인코더·VLM 백본까지 메모리 바운드 → 주행 VLA도 양자화·캐시보다 메모리 대역폭이 한계 | 없음(모델링) | J5 📄 |
| Orin vs Thor 특성화(arXiv 2603.02271 / 2604.24447) | 7B급 VLA를 Orin 64 GB vs Thor 128 GB에서 프로파일링(일반 VLA) | 지연의 최대 75%가 메모리 바운드 액션 생성; Thor 절대값 미확보 ⚠️ | 없음 | J3 J4 📄 |
| RidgeRun **멀티카메라 BEV** 벤치 | 차량형 멀티카메라 BEV 스티칭 성능 Thor vs Orin vs Orin NX | 수치 페이지 참조 | 멀티카메라(종류 미기재) | J9 🏷️ |
| 포럼: Thor INT8 성능 | Blackwell은 INT8보다 FP8/FP4 유리 — 기존 INT8 인식 모델 이식 시 주의 | — | — | J12 💬 |

`분석` — Thor 논문은 아직 "주행 VLA가 Thor에서 얼마나 빠른가"를 재는 단계이고, 카메라·차량 통합이 구체적인 공개 연구는 없다. 자율주행 연구로 가져오려면 FlashDrive 식 Alpamayo 가속을 Thor에서 재현하고(절대 지연값이 공개되지 않아 측정 자체가 기여), 카메라는 아래 1-4의 HSB/GMSL2 경로로 붙여야 한다.

### 1-3. 차량 산업 사례 — Thor 기반 차량용 컴퓨터·캐리어

| 제품 / 사례 | 내용 | 카메라·CAN 등 | 가격 | 출처 |
|---|---|---|---|---|
| **MIIVII APEX THOR**(Autoware 레퍼런스 HW 등재) | T5000 차량용 AD 컴퓨터: 128 GB, GMSL, CAN, SIM, 9–36 V, −25~70 °C | GMSL·CAN 채널 수 미확인 ⚠️ | 미공개 | J18 🔍 |
| **Advantech MIC-742-AT** | T5000 차량용 박스: **8× GMSL2(mini-FAKRA) + 4× CAN FD**; Sensing Tech 차량용 GMSL 카메라 통합 발표(2025-12) | 8 GMSL2, 4 CAN FD | 미공개 | J19 🔍 |
| Advantech MIC-743-AT7A1 | QSFP28(HSB) + 5 GbE + M.2 B-key(LTE) | HSB·LTE | 미공개 | J20 🏷️ |
| **Syslogic RML A5AGX** | 러기드 차량 PC(T4000/T5000): 8× GMSL2(PoC), CAN/CAN FD, IP67/69, −25~60 °C | 8 GMSL2 | 미공개 | J22 📰 |
| Firefly EC-ThorT5000 | 8× GMSL2, 4×10 GbE + 4× GbE, CAN/RS485 | 8 GMSL2 | 미공개 | J23 📰 |
| ASUS IoT PE3000N | 최대 16× GMSL, 2× CAN, 12–60 V, MIL-STD-810H, 2026 Q1 | 16 GMSL | 미공개 | J24 🔍 |
| EverFocus EAR-100T | 12× GMSL2, 2× CAN FD, 2× 5 GbE | 12 GMSL2 | €7,498(예비) | J25 🏷️ |
| **Leopard LI-THOR-BOX-GM2B** | MAX96712 디시리얼라이저 내장 Thor 박스, 최대 8× GMSL2 | 8 GMSL2 | **US$8,500** | J26 🏷️ |
| **Seeed reComputer J601 캐리어** | 8× GMSL2, 4×10 GbE, M.2 E/M/**B**, CAN FD, 19–48 V; 전용 히트싱크+팬 | 8 GMSL2, CAN FD, 5G B-key | 견적 | J28 🏷️ |
| **Connect Tech Gauntlet AGX301 / Anvil-T5** | 캐리어: 16-lane MIPI 확장 → GMSL3/GMSL2/FPD-Link III 브레이크아웃(별매), 2×10 GbE, 2× NVMe | GMSL2/3 via CTI 보드 | 캐리어 US$2,054, 번들 US$9,939–12,914 | J21 📰🏷️ |
| Auvidea X242 / Antmicro 오픈 베이스보드 | 산업용 캐리어(16-lane CSI, PCIe x16) / 오픈하드웨어 24 V 베이스보드 | MIPI CSI | 미공개 | J29 J30 📰 |
| TIER IV × Isuzu L4 버스(참고) | 완성차·버스 프로그램은 **DRIVE AGX Thor**(DriveOS, 별개 제품) + DRIVE Hyperion 센서 세트 | — | — | J37 📰 |
| Ouster REV8 LiDAR | Orin·Thor용 드라이버·Isaac ROS 플러그인 튜닝 발표(JetPack 7 명시 없음 ⚠️) | 이더넷 LiDAR | — | J39 🔍 |

`분석` — 차량 산업은 Thor를 **"데브킷"이 아니라 "T5000 모듈 + 8~16 GMSL2 + CAN FD 박스"** 로 쓴다. 데브킷으로 시작해도 실차 단계에서는 캐리어(Seeed J601, Connect Tech)나 박스(Leopard, Advantech)로 옮기는 그림이 현실적이다. 완성차 양산·L4 프로그램은 Jetson이 아니라 DRIVE AGX Thor를 쓴다.

### 1-4. 데브킷에 붙일 부자재 — 카메라 경로 3가지와 기타

| 경로 | 구성 | 확인된 제품·가격 | 비고 | 출처 |
|---|---|---|---|---|
| **① HSB(QSFP) 카메라** | QSFP28 브레이크아웃 → Lattice CertusPro-NX HSB 보드(2× 10 GbE) → MIPI 카메라 | Lattice LF-SNSR-ETH-EVN US$350; Leopard 듀얼 IMX274 US$329–355(Thor 호환 표기 "N/A", 벤더 확인 필요 ⚠️) | NVIDIA가 데브킷 공식 지원 경로로 확인; JetPack 7.0 초기엔 CoE 카메라만 | J41 J42 💬🏷️ |
| **② HSB + GMSL2 디시리얼라이저** | Lattice HSB에 Leopard GMSL2 디시리얼라이저 키트 결합 → 양산급 GMSL2 카메라(IMX728 등) | **LI-GMSL2-DESER-HOLOSCAN US$388**(HSB·카메라 별매); LI-IMX728-9295 키트 견적 | 데브킷을 바꾸지 않고 GMSL2를 쓰는 유일한 경로 | J43 🏷️ |
| **③ 10 GbE Holoscan 카메라** | e-con e-CAM31_CUHSB(ISX031 3 MP 120 dB HDR) / e-CAM37_CUHSB(IMX900 GS): RJ45 10 GbE → Thor | 샘플가 요청 | 데브킷 RJ45는 5 GbE라 QSFP 브레이크아웃 또는 10 GbE 경로 필요 ⚠️ | J44 J45 🏷️ |
| MIPI CSI-2 직결 | 16-lane 커넥터에 MIPI 모듈(IMX477 등) | RidgeRun IMX477 드라이버(커스텀 보드); 데브킷 레퍼런스 카메라 미확인 ⚠️ | 저가(Waveshare ISX031 US$88) 모듈의 Thor 호환은 미확인 | J47 J48 J49 🏷️ |
| CAN | J47 헤더 + SN65HVD230 트랜시버 보드 | 수천 원대 모듈 | CAN FD 지원, 종단 점퍼 | J50 🔍 |
| 5G/LTE | 데브킷은 Key B 없음 → Seeed J601·Advantech MIC-743 캐리어의 B-key에 Quectel RM520N-GL | Seeed 위키는 JetPack 6.2 기준(Thor 확인 없음 ⚠️) | — | J52 J28 🏷️ |
| GNSS/INS·LiDAR | USB/시리얼 ROS 2 드라이버(Septentrio·u-blox·Xsens), Nebula(Hesai·Velodyne·RoboSense) | Thor/JetPack 7 테스트 보고 없음 ⚠️ | 이더넷 LiDAR는 5 GbE RJ45 또는 QSFP 브레이크아웃 | J53 J54 🏷️ |
| 전원(차량) | 12 V → 28 V/5 A USB-C PD-EPR 어댑터 솔루션 미확인 ⚠️; 캐리어는 19–48 V(J601), 9–36 V(MIIVII) 직입력 | — | 차량 탑재는 캐리어 전원이 현실적 | J51 J28 J18 |
| 마운트·냉각 | 데브킷 마운트 홀 없음(포럼); 커뮤니티 STL 인클로저; Seeed J601 히트싱크+팬(60 °C까지 풀성능) | — | — | J55 🏷️💬 |

---

## Part 2. 퀄컴 — 라인업 설명과 상위 보드

### 2-1. 라인업은 어떻게 나뉘나 (사전 설명)

| 라인업 | 칩 접두어 | 보드 형태·판매처 | 용도 | OS·SW | 출처 |
|---|---|---|---|---|---|
| **차량용 Snapdragon Digital Chassis** | SA/QAM(SA8155P·SA8255P·SA8295P 콕핏, SA8775P Ride Flex, SA8650P Ride, QAM8797P Ride Elite·QAM8397P Cockpit Elite) | **ADP(Automotive Development Platform)** — Lantronix·Thundercomm 판매, **퀄컴 승인 필요, 소프트웨어 미포함(CreatePoint에서 빌드)** | 콕핏·ADAS 양산 개발 | QNX/Android Automotive/Linux, QNN(SA8295~SA8797 공통 API) | K4 K9 K34 🏷️🔍 |
| **IoT·로보틱스 Dragonwing** | IQ9(QCS9075)·IQ8(QCS8275)·IQ6(QCS615), QCS6490(RB3 Gen 2), QRB5165(RB5), QCS8550 | **EVK** — 퀄컴 직판·DigiKey·Lantronix; RB3/RB5는 Thundercomm; QCS8550은 Thundercomm TurboX·Lantronix Open-Q | 로봇·엣지 AI 박스·드론·산업 | Qualcomm Linux·Ubuntu(IQ), Android(QCS8550), ROS 2(RB5) | K35 K40 K44 K45 K46 K47 🔍🏷️ |
| **PC Snapdragon X** | X Elite(NPU 45 TOPS)·X2 Elite(80 TOPS) | Windows 데브킷은 **2024-10 취소·환불**; 지금은 Copilot+ 노트북이 개발 타깃 | AI PC | Windows ML, QAIRT | K49 K50 K51 📰 |
| **모바일** | Snapdragon 8 Elite / 8 Elite Gen 5 | **HDK**(Lantronix US$1,499), QRD | 스마트폰 레퍼런스 | Android, AI Hub | K54 K55 🏷️📰 |
| 공통 소프트웨어 | — | **AI Hub**(사전 변환 모델·디바이스 벤치), **QNN/QAIRT**(NPU 런타임), **Genie → GenieX**(LLM 런타임, 2026-06 개발자 프리뷰; llama.cpp 또는 QAIRT 백엔드) | — | — | K38 🔍 |

`분석` — "온디바이스 LLM 특화 장치"라는 별도 라인은 없고, **NPU TOPS·메모리가 큰 Dragonwing IQ9(QCS9075)와 QCS8550 키트, 그리고 Snapdragon X·8 Elite 계열**이 그 역할을 한다. 차량용 ADP는 같은 Hexagon NPU를 쓰지만 LLM 공개 수치가 가장 적다.

### 2-2. 보유 보드 기준선

| 보유 보드 | CPU / GPU / NPU | RAM·저장 | 카메라·디스플레이 | 비고 | 출처 |
|---|---|---|---|---|---|
| SA8155P (ADP) | 4세대 Kryo 8코어, Adreno 640, Hexagon 696; **TOPS 비공개**(8295 출시 보도의 "8배"로 역산하면 ≈4 TOPS ⚠️) | 12 GB LPDDR4X, 128 GB UFS | 최대 8 GMSL, 5 mini-DP | 2019 세대 콕핏, SW 미포함 | K1 K2 K7 🏷️📰 |
| SA8255P (ADP, Ride SX 4.0) | Kryo Gen-6, Adreno 663, Hexagon HTP(quad HVX + dual HMX); **TOPS 비공개** | 36 GB LPDDR5(6ch), 2×128 GB UFS + NVMe | 4× MIPI-CSI, 2× DSI + 4× DP | SA8775P와 같은 보드 폼팩터, US$4,999 | K3 K4 🏷️ |
| SA7255P | **공개 사양 없음** ⚠️ | — | — | 엔트리 콕핏 추정 | K5 |
| **Dragonwing IQ-9075 EVK** | Kryo 8코어 2.36 GHz, Adreno 663, **NPU 50 또는 100 밀집 INT8 TOPS**(PMIC 2/4 변종) | **36 GB LPDDR5-3200(ECC)**, 128 GB UFS | Wi-Fi 6E, 2.5 GbE | Ubuntu 지원, 10년 공급; **보유 보드 중 LLM에 가장 적합** | K35 K36 🔍 |

### 2-3. 상위 후보 — 차량용 (같은 라인 안에서 올라가기)

| 보드 | NPU·사양 | 사례(연구·산업) | LLM 공개 수치 | 가격·입수 | 출처 |
|---|---|---|---|---|---|
| **SA8295P ADP** | Kryo 695, Adreno 695, 듀얼 Hexagon HTP; 30 TOPS(2021 보도) vs **"최대 60 TOPS"**(TechInsights 2025) ⚠️ | 양산: Lynk & Co 900·Zeekr(듀얼), **Mercedes 2024 E-Class(듀얼)**, Leapmotor; Nexa AI AutoNeural VLM(SA8295P NPU, TTFT 14× 개선 주장) | **Llama 3.2 1B w4 11.0 tok/s**(AI Hub Genie) | **US$6,300**(열 인클로저 US$6,500, GMSL2 카메라 키트 US$799), 승인 필요 | K7 K8 K13 K12 K10 K11 K9 🏷️📰🔍 |
| **SA8775P Ride Flex ADP** | Kryo Gen-6, Adreno 663, HTP, ASIL-D 세이프티 아일랜드; 공식 TOPS 없음, 변종 **72/96/144/192 TOPS**(Autohome) ⚠️ | 양산: Neta, Buick 至境 L7, Arcfox, Dongfeng Nissan N6(8개 프로그램); **Hyundai Mobis·HL Klemove** 채택 | AI Hub에 **Qwen3-8B·Qwen3-VL-8B w4a16** 빌드 등록(tok/s 미공개); DDRNet23 51 ms(8775) vs 58 ms(8295) | **US$4,999**(SA8255P와 같은 Ride SX 4.0 보드) | K17 K18 K21 K22 K19 K20 K4 🏷️📰🔍 |
| QAM8397P Cockpit Elite / QAM8797P Ride Elite | Oryon CPU, Hexagon NPU "12×"; **공식 TOPS 없음**(중국 보도 320 / 1,280 TOPS ⚠️) | **Visteon: Qwen 7B 온디바이스**(CES 2026), Banma Yan AI(Qwen)·AutoOmni 23B-A3B, Garmin, Mercedes·Li Auto 채택 | — | **ADP 미발견** ⚠️(파트너 경로) | K24 K25 K26 K27 K28 🔍📰 |
| (참고) SA8255P 위 LLM 사례 | — | **Desay SV + ModelBest 1.2B** 음성 모델, 첫 응답 <300 ms; Elektrobit 콕핏 레퍼런스 | — | 보유 보드로 재현 가능한 유일한 공개 사례 | K29 K31 📰 |

### 2-4. 상위 후보 — Dragonwing·기타 (생성 AI 성능으로 올라가기)

| 보드 | NPU·사양 | 사례·벤치 | 가격·입수 | 출처 |
|---|---|---|---|---|
| **IQ-9075 EVK**(보유) | QCS9075: NPU **최대 100 INT8 TOPS**, 36 GB LPDDR5 | 퀄컴 브리프 "**13B 모델 12 tok/s**"(모델명 미기재); Radxa Q900(QCS9075) **Llama 3.2 3B ≈19.4 tok/s**; GenieX 원격 테스트 플랫폼에 QCS9075 포함, Qwen3-8B GENIEX 행 등록; Innodisk COM-HPC 모듈 | **€825(DigiKey)** | K35 K36 K37 K38 K39 🔍🏷️ |
| IQ-8275 EVK | NPU 20/40 INT8 TOPS, LPDDR5x 최대 32 GB(EVK 6 GB), −40~125 °C | Arduino VENTUNO Q 채택 | — | K40 🔍 |
| QCS8550 키트(Thundercomm TurboX C8550 / Lantronix Open-Q 8550CS) | 4 nm, Adreno 740, **48 INT8 / 12 FP16 TOPS**, 8/16 GB LPDDR5x, Wi-Fi 7 | 엣지 AI 박스·멀티카메라 | C8550 €1,490; Open-Q 8550CS 데브킷 US$1,500 | K46 K47 🏷️ |
| RB3 Gen 2(QCS6490) / RB5(QRB5165) | 12 TOPS / 15 TOPS | 로봇·ROS 2(RB5) | US$399–599 / US$485–695 | K44 K45 📰 |
| **Snapdragon 8 Elite HDK** | 모바일 플래그십 NPU(TOPS 비공개); 8 Elite Gen 5는 INT2·FP8, LLM 220 tok/s 주장(모델 미기재) | Llama 3.2 3B ≈10 tok/s(Genie); AI Hub Llama 3 8B·Qwen3-8B 등록 | **US$1,499**(Lantronix) | K54 K55 K56 K57 🏷️📰 |
| Snapdragon X Elite / X2 Elite | NPU 45 / **80 TOPS**, 32 GB급 | 온디바이스 RAG 논문(X Elite NPU: 임베딩 9.1×, 에너지 12.3× 절감) | 데브킷 취소 → Copilot+ 노트북 | K49 K50 K51 K52 📰📄 |

`분석` — IQ-9075(100 TOPS, 36 GB)는 NPU 연산량·메모리에서 보유 차량용 보드를 이미 넘고, 퀄컴이 LLM 개발 플랫폼으로 밀고 있다(GenieX 원격 테스트 대상). **"차량과 같은 칩"이 필요하면 SA8775P ADP(US$4,999, Qwen3-8B 빌드 존재), "LLM 성능"이 필요하면 IQ-9075를 먼저 쓰고 8 Elite HDK로 확장**하는 순서가 합리적이다. 퀄컴 NPU 연구 논문은 대부분 모바일(8 Gen 3·X Elite)에서 나왔고 "NPU가 항상 빠르지 않다"(프리필은 CPU 우세)는 결과도 있다 [K59][K60] 📄.

---

## 제안 구성 (사례 기반)

| 목적 | 구성 | 근거 사례 |
|---|---|---|
| Thor 벤치 → 실차 | 데브킷(240 W PD) + Lattice HSB + Leopard GMSL2 디시리얼라이저(US$388) + GMSL2 카메라 4대 + J47 CAN 트랜시버 → 실차 단계에서 Seeed J601 캐리어(GMSL2 8·CAN FD·5G B-key) 또는 Leopard Thor 박스(US$8,500) | J43 J50 J28 J26 |
| Thor 연구 주제 | FlashDrive 방식 Alpamayo 가속을 Thor에서 재현·절대 지연 공개(미공개 값), 메모리 바운드 분석(VLA-Perf) 검증 | J1 J5 J3 |
| 퀄컴 현 보유 활용 | IQ-9075에 GenieX/AI Hub Qwen3-8B·Llama 3.2 3B 올려 tok/s·전력 측정; SA8255P ADP에는 ModelBest 1.2B급 음성 모델 재현 | K36 K37 K38 K29 |
| 퀄컴 업그레이드 | 1순위 SA8775P ADP(US$4,999, 차량 ASIL-D·Qwen3-8B 빌드, Mobis·Klemove 채택) → 2순위 8 Elite HDK(US$1,499, LLM 공개 수치 多) → SA8295P ADP는 양산 콕핏 재현 목적일 때만(US$6,300) | K19 K22 K55 K9 |

## 미확인·주의

- Jetson Thor를 실제 도로 차량에 올린 논문·FlashDrive의 Thor 절대 지연·MIIVII APEX THOR 사양/가격·Thor 캐리어 다수의 가격 미확인 ⚠️.
- Leopard HSB 카메라의 Thor 호환 표기 "N/A", e-con 10 GbE 카메라의 데브킷 연결 경로, Quectel 5G·GNSS·LiDAR 드라이버의 JetPack 7 검증 보고 없음 ⚠️.
- 퀄컴 공식 TOPS는 IQ·QCS 계열만 공개하고 SA/QAM 계열은 비공개. SA7255P·SA8650P 사양, Cockpit/Ride Elite ADP, AI Hub의 8775/9075 tok/s 수치 미확보 ⚠️.
- 가격은 변동이 크다(Thor 데브킷 +57%).
