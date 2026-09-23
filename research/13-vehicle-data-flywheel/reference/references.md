# 출처 목록 — 자율주행 데이터 플라이휠

작성일 2026-09-22. 보고서 본문(그림 설명 포함)에 인라인으로 붙인 출처 전부(103건)를 처음 쓰인 장 순서로 모았다. 등급은 본문에서 그 출처 앞에 붙인 표시와 같다: 🔍 1차 출처 원문 직접 확인(GitHub raw README·공식 문서·저장소 파일) · ✅ 복수 출처 교차 확인 · 📰 웹 검색 요약·보도만 확인(원문 미열람) · ⚠️ 미확인·회사 주장("공개 주장"). 같은 출처가 여러 장에 쓰였으면 "다른 장" 열에 표시했다. 그림 파일의 출처·라이선스는 [images.md](images.md)에 따로 정리했다.

**조사 환경 제약.** 세션 네트워크 정책상 arxiv.org·huggingface.co·nvidia.com 계열·tesla.com·waymo.com·wayve.ai·mobileye.com과 대부분의 언론 사이트 원문에 직접 접근할 수 없었다. 직접 열람한 것은 GitHub 저장소(raw.githubusercontent.com·github.com) 문서와 파일뿐이며, 나머지는 웹 검색 결과 요약을 근거로 삼았다(📰). 📰 항목의 URL은 독자가 원문을 확인할 수 있도록 적은 것이고, 조사 시점에는 열람하지 못했다. 접근 실패 목록은 문서 끝에 있다.


## 1장

