# Lesson 9 — Real-Life Documents: Putting It Together

Everything from Lessons 1–8, used for documents you'll actually want.
Copy these templates and change the words.

## Document: Weekly plan (checkboxes)

```markdown
# Week of Nov 3

## Must do
- [x] Pay electric bill
- [ ] Return library books
- [ ] 30 minutes on resume

## Should do
- [ ] Meal prep chili
- [ ] Text Mom back

## If energy allows
- [ ] Sort eBay listings
- [ ] Chess puzzle set
```

Two lists, three energy tiers, twelve boxes. Everything from Lessons
3, 4, and 5 in action — done after breakfast most mornings.

## Document: Resume (draft in Markdown, export later)

```markdown
# Dylan Asdale
Nurse, AI author, and founder of ASDALE DYNAMICS, LLC

dylan@example.com · Indianapolis, IN

## Experience

**Founder, Asdale Dynamics, LLC** — 2026–present
Publish beginner-friendly AI guides in plain English.

**Registered Nurse** — 2015–2026
Championed charting standards and patient education.

## Skills

- Plain-language technical writing
- Patient and staff education
- Local-first AI workflows

## Education

**ADN, Nursing** — community college, 2014
```

There are Markdown-to-PDF converters for finished resumes; the draft
stage is where Markdown shines. Never put a home address on a resume
you share online — use city and state at most.

*Styled headings (`##`) and bullets read cleanly for reviewers; many
job posts accept `.txt`, so a Markdown resume copy-pastes well.*

## Document: README (the cover page of a project)

Every GitHub repository looks for a file named `README.md` and shows
it on the front page. The skeleton:

```markdown
# Project Name

One sentence: what this does and for whom.

## Quick start
1. Download the file
2. Open it

## How it works
Brief explanation, maybe a table.

## License
MIT — see [LICENSE](../LICENSE).
```

See the full worked example in the
[tables walkthrough](../walkthroughs/table-gear-inventory.md), which
builds a README plus a small-business gear table from scratch.

## Document: Simple doc / FAQ

```markdown
# How to refill the coffee machine

## Steps
1. Pull the drawer out.
2. Dump the old grounds.
3. Add three scoops.

## Troubleshooting
| Problem | Likely cause | Fix |
| ------- | ------------ | --- |
| Drips slowly | Old grounds | Rinse basket |
| No power | Plug loose | Push plug in |
```

Note the anatomy of every good FAQ: steps first, then a table keyed
by symptom. A reader with a problem gets an *answer*, not an essay.

## Your starter kit

You now have every convention in use wherever Markdown lives:

- `#` headings, blank-line paragraphs
- `**bold**`, `*italic*`, `~~struck~~`
- `- lists`, `1. order`, `   nesting`
- `- [ ] / [x]` checkboxes
- `| tables |` with dividers
- `[links](places)`, `![alt](images)`
- `> quotes`, `` `code` ``, fences, `---` rules, `\* escaping`

Everything else — footnotes, math, definition lists — is an
extension for special renderers, and you can pick it up anytime.

The [cheat sheet](../cheat-sheet.md) is your one-page companion. Print
it, tape it up, stop needing it in a week. Then check the
[common mistakes gallery](../common-mistakes.md) when something
renders sideways.
