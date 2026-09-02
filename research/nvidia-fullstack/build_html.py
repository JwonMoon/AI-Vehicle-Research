#!/usr/bin/env python3
"""md → 통합 HTML 보고서 빌드 스크립트.

사용법:  python3 build_html.py        (이 폴더에서 실행)
입력:    03-autonomous-driving-stack.md, 07-physical-ai-cosmos.md, appendix-a-tier1-workscope.md
출력:    report.html  (외부 JS/CSS 없음, 이미지는 images/ 상대경로)
의존:    pip install markdown  (python-markdown ≥ 3.4)

md 파일이 원본이다. 내용을 고치면 md를 고치고 이 스크립트를 다시 실행한다.
"""
import html
import re
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

HERE = Path(__file__).parent
CHAPTERS = [
    ("c3", "03-autonomous-driving-stack.md", "3장", "자율주행 스택"),
    ("c7", "07-physical-ai-cosmos.md", "7장", "Physical AI / Cosmos"),
    ("ca", "appendix-a-tier1-workscope.md", "부록 A", "Tier-1 관점 작업 범위"),
]
OUT = HERE / "report.html"

GRADES = {
    "✅": ("g-ok", "두 출처 교차검증"),
    "🔍": ("g-src", "1차 출처 원문 확인(GitHub 등)"),
    "📄": ("g-sec", "검색 요약·2차 출처만"),
    "⚠️": ("g-warn", "미확인·추정"),
}


def md_to_html(text: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "footnotes", "toc", "attr_list", "md_in_html", "sane_lists"],
        extension_configs={
            "toc": {"slugify": slugify_unicode, "toc_depth": "2-4"},
            "footnotes": {"BACKLINK_TEXT": "↩", "BACKLINK_TITLE": "본문으로"},
        },
    )
    return md.convert(text)


def split_front(text: str):
    """H1 제목을 떼고 나머지(상단 메타 blockquote 포함)를 본문으로 돌려준다.
    메타 블록을 본문과 함께 변환해야 그 안의 각주 참조가 용어집과 연결된다."""
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip()
    return title, "\n".join(lines[1:])


