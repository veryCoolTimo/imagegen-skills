# imagegen-skills

Claude Code skills for generating **gold-quality AI image prompts** from a one-line idea.

## `image-prompt`

You throw an idea ("постер для стритвир-бренда", "landing hero for a coffee app", "game
screenshot of a viking raid"). The skill auto-detects the archetype, picks the aspect
ratio, palette, and fonts, and builds **one structured, copy-paste-ready prompt** optimized
for **gpt-image-2** by default. Press `c` to copy the prompt block.

It follows a pattern extracted from a corpus of high-quality reference prompts:

- **9-block skeleton** — concept line · canvas+background · named composition zones ·
  subject detail · typography (literal copy + real fonts) · hex palette · font role map ·
  mood cluster · finish + quality tag.
- **Archetypes** — poster, landing hero, product ad, UI mockup, photoreal scene, game
  screenshot, infographic, logo, illustration.
- **gpt-image-2 rules** baked in — labeled sections, exact `size`/`quality`, text-in-quotes,
  IP-safety constraints.

### Install

Symlink the skill into your personal Claude Code skills directory:

```bash
ln -s "$(pwd)/skills/image-prompt" ~/.claude/skills/image-prompt
```

Restart Claude Code so it discovers the skill. Then just describe what you want, or invoke
it explicitly with `/image-prompt <idea>`.

### Usage

```
> постер для панк-выставки в берлине, лимитированный тираж
```

The skill returns a full prompt in a copyable code block plus a one-line assumptions note
(archetype · size · quality · brand · model). Redirect with a single sentence:
"make it 9:16", "darker palette", "brand is NOVA", "another variant".

### Structure

```
skills/image-prompt/
├── SKILL.md                     # trigger + workflow + output format
└── references/
    ├── anatomy.md               # the 9-block skeleton
    ├── archetypes.md            # templates + default aspect/quality per archetype
    ├── fonts-palettes.md        # font library by vibe + hex palette discipline
    ├── gold-examples.md         # curated reference prompts (grows over time)
    └── models/gpt-image-2.md    # gpt-image-2 guide distilled into build rules
```

### Extending

- **New favourite prompt:** add it to `references/gold-examples.md` with a `Teaches:` tag.
- **New model:** add `references/models/<name>.md` (universal / Midjourney / Gemini /
  Ideogram). The workflow is model-agnostic — the core stays unchanged.
