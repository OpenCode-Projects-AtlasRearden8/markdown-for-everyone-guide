# Lesson 7 — Links, Images, and Where Files Live

Links and images are how Markdown documents reach out to the world —
to other files, to websites, and to your own screenshots.

## The link syntax

Square brackets for the label, parentheses for the address, no space
between them:

```markdown
[Click here for the Markdown cheat sheet](../cheat-sheet.md)
```

Renders as: [Click here for the Markdown cheat sheet](../cheat-sheet.md)

Part of speech matters:

- `[label]` — what the reader sees. Write it like a signpost,
  not "click here" on loop.
- `(address)` — where the link goes. Can be a web address,
  a local file, or a section heading.

## Linking to headings inside your own document

Most Markdown renderers auto-generate anchors from headings:

```markdown
See [the mistakes gallery](#the-gallery) below for trap #1.
```

Use `-` instead of spaces, all lowercase, drop punctuation. It's a
little fragile across renderers, so test before publishing.

## Images: same shape, one `!` prefix

```markdown
![A photo of my desk setup](desk.jpg)
```

- `!` before the brackets — that's the whole difference from a link.
- `[brackets]` become *alt text* — describe the image for people
  using screen readers and for you when the link breaks.
- `(parentheses)` take the image's location.

Real example:

```markdown
![My workout log wall calendar for March](calendar-march.png)
```

## Where files live (the part that trips everyone up)

The `(address)` is a path **relative to the file you're writing in**:

```text
my-project/
├── README.md
├── images/
│   └── calendar.png
└── docs/
    └── plan.md
```

- From `README.md`: `images/calendar.png`
- From `docs/plan.md`: `../images/calendar.png`

`..` means "up one folder." Two dots up would be `../..`. Spell paths
out at the moment you write them; fixing a dozen broken links later
is the boring kind of evening.

## Making an image a clickable link

Nest an image inside a link — brackets' content can be anything:

```markdown
[![Open my resume in PDF](resume-preview.png)](resume.pdf)
```

## Try it now

1. Link to one website you visit daily.
2. Add one image reference (even if the file doesn't exist yet —
   note the label question: what's the missing image's alt text say?).
3. Link to a `##` heading inside the same document.

Next lesson: [Quotes, code, and extras](08-quotes-code-and-extras.md).
