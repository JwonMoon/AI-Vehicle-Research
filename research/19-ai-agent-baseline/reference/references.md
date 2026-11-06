# 출처 목록 — 19. AI 에이전트 baseline 조사 (계획 단계)

> **조사일**: 2026-11-06 (P0 계획 단계)
> **성격**: 계획서(`../plan.md`)에서 조사 대상 **후보**로 거론한 벤치마크·프레임워크·프로토콜·오픈소스의 공식 진입점 URL 목록이다. 수치·순위·라이선스는 아직 수록하지 않으며, P1~P3 조사 단계에서 각 항목에 조회 날짜·등급·발췌 내용을 붙여 확장한다.
> **등급 범례**: 🔍 공식(프로젝트 공식 사이트·저장소·리더보드) · 📄 논문·기술 블로그 · 📰 언론·서드파티 · 💬 포럼. 이 단계의 항목은 모두 🔍 공식 진입점이다.
> **주의**: URL은 작성 시점의 공식 진입점으로 알고 있는 주소이며, 조사 단계에서 접속해 확인한다. 접속 불가·이전된 항목은 수정하거나 "확인 불가"로 표기한다.

## 수집 방법

계획서의 각 표에서 이름을 모아 블록별로 번호를 매겼다. 조사 단계에서 리더보드 조회·모델 카드 열람·공식 문서 확인 결과를 같은 번호 아래 추가한다.

## 출처 목록

### [A] 에이전트 벤치마크 (1부 2.1)

1. 🔍 BFCL — Berkeley Function-Calling Leaderboard — https://gorilla.cs.berkeley.edu/leaderboard.html
2. 🔍 τ-bench / τ²-bench — Sierra Research 저장소 — https://github.com/sierra-research/tau2-bench
3. 🔍 GAIA — 벤치마크·리더보드(Hugging Face) — https://huggingface.co/gaia-benchmark
4. 🔍 AgentBench — THUDM 저장소 — https://github.com/THUDM/AgentBench
5. 🔍 Humanity's Last Exam — 공식 사이트 — https://lastexam.ai/
6. 🔍 OSWorld — 공식 사이트 — https://os-world.github.io/
7. 🔍 WebArena — 공식 사이트 — https://webarena.dev/
8. 🔍 AndroidWorld — Google Research 저장소 — https://github.com/google-research/android_world
9. 🔍 BrowseComp — OpenAI 공개 저장소(simple-evals) — https://github.com/openai/simple-evals
10. 🔍 SWE-bench — 공식 사이트·리더보드 — https://www.swebench.com/
11. 🔍 Terminal-Bench — 공식 사이트 — https://www.tbench.ai/

### [B] 에이전트 프레임워크·프로토콜 (1부 2.2)

12. 🔍 Model Context Protocol(MCP) — 공식 사이트 — https://modelcontextprotocol.io/
13. 🔍 A2A(Agent2Agent) 프로토콜 — 공식 사이트 — https://a2a-protocol.org/
14. 🔍 LangGraph — 공식 문서 — https://langchain-ai.github.io/langgraph/
15. 🔍 OpenAI Agents SDK — 공식 문서 — https://openai.github.io/openai-agents-python/
16. 🔍 CrewAI — 공식 저장소 — https://github.com/crewAIInc/crewAI
17. 🔍 AutoGen / AG2 — 공식 저장소 — https://github.com/ag2ai/ag2
18. 🔍 smolagents — Hugging Face 저장소 — https://github.com/huggingface/smolagents
19. 🔍 Google Agent Development Kit(ADK) — 공식 문서 — https://google.github.io/adk-docs/
20. 🔍 Pydantic AI — 공식 문서 — https://ai.pydantic.dev/

### [C] 로컬 LLM 실행 스택 (1부 2.3 · 2부 3.2)

21. 🔍 Ollama — 공식 사이트 — https://ollama.com/
22. 🔍 llama.cpp — 공식 저장소 — https://github.com/ggml-org/llama.cpp
23. 🔍 vLLM — 공식 문서 — https://docs.vllm.ai/
24. 🔍 MLX — Apple 저장소 — https://github.com/ml-explore/mlx
25. 🔍 ONNX Runtime — 공식 사이트 — https://onnxruntime.ai/

### [D] 음성 블록 오픈소스 (2부 3.2)

