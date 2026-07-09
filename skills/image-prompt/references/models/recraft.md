# Model adapter — Recraft (V4 Pro)

Design-first model built for **typography, brand accuracy, and production assets** (posters,
logos, icons, UI, mockups) — and the only one with **editable SVG** output. Ideal for our
poster/UI/brand niche. Output is prompt text only (report settings in assumptions).

## Prompt style

Recraft rewards **structure**, not verbosity:
- **Short prompt → interpretive mode** (model makes aesthetic calls — good for exploration).
- **Long/structured prompt → architectural control** (model executes your art direction —
  intentional, repeatable). Official: *"Short → model designs with you; long → model executes
  your architecture."*
- **Layered brief, global → local:** concept/subjects → background/environment → subject
  framing/pose → attributes → secondary elements + spatial relationships → lighting →
  camera/depth/contrast → mood. Define grid/margins/relationships and Recraft builds the layout
  (not random placement). For photo+graphic hybrids: describe each visual language, then how
  they interact.

## Text & typography (its edge)

- **Quote every literal string** — unquoted words are scene description, not rendered text.
- **Define the typographic *system*, not just the phrase:** format (menu/editorial/poster),
  headline size + placement, secondary hierarchy, body, colour-blocking, surface. Text is a
  structural element integrated into the composition (correct kerning/tracking), not overlaid.
- **Cannot name a font** — describe by trait ("expressive high-fashion sans-serif with
  sculptural clean letterforms", "chunky grotesque wordmark").
- Strength = headlines/labels/signage/menus; dense body copy is weaker.

## Styles

- **`style_id` (custom trained styles) is NOT supported on V4** — only V3 / V3-Vector. **Do not
  emit `style_id` for a V4 target** (biggest gotcha). Steer via prompt + base `style`/`substyle`.
- **Base `style`:** `realistic_image` (default), `digital_illustration`, `vector_illustration`,
  `icon`, `logo_raster`, `any` (i2i). Each has substyles (`b_and_w`, `enterprise`,
  `natural_light`, `studio_portrait`, `hdr`, `hand_drawn`, `pixel_art`, `grain`, …).
- Brand-locked custom styles today ⇒ a **V3** pipeline (train-a-style from up to 5 reference
  images → `style_id`), not V4.

## Colour / brand control

- API `controls.colors`: `[{"rgb":[R,G,B]}]` (0–255) — **exact brand palette enforcement**
  (convert hex → RGB). `controls.background_color`: single `{"rgb":[…]}`. `controls.no_text`:
  suppress unwanted text. In prose, use strict palette / "flat colours only" for brand work.

## Sizes

Explicit size **strings** (not ratio keywords). V4 Pro renders at up to **2048px / ~4MP**:
`1024x1024, 1536x1024, 1024x1536, 2048x1024, 1024x2048, 1365x1024, 1024x1365, 1820x1024,
1024x1820, 1280x1024, 1024x1280, …` (covers 1:1, 4:3/3:4, 3:2/2:3, ~16:9/9:16). For logos/icons
use the **Vector / Vector Pro** variants → true editable SVG; instruct "no gradients, no
shadows" for clean output.

## Editing

image-to-image (`style:"any"`), inpainting/generative fill (mask), background removal,
vectorize (raster→SVG), replace background, upscale, mockup. Reference edit = input image +
prompt.

## Params / API

`generateImage` on `external.api.recraft.ai/v1`. Key: `prompt`, `model` (V4 family; **verify
exact string against the live OpenAPI — likely `recraftv4`**), `style`+`substyle` (or `style_id`
only on V3, mutually exclusive with `style`), `size` (string above), `n` 1–6,
`controls.colors` / `background_color` / `artistic_level` (0–5) / `no_text`, and `text`+`bbox`
(precise text placement, relative 0–1 coords). ~$0.25/image at V4 Pro (varies by provider).

## Output template

```
[FORMAT & INTENT] — e.g. "Vertical A2 event poster, print-ready."
[BACKGROUND LAYER] — base field, texture/flat, grid & margins.
[GRAPHIC/SUBJECT LAYER] — main visual, framing, style logic (vector/logo: "flat, no gradients, no shadows").
[TYPOGRAPHY SYSTEM] — Headline "EXACT" (oversized, top-third, <font-trait>); Subhead "EXACT"; Label "EXACT"; strong size contrast, integrated not overlaid.
[COLOUR SYSTEM] — strict palette (navy #0A1F44, coral #FF6B5C, cream #F7F3E9), flat blocking → enforce via controls.colors (hex→RGB).
[LIGHTING/DEPTH] — only if raster/photo layer.
[MOOD & RESOLUTION] — one line tying layers together.
```
Report: `model=recraftv4(Pro) · style/substyle · size=<WxH> · controls.colors=<brand RGB>`.

## Sources
recraft.ai/docs (prompt-engineering-guide/prompting-with-recraft-v4, api-reference/styles, getting-started), recraft.ai/blog (V4 launch, prompt guide, style creation), runware/fal gateway docs. Uncertain: exact V4 API `model` string; `text`+`bbox` behaviour on V4 specifically; whether any V4 tier has begun supporting `style_id` (as of docs read, no).
