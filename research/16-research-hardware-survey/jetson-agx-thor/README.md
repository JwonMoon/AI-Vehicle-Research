# Jetson AGX Thor로 자율주행 연구하기

16번 주제의 후속편. Jetson AGX Thor 데브킷 구매를 전제로 ① 데브킷 사양 ② 차량 관련 연구 사례와 부자재 ③ 데브킷에 카메라 붙이는 방법(Holoscan Sensor Bridge 설명, 경로 도식, GMSL vs HSB 추세) ④ 참고: 차량 산업의 DRIVE AGX Thor를 보고서 형식으로 정리했다. 로봇·산업 장비 사례는 제외.

| 문서 | 내용 |
|---|---|
| [jetson-agx-thor-guide.md](jetson-agx-thor-guide.md) · [웹 버전](jetson-agx-thor-guide.html) | 본 보고서(글머리 형식). 웹 버전은 출처 ID 클릭 시 원문으로 연결 |
| [mail-report.md](mail-report.md) · [웹 버전](mail-report.html) | 보고용 메일 정리본(같은 구조, 그림 없음) |
| [reference/references.md](reference/references.md) | 출처 38건(ID 접두어 T) |
| `images/` | `hsb-*`: NVIDIA Holoscan Sensor Bridge 공식 문서(GitHub nvidia-holoscan/holoscan-sensor-bridge, Apache-2.0)에서 가져온 사진·도면. `path-01-camera-routes.svg`: 자체 작성 경로 도식 |

작성 규약: 저장소 기존 문서 미참고, 사실 문장마다 출처 ID와 등급(🔍 공식 / 📄 논문 / 📰 언론 / 💬 포럼 / 🏷️ 벤더 / ⚠️ 미확인), 가격은 조사일 공개 표시가.
