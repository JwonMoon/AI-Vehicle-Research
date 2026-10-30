#!/usr/bin/env python3
# 사용: python3 -I scripts/make_figures.py images/
# 자체 작성 도식 3장(스택 지도 · 주행 모델 × 컴퓨트 · R-Car X5H 한 칩)을 SVG로 생성한다.
# 모든 내용은 보고서 본문의 출처 있는 사실만 사용한다. 그리기 도우미는 18-wayve-trends/scripts/make_figures.py와 같다.
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "images")
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
INK, MUTED, LINE, SOFT = "#1f2328", "#59636e", "#d1d9e0", "#f6f8fa"
C = {"rt": "#2563eb", "adas": "#d97706", "base": "#6b7280", "safe": "#059669", "nv": "#4d7c0f", "rc": "#7c3aed"}
FILL = {"rt": "#eff6ff", "adas": "#fffbeb", "base": "#f3f4f6", "safe": "#ecfdf5", "nv": "#f7fee7", "rc": "#f5f3ff"}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}" role="img" aria-label="{esc(title)}">\n<title>{esc(title)}</title>\n'
            f'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>'


def rect(x, y, w, h, fill="#fff", stroke=LINE, rx=8, sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, stroke=MUTED, sw=1.4, arrow=False, dash=None):
    m = ' marker-end="url(#arr)"' if arrow else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{m}{d}/>'


def box(x, y, w, h, head, lines, k, size=13):
    out = [rect(x, y, w, h, FILL[k], C[k], 10, 1.6), text(x + 14, y + 26, head, 14.5, C[k], "bold")]
    yy = y + 50
    for ln in lines:
        out.append(text(x + 14, yy, ln, size))
        yy += size + 9
    return "\n".join(out)


# ---------------------------------------------------------------- 그림: 스택 지도(핵심만)
def fig_map():
    W, H = 1100, 560
    b = [text(W / 2, 34, "AWF 스택 지도 — 두 트랙과 공통 기반 (2026-10)", 18, INK, "bold", "middle")]
    cw = 510
    for i, (k, title, wg) in enumerate([("rt", "① 로보택시 · L4", "Software WG · Robotaxi WG"),
                                        ("adas", "② ADAS · 개인차량(POV)", "ADAS WG (옛 POV WG)")]):
        x = 30 + i * (cw + 20)
        b.append(rect(x, 54, cw, 46, C[k], C[k], 10))
        b.append(text(x + cw / 2, 76, title, 17, "#fff", "bold", "middle"))
        b.append(text(x + cw / 2, 94, wg, 12.5, "#fff", "normal", "middle"))
    b.append(box(30, 114, cw, 120, "주행 스택: Autoware 2.0.0 (2026-10-29)",
                 ["core 1.10.0 + universe 0.53.1 + launch 0.53.0", "planning_setting = rule_based | diffusion_planner",
                  "Selector(안전 게이트·순위화)는 아직 미기동"], "rt"))
    b.append(box(560, 114, cw, 120, "주행 스택: Vision Pilot 1.2 (2026-08-10)",
                 ["오픈소스 L2 ADAS · Apache 2.0(가중치 포함)", "단안 카메라 1대 · HD맵 없음 · ONNX Runtime",
                  "목표: 3–5 INT8 TOPS 칩에서 10 FPS 이상"], "adas"))
    b.append(box(30, 248, cw, 120, "학습 모델",
                 ["Diffusion Planner (2.0.0 런치에 포함)", "AutoE2E · LatentDrive · OnePlanner (독립 런타임)",
                  "연산: NVIDIA GPU · TensorRT 전제"], "rt"))
    b.append(box(560, 248, cw, 120, "학습 모델",
                 ["AutoSteer (경로) · AutoSpeed (CIPO) · AutoDrive (E2E)", "AutoSeg 계열 (SceneSeg · Scene3D · EgoLanes …)",
                  "INT8 ONNX 가중치 제공"], "adas"))
    b.append(rect(30, 386, 1040, 140, FILL["base"], C["base"], 10, 1.4))
    b.append(text(48, 412, "공통 기반", 14.5, C["base"], "bold"))
    cols = [("모델 배포", ["Hugging Face", "AutowareFoundation"]),
            ("패키지 유통", ["Autoware Index", "Reference Design"]),
            ("배포", ["Open AD Kit", "v2.0 Autoware → v2.1 Vision Pilot"]),
            ("안전", ["Safety Island", "S32Z · R-Car X5H (Cortex-R52)"])]
    for j, (h, ls) in enumerate(cols):
        x = 48 + j * 258
        b.append(rect(x, 424, 240, 88, "#fff", LINE, 8))
        b.append(text(x + 120, 448, h, 13.5, INK, "bold", "middle"))
        for n, s in enumerate(ls):
            b.append(text(x + 120, 472 + n * 20, s, 12.5, MUTED if n else INK, "normal", "middle"))
    b.append(text(W / 2, 550, "두 트랙은 같은 E2E 진화 방향(Architecture 2.0)을 공유하지만, 코드베이스·센서·연산·릴리스는 별개다.", 13, MUTED, "normal", "middle"))
    (OUT / "01-awf-stack-map.svg").write_text(svg(W, H, "\n".join(b), "AWF 스택 지도"), encoding="utf-8")


