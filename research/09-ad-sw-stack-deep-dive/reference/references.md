# 출처 목록 — 자율주행 SW 스택 파헤치기 심층편

> **열람일**: 모든 출처 2026-09-15 · ID는 [보고서](../ad-sw-stack-deep-dive.md)와 [기사](../article.md)의 인용 표기와 같다.
>
> **등급**: 💻 고정 커밋 코드 직접 확인 · 🔍 1차 원문 직접 열람 · 📄 서드파티(해설·보도·미러·Wikipedia) 직접 열람 · ✅ 2개 이상 교차 확인 · 📰 검색 요약만(원문 미열람) · ⚠️ 미확인
>
> "벤더 주장"은 기업 자료에 적힌 내용이며 독립 검증을 거치지 않았다. 조사 영역별로 독립 수집해 같은 문서가 여러 접두어에 중복 등재된 경우가 있다(예: NAVSIM은 [E40]과 [D15]). 일부 행은 원 조사 노트의 번호 체계를 유지해 결번이 있다.

| 접두어 | 영역 |
|---|---|
| E | 1부 진화 과정 |
| A | 2부 Autoware |
| N | 2부 NVIDIA DRIVE AV·Alpamayo |
| D | 3부 데이터 플라이휠·검증 |
| P | 4부 양산 스택 |
| F | 5부 미래 방향 |
| V | 약한 근거 재검증 (2026-09-15) |
| K | 고정 커밋 소스 코드 (2026-09-15 클론) |

## [E] 1부 진화 과정 (66건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| E1 | Thrun et al., "Stanley: The Robot that Won the DARPA Grand Challenge," JFR 23(9), 2006 (PDF p.661–680 열람) | http://robots.stanford.edu/papers/thrun.stanley05.pdf | 🔍 |
| E2 | Urmson et al., "Autonomous Driving in Urban Environments: Boss and the Urban Challenge," JFR 25(8), 2008 — CMU RI 초록 | https://publications.ri.cmu.edu/autonomous-driving-in-urban-environments-boss-and-the-urban-challenge/ | 🔍(초록) |
| E3 | SPIE News, "CMU robot car first in DARPA Urban Challenge" | https://spie.org/news/darpa-challenge | 🔍 |
| E4 | Bojarski et al., "End to End Learning for Self-Driving Cars," arXiv:1604.07316 | https://arxiv.org/abs/1604.07316 | 🔍 |
| E5 | NVIDIA Technical Blog, "End-to-End Deep Learning for Self-Driving Cars" (2016-08-17) | https://developer.nvidia.com/blog/deep-learning-self-driving-cars/ | 🔍 |
| E6 | NVIDIA Newsroom, DRIVE PX 2 발표 (2016-01-04) | https://nvidianews.nvidia.com/news/nvidia-boosts-iq-of-self-driving-cars-with-world-s-first-in-car-artificial-intelligence-supercomputer | 🔍 |
| E7 | NVIDIA Newsroom, DRIVE PX Pegasus (2017-10-10) | https://nvidianews.nvidia.com/news/nvidia-announces-world-s-first-ai-computer-to-make-robotaxis-a-reality | 🔍 |
| E8 | NVIDIA Technical Blog, "Jetson AGX Xavier Delivers 32 TeraOps" (2018-12-12) | https://developer.nvidia.com/blog/nvidia-jetson-agx-xavier-32-teraops-ai-robotics/ | 🔍 |
| E9 | NVIDIA Newsroom, "NVIDIA Unveils DRIVE Thor" (2022-09-20) | https://nvidianews.nvidia.com/news/nvidia-unveils-drive-thor-centralized-car-computer-unifying-cluster-infotainment-automated-driving-and-parking-in-a-single-cost-saving-system | 🔍 |
| E10 | NVIDIA, "DRIVE AGX Thor Development Platform" PDF (2025-12) | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | 🔍 |
| E11 | PR Newswire, Mobileye EyeQ4 발표 (2015-03-04) | https://www.prnewswire.com/news-releases/moving-closer-to-automated-driving-mobileye-unveils-eyeq4-system-on-chip-with-its-first-design-win-for-2018-300045242.html | 🔍 |
| E12 | Mobileye Blog, "Meet EyeQ6" (2022-05-25) | https://www.mobileye.com/blog/eyeq6-system-on-chip/ | 🔍 |
| E13 | Apollo 3.0 Software Architecture (공식 문서 미러) | https://daobook.github.io/apollo/docs/specs/Apollo_3.0_Software_Architecture.html | 📄 (공식 문서 미러) |
| E14 | ApolloAuto/apollo RELEASE.md | https://github.com/ApolloAuto/apollo/blob/master/RELEASE.md | 🔍 |
| E15 | The Last Driver License Holder, "Baidu's Open Source … Apollo in Detail" (2017-10-26) | https://thelastdriverlicenseholder.com/2017/10/26/baidus-open-source-self-driving-plattform-apollo-in-detail/ | 📄 (3자) |
| E16 | ApolloAuto/apollo README | https://github.com/ApolloAuto/apollo/blob/master/README.md | 🔍 |
| E17 | Autoware Foundation, "Past, Present and the Future of Autoware" | https://autoware.org/past-present-and-the-future-of-autoware/ | 📰 |
| E18 | Bansal, Krizhevsky, Ogale, "ChauffeurNet," arXiv:1812.03079 | https://arxiv.org/abs/1812.03079 | 🔍 |
| E19 | Waymo, "Safety Methodologies and Safety Readiness Determinations," arXiv:2011.00054 | https://arxiv.org/abs/2011.00054 | 🔍 |
| E20 | Shalev-Shwartz et al., "On a Formal Model of Safe and Scalable Self-driving Cars" (RSS), arXiv:1708.06374 | https://arxiv.org/abs/1708.06374 | 🔍 |
| E21 | Geiger et al., "Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite," CVPR 2012 | https://www.cvlibs.net/publications/Geiger2012CVPR.pdf | 🔍 |
| E22 | Caesar et al., "nuScenes," arXiv:1903.11027 | https://arxiv.org/abs/1903.11027 | 🔍 |
| E23 | Sun et al., "Scalability in Perception for Autonomous Driving: Waymo Open Dataset," arXiv:1912.04838 (PDF p.1) | https://arxiv.org/pdf/1912.04838 | 🔍 |
| E24 | Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep CNNs," NeurIPS 2012 (PDF p.1) | https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf | 🔍 |
| E25 | Li et al., "BEVFormer," arXiv:2203.17270 | https://arxiv.org/abs/2203.17270 | 🔍 |
| E26 | Liu et al., "BEVFusion," arXiv:2205.13542 | https://arxiv.org/abs/2205.13542 | 🔍 |
| E27 | Electrek, "Elon Musk announces Tesla AI Day on August 19" (2021-07-29) | https://electrek.co/2021/07/29/elon-musk-tesla-ai-day-august-19/ | 📰 |
| E28 | Think Autonomous, "Tesla's FSD Architecture: From HydraNets to End-To-End" | https://www.thinkautonomous.ai/blog/tesla-end-to-end-deep-learning/ | 📄 (3자) |
| E29 | Ashok Elluswamy(Tesla) X 게시물, CVPR 2022 Occupancy Networks | https://x.com/aelluswamy/status/1561151207858573312 | 📰 |
| E30 | Occ3D arXiv:2304.14365 / SurroundOcc arXiv:2303.09551 / OccNet arXiv:2306.02851 | https://arxiv.org/abs/2304.14365 · https://arxiv.org/abs/2303.09551 · https://arxiv.org/abs/2306.02851 | 📰 |
| E31 | Not a Tesla App, "How Tesla's FSD Hardware Has Changed Over the Years" (2026-05-27) | https://www.notateslaapp.com/news/3521/how-teslas-fsd-hardware-has-changed-over-the-years | 📄 (3자) |
| E32 | Hu et al., "Planning-oriented Autonomous Driving" (UniAD), arXiv:2212.10156 | https://arxiv.org/abs/2212.10156 | 🔍 |
| E33 | Jiang et al., "VAD," arXiv:2303.12077 | https://arxiv.org/abs/2303.12077 | 🔍 |
| E34 | Tesla 2024.3.20 (FSD 12.3.5) 릴리스노트 미러 | https://www.notateslaapp.com/software-updates/version/2024.3.20/release-notes | ✅ |
| E35 | Tesla 2024.39.10 (FSD 13.2) 릴리스노트 미러 | https://www.notateslaapp.com/software-updates/version/2024.39.10/release-notes | 📄 (미러) |
| E36 | Tesla Oracle, FSD v14.1 (2025.32.8.5) 릴리스노트 (2025-10-07) | https://www.teslaoracle.com/2025/10/07/tesla-tsla-beings-the-rollout-of-fsd-v14-software-update-2025-32-8-5-release-notes/ | 📄 (미러) |
| E37 | Tesla Oracle, Musk "10X higher parameter count" (2025-08-11) | https://www.teslaoracle.com/2025/08/11/tesla-to-rollout-fsd-v14-in-6-weeks-with-10x-parameters-and-exponentially-better-safety-says-musk/ | 📄 (3자 인용) |
| E38 | Wayve, "LINGO-2: Driving with Natural Language" (2024-04-17) | https://wayve.ai/thinking/lingo-2-driving-with-language/ | 🔍 |
| E39 | Russell et al., "GAIA-2," arXiv:2503.20523 | https://arxiv.org/abs/2503.20523 | 🔍 |
| E40 | Dauner et al., "NAVSIM," arXiv:2406.15349 | https://arxiv.org/abs/2406.15349 | 🔍 |
| E41 | Cao et al., "Pseudo-Simulation for Autonomous Driving," arXiv:2506.04218 | https://arxiv.org/abs/2506.04218 | 🔍 |
| E42 | Li et al., "Hydra-MDP," arXiv:2406.06978 | https://arxiv.org/abs/2406.06978 | 🔍 |
| E43 | Liao et al., "DiffusionDrive," arXiv:2411.15139 | https://arxiv.org/abs/2411.15139 | 🔍 |
| E44 | Waymo Blog, "Introducing EMMA" (2024-10-30) / arXiv:2410.23262 | https://waymo.com/blog/2024/10/introducing-emma/ | 🔍 / 📰 |
| E45 | NVIDIA Newsroom, Alpamayo 패밀리 발표 (2026-01-05) | https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development | 🔍 |
| E46 | NVIDIA Technical Blog, "Building Autonomous Vehicles That Reason with NVIDIA Alpamayo" (2026-01-05) | https://developer.nvidia.com/blog/building-autonomous-vehicles-that-reason-with-nvidia-alpamayo | 🔍 |
| E47 | NVIDIA, "Alpamayo-R1," arXiv:2511.00088 | https://arxiv.org/abs/2511.00088 | 🔍 |
| E48 | Hugging Face 모델카드 nvidia/Alpamayo-R1-10B | https://huggingface.co/nvidia/Alpamayo-R1-10B | 🔍 |
| E49 | NVIDIA Newsroom, "Alpamayo 2 Super" (2026-05-31) | https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis | 🔍 |
| E50 | NVIDIA Blog, "Alpamayo 2 Super … Now Available for Commercial Use" (2026-08-04) | https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/ | 🔍 |
| E51 | NVIDIA Alpamayo 제품 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/ | 🔍 |
| E52 | Radiance Fields, "Inside NVIDIA's Alpamayo 1.5, NuRec, and AlpaDreams" (GTC 2026 인터뷰) | https://radiancefields.com/inside-nvidia-s-alpamayo-1.5-nurec-and-alpadreams-a-gtc-conversation-with-matt-cragun | 📄 (3자) |
| E53 | XPENG 뉴스룸, VLA 2.0·Robotaxi·IRON 발표 (2025-11-05) | https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7 | 🔍 |
| E54 | XPENG 뉴스룸, VLA 2.0 글로벌 공로 테스트·2027 인도 (2026-03-02) | https://www.xpeng.com/pressroom/news/019cae5e67b99c0960ee8a028129016a | 🔍 |
| E55 | 36Kr, "Assisted Driving Models Growing Larger: XPeng and Li Auto … 7-Billion Parameter" (2025-10-15) | https://eu.36kr.com/en/p/3510288150944643 | 📄 (3자) |
| E56 | CnEVPost, "Li Auto unveils MindVLA" (2025-03-18) | https://cnevpost.com/2025/03/18/li-auto-unveils-mindvla-autonomous-driving-architecture/ | 📄 (3자) |
| E57 | KrASIA, "Huawei's Qiankun 4.0 targets Level 3" (2025-04-29) | https://kr-asia.com/huaweis-qiankun-4-0-targets-level-3-driving-autonomy-with-radar-and-ai-upgrades | 📄 (3자) |
| E58 | ChinaEVHome, "WA over VLA: Huawei Diverges…" (2025-08-28) | https://chinaevhome.com/2025/08/28/huaweis-jin-yuzhi-skipping-vla-in-favor-of-wa-for-autonomous-driving/ | 📄 (3자) |
| E59 | Chen et al., "End-to-end Autonomous Driving: Challenges and Frontiers," arXiv:2306.16927 (270+편 서베이) | https://arxiv.org/abs/2306.16927 | 🔍 |
| E60 | Yurtsever et al., "A Survey of Autonomous Driving: Common Practices and Emerging Technologies," arXiv:1906.05113 | https://arxiv.org/abs/1906.05113 | 🔍 |
| E61 | Jiang et al., "A Survey on Vision-Language-Action Models for Autonomous Driving," arXiv:2506.24044 (20+모델 비교) | https://arxiv.org/abs/2506.24044 | 🔍 |
| E62 | Feng, Wang, Yang, "A Survey of World Models for Autonomous Driving," arXiv:2501.11260 | https://arxiv.org/abs/2501.11260 | 🔍 |
| E63 | Naumann et al., "Data Scaling Laws for End-to-End Autonomous Driving," arXiv:2504.04338 | https://arxiv.org/abs/2504.04338 | 🔍 |
| E64 | Forbes/HotHardware, NVIDIA Orin 200 TOPS 발표 (2019-12-18) | https://www.forbes.com/sites/tiriasresearch/2019/12/18/nvidia-announces-new-orin-auto-ai-processor/ | 📰 |
| E65 | Electrek, FSD Beta 확대 (2022-09-19) | https://electrek.co/2022/09/19/tesla-full-self-driving-beta-expands-owners/ | 📰 |
| E73 | Electrek, Tesla AI Day 2 초대 (2022-09-23) | https://electrek.co/2022/09/23/tesla-sends-invites-ai-day-2-teases-full-self-driving-tesla-bot-dojo/ | 📰 |