| # | 출처 | 등급 | 뒷받침하는 내용(본문 발췌) | 다른 장 |
|---|---|---|---|---|
| 1 | [retaildogma](https://www.retaildogma.com/amazon-flywheel/) `retaildogma.com` | 📰 | 가격을 낮추면 고객이 늘고, 고객이 늘면 판매자와 상품이 늘고, 그러면 고객 경험이 좋아져 다시 고객이 는다  (retaildogma, feedvisor). |  |
| 2 | [feedvisor](https://feedvisor.com/resources/amazon-trends/amazon-flywheel-explained/) `feedvisor.com` | 📰 | 가격을 낮추면 고객이 늘고, 고객이 늘면 판매자와 상품이 늘고, 그러면 고객 경험이 좋아져 다시 고객이 는다  (retaildogma, feedvisor). |  |
| 3 | [NVIDIA Glossary](https://www.nvidia.com/en-us/glossary/data-flywheel/) `nvidia.com` | 📰 | NVIDIA 용어집은 "상호작용과 프로세스에서 모은 데이터로 AI 모델을 계속 개선하고, 그 모델이 더 좋은 결과와 더 가치 있는 데이터를 낳는 피드백 루프"라고 정의한다  (NVIDIA Glossary). 핵심은 두 가지다. |  |
| 4 | [Awesome Data-Centric AD README](https://raw.githubusercontent.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving/main/README.md) `raw.githubusercontent.com` | 🔍 | 2024년 학술 서베이는 자율주행의 폐쇄루프를 "(1) 데이터 수집 → (2) 저장 → (3) 선별·전처리 → (4) 라벨링 → (5) 모델 학습 → (6) 시뮬레이션·테스트 검증 → (7) 실세계 배포"의 반복으로 정의하고, Tesla·NVIDIA·Momenta·Horizon·Ba… |  |
| 5 | [릴리스 노트 인용](https://www.notateslaapp.com/software-updates/version/2024.3.20/release-notes) `notateslaapp.com` | 📰 | 2024년 3월 Tesla는 FSD v12 릴리스 노트에서 "도심 주행 스택을 수백만 개 영상 클립으로 학습한 단일 종단간(end-to-end) 신경망으로 바꾸고, 30만 줄 이상의 명시적 C++ 코드를 대체했다"고 썼다  (릴리스 노트 인용). 종단간이란 카메라 영상이 들어가면 조… |  |
| 6 | [Waymo 블로그](https://waymo.com/blog/2024/10/ai-and-ml-at-waymo/) `waymo.com` | 📰 | Waymo는 2024년 10월 "Waymo Foundation Model이 인지·예측·계획에 걸쳐 스택 전반의 성능을 끌어올리고 있다"고 밝혔다  (Waymo 블로그). 영국의 Wayve는 아예 "AV2.0"이라는 이름으로 센서 입력에서 주행 결정까지를 하나의 네트워크로 잇는 방식을… |  |
| 7 | [Wayve](https://wayve.ai/technology/) `wayve.ai` | 📰 | 영국의 Wayve는 아예 "AV2.0"이라는 이름으로 센서 입력에서 주행 결정까지를 하나의 네트워크로 잇는 방식을 내세운다  (Wayve). 오픈소스 openpilot도 2025년 8월 종방향 제어의 고전 제어기(MPC)를 월드모델 기반 종단간 계획으로 바꿨고, 2026년 3월에는 … |  |
| 8 | [openpilot RELEASES.md](https://raw.githubusercontent.com/commaai/openpilot/master/RELEASES.md) `raw.githubusercontent.com` | 🔍 | 오픈소스 openpilot도 2025년 8월 종방향 제어의 고전 제어기(MPC)를 월드모델 기반 종단간 계획으로 바꿨고, 2026년 3월에는 "학습된 시뮬레이터로 전량 학습한" 주행 모델을 배포했다  (openpilot RELEASES.md). | 3장, 4장 |
| 9 | [OpenDriveLab/End-to-end-Autonomous-Driving](https://github.com/OpenDriveLab/End-to-end-Autonomous-Driving) `github.com` | 🔍 | 그림 출처: 학계 서베이가 정리한 고전 파이프라인(a: 인지 → 예측 → 계획을 사람이 정한 인터페이스로 잇는다)과 종단간 패러다임(b: 모듈 사이를 학습으로 잇고 역전파로 함께 고친다). 맨 아래 "미래 과제"에 데이터 엔진(Data Engine)이 들어 있다. |  |
| 10 | [Li et al. 2024 서베이 저장소](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) `github.com` | 🔍 | 그림 출처: 주행 시나리오의 빈도 분포. 도심 직진 같은 상황이 90%를 차지하고, 안개·폭우 야간 같은 상황은 1% 아래의 긴 꼬리에 있다. | 2장, 3장, 4장 |
| 11 | [arXiv 2510.26125](https://arxiv.org/abs/2510.26125) `arxiv.org` | 📰 | 일상 주행에서 발생 빈도 0.03% 미만인 상황만 골라 4,021개 구간(약 12시간)을 모았고, 평가 지표도 "기록된 궤적과 얼마나 가까운가"가 아니라 "사람 평가자가 선호한 궤적에 얼마나 가까운가"(RFS, Rater Feedback Score)로 바꿨다  (arXiv 2510.… |  |
| 12 | [Waymo 비교 연구](https://waymo.com/research/comparison-of-waymo-rider-only-crash-data-to-human/) `waymo.com` | 📰 | 미국에서 사람 운전자의 부상 신고 충돌은 100만 마일당 2.80건이다  (Waymo 비교 연구). 100만 마일에서 세 번 남짓 일어나는 사건을 줄이려면, 100만 마일 중 99.99%를 잘하는 것으로는 부족하고 나머지 0.01%에서 무엇을 하는지가 결정한다. |  |
| 13 | [보도](https://www.carswithcords.net/2020/07/tesla-and-long-march-of-nines-to-full.html) `carswithcords.net` | 📰 | 신뢰도 99%에서 99.9%, 99.99%로 9를 하나씩 더 붙일 때마다 남은 예외 상황을 처리해야 하고, 그 예외가 곧 롱테일이다  (보도). |  |
| 14 | [arXiv 1912.04838](https://arxiv.org/pdf/1912.04838) `arxiv.org` | 📰 | Waymo Open Dataset 논문(2020)은 샌프란시스코 도심 데이터로 학습한 3D 차량 검출기를 교외(피닉스·마운틴뷰)에서 평가하면 정확도 지표(APH)가 8.0 떨어지고, 교외로만 학습한 보행자 검출기를 도심에서 평가하면 19.8 떨어진다고 보고하며 이를 "뚜렷한 도메인 … |  |
| 15 | [BEVUDA](https://arxiv.org/pdf/2211.17126) `arxiv.org` | 📰 | 보스턴(우측통행)과 싱가포르(좌측통행)를 함께 담은 nuScenes 데이터셋을 두고도 "장면·날씨·밤낮"이 바뀔 때 적응 없이는 성능이 크게 떨어진다는 연구가 여럿이다  (BEVUDA, DA-BEV). |  |
| 16 | [DA-BEV](https://arxiv.org/pdf/2401.08687) `arxiv.org` | 📰 | 보스턴(우측통행)과 싱가포르(좌측통행)를 함께 담은 nuScenes 데이터셋을 두고도 "장면·날씨·밤낮"이 바뀔 때 적응 없이는 성능이 크게 떨어진다는 연구가 여럿이다  (BEVUDA, DA-BEV). |  |
| 17 | [Wayve](https://wayve.ai/thinking/multi-country-generalization/) `wayve.ai` | 📰 | Wayve는 영국(좌측통행)에서만 배운 모델을 미국에 그대로 가져갔을 때 처음에는 영국 수준에 못 미쳤고, 미국 데이터 100시간을 더하자 크게 좋아졌으며, 8주 동안 모은 500시간으로 영국 수준에 근접했다고 밝혔다  (Wayve). 새 시장에 들어갈 때마다 그 시장의 데이터를 모… |  |
| 18 | [IEEE](https://ieeexplore.ieee.org/abstract/document/10801619) `ieeexplore.ieee.org` | 📰 | 자율주행의 지속 학습에서도 보호 장치 없이 재학습만 하면 망각이 생긴다는 연구가 있다  (IEEE). |  |
| 19 | [발표 요약](https://dynamicallytyped.com/stories/2021/karpathy-autopilot-cvpr/) `dynamicallytyped.com` | 📰 | "섀도 모드로 배포 → 예측을 관찰 → 트리거를 조정해 새 데이터 수집 → 잘못된 예측을 '유닛 테스트'로 만들기 → 비슷한 예제를 데이터셋에 추가 → 재학습 → 반복". 당시 플릿에서 221개 트리거가 돌고 있었다  (발표 요약). 틀렸던 상황을 테스트로 남겨 두면 다음 모델이 그… | 3장 |
| 20 | [Waymo CAT](https://waymo.com/blog/2022/12/waymos-collision-avoidance-testing/) `waymo.com` | 📰 | Waymo도 새 소프트웨어를 낼 때마다 "테스트 트랙·실도로·합성 시나리오 전부를 시뮬레이션에서 다시 실행"하고, 충돌 회피 시나리오는 상대 차량의 위치·속도를 조금씩 바꿔 가며(fuzzing) 돌린다  (Waymo CAT). | 3장 |
| 21 | [RAND RR-1478](https://www.rand.org/pubs/research_reports/RR1478.html) `rand.org` | 📰 | 보고서의 결론은 "주행만으로는 안전에 도달할 수 없다(cannot drive their way to safety)"였다  (RAND RR-1478). |  |
| 22 | [Waymo Safety Impact](https://waymo.com/blog/shorts/waymo-safety-impact-update-170m/) `waymo.com` | 📰 | Waymo는 2026년 3월 기준 무인(rider-only) 누적 2억 2,060만 마일을 달렸고, 1억 7,070만 마일 분석에서 사람 대비 중상 이상 충돌 92% 감소, 에어백 전개 83% 감소, 보행자 부상 92% 감소를 보고했다  (Waymo Safety Impact). 독립… |  |
| 23 | [tesla.com/fsd/safety](https://www.tesla.com/fsd/safety) `tesla.com` | 📰⚠️ | Tesla는 FSD 누적 100억 마일을 공개했지만 충돌 집계 방식이 정부 데이터와 달라 독립 검증이 없다는 비판을 받는다  (tesla.com/fsd/safety, 비판). |  |
| 24 | [비판](https://cryptobriefing.com/tesla-fsd-safety-data-collision-reduction/) `cryptobriefing.com` | 📰⚠️ | Tesla는 FSD 누적 100억 마일을 공개했지만 충돌 집계 방식이 정부 데이터와 달라 독립 검증이 없다는 비판을 받는다  (tesla.com/fsd/safety, 비판). |  |
| 25 | [Ansys SOTIF 해설](https://www.ansys.com/simulation-topics/what-is-sotif) `ansys.com` | 📰 | 그 주요 수단이 시뮬레이션을 포함한 광범위한 검증이다  (Ansys SOTIF 해설). |  |
| 26 | [Simulation City](https://waymo.com/blog/2021/07/simulation-city/) `waymo.com` | 📰 | 그래서 Waymo는 실주행 2,000만 마일에 시뮬레이션 200억 마일 이상을 얹었고, 자체 시뮬레이터 Carcraft는 하루 800만~1,000만 마일을 달린다  (Simulation City, CACM 2018). 2026년 2월에는 Google DeepMind의 Genie 3 … |  |
| 27 | [CACM 2018](https://cacmb4.acm.org/magazines/2018/2/224621-a-comprehensive-self-driving-car-test) `cacmb4.acm.org` | 📰 | 그래서 Waymo는 실주행 2,000만 마일에 시뮬레이션 200억 마일 이상을 얹었고, 자체 시뮬레이터 Carcraft는 하루 800만~1,000만 마일을 달린다  (Simulation City, CACM 2018). 2026년 2월에는 Google DeepMind의 Genie 3 … |  |
| 28 | [Waymo 블로그](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/) `waymo.com` | 📰 | 2026년 2월에는 Google DeepMind의 Genie 3 기반 "Waymo World Model"로 플릿이 본 적 없는 상황(토네이도, 도로 위 코끼리)까지 만들어 시험한다고 밝혔다  (Waymo 블로그). | 4장 |

## 2장

| # | 출처 | 등급 | 뒷받침하는 내용(본문 발췌) | 다른 장 |
|---|---|---|---|---|
| 29 | [data-flywheel README](https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/README.md) `raw.githubusercontent.com` | 🔍 | "데이터 플라이휠은 생산 애플리케이션의 데이터 배기가스(예: LLM 프롬프트·응답 로그, 사용자 피드백, 전문가 라벨)를 사용해 생성형 AI 시스템의 정확도를 높이고 지연·비용을 줄이는 프로세스다"  (data-flywheel README). |  |
| 30 | [제한 사항](https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/docs/05-limitations-best-practices.md) `raw.githubusercontent.com` | 🔍 | README는 "플라이휠은 자동 조종 장치가 아니라 손전등"이라고 쓰고, 제한 사항 문서는 "이 플라이휠은 어떤 모델도 자동으로 승격·배포하지 않으며, 사용자 피드백도 받지 않는다"고 명시한다  (제한 사항, 구조 문서). 즉 여섯 단계는 후보를 찾아 점수를 매기는 데서 끝나고, 승… |  |
| 31 | [구조 문서](https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/docs/01-architecture.md) `raw.githubusercontent.com` | 🔍 | README는 "플라이휠은 자동 조종 장치가 아니라 손전등"이라고 쓰고, 제한 사항 문서는 "이 플라이휠은 어떤 모델도 자동으로 승격·배포하지 않으며, 사용자 피드백도 받지 않는다"고 명시한다  (제한 사항, 구조 문서). 즉 여섯 단계는 후보를 찾아 점수를 매기는 데서 끝나고, 승… |  |
| 32 | [arXiv 2510.27051](https://arxiv.org/abs/2510.27051) `arxiv.org` | 📰 | 3개월간 부정 피드백 495건을 모아 라우팅 오류 5.25%를 찾아냈고, 라우터를 70B 모델에서 미세조정한 8B 모델로 바꿔 정확도 96%에 지연 70% 감소를 얻었다  (arXiv 2510.27051). |  |
| 33 | [NVIDIA-AI-Blueprints/data-flywheel](https://github.com/NVIDIA-AI-Blueprints/data-flywheel) `github.com` | 🔍 | 그림 출처: NVIDIA가 공개한 데이터 플라이휠 블루프린트의 공식 구조도에 위 6단계의 번호를 표시한 것. ① 배포된 에이전트 앱의 로그가 Elasticsearch에 쌓이고 플라이휠 서버가 가져온다. ②③④ 서버가 작업별로 묶고 중복을 없애고 데이터셋을 만들어 Datastore에 … |  |
| 34 | [CleanTechnica](https://cleantechnica.com/2021/08/30/observations-on-teslas-ai-day/) `cleantechnica.com` | 📰 | Tesla가 2021년 AI Day에서 설명한 데이터 엔진  (CleanTechnica), NVIDIA·AWS가 2026년 3월 설명한 "AV 3.0 데이터 파이프라인"  (AWS 블로그, 요약만 확인), 그리고 학술 서베이의 7단계 폐쇄루프 . |  |
| 35 | [AWS 블로그, 요약만 확인](https://aws.amazon.com/blogs/industries/building-an-end-to-end-physical-ai-data-pipeline-for-autonomous-vehicle-3-0-on-aws-with-nvidia/) `aws.amazon.com` | 📰 | Tesla가 2021년 AI Day에서 설명한 데이터 엔진  (CleanTechnica), NVIDIA·AWS가 2026년 3월 설명한 "AV 3.0 데이터 파이프라인"  (AWS 블로그, 요약만 확인), 그리고 학술 서베이의 7단계 폐쇄루프 . |  |
| 36 | [SGO 2021-01](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting) `nhtsa.gov` | 📰 | Tesla 섀도 모드는 모델 출력과 운전자 행동을 비교 ; NHTSA는 자율주행 충돌을 1~5일 내 보고하게 함  (SGO 2021-01) |  |
| 37 | [UL 해설](https://www.ul.com/sis/blog/safety-related-systems-road-vehicles-artificial-intelligence-are-addressed-isopas-88002024) `ul.com` | 📰 | 3 —  (UL 해설) |  |
| 38 | [요약](https://diadrom.com/insights/un-r156-sums-requirements) `diadrom.com` | 📰 | 4 —  (요약) |  |
| 39 | [Electrek 2026-02](https://electrek.co/2026/02/06/tesla-ai-training-capability-china-critical-step-full-self-driving/) `electrek.co` | 📰 | (Electrek 2026-02, 국내 보도) |  |
| 40 | [국내 보도](https://m.news.nate.com/view/20260123n23984) `m.news.nate.com` | 📰 | (Electrek 2026-02, 국내 보도) |  |
| 41 | [CleanTechnica](https://cleantechnica.com/2021/08/27/how-teslas-autopilot-team-refines-an-unfathomable-amount-of-data-is-pretty-cool/) `cleantechnica.com` | 📰 | 당시 수치는 누적 100만 클립, 60억 개 객체 라벨, 1.5PB, 주당 1만 클립 자동 라벨링이었다  (CleanTechnica, Electrek). |  |
| 42 | [Electrek](https://electrek.co/2021/12/01/tesla-releases-new-footage-auto-labeling-tool-self-driving/) `electrek.co` | 📰 | 당시 수치는 누적 100만 클립, 60억 개 객체 라벨, 1.5PB, 주당 1만 클립 자동 라벨링이었다  (CleanTechnica, Electrek). |  |
| 43 | [Cosmos README](https://raw.githubusercontent.com/NVIDIA/Cosmos/main/README.md) `raw.githubusercontent.com` | 🔍 | 파운데이션 모델 자동 라벨링: NVIDIA Cosmos Curator가 "처리·주석·필터·중복 제거"를 맡고  (Cosmos README), Cosmos Reason 같은 시각언어모델이 "왜 이렇게 운전했나"까지 글로 붙인다 |  |
| 44 | [arXiv 2202.05263](https://arxiv.org/pdf/2202.05263) `arxiv.org` | 📰 | 장면 재현 — 3D 재구성: Waymo Block-NeRF는 사진 280만 장으로 샌프란시스코 한 구역(0.5km²)을 35개 신경 모델로 재구성  (arXiv 2202.05263); NVIDIA NuRec은 3D 가우시안 스플래팅으로 주행 로그를 다시 걸어 다닐 수 있는 3D 장면… |  |
| 45 | [Wayve](https://wayve.ai/thinking/gaia-3/) `wayve.ai` | 📰 | 장면 생성 — 생성형 월드모델: Wayve GAIA-3(150억 파라미터, 10배 데이터)  (Wayve); Waymo World Model(Genie 3 기반) ; NVIDIA Cosmos |  |
| 46 | [보도](https://www.autopilotreview.com/full-self-driving-update/) `autopilotreview.com` | 📰 | 배포 — 주 단위 OTA(v14.x는 1~2주 간격)  (보도) |  |

## 3장

| # | 출처 | 등급 | 뒷받침하는 내용(본문 발췌) | 다른 장 |
|---|---|---|---|---|
| 47 | [Intel 2016](https://download.intel.com/newsroom/2021/archive/2016-11-15-editorials-krzanich-the-future-of-automated-driving.pdf) `download.intel.com` | 📰 | Intel은 2016년에 차량당 하루 약 4,000GB로 추정했고(카메라 초당 20~60MB, 라이다 초당 10~70MB)  (Intel 2016), 최근 업계 추정은 시간당 1~5TB다  (Siemens 블로그). 양산차 통신 요금으로는 감당할 수 없으므로 차 안에서 골라야 한다. |  |
| 48 | [Siemens 블로그](https://blogs.sw.siemens.com/polarion/the-data-deluge-what-do-we-do-with-the-data-generated-by-avs/) `blogs.sw.siemens.com` | 📰⚠️ | Intel은 2016년에 차량당 하루 약 4,000GB로 추정했고(카메라 초당 20~60MB, 라이다 초당 10~70MB)  (Intel 2016), 최근 업계 추정은 시간당 1~5TB다  (Siemens 블로그). 양산차 통신 요금으로는 감당할 수 없으므로 차 안에서 골라야 한다. |  |
| 49 | [해설](https://autocrypt.io/edr-dssad-vehicle-accident-analysis-tools/) `autocrypt.io` | 📰 | 규칙 — openpilot의 crash/ 폴더는 즉시 업로드 ; UN R157의 DSSAD는 시스템 켜짐·꺼짐, 전환 요구, 최소위험기동, 운전자 개입을 시각과 함께 기록하도록 요구  (해설) |  |
| 50 | [NVIDIA 블로그](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f) `medium.com` | 📰 | 모델 점수 — Tesla는 2021년 기준 221개 트리거를 플릿에서 돌렸고, 걸리면 약 10초 클립을 올렸다  (Karpathy CVPR'21 요약); NVIDIA는 모델 앙상블의 불일치로 고른 데이터가 수동 선별보다 야간 보행자 검출을 3배, 자전거를 4.4배 개선했다고 보고  … |  |
| 51 | [README](https://raw.githubusercontent.com/NVIDIA-Omniverse-blueprints/cosmos-dataset-search/main/README.md) `raw.githubusercontent.com` | 🔍 | - NVIDIA Cosmos Dataset Search는 오픈 블루프린트로, 영상·텍스트를 같은 공간에 놓는 임베딩 모델(Cosmos-Embed1)과 GPU 가속 벡터 DB(Milvus + cuVS), Ray 기반 배치 수집 파이프라인으로 구성된다  (README). 임베딩 모델은 … |  |
| 52 | [README](https://raw.githubusercontent.com/voxel51/fiftyone/develop/README.md) `raw.githubusercontent.com` | 🔍 | - Voxel51 FiftyOne은 오픈소스 데이터셋 도구로 "데이터 문제·라벨 오류·엣지 케이스를 빠르게 찾고 고친다"고 README에 쓴다  (README). |  |
| 53 | [README](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-curate/main/README.md) `raw.githubusercontent.com` | 🔍 | - NVIDIA Cosmos Curator는 분할 → 필터 → 캡션 → 임베딩 → 중복 제거 → 데이터셋 생성 파이프라인이다  (README). NVIDIA는 2,000만 시간 영상을 Blackwell GPU로 14일(Hopper 40일, CPU로는 3년 이상)에 처리한다고 발표했지… |  |
| 54 | [NVIDIA 뉴스룸](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development) `nvidianews.nvidia.com` | 📰 | NVIDIA는 2,000만 시간 영상을 Blackwell GPU로 14일(Hopper 40일, CPU로는 3년 이상)에 처리한다고 발표했지만 README에는 처리량 수치가 없다  (NVIDIA 뉴스룸). |  |
| 55 | [README](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-reason2/main/README.md) `raw.githubusercontent.com` | 🔍 | Cosmos Reason 2(2B/8B/32B)는 "영상 캡션, 시간 구간 찾기, 물리 추론"을 하는 모델이고  (README), Uber가 자율주행 학습 데이터 캡션에 검토 중이라고 AWS 블로그가 전한다 . |  |
| 56 | [nvidia-cosmos/cosmos-curate](https://github.com/nvidia-cosmos/cosmos-curate) `github.com` | 🔍 | 그림 출처: Cosmos Curator의 공식 파이프라인 그림. 분할·주석 파이프라인(다운로드 → 디코드 → 샷 경계 분할 → 트랜스코드 → 움직임·품질 필터 → VLM 캡션 → 영상 임베딩 → 저장), 의미 기반 중복 제거, 데이터셋 샤딩의 세 단계가 Ray 위에서 돈다. |  |
| 57 | [요약](https://www.nocode.ai/recap-tesla-ai-day-2022/) `nocode.ai` | 📰⚠️ | - Tesla는 2022년 AI Day에서 여러 주행을 합쳐 4D(3D + 시간)로 재구성한 뒤 차선·객체 라벨을 자동으로 만드는 파이프라인을 설명했고, 1만 주행 기준 "수작업 500만 시간 → 클러스터 12시간"을 주장했다(자동 라벨링용 GPU 4,000장)  (요약). |  |
| 58 | [arXiv 2103.05073](https://arxiv.org/abs/2103.05073) `arxiv.org` | 📰 | - Waymo의 3D 자동 라벨링 논문(CVPR 2021)은 포인트클라우드 시퀀스 전체를 써서 만든 3D 박스가 사람 라벨과 대등하다고 보고했다  (arXiv 2103.05073). |  |
| 59 | [README](https://raw.githubusercontent.com/IDEA-Research/GroundingDINO/main/README.md) `raw.githubusercontent.com` | 🔍 | Grounding DINO는 글 프롬프트("construction worker . traffic cone")로 박스를 만들고(COCO 제로샷 52.5 AP)  (README), SAM 2는 점·박스 프롬프트로 영상 전체의 마스크와 추적을 만든다(tiny 38.9M ~ large 22… |  |
| 60 | [README](https://raw.githubusercontent.com/facebookresearch/sam2/main/README.md) `raw.githubusercontent.com` | 🔍 | Grounding DINO는 글 프롬프트("construction worker . traffic cone")로 박스를 만들고(COCO 제로샷 52.5 AP)  (README), SAM 2는 점·박스 프롬프트로 영상 전체의 마스크와 추적을 만든다(tiny 38.9M ~ large 22… |  |
| 61 | [ASAM](https://www.asam.net/news-media/news/detail/news/asam-releases-asam-openlabel-v100/) `asam.net` | 📰 | - 라벨 형식은 ASAM OpenLABEL(2021-11, JSON으로 2D/3D 박스·폴리곤과 "객체·행동·사건·맥락" 태그를 통일)이 표준이다  (ASAM). |  |
| 62 | [waymo-research/waymo-open-dataset](https://github.com/waymo-research/waymo-open-dataset) `github.com` | 🔍 | 그림 출처: 라이다 포인트클라우드 위에 붙은 보행자 3D 박스(주황)와 같은 순간의 카메라 영상(왼쪽 아래). 온보드 모델이 늦게 본 작업자도 클라우드의 자동 라벨러는 이런 3D 박스를 미래 프레임과 여러 주행을 합쳐 첫 프레임부터 만든다. |  |
| 63 | [업계 가이드](https://www.basic.ai/blog-post/how-much-do-data-annotation-services-cost-complete-guide-2025) `basic.ai` | 📰⚠️ | 외주 라벨 단가는 2D 박스 개당 $0.03~1.00, 세그멘테이션 마스크 $0.05~3.00 범위이고 Scale AI 같은 회사는 공개 단가표가 없다  (업계 가이드). | 5장 |
| 64 | [릴리스 노트 인용](https://www.notateslaapp.com/software-updates/version/2026.2.9.6/release-notes) `notateslaapp.com` | 📰⚠️ | Tesla FSD v14.3 릴리스 노트는 "강화학습 단계를 업그레이드해 어려운 예에 집중"했다고 적는다  (릴리스 노트 인용). 하지만 "작업자가 콘 뒤에서 나오는" 변형이나 "비가 더 세게 오는" 변형은 플릿에 없다. |  |
| 65 | [분석](https://arxiv.org/pdf/2510.14677) `arxiv.org` | 📰 | 재생(replay) — 가장 싸고 정확하지만, 내 차가 다르게 움직여도 남들이 반응하지 않아 인과가 끊긴다. "기록된 틈을 기다리는" 편법을 배울 위험  (분석) |  |
| 66 | [README](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/main/README.md) `raw.githubusercontent.com` | 🔍 | 재구성(reconstruction) — 3D 가우시안 스플래팅(1080p 30fps 이상, 학습에 24GB VRAM)  (README); NVIDIA 3DGRUT(어안·롤링셔터·반사까지 처리, USD/NuRec 내보내기) ; InstantNuRec은 10~20초 다중 카메라 장면을 … |  |
| 67 | [README](https://raw.githubusercontent.com/NVIDIA/instant-nurec/main/README.md) `raw.githubusercontent.com` | 🔍 | 재구성(reconstruction) — 3D 가우시안 스플래팅(1080p 30fps 이상, 학습에 24GB VRAM)  (README); NVIDIA 3DGRUT(어안·롤링셔터·반사까지 처리, USD/NuRec 내보내기) ; InstantNuRec은 10~20초 다중 카메라 장면을 … |  |
| 68 | [README](https://raw.githubusercontent.com/nvidia-cosmos/cosmos-transfer1/main/README.md) `raw.githubusercontent.com` | 🔍 | 생성(generation) — NVIDIA Cosmos Transfer1은 세그멘테이션·깊이·엣지, 자율주행용 라이다·HD맵 조건으로 영상을 만들고, 영상 1개를 다시점으로 늘리며, 2025-08 증류 모델은 36스텝을 1스텝으로 줄였다  (README); Wayve GAIA-3(1… |  |
| 69 | [nvidia-cosmos/cosmos-transfer1](https://github.com/nvidia-cosmos/cosmos-transfer1) `github.com` | 🔍 | 그림 출처: Cosmos Transfer1의 공식 구조도. 깊이·엣지·세그멘테이션 영상이 각각의 제어 가지(DepthControl·EdgeControl·SegControl)로 들어가고, 시공간 가중치 영상으로 섞여 디퓨전 백본에 조건을 준다. 기하는 입력 조건이 정하고 외관은 생성된다. |  |
| 70 | [README](https://raw.githubusercontent.com/NVlabs/alpagym/main/README.md) `raw.githubusercontent.com` | 🔍 | AlpaSim(시뮬레이터) + Cosmos-RL(학습기) 조합이고 현재 Alpamayo 1.5(10B) 정책을 GPU 2장 추론으로 지원하며 "초기 개발 단계"라고 밝힌다  (README). |  |
| 71 | [NVlabs/alpamayo-recipes](https://github.com/NVlabs/alpamayo-recipes) `github.com` | 🔍 | 그림 출처: NVIDIA가 공개한 Alpamayo 강화학습 레시피의 구조도. 롤아웃 복제본(vLLM)이 주행을 생성해 보상과 함께 롤아웃 풀에 넣고, 정책 복제본이 이를 소비해 가중치를 갱신하며, 갱신된 가중치가 롤아웃 쪽으로 되돌아간다. |  |
| 72 | [NVlabs/alpasim](https://github.com/NVlabs/alpasim) `github.com` | 🔍 | 그림 출처: NVIDIA AlpaSim의 마이크로서비스 구조. 센서 시뮬레이션(렌더러) → 정책 → 궤적 → 물리 → 런타임 → 평가가 분리되어 각각 다른 GPU에서 돈다. |  |
| 73 | [metrics.md](https://raw.githubusercontent.com/autonomousvision/navsim/main/docs/metrics.md) `raw.githubusercontent.com` | 🔍 | 유사 폐루프 — NAVSIM PDMS = (충돌 없음 × 주행 영역 준수) × 가중 평균(TTC·진행·승차감)  (metrics.md); v2는 차선 유지·신호 준수를 더하고 "사람도 위반한 경우 페널티 해제" |  |
| 74 | [README](https://raw.githubusercontent.com/Thinklab-SJTU/Bench2Drive/main/README.md) `raw.githubusercontent.com` | 🔍 | 시뮬 폐루프 — Bench2Drive(CARLA 220 루트·44 시나리오, 클립 13,638개)  (README); 재구성·생성 시뮬 |  |
| 75 | [UL 해설](https://www.ul.com/sis/insights/software-update-management-systems-according-unece-r156) `ul.com` | 📰 | EU에서는 2024년 7월부터 모든 신차에 적용된다  (UL 해설). UL 4600 안전 케이스 표준은 "분석 + 시뮬레이션 + 폐쇄 도로 + 공도 시험의 조합"으로 안전을 논증하고 소프트웨어 업데이트마다 논증을 갱신하라고 한다 . 배포가 곧 기록(DSSAD)으로 이어지므로, 플라이… |  |

## 4장

| # | 출처 | 등급 | 뒷받침하는 내용(본문 발췌) | 다른 장 |
|---|---|---|---|---|
| 76 | [Electrek](https://electrek.co/2026/05/03/tesla-fsd-10-billion-miles-no-magical-milestone-autonomy/) `electrek.co` | 📰⚠️ | FSD(Supervised) 누적 주행은 2026년 5월 100억 마일, 8월 140억 마일을 넘었다고 발표했고(하루 약 3,500만 마일 추정)  (Electrek). FSD를 켜지 않은 차에서도 백그라운드에서 판단을 내려 실제 운전과 비교하는 섀도 모드가 돈다 . 학습 클러스터 … |  |
| 77 | [TechCrunch](https://techcrunch.com/2026/04/22/tesla-just-increased-its-capex-to-25b-heres-where-the-money-is-going/) `techcrunch.com` | 📰⚠️ | FSD를 켜지 않은 차에서도 백그라운드에서 판단을 내려 실제 운전과 비교하는 섀도 모드가 돈다 . 학습 클러스터 Cortex는 2026년 1분기 "H100 상당 10만 장 이상", Cortex 2가 추가 가동됐으며, 2026년 설비투자 가이던스는 250억 달러 이상이다(2025년 8… |  |
| 78 | [comma.ai](https://www.comma.ai/openpilot) `comma.ai` | 📰 | 사용자 2만 명 이상, 누적 3억 마일 이상(56%가 openpilot 주행)  (comma.ai). 릴리스 노트로 진화가 확인된다. |  |
| 79 | [Waymo](https://waymo.com/safety/impact/) `waymo.com` | 📰 | Waymo. 2026년 3월 말 기준 무인 누적 2억 2,060만 마일, 주 400만 마일 이상  (Waymo). 안전 허브는 사람 대비 중상·사망 충돌 94% 감소, 에어백 전개 82% 감소, 부상 충돌 82% 감소를 보고하고(5개 도시), IIHS 독립 연구는 부상 충돌 81% … |  |
| 80 | [Baidu 6-K](https://www.sec.gov/Archives/edgar/data/1329099/000119312526110843/d34060dex991.pdf) `sec.gov` | 📰 | Baidu Apollo Go. 2026년 2분기 완전 무인 탑승 약 100만 회, 6월 누적 2,300만 회  (Baidu 6-K). 무인 차량의 에어백 전개는 평균 1,440만 km당 1회라고 밝혔다(공개 주장) . 6세대 RT6는 자체 파운데이션 모델 ADFM을 싣고, 2026년… |  |
| 81 | [TechCrunch](https://techcrunch.com/2026/07/30/zoox-clears-final-federal-hurdle-to-launch-paid-robotaxi-service/) `techcrunch.com` | 📰 | 무인 차량의 에어백 전개는 평균 1,440만 km당 1회라고 밝혔다(공개 주장) . 6세대 RT6는 자체 파운데이션 모델 ADFM을 싣고, 2026년부터 Lyft와 독일·영국에 투입한다 . Zoox는 2026년 7월 30일 NHTSA에서 핸들 없는 로보택시의 첫 상업 면제(연 2,5… |  |
| 82 | [Mobileye REM](https://www.mobileye.com/technology/rem/) `mobileye.com` | 📰 | 18개 브랜드·50개 차종·800만 대 이상의 양산 ADAS 차량이 km당 약 10KB의 익명 데이터를 보내고, 이를 모아 10cm 정확도의 "Roadbook" 지도를 만들어 다시 내려보낸다  (Mobileye REM). 검증은 "True Redundancy"(카메라 계열과 레이더·… |  |
| 83 | [Wayve](https://wayve.ai/thinking/gaia-4/) `wayve.ai` | 📰 | GAIA-3(2025-12)는 150억 파라미터에 이전 세대의 10배 데이터로 학습했고 검증용으로 외부 제공하며, GAIA-4(2026-08)는 AI Driver를 루프 안에 넣어 기록된 장면에서 출발하는 반사실 시나리오를 만든다  (Wayve). 단일 모델로 유럽·북미·일본 506… |  |
| 84 | [Momenta](https://momenta.cn/en/article/568.html) `momenta.cn` | 📰 | Momenta. 양산 탑재 차량 100만 대 돌파(2025년 30만 → 80만 → 상장 직전 100만)  (Momenta). R6 "플라이휠 대형 모델"은 고가치 클립 7,000만 개와 실주행 30억 km로 학습한 강화학습 기반 종단간 모델이고, R7(2026-04)은 사전학습·시뮬… |  |
| 85 | [현대차그룹](https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-accelerates-autonomous-driving-innovation-with-ai-powered-data-flywheel) `hyundaimotorgroup.com` | 📰 | 수집 → 학습 → 검증 → 배포의 순환을 자율주행 전략의 핵심 엔진으로 두고, 42dot이 개발한 종단간 시스템 Atria AI를 2026년 말까지 국내 차량에 실어 엣지 케이스 데이터를 모으며, 국토부와 협력해 전남·광주에 Atria AI 탑재 "SDV Pace Car"를 투입한다… |  |
| 86 | [PR Newswire](https://www.prnewswire.com/news-releases/hyundai-mobis-develops-data-driven-validation-system-to-dramatically-cut-testing-time-for-sdvs-302745490.html) `prnewswire.com` | 📰⚠️ | 시뮬레이터 60대를 연결하면 "1만 시간 상당 검증을 1주일에" 끝내는 것이 목표이고, 야간·우천·돌발 상황 재현이 강점이라고 밝혔다(계획치)  (PR Newswire). |  |
| 87 | [electrive](https://www.electrive.com/2026/07/02/vw-confirms-end-of-automated-driving-alliance-with-bosch/) `electrive.com` | 📰 | 다른 OEM. Toyota·Woven의 Arene은 동의 기반 주행 데이터 수집·분석(Arene Data)과 가상 검증(Arene Tools)을 2025년 RAV4부터 적용한다 . VW는 Bosch와의 자율주행 얼라이언스에 약 15억 유로를 쓴 뒤 2026년 7월 조기 종료를 확인했… |  |
| 88 | [NVIDIA 뉴스룸](https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development) `nvidianews.nvidia.com` | 📰 | Cosmos Curator(대규모 처리·주석) → Cosmos Transfer(날씨·조명·환경 변형으로 희소 시나리오 증폭) → Cosmos Reason/Evaluator(물리 정확성 자동 점수) → OSMO 오케스트레이션(코딩 에이전트 연동)으로 이어지며 Uber·Skild AI … |  |
| 89 | [Sacra](https://sacra.com/c/applied-intuition/) `sacra.com` | 📰⚠️ | Applied Intuition. 2025년 6월 기업가치 150억 달러에 6억 달러를 조달했고, 상위 20개 OEM 중 18개가 고객이며 시뮬·테스트가 매출의 약 1/3이라는 추정이 있다  (Sacra). Scale AI는 2025년 6월 Meta의 143억 달러 투자 뒤 고객 이… |  |
| 90 | [TIER IV](https://tier4.co.jp/en/updates/20260805-tieriv-develops-platform-with-astemo) `tier4.co.jp` | 📰⚠️ | Scale AI는 2025년 6월 Meta의 143억 달러 투자 뒤 고객 이탈과 감원을 겪었고, 자율주행 라벨링 비중은 2022년 이후 줄어 LLM 데이터로 옮겨갔다 . Voxel51은 페타바이트급 플릿 로그에서 임베딩·자연어 검색으로 엣지 케이스를 캐고 NuRec과 연동한다 . F… |  |

## 5장

| # | 출처 | 등급 | 뒷받침하는 내용(본문 발췌) | 다른 장 |
|---|---|---|---|---|
| 91 | [TÜV SÜD 백서](https://www.tuvsud.com/-/jssmedia/global/pdf-files/whitepaper-report-e-books/tuvsud-sotif.pdf) `tuvsud.com` | 📰 | ISO 21448(SOTIF)은 이를 "모르는 불안전 시나리오(영역 3)"라고 부르고, 이 영역을 합리적 노력으로 최대한 줄이는 것을 표준의 핵심으로 둔다  (TÜV SÜD 백서). 희소성은 숫자로 드러난다. |  |
| 92 | [해설](https://lacuna.tiptreesystems.com/work/active-data-discovery-mining-unknown-data-using-submodular-information-measures/wrk_c7958570151368a9e16a1f703eafc370) `lacuna.tiptreesystems.com` | 📰 | 불확실성 기반 능동학습은 초기 라벨 집합에 아예 없는 클래스("unknown unknown")를 잡지 못한다  (해설). 2026년 연구는 예측 월드모델의 "놀람" 신호로 희소 사건을 고르는 접근을 제안한다  (arXiv 2608.29772). |  |
| 93 | [arXiv 2608.29772](https://arxiv.org/abs/2608.29772) `arxiv.org` | 📰 | 2026년 연구는 예측 월드모델의 "놀람" 신호로 희소 사건을 고르는 접근을 제안한다  (arXiv 2608.29772). |  |
| 94 | [NAVSIM](https://github.com/autonomousvision/navsim/blob/main/README.md) `github.com` | 📰🔍 | 중간 해법과 그 한계. NAVSIM v2의 "의사 시뮬레이션"은 3D 가우시안 스플래팅으로 후속 관측을 합성해 폐루프 시뮬과 상관 0.89를 얻으면서 환경 상호작용을 6배 줄였다  (NAVSIM). 그러나 2026년 5월 Bench2Drive-Robust는 프레임 드롭·GPS 잡음·… |  |
| 95 | [arXiv 2605.18059](https://arxiv.org/abs/2605.18059) `arxiv.org` | 📰 | 그러나 2026년 5월 Bench2Drive-Robust는 프레임 드롭·GPS 잡음·추론 지연 같은 "배포 교란"이 폐루프 성능을 크게 떨어뜨리는데 기존 이미지 손상 평가로는 잡히지 않는다고 보고했다  (arXiv 2605.18059). 2025년 12월 자율주행 테스트 서베이는 "… |  |
| 96 | [arXiv 2512.11887](https://arxiv.org/abs/2512.11887) `arxiv.org` | 📰 | 2025년 12월 자율주행 테스트 서베이는 "코너 케이스 다양성, 시뮬–실제 격차, 체계적 기준 부재, 파운데이션 모델 테스트 비용"을 미해결 과제로 꼽는다  (arXiv 2512.11887). |  |
| 97 | [TÜV SÜD 해설](https://www.tuvsud.com/-/jssmedia/global/pdf-files/whitepaper-report-e-books/tuvsud_virtual-homologation-of-an-alks-according-to-unece-r157.pdf) `tuvsud.com` | 📰 | 규제는 시뮬레이션 증거를 조건부로 받는다. UN R157(자동 차선 유지) 부속서 4는 시험장·실도로에서 재현하기 어려운 시나리오에 시뮬레이션 사용을 허용하되, 제조사가 도구의 범위·해당 시나리오의 유효성·물리 시험과의 상관을 입증하도록 한다  (TÜV SÜD 해설). EU의 완전자… |  |
| 98 | [Introl](https://introl.com/blog/autonomous-vehicle-ai-infrastructure-edge-cloud) `introl.com` | 📰⚠️ | 데이터 양 —  (Introl) |  |
| 99 | [CloudZero](https://www.cloudzero.com/blog/s3-pricing/) `cloudzero.com` | 📰 | 클라우드 반출(egress) —  (CloudZero) |  |
| 100 | [Bosch](https://www.bosch-engineering.com/stories/neural-automated-labeling/) `bosch-engineering.com` | 📰⚠️ | 자동 라벨링 절감 —  (Bosch) |  |
| 101 | [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/11/the-eu-data-act-has-taken-effect-focus-on-automotive-and-cloud-providers) `mayerbrown.com` | 📰 | EU — GDPR + EDPB 커넥티드카 가이드라인(차량 데이터 대부분을 개인정보로 간주, 차내 처리 권고) ; Data Act 2025-09-12 적용, 2026-09-12부터 설계 의무(사용자가 데이터에 직접 접근)  (Mayer Brown); AI Act 부속서 I(형식승인 대… |  |
| 102 | [China Briefing](https://www.china-briefing.com/news/vehicle-data-export-rules-china/) `china-briefing.com` | 📰 | 중국 — 2026-01-30 8개 부처 "자동차 데이터 국외 이전 보안 가이드라인(2026판)": 연구개발·자율주행·소프트웨어 업그레이드 시나리오별 중요 데이터 식별, 보안 평가·표준 계약·인증, 로그 3년 보관  (China Briefing) |  |
| 103 | [머니투데이](https://www.mt.co.kr/tech/2026/01/23/2026012309533977120) `mt.co.kr` | 📰 | 한국 — 2026-01 개인정보위: 규제 샌드박스로 안전 조치 시 자율주행차·로봇의 원본 영상(비식별 없이) 활용 허용, 9개사 신청; "자율주행 영상처리장치" 정의, 접근 기록·삭제 의무 신설  (머니투데이) |  |

## 직접 열람한 1차 출처(🔍)

아래 문서·저장소는 이 세션에서 원문 또는 파일을 직접 읽었다(열람일 2026-09-22). openpilot 코드 인용은 커밋 `521db4c`(2026-09-20) 기준이다. 그림을 내려받은 저장소는 LICENSE 파일도 함께 확인했다.

- https://raw.githubusercontent.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving/main/README.md
- https://raw.githubusercontent.com/commaai/openpilot/master/RELEASES.md
- https://github.com/OpenDriveLab/End-to-end-Autonomous-Driving
- https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving
- https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/README.md
- https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/docs/05-limitations-best-practices.md
- https://raw.githubusercontent.com/NVIDIA-AI-Blueprints/data-flywheel/main/docs/01-architecture.md
- https://github.com/NVIDIA-AI-Blueprints/data-flywheel
- https://raw.githubusercontent.com/NVIDIA/Cosmos/main/README.md
- https://raw.githubusercontent.com/NVIDIA-Omniverse-blueprints/cosmos-dataset-search/main/README.md
- https://raw.githubusercontent.com/voxel51/fiftyone/develop/README.md
- https://raw.githubusercontent.com/nvidia-cosmos/cosmos-curate/main/README.md
- https://raw.githubusercontent.com/nvidia-cosmos/cosmos-reason2/main/README.md
- https://github.com/nvidia-cosmos/cosmos-curate
- https://raw.githubusercontent.com/IDEA-Research/GroundingDINO/main/README.md
- https://raw.githubusercontent.com/facebookresearch/sam2/main/README.md
- https://github.com/waymo-research/waymo-open-dataset
- https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/main/README.md
- https://raw.githubusercontent.com/NVIDIA/instant-nurec/main/README.md
- https://raw.githubusercontent.com/nvidia-cosmos/cosmos-transfer1/main/README.md
- https://github.com/nvidia-cosmos/cosmos-transfer1
- https://raw.githubusercontent.com/NVlabs/alpagym/main/README.md
- https://github.com/NVlabs/alpamayo-recipes
- https://github.com/NVlabs/alpasim
- https://raw.githubusercontent.com/autonomousvision/navsim/main/docs/metrics.md
- https://raw.githubusercontent.com/Thinklab-SJTU/Bench2Drive/main/README.md
- https://github.com/autonomousvision/navsim/blob/main/README.md

## 접근 실패 URL(프록시 차단·404) — 검색 요약으로만 확보

조사 중 열람을 시도했으나 실패한 주소·도메인이다. 해당 내용은 검색 엔진 요약과 2차 보도로만 확인했으므로 본문에서 📰로 표시했다.

- 정책상 미접근 도메인: arxiv.org, huggingface.co, nvidia.com·nvidianews.nvidia.com·blogs.nvidia.com·developer.nvidia.com, tesla.com, waymo.com, wayve.ai, mobileye.com, medium.com
- 차단된 공식·규제 문서: aws.amazon.com(AV 3.0 파이프라인 블로그), rand.org(RR-1478), unece.org(R156·R157 원문), eur-lex.europa.eu(2021/1426·AI Act·Data Act), federalregister.gov, dmv.ca.gov, asam.net, ul.com, dspace.com
- 차단된 기업·보도 사이트: blog.comma.ai, momenta.ai·momenta.cn, xpeng.com, appliedintuition.com, voxel51.com, foretellix.com, catena-x.net, tier4.co.jp·co-mlops.tier4.jp, hyundaimotorgroup.com·hyundai.news, volkswagen-group.com, ir.baidu.com, electrek.co, techcrunch.com, cleantechnica.com, towardsdatascience.com, spectrum.ieee.org, technologyreview.com, prnewswire.com, globenewswire.com, cnevpost.com, electrive.com, autonomousvehicleinternational.com, automotiveworld.com, notateslaapp.com, teslaoracle.com, basenor.com, dynamicallytyped.com, autocrypt.io, download.intel.com, openaccess.thecvf.com, pubmed.ncbi.nlm.nih.gov, tandfonline.com, crowell.com, twobirds.com, youtube.com
- 404: raw.githubusercontent.com/NVIDIA/alpamayo(실제 저장소는 NVlabs/alpasim·NVlabs/alpamayo-recipes), raw.githubusercontent.com/NVIDIA/nurec(NuRec는 NVIDIA/instant-nurec·NVIDIA/nurec-skills로 공개), tier4/data_recording_system의 main 브랜치(master로 성공)

## 미확인 항목

보고서 본문 끝의 [미확인 항목 표](../vehicle-data-flywheel.md#미확인-항목)(15개)를 참고. 회사 발표 수치는 독립 검증이 없으므로 ⚠️ 또는 "공개 주장"으로 표기했다. 발표 슬라이드 화면(Tesla·Waymo·Momenta)의 발표 행사·연도는 수록 저장소에 기재가 없어 미확인이다.