# ---------------------------------------------------------------- 그림: 주행 모델 × 컴퓨트
def fig_model_compute():
    W, H = 1180, 520
    cols = [
        ("Diffusion Planner", "rt", "Autoware 2.0.0 생성기", "TensorRT", "NVIDIA GPU", "필수"),
        ("OnePlanner", "rt", "LiDAR BEV + 벡터맵", "TensorRT 10", "NVIDIA GPU", "RTX PRO 6000: p50 12.7 ms"),
        ("LatentDrive", "rt", "카메라 1·3대 2 s 영상", "TensorRT 10.8", "NVIDIA GPU", "연구 모델"),
        ("AutoE2E", "rt", "서라운드 카메라 6대", "PyTorch", "NVIDIA GPU", "RTX 5080: 최대 약 76 FPS"),
        ("Alpamayo 노드", "rt", "카메라 4대 (포크)", "Python · ROS 2", "NVIDIA GPU", "VRAM 24 GB 이상 권장"),
        ("Vision Pilot", "adas", "단안 카메라 1대", "ONNX Runtime", "양산 칩 / CPU 가능", "3–5 INT8 TOPS · 10 FPS+"),
        ("Safety Island", "safe", "궤적 → 제어 명령", "Zephyr · FreeRTOS", "S32Z · R-Car X5H", "Cortex-R52 (CR52 Core1)"),
    ]
    b = [text(22, 34, "주행 모델과 컴퓨트 — 문서에 적힌 실행 환경", 17, INK, "bold")]
    rows = [("모델·스택", 60, 52), ("입력", 126, 44), ("런타임", 184, 44), ("연산", 242, 56)]
    for name, y, h in rows:
        b.append(text(22, y + h / 2 + 5, name, 13.5, MUTED, "bold"))
    lx, cw, gap = 120, 142, 8
    for i, (m, k, inp, rt, hw, note) in enumerate(cols):
        x = lx + i * (cw + gap)
        b.append(rect(x, 60, cw, 52, FILL[k], C[k], 10, 1.8))
        b.append(text(x + cw / 2, 91, m, 13.5, C[k], "bold", "middle"))
        b.append(rect(x, 126, cw, 44, "#fff", LINE, 8))
        b.append(text(x + cw / 2, 153, inp, 11.5, INK, "normal", "middle"))
        b.append(rect(x, 184, cw, 44, "#fff", LINE, 8))
        b.append(text(x + cw / 2, 211, rt, 12, INK, "normal", "middle"))
        hk = "nv" if hw.startswith("NVIDIA") else ("rc" if "X5H" in hw else "adas")
        b.append(rect(x, 242, cw, 56, FILL[hk], C[hk], 10, 1.6))
        b.append(text(x + cw / 2, 266, hw, 12.5, C[hk], "bold", "middle"))
        b.append(text(x + cw / 2, 286, note, 10.5, MUTED, "normal", "middle"))
        for y1, y2 in ((112, 126), (170, 184), (228, 242)):
            b.append(line(x + cw / 2, y1, x + cw / 2, y2, LINE, 1.3))
    # brackets
    rx0, rx1 = lx, lx + 5 * (cw + gap) - gap
    b.append(line(rx0, 318, rx1, 318, C["rt"], 2))
    b.append(text((rx0 + rx1) / 2, 340, "① 로보택시·L4 — Generator 후보는 모두 NVIDIA GPU 전제", 13.5, C["rt"], "bold", "middle"))
    ax = lx + 5 * (cw + gap)
    b.append(line(ax, 318, ax + cw, 318, C["adas"], 2))
    b.append(text(ax + cw / 2, 340, "② ADAS", 13.5, C["adas"], "bold", "middle"))
    sx = lx + 6 * (cw + gap)
    b.append(line(sx, 318, sx + cw, 318, C["safe"], 2))
    b.append(text(sx + cw / 2, 340, "공통 안전층", 13.5, C["safe"], "bold", "middle"))
    notes = ["• Generator-Selector는 회원사 사내 독점 모델도 생성기로 명시한다 — 같은 스택 위에서 생성기를 바꿔 끼우는 구조.",
             "• 2.0.0 런치에 실제로 들어간 생성기는 규칙 기반과 Diffusion Planner 둘뿐이고, 한 번에 하나만 돈다.",
             "• POV 가이드: NVIDIA GPU는 지원, AMD · Qualcomm · Hailo-8 NPU는 로드맵. Jetson AGX Orin에서 AutoSeg FP16 약 29–30 FPS.",
             "• R-Car X5H 한 칩에 AutoSD(Cortex-A720AE)와 FreeRTOS(Cortex-R52)를 함께 올리는 이식이 2026-09 완료됐다."]
    for n, s in enumerate(notes):
        b.append(text(120, 384 + n * 30, s, 13, INK if n in (0, 3) else MUTED, "bold" if n in (0, 3) else "normal"))
    (OUT / "16-model-compute.svg").write_text(svg(W, H, "\n".join(b), "주행 모델과 컴퓨트"), encoding="utf-8")


