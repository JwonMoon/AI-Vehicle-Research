# 2회차 — 차량용 HPC 플랫폼 설계: SoC, E/E 아키텍처, 기능안전

> **대상**: 차량용 HPC 아키텍처 설계 팀 | **형식**: 세미나 발표 정리본 (발표 대본 수준)
> **한 줄 요약**: 플랫폼 선택의 축은 ① precision 기준을 병기한 SoC 비교, ② zonal+중앙집중 E/E 전환이 만드는 I/O·전력·열 요구, ③ safety island + FFI + fail-operational이라는 기능안전 제약 — 세 가지가 함께 움직인다.

---

## 0. 발표 흐름 안내 (5분)

1회차에서 "무엇이 돌아가는가(워크로드)"를 봤다면, 이번에는 **"무엇 위에서, 어떤 제약으로 돌리는가(플랫폼)"**입니다.

1. 주요 AD SoC 비교 — precision 함정과 함께
2. E/E 아키텍처 진화 — 분산형 → 도메인 → 존/중앙집중형
3. SW 플랫폼/미들웨어 — DriveOS, AUTOSAR, ROS 2, 하이퍼바이저와 mixed-criticality
4. 기능안전·규제 — ISO 26262/SOTIF/ISO 8800, UNECE R157/R171/R155/R156
5. 종합: 우리 팀 HPC 설계 체크리스트

---

## 1. 주요 AD SoC 비교 (25분)

> ⚠️ **TOPS 해석 주의**: 벤더별 TOPS는 precision(INT8 dense/sparse, FP8, FP4)과 sparsity 가정이 제각각이라 직접 비교 불가. NVIDIA Thor의 "2,000 TFLOPS"는 **FP4 기준**이며 INT8 기준 약 1,000 TOPS. 비교표에는 반드시 precision 컬럼을 넣을 것.

### 1.1 NVIDIA — 성능·생태계 진영

