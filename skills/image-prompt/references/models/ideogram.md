# Model adapter — Ideogram (v4)

How to render the 9-block content as an Ideogram prompt. Ideogram is the in-image **text**
specialist. Two modes: **plain-text** (default) and **structured JSON** (per-element control).
Output is prompt text only.

## Prompt structure (plain-text, default)

- **Order:** subject → key details → secondary elements → background → lighting → atmosphere.
  Lead with the subject (earlier = weighted more).
- **Natural English sentences**, not tag lists. Write in **English** (non-Latin scripts render
  unreliably). Don't overload with unrelated concepts; ~<150 words performs best.

## Text rendering (headline capability)

- Put literal text **in quotes** and describe it **near the beginning** (better accuracy than
  at the end): `A poster with text that reads "SLOW MORNINGS" …`.
- **You cannot name a font** — describe style instead: "bold sans-serif", "thin rounded
  Bauhaus", "elegant formal script with flourishes". State color, weight, placement inline.
- Short beats long; break longer text into chunks with per-chunk placement. Reduce scene
  clutter when clean text matters. For critical/long copy, add text in post.

## Settings

- **Magic Prompt:** `OFF` for deterministic control (default here); `AUTO`/`ON` for
  exploration (it rewrites/expands your prompt).
- **style_type:** `AUTO | GENERAL | REALISTIC | DESIGN | FICTION` (mutually exclusive with
  style-reference images).
- **color_palette:** named presets (`EMBER FRESH JUNGLE MAGIC MELON MOSAIC PASTEL
  ULTRAMARINE`) or custom hex; in JSON, hex must be **UPPERCASE `#RRGGBB`** (lowercase/shorthand
  can degrade quality). Include highlight + shadow colours for controlled lighting.
- **negative_prompt:** exclusions (positive description still takes precedence).

## Aspect ratios / resolutions

Vertical `1:3 1:2 9:16 10:16 2:3 3:4 4:5` · square `1:1` · horizontal `5:4 4:3 3:2 16:10 16:9
2:1 3:1` (API uses `x`, e.g. `2x3`). v4 spans 256–2048 px/side; aspect ratio and explicit
resolution are mutually exclusive; the system may normalise to the nearest supported tier.

## Output template (plain-text, default)

```
[Subject], [defining details], with text that reads "EXACT TEXT" in a [font-style, weight, color] typeface positioned [where].
[Secondary elements]. [Background/setting]. [Lighting & atmosphere].
[Overall style: realistic photo / flat design / illustration], [palette or mood].
```
Settings to report: `style_type` · `magic_prompt` (default OFF) · `aspect_ratio` · optional
`color_palette` (preset or hex) · optional `negative_prompt`.

## JSON mode (advanced, v4)

When the endpoint supports it, emit a caption object — required block is
`compositional_deconstruction` (`background` + `elements[]`), with `high_level_description` and
`style_description` (exactly one of `photo`/`art_style`, plus `color_palette` UPPERCASE hex).
A typed `{"type":"text","text":"…","desc":"…"}` element separates the string from its styling
(enables multi-line / multi-font). Bridge: on the app, Magic Prompt auto-converts plain text
to this JSON.

## Sources
docs.ideogram.ai (prompting-guide: fundamentals, text-and-typography, in-a-nutshell; generation-settings: magic-prompt, aspect-ratio), developer.ideogram.ai (generate v3 enums), ideogram.ai/blog/ideogram-4.0. Uncertain: <150-word figure is guidance; exact resolution tables are endpoint-dependent.
