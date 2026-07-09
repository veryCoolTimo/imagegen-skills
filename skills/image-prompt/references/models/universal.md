# Model adapter — universal (rich natural language)

The model-agnostic default: a single, richly detailed natural-language prompt that works well
across almost any capable model (and is the style of the original gold examples). Use when the
target model is unknown, unsupported, or when the user just wants "a great prompt".

## How to render

Write the full **9-block skeleton as flowing descriptive prose** (see `anatomy.md`) — do NOT
use API-style labeled sections or model flags. One rich paragraph (or a few), covering in order:

1. Concept line (format + medium + fictional brand + reference aesthetic + intended use)
2. Canvas & background (aspect ratio in words + treatment with **hex** + global texture)
3. Named composition zones (position + size% + tilt + content)
4. Subject detail (granular; IP-safe)
5. Typography & text (literal copy **in quotes** + **named real fonts** + color hex + placement)
6. Palette (4–6 **hex** codes, each mapped to an element)
7. Font role map
8. Mood cluster + era/reference anchor
9. Finish/texture + an authority **quality tag** ("Awwwards / Behance-quality … 4k")

Calibrate depth against `gold-examples.md` — this adapter is exactly that level of richness.

## Rules

- Keep everything the gold examples do: real font names, hex for every colour, named zones,
  finish cue, IP-safety ("generic, not resembling any real brand").
- State the aspect ratio in words (e.g. "vertical 2:3", "full-width 16:9") since there are no
  size params.
- No API params, no `--flags` (those belong to the model-specific adapters).

## Output

One clean, self-contained prose prompt in a fenced block, then the assumptions line
(archetype · aspect · brand · model=universal). No CONSTRAINTS/size/quality block (that's
gpt-image-2-specific), though you may end with "original design, no logos/trademarks/watermark".

## When to switch

If the user names a supported model, use that adapter instead (gpt-image-2, midjourney, flux,
ideogram, …). Universal is the safe fallback and the best choice for pasting into an unknown
tool.
