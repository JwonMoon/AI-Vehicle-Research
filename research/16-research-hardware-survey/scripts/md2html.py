#!/usr/bin/env python3
# 사용: python3 -I scripts/md2html.py <report.md> <reference/references.md> <out.html> [title]
# 의존: pip install markdown. 본문의 [ID]와 출처 열의 ID를 references.md의 첫 URL로 연결한 자체 완결 HTML을 만든다.
"""Convert a report .md to self-contained HTML; citation IDs become links to the first URL in references.md."""
import re, sys, html, pathlib
import markdown

md_path = pathlib.Path(sys.argv[1]); ref_path = pathlib.Path(sys.argv[2]); out_path = pathlib.Path(sys.argv[3])
title_override = sys.argv[4] if len(sys.argv) > 4 else None

# --- parse references.md: | ID | title | URL(s) | date | grade |
refs = {}
for line in ref_path.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^\|\s*([JKNQXMSVOP]\d{1,2})\s*\|(.*)$", line)
    if not m: continue
    cells = [c.strip() for c in m.group(2).strip().strip("|").split("|")]
    if len(cells) < 3: continue
    title, urls_raw = cells[0], cells[1]
    urls = re.findall(r"https?://[^\s;)]+", urls_raw)
    refs[m.group(1)] = {"title": title, "urls": urls, "date": cells[2] if len(cells) > 2 else "", "grade": cells[3] if len(cells) > 3 else ""}

ID_RE = re.compile(r"\b([JKNQXMSVOP]\d{1,2})\b")
EMOJI = "🔍📄📰💬🏷️⚠️✅💡"

def link_id(i):
    r = refs.get(i)
    if not r or not r["urls"]:
        return f'<span class="cite missing" title="출처 목록에 없음">{i}</span>'
    t = html.escape(r["title"], quote=True)
    extra = ""
    if len(r["urls"]) > 1:
        extra = "".join(f'<a class="cite-more" href="{html.escape(u)}" target="_blank" rel="noopener" title="{t} (추가 링크 {k+2})">+</a>' for k, u in enumerate(r["urls"][1:]))
    return f'<a class="cite" href="{html.escape(r["urls"][0])}" target="_blank" rel="noopener" title="{t}">{i}</a>{extra}'

def cell_is_citation(cell):
    s = cell.strip()
    if not s: return False
    stripped = re.sub(r"[JKNQXMSVOP]\d{1,2}", "", s)
    stripped = re.sub(r"[\s·,/]", "", stripped)
    stripped = "".join(ch for ch in stripped if ch not in EMOJI and ch not in "️")
    return stripped == "" and ID_RE.search(s) is not None

def process_line(line):
    # bracketed citations anywhere
    line = re.sub(r"\[([JKNQXMSVOP]\d{1,2})\]", lambda m: "[" + link_id(m.group(1)) + "]", line)
    # table rows: citation-only cells
    if line.startswith("|") and not re.match(r"^\|\s*-{3,}", line):
        cells = line.split("|")
        for k, c in enumerate(cells):
            if cell_is_citation(c) and "<a " not in c:
                cells[k] = ID_RE.sub(lambda m: link_id(m.group(1)), c)
        line = "|".join(cells)
    return line

