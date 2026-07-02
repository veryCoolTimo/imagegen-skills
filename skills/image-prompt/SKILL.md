---
name: image-prompt
description: >-
  Use when the user wants to turn a short idea into a rich, production-grade
  image-generation prompt — posters, landing-page or UI mockups, ads, editorial
  layouts, photoreal scenes, game screenshots, logos, or illustrations. Builds ONE
  structured, copy-paste-ready prompt optimized for gpt-image-2 by default, following
  proven layered-composition patterns (named zones, hex palette, real font references,
  mood/finish, IP-safety). Triggers on requests like "сделай крутой промт для постера",
  "нужна картинка/постер/лендинг для…", "generate a prompt for a landing hero",
  "prompt for an ad / logo / game screenshot".
---

# image-prompt

Turn a one-line idea into a single, gold-quality image-generation prompt. Auto-first:
infer everything sensible, output the prompt, let the user redirect in one line.

## Workflow

1. **Read the idea.** Extract: subject/brand, any style hints, aspect/format, target model.
   Invent a fictional placeholder brand name if branding is implied but none given.

2. **Pick the archetype** using `references/archetypes.md` (poster / landing-hero /
   product-ad / ui-mockup / photoreal-scene / game-screenshot / infographic / logo /
   illustration). Use the routing table. If ambiguous, choose the richest layout and note it.

3. **Set defaults** from the archetype: aspect → `size`, `quality`. (See the model adapter.)

4. **Expand into the 9-block skeleton** using `references/anatomy.md`. Skim the matching
   gold example(s) in `references/gold-examples.md` to calibrate depth and phrasing. Pull
   fonts + a cohesive hex palette from `references/fonts-palettes.md`. Fill every block:
   named zones with position/size%/tilt, literal copy in quotes, named fonts, hex palette,
   mood cluster, finish + quality tag. Photoreal/game ideas use the labeled-block variant.

5. **Format for the target model.** Default `gpt-image-2` → follow
   `references/models/gpt-image-2.md` (labeled sections, text-in-quotes, CONSTRAINTS block,
   size/quality). If the user names another model and its file doesn't exist yet, say so and
   fall back to the rich natural-language style, then proceed.

6. **Output** (see format below): the finished prompt in its own fenced code block, then a
   one-line assumptions/knobs note underneath.

## Auto-first — do NOT interrogate

Produce a full prompt on the first turn. Only ask **one** question if the idea is truly
unworkable (e.g. no discernible subject at all). Everything else — archetype, aspect,
palette, brand name, copy — you infer and surface in the assumptions line so the user can
correct with a single sentence ("make it 9:16", "darker palette", "brand is NOVA").

## Model handling

- Default target model: **gpt-image-2**. Adapter: `references/models/gpt-image-2.md`.
- If the user says a model with no file yet (universal / Midjourney / Gemini / Ideogram),
  note "no dedicated adapter yet, using rich NL style" and build a model-agnostic rich
  prompt (drop the gpt-image-2 CONSTRAINTS/size wording, add flags like `--ar/--v` only for
  Midjourney).

## Output format

Put the prompt in **its own fenced code block** so the user can copy it in one action.
Nothing else inside the block. Then one assumptions line beneath it:

````
```
<the finished prompt — labeled sections for gpt-image-2>
```
**Assumptions:** archetype=<x> · size=<WxH> · quality=<low|medium|high> · brand=<name> ·
model=gpt-image-2. Change any of these in one line, or say "another variant".
````

Keep the prompt itself clean and self-contained (no meta-commentary inside it).

## Quality bar (non-negotiable)

- Name **real fonts** for every text role; never "a nice font".
- Give **every color a hex code**; never a bare color word.
- Break the canvas into **named zones with positions** — this is the #1 quality signal.
- Include a **finish/texture cue** (grain, halftone, brushwork, pores) and a quality tag.
- Put **all rendered text in quotes**; keep it short; render each string once.
- Always add IP-safety: original design, no logos/trademarks/watermark; brand-like glyphs
  are "generic, not resembling any real brand".

## Growing the skill

New favourite prompt → add it to `references/gold-examples.md` (with a "Teaches:" tag).
New model → add `references/models/<name>.md`; the workflow above stays unchanged.
