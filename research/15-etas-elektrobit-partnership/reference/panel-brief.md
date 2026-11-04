# ETAS × Elektrobit 패널 토론 — 요약

- 자료: 양사 공동 웨비나 패널 토론(2026-10-06, Mobex 주최 "Elektrobit and ETAS: accelerating the future of ADAS through strategic partnership"), 영문 자동 전사본
- 정리일: 2026-11-04
- 원문: [영문 전사](panel-transcript-raw-en.md) · [줄 단위 해석](panel-transcript-line-by-line-ko.md)
- 참석: Björn Reistel(ETAS, 오픈소스 커뮤니티) · Subhash Sindhya(ETAS, 컴퓨트 제품 총괄) · Isaac Trebs(EB, Linux for Safety Applications PM) · Moritz Neukirchner(EB, HPC·SDV 사업) · 사회 Anton(EB)

## 1. 핵심

- 주제: 모회사(Bosch / Continental→AUMOVIO)가 경쟁 관계인 두 소프트웨어 회사의 협력 배경
- 공동 제품: EB corbos Linux for Safety Applications(안전 인증 리눅스) + ETAS EDMS(ADAS 미들웨어)의 사전 통합
- 다음 단계: 첫 양산(SOP) 적용, 2026-10-20 ETAS Connections(슈투트가르트) 공동 데모

## 2. 업계 진단

- SDV 프로그램 현실화, 협업 비중 증가
- 존(zonal) 아키텍처 전환 지속
- 타 산업 검증 기술(리눅스 등)의 자동차 안전 영역 유입
- HPC 도입 7~8년 경과, 컴퓨트 SW 시장은 여전히 파편화 → 공동 제안 여지
- 고객은 기초 작업을 끝낸 파트너를 선호

## 3. 협력 근거

### 3.1 역할 분담
- EB: OS 층. 기능 안전 확보한 리눅스, 도메인 기능 없음
- ETAS: 미들웨어 층. ADAS용 결정적 데이터 처리·고처리량, Bosch ADAS 도메인 지식 기반
- 기본 SW·HPC 미들웨어 등 경쟁 분야는 협력 대상에서 제외

### 3.2 오픈소스 전략 (Eclipse S-CORE)
- ETAS가 S-CORE를 시작한 계기: 고객과의 "공동 비용·공동 투자" 논의에서 반복 거론된 레이어
- 구조: 범용 부분 = S-CORE 기반 General Purpose 프로파일(오픈소스), ADAS 특화 = EDMS(상용)
- 원칙: 공동 기반만 공개, 차별화 요소는 각사 상용. "오픈소스 그린워싱 아님"
- EB가 자발적으로 S-CORE에 참여해 리눅스를 레퍼런스 OS로 추진 → 협력 가능성의 결정적 신호

### 3.3 고객 문제 해결
- 기존 패턴: 리눅스로 개발 → 양산 직전 기능 안전 때문에 독점 OS로 전환 → 리스크·일정 지연
- 해법: 처음부터 안전 인증 리눅스 사용 + 미들웨어 사전 통합. 호환성 검증은 공급사 책임
- 방향: 맞춤형 ADAS 솔루션 → 표준화·반복 적용·하드웨어 비종속

### 3.4 지배구조
- 모회사는 경쟁하지만 소프트웨어 자회사는 그룹 외부 시장 공략 가능. ETAS는 Bosch 경쟁사에도 공급, EB도 동일

### 3.5 시장·문화
- OEM 예산 압박 심화, "SOP 이후에도 존속할 파트너" 요구 → 보완 자산 결합으로 대응
- 양사 개방형 협업 문화 일치, 비독점 협력

## 4. 고객 가치

- 통합 부담 제거: 두 공급사가 상호 동작 보증
- 개발 연속성: 리눅스 도구(Docker·컴파일러·gdb) 그대로 프로토타입→SOP
- 종속 회피: EDMS는 POSIX 기반으로 OS 교체 가능, EB 안전 솔루션은 모든 리눅스에 적용. 사이버보안 유지보수 조건으로 리눅스 공급자 선택 가능
- 안전 실증: 리눅스 기능 안전 실증 사례 보유
- 스택 완성: OS 단독이 아닌 미들웨어 포함 전체 스택 제공

## 5. 로드맵

- 1단계: EDMS + ADAS/AD 사용 사례
- 2단계: S-CORE 기반 플랫폼과 통합 심화, General Purpose 프로파일로 게이트웨이·바디 컴퓨터 등 타 HPC 도메인 확장
- EB 측: 칩 지원 확대, 콕핏 안전·경고등 렌더링 등 타 기능 도메인, 인접 산업
- 시장 반응: JSAE 발표 후 "존재해서는 안 될 파트너십" 보도, 고객 문의 증가
- 목표: 첫 SOP 확보

## 6. 5년 전망 (Subhash Sindhya)

1. 중앙집중형 아키텍처 도입 지연 — 비용 압박, 기존 E/E 아키텍처 활용한 점진 전환. 빅뱅·그린필드는 예외
2. ADAS 대중화 — L2·L2++ 대중 시장 확산
3. 지역화 — 기술 선도 지역과 채택 선도 지역 분리

## 7. 결론

- 합의 구조: 경쟁 영역 유지 + 비경쟁 층(OS/미들웨어) 결합 + 비차별 기반(S-CORE) 오픈소스 공유
- 성립 조건: 고객 통합 리스크에 대한 공통 진단, 자회사의 외부 시장 자유, 개방형 협업 문화

## 용어

| 용어 | 뜻 |
|---|---|
| SDV | 소프트웨어 정의 차량 |
| HPC | 차량용 고성능 컴퓨터 |
| ADAS / AD | 첨단 운전자 보조 시스템 / 자율주행 |
| SOP | 양산 개시 |
| ISO 26262 / ASIL | 자동차 기능 안전 표준 / 위험 등급(A<B<C<D) |
| POSIX | 유닉스 계열 OS 표준 인터페이스 |
| Eclipse S-CORE | Eclipse 재단 오픈소스 차량 미들웨어 코어 |
| EDMS | ETAS Deterministic Middleware Solution |
| 결정적(deterministic) | 같은 입력 → 같은 결과. 재현·검증에 필수 |
