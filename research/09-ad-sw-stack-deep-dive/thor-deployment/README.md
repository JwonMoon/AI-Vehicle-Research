# Thor 위에서 Alpamayo·Autoware 돌리기

> **작성일**: 2026-09-15 · **상태**: 초판
> **목적**: Jetson AGX Thor와 DRIVE AGX Thor 중 무엇으로 시작할지 정하고, Alpamayo(1.5, 2 Super 증류본)와 Autoware를 Thor에서 실행하기 위한 사양·제약·절차·단계별 계획을 정리한다.

## 문서 목록

| 문서 | 내용 |
|---|---|
| [thor-deployment.md](thor-deployment.md) | 보고서. 결론, 보드 비교, Alpamayo on Thor, Autoware on Thor, 실행 계획 |
| [images/](images/) | 플랫폼·버전 호환 지도, 단계별 로드맵, Alpamayo 2 Super SW 컴포넌트 스택(코드 기반) |
| [reference/references.md](reference/references.md) | 출처 목록 (T 보드·플랫폼, L Alpamayo, W Autoware, K 소스 코드) |
| [reference/code-alpamayo2-components.md](reference/code-alpamayo2-components.md) | Alpamayo 2 Super 코드 기반 컴포넌트 인벤토리 (파일·줄 근거) |

배경 설명은 [자율주행 SW 스택 파헤치기 심층편](../README.md)을 참고한다.

## 작성 규약

- 모든 사실 문장에 출처 ID와 등급(💻 코드 직접 · 🔍 1차 직접 · 📄 서드파티 직접 · ✅ 교차 · 📰 검색 요약·제목 · ⚠️ 미확인)을 붙인다.
- 판단은 `분석` 블록에만 쓰고, 수치 계산은 "계산"으로 표시한다.
- NVIDIA 포럼의 커뮤니티 보고는 공식 검증과 구분해 적는다.

## 조사 방법과 제약

- 2026-09-15 웹 조사(WebSearch·WebFetch)로 수집했고, 같은 날 Autoware·Alpamayo 저장소를 고정 커밋으로 클론해 코드와 대조했다(기준 `../reference/code-pins.md`). 실행·실측은 하지 않았다.
- 문서에 인용한 명령어와 버전 문자열은 WebFetch 요약을 거쳤으므로, 실행 전에 원문 파일에서 다시 확인해야 한다.
- DRIVE 개발킷 가격, GPU carveout 공식 문서, Thor 위 Autoware 전체 스택 성능 수치는 공개 자료에서 찾지 못했다.
