# Model adapter — FLUX (Black Forest Labs, FLUX.2 family)

How to render the 9-block content as a FLUX prompt. FLUX wants **flowing natural-language
prose** — flatten the content into a descriptive paragraph (JSON is only an internal scaffold,
see below). Output is prompt text only.

## Rules

- **Prose, not keywords.** Write like describing a scene to a person.
- **Specificity** drives quality — concrete attributes (age, material, texture, mood).
- **Composition order:** `[Subject] + [Action/Pose] + [Style/Medium] + [Setting] + [Lighting]
  + [Camera/Technical] + [Colors]`. A useful start, not a strict formula.
- **Front-load** the subject (and any quoted text) — earlier words weigh more.
- **Lighting is the highest-impact lever** — always specify (golden hour, Rembrandt,
  volumetric fog, low-key chiaroscuro, studio softbox…).
- **NO negative prompts** — FLUX has none; negation makes it focus on the unwanted thing.
  Replace "no X" with the positive alternative (no people → "deserted"; no text → "clean,
  unmarked"; no blur → "tack-sharp").
- **Length:** ~30–80 words is the sweet spot (hard cap 512 tokens). English is most precise.

## Text & typography

- Quote exact text: `a poster with "HELLO WORLD" in bold letters`. Unquoted = description.
- Specify font class (sans/serif/script/display/mono), often with a reference ("bold geometric
  sans-serif similar to Futura"); give size hierarchy + placement; front-load for accuracy.
- Keep strings short (1–4 words most reliable). Use **FLUX.2 [flex]** for best text.

## Hex color control (supported)

- **Always pair hex with a color name:** `#FF6B6B (coral pink)` — never bare hex.
- Bind each color to an object; **limit to 3–5 colors**; gradients ok
  (`from #02EB3C to #EDFA3C`). Anti-bleed: `the LEFT chair in #…`, `maintaining exact color #…`.

## Model variants (FLUX.2)

`[klein]` fastest/high-volume (open, ≤4 refs, no prompt upsampling) · `[pro]` balanced default
(≤8 refs) · `[flex]` best for typography/posters/UI (exposes `steps` 1–50, `guidance` 1.5–10)
· `[max]` highest quality + real-time **grounding search** (≤8 refs). FLUX.1 legacy: Kontext =
editing, Fill = inpainting — use only when asked. **In FLUX.2 editing = T2I + reference images
(no separate edit model).**

## Editing & multi-reference

Pass source image(s) via `input_image`, `input_image_2`, … (URLs preferred). Phrase edits as
imperatives + explicit preserve list: `Change the background to a beach while keeping the
subject's pose, clothing, and expression exactly the same, maintaining the photo's realistic
style and color grading.` Multi-ref: assign each image a role by index ("face from image 1,
outfit from image 3, environment from image 5"). Break dramatic edits into sequential steps.

## Aspect ratios / resolution

Named: `1:1 16:9 9:16 4:3 3:2 21:9`; FLUX.2 also custom `width`/`height` (commonly ≤2048/side),
output up to ~4MP; editing input capped ~9MP total (pro API).

## JSON scaffold (optional)

For complex/multi-subject scenes, BFL suggests organising with a JSON object
(`scene / subjects[] / style / technical / colors`) — but **flatten it to flowing prose before
sending**. Keep JSON only as an internal or companion artifact.

## Output template (prose)

```
<subject + key attributes>, <action/pose>, <style/medium>, in <setting>.
<lighting>. <camera body + lens + aperture / film stock>. <composition>.
[palette: #HEX (name), #HEX (name)]. [quoted "TEXT" + font + placement].
```

**Report in assumptions:** `model=flux.2-<pro|flex|klein|max> · <WxH or aspect>`.

## Sources
docs.bfl.ml/guides/* and docs.bfl.ml/flux_2/*; official BFL Claude Code skill github.com/black-forest-labs/skills (`flux-best-practices`). Uncertain: exact per-model pixel bounds / whether enum vs raw width-height — defer to /api-reference.
