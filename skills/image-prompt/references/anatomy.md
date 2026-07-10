# Anatomy of a great prompt — the 9-block skeleton

Every high-quality prompt in the gold set is built from the same nine blocks, in
roughly this order. You fill these blocks *internally* first (model-agnostic), then
hand them to a model adapter (e.g. `models/gpt-image-2.md`) for final formatting.

The single biggest quality lever is **Block 3 (Composition zones)**: naming spatial
regions and describing each one's position, size, tilt, and content. Generic prompts
skip this; great prompts never do.

---

## Block 1 — Concept line (one sentence)

State, in order: **format** (vertical/horizontal + ratio) · **medium** (poster / landing
hero / editorial spread / ad / UI mockup / game screenshot / logo / illustration) ·
**subject or brand** · **reference aesthetic** · **intended use**.

The intended use sets the model's "mode" and polish level — always include it.

> "Vertical mobile-first landing page for a fictional streetwear brand called 'LOUD KIDS
> CLUB'. Full-page poster-as-landing aesthetic in the spirit of Y2K skate-surf streetwear."

> "Horizontal desktop landing page hero for a fictional homeware store 'kiln & co.'.
> Minimalist editorial layout with whimsical character-driven ceramic renders."

Rules:
- Brand names are always **fictional / placeholder** — invent one if the user didn't give one.
- Name a **reference aesthetic** (an era, a movement, or 2-3 reference brands): "Y2K
  skate-surf", "Cereal/Kinfolk editorial", "1977 London punk silkscreen", "Sega Dreamcast
  Y2K UI", "God of War + Ghost of Tsushima fidelity".

## Block 2 — Canvas & background

- **Aspect ratio**, stated explicitly (9:16, 3:4, 2:3, 4:3, 16:9, 1:1).
- **Background treatment** with hex: gradient ("deep royal-blue #2E5BAC fading to navy
  #1A2D4F"), warm paper cream, solid saturated block, aqua-cyan grid, snow-white→icy-blue.
- **Global texture**: film grain, halftone dots, subtle vignette, CRT scanlines + glow,
  paper grain, screen-print noise, drifting particles. Pick what matches the aesthetic.

## Block 3 — Composition zones (the spine)

Break the canvas into **named regions**, top to bottom. For each region give:
**position** ("top banner", "top-right corner", "center, fills ~60% of vertical space",
"lower-left below the wordmark") · **size** (rough %) · **tilt/angle** where playful
("tilted 35°", "slightly misaligned") · **content + styling**.

Typical region set for a poster/landing:
- Top banner / nav (intro line, wordmark, or nav links)
- Hero (dominant photo / character / render — usually 50-70% of area)
- Overlays (stickers, badges, floating UI panels — with position + tilt each)
- Content block (headline, body copy, CTA)
- Footer strip (thin full-width meta line: brand · est. date · url · tagline)

> "Three yellow star stickers floating over the photo at playful angles; left sticker
> (middle-left) tilted left with a lollipop clipping inside; right sticker (middle-right)
> tilted right with the blob face inside; each has a white vinyl border + soft cast shadow."

Depth cues that repeat across the gold set: white vinyl sticker edge, tape corner, soft
cast shadow beneath floating elements, chrome bevel, glossy panel frame.

## Block 4 — Subject detail

For the hero subject (person / product / creature / scene), be granular:
- **Person:** clothing (each item), expression, gaze direction, pose, hands/props,
  lighting on skin, hair. "gazing slightly upward, casual cool expression, holds a red
  lollipop at mouth-level, slight motion blur in one hand."
- **Product:** material, glaze/finish, geometry, painted details, how it floats/sits +
  cast shadow.
- **Creature/scene:** anatomy, texture, action beat, breath vapor, environment detail.

**IP-safety, always:** describe brand-like glyphs as "generic / original, NOT resembling
[any real brand]". For photoreal people, add real-texture cues (pores, chapped lips,
frost on eyebrows) to escape the plastic-AI look.