## [A] 2부A Autoware (123건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| A1 | Autoware concepts | https://docs.autoware.org/main/design/autoware-concepts/ | 🔍 |
| A2 | Autoware's Design (index) | https://docs.autoware.org/main/design/ | 🔍 |
| A3 | Architecture 1.0 overview | https://docs.autoware.org/main/design/autoware-architecture-v1/ | 🔍 |
| A4 | Node diagram | https://docs.autoware.org/main/design/autoware-architecture-v1/node-diagram/ | 🔍 |
| A5 | Localization component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/localization/ | 🔍 |
| A6 | Perception component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/perception/ | 🔍 |
| A7 | Perception reference implementation | https://docs.autoware.org/main/design/autoware-architecture-v1/components/perception/reference_implementation/ | 🔍 |
| A8 | Planning component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/planning/ | 🔍 |
| A9 | Control component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/control/ | 🔍 |
| A10 | Sensing component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/sensing/ | 🔍 |
| A11 | Vehicle interface component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/vehicle/ | 🔍 |
| A12 | Map component design | https://docs.autoware.org/main/design/autoware-architecture-v1/components/map/ | 🔍 |
| A13 | Interfaces design | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/ | 🔍 |
| A14 | AD API | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/ad-api/ | 🔍 |
| A15 | AD API list | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/ad-api/list/ | 🔍 |
| A16 | Planning component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/planning/ | 🔍 |
| A17 | Control component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/control/ | 🔍 |
| A18 | Localization component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/localization/ | 🔍 |
| A19 | Perception component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/perception-interface/ | 🔍 |
| A20 | Vehicle interface (component interface) | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/vehicle-interface/ | 🔍 |
| A21 | Sensing component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/sensing/ | 🔍 |
| A22 | Map component interface | https://docs.autoware.org/main/design/autoware-architecture-v1/interfaces/components/map/ | 🔍 |
| A23 | Autoware 2.0 Architecture | https://docs.autoware.org/main/design/autoware-architecture-v2/ | 🔍 |
| A24 | Architecture 2.0 roadmap | https://docs.autoware.org/main/design/autoware-architecture-v2/roadmap/ | 🔍 |
| A25 | v2: Autonomous Driving Stack Architecture | https://docs.autoware.org/main/design/autoware-architecture-v2/roadmap/autonomous-driving-stack-architecture/ | 🔍 |
| A26 | v2: Detailed Architectural Interface | https://docs.autoware.org/main/design/autoware-architecture-v2/roadmap/detailed-architectural-interface/ | 🔍 |
| A27 | v2: Development Roadmap (TBD) | https://docs.autoware.org/main/design/autoware-architecture-v2/roadmap/development-roadmap/ | 🔍 |
| A28 | v2: Assessment of Safety and Benchmarks (TBD) | https://docs.autoware.org/main/design/autoware-architecture-v2/roadmap/assessment-safety-and-benchmarks/ | 🔍 |
| A29 | Versioning and release | https://docs.autoware.org/main/design/versioning-and-release/ | 🔍 |
| A30 | Repository structure | https://docs.autoware.org/main/design/repository-structure/ | 🔍 |
| A31 | Difference from Autoware.AI / Auto | https://docs.autoware.org/main/design/autoware-concepts/difference-from-ai-and-auto/ | 🔍 |
| A32 | Core package inclusion criteria | https://docs.autoware.org/main/design/autoware-concepts/core-package-inclusion-criteria/ | 🔍 |
| A33 | System capabilities | https://docs.autoware.org/main/design/autoware-system-capabilities/ | 🔍 |
| A34 | Multi-year roadmap | https://docs.autoware.org/main/home/roadmap/multi-year-roadmap/ | 🔍 |
| A35 | Humble→Jazzy timeline | https://docs.autoware.org/main/home/roadmap/timelines/humble-jazzy/ | 🔍 |
| A36 | Point cloud type transition timeline | https://docs.autoware.org/main/home/roadmap/timelines/point-types/ | 🔍 |
| A37 | Installation (index) | https://docs.autoware.org/main/installation/ | 🔍 |
| A38 | Source installation | https://docs.autoware.org/main/installation/autoware/source-installation/ | 🔍 |
| A39 | Docker installation | https://docs.autoware.org/main/installation/autoware/docker-installation/ | 🔍 |
| A40 | DDS settings | https://docs.autoware.org/main/installation/additional-settings-for-developers/network-configuration/dds-settings/ | 🔍 |
| A41 | Running Autoware without CUDA | https://docs.autoware.org/main/tutorials/others/running-autoware-without-cuda/ | 🔍 |
| A42 | Reference design (index) | https://docs.autoware.org/main/reference-design/ | 🔍 |
| A43 | Reference HW: AD computers | https://docs.autoware.org/main/reference-design/reference-hw/ad-computers/ | 🔍 |
| A44 | Reference HW: vehicle platform suppliers | https://docs.autoware.org/main/reference-design/reference-hw/vehicle_platform_suppliers/ | 🔍 |
| A45 | AutoSDV | https://docs.autoware.org/main/reference-design/get-started/AutoSDV/ | 🔍 |
| A46 | Reference design metrics | https://docs.autoware.org/main/reference-design/metrics/ | 🔍 |
| A47 | Coding guideline: topic message handling | https://docs.autoware.org/main/contributing/coding-guidelines/ros-nodes/topic-message-handling/ | 🔍 |
| A48 | Coding guideline: topic namespaces | https://docs.autoware.org/main/contributing/coding-guidelines/ros-nodes/topic-namespaces/ | 🔍 |
| A49 | GitHub API: autoware releases | https://api.github.com/repos/autowarefoundation/autoware/releases | 🔍 |
| A50 | GitHub API: autoware_core releases | https://api.github.com/repos/autowarefoundation/autoware_core/releases | 🔍 |
| A51 | GitHub API: autoware_universe releases | https://api.github.com/repos/autowarefoundation/autoware_universe/releases | 🔍 |
| A52 | autoware 1.9.0 release notes | https://github.com/autowarefoundation/autoware/releases/tag/1.9.0 | 🔍 |
| A53 | autoware.repos (main) | https://raw.githubusercontent.com/autowarefoundation/autoware/main/repositories/autoware.repos | 🔍 |
| A54 | ansible cuda defaults | https://raw.githubusercontent.com/autowarefoundation/autoware/main/ansible/roles/cuda/defaults/main.yaml | 🔍 |
| A55 | ansible tensorrt defaults | https://raw.githubusercontent.com/autowarefoundation/autoware/main/ansible/roles/tensorrt/defaults/main.yaml | 🔍 |
| A56 | ansible rmw_implementation defaults | https://raw.githubusercontent.com/autowarefoundation/autoware/main/ansible/roles/rmw_implementation/defaults/main.yaml | 🔍 |
| A57 | ansible artifacts tasks (ML models) | https://raw.githubusercontent.com/autowarefoundation/autoware/main/ansible/roles/artifacts/tasks/main.yaml | 🔍 |
| A58 | autoware LICENSE | https://github.com/autowarefoundation/autoware/blob/main/LICENSE | 🔍 |
| A59 | autoware_core repo README | https://github.com/autowarefoundation/autoware_core | 🔍 |
| A60 | autoware_universe README | https://raw.githubusercontent.com/autowarefoundation/autoware_universe/main/README.md | 🔍 |
| A61 | autoware_ai README (archived) | https://github.com/autowarefoundation/autoware_ai | 🔍 |
| A62 | autoware_msgs repo | https://github.com/autowarefoundation/autoware_msgs | 🔍 |
| A63 | agnocast repo README | https://github.com/autowarefoundation/agnocast | 🔍 |
| A64 | AWF Discussion #5835 (Agnocast) | https://github.com/orgs/autowarefoundation/discussions/5835 | 🔍 |
| A65 | autoware_agnocast_wrapper (core docs) | https://autowarefoundation.github.io/autoware_core/main/common/autoware_agnocast_wrapper/ | 🔍 |
| A66 | cuda_blackboard repo README | https://github.com/autowarefoundation/cuda_blackboard | 🔍 |
| A67 | autoware_core docs index | https://autowarefoundation.github.io/autoware_core/main/ | 🔍 |
| A68 | autoware_universe docs index | https://autowarefoundation.github.io/autoware_universe/main/ | 🔍 |
| A69 | autoware_ndt_scan_matcher | https://autowarefoundation.github.io/autoware_core/main/localization/autoware_ndt_scan_matcher/ | 🔍 |
| A70 | autoware_ekf_localizer | https://autowarefoundation.github.io/autoware_core/main/localization/autoware_ekf_localizer/ | 🔍 |
| A71 | autoware_gyro_odometer | https://autowarefoundation.github.io/autoware_core/main/localization/autoware_gyro_odometer/ | 🔍 |
| A72 | autoware_pose_initializer | https://autowarefoundation.github.io/autoware_core/main/localization/autoware_pose_initializer/ | 🔍 |
| A73 | autoware_mission_planner | https://autowarefoundation.github.io/autoware_core/main/planning/autoware_mission_planner/ | 🔍 |
| A74 | autoware_velocity_smoother | https://autowarefoundation.github.io/autoware_core/main/planning/autoware_velocity_smoother/ | 🔍 |
| A75 | autoware_motion_velocity_planner | https://autowarefoundation.github.io/autoware_core/main/planning/motion_velocity_planner/autoware_motion_velocity_planner/ | 🔍 |
| A76 | autoware_behavior_velocity_planner | https://autowarefoundation.github.io/autoware_core/main/planning/behavior_velocity_planner/autoware_behavior_velocity_planner/ | 🔍 |
| A77 | autoware_path_generator | https://autowarefoundation.github.io/autoware_core/main/planning/autoware_path_generator/ | 🔍 |
| A78 | autoware_command_gate (core) | https://autowarefoundation.github.io/autoware_core/main/control/autoware_command_gate/ | 🔍 |
| A79 | autoware_simple_pure_pursuit | https://autowarefoundation.github.io/autoware_core/main/control/autoware_simple_pure_pursuit/ | 🔍 |
| A80 | autoware_map_loader | https://autowarefoundation.github.io/autoware_core/main/map/autoware_map_loader/ | 🔍 |
| A81 | autoware_vehicle_cmd_gate | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_vehicle_cmd_gate/ | 🔍 |
| A82 | autoware_trajectory_follower_node | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_trajectory_follower_node/ | 🔍 |
| A83 | autoware_mpc_lateral_controller | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_mpc_lateral_controller/ | 🔍 |
| A84 | autoware_pid_longitudinal_controller | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_pid_longitudinal_controller/ | 🔍 |
| A85 | autoware_control_validator | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_control_validator/ | 🔍 |
| A86 | autoware_lidar_centerpoint | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_lidar_centerpoint/ | 🔍 |
| A87 | autoware_lidar_transfusion | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_lidar_transfusion/ | 🔍 |
| A88 | autoware_multi_object_tracker | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_multi_object_tracker/ | 🔍 |
| A89 | autoware_map_based_prediction | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_map_based_prediction/ | 🔍 |
| A90 | autoware_probabilistic_occupancy_grid_map | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_probabilistic_occupancy_grid_map/ | 🔍 |
| A91 | autoware_image_projection_based_fusion | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_image_projection_based_fusion/ | 🔍 |
| A92 | autoware_tensorrt_yolox | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_tensorrt_yolox/ | 🔍 |
| A93 | autoware_traffic_light_classifier | https://autowarefoundation.github.io/autoware_universe/main/perception/autoware_traffic_light_classifier/ | 🔍 |
| A94 | autoware_behavior_path_planner | https://autowarefoundation.github.io/autoware_universe/main/planning/behavior_path_planner/autoware_behavior_path_planner/ | 🔍 |
| A95 | autoware_scenario_selector | https://autowarefoundation.github.io/autoware_universe/main/planning/autoware_scenario_selector/ | 🔍 |
| A96 | autoware_planning_validator | https://autowarefoundation.github.io/autoware_universe/main/planning/planning_validator/autoware_planning_validator/ | 🔍 |
| A97 | autoware_diffusion_planner | https://autowarefoundation.github.io/autoware_universe/main/planning/autoware_diffusion_planner/ | 🔍 |
| A98 | autoware_trajectory_ranker | https://autowarefoundation.github.io/autoware_universe/main/planning/autoware_trajectory_ranker/ | 🔍 |
| A99 | autoware_mrm_handler | https://autowarefoundation.github.io/autoware_universe/main/system/autoware_mrm_handler/ | 🔍 |
| A100 | autoware_diagnostic_graph_aggregator | https://autowarefoundation.github.io/autoware_universe/main/system/autoware_diagnostic_graph_aggregator/ | 🔍 |
| A101 | autoware_operation_mode_transition_manager | https://autowarefoundation.github.io/autoware_universe/main/control/autoware_operation_mode_transition_manager/ | 🔍 |
| A102 | autoware_raw_vehicle_cmd_converter | https://autowarefoundation.github.io/autoware_universe/main/vehicle/autoware_raw_vehicle_cmd_converter/ | 🔍 |
| A103 | autoware_pointcloud_preprocessor | https://autowarefoundation.github.io/autoware_universe/main/sensing/autoware_pointcloud_preprocessor/ | 🔍 |
| A104 | autoware_cuda_pointcloud_preprocessor (+ docs/cuda-pointcloud-preprocessor) | https://autowarefoundation.github.io/autoware_universe/main/sensing/autoware_cuda_pointcloud_preprocessor/ , https://autowarefoundation.github.io/autoware_universe/main/sensing/autoware_cuda_pointcloud_preprocessor/docs/cuda-pointcloud-preprocessor/ | 🔍 |
| A105 | autoware_pipeline_latency_monitor | https://autowarefoundation.github.io/autoware_universe/main/system/autoware_pipeline_latency_monitor/ | 🔍 |
| A106 | autoware_default_adapi (core) / autoware_default_adapi_universe | https://autowarefoundation.github.io/autoware_core/main/api/autoware_default_adapi/ , https://autowarefoundation.github.io/autoware_universe/main/system/autoware_default_adapi_universe/ | 🔍 |
| A107 | Autoware Overview (autoware.org) | https://autoware.org/autoware-overview/ | 🔍 |
| A108 | Autoware Foundation 2.0 (2025-06-03) | https://autoware.org/autoware-foundation-2-0-growing-together-toward-scalable-autonomy/ | 🔍 |
| A109 | autoware.org Announcements | https://autoware.org/category/announcements/ | 🔍 |
| A110 | autoware.org News | https://autoware.org/category/news/ | 🔍 |
| A111 | AWF partners with Renesas (2026-09-01) | https://autoware.org/autoware-foundation-partners-with-renesas-to-accelerate-production-ready-end-to-end-ai-for-adas-and-autonomous-driving/ | 🔍 |
| A112 | Neolix joins AWF (PR Newswire) | https://www.prnewswire.com/news-releases/neolix-technologies-joins-autoware-foundation-as-premium-member-to-deliver-fully-commercialized-autonomous-driving-solutions-to-the-ecosystem-302654988.html | 📰 |
| A113 | NATIX joins AWF (2026-04-13) | https://autoware.org/natix-joins-the-autoware-foundation/ | 🔍 |
| A114 | Open AD Kit: first SOAFEE blueprint (2025-11-24) | https://autoware.org/open-ad-kit-the-first-soafee-blueprint-powering-open-collaboration-in-autonomous-driving/ | 🔍 |
| A115 | Open Source Autonomy at CES 2026 | https://autoware.org/open-source-autonomy-will-have-a-moment-at-the-ces-2026/ | 🔍 |
| A116 | Autoware Tutorial & Workshop at IEEE IV 2026 | https://autoware.org/iv2026/ | 🔍 |
| A117 | AWF Members | https://autoware.org/about/members/ | 🔍 |
| A118 | Isuzu newsroom: TIER IV·Isuzu L4 buses on DRIVE Hyperion (2026-03-17) | https://www.isuzu-global.com/en/newsroom/20260317_1.html | 🔍 |
| A119 | TIER IV unveils AI-based L4 (PR Newswire, 2026-03-20) | https://www.prnewswire.com/news-releases/tier-iv-unveils-ai-based-level-4-autonomous-driving-accelerating-global-platform-expansion-across-japan-us-and-europe-302714131.html | 📰 |
| A120 | autoware_vision_pilot README | https://github.com/autowarefoundation/autoware_vision_pilot | 🔍 |
| A121 | AWF Discussion #2822 (CARET performance analysis) | https://github.com/orgs/autowarefoundation/discussions/2822 | 🔍(수치 미포함) |
| A122 | CARET paper / ROSCon 2022 (검색 결과) | https://ieeexplore.ieee.org/document/10086380/ , http://download.ros.org/downloads/roscon/2022/Chain-Aware%20ROS%20Evaluation%20Tool%20(CARET).pdf | 📰 |
| A123 | Agnocast arXiv 2506.16882 (검색 결과, 미열람) | https://arxiv.org/abs/2506.16882 | 📰 |

