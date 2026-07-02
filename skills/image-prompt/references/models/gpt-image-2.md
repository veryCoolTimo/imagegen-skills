# Model adapter — gpt-image-2 (default)

How to render the 9-block content as a prompt tuned for OpenAI's `gpt-image-2`, and how
to pick `size` and `quality`. Distilled from OpenAI's official gpt-image-2 guide.

Output is **prompt text only** (v1). Report the recommended `size` and `quality` in the
assumptions line so the user can plug them into whatever tool they use.

---

## Parameters reference

**quality:** `low` | `medium` | `high`
- `high` — dense/small in-image text, infographics, close-up portraits, multi-font layouts,
  identity-sensitive work, anything shipped without review. **Default for text-heavy work.**
- `medium` — good general default for photos/ads/illustration.
- `low` — speed/volume/ideation; often enough, much faster.

`input_fidelity` does not apply to gpt-image-2 (output is high-fidelity by default).

**size constraints (any resolution that satisfies ALL):**
- max edge < 3840px
- both edges a multiple of 16
- long:short ratio ≤ 3:1
- 655,360 ≤ total pixels ≤ 8,294,400
- above 2560×1440 (2K) is **experimental** — results more variable.

**aspect → size map** (use these defaults):

| Aspect / use | size | Note |
|---|---|---|
| Square | `1024x1024` | general-purpose default |
| Portrait / poster (2:3) | `1024x1536` | standard portrait |
| Landscape / hero (3:2) | `1536x1024` | standard landscape |
| Widescreen 16:9 | `1536x864` | decks, game screenshots |
| Mobile 9:16 | `864x1536` | ratio 1.78, both ×16 ✓ |
| Premium wide 2K | `2560x1440` | reliability upper boundary |
| 4K UHD | `3824x2144` | experimental; rounded under the <3840 rule |

If the user asks for an aspect not in the map, compute the nearest size where both edges
are multiples of 16 and the ratio is ≤ 3:1.

---

## Prompting rules (baked in)

1. **Structure order:** background/scene → subject → key details → constraints. For complex
   requests use **short labeled segments / line breaks**, not one long paragraph.
2. **Intended use** up front (ad / UI mock / infographic / poster) — sets mode + polish.
3. **Specificity:** concrete materials, shapes, textures, and the visual medium (photo /
   watercolor / 3D render). Add quality levers only when needed (film grain, macro detail).
4. **Photorealism:** include the literal word **"photorealistic"** (or "real photograph",
   "professional photography", "35mm film"). Camera specs are interpreted loosely — use for
   look/composition, not exact simulation.
5. **Composition:** call out framing, viewpoint, perspective, lighting/mood, and explicit
   placement ("logo top-right", "subject centered with negative space on the left").
6. **People:** describe scale, body framing, gaze, and object interaction ("full body, feet
   included", "looking down at the book, not the camera", "hands gripping the handlebars").
7. **Text in images:** put literal copy in **quotes** or ALL CAPS; specify font style, size,
   color, placement. Spell tricky/brand words letter-by-letter. Use `quality: high` for
   small/dense text. Render each string **once, verbatim**.
8. **Constraints block (always include):** "no watermark, no logos or trademarks, original
   design". For a specific brand mark, say "generic / original, not resembling any real brand".
9. **Iterate, don't overload:** the prompt should be rich but clean; edits are single-change
   follow-ups ("make the lighting warmer", "remove the extra sticker") — mention this to the
   user if they want to refine.

---

## Output template

Assemble labeled sections in this order. Omit sections that don't apply to the archetype
(e.g. TYPOGRAPHY for a candid photo; HUD only for game screenshots).

```
[Concept line — format + medium + fictional brand + reference aesthetic + intended use.]

BACKGROUND / CANVAS:
[aspect ratio, background treatment with hex, global texture]

SUBJECT:
[granular hero detail; IP-safe; real-texture cues if photoreal]

LAYOUT / COMPOSITION:
[named zones top→bottom, each with position + size% + tilt + content]

TYPOGRAPHY & TEXT:
[each text element: "LITERAL COPY" + named font + weight/tracking/case + hex + placement]

PALETTE:
[4-6 hex codes, each mapped to an element]

MOOD:
[adjective cluster + era/reference anchor]

FINISH:
[post-processing + authority/quality tag]

CONSTRAINTS:
Original design, no logos or trademarks, no watermark. Render each text string once, exactly
as written. [+ any preserve/exclude notes]
```

For **photoreal scene / game screenshot**, swap LAYOUT/TYPOGRAPHY/PALETTE for the labeled
technical blocks: `SCENE:` `SUBJECT:` `ACTION:` `LIGHTING:` `CAMERA:` `HUD:` `TECHNICAL:`
(see `anatomy.md`, photoreal variant).

---

## Quality/size selection heuristic

1. Map the archetype's default aspect → `size` (table above); override if the user gave an
   aspect.
2. `quality`: `high` if the image has dense/small text, is an infographic, a close-up
   portrait, or a poster with heavy typography; else `medium`; `low` only if the user wants
   speed/drafts.
3. State both in the assumptions line, e.g. `size=1024x1536 · quality=high`.
