#!/usr/bin/env python3
"""Verify the markdown-for-everyone-guide repository.

Checks (all pass silently, exits non-zero on failure):
  1. Every expected docs/ and site/ file exists.
  2. Every Markdown source in docs/ renders without error.
  3. Every internal link in docs/*.md resolves to a real file or
     a heading that exists in the target file (when a #fragment is used).
  4. Every internal <a href> and asset link in site/*.html resolves.
  5. Site pages parse as HTML and contain no external requests
     (no analytics, no webfonts, nothing fetched from the network).
  6. No obvious secrets (API keys, etc.) in any tracked text file.
"""

from pathlib import Path
from html.parser import HTMLParser
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_DOCS = [
    "docs/README.md",
    "docs/cheat-sheet.md",
    "docs/common-mistakes.md",
    *[f"docs/lessons/{n}" for n in [
        "01-what-is-markdown.md",
        "02-headings-and-paragraphs.md",
        "03-bold-italic-and-emphasis.md",
        "04-lists.md",
        "05-todo-checkboxes.md",
        "06-tables.md",
        "07-links-and-images.md",
        "08-quotes-code-and-extras.md",
        "09-real-life-documents.md",
    ]],
    *[f"docs/walkthroughs/{n}" for n in [
        "checkboxes-week-plan.md",
        "table-gear-inventory.md",
    ]],
]

EXPECTED_SITE = [
    "site/index.html",
    "site/style.css",
    "site/cheat-sheet.html",
    "site/common-mistakes.html",
    *[f"site/lessons/{n}" for n in [
        "01-what-is-markdown.html",
        "02-headings-and-paragraphs.html",
        "03-bold-italic-and-emphasis.html",
        "04-lists.html",
        "05-todo-checkboxes.html",
        "06-tables.html",
        "07-links-and-images.html",
        "08-quotes-code-and-extras.html",
        "09-real-life-documents.html",
    ]],
    *[f"site/walkthroughs/{n}" for n in [
        "checkboxes-week-plan.html",
        "table-gear-inventory.html",
    ]],
]

problems = []


def fail(msg):
    problems.append(msg)


# --- 1. Expected files ---------------------------------------------------
for rel in EXPECTED_DOCS + EXPECTED_SITE + ["README.md", "LICENSE"]:
    if not (ROOT / rel).is_file():
        fail(f"missing expected file: {rel}")

# --- 2. Markdown rendering ------------------------------------------------
try:
    import markdown
except ImportError:
    markdown = None

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

if markdown is None:
    fail("python-markdown not installed; cannot render-verify docs")
else:
    for rel in EXPECTED_DOCS:
        src = (ROOT / rel).read_text(encoding="utf-8")
        try:
            markdown.markdown(src, extensions=MD_EXTENSIONS)
        except Exception as exc:  # noqa: BLE001
            fail(f"{rel}: markdown rendering failed: {exc}")


# --- 3. Internal links in markdown ----------------------------------------
def strip_code_blocks(text):
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
    return re.sub(r"`[^`]*`", "", text)


def headings_in(path):
    headings = set()
    text = strip_code_blocks(path.read_text(encoding="utf-8"))
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w\- ]", "", match.group(2).lower())
            headings.add(slug.replace(" ", "-"))
    return headings


def resolve_link(source: Path, target: str):
    if re.match(r"^[a-z]+:", target) and not target.startswith("mailto:"):
        if target.startswith("http"):
            return None  # external URL, allowed
        return f"unusual url scheme in {target}"
    target_path, _, fragment = target.partition("#")
    if target_path == "":
        doc_path = source.with_suffix(".md") if source.suffix == ".md" else source
    else:
        doc_path = (source.parent / target_path).resolve()
        if not doc_path.is_file():
            return f"target not found: {target} (from {source.relative_to(ROOT)})"
    if fragment and fragment not in headings_in(doc_path):
        return f"missing heading #{fragment} in {target} (from {source.relative_to(ROOT)})"
    return None


# Links that are deliberately broken: they exist only as examples
# inside the mistakes gallery.
INTENTIONALLY_MISSING = {"notes.md"}

for rel in EXPECTED_DOCS:
    path = ROOT / rel
    text = strip_code_blocks(path.read_text(encoding="utf-8"))
    for match in re.finditer(r"\[[^\]]+\]\(([^)\s]+)\)", text):
        url = match.group(1)
        if url.lstrip("./") in INTENTIONALLY_MISSING:
            continue
        result = resolve_link(path, url)
        if result:
            fail(result)


