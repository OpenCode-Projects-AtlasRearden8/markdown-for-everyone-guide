# The Common-Mistakes Gallery

Every entry below is a real mistake that renders *wrong* on GitHub and
almost every Markdown app. Each one shows the broken input, the
symptom you'll see, and the one-move fix. Use this as a diagnosis
chart when something looks sideways.

---

## 1 — The missing space after `#`

```markdown
#My Heading
```

**Symptom:** renders as literal text with a hash in front of it.

**Fix:** add a space: `# My Heading`. The `#` must be followed by a
space to become a heading.

---

## 2 — Bold with spaces inside

```markdown
** bold text **
```

**Symptom:** asterisks show as asterisks. Nothing bolds.

**Fix:** hug the text: `**bold text**`. Spaces inside the markers
break them in nearly every renderer.

---

## 3 — List glued to the paragraph

```markdown
Here is my list of steps:
- Brush teeth
- Floss
```

**Symptom:** this *works* on GitHub, but many stricter parsers (older
tools, some static-site generators) run the items into the paragraph
as one line instead of list items.

**Fix:** put a blank line between the sentence and the list. Blank
lines are free.

---

## 4 — Wrong list-break style

```markdown
1. Step one
2. Step two
Sentence after the list.
```

**Symptom:** that trailing sentence renders as paragraph — fine — but
if you *wanted* it inside item 2 you'll get two separate blocks.

**Fix:** indent the continuation line two spaces:

```markdown
2. Step two
   continued text under item two
```

---

## 5 — Table with mismatched pipes

```markdown
| Item | Qty | Notes |
| --- | --- |
| Lamp | 2 | garage |
```

**Symptom:** header row renders as one column and then the table
splits, or text renders with pipes everywhere.

**Fix:** one divider `|` per column, every row:

```markdown
| Item | Qty | Notes |
| --- | --- | --- |
| Lamp | 2 | garage |
```

---

## 6 — Line break swallowed by the paragraph rule

```markdown
Line one.
Line two.
```

**Symptom:** renders as `Line one. Line two.` on one line.

**Fix:** either put a blank line between them (paragraphs — usually
what you want), or end line one with two trailing spaces or a `\` for
a hard break inside a paragraph.

---

## 7 — Nested list with wrong indent

```markdown
- Outer item
    - Inner item (4 spaces)
  - Inner item (2 spaces)
```

**Symptom:** usually renders fine, but some parsers treat four-space
inner lines as code blocks instead of list items.

**Fix:** use two spaces for nesting — the lowest common denominator:

```markdown
- Outer item
  - Inner item
```

---

## 8 — Code fence left unclosed

````
```
print("hello")
````

**Symptom:** everything after the opening fence turns into a code
block — the rest of the document looks like one giant code sample.

**Fix:** each ``` opener needs a ``` closer on its own line. Count
your fences in pairs.

---

## 9 — Broken relative links

```markdown
See [my notes](notes.md) for details.
```

That link works from `README.md` at the project root but 404s from
`docs/plan.md`, which needs `../notes.md`. (The link above is a
deliberate example — it intentionally points at a file that is not
here, which is exactly the mistake it's teaching.)

**Fix relative-path math once:** the path in `( )` is counted from
where the file *siting* lives, not from your browser or your project
root. `./` = this folder. `../` = one folder up.

---

## 10 — Checkbox flavor: `[X]` or `[x ]`

```markdown
- [X] caps — some parsers miss it
- [x ] stray space — almost all parsers miss it
- [x] correct
```

**Symptom:** "done" items that don't check off.

**Fix:** always the exact string `[x]` (lowercase, no inner space) or
`[ ]` (exactly one inner space) for open items.

---

## The five-second debug checklist

When markdown breaks, run down these in order — 90% of problems
die at step 2:

1. **Blank line?** — between blocks of different types (heading, list,
   table, paragraph, fence).
2. **Space after the marker?** — `# `, `- `, `1. `, `> `.
3. **Same pipe count in the table?**
4. **Fences paired?** — count your ``` in twos.
5. **Path relative to the file writing it?**

*Found a mistake not in this gallery? Fix it and send it our way —
this file is MIT-licensed like everything here.*
