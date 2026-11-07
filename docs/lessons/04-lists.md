# Lesson 4 — Lists: Bullets, Numbers, and Nested Steps

Lists are where Markdown starts paying rent. Grocery runs, care plans,
packing bags, troubleshooting steps — anything with items belongs in a list.

## Bulleted (unordered) lists

Start lines with `- ` (hyphen, space). That's all:

```markdown
- Milk
- Dog food
- Coffee filters
- Stamps
```

- Milk
- Dog food
- Coffee filters
- Stamps

`*` and `+` also work, but `-` is cleanest to read and most common.

## Numbered (ordered) lists

Start lines with a number, a dot, and a space:

```markdown
1. Preheat oven to 400°F.
2. Season the chicken.
3. Roast for 35 minutes.
```

1. Preheat oven to 400°F.
2. Season the chicken.
3. Roast for 35 minutes.

Handy honesty: the numbers don't have to be correct. `3. 4. 5.` renders
as 1, 2, 3 — the *order of the lines* decides the numbers, so copy-pasted
lists never come out wrong.

## Nested lists (sub-items)

Indent two spaces (some apps want four; two spaces works on GitHub):

```markdown
1. Get the car ready
   - Check tire pressure
   - Top off wiper fluid
2. Check in
   - License
   - Insurance card
   - Clinic card
```

1. Get the car ready
   - Check tire pressure
   - Top off wiper fluid
2. Check in
   - License
   - Insurance card
   - Clinic card

You can mix bullet types when nesting: numbers for main steps, hyphens
for details. That mixing is a driver's-license-day classic.

## Separating steps from stuff

This distinction is the whole game:

- **Numbered lists** mean *order matters* — do step 1 before step 2.
- **Bulleted lists** mean *order doesn't matter* — it's a pile of stuff.

If your "steps" are bullets, a reader may do them in the wrong order.
If your "stuff" is numbered, a reader may think there's a required
sequence. Choose on purpose.

## Try it now

1. Make a 4-item grocery list with `- `.
2. Make a 3-step bedtime routine with `1. 2. 3.`.
3. Nest two sub-items under step 2, indented two spaces.

Next lesson: [To-do checkboxes](05-todo-checkboxes.md).
