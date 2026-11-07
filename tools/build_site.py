#!/usr/bin/env python3
"""Build the static HTML site from docs/.

Optional helper: the generated site/ output is committed, so readers
never need to run this. Requires only the Python standard library plus
the `markdown` package (pip install markdown).

Usage: python3 tools/build_site.py
"""

from pathlib import Path
import re

import markdown

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

# (label, url) shown in the shared header nav
NAV = [
    ("Home", "index.html"),
    ("Cheat sheet", "cheat-sheet.html"),
    ("Mistakes gallery", "common-mistakes.html"),
    ("Walkthrough 1", "walkthroughs/checkboxes-week-plan.html"),
    ("Walkthrough 2", "walkthroughs/table-gear-inventory.html"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Markdown for Everyone</title>
<meta name="description" content="Plain-English Markdown lessons for everyday life: notes, to-do lists, tables, and READMEs. No tracking, fully offline.">
<link rel="stylesheet" href="{css}">
</head>
<body>
<header class="site">
  <div class="wrap">
    <h1>Markdown for Everyone</h1>
    <p>Nine tiny lessons · a life skill · no tracking, fully offline</p>
    <nav aria-label="Site sections"><p>
    {navlinks}
    </p></nav>
  </div>
</header>
<main class="wrap">
<article>
"""

TAIL = """</article>
<nav class="pager">{pager}</nav>
</main>
<footer class="site">
  <div class="wrap">
    <p>Part of <a href="https://dylanasdale.github.io">Dylan Asdale's guides</a> ·
    markdown-for-everyone-guide · MIT licensed ·
    Copyright (c) 2026 Asdale Dynamics, LLC</p>
  </div>
</footer>
</body>
</html>
"""

PAGER_PREV = '<span>&larr; <a href="{url}">previous</a></span>'
PAGER_NEXT = '<span><a href="{url}">next</a> &rarr;</span>'


def rel_prefix(rel_target: Path) -> str:
    """'../' repeated for the depth of the output file (root = '')."""
    depth = len(rel_target.parent.parts)
    return "" if depth == 0 else "../" * depth


def nav_links(rel_target: Path) -> str:
    prefix = rel_prefix(rel_target)
    here = str(rel_target)
    parts = []
    for label, url in NAV:
        css = ' aria-current="page"' if url == here else ""
        parts.append(f'<a href="{prefix}{url}"{css}>{label}</a>')
    return " · ".join(parts)


def rewrite_md_links(html: str) -> str:
    # docs/README.md becomes the folder's index.html in the site…
    html = re.sub(r'href="([^"#]*?)README\.md(#?[^"]*)"', r'href="\1index.html\2"', html)
    # …and every other internal .md link points at its .html twin.
    return re.sub(r'href="([^"#]+?)\.md(#?[^"]*)"', r'href="\1.html\2"', html)


def task_checkboxes(html: str) -> str:
    """Turn <li>[ ] text</li> into real checkboxes, GitHub-style."""
    html = re.sub(
        r'<li>\[ \] ',
        '<li class="task-list-item">'
        '<input type="checkbox" disabled aria-label="open task"> ',
        html,
    )
    return re.sub(
        r'<li>\[[xX]\] ',
        '<li class="task-list-item">'
        '<input type="checkbox" disabled checked aria-label="done task"> ',
        html,
    )


def first_heading(html: str, fallback: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    inner = match.group(1) if match else fallback
    return re.sub(r"<[^>]+>", "", inner).strip()


PAGES = ["index.html", "cheat-sheet.html", "common-mistakes.html"]


def page_list() -> list:
    lessons = [f"lessons/{name[:-3]}.html" for name in LESSONS]
    return [PAGES[0]] + lessons + PAGES[1:]


def pager_links(rel_target: Path) -> str:
    pages = page_list()
    here = str(rel_target)
    if here not in pages:
        return ""
    idx = pages.index(here)
    prefix = rel_prefix(rel_target)
    left, right = "<span></span>", "<span></span>"
    if idx > 0:
        left = PAGER_PREV.format(url=prefix + pages[idx - 1])
    if idx + 1 < len(pages):
        right = PAGER_NEXT.format(url=prefix + pages[idx + 1])
    return f"{left}{right}"


def build_one(md_path: Path) -> Path:
    rel = md_path.relative_to(DOCS)
    if rel.name == "README.md":
        out_rel = Path(rel.parent) / "index.html"
    else:
        out_rel = rel.with_suffix(".html")
    out = SITE / out_rel
    out.parent.mkdir(parents=True, exist_ok=True)

    text = md_path.read_text(encoding="utf-8")
    html = markdown.markdown(text, extensions=MD_EXTENSIONS)
    html = task_checkboxes(html)
    html = rewrite_md_links(html)

    title = first_heading(html, out_rel.stem)
    page = (HEAD.format(title=title, css=rel_prefix(out_rel) + "style.css",
                        navlinks=nav_links(out_rel))
            + html + TAIL.format(pager=pager_links(out_rel)))
    out.write_text(page, encoding="utf-8")
    return out


LESSONS = [
    "01-what-is-markdown.md",
    "02-headings-and-paragraphs.md",
    "03-bold-italic-and-emphasis.md",
    "04-lists.md",
    "05-todo-checkboxes.md",
    "06-tables.md",
    "07-links-and-images.md",
    "08-quotes-code-and-extras.md",
    "09-real-life-documents.md",
]


def main() -> None:
    targets = [DOCS / "README.md"] + [DOCS / "lessons" / name for name in LESSONS]
    targets += [
        DOCS / "cheat-sheet.md",
        DOCS / "common-mistakes.md",
        DOCS / "walkthroughs" / "checkboxes-week-plan.md",
        DOCS / "walkthroughs" / "table-gear-inventory.md",
    ]
    for path in targets:
        out = build_one(path)
        print(f"built {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
