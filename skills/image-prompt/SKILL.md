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
   If the user names a saved style ("in the <name> style", "use preset <name>") or asks to
   save one ("save this style as <name>"), handle it via **Style presets** below. If the user
   wants help choosing a look ("help me with the style", "what styles can you do", "в каких
   стилях можешь"), present the **Style menu** below. If the user supplies an existing image to
   transform, composite, restyle, localize, or place someone/something into — or wants a
   poster/ad built around a supplied person or product — that is an EDIT: use **Edit / remix
   mode** below.

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

Default target: **gpt-image-2**. When the user names a model, load its adapter and follow it —
the 9-block content stays the same; only the rendering (output shape, params/flags, size/ratio)
changes.

| Model (match loosely, incl. RU) | Adapter |
|---|---|
| gpt-image-2 (default), gpt-image-1, gpt-image-1.5, "openai" | `references/models/gpt-image-2.md` |
| nano banana pro, gemini 3 pro image, "gemini", "нанобанана" | `references/models/gemini.md` |
| midjourney, "mj", "миджорни" | `references/models/midjourney.md` |
| flux, flux.2 | `references/models/flux.md` |
| ideogram | `references/models/ideogram.md` |
| recraft | `references/models/recraft.md` |
| reve | `references/models/reve.md` |
| universal / unknown tool | `references/models/universal.md` |

If the user names a model with no adapter yet, use `universal` and say so. **Pick by fit** when
the user is unsure: text-heavy / infographic / factual → **gemini (Nano Banana Pro)** or
gpt-image-2; brand / typography / vector / logo → **recraft**; pure aesthetics → **midjourney**;
open-weight / local / hex control → **flux**; strong prompt-adherence + layout editing →
**reve**; unknown tool or "just a great prompt" → **universal**.

## Style presets (user-local, private)

Presets are saved **styles** (never content) the user has dialed in, stored per-user at
`~/.claude/image-prompt/presets/<name>.md` — NOT in this repo, never committed, private to
the machine. Create the directory on first save. Each user grows their own set.

- **Save** — on "save this style as <name>" / "запомни этот стиль как …": distill ONLY the
  style layer (never subject, copy, or specific zones). Capture the **distinctive signatures
  that make the style non-generic** — palette + fonts alone flatten the output. Nail:
  **MEDIUM/technique** (watercolor vs flat vector vs risograph vs 3D render vs photo), **how
  and WHERE fills are painted** (flat vs mottled/grainy; applied globally vs confined to
  specific accent elements — apply a texture where the reference uses it, not everywhere),
  **LINE quality** (loose/varied vs clean/even),
  **COMPOSITION rhythm** (sparse/airy vs dense; organic vs grid; negative space), and an
  explicit **AVOID** list of anti-patterns that would drift toward a generic look. When
  deriving from reference images, name the 2-3 traits that separate this style from a generic
  version and encode them; if refs are available, sanity-check the intended output against
  them. A big AI-tell is the model's own default "polished illustration" look — soft digital
  watercolor gradients, airbrushed bleed, over-clean vector lines, glossy 3D; name these in
  AVOID and prefer flat color + real (grain/halftone/print) texture + restraint. Do NOT
  over-stack texture adjectives, which can trigger that exact generic look. Write the file
  (format below), then confirm what was captured.
- **Use** — on "in the <name> style" / "use preset <name>": read the preset, build the
  CONTENT from the new idea as usual, but take background/texture, palette, fonts, motifs,
  mood, and finish from the preset (overriding the archetype's style defaults). Keep the
  preset's `model`. If no preset by that name exists, say so and list what's available.
- **Manage** — "list my presets" (read the dir), "update <name>", "delete <name>".

Preset file format:

```md
---
name: <kebab-name>
description: <one line>
suits: [poster, landing-hero, illustration, ...]
model: gpt-image-2
---
MEDIUM: <what it physically is + technique — watercolor illustration / flat vector / risograph / 3D render / photo>
BACKGROUND: <bg + global texture, with hex>
PALETTE: <hex codes + HOW fills are painted (flat? mottled watercolor? grain showing through?)>
LINE: <stroke quality if line-based — loose/varied vs clean/even> (omit if not line-art)
FONTS: <named fonts + roles + effects>
MOTIFS: <signature graphic devices>
COMPOSITION: <density & rhythm — sparse/airy vs dense; organic vs grid; negative space>
MOOD: <adjective cluster>
FINISH: <texture / post-processing>
AVOID: <anti-patterns that would drift toward a generic look>
CONSTRAINTS: <IP-safety etc.>
```
Older presets may omit MEDIUM / LINE / COMPOSITION / AVOID — add them when updating a preset
that renders too "generic".

### Sharing presets (preset codes)

Presets are portable: export one to a self-contained **code** anyone can import — no hosting,
no accounts. Format: `imgpreset:v1:<b64>` where `<b64>` is base64 of gzip of the preset file's
UTF-8 bytes (verified round-trip).

- **Export** — on "export preset <name>": encode `~/.claude/image-prompt/presets/<name>.md`
  and print the code in its own copy block. Reference command (P = the preset path):
  `python3 -c "import gzip,base64;print('imgpreset:v1:'+base64.b64encode(gzip.compress(open('$P','rb').read())).decode())"`
  Any equivalent gzip+base64 tool works; keep the `imgpreset:v1:` prefix. Also try to copy the
  code straight to the system clipboard when a tool is present (`pbcopy` on macOS,
  `wl-copy` or `xclip -selection clipboard` on Linux) and tell the user it's copied — but
  always print the block too, so Claude Code's built-in copy works as a fallback.
- **Import** — on "import preset `imgpreset:v1:…`": decode the payload after the prefix, gunzip
  it, read `name:` from the decoded frontmatter, and write `presets/<name>.md`. Confirm what
  landed; if a preset with that name already exists, ask before overwriting. Reference command
  (OUT = target path, C = the code):
  `python3 -c "import sys,gzip,base64;open('$OUT','wb').write(gzip.decompress(base64.b64decode('$C'.split(':',2)[2])))"`
- **Validate** after import: the decoded file must start with `---` frontmatter and contain a
  `name:` line. Reject anything that doesn't decode to a valid preset.

### Reference-library presets

A preset can also be a **reference library** (`type: reference-library` in its frontmatter):
instead of one style it holds many distilled reference cards plus a pointer to source images
(e.g. `~/.claude/image-prompt/references/<name>/`). When the user invokes it ("use my ui
references", "по моей ui-базе"): read the cards, **propose the 2-3 that best fit the project**
(the user can swap or add — offer, don't lock), then compose the mockup from those, favouring
what fits the project over any single house style. To ingest new screenshots dropped into the
source folder: view each image, append a card (template inside the library file), and refresh
the aggregated-patterns summary. Libraries are user-local and private — never committed.

## Style menu (help me choose a look)

When the user knows the deliverable but wants help with the style ("help me with the style",
"what styles can you do", "в каких стилях можешь"), present the built-in repertoire from
`references/styles.md`: show **names + one-line vibes, grouped**, and offer the user's own
private presets alongside. Let them pick one or combine two, then build using that style's
spec (it fills the style layer; content comes from the idea). Offer to save the result as a
preset. Keep the on-screen menu short — pull a style's full spec only once it's chosen.

## Edit / remix mode

When the user gives an existing image (or refers to one) and wants to transform / composite /
restyle / localize it, or build a poster/ad around a supplied person or product, this is an
**edit**, not a generate. Follow `references/edit-remix.md`: pick the matching workflow and
build the prompt with the change-vs-preserve framing (state what changes, list the invariants,
repeat them), reference each input image by index + role, and set params (`input_fidelity=high`,
`background=opaque` for product extraction, quality/size to fit). Use the edit template in that
file. Still prompt-only — the user attaches the image(s) in their tool.

## Generate (optional, opt-in)

The skill is prompt-only by default. If the user **explicitly asks to generate/render** the
image AND a provider API key is in the environment, you may run the optional generate step via
`scripts/generate.py` — see `references/generation.md`. **Confirm first** that it's a paid
API call, then write the prompt to a temp file and run the script, save the PNG into the
project, and view it to check. Never generate without an explicit request and a present key;
otherwise just deliver the prompt. Midjourney has no API — prompt only.

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
