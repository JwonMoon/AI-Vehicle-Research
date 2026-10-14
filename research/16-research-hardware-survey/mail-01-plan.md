# [메일용] 차량용 AI 연구 장비 조사 — 계획 공유

> 작성일 2026-10-14. 장비 구입 전에 "비슷한 연구·업체가 실제로 어떤 하드웨어를 쓰는지"를 연구 유형별로 조사하겠다는 계획입니다. 괄호 안은 각 항목에 들어갈 내용의 예고입니다.

## 1. 자율주행 연구별 하드웨어

- **E2E/VLA 주행 모델** → 사례 소개 + 하드웨어 소개
  (공개 모델 Alpamayo·Qwen-Drive와 양산 사례 Li Auto·Xpeng·DriveVLM 논문. 연구는 24 GB급 GPU, 양산은 차량 SoC로 흐름이 나뉨. NVIDIA Thor 계열과 Orin 계열로 나눠 연산량·메모리·정밀도 사양을 간단히 비교)
- **인식·데이터 수집** → 사례 소개 + 하드웨어 소개
  (대학 연구차량 UB·TUM·KIT, NVIDIA Hyperion, 로보택시 사례. 여기는 임베디드 보드보다 서버급 x86 PC + 데스크톱 GPU를 많이 쓴다는 점을 강조. 멀티카메라·LiDAR·GNSS/INS 센서 구성과 차량 신호·제어를 받기 위한 DBW(Drive-by-Wire)·CAN 인터페이스가 특징)
- **엣지 배포·지연 최적화** → 사례 소개 + 하드웨어 소개
  (TensorRT-Edge-LLM VLA 예제, FlashDrive 가속 논문, Orin vs Thor 특성화 논문. Jetson AGX Thor / Jetson AGX Orin / DRIVE AGX Thor의 차이와 연구용 입수 경로·가격)

## 2. 자율주행 — 시뮬레이터 / 실차 탑재 상황별 하드웨어

- **시뮬레이터·녹화 데이터로 진행할 때**
  (서버·워크스테이션 GPU로 학습, CARLA·Bench2Drive·NAVSIM·MORAI 시뮬레이터, 엣지 배포 검증용 보드(Thor·Orin) 1대. 개루프 지표와 폐루프 점수의 상관이 낮다는 최근 연구도 짚음)
- **실차에 탑재해 주행할 때 (VLA 기준)**
  (카메라·센서(GMSL2 카메라 4~7대, HDR), 인터페이스(GMSL 디시리얼라이저, CAN FD 어댑터, DBW 키트, 자동차 이더넷 변환기), 전원(12 V DC-DC, 보드별 소비 전력), 기타(마운트·냉각·전력 계측·5G 모듈)와 공개 가격)

## 3. 온디바이스 AI 연구별 하드웨어

- **콕핏 어시스턴트 SLM/VLM** → 사례 소개 + 하드웨어
  (Cerence CaLLM Edge, Visteon Qwen 7B on Cockpit Elite, Banma·Xpeng 30B급, FEV Phi-4-mini, Lynk & Co 900·Zeekr 9X 듀얼 8295. 양산은 퀄컴 콕핏 SoC가 주류이고 연구는 Jetson 위주. 보드 외에 마이크 어레이·스피커·디스플레이·실내 카메라·LTE/5G까지 부자재 포함)
- **엣지 LLM/VLM 최적화** → 사례 소개 + 하드웨어
  (TensorRT-Edge-LLM 공식 벤치, Jetson Orin 전력 모드별 LLM 측정 논문, Qualcomm AI Hub 8295 수치. Jetson Orin 64 GB / Jetson Thor / DGX Spark / 퀄컴 ADP의 정밀도 지원과 tok/s, 전력 계측 도구)
- **엣지 ↔ 클라우드 하이브리드** → 사례 소개 + 하드웨어
  (Li Auto Mind GPT-3o, Cerence xUI, FEV 오프라인 폴백, AWS 인-비히클 어시스턴트 가이드, 엣지-클라우드 투기 디코딩 논문. 엣지 보드 + 호스트 GPU(RTX PRO 6000 / DGX Spark) + 유선 10 GbE 또는 5G 모듈)
- **에이전트·툴 사용(차량 데이터)** → 사례 소개 + 하드웨어
  (Peykan MCP-CAN 서버, KUKSA/VSS, Android VHAL, Pi + CAN HAT 테스트베드. CAN/OBD-II 접근이 특징이라 가상 CAN으로 시작해 CAN FD 어댑터·OBD 커넥터로 확장. 쓰기는 안전상 기본 차단)
- **AD와 컴퓨트 공유·통합** → 사례 소개 + 하드웨어
  (NIO 4× Orin-X 중 256 TOPS를 콕핏 모델에 공유, MediaTek 콕핏 SoC + DRIVE AGX, Qualcomm Ride Flex 콕핏+ADAS 단일 SoC. 연구실 재현은 Jetson 1대 분리 실험 → 2보드(Jetson + 퀄컴 ADP) 구성 제안)

## 산출물·원칙

- 결과는 같은 구조로 정리한 조사 보고(메일 본문 + 저장소 문서). 모든 수치에 출처와 등급(공식/논문/언론/포럼/미확인)을 붙이고, 사례에 없는 제안은 "제안"으로 구분합니다.
- 가격은 조사일 공개 표시가(USD 등 표시 통화)만 적고 환산하지 않습니다.