## [N] 2부B NVIDIA DRIVE AV·Alpamayo (55건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| N1 | NVIDIA DRIVE AV (제품 페이지) | https://www.nvidia.com/en-us/self-driving-cars/drive-av/ | 🔍 |
| N2 | NVIDIA DriveOS (개발자 페이지) | https://developer.nvidia.com/drive/os | 🔍 |
| N3 | NVIDIA DRIVE AGX Thor Development Platform (PDF, December 2025) | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | 🔍 |
| N4 | Full-Stack Safety for Robotaxis and AVs — NVIDIA Halos | https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/ | 🔍 |
| N5 | nvidia/Alpamayo-R1-10B 모델 카드 | https://huggingface.co/nvidia/Alpamayo-R1-10B | 🔍 |
| N6 | arXiv 2511.00088 Alpamayo-R1 (abs) | https://arxiv.org/abs/2511.00088 | 🔍 |
| N6b | arXiv 2511.00088 PDF(v2) 본문(pdftotext 열람) | https://arxiv.org/pdf/2511.00088 | 🔍 |
| N7 | HF 블로그 "Taking Alpamayo to New Heights…" (2026-06-01, Pavone·Ivanovic) | https://huggingface.co/blog/nvidia/nvidia-alpamayo-2 | 🔍 |
| N8 | NVIDIA 블로그 "Alpamayo 2 Super … Now Available for Commercial Use" (2026-08-04) | https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/ | 🔍 |
| N9 | NVIDIA 기술 블로그 "Generate Trajectories, Reasoning Traces, and Auto-Labels with Alpamayo 2 Super" (2026-08-04) | https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/ | 🔍 |
| N10 | GitHub NVlabs/alpamayo2 | https://github.com/NVlabs/alpamayo2 | 🔍 |
| N11 | NVIDIA 블로그 CES 2026 special presentation | https://blogs.nvidia.com/blog/2026-ces-special-presentation/ | 🔍 |
| N12 | NVIDIA 뉴스룸 Alpamayo 발표 (2026-01-05) | https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development | 🔍 |
| N13 | NVIDIA 블로그 "DRIVE AV Software Debuts in All-New Mercedes-Benz CLA" (2026-01-05) | https://blogs.nvidia.com/blog/drive-av-software-mercedes-benz-cla/ | 🔍 |
| N14 | NVIDIA DRIVE Hyperion 제품 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-hyperion/ | 🔍 |
| N15 | NVIDIA 뉴스룸 Uber 로보택시/Hyperion 10 (2025-10-28) | https://nvidianews.nvidia.com/news/nvidia-uber-robotaxi | 🔍 |
| N16 | nvidia/Alpamayo2-Super 모델 카드 | https://huggingface.co/nvidia/Alpamayo2-Super | 🔍 |
| N17 | GitHub NVlabs/alpamayo (Alpamayo 1) | https://github.com/NVlabs/alpamayo | 🔍 |
| N18 | NVIDIA Alpamayo LLM info 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/llm-info/ | 🔍 |
| N19 | NVIDIA 뉴스룸 Alpamayo 2 Super (2026-05-31, GTC Taipei) | https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis | 🔍 |
| N20 | NVIDIA 뉴스룸 Hyperion 안전·사이버보안 마일스톤 (2025-01-06) | https://nvidianews.nvidia.com/news/nvidia-drive-hyperion-platform-achieves-critical-automotive-safety-and-cybersecurity-milestones-for-av-development | 🔍 |
| N21 | NVIDIA In-Vehicle Computing 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/ | 🔍 |
| N22 | Bosch 보도자료 Thor 통합 (2025-09-30) | https://us.bosch-press.com/pressportal/us/en/press-release-28736.html | 🔍 |
| N23 | NVIDIA 블로그 Global DRIVE Hyperion Ecosystem (2026-01-05) | https://blogs.nvidia.com/blog/global-drive-hyperion-ecosystem-full-autonomy/ | 🔍 |
| N24 | NVIDIA 뉴스룸 BYD/Geely/Isuzu/Nissan Hyperion L4 (2026-03-16) | https://nvidianews.nvidia.com/news/drive-hyperion-level-4 | 🔍 |
| N25 | NVIDIA 뉴스룸 Hyperion Robotaxi-Ready World (2026-05-31) | https://nvidianews.nvidia.com/news/nvidia-drive-hyperion-becomes-the-global-platform-for-a-robotaxi-ready-world | 🔍 |
| N26 | Magna 보도자료 Hyperion-Compatible ECUs (2026-01-05) | https://www.magna.com/stories/news-press-release/2026/magna-to-offer-drive-hyperion-compatible-ecus-and-tier-1-integration-services-for-nvidia-drive-av | 🔍 |
| N27 | DriveOS 7.0.3 Virtualization overview | https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/embedded-software-components/DRIVE_AGX_SoC/Virtualization/devguide_overview.html | 🔍 |
| N28 | DriveOS 7.0.3 Linux SDK Introduction | https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/introduction/introduction.html | 🔍 |
| N29 | DriveOS 7.0.3 Virtualization Concepts | https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/core-concepts/FoundationServicesStack1.html | 🔍 |
| N30 | GitHub NVlabs/alpamayo-recipes | https://github.com/NVlabs/alpamayo-recipes | 🔍 |
| N31 | GitHub NVlabs/alpasim | https://github.com/NVlabs/alpasim | 🔍 |
| N32 | GitHub NVlabs/alpagym | https://github.com/NVlabs/alpagym | 🔍 |
| N33 | NVIDIA 기술 블로그 closed-loop post-training (2026-05-31) | https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/ | 🔍 |
| N34 | NVIDIA DriveWorks 페이지 | https://developer.nvidia.com/drive/driveworks | 🔍 |
| N35 | HF 데이터셋 nvidia/PhysicalAI-Autonomous-Vehicles | https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles | 🔍 |
| N36 | NVIDIA 개발자 포럼 "Alpamayo1.5 fp8 quantization for Thor" | https://forums.developer.nvidia.com/t/how-to-perform-alpamayo1-5-fp8-quantization-for-nvidia-thor/382409 | 🔍 |
| N37 | nvidia/Alpamayo-1.5-10B 모델 카드 | https://huggingface.co/nvidia/Alpamayo-1.5-10B | 🔍 |
| N38 | HF 블로그 (drmapavone) Alpamayo 1.5 (2026-03-16) | https://huggingface.co/blog/drmapavone/nvidia-alpamayo-1-5 | 🔍 |
| N39 | NVIDIA Alpamayo overview 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/ | 🔍 |
| N40 | NVIDIA 뉴스룸 Cosmos 3 (2026-05-31) | https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai | 🔍 |
| N41 | NVIDIA 블로그 auto ecosystem / Halos (2025-03-18) | https://blogs.nvidia.com/blog/auto-ecosystem-physical-ai/ | 🔍 |
| N42 | TensorRT for DRIVE OS 6.0.10 Release Notes (TensorRT 8.6.13) | https://developer.nvidia.com/docs/drive/drive-os/6.0.10/public/drive-os-tensorrt/release-notes/index.html | 🔍 |
| N43 | NVIDIA 8-K Q2 FY2026 실적 보도자료 | https://www.sec.gov/Archives/edgar/data/1045810/000104581025000207/q2fy26pr.htm | 🔍 |
| N44 | NVIDIA 뉴스룸 Halos for Robotics (2026-06-22) | https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai | 🔍 |
| N45 | NVIDIA 뉴스룸 DRIVE Thor 공개 (2022-09-20) | https://nvidianews.nvidia.com/news/nvidia-unveils-drive-thor-centralized-car-computer-unifying-cluster-infotainment-automated-driving-and-parking-in-a-single-cost-saving-system | 🔍 |
| N46 | NVIDIA DRIVE Documentation 포털 | https://developer.nvidia.com/drive/documentation | 🔍 |
| N47 | GitHub NVlabs/alpamayo1.5 | https://github.com/NVlabs/alpamayo1.5 | 🔍 |
| N48 | NVIDIA at CVPR 2026 (Alpamayo Summit 2026-06-04) | https://www.nvidia.com/en-us/events/cvpr/ | 🔍 |
| N49 | Lucid IR 보도자료 L4 with NVIDIA (2025-10-28) — fetch 타임아웃 | https://ir.lucidmotors.com/news-releases/news-release-details/lucid-intends-deliver-first-level-4-autonomous-evs-consumers | 📰 |
| N50 | GTC 2026 세션 S81779 / Alpamayo Summit on-demand | https://www.nvidia.com/en-us/on-demand/session/gtc26-s81779/ | 📰 |
| N51 | Mercedes-Benz Group MB.DRIVE ASSIST PRO — 403 | https://group.mercedes-benz.com/technology/autonomous-driving/driving/mb-drive-assist-pro.html | 📰 |
| N52 | eeNews Europe CES 2026 Hyperion 생태계 보도 | https://www.eenewseurope.com/en/nvidia-drive-hyperion-ecosystem-expands-ces-2026/ | 📰 |
| N53 | Cosmos 3 기술 보고서 PDF — 크기 초과 미열람 | https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf | ⚠️ |
| N54 | Electrek CLA Q1 2026 보도 | https://electrek.co/2026/01/05/nvidia-unveils-open-source-ai-for-autonomous-driving-ships-in-mercedes-benz-cla-in-q1-2026/ | 📰 |

