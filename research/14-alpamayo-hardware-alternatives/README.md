# Alpamayo를 돌릴 DRIVE Thor 대안 하드웨어

> **작성일**: 2026-09-29 · **상태**: 초판
> **목적**: NVIDIA Alpamayo(1 / 1.5 / 2 Super)를 DRIVE AGX Thor 밖에서 실행할 하드웨어를 고르기 위해, 모델이 요구하는 사양을 기능별(양자화·궤적 샘플 수·VQA·내비 CFG)로 정리하고, Thor에서 되는 범위를 기준선으로 세운 뒤, 후보 보드·GPU(Jetson AGX Thor·T4000·AGX Orin, DRIVE AGX Orin, DGX Spark, RTX 30/40/50, RTX PRO, H100 등)마다 "되는 것·안 되는 것"과 2026-09 가격을 함께 적는다.

## 문서 목록

| 문서 | 내용 |
|---|---|
| [alpamayo-hardware-brief.md](alpamayo-hardware-brief.md) | **요약 보고**. 공식 요구 사양(모델별·궤적 샘플 수별·학습/폐루프, 양자화·최적화 제외), 비교 항목별 요구치, 후보 하드웨어 18종 지원 범위 표(DRIVE Thor 기준, 분류·원화 가격 포함), 용어 주석. 본문에 출처 미표기, 끝에 근거 자료 상세 목록 |
| [alpamayo-hardware-alternatives.md](alpamayo-hardware-alternatives.md) | 보고서. 결론, 1부 요구 사양(기능별 메모리·세대·양자화 경로), 2부 Thor 기준선과 동일 런타임 3플랫폼 대리 지표, 3부 후보별 실행 범위 매트릭스·보드별 상세·가격, 4부 목표별 최저가 후보와 시나리오, 5부 제외 후보, 부록 미확인 항목 |
| [alpamayo-hardware-alternatives.html](alpamayo-hardware-alternatives.html) | 웹 버전 (자체 완결 페이지, 목차·다크 모드. 내용은 Markdown 원본과 동일) |
| [images/01-memory-ladder.svg](images/01-memory-ladder.svg) | 메모리 요구 사다리(11·18.3·24·31.6·40·60·72·96·138 GB) vs 후보 하드웨어 메모리 도식(자체 작성) |
| [reference/references.md](reference/references.md) | 출처 목록 (M 모델·런타임, J Jetson, D DRIVE, G 데스크톱·워크스테이션·DGX Spark, C 데이터센터·클라우드, P 가격) |

관련 문서: [Thor 배포편](../09-ad-sw-stack-deep-dive/thor-deployment/thor-deployment.md) · [Alpamayo SW/HW 요구사항](../03-nvidia-alpamayo/alpamayo_sw_hw_요구사항.md) · [FlashDrive 분석](../04-flashdrive/flashdrive_analysis.md) · [TIER IV × Alpamayo](../07-tier4-alpamayo-autoware/tier4_alpamayo_autoware_보고서.md)

## 작성 규약

- 모든 사실 문장에 출처 ID와 등급(💻 저장소 raw 파일 직접 · 🔍 1차 페이지 직접 · 📚 앞선 보고서의 직접 열람 기록 · 📰 검색 요약 · ✅ 교차 · ⚠️ 미확인)을 붙인다.
- 판단은 `분석` 블록에만 쓰고, 계산은 "계산"으로 표시한다.
- 가격은 조사일 USD 표시가이며 환율·VAT를 반영하지 않았다. 2026년 메모리 수급난으로 변동이 크므로 구매 시 재확인이 필요하다.

## 조사 환경 제약 (2026-09-29)

세션 네트워크 정책상 nvidia.com·developer.nvidia.com·forums.developer.nvidia.com·docs.nvidia.com·huggingface.co·arxiv.org·리셀러 사이트 원문에 접근할 수 없었다. GitHub raw 파일·이슈와 웹 검색 요약만 가능했고, 실행·실측은 하지 않았다.
