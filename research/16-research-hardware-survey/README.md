# 16. 차량용 AI 연구 — 무엇을 연구하고, 무엇을 갖춰야 하나

차량에서 진행 중인 AI 연구를 a) 자율주행 / b) 온디바이스 AI로 나눠 사례 → 카테고리로 정리하고, 각 카테고리의 연구(또는 변형 연구)에 필요한 하드웨어·부자재 조합을 제시한다. 자율주행은 시뮬·녹화 데이터 / 실차 탑재 두 갈래. 외부 출처만 사용.

## 문서 목록

| 문서 | 내용 |
|---|---|
| [research-topics-and-hardware.md](research-topics-and-hardware.md) | **2판(주 문서)** — 연구 후보 6개와 장비 세트, Part A 자율주행(연구 사례·카테고리 A1–A5 → 시뮬/녹화·실차 두 갈래 장비 조합), Part B 온디바이스 AI(B1–B5 → 벤치/실차 장비 조합), 사례에 없는 제안(💡 퀄컴 NPU 등), 후보→장비 매핑 |
| [jetson-agx-thor/](jetson-agx-thor/jetson-agx-thor-guide.md) · [웹 버전](jetson-agx-thor/jetson-agx-thor-guide.html) · [메일용](jetson-agx-thor/mail-report.md) · [메일용 웹](jetson-agx-thor/mail-report.html) | **후속편(Jetson AGX Thor 전용, 2026-10-15, 보고서 형식)** — ① 데브킷 사양(128 GB·273 GB/s, QSFP28 HSB 카메라 입력, CSI 커넥터 없음, CAN 헤더, 240 W PD) ② 차량 관련 연구 사례와 부자재(FlashDrive Thor 3,770→944 ms, VLA-Perf π0 52.6 ms 메모리 바운드, Orin vs Thor 1.4×, RidgeRun BEV, 텔레리안·Advantech·Leopard·Connect Tech·Seeed GMSL2 8채널 캐리어) ③ 카메라 연결 방법(Holoscan Sensor Bridge 설명·공식 그림, A-1/A-2/A-3 HSB 경로와 B CSI 경로 도식, GMSL vs HSB 추세); 연구 사례에 Qwen-Drive-1.0·Alpamayo 연구 계보(사용 하드웨어) 포함 ④ 참고: DRIVE AGX Thor. 출처 44건 |
| [jetson-thor-qualcomm-boards/](jetson-thor-qualcomm-boards/jetson-thor-qualcomm-boards.md) · [웹 버전](jetson-thor-qualcomm-boards/jetson-thor-qualcomm-boards.html) · [메일용](jetson-thor-qualcomm-boards/mail-report.md) · [메일용 웹](jetson-thor-qualcomm-boards/mail-report.html) | **후속편(보드 특정, 2026-10-15)** — Jetson AGX Thor 데브킷 구매 전제: Thor를 쓴 차량 관련 연구(FlashDrive·VLA-Perf·BEV 벤치)와 차량 산업 사례(Thor 기반 GMSL2/CAN FD 박스 PC·캐리어; 로봇·산업 장비 사례 제외), 데브킷에 붙이는 부자재(HSB·GMSL2 디시리얼라이저·CAN 헤더·전원·캐리어). 퀄컴 보유 보드(SA8155P/8255P/7255P ADP, IQ-9075 EVK) 대비 상위 보드: 라인업 설명(차량용 ADP / Dragonwing IQ·QCS / Snapdragon X / 모바일 HDK), SA8295P·SA8775P ADP, QCS9075·QCS8550·8 Elite HDK와 사례. 출처 90건은 [하위 폴더 reference](jetson-thor-qualcomm-boards/reference/references.md) |
| [mail-01-plan.md](mail-01-plan.md) | **메일용 ① 조사 계획 공유** — 1. 자율주행 연구별 하드웨어(E2E/VLA·인식·데이터 수집·엣지 배포) 2. 시뮬레이터/실차 상황별 3. 온디바이스 AI 연구별(콕핏·엣지 LLM·하이브리드·에이전트·AD 컴퓨트 공유) 구조와 각 항목에 들어갈 내용 예고 |
| [mail-02-report.md](mail-02-report.md) | **메일용 ② 조사 결과** — 위 구조 그대로 사례 소개 + 하드웨어 소개(Thor/Orin 사양 비교, 서버급 연구차량, 실차 VLA 부자재, 퀄컴 ADP 제안 등), 핵심 출처 요약 |
| [research-hardware-survey.md](research-hardware-survey.md) | **1판(장비 카탈로그)** — 칩 비교표 19종(연구용 입수 경로 포함), 주변 장비 표, 3단계 구매 조합, 미확인 사항 |
| [reference/references.md](reference/references.md) | 출처 목록(ID 접두어 N·Q·X·M·S·V·O·P, 총 118건) — 제목·URL·날짜·등급. 1판·2판 공용 |

## 작성 규약

- **저장소의 기존 문서를 참고하지 않았다.** 외부 공개 자료(제품 페이지·README·모델카드·논문·포럼·언론)만 사용했고, 기존 보고서로의 링크·재인용이 없다.
- 모든 사실 문장에 출처 ID와 등급(🔍 공식 / 📄 논문 / 📰 언론·2차 / 💬 포럼 / ⚠️ 미확인·충돌)을 붙였다. 💡는 사례에 없는 **제안**(출처 없음, 판단)이다. TOPS는 정밀도를 병기하고, 가격은 조사일 공개 표시가(표시 통화 그대로)다.
- 조사 환경 제약으로 GitHub·PyPI만 직접 열람(✅)했고, 나머지는 검색 엔진 본문 발췌로 확인했다.

## 스크립트

- `scripts/md2html.py` — 보고서 `.md`와 `reference/references.md`를 받아, 본문의 출처 ID(`[J1]`, 표의 출처 열)를 원문 URL로 연결한 자체 완결 HTML(목차·스크롤 스파이·다크 모드)을 만든다. `pip install markdown` 후 `python3 -I scripts/md2html.py <md> <references.md> <out.html>`.
