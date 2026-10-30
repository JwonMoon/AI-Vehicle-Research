# Autoware 재단 스택 지도 — Autoware 2.0 시대의 저장소 157개와 두 트랙

> **작성일**: 2026-10-30 · **상태**: 2판(글머리 형식 재구성, 최근 소식·주행 모델 × 컴퓨트 장 추가, 미확인 내용 삭제)

## 문서 목록

| 문서 | 내용 |
|---|---|
| [autoware-foundation-stack-map.md](autoware-foundation-stack-map.md) | 보고서(원본). 최근 소식(Autoware 2.0.0), 0 한눈에 보기, 1 두 트랙 구조와 가설 점검, 2 로보택시·L4 트랙, 3 ADAS·POV 트랙(Vision Pilot), 4 주행 모델과 컴퓨트, 5 배포·안전 층, 6 공통 기반, 7 저장소 157개 분류, 8 로드맵 위의 위치, 9 HPC 시사점, 10 조사 방법과 한계 |
| [autoware-foundation-stack-map.html](autoware-foundation-stack-map.html) | 웹 버전(기본 디자인 — 1판과 같은 상단 바·왼쪽 고정 목차·다크 모드). `[n]` 인용이 출처 URL로 연결된다 |
| [autoware-foundation-stack-map-anthropic.html](autoware-foundation-stack-map-anthropic.html) | 웹 버전(보고서풍 디자인 — 아이보리 바탕·세리프 본문·고정 장 표시줄·그림 카드·저장소 157개 점 표지). 내용은 같다 |
| [images/](images/) | 그림 18장. 01·16·18은 자체 작성, 나머지는 Autoware 문서·저장소 원본 그림(캡션에 경로 표기) |
| [reference/references.md](reference/references.md) | 출처 75건(💻 저장소 원본 · 🔍 GitHub 1차 페이지) |
| [reference/repo-inventory.md](reference/repo-inventory.md) | 저장소 157개 전수 목록(분류·설명·별·포크·갱신일·상태) |
| [scripts/](scripts/) | `make_figures.py`(자체 도식 생성), `build_html.py` + `templates/`(HTML 변환, 테마 2종) |

## 다시 만들기

```bash
python3 -I scripts/make_figures.py images/
python3 -I scripts/build_html.py classic     # 기본 디자인
python3 -I scripts/build_html.py anthropic   # 보고서풍 디자인
```

## 관련 문서

- [12 Autoware E2E 전환](../12-autoware-e2e-architecture/autoware-e2e-architecture-transition.md) — 2026-06, Autoware 1.8.0 기준의 이전 조사. 이 보고서는 출처로 쓰지 않았다.

## 조사 환경 제약 (2026-10-30)

세션 네트워크 정책으로 autoware.org · docs.autoware.org · medium.com · 언론 사이트 · GitHub 조직 API에 접근할 수 없었다. 공식 문서는 `autoware-documentation` 저장소 원본으로 읽었고, 원문으로 확인하지 못한 내용은 싣지 않았다.