## [D] 3부 데이터 플라이휠·검증 (72건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| D1 | Hyundai Motor Group, "Hyundai Motor Group Accelerates Autonomous Driving Innovation with AI-Powered Data Flywheel" (2026-09-13) | https://www.hyundai.com/worldwide/en/newsroom/detail/0000001273 | 🔍 |
| D2 | NVIDIA, "Cosmos World Foundation Model Platform for Physical AI" (arXiv 2501.03575, 2025-01-07/rev 2025-07-09) | https://arxiv.org/abs/2501.03575 · https://arxiv.org/html/2501.03575 | 🔍 |
| D3 | NVIDIA PhysicalAI-Autonomous-Vehicles dataset card (v26.09) | https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles | 🔍 |
| D4 | "Cosmos-Drive-Dreams: Scalable Synthetic Driving Data Generation with World Foundation Models" (arXiv 2506.09042, 2025-06-10) | https://arxiv.org/abs/2506.09042 · https://arxiv.org/html/2506.09042 | 🔍 |
| D5 | PR Newswire, "TIER IV to jointly develop next-generation development platform with Astemo ... Co-MLOps" (2026-08-04) | https://www.prnewswire.com/news-releases/tier-iv-to-jointly-develop-next-generation-development-platform-with-astemo-accelerating-e2e-autonomous-driving-ai-with-co-mlops-solution-302842437.html | 🔍 |
| D6 | PR Newswire, "TIER IV to showcase integrated AI, data, and computing solution for SDVs at Automotive World 2026" (2026-09-09~11) | http://www.prnewswire.com/news-releases/tier-iv-to-showcase-integrated-ai-data-and-computing-solution-for-sdvs-at-automotive-world-2026-302859969.html | 🔍 |
| D7 | Towards Data Science, "Tesla AI Day 2021 Review — Part 2: Training Data" | https://towardsdatascience.com/tesla-ai-day-2021-review-part-2-training-data-how-does-a-car-learn-e8863ba3f5b0/ | 📄 (2차 해설) |
| D8 | pharath.github.io, "Andrej Karpathy (Tesla): CVPR 2021 Workshop on Autonomous Vehicles" (강연 필기) | https://pharath.github.io/self%20driving/Karpathy-CVPR-2021/ | 📄 (3rd-party 필기) |
| D9 | The Money Carnival (Substack), "Tesla's AI Day Sep 2022" | https://themoneycarnival.substack.com/p/teslas-ai-day-sep-2022 | 📄 (2차 해설) |
| D10 | Drive Tesla Canada, "AI Day 2022: FSD Simplified" 등 검색 요약 | https://driveteslacanada.ca/news/ai-day-2022-fsd-simplified/ | 📰(원문 403) |
| D11 | codecompass00 (Substack), "How Tesla Continuously and Automatically Improves Autopilot ... trigger classifiers" (2024-04-17) | https://codecompass00.substack.com/p/tesla-data-engine-trigger-classifiers | 📄 (2차 해설) |
| D12 | Tesla Autonomy Day 2019 shadow mode 관련 검색 요약(teslarati 등) | https://www.teslarati.com/tesla-autonomy-day-livestream-updates/ | 📰 |
| D13 | Zhai et al., "Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes" (AD-MLP, arXiv 2305.10430) | https://arxiv.org/abs/2305.10430 | 🔍 |
| D14 | Li et al., "Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?" (arXiv 2312.03031, CVPR 2024) | https://arxiv.org/abs/2312.03031 | 🔍 |
| D15 | Dauner et al., "NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking" (arXiv 2406.15349) | https://arxiv.org/abs/2406.15349 · https://arxiv.org/html/2406.15349 | 🔍 |
| D16 | Cao et al., "Pseudo-Simulation for Autonomous Driving" (arXiv 2506.04218, CoRL 2025) | https://arxiv.org/abs/2506.04218 · https://arxiv.org/html/2506.04218 | 🔍 |
| D17 | Jia et al., "Bench2Drive" (arXiv 2406.03877, NeurIPS 2024 D&B) | https://arxiv.org/abs/2406.03877 · https://arxiv.org/html/2406.03877 | 🔍 |
| D18 | NVIDIA (Hugging Face blog), "Taking Alpamayo to New Heights with Driving Foundation Models and Closed-Loop Training" (2026-06-01) | https://huggingface.co/blog/nvidia/nvidia-alpamayo-2 | 🔍 |
| D19 | NVIDIA Newsroom, "NVIDIA Launches Alpamayo 2 Super Open Reasoning Model for Robotaxis" (GTC Taipei, 2026-05-31) | https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis | 🔍 |
| D20 | NVIDIA Technical Blog, "Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super" (2026-08-04) | https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/ | 🔍 |
| D21 | "Alpamayo-R1: Bridging Reasoning and Action Prediction ..." (arXiv 2511.00088, 2025-10-30) | https://arxiv.org/abs/2511.00088 | 🔍 |
| D22 | Waymo Blog, "10 AI Lessons from Driving 200+ Million Fully Autonomous Miles" (2026-08-26) | https://waymo.com/blog/2026/08/10ailessons/ | 🔍 |
| D23 | Waymo Safety Impact hub (데이터 기준 2026-03) | https://waymo.com/safety/impact/ | 🔍 |
| D24 | Waymo Driver 페이지(20B+ 시뮬 마일) | https://waymo.com/waymo-driver/ | 🔍 |
| D25 | Xu et al., "WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios" (arXiv 2510.26125) | https://arxiv.org/abs/2510.26125 | 🔍 |
| D26 | Gulino et al., "Waymax" (arXiv 2310.08710) | https://arxiv.org/abs/2310.08710 | 🔍 |
| D27 | Wayve, "GAIA-3: Scaling World Models to Power Safety and Evaluation" (2025-12-02) | https://wayve.ai/thinking/gaia-3/ | 🔍 |
| D28 | NVIDIA Omniverse NuRec 개발자 페이지 — https://developer.nvidia.com/omniverse/nurec — 🔍 ; Radiance Fields, "NVIDIA Omniverse NuRec Reaches General Availability" (GTC 2026-03-25) | https://radiancefields.com/nvidia-omniverse-nurec-reaches-general-availability | 🔍 |
| D29 | NVIDIA DriveWorks SDK, "High Throughput Recording" | https://developer.nvidia.com/docs/drive/drive-os/6.0.6/public/driveworks-nvsdk/dwx_recording_devguide_high_throughput_recording.html | 🔍 |
| D30 | NVIDIA Developer Forums, "DRIVE Hyperion 8.1 NAS Storage Bandwidth is low" | https://forums.developer.nvidia.com/t/drive-hyperion-8-1-nas-storage-bandwidth-is-low/209740 | 🔍 |
| D31 | AUTOCRYPT, "EDR and DSSAD: A Look at Vehicle Accident Analysis Tools" (2024-11-12) | https://autocrypt.io/edr-dssad-vehicle-accident-analysis-tools/ | 📄 (2차 해설) |
| D32 | IEEE SA, "IEEE 1616.1-2023 Standard for Data Storage Systems for Automated Driving" | https://standards.ieee.org/ieee/1616.1/10939/ | 🔍 |
| D33 | Abbaspour et al., "Dataset Safety in Autonomous Driving: Requirements, Risks, and Assurance" (arXiv 2511.08439, v2 2026-04-13) | https://arxiv.org/abs/2511.08439 · https://arxiv.org/html/2511.08439 | 🔍 |
| D34 | RAND, Kalra & Paddock, "Driving to Safety" (RR-1478, 2016) | https://www.rand.org/pubs/research_reports/RR1478.html | 📰(403) |
| D35 | RAND 보도자료 (2016-04-12) | https://www.rand.org/news/press/2016/04/12.html | 📰(403) |
| D36 | Webb et al., "Waymo's Safety Methodologies and Safety Readiness Determinations" (arXiv 2011.00054) | https://arxiv.org/abs/2011.00054 | 🔍 |
| D37 | Transport Topics, "New Autonomous Mileage Reports Are Out, but Is the Data Meaningful?" (2020-02-26) — https://www.ttnews.com/articles/new-autonomous-mileage-reports-are-out-data-meaningful — 🔍 ; Kyle Vogt, "The Disengagement Myth" | https://medium.com/cruise/the-disengagement-myth-1b5cbdf8e239 | 📰(403) |
| D38 | Waymo Blog, "The Waymo World Model: A New Frontier For Autonomous Driving Simulation" (2026-02-06) | https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/ | 🔍 |
| D39 | Kusano et al., "Comparison of Waymo Rider-Only Crash Rates by Crash Type to Human Benchmarks at 56.7 Million Miles" (arXiv 2505.01515; Traffic Injury Prevention 2025) | https://arxiv.org/abs/2505.01515 | 🔍 |
| D40 | Electrek, "Tesla's Autopilot safety data is getting worse" (2025-10-22) — https://electrek.co/2025/10/22/teslas-autopilot-safety-data-is-getting-worse/ — 📰 ; Tesla Vehicle Safety Report | https://www.tesla.com/VehicleSafetyReport | ⚠️(403) |
| D41 | O'Kelly et al., "Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation" (arXiv 1811.00145) | https://arxiv.org/abs/1811.00145 | 🔍 |
| D42 | Mobileye REM 공식 페이지(검색 요약) | https://www.mobileye.com/technology/rem/ | 📰 |
| D43 | Applied Intuition, "Explore Neural Sim" (2025-01-06) | https://www.appliedintuition.com/blog/neural-sim-announced | 🔍 |
| D44 | Applied Intuition, "Neural Sim for end-to-end SDS validation" (2025-10-14) | https://www.appliedintuition.com/blog/neural-sim-end-to-end-sds-validation | 🔍 |
| D45 | Wayve, "PRISM-1" (2024-06-17) | https://wayve.ai/thinking/prism-1/ | 🔍 |
| D46 | Wayve, "Ghost Gym: A Neural Simulator" (2023-12-21) | https://wayve.ai/thinking/ghost-gym-neural-simulator/ | 🔍 |
| D47 | Wayve, "GAIA-2" (2025-03-26) | https://wayve.ai/thinking/gaia-2/ | 🔍 |
| D48 | Applied Intuition Engineering Blog, "World Foundation Models for autonomy: from research to reality" (2026-06-18) | https://www.appliedintuition.com/engineering-blog/world-foundation-models-from-research-to-reality | 🔍 |
| D49 | Foretellix, "Foretellix Accelerates AI-Powered Autonomous Vehicles ..." (2025-05-21) | https://www.foretellix.com/foretellix-accelerates-ai-powered-autonomous-vehicles/ | 🔍 |
| D50 | Automotive Testing Technology International, "Foretellix integrates Foretify physical AI toolchain with Nvidia Drive AV platform" (2025-10-31) | https://www.automotivetestingtechnologyinternational.com/news/software-engineering-sdvs/foretellix-integrates-foretify-physical-ai-toolchain-with-nvidia-drive-av-platform.html | 🔍 |
| D51 | Foretellix, "Foretellix and Inverted AI Partner ..." (2025-11-13) | https://www.foretellix.com/foretellix-invertedai-scenario-ai/ | 🔍 |
| D52 | Yan et al., "AD-R1: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving with Impartial World Models" (CVPR 2026) | https://cvpr.thecvf.com/virtual/2026/poster/40620 | 📰(초록 미제공, PDF 403) |
| D53 | KITTI Vision Benchmark Suite | https://www.cvlibs.net/datasets/kitti/ | 🔍 |
| D54 | Caesar et al., "nuScenes" (arXiv 1903.11027) | https://arxiv.org/abs/1903.11027 | 🔍 |
| D55 | Sun et al., "Scalability in Perception for Autonomous Driving: Waymo Open Dataset" (arXiv 1912.04838) | https://arxiv.org/abs/1912.04838 | 🔍 |
| D56 | Caesar et al., "nuPlan" (arXiv 2106.11810) | https://arxiv.org/abs/2106.11810 | 🔍 |
| D57 | Dosovitskiy et al., "CARLA: An Open Urban Driving Simulator" (arXiv 1711.03938) | https://arxiv.org/abs/1711.03938 | 🔍 |
| D58 | dSPACE ASM 제품 페이지 | https://www.dspace.com/en/inc/home/products/sw/automotive_simulation_models.cfm | 🔍 |
| D59 | Aptiv, "What is vehicle-in-the-loop testing?" (2022-04-01) | https://www.aptiv.com/en/insights/article/what-is-vehicle-in-the-loop-testing | 🔍 |
| D60 | Foretellix, "ASAM OpenSCENARIO 2.0.0 is out; what's next?" | https://www.foretellix.com/asam-openscenario-2-0-0-is-out-whats-next/ | 🔍 |
| D61 | ASAM OpenSCENARIO v2.0.0 페이지(검색 요약) | https://www.asam.net/standards/detail/openscenario/v200/ | 📰 |
| D62 | PEGASUS Project, "Pegasus Method" | https://www.pegasusprojekt.de/en/pegasus-method | 🔍 |
| D63 | VVM Project | https://www.vvm-projekt.de/en/ | 🔍 |
| D64 | California DMV, Autonomous Vehicle Regulations | https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/california-autonomous-vehicle-regulations/ | 🔍 |
| D65 | ISO 21448:2022 (검색 요약; ISO 페이지 403) — https://www.iso.org/standard/77490.html — 📰 ; PatSnap 해설 | https://www.patsnap.com/resources/blog/articles/iso-21448-sotif-validation-for-ai-perception-systems-2/ | 📄 (2차) |
| D66 | UL Solutions, "Safety-Related Systems in Road Vehicles with AI Are Addressed in ISO/PAS 8800:2024" | https://www.ul.com/sis/blog/safety-related-systems-road-vehicles-artificial-intelligence-are-addressed-isopas-88002024 | 🔍 |
| D67 | TÜV Rheinland, "ISO/PAS 8800" | https://www.tuv.com/world/en/iso-pas-8800.html | 🔍 |
| D68 | UL Solutions, "UL 4600 Edition 3 Updates Incorporate Autonomous Trucking" (2023-03-17) | https://www.ul.com/news/ul-4600-edition-3-updates-incorporate-autonomous-trucking | 🔍 |
| D69 | NVIDIA Newsroom, "NVIDIA Announces Alpamayo Family ..." (CES, 2026-01-05) | https://nvidianews.nvidia.com/news/alpamayo-autonomous-vehicle-development | 🔍 |
| D70 | NVIDIA Blog, "GTC 2026: Live Updates" | https://blogs.nvidia.com/blog/gtc-2026-news/ | 🔍(AV 세부 수치 없음) |
| D71 | Carziqo 보도자료, closed-loop "Data Flywheel" (2026-01-06, 검색 요약) | https://finance.yahoo.com/news/carziqo-shortens-data-model-cycle-075000256.html | 📰 |
| D72 | Wayve 보도자료 검색 요약: GAIA-3 출시(2025-12-02), Nissan 로보택시 GTC 2026(2026-03), Uber 런던 자율주행 개시(2026-09-03) | https://wayve.ai/press/wayve-launches-gaia3/ · https://wayve.ai/press/wayve-uber-launch-autonomous-rides/ | 📰 |
| D73 | Kusano, Beatty, Schnelle, Favaro, Crary, Victor, "Collision Avoidance Testing of the Waymo Automated Driving System" (arXiv 2212.08148, 2022-12-15) | https://arxiv.org/abs/2212.08148 | 🔍 |

