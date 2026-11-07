# Walkthrough — A Weekly Plan with Checkboxes

Build a real weekly plan in Markdown, from empty file to ticking
boxes. Ten minutes, start to finish. Use any plain-text editor.

## Step 1 — The skeleton

Create `week.md` and start with the title and two headings:

```markdown
# Week of ____

## Must do
## Nice to have
```

## Step 2 — Your first checkbox list

Under `## Must do`, add three open boxes:

```markdown
- [ ] Pay electric bill
- [ ] 20 minutes on resume
- [ ] Refill prescriptions
```

**Rule of thumb:** max 3 "must" boxes per day-tier. More than that
and it's a guilt pile, not a plan.

## Step 3 — Break one big task down

"Resume" is really five tasks. Nest sub-boxes, indented 2 spaces:

```markdown
- [ ] 20 minutes on resume (timer on)
  - [ ] List last 3 jobs
  - [ ] Write 2 bullet points for each
  - [ ] Save as resume-draft.md
```

## Step 4 — Add duplicates and a notes line

Some tasks repeat. Just add another box — Markdown doesn't care:

```markdown
- [ ] Water fern — Mon
- [ ] Water fern — Thu
```

Or use one line and a small inline code note for strength details:

```markdown
- [ ] Push-ups — 3 sets of 10
```

## Step 5 — The "done" side

During the week, flip boxes and *leave them*:

```markdown
- [x] Pay electric bill
- [ ] 20 minutes on resume (timer on)
```

The `[x]` items are your completed record. Don't delete them at
week's end — copy them into a "done" section first:

```markdown
## Done this week
- [x] Pay electric bill
- [x] Texted landlord
```

## Step 6 — Roll open items forward

On Sunday, make next week's plan: carry over each unchecked `- [ ]`
box. Anything left three weeks running is either too big (split it!)
or not actually wanted (delete it, guilt-free).

## Full example file

```markdown
# Week of Nov 3

## Must do
- [x] Pay electric bill
- [ ] 20 minutes on resume (timer on)
  - [ ] List last 3 jobs
  - [ ] Write 2 bullets per job
- [ ] Refill prescriptions

## Nice to have
- [ ] Water fern — Mon
- [ ] Water fern — Thu
- [ ] Chess puzzle set

## Done this week
- [x] Pay electric bill
```

## Variations to try

- **Three-box day:** in a daily file, copy just 3 must-boxes. Reset
  tomorrow.
- **Body doubling:** share the file with a friend; watching each
  other's `[x]` marks accumulate keeps both of you going.
- **Table hybrid:** add a small table at the bottom for numbers you
  kept — calorie counts, weights, or money spent.

When you're ready for the second walkthrough, head to
[table-gear-inventory.md](table-gear-inventory.md).
