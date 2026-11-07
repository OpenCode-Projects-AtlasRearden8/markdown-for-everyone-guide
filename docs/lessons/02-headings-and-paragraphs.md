# Lesson 2 — Headings and Paragraphs: Giving Notes Shape

Formatting isn't decoration — it's wayfinding. Headings tell your future
self (and anyone you share with) what matters and where things live.

## Headings: six sizes, one character

Put `#` (a hash) and a space before a line of text:

```markdown
# Level 1 — biggest
## Level 2 — section
### Level 3 — sub-section
#### Level 4
##### Level 5
###### Level 6 — smallest
```

Renders like:

# Level 1 — biggest

## Level 2 — section

### Level 3 — sub-section

**Three rules that save you trouble:**

1. One `# ` heading per page. It's the document title.
2. Don't skip levels (go `##` then `###`, not `##` then `####`).
3. The space after `#` is required. `#Nope` is not a heading.

## Paragraphs: the blank line is everything

Markdown has one paragraph rule, and it's strict:

```markdown
This is one paragraph.

This is a second paragraph.

But this line
and this line
will be glued into the same paragraph.
```

Why? Markdown is built from plain text. A single line break is invisible
to the reader; a *blank line* is the only way to start a new paragraph.

**The fix for the glued-lines problem:** end the previous line with two
spaces, or (in most apps) a backslash `\`. Better yet, don't fight it —
just write one idea per paragraph and use blank lines generously.

## Line-by-line lists of thoughts? Use lists

If you find yourself using two-space line breaks for a "list of things,"
that's a sign it should be an actual list:

```markdown
- Monday: call the clinic
- Tuesday: refill prescription
- Wednesday: water the plants
```

You'll meet lists properly in Lesson 4 — this is just a preview.

## Real life example: a jump-rope routine

```markdown
# Jump-Rope Plan

**Goal:** 5 minutes unbroken by June.

## This week

Mon and Wed: 3 sets of 60 seconds, rest 60 seconds between.

Fri: try 90 seconds straight, even slowly.

## After this week

Add 30 seconds per set. Rest is allowed — slow beats nothing.
```

Notice: `#` title, `##` sections, a bold goal line. That's a document
anyone can follow with zero explanation.

## Try it now

1. Add a `##` section to `notes.md` called `This Week`.
2. Under it, write two short paragraphs separated by a blank line.
3. Glue test: write two lines with no blank line between them and see
   them join. Add the blank line. Watch them separate.

Next lesson: [Bold, italic, and emphasis](03-bold-italic-and-emphasis.md).