## [P] 4부 양산 스택 (66건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| P2 | EU AI Act Article 2 (미러) | https://artificialintelligenceact.eu/article/2/ | 📄 (비공식 미러) |
| P3 | EU AI Act Article 6 (미러) | https://artificialintelligenceact.eu/article/6/ | 📄 (비공식 미러) |
| P4 | NVIDIA Halos for Autonomous Vehicles | https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/ | 🔍 (벤더 주장) |
| P5 | NVIDIA DriveOS | https://developer.nvidia.com/drive/os | 🔍 (벤더 주장) |
| P6 | EB corbos Linux for Safety Applications | https://www.elektrobit.com/products/ecu/eb-corbos/linux-for-safety-applications/ | 🔍 (벤더 주장) |
| P7 | RTI Connext Drive | https://www.rti.com/products/connext-drive | 🔍 (벤더 주장) |
| P8 | Waymo, Meet the 6th-generation Waymo Driver | https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver | 🔍 (벤더 주장) |
| P9 | QNX Hypervisor and Hypervisor for Safety | https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety | 🔍 (벤더 주장) |
| P10 | Eclipse iceoryx2 GitHub | https://github.com/eclipse-iceoryx/iceoryx2 | 🔍 |
| P11 | Mobileye RSS | https://www.mobileye.com/technology/responsibility-sensitive-safety/ | 🔍 (벤더 주장) |
| P12 | Wikipedia, ISO 26262 | https://en.wikipedia.org/wiki/ISO_26262 | 📄 (Wikipedia) |
| P13 | Wikipedia, Tesla Autopilot | https://en.wikipedia.org/wiki/Tesla_Autopilot | 📄 (Wikipedia) |
| P14 | Eclipse S-CORE project page | https://projects.eclipse.org/projects/automotive.score | 🔍 |
| P15 | Eclipse S-CORE site | https://eclipse.dev/score/ | 🔍 |
| P16 | Autoware mrm_handler | https://autowarefoundation.github.io/autoware_universe/main/system/autoware_mrm_handler/ | 🔍 |
| P17 | Waymo, Fleet response | https://waymo.com/blog/2024/05/fleet-response | 🔍 (벤더 주장) |
| P18 | Waymo Safety | https://waymo.com/safety/ | 🔍 (벤더 주장) |
| P19 | NVIDIA blog, Mercedes-Benz CLA DRIVE AV | https://blogs.nvidia.com/blog/drive-av-mercedes-benz-cla/ | 🔍 (벤더 주장) |
| P20 | NVIDIA In-Vehicle Computing (DRIVE AGX Thor) | https://www.nvidia.com/en-us/self-driving-cars/in-vehicle-computing/ | 🔍 (벤더 주장) |
| P21 | NVIDIA TensorRT | https://developer.nvidia.com/tensorrt | 🔍 (벤더 주장) |
| P22 | Infineon AURIX TriCore | https://www.infineon.com/products/microcontroller/32-bit-tricore | 🔍 (벤더 주장) |
| P23 | BMW Group press, 7 Series L2+L3 | https://www.press.bmwgroup.com/global/article/detail/T0438214EN/the-new-bmw-7-series-is-the-first-car-in-the-world-to-combine-level-2-and-level-3 | 🔍 (벤더 주장) |
| P24 | Casini et al., ECRTS 2019 | https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECRTS.2019.6 | 🔍 (학술) |
| P25 | IEEE 802.1AS-2020 | https://1.ieee802.org/tsn/802-1as-2020/ | 🔍 |
| P26 | 49 CFR Part 563 (govinfo 2023) | https://www.govinfo.gov/content/pkg/CFR-2023-title49-vol6/xml/CFR-2023-title49-vol6-part563.xml | 🔍 (공식) |
| P27 | Koopman, UL 4600 page | https://users.ece.cmu.edu/~koopman/ul4600/index.html | 🔍 |
| P28 | Wikipedia, Automated Lane Keeping Systems | https://en.wikipedia.org/wiki/Automated_Lane_Keeping_Systems | 📄 (Wikipedia) |
| P29 | TIER IV Updates | https://tier4.co.jp/en/updates | 🔍(제목) |
| P30 | Wikipedia, Self-driving car | https://en.wikipedia.org/wiki/Self-driving_car | 📄 (Wikipedia) |
| P31 | Wikipedia, Tesla Full Self-Driving | https://en.wikipedia.org/wiki/Tesla_Full_Self-Driving | 📄 (Wikipedia) |
| P32 | Uptane | https://uptane.org/ | 🔍 |
| P33 | Project ACRN | https://projectacrn.org/ | 🔍 |
| P34 | Autoware GitHub | https://github.com/autowarefoundation/autoware | 🔍 |
| P35 | Wikipedia, Waymo | https://en.wikipedia.org/wiki/Waymo | 📄 (Wikipedia) |
| P36 | Wikipedia, Mercedes-Benz CLA | https://en.wikipedia.org/wiki/Mercedes-Benz_CLA | 📄 (Wikipedia) |
| P36b | Wikipedia, Mercedes-Benz S-Class (W223) | https://en.wikipedia.org/wiki/Mercedes-Benz_S-Class_(W223) | 📄 (Wikipedia) |
| P37 | Wikipedia, Aurora Innovation | https://en.wikipedia.org/wiki/Aurora_Innovation | 📄 (Wikipedia) |
| P38 | Aurora IR press releases | https://ir.aurora.tech/news-events/press-releases | 🔍(제목) |
| P39 | Wikipedia, Regulation of self-driving cars | https://en.wikipedia.org/wiki/Regulation_of_self-driving_cars | 📄 (Wikipedia) |
| P40 | Wikipedia, Event data recorder | https://en.wikipedia.org/wiki/Event_data_recorder | 📄 (Wikipedia) |
| P41 | Wikipedia, Mobileye | https://en.wikipedia.org/wiki/Mobileye | 📄 (Wikipedia) |
| P42 | Mobileye True Redundancy | https://www.mobileye.com/technology/true-redundancy/ | 🔍 (벤더 주장) |
| P43 | ekxide | https://ekxide.io/ | 🔍 (벤더 주장) |
| P44 | Wikipedia, WP.29 | https://en.wikipedia.org/wiki/World_Forum_for_Harmonization_of_Vehicle_Regulations | 📄 (Wikipedia) |
| P45 | ROS 2 Real-Time WG | https://ros-realtime.github.io/ | 🔍 |
| P46 | FR 2026-15483 AV Framework Updates | https://www.federalregister.gov/documents/2026/07/31/2026-15483/av-framework-updates-and-request-for-comments-on-interim-guidance | 🔍 (공식) |
| P47 | FR 2026-17741 comment extension | https://www.federalregister.gov/documents/2026/08/31/2026-17741/av-framework-updates-and-request-for-comments-on-interim-guidance-extension-of-comment-period | 🔍 (공식, 메타데이터) |
| P48 | FR 2026-15485 Zoox exemption | https://www.federalregister.gov/documents/2026/07/31/2026-15485/zoox-grant-of-temporary-exemption-from-portions-of-various-requirements-of-the-federal-motor-vehicle | 🔍 (공식) |
| P49 | FR 2026-15484 ADS guidance update | https://www.federalregister.gov/documents/2026/07/31/2026-15484/updating-and-expanding-guidance-on-safe-development-and-deployment-of-automated-driving-systems | 🔍 (공식, 메타데이터) |
| P50 | FR 2026-12981 FMVSS 135 NPRM | https://www.federalregister.gov/documents/2026/06/26/2026-12981/federal-motor-vehicle-safety-standards-modernization-of-fmvss-no-135-to-accommodate-ads-equipped | 🔍 (공식, 메타데이터) |
| P51 | FR 2026-12980 AV STEP withdrawal | https://www.federalregister.gov/documents/2026/06/26/2026-12980/ads-equipped-vehicle-safety-transparency-and-evaluation-program-withdrawal | 🔍 (공식, 메타데이터) |
| P52 | FR 2026-15486 Robomart | https://www.federalregister.gov/documents/2026/07/31/2026-15486/robomart-inc-receipt-of-application-for-temporary-exemption-from-various-requirements-of-the-federal | 🔍 (공식, 메타데이터) |
| P53 | NVIDIA blog, Introducing NVFP4 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ | 🔍 (벤더 주장) |
| P54 | arXiv search "PAS 8800" | https://arxiv.org/search/?query=%22PAS+8800%22&searchtype=all | 🔍 (arXiv 목록·초록) |
| P55 | Wikipedia, Aumovio | https://en.wikipedia.org/wiki/Aumovio | 📄 (Wikipedia) |
| P56 | arXiv search "ROS 2 executor" | https://arxiv.org/search/?query=ROS+2+executor&searchtype=all | 🔍 (arXiv 목록·초록) |
| P57 | FR 2026-15483 full text | https://www.federalregister.gov/documents/full_text/html/2026/07/31/2026-15483.html | 🔍 (공식) |
| P58 | FR 2026-10363 incident reporting (OMB) | https://www.federalregister.gov/documents/2026/05/26/2026-10363/agency-information-collection-activities-submission-to-the-office-of-management-and-budget-for | 🔍 (공식, 메타데이터) |
| P59 | FR 2026-04240 incident reporting (comment) | https://www.federalregister.gov/documents/2026/03/04/2026-04240/agency-information-collection-activities-notice-and-request-for-comment-incident-reporting-for | 🔍 (공식, 메타데이터) |
| P60 | arXiv 2601.10722 ROS 2 RT survey | https://arxiv.org/abs/2601.10722 | 🔍 (학술) |
| P61 | arXiv 2511.08439 Dataset Safety | https://arxiv.org/abs/2511.08439 | 🔍 (학술) |
| P62 | Apex.AI home | https://www.apex.ai/ | 🔍 (벤더 주장) |
| P62a | arXiv 2404.12683 Containerized ROS 2 AD latency | https://arxiv.org/abs/2404.12683 | 🔍 (학술) |
| P63 | arXiv search runtime monitoring | https://arxiv.org/search/?query=runtime+monitoring+autonomous+driving+safety+fallback&searchtype=all | 🔍 (arXiv 목록·초록) |
| P64 | arXiv search GPU timing | https://arxiv.org/search/?query=GPU+timing+predictability+embedded+autonomous&searchtype=all | 🔍 (arXiv 목록·초록) |
| P65 | arXiv search Autoware latency | https://arxiv.org/search/?query=Autoware+latency&searchtype=all | 🔍 (arXiv 목록·초록) |

