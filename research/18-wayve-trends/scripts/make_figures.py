#!/usr/bin/env python3
# 사용: python3 -I scripts/make_figures.py images/
# 보고서 도식 6장을 SVG로 생성한다. 모든 내용은 보고서 본문의 출처 있는 사실만 사용한다(자체 작성 도식).
import pathlib
import sys
from datetime import date

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "images")
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
INK, MUTED, LINE, SOFT = "#1f2328", "#59636e", "#d1d9e0", "#f6f8fa"
C = {  # 구분 색
    "biz": "#2563eb", "tech": "#7c3aed", "dep": "#059669", "reg": "#d97706",
    "wayve": "#4338ca", "nv": "#4d7c0f", "mom": "#c2410c", "gray": "#6b7280",
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tw(s: str, size: float) -> float:
    """대략적 텍스트 폭(한글 1.0em, 그 외 0.58em)."""
    w = 0.0
    for ch in s:
        w += size * (1.0 if ord(ch) > 0x1100 else 0.58)
    return w


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}" role="img" aria-label="{esc(title)}">\n'
            f'<title>{esc(title)}</title>\n<rect width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>'


def rect(x, y, w, h, fill="#fff", stroke=LINE, rx=8, dash=None, sw=1.2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, stroke=LINE, sw=1.2, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#arr)"' if arrow else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'


ARROW_DEF = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
             f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>')


def box(x, y, w, h, head, lines, color, size=12.5):
    """머리띠가 있는 상자."""
    out = [rect(x, y, w, h, fill="#fff", stroke=color, sw=1.6),
           f'<path d="M{x:.1f},{y+8:.1f} a8,8 0 0 1 8,-8 h{w-16:.1f} a8,8 0 0 1 8,8 v20 h-{w:.1f} z" fill="{color}"/>',
           text(x + 12, y + 19, head, 13.5, "#fff", "bold")]
    yy = y + 46
    for ln in lines:
        out.append(text(x + 12, yy, ln, size))
        yy += size + 7
    return "\n".join(out)


# ---------------------------------------------------------------- 그림 1. 관계도
def fig_ecosystem():
    W, H = 1100, 640
    b = [ARROW_DEF]
    cx, cy, cw, ch = 400, 262, 300, 116
    b.append(rect(cx, cy, cw, ch, fill="#eef2ff", stroke=C["wayve"], sw=2.4, rx=14))
    b.append(text(cx + cw / 2, cy + 40, "Wayve", 26, C["wayve"], "bold", "middle"))
    b.append(text(cx + cw / 2, cy + 66, "AI Driver 소프트웨어 라이선스", 14, INK, "bold", "middle"))
    b.append(text(cx + cw / 2, cy + 90, "차량 제조·플릿 운영은 하지 않음", 12.5, MUTED, "normal", "middle"))

    groups = [
        (30, 20, 330, 200, "투자자 · Series D (2026-02)", C["biz"],
         ["리드: Eclipse · Balderton · SoftBank VF2", "기존: Microsoft · NVIDIA · Uber",
          "OEM 첫 직접 투자: Mercedes · Nissan ·", "  Stellantis", "연장(2026-04): AMD · Arm · Qualcomm"]),
        (740, 20, 330, 200, "OEM 양산 계약", C["biz"],
         ["Nissan — 확정 2025-12 · FY2027 일본", "Stellantis — 2026-05 · 2028 북미 (L2++)",
          "Mercedes-Benz — 확정 2026-09 · 2년 내", "세 건 모두 차종·금액 비공개"]),
        (740, 420, 330, 200, "모빌리티 · 로보택시 (Uber)", C["dep"],
         ["런던 — 감독형 유료 서비스 운영 중", "  (2026-09 개시, 안전 운전자 탑승)",
          "도쿄 — Nissan LEAF 파일럿 MoU", "  (2026년 말 목표, 미개시)", "Stellantis L4 — 3자 MoU (비구속)"]),
        (30, 420, 330, 200, "실리콘 · 컴퓨트 플랫폼", C["tech"],
         ["NVIDIA Orin — 런던 개발 플릿", "NVIDIA Thor · Hyperion — LEAF, 프랑스",
          "Qualcomm Snapdragon Ride — 사전 통합", "AMD · Arm — 통합 협력", "Mercedes 자체 HW + MB.OS"]),
    ]
    for x, y, w, h, head, col, lines in groups:
        b.append(box(x, y, w, h, head, lines, col))

    # 하단 Tier-1 / 정부
    b.append(box(400, 470, 300, 72, "Tier-1 시스템 통합", ["Valeo — Nissan ProPILOT (2026-10)"], C["gray"]))
    b.append(box(400, 20, 300, 96, "정부 · 규제",
                 ["영국 — TfL PHV 면허, AV Act 2024", "프랑스 — 정부 협력 선언 (2026-10)"], C["reg"]))

    def lab(x, y, s):
        return text(x, y, s, 12, MUTED, "bold", "middle")

    b += [line(360, 150, cx, cy + 14, C["biz"], 1.6, arrow=True), lab(362, 236, "투자"),
          line(cx + cw, cy + 14, 740, 150, C["biz"], 1.6, arrow=True), lab(740, 236, "라이선스"),
          line(cx + cw, cy + ch - 14, 740, 490, C["dep"], 1.6, arrow=True), lab(740, 404, "로보택시 탑재"),
          line(360, 490, cx, cy + ch - 14, C["tech"], 1.6, arrow=True), lab(362, 404, "구동 플랫폼"),
          line(550, 470, 550, cy + ch, C["gray"], 1.6, arrow=True), lab(600, 452, "통합"),
          line(550, 116, 550, cy, C["reg"], 1.6, arrow=True), lab(600, 240, "인허가·협력")]
    (OUT / "01-ecosystem.svg").write_text(svg(W, H, "\n".join(b), "Wayve 생태계 관계도"), encoding="utf-8")


# ---------------------------------------------------------------- 그림 2. 12개월 타임라인
def fig_timeline():
    lanes = [
        ("사업", "biz", [((2025, 12, 10), "Nissan 확정계약"), ((2026, 2, 24), "Series D $1.2B"),
                       ((2026, 4, 15), "$60M 연장"), ((2026, 5, 21), "Stellantis L2++"),
                       ((2026, 6, 17), "Stellantis·Uber L4 MoU"), ((2026, 6, 30), "테더오퍼 $8.5B"),
                       ((2026, 9, 16), "CFO 선임"), ((2026, 9, 22), "Mercedes 양산계약"),
                       ((2026, 10, 1), "Valeo Tier-1"), ((2026, 10, 23), "프랑스 협력")]),
        ("기술", "tech", [((2025, 12, 2), "GAIA-3"), ((2025, 12, 6), "NeurIPS 데모"),
                        ((2025, 12, 20), "AI-500 500개 도시"), ((2026, 3, 10), "Qualcomm 사전통합"),
                        ((2026, 3, 16), "GTC LEAF 시제차"), ((2026, 4, 28), "LA-Pose"),
                        ((2026, 5, 29), "Wayve Labs"), ((2026, 6, 3), "CVPR 강연·포스터"),
                        ((2026, 8, 3), "GAIA-4")]),
        ("배포", "dep", [((2026, 3, 12), "도쿄 파일럿 MoU"), ((2026, 6, 10), "런던 대기자 명단"),
                       ((2026, 8, 13), "도쿄 운영사 선정"), ((2026, 9, 3), "★ 런던 서비스 개시"),
                       ((2026, 10, 7), "토리노 시승"), ((2026, 10, 17), "노조 시위")]),
        ("규제", "reg", [((2025, 12, 15), "AV Act 시행령 No.1"), ((2026, 4, 20), "No.2 · APS 허가제"),
                       ((2026, 7, 1), "No.3 · 마케팅 규제"), ((2026, 8, 5), "TfL PHV 면허"),
                       ((2026, 10, 12), "런던의회 보고서")]),
    ]
    W = 1180
    x0, x1 = 110, 1150
    d0, d1 = date(2025, 11, 1), date(2026, 11, 1)

    def X(t):
        return x0 + (x1 - x0) * (date(*t) - d0).days / (d1 - d0).days

    size = 12
    lane_blocks = []
    for name, key, evs in lanes:
        rows_end = []
        placed = []
        for t, s in sorted(evs):
            x = X(t)
            wpx = tw(s, size) + 14
            lx = min(x - 4, x1 - wpx)
            r = 0
            while r < len(rows_end) and rows_end[r] > lx - 6:
                r += 1
            if r == len(rows_end):
                rows_end.append(0)
            rows_end[r] = lx + wpx
            placed.append((x, lx, wpx, r, s))
        lane_blocks.append((name, key, placed, len(rows_end)))

    top = 60
    body = []
    y = top
    lane_y = []
    for name, key, placed, nrows in lane_blocks:
        hgt = 26 + nrows * 26
        lane_y.append((y, hgt))
        body.append(rect(14, y, W - 28, hgt, fill=SOFT, stroke="none", rx=8))
        body.append(text(28, y + hgt / 2 + 5, name, 15, C[key], "bold"))
        base = y + 14
        for x, lx, wpx, r, s in placed:
            py = base + r * 26
            body.append(line(x, y + 6, x, py + 2, C[key], 1, "2,2"))
            body.append(f'<circle cx="{x:.1f}" cy="{y + 6:.1f}" r="4" fill="{C[key]}"/>')
            star = s.startswith("★")
            body.append(rect(lx, py, wpx, 21, fill=C[key] if star else "#fff", stroke=C[key], rx=10, sw=1.2))
            body.append(text(lx + 7, py + 15, s, size, "#fff" if star else INK, "bold" if star else "normal"))
        y += hgt + 10
    H = y + 30
    # 월 눈금
    head = []
    for i in range(13):
        yy, mm = (2025 + (10 + i) // 12, (10 + i) % 12 + 1)
        x = X((yy, mm, 1))
        head.append(line(x, top - 8, x, H - 26, "#e5e7eb", 1))
        if i < 12:
            lab = f"{yy % 100:02d}.{mm:02d}"
            head.append(text(x + (x1 - x0) / 24, top - 16, lab, 12, MUTED, "bold", "middle"))
    head.append(text(x0, 24, "2025-11 ~ 2026-10 주요 사건 (점 = 발생일)", 14, INK, "bold"))
    now = X((2026, 10, 30))
    head.append(line(now, top - 8, now, H - 26, "#dc2626", 1.4, "4,3"))
    head.append(text(now - 4, H - 10, "조사일 2026-10-30", 11.5, "#dc2626", "bold", "end"))
    (OUT / "02-timeline.svg").write_text(svg(W, H, "\n".join(head + body), "Wayve 최근 12개월 타임라인"), encoding="utf-8")


# ---------------------------------------------------------------- 그림 3. 상용화 로드맵(실제 vs 계획)
def fig_roadmap():
    W, H = 1180, 560
    x0, x1 = 300, 1150
    d0, d1 = date(2025, 7, 1), date(2029, 1, 1)

    def X(t):
        return x0 + (x1 - x0) * (date(*t) - d0).days / (d1 - d0).days

    b = [ARROW_DEF]
    b.append(text(20, 30, "실선·채움 = 실제(체결·운영)   점선·빈 상자 = 공식 목표(미실현)", 13.5, INK, "bold"))
    top = 70
    for yy in range(2025, 2029):
        for h in (1, 7):
            t = (yy, h, 1)
            if date(*t) < d0:
                continue
            x = X(t)
            b.append(line(x, top - 10, x, H - 40, "#e5e7eb", 1))
            if h == 1:
                b.append(text(x + 4, top - 16, str(yy), 13, MUTED, "bold"))
    b.append(line(x1, top - 10, x1, H - 40, "#e5e7eb", 1))
    rows = [
        ("런던 Uber 로보택시", "dep", [("solid", (2026, 9, 3), (2026, 10, 30), "감독형 유료 서비스 운영 중"),
                                    ("note", (2026, 11, 15), None, "→ 무인 전환: APS 허가 필요 · 일정 미정")]),
        ("도쿄 Uber 파일럿", "dep", [("mark", (2026, 3, 12), None, "MoU"),
                                 ("plan", (2026, 10, 1), (2026, 12, 31), "2026년 말 목표")]),
        ("Nissan 차세대 ProPILOT", "biz", [("mark", (2025, 12, 10), None, "확정계약"),
                                         ("plan", (2027, 4, 1), (2028, 3, 31), "FY2027 첫 모델(일본)")]),
        ("Mercedes-Benz", "biz", [("mark", (2026, 9, 22), None, "확정계약"),
                                 ("plan", (2026, 9, 22), (2028, 9, 22), "\"향후 2년 내\" 고객 제공")]),
        ("Stellantis L2++", "biz", [("mark", (2026, 5, 21), None, "파트너십"),
                                   ("plan", (2028, 1, 1), (2028, 12, 31), "2028 북미 첫 양산")]),
        ("Stellantis·Uber L4", "biz", [("mark", (2026, 6, 17), None, "MoU(비구속)"),
                                      ("note", (2026, 7, 20), None, "→ 차종·시장·일정 미정")]),
        ("프랑스 L4 (Greater Paris)", "biz", [("mark", (2026, 10, 23), None, "협력 선언"),
                                            ("plan", (2028, 1, 1), (2028, 12, 31), "2028~ 실증 계획")]),
        ("영국 AV Act 2024", "reg", [("mark", (2026, 5, 15), None, "APS 허가제 발효"),
                                    ("mark", (2027, 1, 7), None, "마케팅 규제"),
                                    ("plan", (2027, 7, 1), (2027, 12, 31), "전면 시행 목표")]),
    ]
    rh = 54
    for i, (name, key, items) in enumerate(rows):
        y = top + i * rh
        if i % 2 == 0:
            b.append(rect(14, y, W - 28, rh, fill=SOFT, stroke="none", rx=6))
        b.append(text(28, y + rh / 2 + 5, name, 13.5, INK, "bold"))
        cy = y + rh / 2
        mark_n = 0
        for kind, s, e, lab in items:
            if kind == "solid":
                xa, xb = X(s), X(e)
                b.append(rect(xa, cy - 9, max(xb - xa, 8), 18, fill=C[key], stroke=C[key], rx=4))
                b.append(text(xa - 6, cy + 5, lab, 12, C[key], "bold", "end"))
            elif kind == "plan":
                xa, xb = X(s), X(e)
                b.append(rect(xa, cy - 11, xb - xa, 22, fill="#fff", stroke=C[key], rx=4, dash="5,3", sw=1.6))
                if tw(lab, 12) + 16 < xb - xa:
                    b.append(text((xa + xb) / 2, cy + 5, lab, 12, INK, "normal", "middle"))
                elif xb + 8 + tw(lab, 12) < W - 10:
                    b.append(text(xb + 8, cy + 5, lab, 12, INK))
                else:
                    b.append(text(xa - 8, cy + 5, lab, 12, INK, "normal", "end"))
            elif kind == "note":
                b.append(text(X(s), cy + 5, lab, 12, MUTED, "bold"))
            else:
                x = X(s)
                b.append(f'<circle cx="{x:.1f}" cy="{cy:.1f}" r="6" fill="{C[key]}"/>')
                b.append(text(x, cy - 12 if mark_n % 2 == 0 else cy + 22, lab, 11.5, C[key], "bold", "middle"))
                mark_n += 1
    now = X((2026, 10, 30))
    b.append(line(now, top - 10, now, H - 40, "#dc2626", 1.4, "4,3"))
    b.append(text(now, H - 22, "조사일 2026-10-30", 11.5, "#dc2626", "bold", "middle"))
    (OUT / "04-roadmap.svg").write_text(svg(W, H, "\n".join(b), "Wayve 상용화 로드맵 — 실제와 계획"), encoding="utf-8")


# ---------------------------------------------------------------- 그림 4. 런던 서비스 발표 vs 실제
def fig_london():
    W, H = 1180, 300
    b = [ARROW_DEF]
    steps = [
        ("2025-06-10", "발표", ["\"2026년 봄 런던", "L4 완전자율 시범\""], "plan"),
        ("2026-06", "대기자 명단", ["Uber 앱 내 개설", "\"수개월 내 출범\""], "done"),
        ("2026-08-05", "TfL 면허", ["일반 PHV 면허 · 최대 15대", "1년 · 안전 운전자 필수"], "done"),
        ("2026-09-03", "서비스 개시", ["Mach-E · 표준 요금", "안전 운전자 상시 탑승"], "done"),
        ("미정", "무인 운행", ["APS 허가 필요", "신청 보도 없음 · 발급 0건"], "todo"),
    ]
    bw, gap, y = 200, 36, 70
    x = 22
    b.append(text(22, 36, "런던 Uber–Wayve: 발표된 계획과 실제 진행", 15, INK, "bold"))
    for i, (d, head, lines, st) in enumerate(steps):
        col = {"plan": C["gray"], "done": C["dep"], "todo": C["gray"]}[st]
        dash = "6,4" if st in ("plan", "todo") else None
        fill = "#ecfdf5" if st == "done" else "#fff"
        b.append(rect(x, y, bw, 150, fill=fill, stroke=col, sw=1.8, dash=dash, rx=12))
        b.append(text(x + 14, y + 28, d, 13, col, "bold"))
        b.append(text(x + 14, y + 54, head, 16, INK, "bold"))
        yy = y + 84
        for ln in lines:
            b.append(text(x + 14, yy, ln, 12.5, INK))
            yy += 22
        tag = {"plan": "계획", "done": "실제", "todo": "미실현"}[st]
        b.append(rect(x + bw - 62, y + 12, 50, 22, fill=col, stroke=col, rx=11))
        b.append(text(x + bw - 37, y + 28, tag, 12, "#fff", "bold", "middle"))
        if i < len(steps) - 1:
            b.append(line(x + bw + 4, y + 75, x + bw + gap - 4, y + 75, MUTED, 1.6, arrow=True))
        x += bw + gap
    b.append(text(22, 262, "결과: 발표 대비 약 5개월 늦게, \"L4 시범\"이 아니라 \"안전 운전자가 탑승한 일반 PHV 서비스\" 형태로 시작됨.", 13.5, INK, "bold"))
    (OUT / "05-london-service.svg").write_text(svg(W, H, "\n".join(b), "런던 서비스 발표와 실제"), encoding="utf-8")


# ---------------------------------------------------------------- 그림 5. GAIA 계보
def fig_gaia():
    W, H = 1180, 330
    b = [ARROW_DEF]
    items = [
        ("GAIA-1", "2023-10", ["비디오·텍스트·행동 조건", "생성형 세계모델 · 9B"], "생성 데모"),
        ("GAIA-2", "2025-03", ["잠재 확산 · 멀티뷰", "최대 5카메라 동시 생성"], "합성 데이터"),
        ("GAIA-3", "2025-12", ["15B · 데이터 10배", "World-on-Rails 교란"], "오프라인 평가"),
        ("GAIA-4", "2026-08", ["AI Driver in-the-loop", "반응형 에이전트 · 합성 레이더"], "폐루프 검증"),
    ]
    b.append(text(22, 34, "GAIA 세계모델 계보 — 용도가 \"데이터 생성\"에서 \"안전 검증 인프라\"로 이동", 15, INK, "bold"))
    bw, gap, x, y = 250, 48, 22, 64
    shades = ["#ede9fe", "#ddd6fe", "#c4b5fd", "#a78bfa"]
    for i, (name, d, lines, use) in enumerate(items):
        b.append(rect(x, y, bw, 170, fill=shades[i], stroke=C["tech"], sw=1.6, rx=12))
        b.append(text(x + 16, y + 34, name, 20, C["tech"] if i < 3 else "#3b0764", "bold"))
        b.append(text(x + bw - 16, y + 32, d, 13, INK, "bold", "end"))
        yy = y + 70
        for ln in lines:
            b.append(text(x + 16, yy, ln, 13, INK))
            yy += 24
        b.append(rect(x + 16, y + 126, bw - 32, 30, fill="#fff", stroke=C["tech"], rx=15))
        b.append(text(x + bw / 2, y + 146, "용도: " + use, 13, C["tech"], "bold", "middle"))
        if i < 3:
            b.append(line(x + bw + 4, y + 85, x + bw + gap - 4, y + 85, MUTED, 1.8, arrow=True))
        x += bw + gap
    b.append(text(22, 276, "GAIA-3·4는 논문 없이 블로그로 공개 · 가중치 비공개 · 성능 주장은 모두 Wayve 자체 주장(독립 검증 없음).", 13, MUTED))
    b.append(text(22, 300, "GAIA-4 메시지: \"검증은 도로 주행 거리가 아니라 컴퓨트로 확장된다\" (Simulation 2.0).", 13, MUTED))
    (OUT / "03-gaia-lineage.svg").write_text(svg(W, H, "\n".join(b), "GAIA 세계모델 계보"), encoding="utf-8")


# ---------------------------------------------------------------- 그림 6. 같은 칩 위 모델 경쟁
def fig_same_chip():
    W, H = 1180, 470
    b = []
    cols = [
        ("Nissan", "LEAF 로보택시", "L4 · 시제차", ("Wayve AI Driver", "wayve"), ("NVIDIA Hyperion", "듀얼 Thor", "nv")),
        ("Stellantis", "프랑스 L4 실증", "L4 · 2028~ 계획", ("Wayve AI Driver", "wayve"), ("NVIDIA Hyperion", "+ Halos", "nv")),
        ("Mercedes-Benz", "CLA", "L2+ · 양산 중", ("NVIDIA DRIVE AV", "nv"), ("NVIDIA Orin급", "254 TOPS", "nv")),
        ("Mercedes-Benz", "미래 차종", "주행보조 · 2년 내", ("Wayve AI Driver", "wayve"), ("Mercedes 자체 HW", "+ MB.OS", "gray")),
        ("Stellantis", "북미 차종", "L2++ · 2028", ("Wayve AI Driver", "wayve"), ("STLA AutoDrive", "SoC 비공개", "gray")),
        ("Stellantis", "Peugeot · Jeep", "ADAS · DSAT 계열", ("Momenta", "mom"), ("비공개", "", "gray")),
    ]
    b.append(text(22, 34, "같은 칩 위의 모델 경쟁 — 차량 프로그램별 \"주행 모델\"과 \"컴퓨트\" 조합", 15, INK, "bold"))
    lx, cw, gap = 150, 160, 10
    rows_y = {"oem": 60, "model": 170, "hw": 270}
    b.append(text(22, rows_y["oem"] + 42, "차량 프로그램", 13.5, MUTED, "bold"))
    b.append(text(22, rows_y["model"] + 36, "주행 모델", 13.5, MUTED, "bold"))
    b.append(text(22, rows_y["hw"] + 36, "컴퓨트", 13.5, MUTED, "bold"))
    fills = {"wayve": "#eef2ff", "nv": "#f7fee7", "mom": "#fff7ed", "gray": "#f3f4f6"}
    for i, (oem, prog, lvl, model, hw) in enumerate(cols):
        x = lx + i * (cw + gap)
        b.append(rect(x, rows_y["oem"], cw, 84, fill="#fff", stroke=LINE, rx=10))
        b.append(text(x + cw / 2, rows_y["oem"] + 24, oem, 13.5, INK, "bold", "middle"))
        b.append(text(x + cw / 2, rows_y["oem"] + 46, prog, 13, INK, "normal", "middle"))
        b.append(text(x + cw / 2, rows_y["oem"] + 68, lvl, 12, MUTED, "normal", "middle"))
        mk = model[1]
        b.append(rect(x, rows_y["model"], cw, 60, fill=fills[mk], stroke=C[mk], sw=1.8, rx=10))
        b.append(text(x + cw / 2, rows_y["model"] + 36, model[0], 13.5, C[mk], "bold", "middle"))
        hk = hw[2]
        b.append(rect(x, rows_y["hw"], cw, 60, fill=fills[hk], stroke=C[hk], sw=1.8, rx=10))
        b.append(text(x + cw / 2, rows_y["hw"] + 26, hw[0], 13, C[hk] if hk != "gray" else INK, "bold", "middle"))
        if hw[1]:
            b.append(text(x + cw / 2, rows_y["hw"] + 46, hw[1], 12, MUTED, "normal", "middle"))
        for a, bb in (("oem", "model"), ("model", "hw")):
            y1 = rows_y[a] + (84 if a == "oem" else 60)
            b.append(line(x + cw / 2, y1, x + cw / 2, rows_y[bb], LINE, 1.4))
    # 범례·주석
    y = 360
    leg = [("wayve", "Wayve"), ("nv", "NVIDIA"), ("mom", "Momenta"), ("gray", "OEM 자체·비공개")]
    x = 150
    for k, s in leg:
        b.append(rect(x, y, 18, 18, fill=fills[k], stroke=C[k], sw=1.6, rx=4))
        b.append(text(x + 26, y + 14, s, 12.5, INK))
        x += 40 + tw(s, 12.5) + 20
    b.append(text(150, 410, "NVIDIA는 Wayve의 투자자이자 컴퓨트 공급자이면서, Mercedes CLA에는 자사 모델을 직접 공급하는 경쟁자다.", 13, INK, "bold"))
    b.append(text(150, 436, "Mercedes·Stellantis는 모두 두 곳 이상의 주행 모델 공급사를 병행한다.", 13, INK))
    (OUT / "06-same-chip.svg").write_text(svg(W, H, "\n".join(b), "같은 칩 위 모델 경쟁 구조"), encoding="utf-8")


for f in (fig_ecosystem, fig_timeline, fig_roadmap, fig_london, fig_gaia, fig_same_chip):
    f()
print("figures:", sorted(p.name for p in OUT.glob("*.svg")))