## Block 5 — Typography & text

For **each** text element on the canvas:
- **Literal copy in quotes** (this is what gets rendered — write the actual words).
- **Font style** + a **named real font reference** (see `fonts-palettes.md`).
- **Weight · tracking · case · color (hex) · effects · placement.**

> Wordmark: massive chunky slab-serif (like Bungee Slab), vivid marigold #F4C542, thick 3D
> bevel shadow in #C98A1E, tightly tracked, slightly tilted, chrome highlight on top edges,
> reads "BOOM".
> Body: 4 lines small italic serif (Tiempos Text / Garamond Italic), cream #F5EFE3.

Naming a real font family is the strongest style anchor available — use it every time, EXCEPT
for models that can't consume font names (Gemini, Ideogram, Recraft): there, describe the font
by trait (weight, contrast, era) instead, per the model adapter.

## Block 6 — Palette

An explicit **hex list, each color mapped to an element**. 4-6 colors. This makes the
image cohesive and controllable.

> royal-blue→navy gradient (#2E5BAC → #1A2D4F), marigold #F4C542, shadow #C98A1E, cream
> #F5EFE3, charcoal linework #1A1A1A, lollipop red #D44A3A, natural skin tones.

## Block 7 — Typography summary

Restate the fonts as a role map (helps the model keep hierarchy consistent):

> "massive chunky slab-serif for wordmark, bold condensed uppercase sans for labels,
> italic serif for body copy, hand-drawn playful lettering for the brand glyph."

## Block 8 — Mood

A tight **adjective cluster** (3-6 words) + era/reference anchors.

> "playful, irreverent, Gen-Z youth-coded, Y2K skate-surf-streetwear, confident, fun."

## Block 9 — Finish / texture + quality tag

- **Finish:** the post-processing — "subtle film grain, slight CRT-warmth, sticker
  drop-shadows, vintage screen-print feel."
- **Quality/authority tag:** "Awwwards / Behance-quality streetwear landing page, 4k
  vertical." (Model-specific alternatives: Midjourney flags `--ar 4:3 --style raw --v 7`;
  engine tags "Unreal Engine 5.3, Lumen GI, Nanite, path-traced, 4K".)

---

## Photoreal / rendered-scene variant

For candid-photo and game-screenshot archetypes, replace blocks 3/5/6/7 with **labeled
technical blocks** (comma-separated fragments work well here):

- **SCENE** — environment, era, weather, ground detail, atmosphere.
- **SUBJECT(S)** — character/creature with anatomy, wardrobe, micro-detail, pose/action.
- **COMBAT/ACTION MOMENT** (if any) — the frozen beat, physics, motion blur.
- **LIGHTING** — source, color temperature (e.g. 6500K), GI, tone mapping (ACES filmic),
  what to avoid (no bloom / no god rays / no lens flare).
- **CAMERA** — angle, framing (anamorphic 2.39:1), depth of field (f/2.8), bokeh.
- **HUD** (game only) — corner-by-corner UI: health/stamina, boss bar, minimap, item slots,
  button prompts, quest text.
- **TECHNICAL** — engine, GI system, geometry, resolution, grain, chromatic aberration,
  fidelity references.

Still keep Block 1 (concept line) and Block 4 discipline (real texture, IP-safety).

---

## Build checklist

- [ ] Concept line names format, medium, fictional brand, reference aesthetic, intended use
- [ ] Aspect ratio stated; background has hex + a global texture
- [ ] Composition broken into named zones with position + size% (+ tilt where playful)
- [ ] Hero subject granular; IP-safety + real-texture cues where relevant
- [ ] Every text element: literal copy in quotes + named font + color hex + placement
- [ ] Palette = 4-6 hex codes, each mapped to an element
- [ ] Mood adjective cluster + era/reference anchor
- [ ] Finish line + quality/authority tag
- [ ] (gpt-image-2) CONSTRAINTS block + recommended size + quality
