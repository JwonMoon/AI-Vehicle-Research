#!/usr/bin/env python3
"""results.csv 로부터 보고서 §4.2 의 막대 그래프(images/05-bench-results.svg)를 만든다.

측정값을 손으로 옮겨 적지 않기 위한 스크립트다. run.sh 를 다시 돌린 뒤
이 스크립트를 다시 실행하면 그림이 최신 측정치로 갱신된다.

사용:  python3 make_chart.py [results.csv] [출력.svg]
"""
import csv
import html
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "../reference/bench-logs/results.csv"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "../images/05-bench-results.svg"

# --- 색: 포맷(엔티티)에 색을 고정한다. 변형(arena/재사용/스크래치)은 같은 색 + 라벨로 구분 ---
C_PB = "#eb6834"      # Protobuf
C_CP = "#2a78d6"      # Cap'n Proto
C_CPP = "#1baf7a"     # Cap'n Proto (packed)
INK, INK2, MUTED, LINE = "#15181d", "#4d545e", "#848a94", "#cdd3db"

COLOR = {
    "protobuf": C_PB, "protobuf-reuse": C_PB, "protobuf-arena": C_PB,
    "capnp": C_CP, "capnp-scratch": C_CP, "capnp-packed": C_CPP,
}
LABEL = {
    "protobuf": "Protobuf", "protobuf-reuse": "Protobuf · 객체 재사용",
    "protobuf-arena": "Protobuf · arena", "capnp": "Cap'n Proto",
    "capnp-scratch": "Cap'n Proto · 스크래치", "capnp-packed": "Cap'n Proto · packed",
}

vals = {}
with open(CSV, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        vals[(r["message"], r["variant"], r["metric"])] = float(r["value"])


def series(msg, metric, variants):
    out = []
    for v in variants:
        key = (msg, v, f"{metric}_mean")
        if key in vals:
            out.append((v, vals[key]))
    return out


PB_ENC = ["protobuf", "protobuf-arena", "protobuf-reuse"]
CP_ENC = ["capnp", "capnp-scratch"]
PB_DEC = ["protobuf", "protobuf-reuse"]
CP_DEC = ["capnp", "capnp-packed"]

PANELS = [
    ("A", "VehicleState · 65–96 B (고빈도 상태)", [
        ("인코딩", series("A", "encode", PB_ENC + CP_ENC)),
        ("디코딩 + 전체 읽기", series("A", "decode", PB_DEC + CP_DEC)),
        (None, []),
    ]),
    ("B", "ObjectList · 6.4 KB (인지 객체 64개)", [
        ("인코딩", series("B", "encode", PB_ENC + CP_ENC)),
        ("디코딩 + 전체 읽기", series("B", "decode", PB_DEC + CP_DEC)),
        ("헤더 필드 1개만 읽기", series("B", "peek", ["protobuf", "capnp"])),
    ]),
    ("C", "SensorFrame · 1 MiB (센서 페이로드)", [
        ("인코딩", series("C", "encode", ["protobuf", "capnp"])),
        ("디코딩 + 전체 읽기", series("C", "decode", ["protobuf", "capnp"])),
        ("헤더 필드 1개만 읽기", series("C", "peek", ["protobuf", "capnp"])),
    ]),
]

W = 1240
COL_X = [40, 450, 850]
COL_W = [370, 360, 350]
LABEL_W = 152
BAR_H, BAR_GAP = 17, 9
e = html.escape
S = []


def fmt(ns):
    if ns >= 1000:
        return f"{ns/1000:,.1f} µs"
    return f"{ns:,.1f} ns"


def panel(x, w, y, title, data):
    """가로 막대 하나. 패널마다 자기 축을 쓴다(값 범위가 자릿수로 다르므로)."""
    if not data:
        return y
    S.append(f'<text x="{x}" y="{y}" font-size="12.5" font-weight="700" fill="{INK}">{e(title)}</text>')
    y += 12
    bar_x = x + LABEL_W
    bar_w = w - LABEL_W - 62
    vmax = max(v for _, v in data)
    for variant, v in data:
        y += BAR_GAP + BAR_H
        cy = y - BAR_H / 2 + 0.5
        S.append(f'<text x="{bar_x - 8}" y="{cy + 4}" text-anchor="end" font-size="11.5" '
                 f'fill="{INK2}">{e(LABEL[variant])}</text>')
        bw = max(2.0, bar_w * v / vmax)
        S.append(f'<rect x="{bar_x}" y="{y - BAR_H}" width="{bw:.1f}" height="{BAR_H}" rx="4" '
                 f'fill="{COLOR[variant]}"/>')
        S.append(f'<text x="{bar_x + bw + 7:.1f}" y="{cy + 4}" font-size="11.5" '
                 f'font-family="\'IBM Plex Mono\',monospace" fill="{INK}">{fmt(v)}</text>')
    return y + 6


rows = []
yy = 132
for msg, subtitle, panels in PANELS:
    S.append(f'<text x="40" y="{yy}" font-size="15" font-weight="700" fill="{INK}">'
             f'{e(msg)}. {e(subtitle)}</text>')
    S.append(f'<line x1="40" y1="{yy+9}" x2="{W-40}" y2="{yy+9}" stroke="{LINE}"/>')
    ybase = yy + 26
    ymax = ybase
    for i, (title, data) in enumerate(panels):
        if title is None:
            continue
        ymax = max(ymax, panel(COL_X[i], COL_W[i], ybase, title, data))
    yy = ymax + 34

H = yy + 58

head = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    'font-family="\'Pretendard\',\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif" '
    'role="img" aria-label="Cap\'n Proto 와 Protobuf 의 인코딩·디코딩·단일 필드 읽기 실측 결과">',
    f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
    f'<text x="40" y="44" font-size="23" font-weight="700" fill="{INK}">직접 측정한 결과 — 짧을수록 빠르다</text>',
    f'<text x="40" y="70" font-size="13.5" fill="{INK2}">막대 길이는 <tspan font-weight="700">패널 안에서만</tspan> 비교한다. '
    '패널마다 값의 자릿수가 달라 축을 따로 썼다.</text>',
]
# 범례
lx = 40
head.append(f'<text x="{lx}" y="{100}" font-size="12" fill="{MUTED}">색 = 포맷</text>')
lx += 66
for c, t in [(C_PB, "Protobuf"), (C_CP, "Cap'n Proto"), (C_CPP, "Cap'n Proto · packed")]:
    head.append(f'<rect x="{lx}" y="{91}" width="11" height="11" rx="2.5" fill="{c}"/>')
    head.append(f'<text x="{lx+17}" y="{100}" font-size="12" fill="{INK2}">{e(t)}</text>')
    lx += 22 + len(t) * 7.2 + 26

foot = (f'<text x="40" y="{H-26}" font-size="11.5" fill="{MUTED}">'
        'Intel Xeon @ 2.10GHz(4 vCPU) · Ubuntu 24.04 · g++ 13.3 -O2 · capnp 1.0.1 · protobuf 3.21.12 · 단일 스레드 · 2026-09-21 측정. '
        '공용 클라우드 vCPU 이므로 절대값보다 같은 패널 안의 비율을 보라. '
        '재현: scripts/run.sh · 자체 작성</text>')

OUT.write_text("\n".join(head + S + [foot, "</svg>"]) + "\n", encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} B, {W}x{H})")
