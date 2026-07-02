# image-prompt skill — design spec

**Date:** 2026-07-02
**Status:** approved, building v1

## Goal

A Claude Code skill: user throws a short idea, the skill auto-builds one
production-grade image-generation prompt following the proven layered-composition
pattern extracted from a corpus of high-quality reference prompts. Output is a
single clean, copy-paste-ready prompt (press `c` to copy) — no code, no API calls.

## Decisions (from brainstorming)

- **Output:** prompt text only. One clean copyable block + a short "assumptions/knobs"
  line so the user can redirect in one sentence. No runnable snippet, no auto-generation.
- **Default model:** `gpt-image-2`. Launch supports gpt-image-2 only.
- **Extensible:** adding a model later = adding one file under `references/models/`;
  the core builder is model-agnostic.
- **Auto-first:** infer archetype + defaults from the idea; do not interrogate.
  Ask at most one question only when genuinely ambiguous.

## The extracted pattern (9-block skeleton)

1. **Concept line** — format + medium + subject/brand + reference aesthetic + intended use.
2. **Canvas & background** — aspect ratio + background treatment (with hex) + global texture.
3. **Composition zones** — named regions with position + size% + tilt + content. The spine.
4. **Subject detail** — granular attributes; IP-safe "generic/original".
5. **Typography & text** — literal copy in quotes; per element: font style + named font
   reference + weight + tracking + case + color + effects + placement.
6. **Palette** — explicit hex list, each mapped to an element.
7. **Typography summary** — fonts mapped to roles.
8. **Mood** — adjective cluster + reference brands/eras.
9. **Finish / texture + quality tag** — post-processing + authority tag.

For gpt-image-2, also fold in a **CONSTRAINTS** block (no logos/trademarks/watermark,
original design, verbatim text) plus recommended `size` and `quality`.

## Two archetype families

- **Graphic design** (poster / landing-hero / editorial / product-ad / ui-mockup / logo /
  illustration): typography- and layout-heavy; all 9 blocks matter.
- **Photoreal / rendered scene** (candid photo / game-screenshot): labeled blocks
  (SCENE / SUBJECT / LIGHTING / CAMERA / [HUD] / TECHNICAL); palette/typography secondary.

## Architecture

```
idea → detect archetype → expand to 9-block content (model-agnostic)
     → model adapter (gpt-image-2: labeled sections + size/quality + text/IP rules)
     → output: one copyable prompt block + assumptions line
```

## Files

```
imagegen-skills/                         (remote: git@github.com:veryCoolTimo/imagegen-skills.git)
├── README.md                            # what it is + install (symlink into ~/.claude/skills)
└── skills/image-prompt/
    ├── SKILL.md                         # trigger + workflow + pointers + output format
    └── references/
        ├── anatomy.md                   # the 9-block skeleton, in depth
        ├── archetypes.md                # templates + default aspect/quality per archetype
        ├── fonts-palettes.md            # font library by vibe + hex palette discipline + ready palettes
        ├── gold-examples.md             # curated reference prompts (grows over time)
        └── models/gpt-image-2.md        # full gpt-image-2 guide distilled into build rules
```

## gpt-image-2 rules baked in (from official guide)

- Structure order: background/scene → subject → key details → constraints; labeled
  segments for complex requests.
- Include intended use to set mode + polish.
- Photorealism: include the word "photorealistic".
- Text in image: literal text in quotes / ALL CAPS; font/size/color/placement; spell
  tricky words letter-by-letter.
- Constraints: no watermark/logos/trademarks; original; verbatim text once.
- `quality`: high for dense text / small text / portraits / infographics; medium default;
  low for speed/batch.
- `size` constraints: max edge < 3840, both edges multiple of 16, long:short ratio ≤ 3:1,
  655,360 ≤ total pixels ≤ 8,294,400; >2560×1440 is experimental.
- aspect→size map: poster 1024×1536, landing/16:9 1536×864, mobile 9:16 864×1536,
  square 1024×1024, premium-wide 2560×1440, 4K→3824×2144 (experimental).

## Non-goals (v1)

- No API calls / image generation / edits execution.
- No models beyond gpt-image-2 (universal / Midjourney / Gemini / Ideogram come later as files).

## Success test

User gives a one-line idea from any covered archetype; skill returns a prompt of
gold-example quality with correct size/quality and a one-line assumptions note.