def meta_from_first_blockquote(h: str) -> str:
    """본문 첫 blockquote(작성일·범위·등급 범례)를 .meta 박스로 바꾼다."""
    m = re.search(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>", h, flags=re.S)
    if not m:
        return h
    items = [x.strip() for x in m.group(1).split("\n") if x.strip()]
    box = '<div class="meta">' + "".join(f"<div>{x}</div>" for x in items) + "</div>"
    return h[:m.start()] + box + h[m.end():]


def badge_grades(h: str) -> str:
    for emo, (cls, tip) in GRADES.items():
        h = h.replace(emo, f'<span class="g {cls}" title="{tip}">{emo}</span>')
    return h


def cards_from_tables(h: str) -> str:
    """'전체 그림 속 위치' 4행 표 → 카드 그리드."""
    CARD_KEYS = {"전체 그림 속 위치", "담당 역할", "현재 위치", "현재 위치(성숙도)", "다음 이정표"}

    def repl(m):
        tbl = m.group(0)
        rows = re.findall(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>", tbl, flags=re.S)
        if not rows or not all(re.sub(r"<[^>]+>", "", k).strip() in CARD_KEYS for k, _ in rows):
            return tbl
        cards = "".join(
            f'<div class="card"><div class="card-k">{k}</div><div class="card-v">{v}</div></div>'
            for k, v in rows
        )
        return f'<div class="card-grid">{cards}</div>'
    return re.sub(r"<table>.*?</table>", repl, h, flags=re.S)


def wrap_tables(h: str) -> str:
    return re.sub(r"<table>", '<div class="tbl"><table>', h).replace("</table>", "</table></div>")


def keyfacts(h: str) -> str:
    return re.sub(
        r"(<h3[^>]*>[^<]*핵심 사실[^<]*</h3>)\s*<ol>",
        r'\1<ol class="keyfacts">',
        h,
    )


def cite_chips(h: str) -> str:
    # ( <a>…</a>[, <a>…</a>]* ) → 칩 묶음
    pat = re.compile(r"\((\s*(?:<a href=\"[^\"]+\">[^<]+</a>\s*(?:,|·)?\s*)+)\)")
    def repl(m):
        inner = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'<a class="cite" href="\1" target="_blank" rel="noopener">\2</a>', m.group(1))
        inner = re.sub(r"\s*(,|·)\s*", "", inner)
        return f'<span class="cites">{inner}</span>'
    return pat.sub(repl, h)


def figures(h: str) -> str:
    pat = re.compile(r"<p><img ([^>]*?)/?></p>\s*<p><em>(.*?)</em></p>", flags=re.S)
    def repl(m):
        attrs, cap = m.group(1), m.group(2)
        src = re.search(r'src="([^"]+)"', attrs).group(1)
        return (f'<figure><a href="{src}" target="_blank" rel="noopener"><img {attrs} loading="lazy"></a>'
                f"<figcaption>{cap}</figcaption></figure>")
    return pat.sub(repl, h)


def prefix_ids(h: str, pfx: str) -> str:
    h = h.replace('id="fn:', f'id="{pfx}-fn-').replace('href="#fn:', f'href="#{pfx}-fn-')
    h = h.replace('id="fnref:', f'id="{pfx}-fnref-').replace('href="#fnref:', f'href="#{pfx}-fnref-')
    h = re.sub(r'<(h[2-4]) id="([^"]+)"', lambda m: f'<{m.group(1)} id="{pfx}-{m.group(2)}"', h)
    return h


def footnote_tooltips(h: str) -> str:
    notes = {}
    for m in re.finditer(r'<li id="([^"]+)">\s*<p>(.*?)<a class="footnote-backref"', h, flags=re.S):
        txt = re.sub(r"<[^>]+>", "", m.group(2)).replace("&#160;", " ").strip()
        notes[m.group(1)] = html.escape(txt[:300])
    def repl(m):
        target = m.group(1)
        tip = notes.get(target, "")
        return f'<sup id="{m.group(2)}"><a class="footnote-ref" href="#{target}" title="{tip}">{m.group(3)}</a></sup>'
    h = re.sub(r'<sup id="([^"]+)"><a class="footnote-ref" href="#([^"]+)">([^<]+)</a></sup>',
               lambda m: repl(type("M", (), {"group": lambda s, i, m=m: {1: m.group(2), 2: m.group(1), 3: m.group(3)}[i]})()),
               h)
    h = h.replace('<div class="footnote">', '<div class="footnote glossary"><h3>용어집</h3>')
    return h


def headings(h: str):
    return [(int(t), i, re.sub(r"<[^>]+>", "", txt).strip())
            for t, i, txt in re.findall(r'<h([23]) id="([^"]+)">(.*?)</h[23]>', h, flags=re.S)]


def build():
    chapters = []
    for pfx, fname, label, short in CHAPTERS:
        title, body = split_front((HERE / fname).read_text(encoding="utf-8"))
        h = md_to_html(body)
        h = prefix_ids(h, pfx)
        h = meta_from_first_blockquote(h)
        h = cards_from_tables(h)
        h = figures(h)
        h = cite_chips(h)
        h = badge_grades(h)
        h = keyfacts(h)
        h = wrap_tables(h)
        h = footnote_tooltips(h)
        h = re.sub(r"<hr\s*/?>", '<hr class="sep">', h)
        chapters.append(dict(pfx=pfx, label=label, short=short, title=title,
                             html=h, heads=headings(h), src=fname))

    # sidebar
    nav = []
    for c in chapters:
        nav.append(f'<div class="nav-ch"><a href="#{c["pfx"]}">{c["label"]} · {c["short"]}</a></div>')
        for lvl, hid, txt in c["heads"]:
            nav.append(f'<a class="nav-h{lvl}" href="#{hid}">{txt}</a>')
    nav_html = "\n".join(nav)

    legend = "".join(f'<span class="g {cls}">{emo}</span> {tip}' + (" · " if i < 3 else "")
                     for i, (emo, (cls, tip)) in enumerate(GRADES.items()))

    ch_cards = "".join(
        f'<a class="chcard" href="#{c["pfx"]}"><div class="chcard-l">{c["label"]}</div>'
        f'<div class="chcard-t">{c["short"]}</div><div class="chcard-s">{c["title"].split("—")[-1].strip()}</div></a>'
        for c in chapters)

    sections = ""
    for c in chapters:
        sections += (f'<section class="chapter" id="{c["pfx"]}">'
                     f'<div class="ch-head"><div class="ch-label">{c["label"]}</div><h1>{c["title"]}</h1></div>'
                     f'{c["html"]}'
                     f'<p class="src-note">원본: <code>{c["src"]}</code></p></section>')

    page = TEMPLATE.replace("{{NAV}}", nav_html).replace("{{LEGEND}}", legend) \
        .replace("{{CHCARDS}}", ch_cards).replace("{{SECTIONS}}", sections)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB), headings={sum(len(c['heads']) for c in chapters)}")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NVIDIA 차량용 풀스택 SW 조사 — 3장 자율주행 스택 · 7장 Physical AI/Cosmos · 부록 A Tier-1 관점</title>
