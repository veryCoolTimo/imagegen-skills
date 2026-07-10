# Model adapter — Midjourney (V7 / V8.1)

How to render the 9-block content as a Midjourney prompt. Unlike gpt-image-2, Midjourney does
NOT take labeled sections — **flatten the content into one descriptive prose line, then append
`--flags`**. Output is prompt text only.

Target V7 by default (V8.1 is the 2026 default model; note differences below).

## Prompt shape

```
[image URL(s)]  <one flowing descriptive sentence-style prompt>  --flags
```
- Optional image prompt URLs go **first**; reference systems (`--sref`, `--oref`) are flags.
- Descriptive prose in the middle: **coherent sentences, not keyword-soup** (V7 penalises tag
  lists). Front-load the subject; then setting, lighting/atmosphere, medium/lens/finish.
- All `--flags` at the very end, space-separated (no commas).

## Rules

- **No booster tags.** Drop "8k, masterpiece, ultra-detailed, beautiful" — they add noise in
  V7. Control finish with real craft language (film stock, lens, lighting) + flags.
- **Text in images:** wrap literal words in double quotes, keep short (1–4 words), e.g.
  `a neon sign that reads "OPEN"`. Long/small text garbles.
- **Multi-prompt weights:** `concept A:: concept B::2` weights parts; sum must stay positive.

## Parameters (emit in this order)

| Flag | Values / default | Use |
|---|---|---|
| `--ar W:H` | whole numbers, def `1:1` | aspect ratio |
| `--v` | `7`, `8.1`, `niji 7` | model version (`--niji 7` = anime) |
| `--style raw` | flag | literal, less MJ "beautifying"; pair with low `--s` |
| `--s` / `--stylize` | 0–1000 (def 100) | artistic license amount |
| `--c` / `--chaos` | 0–100 (def 0) | variety across the 4 grid images |
| `--w` / `--weird` | 0–3000 | offbeat aesthetics |
| `--no` | text list | negative prompt (exclude) |
| `--sref` | code / URL / `random` | **style reference** (aesthetic, not content); `--sw 0–1000` strength; needs `--sv 4|6` |
| `--oref` | public image URL | **Omni Reference (V7)** — carry a subject/character/object; `--ow 0–1000` (~400 to lock a face) |
| `--seed` | 0–4294967295 | reproducibility |
| `--tile` | flag | seamless patterns |
| `--q` | `.25`–`4` (V7) | detail vs GPU cost (V8.1 drops `--q`) |

**Version gate (critical):** V7 uses **`--oref`/`--ow`** for characters — `--cref`/`--cw` are
V6/Niji only and silently fail in V7. Never emit both. `--hd` (native ~2048px) is V8.1-only.

## Aspect ratios & size

Common: `1:1 16:9 9:16 4:3 3:4 3:2 2:3 4:5 5:4 21:9`. MJ renders a ~1MP base then offers
Upscale ×2/×4; V8.1 can output ~2048px with `--hd`. Extreme ratios are experimental.

## Style consistency

Use numeric `--sref <code>` (each code = a reproducible aesthetic) to lock a brand look across
images without describing it; raise `--sw` to 150–300 if weak. Use `--oref` for a consistent
subject/character.

## Output template

```
<subject + key descriptors>, <setting/context>, <lighting & atmosphere>, <medium/lens/finish>[, "QUOTED TEXT" in <font style>] --ar <W:H> --v 7 [--style raw] [--s <0-1000>] [--sref <code|url> --sw <n>] [--oref <url> --ow <n>] [--chaos <n>] [--no <exclusions>] [--seed <n>]
```
Example: `A weathered fisherman mending nets at dawn on a wooden dock, fog over calm water, soft golden backlight, shot on 35mm film with shallow depth of field and subtle grain --ar 3:2 --v 7 --style raw --s 150`

**Report in assumptions:** `model=midjourney · --ar <W:H> · --v 7 [· --style raw · --s <n>]`.

## Sources
docs.midjourney.com (Parameter List, Style/Character/Omni Reference, Multi-Prompts), updates.midjourney.com/omni-reference-oref/. (Official docs 403 to bots; cross-checked with RunThePrompts / BlakeCrosley cheat sheets.) Uncertain: exact V7 `--q` set, `--iw` upper bound, hard `--ar` cap — treat as tunable.