## [F] 5부 미래 방향 (57건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| F1 | Waymo, "Demonstrably safe AI for autonomous driving" (2025-12-09) | https://waymo.com/blog/2025/12/demonstrably-safe-ai-for-autonomous-driving | 🔍 |
| F2 | NVIDIA, Alpamayo 제품 페이지 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/ | 🔍 |
| F3 | NVIDIA Blog, "Alpamayo 2 Super ... Now Available for Commercial Use" (2026-08-04) | https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/ | 🔍 |
| F4 | arXiv 2511.00088 Alpamayo-R1 | https://arxiv.org/abs/2511.00088 | 🔍 |
| F5 | arXiv 2608.12932 FlashDrive | https://arxiv.org/abs/2608.12932 | 🔍 |
| F6 | arXiv 2608.30144 Rethinking Language's Role in Efficient VLA | https://arxiv.org/abs/2608.30144 | 🔍 |
| F7 | arXiv 2609.03602 SV-WAM | https://arxiv.org/abs/2609.03602 | 🔍 |
| F8 | arXiv 2510.12796 DriveVLA-W0 | https://arxiv.org/abs/2510.12796 | 🔍 |
| F9 | arXiv 2607.09045 Can the Cloud Drive? | https://arxiv.org/abs/2607.09045 | 🔍 |
| F10 | arXiv 2410.23262 EMMA | https://arxiv.org/abs/2410.23262 | 🔍 |
| F11 | Wikipedia, Tesla Robotaxi | https://en.wikipedia.org/wiki/Tesla_Robotaxi | 📄 (Wikipedia) |
| F12 | Wikipedia, Tesla Cybercab | https://en.wikipedia.org/wiki/Tesla_Cybercab | 📄 (Wikipedia) |
| F13 | Wikipedia, Tesla Autopilot hardware | https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware | 📄 (Wikipedia) |
| F14 | Wikipedia, XPeng | https://en.wikipedia.org/wiki/XPeng | 📄 (Wikipedia) |
| F15 | Wikipedia, Nio Inc. | https://en.wikipedia.org/wiki/Nio_Inc. | 📄 (Wikipedia) |
| F16 | Wikipedia, Horizon Robotics | https://en.wikipedia.org/wiki/Horizon_Robotics | 📄 (Wikipedia) |
| F17 | Wikipedia, Nvidia Drive | https://en.wikipedia.org/wiki/Nvidia_Drive | 📄 (Wikipedia) |
| F18 | Wikipedia, Mobileye | https://en.wikipedia.org/wiki/Mobileye | 📄 (Wikipedia) |
| F19 | Waymo, "The Waymo World Model" (2026-02-06) | https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation | 🔍 |
| F20 | Wayve, "GAIA-4" (2026-08-03) | https://wayve.ai/thinking/gaia-4/ | 🔍 |
| F21 | Wayve, "Building Intelligence That Can Act in the World" (2026-05-29) | https://wayve.ai/thinking/building-intelligence-that-can-act-in-the-world/ | 🔍 |
| F22 | NVIDIA Blog, "Physical AI Takes the Wheel" (2026-09-10) | https://blogs.nvidia.com/blog/robotaxi-leaders-full-stack-open-platform/ | 🔍 |
| F23 | arXiv 2609.06055 DriveZero | https://arxiv.org/abs/2609.06055 | 🔍 |
| F24 | arXiv 2603.14972 TakeVLA | https://arxiv.org/abs/2603.14972 | 🔍 |
| F25 | arXiv 2605.10034 Beyond Self-Play and Scale | https://arxiv.org/abs/2605.10034 | 🔍 |
| F26 | arXiv 2608.28404 Scaling Law Analysis of Video Diffusion (5,500 h) | https://arxiv.org/abs/2608.28404 | 🔍 |
| F27 | arXiv 검색 "scaling law autonomous driving" | https://arxiv.org/search/?query=scaling+law+autonomous+driving&searchtype=all | 📰 |
| F28 | arXiv 검색 RL post-training closed-loop | https://arxiv.org/search/?query=reinforcement+learning+post-training+end-to-end+driving+closed-loop&searchtype=all | 📰 |
| F29 | arXiv 2406.06978 Hydra-MDP | https://arxiv.org/abs/2406.06978 | 🔍 |
| F30 | arXiv 2411.15139 DiffusionDrive | https://arxiv.org/abs/2411.15139 | 🔍 |
| F31 | arXiv 2605.17268 Is VLA Reasoning Faithful? | https://arxiv.org/abs/2605.17268 | 🔍 |
| F32 | arXiv 검색 "Alpamayo" | https://arxiv.org/search/?query=Alpamayo&searchtype=all | 📰 |
| F33 | Wayve, "A Global Regulatory Breakthrough..." (2026-02-10) | https://wayve.ai/thinking/a-global-regulatory-breakthrough-for-assisted-and-automated-driving/ | 📄 (회사 해석, UNECE 원문 미확인) |
| F34 | arXiv 검색 "ISO PAS 8800" | https://arxiv.org/search/?query=ISO+PAS+8800&searchtype=all | 📰 |
| F35 | Autoware Foundation 홈 | https://autoware.org/ | 🔍 |
| F36 | NVIDIA Newsroom 검색(alpamayo) | https://nvidianews.nvidia.com/news?q=alpamayo | 🔍(목록만) |
| F37 | ROS 2 docs, Release-Lyrical-Luth.rst | https://raw.githubusercontent.com/ros2/ros2_documentation/rolling/source/Releases/Release-Lyrical-Luth.rst | 🔍 |
| F38 | REP 2000 | https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-2000.rst | 🔍 |
| F39 | GitHub ros2/rmw_zenoh | https://github.com/ros2/rmw_zenoh | 🔍 |
| F40 | Eclipse Projects, automotive.score | https://projects.eclipse.org/projects/automotive.score | 🔍 |
| F41 | Eclipse S-CORE docs | https://eclipse-score.github.io/score/main/ | 🔍 |
| F42 | GitHub eclipse-score/score releases | https://github.com/eclipse-score/score/releases | 📰 |
| F43 | Ferrocene | https://ferrocene.dev/en/ | 🔍 |
| F44 | Wayve, "Autonomy for Any Vehicle, Anywhere" (2026-03-06) | https://wayve.ai/thinking/the-path-to-autonomy/ | 🔍 |
| F45 | Waymo, "Opening our doors to Tokyo riders in 2027" (2026-09-14) | https://waymo.com/blog/2026/09/opening-tokyo-in-2027-with-nihon-kotsu-go | 🔍 |
| F46 | Wikipedia, Waymo | https://en.wikipedia.org/wiki/Waymo | 📄 (Wikipedia) |
| F47 | Waymo, safety data June 2026 | https://waymo.com/blog/shorts/safetydata-june26/ | 🔍 |
| F48 | Waymo Blog 목록 | https://waymo.com/blog/ | 🔍 |
| F49 | Waymo, "Vegas, Deal Us In!" (2026-09-14) | https://waymo.com/blog/2026/09/ride-in-las-vegas | 🔍 |
| F50 | Wikipedia, Tesla Autopilot | https://en.wikipedia.org/wiki/Tesla_Autopilot | 📄 (Wikipedia) |
| F51 | Wikipedia, Apollo Go | https://en.wikipedia.org/wiki/Apollo_Go | 📄 (Wikipedia) |
| F52 | Wikipedia, WeRide | https://en.wikipedia.org/wiki/WeRide | 📄 (Wikipedia) |
| F53 | Wikipedia, Pony.ai | https://en.wikipedia.org/wiki/Pony.ai | 📄 (Wikipedia) |
| F54 | Wikipedia, Momenta | https://en.wikipedia.org/wiki/Momenta | 📄 (Wikipedia) |
| F55 | Wikipedia, Wayve | https://en.wikipedia.org/wiki/Wayve | 📄 (Wikipedia) |
| F56 | Wayve Blog 목록 | https://wayve.ai/thinking/ | 🔍 |
| F57 | Wikipedia, Yinwang (Huawei) | https://en.wikipedia.org/wiki/Yinwang | 📄 (Wikipedia) |

