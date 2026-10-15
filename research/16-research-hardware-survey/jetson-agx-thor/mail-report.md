# [메일용] Jetson AGX Thor로 자율주행 연구하기 — 사양 · 연구 사례와 부자재 · 카메라 연결 방법

> 작성일 2026-10-15. 외부 공개 자료만으로 조사(저장소 기존 문서 미참고). 등급: 🔍 공식 / 📄 논문 / 📰 언론 / 💬 포럼 / 🏷️ 벤더 / ⚠️ 미확인. 괄호 ID는 [출처 44건](reference/references.md). 그림과 상세 표는 [본 보고서](jetson-agx-thor-guide.md) 참조.

## 0. 한 줄 요약
- 데브킷은 **128 GB·FP4/FP8이 강점, 메모리 대역폭(~270 GB/s)이 병목**. VLA·LLM은 Thor에서도 메모리 바운드, INT8은 FP16보다 느릴 수 있음 [T9][T7].
- 주행 VLA(Alpamayo 10B)는 **Thor에서 최적화 후에도 약 1 Hz**(3,770→944 ms). 소형 VLA(π0 2.7B)는 52.6 ms/19 Hz(분석 모델) [T8][T9]. Qwen-Drive(4B)는 Thor 수치 없음 [T37].
- 데브킷에는 **GMSL2 커넥터도 CSI 커넥터도 없음** → 카메라는 QSFP28로 들어오는 **Holoscan Sensor Bridge(HSB)** 가 공식 경로. GMSL2 카메라는 HSB 앞단에 디시리얼라이저(TauroTech DA326 / Leopard 키트)를 두면 됨 [T23][T26][T19].
- 차량 산업의 Thor는 **DRIVE AGX Thor**(GMSL2 16ch 내장). Jetson Thor 실차 논문은 아직 없고, "GMSL2 8ch + CAN FD" 캐리어/박스가 차량용 진입점 [T33][T18][T21].

## 1. 데브킷 사양 요약
- **컴퓨트**: T5000, Blackwell 2,560 CUDA, 14× Neoverse-V3AE, 2,070 FP4 TFLOPS(희소), 40–130 W [T1]
- **메모리**: 128 GB LPDDR5X, **273 GB/s** [T1][T11]
- **카메라 입력**: QSFP28(4×25 GbE) → **HSB 카메라 최대 20대**. 모듈은 CSI 16레인이지만 **데브킷 캐리어에 CSI 커넥터 없음**(Stereolabs 문서) ⚠️ [T1][T23]
- **네트워크·확장**: RJ45 5 GbE, Wi-Fi 6E(M.2 E), NVMe 1 TB(M.2 M). **M.2 B-key(5G) 없음** [T1]
- **CAN**: J47 헤더 2채널(CAN FD), **외부 트랜시버 필요** [T2]
- **전원**: 240 W USB-C PD 동봉(28 V 5 A). 차량 12 V→28 V PD 어댑터 미확인 ⚠️ [T3]
- **SW**: JetPack 7.0(CUDA 13) → 7.1(TensorRT-Edge-LLM, Thor HSB 정식) → 7.2(SIPL 카메라, MIG 프리뷰) [T4][T31]
- **가격**: US$3,499(2025-08) → **US$5,499(2026-07)** [T5]. DRIVE AGX Thor와 별개 제품 [T36]