**DRIVE AGX Orin (현행 양산 baseline, 2022~)**
- 254 TOPS (INT8 sparse), 12× Cortex-A78AE, LPDDR5 ~205 GB/s, 시스템 60–70W
- Safety Island: 4× Cortex-R52 lock-step — 칩 random HW는 ASIL-B, 시스템 ASIL-D는 decomposition으로
- DriveOS 6.0이 TÜV로부터 **ISO 26262 ASIL-D 인증** (세계 최초 ASIL-D OS 주장)
- 채택: NIO, XPeng, Li Auto, Polestar, Volvo EX90/ES90(dual Orin)
- 출처: [Orin 개발자 문서](https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-orin-platform-for-developers.pdf), [DriveOS ASIL-D](https://blogs.nvidia.com/blog/nvidia-drive-os-tuv-sud-safety-certification/)

**DRIVE AGX Thor (2025 양산, 차세대 플래그십)**
- **1,000 TOPS INT8 sparse = 2,000 TFLOPS FP4** (동일 실리콘, precision 차이). 파생형 Thor-U는 700 TOPS급
- Blackwell GPU + **FP4/FP8 Transformer Engine** → 차량 내 LLM/VLA 실행 겨냥
- **14× Arm Neoverse V3AE** (서버급 automotive 코어 — CPU 성능 대폭 상승)
- LPDDR5X 최대 128GB, **~273 GB/s** (DevKit 기준) — 1,000 TOPS 대비 낮은 B/F 비율로 병목 논쟁 존재
- **NVLink-C2C**로 dual-Thor 결합 (~2,000 TOPS INT8). MIG로 도메인 격리
- QNX OS for Safety 8 통합, Thor-X SoC ASIL-D conformant 평가
- 디자인윈: Zeekr 9X(dual Thor-U, 1,400 TOPS), BYD, GAC Hyper, Li Auto i8(VLA), Xiaomi, Volvo(차세대), Lucid. 첫 양산차 Lynk & Co 900(2025 Q2)
- 출처: [Thor 개발자 문서](https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf), [QNX×Thor](https://www.automotiveworld.com/news-releases/qnx-os-for-safety-integrated-in-nvidia-drive-agx-thor-thor-development-kit-at-general-availability/), [Zeekr](https://autotechinsight.spglobal.com/news/5267919/nvidia-to-supply-zeekr-with-its-flagship-thor-automated-driving-chip-in-2025-)

### 1.2 Qualcomm — 융합·비용 진영

- **Ride Flex (SA8775P)**: cockpit+ADAS **단일 SoC 융합**(업계 최초 주장). SEooC로 ASIL-D 타깃, safety island + 하이퍼바이저. 2-SoC→1-SoC 통합으로 **BOM 25–50% 절감** 소구. TOPS는 공식 미공개(보도치 편차 큼 — 인용 주의). 양산 중
- **Ride Elite (SA8797P)**: 커스텀 Oryon CPU(CPU 3배·AI 12배 주장), 최대 **640 TOPS**(precision 미공개). Leapmotor D19에 dual SA8797로 2026 Q1 첫 양산
- **BMW 전략 협업**: 공동 개발 "Snapdragon Ride Pilot" — **Neue Klasse iX3에 2025년 11월 첫 양산** 적용, 10년 장기 칩 공급 보도
- 소구점: 스케일러블 포트폴리오 + 스마트폰 검증 전성비 + cockpit 융합 BOM 절감
- 출처: [Ride Flex](https://www.qualcomm.com/news/releases/2023/01/qualcomm-unveils-snapdragon-ride-flex---the-automotive-industry-), [BMW Ride Pilot](https://autotechinsight.spglobal.com/news/5283871/iaa-mobility-2025-bmw-and-qualcomm-unveil-snapdragon-ride-pilot-for-automated-driving), [Elite](https://futurumgroup.com/insights/qualcomm-launches-new-elite-snapdragon-automotive-platforms/)

### 1.3 Mobileye — 효율(efficiency-first) 진영

- **EyeQ6H**: **34 TOPS (INT8)**, ~40W(≈0.85 TOPS/W), 2025 초 양산. 1칩 Surround ADAS, 2칩 SuperVision(hands-off), 확장 시 Chauffeur
- **EyeQ Ultra**: 176 TOPS, 5nm, 12× RISC-V + 자체 가속기 4종(XNN·PMA·VMP·MPC) — L4 단일칩 지향(2022 발표). 이후 실제 전개는 EyeQ6H 멀티칩 중심
- 디자인윈: VW 그룹 Surround ADAS(Tier-1 Valeo), Top-10 US OEM, Porsche/Audi C-sample
- 포인트: **TOPS 경쟁 자체를 거부** — 알고리즘-HW 공동설계로 "34 TOPS로 11카메라 처리". 리스크: 폐쇄적 블랙박스 모델이 SDV 시대 OEM 통제권 요구와 충돌
- 출처: [EyeQ6](https://ir.mobileye.com/news-releases/news-release-details/meet-eyeqr6-our-most-advanced-driver-assistance-chips-yet), [VW 수주](https://www.automotiveworld.com/news/mobileye-wins-second-top-10-automaker-for-surround-adas/)

### 1.4 기타 주요 플레이어

| 벤더/칩 | 핵심 | 상태 |
|---|---|---|
| **TI TDA4VH-Q1** | 32 TOPS INT8, 8× A72, ASIL-D MCU island 통합 — 저전력·저BOM, L2 볼륨존 | 양산 중 |
| **Renesas R-Car V4H** | 34 TOPS, 3× lock-step R52 내장(외장 MCU 불요) | 2024 양산 |
| **Renesas R-Car X5H** | 업계 최초 **3nm** 멀티도메인. 400 TOPS + **AI chiplet으로 4배+ 확장**, 32× A720AE. ADAS+IVI+GW 통합, 5nm 대비 전력 -35% | 2025 샘플, 2027 H2 양산 |
| **Ambarella CV3-AD685** | CVflow 자체 엔진, 12× A78AE, ASIL-B 칩 + ASIL-D island. "업계 최고 perf/W" 소구 | Continental 경유 2027 목표 |
| **Horizon Journey 6P** | 560 TOPS + 410K DMIPS, BPU Nash(Transformer 네이티브). 중국 로컬 최대 강자 — J6 패밀리 20+ OEM/100+ 차종 | 2025 양산 (Chery) |
| **Black Sesame A2000X** | "1,000 TOPS equivalent"(환산 기준 불명확 — 주의) | 2026 목표 |
| **Tesla AI5** | AI4 대비 compute 8배·메모리 대역폭 5배·효율 3배/W (TOPS 미공개). TSMC AZ + Samsung TX 이원 생산. 초기 물량은 Optimus/DC 우선 | 2027 중반 양산 목표 |
| **NIO NX9031** | 중국 OEM 최초 5nm 자체 칩, ET9 dual 구성 | 2025 양산 |
| **XPeng Turing** | 700–750 TOPS(자체 발표), E2E 대형모델 특화, 자체 컴파일러 | 2025 Q2~ 자사 적용 |

출처: [TI](https://www.ti.com/product/TDA4VH-Q1), [Renesas X5H](https://www.renesas.com/en/about/newsroom/renesas-fast-tracks-sdv-innovation-r-car-gen-5-soc-based-end-end-multi-domain-solution-platform), [Ambarella](https://www.ambarella.com/news/ambarella-expands-cv3-family-of-automotive-ai-domain-controllers-with-new-cv3-ad685/), [Horizon](https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6), [Tesla AI5](https://www.notateslaapp.com/news/3115/musk-calls-teslas-ai5-chip-a-monster-reveals-specs-for-next-gen-fsd-hardware), [NIO](https://www.autocango.com/news-detail/nio-nx9031-chip-5nm-automotive-chips-china-localization), [XPeng](https://cnevpost.com/2025/04/15/xpeng-to-start-using-turing-chip-q2-report/)

### 1.5 종합 비교표 (세미나 배포용)

| 플랫폼 | AI 성능 (precision) | 전력 | 메모리 | CPU | Safety | 양산 |
|---|---|---|---|---|---|---|
| NVIDIA Thor | 1,000 TOPS INT8 / 2,000 TFLOPS FP4 | DevKit 최대 350W(킷 기준) | LPDDR5X 273 GB/s | 14× Neoverse V3AE | island + Thor-X ASIL-D 평가 | 2025 |
| NVIDIA Orin | 254 TOPS INT8 sparse | 60–70W | LPDDR5 205 GB/s | 12× A78AE | R52 island, 칩 B/시스템 D | 2022 |
| Qualcomm SA8797P | ~640 TOPS (기준 미공개) | 미공개 | 미공개 | Oryon | ASIL 지원 | 2026 Q1 |
| Qualcomm SA8775P | 미공개 (보도치 편차) | ~75W 보도 | LPDDR5 | Kryo | SEooC ASIL-D 타깃 | 양산 중 |
| Mobileye EyeQ6H | 34 TOPS INT8 | ~40W | LPDDR5 | 8C/32T | ASIL-B(D) 전통 | 2025 |
| TI TDA4VH | 32 TOPS INT8 | ~20W급 | LPDDR4x | 8× A72 | ASIL-D MCU 통합 | 양산 중 |
| Renesas X5H | 400 TOPS (+chiplet 4×) | 5nm 대비 -35% | 미공개 | 32× A720AE + 6× R52 | lock-step R52 | 2027 H2 |
| Horizon J6P | 560 TOPS (기준 미공개) | 미공개 | 미공개 | 410K DMIPS | — | 2025 |
| Tesla AI5 | AI4×8 (compute) | 효율 3×/W | 대역폭 5× | 자체 | 자체 | 2027 |

### 1.6 구조적 트렌드 7가지

1. **Precision 인플레이션**: FP4 마케팅 수치 확산 → 비교표에 precision 컬럼 필수
2. **ADAS+Cockpit 융합 중앙집중형**: Ride Flex, Renesas X5H, Thor — 전 벤더 공통 로드맵
3. **멀티 SoC 스케일링 표준화**: dual Thor-U/NX9031/SA8797/Orin — 플래그십은 2칩 이중화+확장. NVLink-C2C vs PCIe/이더넷
4. **Chiplet 전환**: Renesas X5H가 AI chiplet 첫 상용 사례. imec Automotive Chiplet Program(Arm·BMW·Bosch 등), UCIe + automotive qualification이 2026+ 과제
5. **메모리가 새 병목**: 차세대 요구 300–500 GB/s급. automotive LPDDR5X 9,600 Mbps + DLEP(in-line ECC 페널티 없이 대역폭 15–25% 회복)
6. **Safety/SW 스택의 상품화**: ASIL-D 인증 OS(DriveOS, QNX 8), R52 lock-step island가 공통 패턴
7. **수직통합 vs 머천트 분화**: Tesla/NIO/XPeng 자체 칩, 중국 볼륨존은 Horizon/Black Sesame, 서구는 NVIDIA·Qualcomm·Mobileye 3파전

출처: [imec chiplet](https://www.imec-int.com/en/press/arm-ase-bmw-group-bosch-cadence-siemens-siliconauto-synopsys-tenstorrent-and-valeo-commit), [Micron LPDDR5X/DLEP](https://www.micron.com/about/blog/memory/dram/micron-and-synopsys-accelerate-automotive-and-ai-innovation-with-dlep)

---

## 2. E/E 아키텍처 진화 (15분)

### 2.1 분산형 → 도메인 → 존(Zonal) + 중앙집중

- **분산형**: 기능당 1 ECU, 프리미엄 차량 100–150개+ — 하네스 복잡도·SW 통합 비용 한계
- **도메인형**: 기능 도메인별 컨트롤러 통합. 현행 양산 주력
- **존형+중앙집중**: 물리 위치 기준 zonal controller(로컬 I/O·전력분배·프로토콜 변환) + 1~4개 HPC. 이더넷 백본이 신경망 역할

**정량 효과**:
| 사례 | 수치 |
|---|---|
| 업계 전망 | ECU 100+ → 2030년경 10개 미만, 하네스 30–40% 단축 |
| Rivian Gen2 | ECU 17→7 (zonal 3개), 배선 2.6km·20kg 감소, 자재비 20% 절감 |
| BMW Neue Klasse | 하네스 600m/30% 경량화, eFuse가 기계식 퓨즈 최대 150개 대체, 전력효율 +20% |
| Tesla Cybertruck | Etherloop(GbE 링)로 368 endpoints를 155개 배선에 — Model 3 대비 68% 감소. **48V 아키텍처** 문서 공개 |

출처: [MarketsandMarkets](https://www.marketsandmarkets.com/PressReleases/automotive-ee-architecture.asp), [Rivian](https://insideevs.com/news/761865/rivian-zonal-architecture-development/), [BMW Superbrains](https://www.press.bmwgroup.com/usa/article/detail/T0448737EN_US/four-superbrains-for-the-neue-klasse:-more-intelligent-more-efficient-more-powerful?language=en_US), [Tesla Etherloop](https://grokipedia.com/page/etherloop)

### 2.2 OEM별 현황 (2025–2026)

- **BMW Neue Klasse**: 4개 "Superbrain"(Infotainment/AD/주행역학/기본기능) — 이전 대비 **20배 연산**, 4-zone 하네스
- **Mercedes MB.OS**: 2025 신형 CLA부터 4도메인 chip-to-cloud 통합, ADAS에 **수랭식 NVIDIA 칩**
- **VW 그룹**: 자체 E3 2.0 지연 후 **Rivian JV(RV Tech)로 전환** — zonal+SDV 스택, 첫 양산 ID.EVERY1(2027), 그룹 3,000만 대 확산 목표. CARIAD는 조율 역할로 축소
- **현대차그룹 Pleos**: 인하우스 차량 OS + **HPVC(고성능 차량 컴퓨터) + zone controller**, 2026 Q2 Pleos Connect, 2030년 2,000만 대 목표
- **BYD XUANJI**: "One Brain" 중앙연산, cockpit·driving·propulsion 융합(2.0), 자체 4nm 칩 A3(700 TOPS), ADAS 전 라인업 표준화
- **NIO**: 자체 5nm NX9031 + SkyOS(1,600개 atomic API SOA) full-stack 내재화

출처: [BMW](https://www.bmwgroup.com/en/news/general/2025/superbrains.html), [Mercedes CLA](https://media.mbusa.com/releases/the-all-new-mercedes-benz-cla-gorgeous-effortless-intuitive-and-flexible), [VW-Rivian JV](https://www.volkswagen-group.com/en/press-releases/one-year-after-its-founding-joint-venture-between-volkswagen-group-and-rivian-shows-strong-progress-19980), [현대 Pleos](https://www.hyundainews.com/en-us/releases/4408), [BYD](https://thenextweb.com/news/byd-has-built-chinas-first-4nm-driving-chip-and-its-putting-lidar-on-a-10000-car)

### 2.3 차량 내 네트워크 — HPC는 "스위치 + 컴퓨터"

- **이더넷 티어**: edge 10BASE-T1S(10Mbps, CAN/LIN 대체) → zone-HPC 1000BASE-T1(1Gbps) → 백본/센서 2.5–10Gbps Multi-Gig(802.3ch), 향후 25G
- **TSN**: 802.1AS(gPTP 시간동기), 802.1Qbv(Time-Aware Shaper — bounded latency), **802.1CB(FRER — 프레임 복제/제거 이중화)**, 차량 프로파일 P802.1DG — 센서퓨전의 결정론적 전달이 채택 동인
- **CAN XL**: 데이터 구간 최대 20Mbps, payload 2048B — 10BASE-T1S와 100BASE-T1 사이 갭 커버, ISO 11898 3판(2024) 편입
- **SoC 간**: PCIe Gen4 주류(+PCIe switch), NVIDIA는 NVLink-C2C(PCIe Gen5 대비 에너지효율 25배 주장)
- **센서 링크**: proprietary 진영 GMSL3(12Gbps/링크, PoC) · FPD-Link vs 표준화 진영 **MIPI A-PHY / ASA Motion Link** — 2023 MIPI-ASA 제휴로 CSI-2 over ASA-ML 수렴 중
- 규모감: 차량 총 센서 대역폭 **3–40 Gbps**, 플랫폼 처리 ~6 GB/s급

출처: [ADI 10BASE-T1S](https://www.analog.com/en/resources/analog-dialogue/articles/how-10base-t1s-ethernet-simplifies-zonal-architectures.html), [TSN 정리](https://encyclopedia.pub/entry/47220), [CAN XL](https://www.can-cia.org/can-knowledge/can-xl), [NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/), [MIPI-ASA](https://www.mipi.org/press-releases/mipi-asa-enter-liaison-agreement-to-enable-native-mipi-csi-2-implementation), [GMSL](https://www.analog.com/en/solutions/gigabit-mulitimedia-serial-link.html)

---

## 3. SW 플랫폼 / 미들웨어 (15분)

### 3.1 스택 구도

실무 구도: **HPC의 safety/vehicle-motion 파티션 = AUTOSAR Adaptive(또는 CP 게이트웨이), zonal MCU = AUTOSAR Classic, IVI = AAOS/Linux, AD 스택 = 전용 미들웨어** — 의 혼합.

- **NVIDIA DriveOS**: Type-1 hypervisor(Foundation) 위 파티션별 Guest OS(Linux/QNX), 파티션-코어 바인딩으로 간섭 최소화. Thor 세대는 QNX OS for Safety 8(ASIL-D, ISO 21434 사전인증) guest 지원
- **AUTOSAR Classic vs Adaptive**: CP = 정적 스케줄·하드 RT MCU용(존속). AP = POSIX 기반 SOA(ara::com service discovery), C++, OTA 전제 — HPC·central application server 타깃
- **ROS 2 양산 경로**: ① Apex.Grace(ROS 2 fork) — TÜV Nord **ISO 26262 ASIL-D SEooC 인증**, zero-copy 통신(iceoryx) ② Autoware Open AD Kit — SOAFEE 첫 blueprint(컨테이너 기반 cloud-native)
- **통신 미들웨어**: SOME/IP(AUTOSAR 표준, 기능 최소주의) vs DDS(풍부한 QoS+보안, ROS 2/AP 채택) vs **zenoh**(2024 Eclipse 정식 릴리스 — discovery 최속, WAN에서 DDS 우위, Woven by Toyota 채택)
- **컨테이너화(SOAFEE)**: OCI 컨테이너+오케스트레이션으로 클라우드-차량 environment parity. 단, **컨테이너는 배포 단위이지 safety isolation 단위가 아님** — 실시간성은 하부 OS/hypervisor 책임

출처: [DriveOS](https://developer.nvidia.com/drive/os), [AUTOSAR AP](https://www.autosar.org/standards/adaptive-platform), [Apex.AI 인증](https://www.apex.ai/apexgrace), [zenoh 비교 논문](https://arxiv.org/pdf/2505.02734), [SOAFEE](https://www.soafee.io/blog/2025/openadkit-blueprint/)

### 3.2 하이퍼바이저와 Mixed-Criticality

- **QNX Hypervisor for Safety 8** (Type-1 마이크로커널): 시장점유 27%+(2025). Android/Linux(QM)와 safety OS 병행, ASIL-D 인증
- **오픈소스 흐름**: AGL + **Xen**(dom0less, Safety Committee 출범) + Zephyr + VirtIO 스택이 공통 오픈 SDV 스택으로 수렴 중. ACRN/KVM/L4Re도 옵션
- **Qualcomm Ride Flex**: cockpit(QM)+ADAS(ASIL)를 단일 SoC co-host하는 최초 스케일러블 SoC — 규범적 근거는 ISO 26262의 **FFI(Freedom From Interference)**

**FFI 3축과 하드웨어 메커니즘** (HPC 설계 핵심):
| 축 | 위협 | 메커니즘 |
|---|---|---|
| Spatial (공간) | QM 워크로드의 메모리 오염 | MMU + stage-2 translation, **IOMMU/SMMU**(DMA 격리), ECC |
| Temporal (시간) | 실행시간 침해·스로틀링 | 코어 정적 할당, 실행 버짓, watchdog, **cache partitioning(MPAM류) + 메모리 대역폭 regulation** |
| Communication | 메시지 오염 | E2E protection(CRC/시퀀스), MACsec/CANsec, TSN ingress policing |

> 💡 **IOMMU는 접근 영역만 제한할 뿐 대역폭은 제어하지 못한다** — 공유 자원(DRAM 컨트롤러, LLC, NoC)의 QoS/regulator가 FFI 입증의 최대 난점이자, SoC 선정 시 반드시 확인할 하드웨어 기능. 정적 파티셔닝은 활용률 손실과의 트레이드오프.

출처: [QNX](https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety), [Xen OSS Japan 2025](https://xenproject.org/blog/oss-japan-2025-a-breakthrough-year-for-open-automotive-innovation/), [FFI 해설](https://piembsystech.com/freedom-from-interference-iso-26262/), [Mixed-criticality HPC SLR (ECSA 2025)](https://arxiv.org/html/2506.05822v1)

---

## 4. 기능안전·규제 (20분)

### 4.1 ISO 26262 — 컴퓨트 플랫폼 설계자의 핵심

- **ASIL A~D**: Severity × Exposure × Controllability. 등급이 높을수록 진단 커버리지·프로세스 엄격성 증가
- **ASIL Decomposition** (Part 9): ASIL-D 요구를 **충분히 독립적인** 두 요소로 분할 (예: D → B(D)+B(D)). 독립성 입증(공통원인 고장 배제, DFA)이 전제 — 고ASIL을 단일 요소로 구현하는 비용을 낮추는 실무 수단

**AD SoC의 ASIL-D 달성 패턴 = "doer + checker"**:
- 거대 AI SoC 전체를 ASIL-D로 개발하는 것은 비현실적 → **"큰 QM/ASIL-B 컴퓨트(doer) + 작은 ASIL-D safety island(checker)"** 구조가 업계 표준
- Safety island 구성: **DCLS(dual-core lockstep) Cortex-R52** + 전용 TCM + 독립 watchdog + fault aggregator + **독립 전원 레일** + ECC 보호 메모리
- NVIDIA Orin FSI: 4× DCLS R52(~10K ASIL-D MIPS), 독립 전압/전원 — SoC 나머지와 무관하게 안전 기능 실행. Orin 전체는 "systematic ASIL-D, random HW ASIL-B" → 시스템 클레임은 decomposition으로
- 외장 safety MCU 병용: Infineon AURIX TC4xx 등이 HPC 보드의 companion MCU 역할
- AI 가속기(NPU/GPU)는 lockstep이 비경제적 → **safety monitor + BIST + ECC** 조합 (ASIL-D급: stuck-at 커버리지 ≥90% LBIST/MBIST). 상용 IP 예: Synopsys ARC NPX6FS(ASIL-B/D Ready NPU)

출처: [Promwad Safety Island](https://promwad.com/news/safety-island-design-asil-decomposition-heterogeneous-compute-fabrics), [NVIDIA FSI 문서](https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/embedded-software-components/Functional_Safety_Island_FSI/Functional_Safety_Island.html), [Synopsys NPX6FS](https://www.synopsys.com/dw/ipdir.php?ds=arc-npx6fs), [SemiEngineering LBIST](https://semiengineering.com/automotive-functional-safety-using-lbist-and-other-detection-methods/)

### 4.2 SOTIF와 AI 안전 표준 스택

- **SOTIF (ISO 21448)**: 고장이 아니라 **"의도대로 동작해도 발생하는 위험"** — 성능 한계, 사양 부족, 예견 가능한 오사용. known/unknown-unsafe 시나리오 축소가 핵심. AI perception의 ODD 경계 검증, 개발/검증 데이터 통계적 독립성 요구
- **ISO/PAS 8800:2024** (2024-12 발행): 차량 내 AI의 안전 — AI 안전 라이프사이클 전 단계(데이터셋 품질, AI 안전요구, 학습/검증/배포·모니터링, 안전 논증). 26262+21448을 확장. 2025-08 Geely가 세계 최초 인증
- **ISO/TS 5083:2025**: L3/L4 ADS의 safety by design + V&V + 배포 후 활동 (ISO/TR 4804 대체)
- 실무 스택: **26262(고장) + 21448(성능한계) + 8800(AI) + 5083(ADS 전체) + 21434(사이버보안)**

> 💡 HPC 함의: AI 가속기의 random fault가 AI 출력 오류로 이어지는 경로가 표준 관리 대상 → **NPU/GPU에 대한 fault 모델링·진단 메커니즘·런타임 모니터링**이 안전 논증의 일부가 된다. SOTIF는 데이터 기록/리플레이 인터페이스, 런타임 ODD 모니터링용 여분 컴퓨트, shadow mode 수집 대역폭을 플랫폼에 요구.

출처: [ISO/PAS 8800](https://www.iso.org/standard/83303.html), [ISO/TS 5083](https://www.iso.org/standard/81920.html), [SGS-Geely](https://www.sgs.com/en-hk/news/2025/08/geely-auto-awarded-first-global-ai-safety-certification-for-road-vehicles), [SOTIF-AI 검증](https://www.patsnap.com/resources/blog/articles/iso-21448-sotif-validation-for-ai-perception-systems-2/)

### 4.3 UNECE 규제가 HPC에 거는 요구

**UN R157 (ALKS, L3)** — 130 km/h 개정(2023 발효):
- **Transition Demand 최소 10초 + MRM(최소 위험 기동)**: 단일 고장 후에도 이 구간 동안 인지·판단·제어 지속 → **fail-operational 컴퓨트/전원**이 아키텍처 요구로 직결
- 운전자 가용성 모니터링(최소 2개 기준, 30초 내 판정) → **DMS 컴퓨트가 규제 필수 요소**
- **DSSAD**(데이터 저장 시스템): 이벤트별 플래그·사유·타임스탬프(±1.0s), SW 버전(R157SWIN) 식별, 무결성 self-check, 조작 방지 → **변조 방지 비휘발성 로깅 경로** 필요

**UN R171 (DCAS, L2+)** — 2024-09 발효, 빠른 진화:
- 01 시리즈(2025-09): 시스템 주도 기동 확장. 02 시리즈(2027-01 발효 예정): 고속도로 **hands-off** 허용
- 운전자 관여 모니터링 + **시판 후 모니터링(연 1회+ 보고)** → L2+임에도 DMS 상시 실행, 텔레메트리 인프라 요구

**UN R155/R156 (사이버보안/SW 업데이트)**:
- CSMS/SUMS 인증 + TARA(ISO 21434) + RXSWIN 버전 추적 → **HSM/secure boot/서명 OTA(A/B 파티션)/IDS 상주 워크로드**가 플랫폼 기본 요건

**지역 현황 (2025–26)**: EU 2022/1426(무인 ADS 형식승인), 미국 NHTSA AV Framework(2025-04, Part 555 확대), 중국 최초 승용차 L3 허가(2025-12, Changan·Arcfox), 한국 L3 안전기준 + L4 성능인증제(2027 상용화 목표)

출처: [UNECE R157](https://unece.org/sustainable-development/press/un-regulation-extends-automated-driving-130-kmh-certain-conditions), [R171](https://unece.org/media/press/387961), [R171 진화 분석](https://roboticsandautomationnews.com/2025/11/11/a-year-after-the-uns-driver-assistance-regulation-came-into-force-the-real-race-begins/96455/), [R155](https://finitestate.io/blog/buckle-up-for-security-a-look-at-the-un-r155-regulation-for-connected-vehicles), [R156](https://www.itemis.com/en/glossary/unece-r156/), [중국 L3](https://cnevpost.com/2025/12/15/china-grants-1st-l3-autonomous-driving-permits-passenger-cars/), [한국 L4](https://www.newsis.com/view/NISX20251125_0003416684)

### 4.4 양산 리던던시 사례

- **Mercedes DRIVE PILOT (L3)**: 제동·조향·전원·센서·연산 알고리즘까지 **물리적+기능적 이중화**, 30개+ 센서 다양성 리던던시. 2024-12 KBA 승인 95km/h — 기존 차량 OTA 업그레이드(R156형 SW 관리의 실례)
- **Waymo (L4)**: 컴퓨트를 "두 개의 독립 엔진"으로 — 평시 병렬 수행, 한쪽 fault 시 **seamless 인수**. 조향·제동·전원·컴퓨트 전부 백업, 초당 수천 회 자기진단
- **NVIDIA**: 센서 다양성 + **연산 엔진 다양성**(CPU/GPU/DLA/PVA에 알고리즘 분산) diverse redundancy. Thor 세대는 NVLink 듀얼 SoC 리던던시 공식 지원
- fail-safe(정지) vs **fail-operational**(기능 유지): L3+는 최소 TD 10초+MRM 구간의 fail-operational. 전원도 상호 고장-독립 2계통이 전제

출처: [Mercedes redundancy](https://group.mercedes-benz.com/technology/autonomous-driving/driving/redundancy-drive-pilot.html), [Waymo](https://waymo.com/blog/2026/08/look-under-our-trunk/), [NVIDIA Safety Report](https://docs.nvidia.com/self-driving-cars/autonomous-driving-safety-report/index.html)

### 4.5 열·전력 — 물리적 제약

- L4급 연산은 **400–600W** 소비 → EV 주행거리 7–10% 잠식 가능. 중앙연산 열부하 1–4kW 보고, 국부 heat flux 10 W/cm² 초과
- **수랭(cold plate)·차량 냉각루프 연동이 프리미엄 HPC 기본값**화 — Mercedes CLA의 수랭식 NVIDIA 칩이 양산 사례
- 48V 저전압망 + smart eFuse 기반 전력 게이팅(BMW: 효율 +20%)이 HPC 전원트리와 직결
- TDP 버짓은 peak TOPS가 아니라 **통합 후 동시성 시나리오**(ADAS full-load + IVI 렌더링 + OTA)로 산정. 열 스로틀링이 safety 워크로드의 temporal FFI를 침해하지 않도록 **파티션별 전력/열 버짓 분리**

출처: [PatSnap thermal](https://eureka.patsnap.com/blog/research-report/centralized-vehicle-computing-thermal-limits-fail-operational-design-cost-tradeoffs/), [Electronics Cooling](https://www.electronics-cooling.com/2026/03/the-physics-of-cooling-in-confined-spaces-advanced-driver-assistance-systems-adas-automotive-electronics/)

---

## 5. 종합 — 우리 팀 HPC 설계 체크리스트 (10분 + 토론)

| # | 설계 결정 항목 | 체크 포인트 |
|---|---|---|
| 1 | **ASIL 배분** | 시스템 안전목표(D) → decomposition 채널 분할, 채널 간 독립성(전원·클록·배치) 입증. SoC random fault 등급(대개 B)과 시스템 클레임의 갭은 외부 safety MCU/듀얼 SoC로 보전 |
| 2 | **Safety island** | DCLS 코어, 독립 전원/클록, fault aggregator, SoC 전체에 대한 감시·safe-state 강제 권한 |
| 3 | **FFI** | 하이퍼바이저 정적 파티셔닝 + 메모리/캐시/NoC QoS + DFA 문서화. **SoC 선정 시 대역폭 regulator 유무 확인** — IOMMU만으로는 부족 |
| 4 | **Fail-operational 예산** | R157 "TD 10초 + MRM"이 최소 유지시간 스펙 — degraded perception/planning 경로와 전원 유지 설계. 컴퓨트·전원 2계통 |
| 5 | **메모리 사양** | 워크로드 믹스 기반: 용량(모델 상주) + 대역폭(LLM decode, 300–500 GB/s급) + ECC(DLEP류) — 1회차 결론과 연결 |
| 6 | **I/O 설계** | Multi-Gig TSN 이더넷 다포트 + 센서 SerDes(GMSL3/A-PHY/ASA-ML) + PCIe/NVLink(멀티 SoC) + CAN FD/XL 게이트웨이. 총 인입 3–40 Gbps |
| 7 | **규제성 데이터 경로** | DSSAD/EDR 변조 방지 로깅(±1s, SW 버전 식별), R171 시판 후 모니터링 텔레메트리 |
| 8 | **보안 기반** | HSM/secure boot/서명 OTA(A/B), RXSWIN 추적성, IDS 상주 워크로드 (R155/156) |
| 9 | **AI 안전 보증** | ISO/PAS 8800 라이프사이클 증거 + 가속기 진단 커버리지(BIST/ECC/monitor) + SOTIF용 데이터 기록/리플레이 |
| 10 | **열/전력** | 동시성 시나리오 기반 TDP, 수랭 연동 검토, 파티션별 전력/열 버짓 분리, 48V/eFuse 전원트리 |

### 토론 주제 제안

- 우리 설계에서 doer/checker 분리를 어디에 둘 것인가 — 온칩 island로 충분한가, 외장 MCU가 필요한가?
- 멀티 SoC 확장 시 인터커넥트 선택(PCIe vs NVLink-C2C vs 이더넷)과 FFI 입증 전략은?
- SoC 후보별로 "메모리 대역폭 QoS/regulator" 지원을 어떻게 검증할 것인가?
- 벤더 종속(컴파일러·OS·safety 패키지) vs 자체 스택의 경계선을 어디에 둘 것인가?

---

## 부록: 전체 출처

**SoC**: [NVIDIA Orin](https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-orin-platform-for-developers.pdf) · [Thor](https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf) · [DriveOS ASIL-D](https://blogs.nvidia.com/blog/nvidia-drive-os-tuv-sud-safety-certification/) · [QNX×Thor](https://www.automotiveworld.com/news-releases/qnx-os-for-safety-integrated-in-nvidia-drive-agx-thor-thor-development-kit-at-general-availability/) · [Qualcomm Ride Flex](https://www.qualcomm.com/news/releases/2023/01/qualcomm-unveils-snapdragon-ride-flex---the-automotive-industry-) · [BMW Ride Pilot](https://autotechinsight.spglobal.com/news/5283871/iaa-mobility-2025-bmw-and-qualcomm-unveil-snapdragon-ride-pilot-for-automated-driving) · [Mobileye EyeQ6](https://ir.mobileye.com/news-releases/news-release-details/meet-eyeqr6-our-most-advanced-driver-assistance-chips-yet) · [TI TDA4VH](https://www.ti.com/product/TDA4VH-Q1) · [Renesas X5H](https://www.renesas.com/en/about/newsroom/renesas-fast-tracks-sdv-innovation-r-car-gen-5-soc-based-end-end-multi-domain-solution-platform) · [Ambarella CV3](https://www.ambarella.com/news/ambarella-expands-cv3-family-of-automotive-ai-domain-controllers-with-new-cv3-ad685/) · [Horizon J6](https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6) · [Tesla AI5](https://www.notateslaapp.com/news/3115/musk-calls-teslas-ai5-chip-a-monster-reveals-specs-for-next-gen-fsd-hardware) · [NIO NX9031](https://www.autocango.com/news-detail/nio-nx9031-chip-5nm-automotive-chips-china-localization) · [XPeng Turing](https://cnevpost.com/2025/04/15/xpeng-to-start-using-turing-chip-q2-report/) · [imec chiplet](https://www.imec-int.com/en/press/arm-ase-bmw-group-bosch-cadence-siemens-siliconauto-synopsys-tenstorrent-and-valeo-commit) · [Micron DLEP](https://www.micron.com/about/blog/memory/dram/micron-and-synopsys-accelerate-automotive-and-ai-innovation-with-dlep)

**E/E·네트워크**: [MarketsandMarkets](https://www.marketsandmarkets.com/PressReleases/automotive-ee-architecture.asp) · [Rivian zonal](https://insideevs.com/news/761865/rivian-zonal-architecture-development/) · [BMW Superbrains](https://www.press.bmwgroup.com/usa/article/detail/T0448737EN_US/four-superbrains-for-the-neue-klasse:-more-intelligent-more-efficient-more-powerful?language=en_US) · [Mercedes CLA](https://media.mbusa.com/releases/the-all-new-mercedes-benz-cla-gorgeous-effortless-intuitive-and-flexible) · [VW-Rivian JV](https://www.volkswagen-group.com/en/press-releases/one-year-after-its-founding-joint-venture-between-volkswagen-group-and-rivian-shows-strong-progress-19980) · [현대 Pleos](https://www.hyundainews.com/en-us/releases/4408) · [Tesla Etherloop](https://grokipedia.com/page/etherloop) · [ADI 10BASE-T1S](https://www.analog.com/en/resources/analog-dialogue/articles/how-10base-t1s-ethernet-simplifies-zonal-architectures.html) · [TSN](https://encyclopedia.pub/entry/47220) · [CAN XL](https://www.can-cia.org/can-knowledge/can-xl) · [NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/) · [MIPI-ASA](https://www.mipi.org/press-releases/mipi-asa-enter-liaison-agreement-to-enable-native-mipi-csi-2-implementation)

**SW·하이퍼바이저**: [DriveOS](https://developer.nvidia.com/drive/os) · [AUTOSAR AP](https://www.autosar.org/standards/adaptive-platform) · [Apex.Grace](https://www.apex.ai/apexgrace) · [미들웨어 비교](https://arxiv.org/pdf/2505.02734) · [SOAFEE](https://www.soafee.io/blog/2025/openadkit-blueprint/) · [QNX Hypervisor](https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety) · [Xen automotive](https://xenproject.org/blog/oss-japan-2025-a-breakthrough-year-for-open-automotive-innovation/) · [Mixed-criticality SLR](https://arxiv.org/html/2506.05822v1)

**기능안전·규제**: [Promwad Safety Island](https://promwad.com/news/safety-island-design-asil-decomposition-heterogeneous-compute-fabrics) · [NVIDIA FSI](https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/embedded-software-components/Functional_Safety_Island_FSI/Functional_Safety_Island.html) · [ISO/PAS 8800](https://www.iso.org/standard/83303.html) · [ISO/TS 5083](https://www.iso.org/standard/81920.html) · [SGS-Geely](https://www.sgs.com/en-hk/news/2025/08/geely-auto-awarded-first-global-ai-safety-certification-for-road-vehicles) · [SOTIF-AI](https://www.patsnap.com/resources/blog/articles/iso-21448-sotif-validation-for-ai-perception-systems-2/) · [UNECE R157](https://unece.org/sustainable-development/press/un-regulation-extends-automated-driving-130-kmh-certain-conditions) · [R171](https://unece.org/media/press/387961) · [R155](https://finitestate.io/blog/buckle-up-for-security-a-look-at-the-un-r155-regulation-for-connected-vehicles) · [R156](https://www.itemis.com/en/glossary/unece-r156/) · [중국 L3](https://cnevpost.com/2025/12/15/china-grants-1st-l3-autonomous-driving-permits-passenger-cars/) · [한국 L4](https://www.newsis.com/view/NISX20251125_0003416684) · [Mercedes redundancy](https://group.mercedes-benz.com/technology/autonomous-driving/driving/redundancy-drive-pilot.html) · [Waymo](https://waymo.com/blog/2026/08/look-under-our-trunk/) · [Synopsys NPX6FS](https://www.synopsys.com/dw/ipdir.php?ds=arc-npx6fs) · [열 설계](https://eureka.patsnap.com/blog/research-report/centralized-vehicle-computing-thermal-limits-fail-operational-design-cost-tradeoffs/)
