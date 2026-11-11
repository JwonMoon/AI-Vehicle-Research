# 출처 목록 — AI 에이전트·멀티 에이전트 학습 트랙 (로드맵·요약본·자료 가이드 공용)

> **작성일 / URL 확인일**: 2026-11-11
> **성격**: `../roadmap.md`, `../primer.md`, `../reading-guide.md` 세 문서가 `[번호]`로 인용하는 단일 출처 목록. 번호는 로드맵 단계 순서(개념 → 벤치마크 → 프레임워크·프로토콜)로 매겼다.
> **등급 범례**: 🔍 공식(프로젝트 공식 사이트·저장소·리더보드·사양서) · 📄 논문·기술 블로그 · 📰 언론·서드파티 · 💬 포럼
> **확인 방법**: 2026-11-11에 각 URL에 HTTP 요청을 보내 응답 코드를 기록했다. 🟢 200 정상 · 🟡 리다이렉트(새 주소 병기) · 🔴 봇 차단 또는 이 환경에서 접속 불가(주소 자체는 공식 진입점으로 알려진 것, 브라우저로 재확인 권장). 논문은 arXiv 초록 페이지에서 제목·게시일을 확인했고, 핵심 자료 10여 건은 본문(HTML판)을 열어 장·표·그림 구성을 확인했다(자료 가이드에 반영).
> **원칙**: 저장소의 기존 문서는 참고·인용하지 않았다. 2차 블로그·벤더 비교글은 수록하지 않는다.

## [A] 1단계 — 개념 뼈대 (에이전트 기본 구조·멀티 에이전트 패턴·언제 도움이 되는가)

1. 📄 Lilian Weng, "LLM Powered Autonomous Agents" (2023-06-23) — https://lilianweng.github.io/posts/2023-06-23-agent/ 🟢
2. 📄 Anthropic, "Building effective agents" (2024-12-19) — https://www.anthropic.com/engineering/building-effective-agents 🟢
3. 📄 Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022-10-06) — https://arxiv.org/abs/2210.03629 🟢
4. 📄 Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools" (2023-02-09) — https://arxiv.org/abs/2302.04761 🟢 (선택)
5. 📄 Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning" (2023-03-20) — https://arxiv.org/abs/2303.11366 🟢 (선택)
6. 📄 Li et al., "CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Model Society" (2023-03-31) — https://arxiv.org/abs/2303.17760 🟢
7. 📄 Hong et al., "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" (2023-08-01) — https://arxiv.org/abs/2308.00352 🟢
8. 📄 Qian et al., "ChatDev: Communicative Agents for Software Development" (2023-07-16) — https://arxiv.org/abs/2307.07924 🟢
9. 📄 Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" (2023-08-16) — https://arxiv.org/abs/2308.08155 🟢
10. 📄 Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate" (2023-05-23) — https://arxiv.org/abs/2305.14325 🟢
11. 📄 Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (2023-04-07) — https://arxiv.org/abs/2304.03442 🟢 (선택)
12. 📄 Anthropic, "How we built our multi-agent research system" (2025-06-13) — https://www.anthropic.com/engineering/multi-agent-research-system 🟢
13. 📄 Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (UC Berkeley, 2025-03-17; MAST 분류) — https://arxiv.org/abs/2503.13657 🟢 · 본문 HTML https://arxiv.org/html/2503.13657
14. 📄 Kim et al., "Towards a Science of Scaling Agent Systems" (Google Research·MIT, 2025-12-09) — https://arxiv.org/abs/2512.08296 🟢 · Google Research 블로그 "Towards a science of scaling agent systems: When and why agent systems work" https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ 🟢
15. 📄 LangChain, "How and when to build multi-agent systems" — https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems 🟡 (구 주소 blog.langchain.com/… 가 이 주소로 301 리다이렉트. 새 호스트는 이 환경에서 접속 불가, 본문 미열람)

## [B] 2단계 — 정량 baseline (벤치마크·리더보드·평가 방법론)