**VAD·턴 검출**
26. 🔍 Silero VAD — 공식 저장소 — https://github.com/snakers4/silero-vad
27. 🔍 WebRTC VAD(py-webrtcvad) — 저장소 — https://github.com/wiseman/py-webrtcvad

**ASR**
28. 🔍 Whisper — OpenAI 저장소 — https://github.com/openai/whisper
29. 🔍 faster-whisper — 저장소 — https://github.com/SYSTRAN/faster-whisper
30. 🔍 whisper.cpp — 저장소 — https://github.com/ggml-org/whisper.cpp
31. 🔍 NVIDIA NeMo(Parakeet·Canary) — 저장소 — https://github.com/NVIDIA/NeMo
32. 🔍 Moonshine — Useful Sensors 저장소 — https://github.com/usefulsensors/moonshine
33. 🔍 Kyutai STT/TTS(delayed-streams-modeling) — 저장소 — https://github.com/kyutai-labs/delayed-streams-modeling
34. 🔍 Vosk — 공식 사이트 — https://alphacephei.com/vosk/

**TTS**
35. 🔍 Kokoro — 모델 카드(Hugging Face) — https://huggingface.co/hexgrad/Kokoro-82M
36. 🔍 Piper — 저장소 — https://github.com/rhasspy/piper
37. 🔍 Chatterbox — Resemble AI 저장소 — https://github.com/resemble-ai/chatterbox
38. 🔍 Coqui TTS(XTTS) — 저장소 — https://github.com/coqui-ai/TTS
39. 🔍 Orpheus TTS — Canopy Labs 저장소 — https://github.com/canopyai/Orpheus-TTS
40. 🔍 Fish Speech — 저장소 — https://github.com/fishaudio/fish-speech

**speech-to-speech**
41. 🔍 Moshi — Kyutai 저장소 — https://github.com/kyutai-labs/moshi
42. 🔍 Ultravox — Fixie 저장소 — https://github.com/fixie-ai/ultravox
43. 🔍 Qwen-Omni 계열 — Qwen 공식 GitHub 조직 — https://github.com/QwenLM
44. 🔍 Sesame CSM — 저장소 — https://github.com/SesameAILabs/csm

**오케스트레이션·전송**
45. 🔍 Pipecat — 공식 저장소 — https://github.com/pipecat-ai/pipecat
46. 🔍 LiveKit Agents — 공식 문서 — https://docs.livekit.io/agents/
47. 🔍 Vocode — 저장소 — https://github.com/vocodedev/vocode-core
48. 🔍 Rasa — 공식 사이트 — https://rasa.com/
49. 🔍 NVIDIA Riva — 공식 페이지 — https://developer.nvidia.com/riva
50. 🔍 Daily(WebRTC) — 공식 사이트 — https://www.daily.co/

### [E] 음성 벤치마크·데이터셋 (2부 3.3)

51. 🔍 VoiceBench — 저장소 — https://github.com/MatthewCYM/VoiceBench
52. 🔍 Big Bench Audio — Artificial Analysis 데이터셋(Hugging Face) — https://huggingface.co/datasets/ArtificialAnalysis/big_bench_audio
53. 🔍 Common Voice — Mozilla 공식 사이트 — https://commonvoice.mozilla.org/
54. 🔍 LibriSpeech — OpenSLR — https://www.openslr.org/12
55. 🔍 Open ASR Leaderboard — Hugging Face — https://huggingface.co/spaces/hf-audio/open_asr_leaderboard
56. 🔍 TTS Arena — Hugging Face — https://huggingface.co/spaces/TTS-AGI/TTS-Arena

### [F] 상용 음성 플랫폼 공식 문서 (2부 3.4)

57. 🔍 OpenAI Realtime API — 공식 문서 — https://platform.openai.com/docs/guides/realtime
58. 🔍 Gemini Live API — 공식 문서 — https://ai.google.dev/gemini-api/docs/live
59. 🔍 ElevenLabs Agents — 공식 문서 — https://elevenlabs.io/docs/agents-platform/overview
60. 🔍 Deepgram — 공식 문서 — https://developers.deepgram.com/
61. 🔍 Vapi — 공식 문서 — https://docs.vapi.ai/
62. 🔍 Retell AI — 공식 문서 — https://docs.retellai.com/
