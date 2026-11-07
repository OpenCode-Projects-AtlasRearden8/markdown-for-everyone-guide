# Lesson 6 — Tables: Track Anything in a Grid

Tables are Markdown's superpower for messy details: budgets, gear
inventories, medicine schedules, game drop rates. One structure,
reusable for all of them.

## The syntax, decoded

A table is rows of cells separated by `|` (pipes), plus one special
"divider" row that defines the columns:

```markdown
| Item    | Qty | Where          |
| ------- | --- | -------------- |
| Charger | 2   | Desk drawer    |
| Batteries | 6 | Kitchen drawer |
| Extension cord | 1 | Garage bin |
```

| Item | Qty | Where |
| --- | --- | --- |
| Charger | 2 | Desk drawer |
| Batteries | 6 | Kitchen drawer |
| Extension cord | 1 | Garage bin |

**Read the parts:**

- **Row 1** — your column names.
- **Row 2** — the divider. It only needs `|---|---|---|`, but you can
  make it longer (`| :--- | ---: |`) to line things up.
- **Row 3+** — one line per entry.

You don't have to align pipes; most editors do it for you. Aligned is
prettier to read as text, though, so it's worth the two seconds.

## The divider is where alignment lives

```markdown
| Left | Center | Right |
| :--- | :---: | ---: |
| left-side text | centered text | right-side text |
```

| Left | Center | Right |
| :--- | :---: | ---: |
| left-side text | centered text | right-side text |

`---` → left. `:---:` → centered. `---:` → right. Numbers read best
right-aligned.

## Three everyday tables to steal

**A simple budget:**

```markdown
| Category | Plan | Actual | Diff |
| -------- | ---: | -----: | ---: |
| Groceries | 450 | 512 | -62 |
| Gas | 120 | 118 | 2 |
| Fun | 80 | 45 | 35 |
```

**A small-business gear list:**

```markdown
| Item | Cost | Listed On | Status |
| ---- | ---: | --------- | ------ |
| Vintage lamp | 18 | Mar 2 | Listed |
| Film camera | 42 | Mar 5 | Sold |
| Box of comics | 25 | — | Probing |
```

**A weekly workout log:**

```markdown
| Day | Planned | Done | Notes |
| ---- | ------- | :---: | ----- |
| Mon | Legs | Yes | 4 sets |
| Wed | Push | — | Rain |
| Fri | Pull | | |
```

## Table rules and gotchas

1. **One line per row**, always — no wrapped sentences inside a row.
   Long notes belong below the table.
2. **Same number of pipes on every line.** Parsers survive missing
   trailing pipes, but mismatched middle pipes will break the table.
3. **Empty cells are fine** — leave the space between pipes blank.
4. **No blank lines inside a table.** A blank line ends the table and
   starts new content.

## Try it now

1. Make a 3-column, 3-row inventory table.
2. Re-align the pipes neatly (easiest with a monospaced editor).
3. Add a Notes column and leave two cells empty.

Next lesson: [Links and images](07-links-and-images.md).
