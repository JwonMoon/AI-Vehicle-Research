# 이미지 출처 목록

> 작성일 2026-09-02. `images/` 폴더의 모든 파일과 출처·저작권·사용 위치. 외부 그림은 설명·인용 목적으로만 사용하며 원 저작권은 각 소유자에게 있다. 접근 불가(nvidia.com·arXiv)로 내려받지 못한 그림은 문서 본문에 링크만 남겼다.

## 자체 작성 (SVG)

| 파일 | 설명 | 사용 문서 |
|---|---|---|
| `3-0-av-stack-map.svg` | NVIDIA 자율주행 스택 계층·3-computer 위치·성숙도 요약 지도 | 3장 3.0.3 |
| `7-0-cosmos-map.svg` | Cosmos 모델군·Omniverse 위치·역할·성숙도 요약 지도 | 7장 7.0.3 |
| `7-2-data-flywheel.svg` | AV 데이터 플라이휠에서 Cosmos/Omniverse 구성 요소가 붙는 지점 | 7장 7.2.4 |
| `7-3-omniverse-cosmos-pipeline.svg` | Omniverse 출력 → Cosmos Transfer 조건 입력 결합 구조 | 7장 7.3.3 |
| `appendix-a-tier1-workmap.svg` | NVIDIA 제공 범위 vs Tier-1 책임 레이어 지도 + 차별화 매트릭스 | 부록 A A.3 |

규약: 실선 = 출처로 확인, 점선 = 추정. 색: 파랑 = 3장 범위, 초록 = Cosmos, 주황 = Omniverse, 회색 = 다른 장/NVIDIA 제공, 노랑·빨강 = Tier-1 책임.

## 외부 출처 (GitHub에서 내려받음)

| 파일 | 원본 URL | 페이지 | 저작권·라이선스 | 사용 문서 |
|---|---|---|---|---|
| `3-1-alpamayo2-super-architecture.png` | https://raw.githubusercontent.com/NVlabs/alpamayo2/main/alpamayo2super_arch.png | https://github.com/NVlabs/alpamayo2 | © NVIDIA, 저장소 코드 Apache-2.0 | 3장 3.1.2 |
| `3-2-alpasim-architecture.png` | https://raw.githubusercontent.com/NVlabs/alpasim/main/docs/assets/images/alpasim-architecture.png | https://github.com/NVlabs/alpasim/blob/main/docs/DESIGN.md | © NVIDIA, Apache-2.0 | 3장 3.2.6 |
| `3-2-alpasim-demo.gif` | https://raw.githubusercontent.com/NVlabs/alpasim/main/docs/assets/images/thumbnail.gif | https://github.com/NVlabs/alpasim | © NVIDIA, Apache-2.0 | 3장 3.2.6 |
| `7-1-cosmos3-architecture.png` | https://raw.githubusercontent.com/NVIDIA/Cosmos/main/cookbooks/cosmos3/cosmos3-model-architecture.png | https://github.com/NVIDIA/Cosmos | © NVIDIA, OpenMDW-1.1 | 7장 7.1.4 |
| `7-1-predict1-diagram.png` | https://raw.githubusercontent.com/nvidia-cosmos/cosmos-predict1/main/assets/predict1_diagram.png | https://github.com/nvidia-cosmos/cosmos-predict1 | © NVIDIA, 코드 Apache-2.0 | 7장 7.1.2 |
| `7-1-transfer1-diagram.png` | https://raw.githubusercontent.com/nvidia-cosmos/cosmos-transfer1/main/assets/transfer1_diagram.png | https://github.com/nvidia-cosmos/cosmos-transfer1 | © NVIDIA, 코드 Apache-2.0 | 7장 7.1.3 |
| `7-1-predict2-diagram.png` | https://raw.githubusercontent.com/nvidia-cosmos/cosmos-predict2/main/assets/cosmos-predict-diagram.png | https://github.com/nvidia-cosmos/cosmos-predict2 | © NVIDIA, 코드 Apache-2.0 | 7장 7.1.3 |
| `7-2-cosmos-curator-pipelines.png` | https://raw.githubusercontent.com/NVIDIA/cosmos-curator/main/docs/assets/cosmos-curator-pipelines.png | https://github.com/NVIDIA/cosmos-curator | © NVIDIA | 7장 7.2.1 |
| `7-2-drive-dreams-teaser.png` | https://media.githubusercontent.com/media/nv-tlabs/Cosmos-Drive-Dreams/main/assets/teaser.png | https://github.com/nv-tlabs/Cosmos-Drive-Dreams | © NVIDIA, Apache-2.0 | 7장 7.2.4 |
| `7-3-transfer25-world-scenario-rendering.png` | https://media.githubusercontent.com/media/nvidia-cosmos/cosmos-transfer2.5/main/assets/docs/rendering_diagram.png | https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/world_scenario_video_generation.md | © NVIDIA, 코드 Apache-2.0 | 7장 7.3.3 |
| `7-3-omnidreams-hdmap-overlay.png` | https://raw.githubusercontent.com/NVlabs/alpasim/main/docs/assets/images/frame-with-hdmap-render-overlaid.png | https://github.com/NVlabs/alpasim/blob/main/docs/VIDEO_MODEL.md | © NVIDIA, Apache-2.0 | 7장 7.3.3 |
| `7-3-carla-nurec-api.svg` | https://raw.githubusercontent.com/carla-simulator/carla/ue4-dev/Docs/img/carla-nurec-api.svg | https://github.com/carla-simulator/carla/blob/ue4-dev/Docs/nvidia_nurec.md | © CARLA, MIT | 7장 7.3.1 |
| `7-4-cosmos-rl-infra.svg` | https://raw.githubusercontent.com/nvidia-cosmos/cosmos-rl/main/assets/rl_infra.svg | https://github.com/nvidia-cosmos/cosmos-rl | © NVIDIA, Apache-2.0 | 7장 7.4.3 |

## 내려받지 못한 그림 (링크만, 후속 세션 과제)

| 그림 | 페이지 | 이유 |
|---|---|---|
| Alpamayo-R1 논문 Fig.1 (아키텍처) | https://arxiv.org/html/2511.00088v2 | arxiv.org 차단 |
| Cosmos WFM 플랫폼 개요 Fig.1 | https://arxiv.org/html/2501.03575v2 | arxiv.org 차단 |
| Cosmos-Transfer1 / Reason1 논문 그림 | https://arxiv.org/abs/2503.14492 · https://arxiv.org/abs/2503.15558 | arxiv.org 차단 |
| DRIVE AV 듀얼 스택 다이어그램 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-av/ | nvidia.com 차단 |
| Hyperion 10 센서 배치·2×Thor 보드 | https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-hyperion/ | nvidia.com 차단 |
| Halos 계층 다이어그램 | https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/ | nvidia.com 차단 |
| NVIDIA "three computers" 그래픽 | https://blogs.nvidia.com/blog/three-computer-cosmos-ces/ | blogs.nvidia.com 차단 |
| Omniverse Blueprint for AV simulation 다이어그램 | https://nvidianews.nvidia.com/news/nvidia-expands-omniverse-with-generative-physical-ai | nvidianews 차단 |
| DRIVE AGX Thor 개발 키트 보드 사진 | https://developer.nvidia.com/drive/agx | developer.nvidia.com 차단 |
| 3DGRUT 플레이그라운드 GIF | https://github.com/nv-tlabs/3dgrut | Git LFS 포인터만 반환 |
