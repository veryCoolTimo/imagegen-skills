# Model adapter — Reve (Reve 2.0)

Top-tier model (~#2 on Artificial Analysis, mid-2026). Defining trait: it resolves the prompt
into a structured **layout** ("images as code") before rendering native 4K — so its edge is
**prompt adherence + layout/element editing** and **legible typography**. Output is prompt text
only.

## Prompt style

- **Plain, direct natural-language prose** — not keyword salad, not overly poetic. Describe
  subject, composition, mood, style, lighting in a clear paragraph; Reve derives the layout.
- **Be specific and concrete** — name **position, lighting source, and medium**; that improves
  adherence more than piling on adjectives.
- **Structured simplicity — one clear intent, minimal modifiers.** Mixing several art styles
  degrades results. Reve's thesis: "ambiguity is the enemy of control."
- Note: "Enhance" is on by default in the app (rewrites your prompt); 2.0 can occasionally drop
  a prompt element — verify output and fix via a layout edit rather than re-rolling.

## Text in images

- Quote the exact copy: `the sign reads "KELLERMAN'S HARDWARE — SINCE 1931"`.
- Describe font/weight/case/placement ("bold condensed sans-serif masthead, top-centered, all
  caps"). Good for mastheads, packaging, poster headlines, UI labels.
- Keep text short/prominent; very small/dense text can garble or typo — verify spelling; fix a
  bad string via layout edit.

## Editing / references (its strength)

- **Instruct edit:** input image + plain instruction. **"Change X, keep the rest"** works well —
  state what changes AND what to preserve ("move this object, shrink that text block, keep the
  subject, adjust the background, preserve the structure").
- **Layout/region edit:** select any element and edit its node (position, size, text) without
  redrawing the scene — the layout is the persistent source of truth.
- **Remix / multi-reference:** feed **1–4 reference images** as ingredients; Reve borrows
  character / lighting / material / environment from each and merges. More descriptive style
  text + a stronger reference = more accurate.
- **Weakness:** real-photo multi-subject **identity preservation** is less exact than Nano
  Banana Pro — recognizable, not pixel-faithful. For strict likeness, prefer gpt-image-2 /
  Nano Banana Pro.

## Aspect ratios / resolution

- **7 ratios:** `16:9 9:16 3:2 2:3 4:3 3:4 1:1` (API default `3:2`).
- Native **2048×2048**, upscalable to **4096×4096 (4K)**. Output PNG/JPEG/WebP.
- Prompt budget ~**2560 characters**.

## Params / API

Base `https://api.reve.com/v1/` — operations **Create / Edit / Remix** (+ upscale, background
removal, resize, saved effects). Third-party aggregator IDs (unconfirmed as native):
`reve/create-image` (`prompt`, `aspect_ratio` def `3:2`), `reve/edit-image` (`image_url` +
`prompt`), `reve/remix-edit-image` (`image_urls` 1–4). No documented `seed`/`negative_prompt`/
`width-height` in that schema — verify against the native API.

## Output template

```
[Subject + key attributes], [composition & where each element sits]. [In-image text in quotes] rendered as [font/weight/case], [placement]. Style: [one coherent medium/aesthetic]. Lighting: [single clear source/direction]. Palette: [2–3 colours or mood]. [aspect ratio], 4K.
```
Editing: `Keep [everything to preserve] exactly as is; change only [X] to [Y].`
Remix: `Combine these references: use [ref 1] for the character, [ref 2] for lighting/environment; render as [style]. [scene].`

## Sources
blog.reve.com (Reve 2.0 announcement, "The Layout Bet", editing model), help.reve.com (API — 403 to bots), app.reve.com; Artificial Analysis leaderboard; reputable reviews (Decrypt, Morphic, WaveSpeed). Uncertain: official prompt docs are thin (product/philosophy pages, not a formal guide); model IDs + 2560-char limit are from a third-party aggregator, not confirmed native.