16. 🔍 SWE-bench 공식 리더보드 — https://www.swebench.com/ 🟢 (Verified·Multimodal·Multilingual·Lite·Full·Bash Only 탭, "Resolved vs cost" 등 비교 차트 제공) · 📄 Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (2023-10-10) https://arxiv.org/abs/2310.06770 🟢 · 🔍 OpenAI, "Introducing SWE-bench Verified" https://openai.com/index/introducing-swe-bench-verified/ 🔴(봇 차단 403) · 🔍 SWE-bench Pro 리더보드 https://labs.scale.com/leaderboard/swe_bench_pro 🟡(scale.com/… 에서 308 리다이렉트, 접속 불가)
17. 🔍 Terminal-Bench 공식 사이트·리더보드 — https://www.tbench.ai/ 🟢 (확인일 기준 사이트 표기 "TERMINAL-BENCH 4.1", 리더보드 열: RANK · MODEL · AGENT · RESOLUTION RATE · COST · TOKENS)
18. 🔍 τ-bench / τ²-bench 공식 저장소 (Sierra Research) — https://github.com/sierra-research/tau2-bench 🔴(curl 403, 다른 경로로 README·용어집 열람 확인) · 📄 Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" (2024-06-17) https://arxiv.org/abs/2406.12045 🟢 · 📄 Barres et al., "τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment" (2025-06-09) https://arxiv.org/abs/2506.07982 🟢
19. 🔍 GAIA 리더보드 (Hugging Face) — https://huggingface.co/gaia-benchmark 🟢 · 📄 Mialon et al., "GAIA: a benchmark for General AI Assistants" (2023-11-21) https://arxiv.org/abs/2311.12983 🟢
20. 🔍 BrowseComp — https://openai.com/index/browsecomp/ 🔴(봇 차단 403) · 📄 Wei et al., "BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents" (2025-04-16) https://arxiv.org/abs/2504.12516 🟢 · 데이터·평가 코드 https://github.com/openai/simple-evals
21. 🔍 OSWorld — https://os-world.github.io/ 🟡(osworld-v1.xlang.ai 로 301 리다이렉트, 이 환경에서 접속 불가)
22. 🔍 BFCL — Berkeley Function-Calling Leaderboard (확인일 기준 V4) — https://gorilla.cs.berkeley.edu/leaderboard.html 🟢
23. 📄 Liu et al., "AgentBench: Evaluating LLMs as Agents" (2023-08-07) — https://arxiv.org/abs/2308.03688 🟢 · 저장소 https://github.com/THUDM/AgentBench
24. 📄 Zhu et al., "MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents" (2025-03-03; MARBLE 프레임워크) — https://arxiv.org/abs/2503.01935 🟢 · 저장소 https://github.com/MultiagentBench/MARBLE
25. 📄 "Architectural Design, Not Only Model Intelligence, Governs Multi-Agent LLM Performance" (2026-02-03; MAFBench) — https://arxiv.org/abs/2602.03128 🟢 (검색 결과·2차 글에서는 "Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis" 제목으로도 불림 — arXiv 현재 제목은 전자)
26. 📄 Yehudai et al., "Survey on Evaluation of LLM-based Agents" (2025-03-20) — https://arxiv.org/abs/2503.16416 🟢
27. 🔍 HAL — Holistic Agent Leaderboard (Princeton; 비용 병기·제3자 운영) — https://hal.cs.princeton.edu/ 🟢
28. 📄 Berkeley RDI, "We Scored 100% on AI Benchmarks Without Solving a Single Problem" (Hao Wang·Qiuyang Mang·Alvin Cheung·Koushik Sen·Dawn Song, UC Berkeley, 2026-04) — https://rdi.berkeley.edu/blog/trustworthy-benchmarks 🟢 · 도구 https://github.com/moogician/trustworthy-env

## [C] 3단계 — 정성 비교 (프로토콜·프레임워크 공식 문서)

29. 🔍 Model Context Protocol (MCP) — https://modelcontextprotocol.io/ 🟢 · 사양 https://modelcontextprotocol.io/specification/latest (확인일 기준 사양 버전 2026-07-28) · 아키텍처 개요 https://modelcontextprotocol.io/docs/learn/architecture
30. 🔍 Agent2Agent (A2A) Protocol — https://a2a-protocol.org/ 🟢 (Linux Foundation 산하, Apache 2.0) · 사양 https://a2a-protocol.org/latest/specification/ · 핵심 개념 https://a2a-protocol.org/latest/topics/key-concepts/ · "A2A and MCP" https://a2a-protocol.org/latest/topics/a2a-and-mcp/
31. 🔍 LangGraph 공식 문서 — https://docs.langchain.com/oss/python/langgraph/overview 🟡(구 주소 langchain-ai.github.io/langgraph/ 는 "Documentation has moved" 안내 페이지)
32. 🔍 CrewAI 공식 문서 — https://docs.crewai.com/ 🟢
33. 🔍 OpenAI Agents SDK 공식 문서 — https://openai.github.io/openai-agents-python/ 🟢
34. 🔍 Google Agent Development Kit (ADK) 공식 문서 — https://adk.dev/ 🟡(구 주소 google.github.io/adk-docs/ 에서 301 리다이렉트, 새 호스트는 이 환경에서 접속 불가)
35. 🔍 Microsoft Agent Framework 개요 (AutoGen + Semantic Kernel 통합 후속) — https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview 🟢
36. 🔍 Claude Agent SDK 개요 — https://platform.claude.com/docs/en/agent-sdk/overview 🟢 (docs.claude.com 경로도 동일 내용 200)

## 보조 참고 (본문에서 간접 인용)

37. 🔍 AG2 (구 AutoGen 커뮤니티 분기) 저장소 — https://github.com/ag2ai/ag2 · 🔍 smolagents (Hugging Face) — https://github.com/huggingface/smolagents (프레임워크 지형 설명용, 본문 미열람)
