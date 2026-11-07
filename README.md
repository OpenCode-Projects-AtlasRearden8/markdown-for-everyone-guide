# Markdown for Everyone

Plain-English manual teaching **Markdown as a life skill** — notes, to-do
lists, resumes, READMEs, and simple docs — in nine tiny lessons. With a
printable cheat sheet, step-by-step table and checkbox walkthroughs, and a
common-mistakes gallery. Written the way a friend would explain: step by
step, never condescending.

## What's inside

```text
docs/
├── lessons/          nine tiny lessons, in reading order (01–09)
├── walkthroughs/     two hands-on builds: checkboxes week plan, gear table
├── cheat-sheet.md    one-page printable reference
├── common-mistakes.md  ten real rendering traps + a debug checklist
└── README.md         the guide's own table of contents
site/                 static HTML version — open site/index.html, done
tools/build_site.py   optional re-generator for site/ (already committed)
scripts/verify.py     checks links, HTML, and rendering (see Verification)
```

## How to use it

**Read:** start at [docs/README.md](docs/README.md) for the lesson list, or
open [site/index.html](site/index.html) in any browser — fully offline, no
JavaScript, no tracking, no build step required.

**Practice:** every lesson ends with a short "Try it now" list. Do those
steps in a `notes.md` file as you go; the lessons build on each other.

**Regenerate the site** (optional; the built HTML already ships):

```bash
pip install markdown
python3 tools/build_site.py
```

## Verification

Run the built-in checks:

```bash
python3 scripts/verify.py
```

This verifies every internal link in docs/ and site/ resolves, every HTML
page parses, the site contains all expected pages, and all Markdown
sources render without errors. Exits non-zero on any failure.

## Privacy and design promises

- **Local-first:** everything works offline; your notes stay on your device.
- **No tracking:** no analytics, no cookies, no external requests.
- **No build step:** write text, save, done. The site is plain HTML.

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC

## About

From Dylan Asdale and **Asdale Dynamics, LLC** — beginner-friendly AI and
computer skills, explained like a friend would. Discover more guides, books,
and tools at [dylanasdale.github.io](https://dylanasdale.github.io).

*Healthcare-worker AI aids from Asdale Dynamics are for education only and
never medical advice.*
