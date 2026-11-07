# Lesson 8 — Quotes, Code, Horizontal Rules, and Escaping

A grab-bag of finishing touches. Small tools, but they show up
constantly in notes, READMEs, and documentation.

## Blockquotes: for borrowed words and warnings

Start lines with `> ` (greater-than, space):

```markdown
> Not everything that counts can be counted.
> — often credited to Albert Einstein
```

> Not everything that counts can be counted.
> — often credited to Albert Einstein

Great for: quotes, pull-out warnings in guides, answers in study
notes. Consecutive `>` lines stay one quote; a blank line ends it.

## Code: inline and fenced

**Inline code** — single backticks for a word or two:

```markdown
Press `Ctrl+S` to save, or run `npm install`.
```

Renders: Press `Ctrl+S` to save, or run `npm install`.

**Fenced code** — triple backticks around a block:

````
```text
Project tree:

my-project/
├── README.md
├── docs/
└── images/
```
````

Fenced blocks keep every space and line break exactly as typed —
that's why we've used them all through this guide to *show* you
Markdown without rendering it.

**Formatting a block of existing text:** in VS Code, Obsidian, or
GitHub's editor, select the lines and press backtick three times or
use the language button — faster than typing fences manually.

## Horizontal rules: for "chapter break" moments

Three hyphens on their own line (blank lines above and below):

```markdown
---

New section below the line.
```

Use sparingly — a `##` heading usually does the job better. Two or
three rules per document is plenty.

## Escaping: when Markdown eats your punctuation

Sometimes you *want* people to see a literal `*` or `#`. Put a
backslash in front:

```markdown
\* Not a bullet, just a star
\# Not a heading, just a hash
\_ Not italics
```

Renders as: \* Not a bullet, just a star

The characters that need escaping most often: `` ` ``, `*`, `_`,
`#`, `[`, `]`.

## Try it now

1. Quote one sentence from a book you like.
2. Put your keyboard's Save shortcut in inline code.
3. Write a fenced block holding a tiny folder tree.
4. Escape one `*` so it shows up as a star.

Next lesson: [Real-life documents](09-real-life-documents.md).
