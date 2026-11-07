# Markdown Cheat Sheet — One Page

*Print this. Pin it. You won't need it by next Tuesday.*

## Text

```
# H1 (page title)
## H2 (section)
### H3 (sub-section)

**bold**
*italic*
***both***
~~strikethrough~~
`inline code`
\* escaped star
```

## Paragraphs

- Blank line starts a new paragraph.
- Single line break does **not** start one — end the line with two
  spaces or a backslash to force a break.
- One idea per paragraph. Be generous with blank lines.

## Lists

```
- bullet item
1. numbered item
2. (parser renumbers anyway)
   - nested item (2 spaces)
```

**Bullets** = order doesn't matter.
**Numbers** = order does matter.

## Checkboxes

```
- [ ] open task
- [x] done task
   - [ ] sub-task (2 spaces)
```

Start tasks with verbs. Keep boxes tiny. Never delete finished
items — mark them `[x]`.

## Tables

```
| Item  | Qty | Notes |
| ----- | --: | :---: |
| Lamp  | 2   | garage |
| Cable | 1   | desk  |
```

Align columns: `:---` left, `:---:` center, `---:` right.
Every row needs the same inner pipes. No blank lines inside.

## Links and images

```
[visible label](https://example.com)
[link to heading in this file](#heading-name)
![image alt text](path/to/photo.png)
[![image](img.png)](bigger-destination.html)
```

Image paths are relative to the current file — `..` = up one folder.

## Quote blocks

```
> quoted line one
> quoted line two
```

## Code blocks

````text
```python
print("fenced code keeps every space")
```
````
Open and close with three backticks on their own lines. Put the
language name after the first fence for colored syntax.

## Rules

```
---
```
Three hyphens on their own line, blank lines above and below.

## Two-space check

- After `#` — one space, or it's not a heading.
- After `-` or `1.` — one space, or it's not a list.
- Around `**` and `*` — zero spaces, or it doesn't render.

---

Asdale Dynamics, LLC · markdown-for-everyone-guide · MIT licensed
