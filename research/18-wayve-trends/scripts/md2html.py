#!/usr/bin/env python3
# 사용: python3 -I scripts/md2html.py wayve-trends.md reference/references.md wayve-trends.html
# 의존: pip install markdown. 각주([^x])와 그림을 지원하며, 본문의 [n] 인용 번호를 references.md의 n번 URL로 연결한 자체 완결 HTML을 만든다.
"""Convert the report .md to self-contained HTML; numeric citation [n] becomes a link to source n's URL."""
import html
import pathlib
import re
import sys

import markdown

md_path = pathlib.Path(sys.argv[1])
ref_path = pathlib.Path(sys.argv[2])
out_path = pathlib.Path(sys.argv[3])

# --- references.md: "n. 등급 매체 — 제목 — 날짜 — URL"
refs = {}
for line in ref_path.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^(\d{1,3})\.\s+(.*)$", line)
    if not m:
        continue
    body = m.group(2)
    urls = re.findall(r"https?://[^\s)]+", body)
    title = re.sub(r"\s*—\s*https?://.*$", "", body).strip()
    refs[int(m.group(1))] = {"title": title, "url": urls[0] if urls else ""}


def link_num(n: int) -> str:
    r = refs.get(n)
    if not r:
        return f'<span class="cite missing" title="출처 목록에 없음">[{n}]</span>'
    t = html.escape(r["title"], quote=True)
    if not r["url"]:
        return f'<a class="cite" href="#src-{n}" title="{t}">[{n}]</a>'
    return f'<a class="cite" href="{html.escape(r["url"])}" target="_blank" rel="noopener" title="{t}">[{n}]</a>'


src = md_path.read_text(encoding="utf-8")

# 본문과 출처 목록 분리 — 출처 목록 안의 번호는 링크로 바꾸지 않는다.
parts = re.split(r"^## 출처\s*$", src, maxsplit=1, flags=re.M)
body_md, refs_md = parts[0], (parts[1] if len(parts) > 1 else "")

# [12] / [12][13] / [12, 13] 꼴 인용을 링크로
def repl(m: re.Match) -> str:
    nums = [int(x) for x in re.findall(r"\d+", m.group(0))]
    return "".join(link_num(n) for n in nums)

body_md = re.sub(r"(?<!\w)\[(\d{1,3}(?:\s*,\s*\d{1,3})*)\](?!\()", repl, body_md)

# GitHub식 2칸 하위 목록을 Python-Markdown이 읽는 4칸으로 보정
body_md = re.sub(r"^  (- |\d+\. )", r"    \1", body_md, flags=re.M)

md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists", "footnotes"], extension_configs={"toc": {"toc_depth": "2-3"}, "footnotes": {"BACKLINK_TEXT": "↩"}}, output_format="html5")
body_html = md.convert(body_md)

# 출처 목록은 번호 anchor를 붙여 별도 변환
ref_items = []
for line in refs_md.splitlines():
    m = re.match(r"^(\d{1,3})\.\s+(.*)$", line)
    if not m:
        continue
    n = int(m.group(1))
    txt = m.group(2)
    txt = re.sub(r"(https?://[^\s)]+)", lambda u: f'<a href="{html.escape(u.group(1))}" target="_blank" rel="noopener">{html.escape(u.group(1))}</a>', html.escape(txt))
    ref_items.append(f'<li id="src-{n}" value="{n}">{txt}</li>')
refs_html = "<h2>출처</h2>\n<ol class=\"refs\">\n" + "\n".join(ref_items) + "\n</ol>" if ref_items else ""

title_m = re.search(r"^#\s+(.+)$", src, flags=re.M)
title = title_m.group(1).strip() if title_m else md_path.stem

CSS = """
:root{--fg:#1f2328;--muted:#59636e;--line:#d1d9e0;--bg:#fff;--soft:#f6f8fa;--link:#0a5bd6;--mark:#fff6d5}
@media (prefers-color-scheme:dark){:root{--fg:#e6edf3;--muted:#9da7b3;--line:#3d444d;--bg:#0d1117;--soft:#161b22;--link:#6ea8fe;--mark:#3a3422}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",sans-serif}
main{max-width:980px;margin:0 auto;padding:32px 16px 80px}
h1{font-size:1.75rem;line-height:1.3;margin:0 0 16px;border-bottom:2px solid var(--line);padding-bottom:12px}
h2{font-size:1.35rem;margin:48px 0 12px;border-bottom:1px solid var(--line);padding-bottom:6px}
h3{font-size:1.1rem;margin:28px 0 8px}
p{margin:10px 0}
blockquote{margin:16px 0;padding:8px 16px;border-left:4px solid var(--line);background:var(--soft);color:var(--muted)}
blockquote p{margin:4px 0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.92rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:6px 10px;vertical-align:top;text-align:left}
th{background:var(--soft)}
tr:nth-child(even) td{background:color-mix(in srgb,var(--soft) 50%,transparent)}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
a.cite{font-size:.8em;vertical-align:super;line-height:0;padding:0 1px;background:var(--mark);border-radius:3px}
.cite.missing{color:#c00}
ol.refs{font-size:.88rem;padding-left:2.2em}
ol.refs li{margin:4px 0;word-break:break-all}
hr{border:0;border-top:1px solid var(--line);margin:32px 0}
code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:.9em}
.toc{background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:12px 20px;margin:20px 0;font-size:.92rem}
.toc ul{margin:4px 0;padding-left:1.2em}
img{max-width:100%;height:auto;display:block;margin:18px auto 6px;border:1px solid var(--line);border-radius:8px;background:#fff}
p:has(> img) + p > em:only-child, p > em:only-child{display:block;text-align:center;color:var(--muted);font-size:.88rem;font-style:normal}
.footnote{font-size:.88rem;color:var(--muted);border-top:1px solid var(--line);margin-top:32px}
sup a.footnote-ref{font-size:.75em;padding:0 2px;border-radius:3px;background:var(--soft);border:1px solid var(--line)}
ul ul{margin:2px 0}
li{margin:3px 0}
"""

out_html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<nav class="toc">{md.toc}</nav>
{body_html}
{refs_html}
</main>
</body>
</html>
"""
out_path.write_text(out_html, encoding="utf-8")
missing = sorted({int(x) for x in re.findall(r"\[(\d+)\]", body_md)} - set(refs))
print(f"wrote {out_path} ({out_path.stat().st_size:,} bytes); refs={len(refs)}; missing={missing}")