## 2. 연구 사례와 부자재
### 2-1. 주행 VLA 추론
- **FlashDrive**(Z Lab, 2026-08) [T8] 📄: Alpamayo 10B를 KV 캐시 재사용·투기 추론·W4A8로 가속. RTX PRO 6000 717→151 ms(4.7×), **Thor 3,770→944 ms(4.0×)** → Thor에서는 아직 ~1 Hz. 부자재 없음(클립 재생)
- **Alpamayo 연구들의 하드웨어** [T45][T42][T40][T41][T44] 📄🔍: 공식 요구 ≥24 GB(테스트 RTX 3090/A100/H100; 1.5는 BF16 20.65 GB·FP8 9.94 GB·W4A16 6.9 GB, 2 Super 34B는 H100만). 연구별 — FlashDrive: Thor+3090/4090/5090/PRO 6000 · 지연 분석(RTCSA 2026): **DGX Spark 128 GB**, −69% · OOM-Free(국민대): **RTX 5070 Ti 16 GB** 스와핑 3.55× · Stanford PiDrive: **Jetson Thor 0.5 Hz** ⚠️ · TIER IV: Autoware 통합, 실차는 DRIVE AGX Thor ×2 [T43]. 세 층(24 GB+ 워크스테이션 / 128 GB 통합메모리 엣지 / 16 GB 스와핑), Jetson Thor 실차 사례 없음
- **Qwen-Drive-1.0**(Alibaba×HUST, 2026-09) [T37] 📄: Qwen3.5-4B + BEV 헤드 + 플래닝 전문가, NAVSIM PDMS 90.7. 24 GB+ GPU 권장(bf16 ≈12 GB). **Thor·Jetson·양자화 수치 없음** ⚠️ → Thor 측정이 첫 공개 결과. 논문 논리는 "콕핏+주행 한 컴퓨트 공유"; Alibaba는 인캐빈 Qwen-Omni를 DRIVE AGX Thor에 적응 중 [T38] 📰
- **TensorRT-Edge-LLM Alpamayo 예제**(NVIDIA) [T13] 🔍: FP16만 지원, Thor 지연 수치 미공개, FP16 엔진 OOM 포럼 보고 💬
### 2-2. Thor 하드웨어 특성
- **VLA-Perf**(NVlabs) [T9] 📄: 루프라인 예측 — π0 Thor 52.6 ms(19 Hz), Orin 93.8 ms. Thor는 **세 단계 모두 메모리 바운드** → 바이트 수(양자화·캐시)를 줄여야 빨라짐
- **Action Generation Bottleneck**(Google/Purdue) [T10] 📄: Orin vs Thor, 지연의 75%가 메모리 바운드 액션 생성, Thor 연산 5배지만 E2E 1.4배
- **VLA across XPUs**(SJTU, ICML 2026) [T11] 📄: 연산 바운드 VLM → 메모리 바운드 액션 전문가 패턴, DP-Cache 1.29×
- **GTR**(DRIVE AGX Thor) [T14] 📄: 밀집 예측 백본도 대역폭 지붕 근처 → 커널 융합으로 메모리 트래픽 제거
- **양자화 주의** [T7] 💬: Thor에서 INT8이 FP16보다 느린 사례 다수(MiDaS 5.8 vs 10.3 ms). FP8/FP4로 재양자화
### 2-3. 멀티카메라 BEV
- **RidgeRun 벤치** [T12] 🏷️: Thor 출력 HD 4입력 ≈328 fps, 4K 6입력 ≈65.6 fps; 1080p 4입력 처리 5.9 ms → 6카메라 서라운드 뷰는 10 ms 안쪽
### 2-4. 부자재가 드러난 사례
- **텔레리안 AVS300**(한국, 2026-05): Thor 러기드 플랫폼, **GMSL2 8ch 직결**, 프레임 싱크·PPS 시간동기, HSB 플랫폼 개발 [T17] 📰
- **Advantech × SENSING**(2025-12): Thor 박스 MIC-742-AT에 GMSL 카메라 통합(SerDes·BSP 검증), **8× GMSL2 + 4× CAN FD** [T18] 🔍
- **Leopard Imaging**: 데브킷용 GMSL2 디시리얼라이저 키트(MAX9296, 1ch, US$388), Thor 박스(8× GMSL2, US$8,500) [T19] 🏷️
- **Connect Tech**: Gauntlet 캐리어 + GMSL2/3·FPD-Link 브레이크아웃, 4× CAN; JCB022(8× GMSL2, T5000) [T20] 🏷️
- **Seeed J601 / Forecr / Firefly / Syslogic**: 8× GMSL2·CAN FD·19–48 V 등 차량용 캐리어·박스 [T21] 🏷️
- **e-con**: 10G Holoscan 카메라(e-CAM85 US$469), ISX031 HDR·IMX900 GS [T22] 🏷️ · **Ouster** REV8 LiDAR Thor 드라이버 [T25] 🔍 · **Stereolabs**: 데브킷은 USB3 ZED만, GMSL2는 캐리어 필요 [T23] 🏷️
- 실차에 Jetson Thor를 올려 센서 전체를 공개한 사례: **없음** ⚠️. 패턴은 "차량용 = GMSL2 8ch + CAN FD 캐리어/박스, 데브킷 = HSB 벤치"