## [V] 약한 근거 재검증 (38건)

| ID | 제목 | URL | 등급 |
|---|---|---|---|
| V1 | Nio Onvo to equip updated L90 with Shenji NX9031 (CnEVPost) (2026-04-11) | https://cnevpost.com/2026/04/11/nio-onvo-to-equip-updated-l90-with-shenji-nx9031-chip/ | 📄 |
| V2 | 5 Major Updates We Learned at NIO IN Shanghai Event (2024-07) | https://globalchinaev.com/post/5-major-updates-we-learned-at-nio-in-shanghai-event | 📄 |
| V3 | Nio Inc. (Wikipedia) (2026-09 조회) | https://en.wikipedia.org/wiki/Nio_Inc. | 📄 |
| V4 | XPENG Turing AI Chip (XPeng 공식) (날짜 미표기) | https://www.xpeng.com/au/insight/xpeng_turing_ai_chip | 🔍 |
| V5 | Xpeng details its new AI Turing chip (CarNewsChina) (2024-11-06) | https://carnewschina.com/2024/11/06/xpeng-details-its-new-ai-turing-chip-that-it-will-use-in-its-cars/ | 📄 |
| V6 | XPENG Accelerates Global Deployment of VLA 2.0 (XPeng Pressroom) (2026-03-02) | https://www.xpeng.com/pressroom/news/019cae5e67b99c0960ee8a028129016a | 🔍 |
| V7 | The Computing Power Race of NIO, XPeng, and Li Auto (ChinaEVHome) (2025-06-20) | https://chinaevhome.com/2025/06/20/the-computing-power-race-of-nio-xpeng-and-li-auto/ | 📄 |
| V8 | XPeng X9 Ultra unveiled with 2250 TOPS (CarNewsChina) (2025-11-11) | https://carnewschina.com/2025/11/11/xpeng-x9-ultra-ev-unveiled-with-2250-tops-computing-power/ | 📄 |
| V9 | Journey 6 Series (Horizon 공식) (날짜 미표기) | https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6 | 🔍 |
| V10 | 地平线发布国产智驾芯片征程6P (车质网) (2025-04-19) | https://www.12365auto.com/news/20250419/546385.shtml | 📄 |
| V11 | GAR UN R157 modifications (—) | https://globalautoregs.com/modifications?rule_id=247 | 📄 |
| V12 | UN Regulation increases automated driving speed limit to 130 km/h (Future Transport-News) (2022-06) | https://futuretransport-news.com/un-regulation-increases-automated-driving-speed-limit-to-130km-h/ | 📄 |
| V13 | InterRegs: Updated UN ECE Regulation on ALKS Published (2023-03) | https://www.interregs.com/articles/spotlight/252/updated-un-ece-regulation-on-automated-lane-keeping-systems-published- | 📄 |
| V14 | Automated lane keeping systems (Wikipedia) (—) | https://en.wikipedia.org/wiki/Automated_lane_keeping_systems | 📄 |
| V15 | Regulation (EU) 2019/2144 Annex II (legislation.gov.uk 원문 사본) (2019-11-27 채택) | https://www.legislation.gov.uk/eur/2019/2144/annex/II/adopted | 🔍 |
| V16 | Information regarding type approval for Cyber Security and Software updates (Scania) (날짜 미표기) | https://bodybuilder.scania.com/content/dam/bodybuilder/bbb-files/type-approval/Type_approval_R155_and_R156.pdf | 🔍 |
| V17 | New DCAS regulation adopted by UNECE (CAD Europe) (2025-01-08) | https://www.connectedautomateddriving.eu/blog/new-dcas-regulation-adopted-by-unece/ | 📄 |
| V18 | UN R171 DCAS 01 series vs 00 series (ATIC) (2025-04-07) | https://www.atic-ts.com/un-r171-dcas-01-series-and-00-series-comparison-and-analysis/ | 📄 |
| V19 | GAR WP.29/2026/86 (R171 02 series proposal) (2026-04-14) | https://globalautoregs.com/documents/42373 | 📄 |
| V20 | Tesla FSD Regulations for the EU and UK: UN R171 Explained (2026-08-06) | https://notanfsdtracker.com/tesla-fsd-regulations-eu-uk-unece-dcas-un-r171 | 📄 |
| V21 | NVIDIA DRIVE Hyperion 제품 페이지 (2026-09 조회) | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-hyperion/ | 🔍 |
| V22 | NVIDIA Makes the World Robotaxi-Ready With Uber Partnership (Newsroom) (2025-10-28) | https://nvidianews.nvidia.com/news/nvidia-uber-robotaxi | 🔍 |
| V23 | Physical AI Takes the Wheel (NVIDIA Blog) (2026-09-10) | https://blogs.nvidia.com/blog/robotaxi-leaders-full-stack-open-platform/ | 🔍 |
| V24 | NVIDIA Launches Alpamayo 2 Super (Newsroom) (2026-05-31) | https://nvidianews.nvidia.com/news/nvidia-alpamayo-2-super-robotaxis | 🔍 |
| V25 | Taking Alpamayo to New Heights (HF blog) (2026-06-01) | https://huggingface.co/blog/nvidia/nvidia-alpamayo-2 | 🔍 |
| V26 | Alpamayo 2 Super now available for commercial use (NVIDIA Blog) (2026-08-04) | https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/ | 🔍 |
| V27 | nvidia/Alpamayo2-Super 모델카드 (2026-08-04) | https://huggingface.co/nvidia/Alpamayo2-Super | 🔍 |
| V28 | Mercedes-Benz DRIVE PILOT 95 km/h (그룹 페이지 403 → 제목·요약만) (2024-12-17) | https://group.mercedes-benz.com/technology/autonomous-driving/driving/drive-pilot-95-kmh.html · https://www.electrive.com/2024/12/17/mercedes-receives-approval-for-new-autonomous-system-in-germany/ | 📰 |
| V29 | Mercedes pauses Level 3 driving assistance – for now (electrive) (2026-01-12) | https://www.electrive.com/2026/01/12/mercedes-pauses-level-3-driving-assistance-for-now/ | 📄 |
| V30 | Mercedes-Benz shifts autonomous driving tech in 2026 S-Class (WardsAuto) (2026-02-11) | https://www.wardsauto.com/news/mercedes-benz-shifts-autonomous-driving-tech-in-2026-s-class/811431/ | 📄 |
| V31 | 工业和信息化部许可两款L3级自动驾驶车型产品 (新华网) (2025-12-15) | http://www.news.cn/tech/20251215/31e9de0148a74d20ba70d22a9cef3db0/c.html | 📄 |
| V32 | China grants 1st L3 autonomous driving permits (CnEVPost) (2025-12-15) | https://cnevpost.com/2025/12/15/china-grants-1st-l3-autonomous-driving-permits-passenger-cars/ | 📄 |
| V33 | China's first L3 autonomous driving permits (Xinhua EN) (2025-12-17) | https://english.news.cn/20251217/71c203bbccfa40b8af15718bff40341b/c.html | 📄 |
| V34 | DriveOS 7.0.3 TensorRT Release Notes – New Features (—) | https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-tensorrt-release-notes/features-enhancements.html | 🔍 |
| V35 | NVIDIA TensorRT 11.0.1 Developer Guide, Release 7.2.5 for DriveOS (PDF) (2026-05-11) | https://developer.nvidia.com/docs/drive/drive-os/7.2.5/public/NVIDIA-TensorRT-Developer-Guide.pdf | 🔍 |
| V36 | 2026.2.9.6 release notes (Not a Tesla App) (2026-04) | https://www.notateslaapp.com/software-updates/version/2026.2.9.6/release-notes | 📄 |
| V37 | Tesla rolls out FSD v14.3 (Tesla Oracle) (2026-04-08) | https://www.teslaoracle.com/2026/04/08/tesla-rolls-out-fsd-v14-3-2026-2-9-6-better-reaction-time-rewritten-ai-compiler-mlir-release-notes-status/ | 📄 |
| V38 | Tesla FSD v14.3 rolls out with MLIR rewrite (Electrek) (2026-04-07) | https://electrek.co/2026/04/07/tesla-fsd-14-3-rolling-out-mlir-lattner/ | 📰 |