src = md_path.read_text(encoding="utf-8").splitlines()
body_md = "\n".join(process_line(l) for l in src)
# relative links to local md -> keep but make them open html siblings when exist
body_html = markdown.markdown(body_md, extensions=["tables", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3"}})
toc_html = getattr(markdown, "toc", "")
mdx = markdown.Markdown(extensions=["tables", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3"}})
body_html = mdx.convert(body_md); toc_html = mdx.toc

# references appendix
rows = []
for i, r in refs.items():
    links = " · ".join(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(re.sub(r"^https?://", "", u)[:70])}{"…" if len(u) > 77 else ""}</a>' for u in r["urls"])
    rows.append(f'<tr id="ref-{i}"><td class="refid">{i}</td><td>{html.escape(r["title"])}</td><td class="refurl">{links}</td><td>{html.escape(r["date"])}</td><td>{html.escape(r["grade"])}</td></tr>')
ref_html = '<h2 id="references">출처 목록</h2><p class="muted">ID를 클릭하면 새 탭에서 원문이 열립니다. 본문의 <span class="cite">ID</span> 링크도 같은 원문으로 연결됩니다.</p><table class="refs"><thead><tr><th>ID</th><th>제목</th><th>URL</th><th>날짜</th><th>등급</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table>"

title = title_override or next((l.lstrip("# ").strip() for l in src if l.startswith("# ")), md_path.stem)
CSS = """
:root{--bg:#fff;--fg:#1d2330;--muted:#5b6474;--line:#e3e7ee;--accent:#1f5fbf;--accent-bg:#eef4ff;--th:#f4f6fa;--code:#f1f3f7;--warn:#b7791f}
@media (prefers-color-scheme: dark){:root:not([data-theme=light]){--bg:#0f1319;--fg:#e6e9ef;--muted:#9aa4b5;--line:#2a3140;--accent:#8ab4ff;--accent-bg:#17233a;--th:#161c26;--code:#1a212c}}
:root[data-theme=dark]{--bg:#0f1319;--fg:#e6e9ef;--muted:#9aa4b5;--line:#2a3140;--accent:#8ab4ff;--accent-bg:#17233a;--th:#161c26;--code:#1a212c}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.65 -apple-system,"Apple SD Gothic Neo","Noto Sans KR",Segoe UI,Roboto,sans-serif}
.wrap{display:grid;grid-template-columns:260px minmax(0,1fr);gap:32px;max-width:1500px;margin:0 auto;padding:24px 16px}
nav.toc{position:sticky;top:16px;align-self:start;max-height:calc(100vh - 32px);overflow:auto;font-size:13px;border-right:1px solid var(--line);padding-right:12px}
nav.toc ul{list-style:none;padding-left:0;margin:0}nav.toc ul ul{padding-left:12px}nav.toc a{color:var(--muted);text-decoration:none;display:block;padding:3px 0}nav.toc a:hover{color:var(--accent)}
main{min-width:0}h1{font-size:1.6em;line-height:1.3;margin:.2em 0 .6em}h2{font-size:1.3em;margin-top:2em;padding-top:.5em;border-top:2px solid var(--line)}h3{font-size:1.08em;margin-top:1.6em}
blockquote{margin:1em 0;padding:.6em 1em;border-left:4px solid var(--accent);background:var(--accent-bg);font-size:.94em}blockquote p{margin:.3em 0}
table{border-collapse:collapse;width:100%;font-size:.88em;margin:.8em 0;display:block;overflow-x:auto}th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}th{background:var(--th);position:sticky;top:0}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.92em}a{color:var(--accent)}
a.cite{display:inline-block;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.85em;font-weight:600;background:var(--accent-bg);border:1px solid var(--line);border-radius:4px;padding:0 5px;text-decoration:none;margin:0 1px}a.cite:hover{border-color:var(--accent)}
a.cite-more{font-size:.75em;text-decoration:none;margin-right:2px;color:var(--muted)}span.cite.missing{color:var(--warn);font-family:ui-monospace,monospace;font-size:.85em}
table.refs td.refid{font-family:ui-monospace,monospace;font-weight:600;white-space:nowrap}table.refs td.refurl a{display:block;word-break:break-all;font-size:.9em}
.muted{color:var(--muted);font-size:.9em}.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:.85em;color:var(--muted);margin-bottom:8px}button.theme{background:none;border:1px solid var(--line);color:var(--fg);border-radius:6px;padding:4px 10px;cursor:pointer}
@media (max-width:900px){.wrap{grid-template-columns:1fr;padding:16px}nav.toc{position:static;border-right:0;max-height:none;border-bottom:1px solid var(--line);padding-bottom:12px}}
"""
JS = """
(function(){var b=document.getElementById('theme');function cur(){return document.documentElement.getAttribute('data-theme')||'auto'}b.onclick=function(){var c=cur();var n=c==='dark'?'light':c==='light'?'auto':'dark';if(n==='auto'){document.documentElement.removeAttribute('data-theme')}else{document.documentElement.setAttribute('data-theme',n)}b.textContent='테마: '+n;try{localStorage.setItem('theme',n)}catch(e){}};try{var s=localStorage.getItem('theme');if(s&&s!=='auto'){document.documentElement.setAttribute('data-theme',s)}b.textContent='테마: '+(s||'auto')}catch(e){}
var hs=[].slice.call(document.querySelectorAll('main h2[id],main h3[id]'));var links=[].slice.call(document.querySelectorAll('nav.toc a'));function spy(){var y=window.scrollY+80;var a=hs[0];hs.forEach(function(h){if(h.offsetTop<=y)a=h});links.forEach(function(l){l.style.color=(a&&l.getAttribute('href')==='#'+a.id)?'var(--accent)':''})}window.addEventListener('scroll',spy);spy()})();
"""
out = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><div class="wrap"><nav class="toc"><div class="topbar"><span>목차</span><button class="theme" id="theme">테마: auto</button></div>{toc_html}<p><a href="#references">출처 목록 ({len(refs)}건)</a></p></nav>
<main>{body_html}{ref_html}<p class="muted">Markdown 원본: {html.escape(md_path.name)} · 출처: {html.escape(ref_path.name)} · 생성: 2026-10-15</p></main></div><script>{JS}</script></body></html>"""
out_path.write_text(out, encoding="utf-8")
missing = sorted(set(ID_RE.findall(body_md)) - set(refs))
print(f"wrote {out_path} ({len(out)//1024} KB); refs={len(refs)}; unresolved IDs in body: {missing}")