<style>
:root{
  --bg:#f6f7f5; --paper:#ffffff; --ink:#1f2421; --muted:#5f6b63; --line:#dfe4df;
  --accent:#76b900; --accent-ink:#3f6a00; --accent-soft:#eef7dd;
  --ok:#2e7d32; --ok-bg:#e6f4ea; --src:#1565c0; --src-bg:#e3f0fc; --sec:#8d6e00; --sec-bg:#fff6d6; --warn:#c62828; --warn-bg:#fde8e8;
  --card:#fbfcfa; --sidebar-w:290px;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#141715; --paper:#1c201d; --ink:#e7ebe6; --muted:#9aa59d; --line:#2e352f;
    --accent:#8fd400; --accent-ink:#b9ea4c; --accent-soft:#233016;
    --ok:#7ad38a; --ok-bg:#1c3021; --src:#8ab8ff; --src-bg:#1a2a44; --sec:#e6c35a; --sec-bg:#3a3110; --warn:#ff8a80; --warn-bg:#3d1c1c; --card:#20251f; }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans KR","Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15.5px;line-height:1.7;word-break:keep-all}
a{color:var(--src);text-decoration:none}
a:hover{text-decoration:underline}
code{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.88em;background:var(--accent-soft);padding:.05em .35em;border-radius:4px}

/* layout */
.layout{display:grid;grid-template-columns:var(--sidebar-w) minmax(0,1fr)}
nav.side{position:sticky;top:0;height:100vh;overflow-y:auto;border-right:1px solid var(--line);background:var(--paper);padding:18px 14px 40px;font-size:13px}
nav.side .brand{font-weight:700;color:var(--accent-ink);margin-bottom:10px;font-size:14px}
nav.side .nav-ch{margin:14px 0 4px;font-weight:700;border-top:1px solid var(--line);padding-top:10px}
nav.side .nav-ch a{color:var(--ink)}
nav.side a.nav-h2{display:block;padding:3px 6px;border-radius:5px;color:var(--ink);font-weight:600}
nav.side a.nav-h3{display:block;padding:2px 6px 2px 18px;border-radius:5px;color:var(--muted);font-size:12.5px}
nav.side a.active{background:var(--accent-soft);color:var(--accent-ink)}
nav.side .legend{margin-top:18px;padding-top:10px;border-top:1px solid var(--line);color:var(--muted);font-size:12px;line-height:1.9}
main{padding:0 0 80px}
.wrap{max-width:62rem;margin:0 auto;padding:0 36px}
@media (max-width:1100px){ .layout{grid-template-columns:1fr} nav.side{display:none} .wrap{padding:0 18px} }

/* hero */
.hero{background:linear-gradient(135deg,#0f1a05 0%,#243c07 55%,#3f6a00 100%);color:#f2f7ea;padding:56px 0 40px;margin-bottom:28px}
.hero h1{font-size:30px;margin:0 0 8px;line-height:1.3}
.hero .sub{color:#c9dfa6;font-size:15px;margin-bottom:22px}
.hero .facts{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13.5px;color:#dbe8c4}
.hero .facts b{color:#fff}
.hero .legend{margin-top:16px;font-size:13px;color:#e4efd0}
.hero .legend .g{background:rgba(255,255,255,.14);color:#fff}
.chcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:22px}
.chcard{display:block;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:10px;padding:14px 16px;color:#fff}
.chcard:hover{background:rgba(255,255,255,.16);text-decoration:none}
.chcard-l{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#c9dfa6}
.chcard-t{font-size:18px;font-weight:700;margin:2px 0}
.chcard-s{font-size:12.5px;color:#dbe8c4}
.constraint{background:var(--sec-bg);border-left:4px solid var(--sec);padding:12px 16px;border-radius:6px;font-size:14px;margin:0 0 30px}

/* chapters */
section.chapter{margin-top:48px}
.ch-head{border-bottom:3px solid var(--accent);padding-bottom:10px;margin-bottom:16px}
.ch-label{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);font-weight:700}
section.chapter h1{font-size:27px;margin:2px 0 0;line-height:1.3}
h2{font-size:21px;margin:44px 0 12px;padding-top:8px;scroll-margin-top:16px;color:var(--ink)}
h2::before{content:"";display:inline-block;width:10px;height:10px;background:var(--accent);border-radius:2px;margin-right:10px;vertical-align:baseline}
h3{font-size:17px;margin:30px 0 8px;scroll-margin-top:16px}
h4{font-size:15px;margin:22px 0 6px;color:var(--muted)}
p{margin:.55em 0}
ul,ol{padding-left:1.4em}
li{margin:.25em 0}
hr.sep{border:0;border-top:1px dashed var(--line);margin:34px 0}
strong{font-weight:700}

.meta{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px 16px;font-size:13.5px;color:var(--muted);margin-bottom:22px}
.meta > div{margin:3px 0}
.meta strong{color:var(--ink)}

/* badges */
.g{display:inline-block;font-size:.8em;line-height:1;padding:.18em .32em;border-radius:5px;vertical-align:.1em;margin:0 .05em}
.g-ok{background:var(--ok-bg);color:var(--ok)} .g-src{background:var(--src-bg);color:var(--src)} .g-sec{background:var(--sec-bg);color:var(--sec)} .g-warn{background:var(--warn-bg);color:var(--warn)}

/* cites */
.cites{display:inline-flex;flex-wrap:wrap;gap:3px;vertical-align:baseline;margin:0 .15em}
a.cite{display:inline-block;font-size:.76em;line-height:1.35;padding:.05em .45em;border:1px solid var(--line);border-radius:999px;background:var(--paper);color:var(--src);white-space:nowrap;max-width:22em;overflow:hidden;text-overflow:ellipsis;vertical-align:middle}
a.cite:hover{border-color:var(--src);text-decoration:none}

/* cards */
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin:14px 0 18px}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:10px 12px;font-size:14px}
.card-k{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-ink);font-weight:700;margin-bottom:4px}
.card-v{line-height:1.6}

/* key facts */
ol.keyfacts{list-style:none;padding:0;counter-reset:kf;display:grid;gap:8px;margin:12px 0 18px}
ol.keyfacts>li{counter-increment:kf;background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:10px 14px 10px 46px;position:relative;font-size:14.5px}
ol.keyfacts>li::before{content:counter(kf);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--accent);color:#0f1a05;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}

/* tables */
.tbl{overflow-x:auto;margin:14px 0 20px;border:1px solid var(--line);border-radius:8px;background:var(--paper)}
table{border-collapse:collapse;width:100%;font-size:13.5px;line-height:1.55}
th{position:sticky;top:0;background:var(--accent-soft);color:var(--accent-ink);text-align:left;padding:8px 10px;border-bottom:2px solid var(--accent);white-space:nowrap}
td{padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top;min-width:6em}
tr:nth-child(even) td{background:rgba(118,185,0,.04)}
td:first-child{font-weight:600}

/* figures */
figure{margin:20px 0;text-align:center}
figure img{max-width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff}
figcaption{font-size:12.5px;color:var(--muted);margin-top:6px;text-align:left}

/* glossary */
.glossary{margin-top:34px;padding:14px 18px;background:var(--paper);border:1px solid var(--line);border-radius:10px;font-size:13.5px}
.glossary h3{margin:0 0 8px;font-size:15px}
.glossary hr{display:none}
.glossary ol{padding-left:1.6em}
sup a.footnote-ref{background:var(--accent-soft);color:var(--accent-ink);padding:0 .35em;border-radius:4px;font-weight:700;font-size:.75em}
a.footnote-backref{margin-left:.4em;color:var(--muted)}
.src-note{color:var(--muted);font-size:12.5px;margin-top:30px}

blockquote{margin:12px 0;padding:8px 14px;border-left:4px solid var(--accent);background:var(--accent-soft);border-radius:4px}

@media print{
  nav.side{display:none} .layout{display:block} .hero{background:#243c07;-webkit-print-color-adjust:exact}
  section.chapter{page-break-before:always} a.cite{border:none;padding:0} .tbl{overflow:visible;border:none}
}
</style>
</head>
<body>
<div class="layout">
<nav class="side" id="side">
  <div class="brand">NVIDIA 풀스택 SW 조사</div>
  <a class="nav-h2" href="#top">개요</a>
  {{NAV}}
  <div class="legend">검증 등급<br>{{LEGEND}}</div>
</nav>
<main>
  <div class="hero" id="top"><div class="wrap">
    <h1>NVIDIA 차량용 풀스택 소프트웨어 조사</h1>
    <div class="sub">3장 자율주행 스택 · 7장 Physical AI / Cosmos · 부록 A Tier-1 관점 작업 범위</div>
    <div class="facts"><span><b>작성일</b> 2026-09-02</span><span><b>형식</b> md 원본의 HTML 통합본 (build_html.py로 생성)</span><span><b>범위</b> 팀 합의 7장 목차 중 3장·7장 담당분 + 부록</span></div>
    <div class="legend">검증 등급 &nbsp; {{LEGEND}}</div>
    <div class="chcards">{{CHCARDS}}</div>
  </div></div>
  <div class="wrap">
    <div class="constraint"><b>조사 제약(2026-09-02)</b> 조사 세션의 네트워크 정책으로 nvidia.com·arxiv.org·huggingface.co·주요 언론사 원문에 직접 접근할 수 없었다. NVIDIA 공식 페이지·논문 인용은 검색 엔진 요약(📄)에 의존하며, GitHub 저장소(README·코드·LICENSE)만 원문(🔍)으로 확인했다. 📄 항목은 후속 세션에서 원문 재확인이 필요하다. 출처 전체 목록은 <a href="reference/references.md">reference/references.md</a>, 이미지 출처는 <a href="reference/images.md">reference/images.md</a>.</div>
    {{SECTIONS}}
  </div>
</main>
</div>
<script>
(function(){
  var links=[].slice.call(document.querySelectorAll('nav.side a[href^="#"]'));
  var map={}; links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
  var targets=Object.keys(map).map(function(id){return document.getElementById(id);}).filter(Boolean);
  var current=null;
  function setActive(id){ if(current===id) return; links.forEach(function(a){a.classList.remove('active');}); var a=map[id]; if(a){a.classList.add('active'); var r=a.getBoundingClientRect(), n=document.getElementById('side').getBoundingClientRect(); if(r.top<n.top+40||r.bottom>n.bottom-40){a.scrollIntoView({block:'center'});}} current=id; }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting) setActive(e.target.id); }); },{rootMargin:'0px 0px -75% 0px',threshold:0});
    targets.forEach(function(t){io.observe(t);});
  }
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
