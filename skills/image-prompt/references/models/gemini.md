# Model adapter — Gemini / Nano Banana Pro (Gemini 3 Pro Image)

Google's flagship image model (GA ~mid-2026; verify). Codename **Nano Banana Pro**, API name **Gemini 3
Pro Image**. Best-in-class legible in-image **text**, up to **4K**, and **Google Search
grounding** for factual infographics/diagrams — the top pick for text-heavy and data-accurate
work. Output is prompt text only (report config in the assumptions line).

## Prompt style

- **Describe the scene in rich prose, not keyword lists** — "the more specific, the more
  control". Inherits Gemini best-practices: hyper-specificity, state the **intent/purpose**,
  explicit **camera + lighting** language, and **positive phrasing** (say what you want, not
  "no X").
- It **reasons before rendering** (thinking) — give intent and let it plan layout; great for
  infographics, diagrams, and structured, layout-heavy assets.

## Capabilities

- **Text rendering** — state-of-the-art, multilingual, long/multi-line, varied fonts. Main
  reason to pick it.
- **Up to 4K**; **Search grounding** for accurate charts/diagrams/maps-style visuals;
  **up to 14 reference images** = 6 hi-fi object shots + 5 character images + 3 style refs;
  **subject consistency for up to 5 people**; localized editing/relight/reframe.

## Aspect ratio / resolution

- **Aspect ratios (10):** `1:1 2:3 3:2 3:4 4:3 4:5 5:4 9:16 16:9 21:9`.
- **Resolution tiers:** `512px`, `1K` (~1MP), `2K` (~4MP), `4K` (~16MP). **Uppercase K
  required** (`"1k"` is rejected). Default `1K`. Use `2K`/`4K` for posters/print/dense text.
- Every output carries an invisible **SynthID** watermark.

## Text in images

Put literal copy **in quotes** and describe the font **descriptively** (not by name):
`the headline "GRAND OPENING" in a clean bold sans-serif`. Specify hierarchy + layout + colour.
Reliable for posters, infographics, diagrams, multi-line and multilingual; very small text can
still degrade.

## Grounding (factual visuals)

For infographics/diagrams that must be factually correct, enable the **`google_search`** tool
so it pulls live facts. (Note: Maps grounding not supported; image search results excluded.)

## Editing & references

Change-only phrasing: "Change only the [element] … keep everything else exactly the same."
Use the reference budget deliberately (object refs for product fidelity, character refs for
consistency, style refs for look). Supports background swap, relight, day-to-night, DoF, colour
grade, camera-angle change, aspect reframe, and in-image text/language edits.

## Params / API

- **Model id:** `gemini-3-pro-image-preview` → `gemini-3-pro-image` (GA). Gemini API / AI
  Studio / Vertex AI.
- **Config:** `aspect_ratio` + resolution (`image_size` / `resolution` — value strings
  `"512px" | "1K" | "2K" | "4K"`); `thinking_level` (default `minimal`; `high` for complex
  layouts); add the `google_search` tool for grounding.
- **Pricing:** ~$0.134 / image at 1K–2K, ~$0.24 at 4K (Batch ≈ half). No free tier.

## Output template

```
[Intent + format]: A [poster / infographic / product shot / editorial scene] for [purpose].
[Scene, rich prose]: [subject + appearance], [setting], [composition & placement], [mood].
[Camera & light]: [angle], [lens], [depth of field], [lighting], [colour grade].
[Text, quoted]: Render "[EXACT HEADLINE]" in a [descriptive font]; "[subtext]" in [font]. [layout/hierarchy].
[Style]: [art direction, palette (hex if brand), texture, finish].
[If editing]: Change only [X]; keep everything else exactly the same.
[If factual]: use accurate current data for [topic].   (enable google_search)
```
Report in assumptions: `model=gemini-3-pro-image · aspect_ratio=<…> · resolution=<1K|2K|4K> · thinking=<minimal|high>`.

## Lighter siblings

- **Nano Banana 2 (Gemini 3.1 Flash Image)** — cheaper/high-volume; 1K/2K GA, 4K preview.
- **Gemini 2.5 Flash Image** (original "Nano Banana", 2025) — ~1024px class, weaker text, no
  thinking/grounding. Use for low-latency/cheap; drop to describe-the-scene prose, quotes for
  text, `image_config.aspect_ratio` from the same ratio set.

## Sources
blog.google (Nano Banana Pro announcement + developer post), deepmind.google/models/gemini-image/pro, ai.google.dev/gemini-api/docs (image-generation, models/gemini-3-pro-image), cloud.google.com (GA post May 2026), Vertex AI docs. Uncertain: exact resolution field name across SDKs; max images/call; extended cinematic ratios beyond the 10.
