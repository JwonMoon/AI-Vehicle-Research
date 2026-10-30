# Autoware 재단 스택 지도 — Autoware 2.0 시대의 저장소 157개

> **작성일**: 2026-10-30 · **상태**: 초판
> **목적**: `autowarefoundation` GitHub 조직의 저장소 157개를 전수 조사해 10개 묶음(A~J)으로 분류하고, 로보택시·L4 트랙(Autoware 2.0 본체·Diffusion Planner·AutoE2E·LatentDrive·OnePlanner)과 ADAS·POV 트랙(Vision Pilot·AutoSteer/AutoSpeed/AutoDrive·AutoSeg 계열)으로 나눠 각 스택이 무엇인지, AWF 공식 로드맵(다년 로드맵·Architecture 2.0 4단계·POV 4단계·Open AD Kit 사다리) 위에서 어디에 있는지를 정리한다. 2026-10-29 공개된 Autoware 2.0.0의 실제 내용(Generator-Selector 상태, Hugging Face 모델 이관, Autoware Index, Reference Design)도 다룬다.

## 문서 목록

| 문서 | 내용 |
|---|---|
| [autoware-foundation-stack-map.md](autoware-foundation-stack-map.md) | 보고서(원본). §0 세 줄 요약, §1 한눈에 보는 지도, §2 2026년 변화·릴리스 타임라인, §3 "두 트랙" 가설 검증(다년 로드맵·E2E 4단계·WG), §4 157개 저장소 분류표, §5 핵심 스택 상세(Autoware 2.0·Index·AutoE2E·LatentDrive/OnePlanner·Vision Pilot·AutoSeg·Open AD Kit·Safety Island·미들웨어·ODD 프로젝트), §6 두 트랙 비교, §7 로드맵 매핑, §8 HPC 시사점, §9 미확인 항목, 부록 |
| [autoware-foundation-stack-map.html](autoware-foundation-stack-map.html) | 웹 버전(자체 완결 페이지, 목차·다크 모드. 내용은 Markdown 원본과 동일) |
| [images/](images/) | 그림 24장. `01-awf-stack-map.svg`만 자체 작성, 나머지는 Autoware 공식 문서·각 저장소의 원본 그림을 복사(캡션에 경로 표기) |
| [reference/references.md](reference/references.md) | 출처 목록(D 공식 문서 원본 · P POV 레퍼런스 디자인 문서 · R 저장소 README · G GitHub 1차 페이지 · W 검색 요약) |
| [reference/repo-inventory.md](reference/repo-inventory.md) | 저장소 157개 전수 목록(분류·설명·언어·별·포크·최근 갱신·상태) |

관련 문서: [12 Autoware E2E 전환](../12-autoware-e2e-architecture/autoware-e2e-architecture-transition.md) · [09 AD SW 스택 심층편](../09-ad-sw-stack-deep-dive/ad-sw-stack-deep-dive.md) · [07 TIER IV × Alpamayo](../07-tier4-alpamayo-autoware/tier4_alpamayo_autoware_보고서.md) · [15 ETAS × Elektrobit](../15-etas-elektrobit-partnership/etas-elektrobit-partnership.md)

## 작성 규약

- 모든 사실 문장에 출처 ID와 등급(💻 저장소 원본 · 🔍 1차 페이지 · 📚 앞선 보고서 · 📰 검색 요약 · ⚠️ 추정)을 붙인다. 판단은 "분석"으로 표시한다.
- Architecture 2.0 단계와 각 저장소의 대응(그림 1 하단, §3.2·§7 표)은 공식 정의에 README의 자기 설명을 대응시킨 자체 해석이며 AWF의 공식 라벨이 아니다.

## 조사 환경 제약 (2026-10-30)

세션 네트워크 정책으로 autoware.org · docs.autoware.org · medium.com · GitHub 조직 API에 접근할 수 없었다. 공식 문서는 `autoware-documentation` 저장소의 Markdown 원본을 clone해 읽었고(렌더링 사이트와 내용 동일), 저장소 목록은 조직 페이지를 직접 열람했다. 실행·실측은 하지 않았다.