## [K] 고정 커밋 소스 코드 (13건)

판정표와 파일·줄 근거: [code-autoware.md](code-autoware.md) · [code-alpamayo.md](code-alpamayo.md) · 기준 커밋 [code-pins.md](code-pins.md)

| ID | 저장소 · 기준 | URL | 등급 |
|---|---|---|---|
| K1 | autowarefoundation/autoware @ 1.9.0 (커밋 1071878, 2026-09-15 클론) | https://github.com/autowarefoundation/autoware/tree/10718787ba6e28f038a0cb29ff99cc627b5abfd2 | 💻 |
| K2 | autowarefoundation/autoware_core @ 1.9.0 (커밋 f25f83c, 2026-09-15 클론) | https://github.com/autowarefoundation/autoware_core/tree/f25f83c632c1984ec276c894c41857d4abc0dad8 | 💻 |
| K3 | autowarefoundation/autoware_universe @ 0.52.1 (커밋 02a5892, 2026-09-15 클론) | https://github.com/autowarefoundation/autoware_universe/tree/02a589200c1af644ca4b4cb3ed98695b4b62118b | 💻 |
| K4 | autowarefoundation/autoware_launch @ 0.52.0 (커밋 f942598, 2026-09-15 클론) | https://github.com/autowarefoundation/autoware_launch/tree/f942598d44b5769353167c76b784323d5c14c8c7 | 💻 |
| K5 | autowarefoundation/autoware_msgs @ 1.13.0 (커밋 bb8e7bf, 2026-09-15 클론) | https://github.com/autowarefoundation/autoware_msgs/tree/bb8e7bf5d97168663e0e7b357929e4fcdbd3a967 | 💻 |
| K6 | NVlabs/alpamayo (Alpamayo 1) @ main (커밋 11a0e01, 2026-09-15 클론) | https://github.com/NVlabs/alpamayo/tree/11a0e01c13a5622377c45ee37d653351453ec43b | 💻 |
| K7 | NVlabs/alpamayo1.5 @ main (커밋 36aeb4c, 2026-09-15 클론) | https://github.com/NVlabs/alpamayo1.5/tree/36aeb4c5938cbc2eb2aed33b22434773da4ab639 | 💻 |
| K8 | NVlabs/alpamayo2 @ main (커밋 6d05b9f, 2026-09-15 클론) | https://github.com/NVlabs/alpamayo2/tree/6d05b9f2dcaa6ee45ac6e053cf18653eac23c047 | 💻 |
| K9 | NVlabs/alpamayo-recipes @ main (커밋 670b551, 2026-09-15 클론) | https://github.com/NVlabs/alpamayo-recipes/tree/670b551987280979c157c1cb70b042458dbacc99 | 💻 |
| K10 | autowarefoundation/alpamayo-autoware @ alpamayo1.5 (커밋 65eda63, 2026-09-15 클론) | https://github.com/autowarefoundation/alpamayo-autoware/tree/65eda63b70460fc806a3dd1c619475e1d3bdbe28 | 💻 |
| K11 | autowarefoundation/alpamayo-autoware @ alpamayo2.0-super (커밋 b8747df, 2026-09-15 클론) | https://github.com/autowarefoundation/alpamayo-autoware/tree/b8747df228afd0e0d40d10fcfebd7b827325d50b | 💻 |
| K12 | autowarefoundation/alpamayo-autoware @ main (커밋 4e1c387, 2026-09-15 클론) | https://github.com/autowarefoundation/alpamayo-autoware/tree/4e1c3874a0d58c48369592d5ee6dad9e2ea14a01 | 💻 |
| K13 | NVIDIA/TensorRT-Edge-LLM @ v0.10.1 (커밋 e8b2952, 2026-09-15 클론) | https://github.com/NVIDIA/TensorRT-Edge-LLM/tree/e8b29522938901f6df19ebeedd4b69bc8edbcd97 | 💻 |
