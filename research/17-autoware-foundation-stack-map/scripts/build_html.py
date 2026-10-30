#!/usr/bin/env python3
# 사용: python3 -I scripts/build_html.py classic   → autoware-foundation-stack-map.html (1판 디자인)
#       python3 -I scripts/build_html.py anthropic → autoware-foundation-stack-map-anthropic.html (Anthropic 보고서풍)
# 의존: pip install markdown. 본문의 [n] 인용을 reference/references.md의 n번 URL로 연결한 자체 완결 HTML을 만든다.
import html
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEME = sys.argv[1] if len(sys.argv) > 1 else "classic"
OUT = {"classic": "autoware-foundation-stack-map.html", "anthropic": "autoware-foundation-stack-map-anthropic.html"}[THEME]
src = (ROOT / "autoware-foundation-stack-map.md").read_text(encoding="utf-8")

# --- 출처 목록: "n. 등급 매체 — 제목 — 날짜 — URL"
refs = {}
for ln in (ROOT / "reference" / "references.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"^(\d{1,3})\.\s+(.*)$", ln)
    if m:
        body = m.group(2)
        urls = re.findall(r"https?://[^\s)]+", body)
        refs[int(m.group(1))] = {"title": re.sub(r"\s*—\s*https?://.*$", "", body).strip(), "url": urls[0] if urls else "", "raw": body}

title = re.search(r"^#\s+(.+)$", src, re.M).group(1).strip()
body_md = src.split("\n", 1)[1]
body_md, _ = re.split(r"^## 출처\s*$", body_md, maxsplit=1, flags=re.M)

# Python-Markdown은 문단 바로 뒤의 목록을 목록으로 읽지 않으므로(GitHub는 읽음) 빈 줄을 넣는다. 인용문(>) 안도 같다.
_lines, _prev = [], ""
for _ln in body_md.splitlines():
    _q = re.match(r"^(>\s?)?(.*)$", _ln)
    _pre, _txt = _q.group(1) or "", _q.group(2)
    _pq = re.match(r"^(>\s?)?(.*)$", _prev)
    _ptxt = _pq.group(2)
    if re.match(r"^(\d+\.|[-*])\s", _txt) and _ptxt.strip() and not re.match(r"^\s*(\d+\.|[-*])\s", _ptxt) and not _ptxt.startswith("|"):
        _lines.append(_pre.rstrip() if _pre else "")
    _lines.append(_ln)
    _prev = _ln
body_md = "\n".join(_lines) + "\n"


def cite(m):
    out = []
    for n in (int(x) for x in re.findall(r"\d+", m.group(0))):
        r = refs.get(n)
        t = html.escape(r["title"], quote=True) if r else "출처 목록에 없음"
        href = html.escape(r["url"]) if r and r["url"] else f"#src-{n}"
        out.append(f'<a class="cite" href="{href}" target="_blank" rel="noopener" title="{t}">{n}</a>')
    return '<sup class="cites">' + "".join(out) + "</sup>"


body_md = re.sub(r"(?<![\w\]])\[(\d{1,3}(?:\]\[\d{1,3})*)\](?!\()", cite, body_md)

md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list", "md_in_html", "sane_lists"],
                       extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}}, output_format="html5")
body = md.convert(body_md)
toc = md.toc

# 그림: 이미지 문단 + 바로 뒤 *그림 N. …* 문단 → <figure>
def fig(m):
    img, cap = m.group(1), m.group(2)
    cm = re.match(r"그림 (\d+)\.\s*(.*)", cap, re.S)
    num, txt = (cm.group(1), cm.group(2)) if cm else ("", cap)
    parts = re.split(r"\s+·\s+(?=(원본|자체 작성))", txt, maxsplit=1)
    head = parts[0]
    note = txt[len(head):].lstrip(" ·") if len(parts) > 1 else ""
    return (f'<figure data-num="{num}">{img}<figcaption><span class="fig-label">그림 {num}</span>'
            f'<span class="fig-title">{head}</span>' + (f'<span class="fig-note">{note}</span>' if note else "") + "</figcaption></figure>")


body = re.sub(r"<p>(<img [^>]+>)</p>\s*<p><em>(.*?)</em></p>", fig, body, flags=re.S)
body = body.replace("<blockquote>", '<blockquote class="meta">', 1)
body = re.sub(r"<blockquote>\s*<p><strong>요점</strong>", '<blockquote class="key"><p><strong>요점</strong>', body)
body = re.sub(r"<table>", '<div class="tw"><table>', body).replace("</table>", "</table></div>")

items = []
for n in sorted(refs):
    t = html.escape(refs[n]["raw"])
    t = re.sub(r"(https?://[^\s)]+)", lambda u: f'<a href="{u.group(1)}" target="_blank" rel="noopener">{u.group(1)}</a>', t)
    items.append(f'<li id="src-{n}" value="{n}">{t}</li>')
refs_html = '<h2 id="sources">출처</h2>\n<ol class="refs">\n' + "\n".join(items) + "\n</ol>"


# --- Anthropic 테마: 제목 분리, 표지 도식(저장소 157개 = 점 157개, 분류별 색)
main_t, _, sub_t = title.partition(" — ")
GROUPS = [("A 메타·핵심", 17, "#d97757"), ("B 로보택시 E2E", 6, "#c6613f"), ("C ADAS·POV", 13, "#e0a43c"),
          ("D 미들웨어·GPU", 14, "#788c5d"), ("E 배포·안전", 6, "#4f7c6b"), ("F 레지스트리·인프라", 19, "#6a9bcc"),
          ("G 시뮬·평가", 19, "#8f7fb6"), ("H 차종·레퍼런스", 22, "#b79b78"), ("I 드라이버", 10, "#9c9a92"), ("J 레거시", 31, "#d6d3c9")]
cols, step, r = 23, 26, 9
dots, i = [], 0
for name, n, col in GROUPS:
    for _ in range(n):
        x, y = 22 + (i % cols) * step, 22 + (i // cols) * step
        dots.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>')
        i += 1
w, h = 22 * 2 + (cols - 1) * step, 22 * 2 + ((i - 1) // cols) * step
legend = "".join(f'<span><i style="background:{c}"></i>{html.escape(nm)} {n}</span>' for nm, n, c in GROUPS)
hero = (f'<div class="hero-art"><svg viewBox="0 0 {w} {h}" role="img" aria-label="autowarefoundation 저장소 157개를 분류별 색으로 나타낸 점 도식">'
        + "".join(dots) + f'</svg><div class="hero-legend">{legend}</div>'
        '<p class="hero-cap">점 1개 = 저장소 1개 · autowarefoundation 157개, 분류별 색 · 자체 작성</p></div>')

tpl = (ROOT / "scripts" / "templates" / f"{THEME}.html").read_text(encoding="utf-8")
page = tpl.replace("{{TITLE_MAIN}}", html.escape(main_t)).replace("{{TITLE_SUB}}", html.escape(sub_t)).replace("{{HERO}}", hero).replace("{{TITLE}}", html.escape(title)).replace("{{TOC}}", toc).replace("{{BODY}}", body).replace("{{REFS}}", refs_html)
(ROOT / OUT).write_text(page, encoding="utf-8")
used = {int(x) for x in re.findall(r'class="cite"[^>]*>(\d+)<', body)}
print(f"wrote {OUT} ({len(page):,} bytes); cited={len(used)}; missing={sorted(used - set(refs))}")
