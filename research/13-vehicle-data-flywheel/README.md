# 자율주행 데이터 플라이휠 — 실도로 데이터가 모델을 키우는 순환 구조

> **작성일**: 2026-09-22 · **상태**: 초판
> **목적**: 자율주행에서 "데이터 플라이휠"이 왜 필요한지, 차량·클라우드·검증 환경을 잇는 전체 구조가 무엇인지, 실도로 데이터가 어떤 단계를 거쳐 모델 개선으로 이어지는지, 기업들은 어떻게 하고 있는지, 병목과 사업 경쟁력·진화 방향은 무엇인지를 사실 근거로 정리한다.

## 문서 목록

| 문서 | 내용 | 상태 |
|---|---|---|
| [vehicle-data-flywheel.md](vehicle-data-flywheel.md) | 보고서 원본, 줄글 판 (5장, 모든 사실 문장에 출처·등급) | 초판 |
| [vehicle-data-flywheel.html](vehicle-data-flywheel.html) | 웹 버전 (자체 완결 페이지, 다크 모드·목차) | 초판 |
| [vehicle-data-flywheel-report.md](vehicle-data-flywheel-report.md) | 개조식 보고서 판 (표지·요약·장별 개요/핵심 결론/시사점, 항목·표 중심. 사실·수치·출처·그림은 줄글 판과 동일) | 초판 |
| [vehicle-data-flywheel-report.html](vehicle-data-flywheel-report.html) | 개조식 보고서 웹 버전 | 초판 |
| [images/](images/) | 자체 작성 도식(SVG 10장) + 공개 GitHub 저장소에서 내려받은 원본 그림 13장(NVIDIA·서베이·Waymo Open Dataset 공식 그림, Tesla·Waymo·Momenta·Baidu 발표 슬라이드 화면) | — |
| [reference/references.md](reference/references.md) · [reference/images.md](reference/images.md) | 출처 목록 · 이미지 출처 | — |

## 작성 규약

- **사실근거 원칙**: 모든 사실 문장에 출처와 등급을 붙인다. 🔍 1차 출처 원문 직접 확인(GitHub README·공식 문서·법령 원문) · ✅ 복수 출처 교차 확인 · 📰 웹 검색 요약·보도만 확인(원문 미열람) · ⚠️ 미확인·추정. 기업의 마케팅 수치는 "공개 주장"이라고 적는다.
- **이 저장소의 다른 조사 문서는 인용하지 않는다.** 같은 사실이 필요하면 원 출처를 다시 찾아 붙였다.
- **쉬운 말 원칙**: 전문 용어는 처음 나올 때 한 줄로 풀이하고, 한 문장에 한 가지 생각만 담는다. 용어 풀이는 보고서 끝에 모아 두었다.
- **그림**: 설명용 도식은 자체 SVG로 그렸다(실선 = 출처로 확인, 점선 = 추정). 외부 그림은 접근 가능한 공개 저장소(Apache-2.0 등)에서만 내려받고 출처·라이선스를 [reference/images.md](reference/images.md)에 적었다. 기업 발표 슬라이드 화면은 학술 서베이 저장소(Apache-2.0)에 수록된 것을 옮겼고 원 저작권은 각 회사에 있다. 원본 그림은 내용을 바꾸지 않고 크기만 줄였다.
- **조사 환경 제약(2026-09-22)**: 세션 네트워크 정책상 arxiv.org·huggingface.co·nvidia.com 계열·tesla.com·waymo.com·wayve.ai·mobileye.com 원문에 직접 접근할 수 없었다. GitHub 저장소(clone·raw)·일부 언론·법령 사이트·웹 검색 요약만 가능했으므로, 검색 요약에만 근거한 사실은 📰로 표시했다.