# --- 4/5. HTML pages: parse, links, no external requests -------------------
class Auditor(HTMLParser):
    EXTERNAL = re.compile(r"^(https?:)?//|^[a-z]+:")

    def __init__(self, page_path, site_root):
        super().__init__()
        self.page_path = page_path
        self.site_root = site_root
        self.hrefs = []
        self.external = []
        self.tags = []
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        d = dict(attrs)
        href = d.get("href")
        if href:
            if self.EXTERNAL.match(href):
                if "dylanasdale.github.io" in href:
                    self.external.append(href)  # allowed: attribution link
                elif not href.startswith("mailto:"):
                    self.external.append(href)
            else:
                self.hrefs.append(href)
        src = d.get("src")
        if src and self.EXTERNAL.match(src):
            self.external.append(src)

    def handle_endtag(self, tag):
        pass


VOID_TAGS = {"meta", "link", "br", "hr", "img", "input", "wbr", "source"}

ALLOWED_EXTERNAL_HOSTS = ("dylanasdale.github.io",)


def audit_html(rel):
    path = ROOT / rel
    raw = path.read_text(encoding="utf-8")

    parser = Auditor(path, ROOT / "site")
    try:
        parser.feed(raw)
        parser.close()
    except Exception as exc:  # noqa: BLE001
        fail(f"{rel}: HTML parse error: {exc}")
        return

    for href in parser.hrefs:
        target, _, fragment = href.partition("#")
        if target == "":
            continue  # same-page anchor
        resolved = (path.parent / target).resolve()
        if not resolved.is_file():
            fail(f"{rel}: broken link {href}")
        elif fragment and resolved.suffix == ".html":
            text = resolved.read_text(encoding="utf-8")
            anchor = re.search(
                r'id=["\']' + re.escape(fragment) + r'["\']', text)
            if not anchor:
                fail(f"{rel}: missing anchor #{fragment} in {target}")

    for ext in parser.external:
        host_ok = any(h in ext for h in ALLOWED_EXTERNAL_HOSTS)
        if not host_ok:
            fail(f"{rel}: disallowed external request: {ext}")


# Basic well-formedness: tags balance for non-void tags


def check_tag_balance(rel):
    text = (ROOT / rel).read_text(encoding="utf-8")
    stack = []
    for match in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)([^>]*?)(/?)>", text):
        closing, tag, _, selfclose = match.groups()
        tag = tag.lower()
        if tag in VOID_TAGS or selfclose:
            continue
        if closing:
            if not stack or stack[-1] != tag:
                fail(f"{rel}: unbalanced </{tag}> (open stack: {stack[-3:]})")
                return
            stack.pop()
        else:
            stack.append(tag)
    if stack:
        fail(f"{rel}: unclosed tags: {stack}")


for rel in EXPECTED_SITE:
    if rel.endswith(".html"):
        audit_html(rel)
        check_tag_balance(rel)

# --- 6. Secrets scan -------------------------------------------------------
SECRET_PATTERNS = [
    re.compile(r"(?i)\b(api[_-]?key|secret|password|passwd|token)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]
SKIP_DIRS = {".git", ".opencode", "__pycache__"}
for text_file in ROOT.rglob("*"):
    if not text_file.is_file():
        continue
    if any(part in SKIP_DIRS for part in text_file.parts):
        continue
    if text_file.suffix not in {".md", ".html", ".css", ".py", ".txt", ".license", ""}:
        continue
    body = text_file.read_text(encoding="utf-8", errors="ignore")
    for pattern in SECRET_PATTERNS:
        if pattern.search(body):
            fail(f"possible secret in {text_file.relative_to(ROOT)}")

# --- LICENSE copyright line ------------------------------------------------
license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
required = "Copyright (c) 2026 Asdale Dynamics, LLC"
if required not in license_text:
    fail(f"LICENSE missing exact line: {required}")

readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
if "Asdale Dynamics, LLC" not in readme_text:
    fail("README does not credit Asdale Dynamics, LLC")

# --- Report ----------------------------------------------------------------
if problems:
    print(f"FAILED — {len(problems)} problem(s):")
    for problem in problems:
        print(f"  - {problem}")
    sys.exit(1)
count = len(EXPECTED_DOCS) + len(EXPECTED_SITE)
print(f"OK — {count} files checked: links resolve, pages parse, "
      "rendering clean, no external requests, no secrets.")