# ---------------------------------------------------------------- 그림: R-Car X5H 한 칩
def fig_x5h():
    W, H = 1100, 470
    b = [text(22, 34, "R-Car X5H 한 칩 안의 구성 — 애플리케이션 코어와 안전 코어", 17, INK, "bold")]
    b.append(rect(30, 56, 640, 300, FILL["rc"], C["rc"], 14, 2))
    b.append(text(50, 84, "Renesas R-Car X5H (단일 SoC)", 15, C["rc"], "bold"))
    b.append(box(52, 104, 290, 150, "Cortex-A720AE 클러스터", ["OS: AutoSD", "CES 2026 MCO/MRM 데모 스택 이식", "(Open AD Kit 이슈 #120)"], "rt", 13))
    b.append(box(358, 104, 290, 150, "Cortex-R52 클러스터", ["OS: FreeRTOS", "Safety Island 타깃 freertos-x5h", "= CR52 (Core1)"], "safe", 13))
    b.append(line(342, 200, 356, 200, MUTED, 2, True))
    b.append(line(358, 214, 344, 214, MUTED, 2, True))
    b.append(text(350, 284, "칩 내부 RPMsg — 이더넷 연결을 대체", 13, INK, "bold", "middle"))
    b.append(text(350, 308, "2026-08-07 보드에서 왕복 100/100 확인 · 2026-09-02 완료", 12.5, MUTED, "normal", "middle"))
    b.append(text(350, 334, "이전(CES 2026): 두 상자를 CycloneDDS로 연결", 12.5, MUTED, "normal", "middle"))
    bx = 700
    items = [("Open AD Kit v2.1 (CES 2027 이후)", "주 소비자: \"X5H, Vision Pilot\"", "adas"),
             ("L2 Safety Island 실험 (2026-10-15 보고)", "Vision Pilot 계획 → Safety Island 승인·정지 · CARLA", "safe"),
             ("L4 안전섬 설계 · 최대 안전 분기", "카메라 + 레이더 4대 + 초음파 + IMU/GNSS on X5H", "rc"),
             ("L4 안전섬 설계 · 최소 비용 분기", "S32Z2 · AURIX TC4x · Stellar MCU, 레이더 없음", "base")]
    for n, (h, s, k) in enumerate(items):
        y = 56 + n * 76
        b.append(rect(bx, y, 370, 64, FILL[k], C[k], 10, 1.4))
        b.append(text(bx + 14, y + 26, h, 13.5, C[k], "bold"))
        b.append(text(bx + 14, y + 48, s, 12, INK))
    b.append(text(30, 396, "근거: Open AD Kit 이슈 #120 · 로드맵 #91 · WG 회의 #7357 · Reference Design WG #7358 · autoware-safety-island README", 12, MUTED))
    b.append(text(30, 420, "그림은 문서에 적힌 사실을 나란히 놓은 것이며, Vision Pilot이 X5H의 A720AE 클러스터에서 실행됐다는 기록은 확인되지 않았다.", 12, MUTED))
    (OUT / "18-x5h-one-chip.svg").write_text(svg(W, H, "\n".join(b), "R-Car X5H 한 칩 구성"), encoding="utf-8")


for f in (fig_map, fig_model_compute, fig_x5h):
    f()
print("figures written")
