# STATUS.md — markdown-for-everyone-guide

Last updated: 2026-11-07 · Recommended reading order of this file:
What was built → How to run/verify → Verification results → Known gaps.

## What was built

A plain-English manual teaching **Markdown as a life skill** — notes,
to-do lists, resumes, READMEs, and simple docs — tailored for absolute
beginners and consistent with Asdale Dynamics, LLC's "explain it like a
friend would" style.

**Content (docs/):**

- **Nine tiny lessons** (`docs/lessons/01`–`09`): what Markdown is, headings
  & paragraphs, emphasis, lists, to-do checkboxes, tables, links & images,
  quotes/code/extras, and real-life documents (weekly plan, resume draft,
  README, FAQ). Every lesson ends with a 3-item "Try it now" practice list.
- **Two hands-on walkthroughs** (`docs/walkthroughs/`):
  1. `checkboxes-week-plan.md` — build a weekly to-do plan step by step.
  2. `table-gear-inventory.md` — build a small-business gear-inventory
     table and wrap it in a README (resale-business flavored).
- **Printable one-page cheat sheet** (`docs/cheat-sheet.md`).
- **Common-mistakes gallery** (`docs/common-mistakes.md`) — ten real
  rendering traps (missing space after `#`, spaced bold, mismatched table
  pipes, swallowed line breaks, wrong nesting indent, unclosed fences,
  broken relative links, bad checkbox flavor, plus the glued-list and
  list-break pitfalls), each with symptom + one-move fix, ending in a
  five-second debug checklist.
- **Guide index** (`docs/README.md`) tying it all together.

**Static HTML site (site/):** all of the above as committed standalone
HTML — `site/index.html` plus one page per lesson, cheat sheet, mistakes
gallery, and walkthroughs, with a shared `style.css`. No build step, no
JavaScript, no tracking, no external requests (fully offline), no
analytics. Learners can read either the Markdown docs or the site.

**Tooling:**

- `tools/build_site.py` — optional regenerator for `site/` from `docs/`
  (requires the `markdown` pip package; the built HTML is committed, so
  running it is never required).
- `scripts/verify.py` — dependency-light correctness checks (details below).

**Also included:** `README.md` (project overview, credits to
Asdale Dynamics, LLC) and MIT `LICENSE` with the exact line
`Copyright (c) 2026 Asdale Dynamics, LLC`.

## How to run it

- **Read the guide (Markdown):** open `docs/README.md` — renders on GitHub,
  in VS Code preview, Obsidian, or any Markdown viewer.
- **Read the guide (site):** open `site/index.html` in any browser.
  No server needed; double-click the file.
- **Regenerate the site (optional):**
  `pip install markdown && python3 tools/build_site.py`
- **Run the verification checks:** `python3 scripts/verify.py`

## Verification results

`python3 scripts/verify.py` — **PASS** (as of this run):

```
OK — 29 files checked: links resolve, pages parse, rendering clean,
no external requests, no secrets.
```

What it checks:

1. All 13 expected docs/ files and 16 expected site/ files exist.
2. Every Markdown source renders without errors (python-markdown,
   tables + fenced-code + sane-lists extensions).
3. Every internal link in docs/ resolves — including `#fragment` links,
   which are matched against headings in the target file. (One deliberate
   exception: the intentionally-broken `notes.md` example link inside the
   mistakes gallery.)
4. Every internal `<a href>`/asset link in site/ HTML resolves; anchors
   exist in their targets.
5. All site pages parse as HTML and tags balance; site contains **no**
   external requests except the intentional attribution link to
   dylanasdale.github.io.
6. Secrets scan across text files (no API keys, tokens, private keys).
7. LICENSE contains the exact copyright line; README credits
   Asdale Dynamics, LLC.

Build sanity: `tools/build_site.py` was run and its output committed;
re-running it after these edits produced no diffs beyond the fixes noted
here. Diffs were reviewed — notably the README→index link rewrite and
GitHub-style task checkboxes rendered from `- [ ]`/`- [x]`.

## Known gaps

- **No anchor-link generation dedupe:** heading fragments in markdown
  examples aren't clickable in the HTML site (python-markdown doesn't
  auto-generate heading ids). Lesson 7 teaches the concept; the site
  itself doesn't demonstrate in-page anchors beyond what browsers do
  with `#`.
- **Sample images are references, not files:** Lesson 7's image examples
  (`desk.jpg`, `calendar-march.png`) are illustrative; no image assets
  ship with the guide.
- **Cheat sheet is textual:** it renders well in a browser print-out
  (Ctrl-P from `site/cheat-sheet.html`) but there is no separate PDF.
- **Only two walkthroughs:** tables and checkboxes; coverage of nesting
  + checkboxes in a single walkthrough (e.g., a full weekly planner with
  a nested grid) is a natural next addition.
- **not tested in browsers across engines:** HTML checks are static-analysis
  only; no automated browser screenshots were taken. Pages are simple,
  semantic HTML, so risk is low.

## Maintenance notes

- To edit content: change files in `docs/`, re-run
  `python3 tools/build_site.py`, then `python3 scripts/verify.py`.
- Never put API keys, secrets, or personal data in any file here; the
  verifier will catch most patterns, but nobody's regex is a real
  security control — review manually before sharing.
- Healthcare content rules from the LLC apply: education only, never
  medical advice (not an issue for this topic, but a standing rule).
