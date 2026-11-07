# Walkthrough — A Gear Inventory Table for a Small Resale Business

Build a real table, then grow it into a mini-document. This uses
reselling as the example, but the pattern fits budgets, workout
logs, plant care, or anything with rows.

## Step 1 — Start with three columns

```markdown
| Item | Paid | Status |
| ---- | ---- | ------ |
| Vintage lamp | 18 | Listed |
| Film camera | 42 | Sold |
| Box of comics | 25 | Probing |
```

| Item | Paid | Status |
| ---- | ---- | ------ |
| Vintage lamp | 18 | Listed |
| Film camera | 42 | Sold |
| Box of comics | 25 | Probing |

Three columns is the sweet spot to start — enough structure to be
useful, not so much that rows become essays.

## Step 2 — Widen it when you need more

Add columns by extending the divider row and every data row:

```markdown
| Item | Paid | Listed On | Status | Notes |
| ---- | ---: | --------- | ------ | ----- |
| Vintage lamp | 18 | Mar 2 | Listed | Needs shade |
| Film camera | 42 | Mar 5 | Sold | 24 margin |
| Box of comics | 25 | — | Probing | Check grading |
```

| Item | Paid | Listed On | Status | Notes |
| ---- | ---: | --------- | ------ | ----- |
| Vintage lamp | 18 | Mar 2 | Listed | Needs shade |
| Film camera | 42 | Mar 5 | Sold | 24 margin |
| Box of comics | 25 | — | Probing | Check grading |

Alignment choices: `Paid` is right-aligned (`---:`) so digits line
up; `Listed On` and `Notes` are left; `Status` is centered.

## Step 3 — Add a totals line

Markdown tables don't auto-sum, and that's fine — add a **Total**
row and do the math once:

```markdown
**Invested:** $85 across 3 items · **Recovered:** $66 · **Margin:** -19
```

Bold label, then small facts. One line, not a paragraph.

## Step 4 — Context below the table

Tables carry facts; paragraphs carry *why*. Add short paragraphs:

```markdown
Probing = listed on a single marketplace to test price without
paying a second listing fee.

Rule for this stack: nothing gets listed at a loss unless it's
been sitting 60+ days.
```

## Step 5 — Wrap it in a README

Turn everything into a file GitHub (or a notes app) can present:

```markdown
# Gear Inventory

Tracking what we bought, listed, and sold this season.

## Status

| Item | Paid | Listed On | Status |
| ---- | ---: | --------- | ------ |
| Vintage lamp | 18 | Mar 2 | Listed |
| Film camera | 42 | Mar 5 | Sold |
| Box of comics | 25 | — | Probing |

## Notes

Probing = single-marketplace listing to test price.

## Related

- [Markdown cheat sheet](../cheat-sheet.md)
- [Common mistakes](../common-mistakes.md)
```

That's a document you could paste straight onto GitHub today.

## Sanity checklist before you publish any table

- [ ] Same number of inner pipes on every row
- [ ] No blank line inside the table
- [ ] Numbers right-aligned
- [ ] Empty cells are just blank (never `-` unless you mean "no data")
- [ ] A short paragraph below the table for the *why*

## Variation to try

Add a "Source" column values like `Estate sale`, `Thrift`,
`Buy Nothing` — a month of rows later, that column tells you where
your money is best spent.

Back to all lessons: [docs README](../README.md)