## 3. 데브킷에 카메라 붙이는 법
### 3-1. Holoscan Sensor Bridge(HSB)란
- NVIDIA 오픈소스(Apache-2.0) **센서→GPU 이더넷 브리지**: FPGA가 센서 데이터를 UDP로 보내고 NIC가 GPU 메모리에 직접 기록 [T26] 🔍
- 공식 수치: 4K60 glass-to-glass 17 ms, Thor CoE 시 CPU ≈1%, PTP 1 µs [T27] 🔍
- Thor: 데브킷 QSFP28에 연결, JetPack 7.1부터 CoE 하드웨어 가속(7.2 정식) [T31]
- 보드: 레퍼런스 Lattice CertusPro-NX·Microchip PolarFire, 상용 e-con·Advantech·SENSING·TauroTech·Leopard [T28][T29]
### 3-2. 경로 (카메라 → 중간 부자재 → 데브킷 입력)
- **A-1 HSB + MIPI 카메라**: MIPI 모듈 → Lattice/Microchip HSB 보드(US$350) → QSFP28. 공식 절차, 케이블 짧아 벤치용 [T26][T28]
- **A-2 HSB + GMSL2 카메라** ★권장: GMSL2 카메라 → **TauroTech DA326**(디시리얼라이저+FPGA, NVIDIA 문서에 Thor 절차) 또는 **Lattice HSB + Leopard GMSL2 키트**(US$388) → QSFP28. 데브킷 유지하며 양산급 카메라 [T26][T19]
- **A-3 HSB 일체형 이더넷 카메라**: Leopard VB1940 Eagle(PoE) / e-con CUHSB(10 GbE) → 케이블만 → QSFP28 또는 RJ45. 부품 최소, 모델 한정 [T26][T22]
- **B GMSL→CSI 디시리얼라이저 보드**: Orin 정석이지만 **데브킷에 CSI 커넥터가 없어 불가**, 서드파티 캐리어에서만 ⚠️ [T23][T24][T20]
### 3-3. GMSL vs HSB — 특성과 추세
- GMSL2: 동축 한 가닥·PoC·10 m급, 보드 쪽 디시리얼라이저+CSI 필요(캐리어). 양산 차량 카메라 대부분 [T24]
- HSB: 이더넷 10/25 GbE, PTP 동기, FPGA 브리지 보드 + QSFP → 데브킷 그대로. Thor CoE 가속 [T26][T27]
- 추세: Orin까지 "캐리어+GMSL2" 표준 → Thor부터 NVIDIA가 데브킷 입력을 HSB로 통일 → 벤더는 **GMSL2→HSB 변환 보드**와 **GMSL2 내장 캐리어** 두 갈래. 2025-26 신제품 다수(e-con, Leopard, Advantech, Microchip Rev 2.0, 텔레리안) [T19][T30]
- 권장: 벤치는 A-2로 GMSL2 카메라 2~4대, 6대 이상·차량 탑재는 GMSL2 8ch 캐리어
### 3-4. 그 외 부자재
- CAN 트랜시버(J47) [T2] · 이더넷 LiDAR(RJ45/QSFP 브레이크아웃) [T25] · 5G는 USB 모뎀 또는 B-key 캐리어 ⚠️ [T32] · 차량 전원은 캐리어 DC 직입력 권장 ⚠️ [T3][T21] · 마운트 홀 없음 [T32]

## 4. 참고 — 차량 산업의 DRIVE AGX Thor
- 완성차·L4(TIER IV×Isuzu, Li Auto i8 Thor-U, Zeekr 9X, Hyperion 10)는 **DRIVE AGX Thor** [T33][T34]
- DRIVE DevKit: 64 GB, **16× GMSL2 + 2× GMSL3 내장**, 350 W, SKU 10/12, DriveOS 7, 가격 비공개·프로그램 승인 [T33]
- Jetson과 차이: 메모리·카메라 인터페이스·SW·구매 경로. 모델 결과는 이전 가능, 카메라 배선은 재설계 [T36]

## 5. 미확인·주의
- FlashDrive Thor 수치는 프로젝트 페이지 발췌, VLA-Perf는 분석 모델 예측(실측은 더 느림) ⚠️
- 데브킷 CSI 커넥터: 제품 페이지 "CSI 6대"(모듈 사양) vs Stereolabs "캐리어에 없음" 충돌 → 캐리어 사양으로 해석 ⚠️
- Leopard·Microchip의 Thor 지원 표기("설계상 호환", "드라이버 보장 없음")는 구매 전 확인 ⚠️. 가격 변동 큼(+57%)
