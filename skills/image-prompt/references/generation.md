# Optional generation (calling image APIs)

The skill is **prompt-only by default**. This is the opt-in path that actually renders a PNG by
calling a provider's image API via `scripts/generate.py` (repo root). Rules:

- **Only generate when the user explicitly asks** ("сгенери", "generate it", "render it") AND a
  provider key is present in the environment. Otherwise stay prompt-only.
- **Confirm before spending** — generation costs money (outward-facing, paid). State the
  provider/model and that it's a paid call; proceed only on a clear go.
- Keys come from **environment variables only** (never committed, never printed).
- Midjourney has **no official API** (Discord only) — not supported for generation.

## How the skill runs it

1. Build the prompt as usual for the chosen model's adapter.
2. Write the prompt to a temp file (avoids shell-quoting issues), then run:
   ```
   python3 scripts/generate.py --provider <p> --prompt-file <tmp> --out assets/<name>.png [flags]
   ```
3. The script prints the saved path; then **view the PNG** to confirm it matches, and iterate.

Provider selection: if the user named a model, use its provider; otherwise prefer whichever key
is set (openrouter is the universal one — one key, many models).

## Providers

| provider | env var | endpoint | sync/async | default model | size/aspect flag |
|---|---|---|---|---|---|
| `openai` | `OPENAI_API_KEY` | `/v1/images/generations` | sync | `gpt-image-2` | `--size WxH` `--quality` |
| `openrouter` | `OPENROUTER_API_KEY` | `/api/v1/images` | sync | `google/gemini-3-pro-image` | `--aspect` `--resolution` `--quality` |
| `gemini` | `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) | `…:generateContent` | sync | `gemini-3-pro-image` | `--aspect` `--resolution 1K\|2K\|4K` |
| `ideogram` | `IDEOGRAM_API_KEY` | `/v1/ideogram-v3/generate` (multipart) | sync | `v3` (`--model v4`) | `--aspect` (→ `16x9`) `--style` |
| `recraft` | `RECRAFT_API_KEY` | `/v1/images/generations` | sync | `recraftv3` | `--size WxH` `--style` |
| `bfl` | `BFL_API_KEY` | `/v1/flux-2-pro` | **async (poll)** | `flux-2-pro` (`flux-2-flex` for text) | `--size WxH` or `--aspect` |
| `reve` | `AIMLAPI_KEY` | AI/ML API aggregator | sync | `reve/create-image` | `--aspect` |

## Notes / uncertainties (verify before relying)

- **OpenRouter** is the easiest multi-model path: one key, model slugs like
  `openai/gpt-image-2`, `google/gemini-3-pro-image`, `black-forest-labs/flux.2-pro`,
  `bytedance-seed/seedream-4.5`.
- **BFL** returns a signed result URL that **expires in ~10 minutes** — the script downloads
  immediately.
- **Recraft** V4.1 model string casing is inconsistent in the docs (`recraftv4_1` vs
  `recraft-v4.1`); the script defaults to the safe `recraftv3` — pass `--model` to override.
- **Reve** has no confirmed public native API (console is login-gated); the script uses the
  **AI/ML API aggregator** (`AIMLAPI_KEY`, model `reve/create-image`). Swap to native once its
  spec is confirmed.
- Gemini/gpt-image outputs carry provider watermarks (e.g. SynthID).
