# Lesson 3 — Bold, Italic, and Emphasis

Small touches, big clarity. This is the shortest lesson because it's the
easiest — just four patterns you'll use forever.

## The four patterns

```markdown
**Bold**              → **Bold**
*Italic*              → *Italic*
***Bold and italic*** → ***Bold and italic***
~~Strikethrough~~     → ~~Strikethrough~~
```

Rendered: **Bold**, *Italic*, ***Bold and italic***, ~~Strikethrough~~.

You can also use underscores (`_like this_`), but asterisks are easier to
see and type on most keyboards. Pick one style and stick with it.

## Where emphasis actually helps

Emphasis is not for decoration. It's a pointing finger. Use it when a
reader skimming your text needs one thing to pop out:

- **Deadlines:** "Submit by **Friday, May 9**."
- **Warnings:** "Never share the backup key."
- **Key terms when teaching:** a *hierarchy* is a folder tree.
- ~~Done~~ items you want to keep visible but crossed out.

## A habit worth copying: the "why" line

Many note-takers start documents with one bold line explaining the
document's purpose. Six months later, that one line is priceless:

```markdown
**Why this file exists:** Tracking our small-business gear so tax
season takes 2 hours instead of 2 days.
```

## Small trap, easy fix

If bolding "doesn't work," the usual culprit is a space inside the
marks: `** bold **` renders literally, but `**bold**` works. The marks
must hug the text tight, with no spaces inside.

Common failure:

```markdown
** Good **   → renders with asterisks showing
**Good**     → renders as bold
```

And don't accidentally double-space between marks and text. Markdown
parsers at GitHub and most apps agree on this, so fix it once and it
fixes everywhere.

## Try it now

1. In `notes.md`, bold one deadline.
2. Italicize one term you're learning.
3. Strikethrough one item you already finished.

Next lesson: [Lists: bullets, numbers, and nesting](04-lists.md).
