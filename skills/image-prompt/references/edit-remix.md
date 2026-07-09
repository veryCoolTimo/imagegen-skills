# Edit / remix workflows (gpt-image-2)

Use when the user provides (or refers to) an existing image and wants to transform, composite,
restyle, localize, or place someone/something into it. This is an **edit** (image[+text]→image,
`client.images.edit`), not a generate. Still prompt-only output — the user attaches the image(s)
in their tool and pastes the prompt.

## Core discipline (from the gpt-image-2 guide)

- **Change vs preserve.** State exactly what to change, then "keep everything else the same".
  List the invariants explicitly (identity, geometry, layout, palette, camera, background,
  logos) and **repeat the preserve list on every iteration** — this is what stops drift.
- **Surgical edits.** If the change is small, also say: do not alter saturation, contrast,
  layout, labels, arrows, camera angle, or surrounding objects.
- **Multiple inputs.** Reference each by index + role ("Image 1: the person's photo; Image 2:
  the product"). Be explicit about which element moves where.
- **In-image text.** Literal copy in quotes, verbatim, rendered once; specify font + placement.
- **Params.** `input_fidelity=high` to hold likeness/geometry during bigger edits;
  `background=opaque` for product extraction (remove bg downstream); `quality=high` for small
  text / portraits; pick `size` to match the source aspect or the intended output.
- **Iterate** with single-change follow-ups, re-specifying critical invariants each time.

## Edit output template

```
[One line: what this edit does + intended use. Note: this is an IMAGE EDIT.]

INPUTS:
- Image 1: <what it is / its role>
- (Image 2: <…>)

CHANGE:
<only what should change>

PRESERVE (do not alter):
<identity / geometry / layout / palette / camera / background / logos — the invariants>

[Add STYLE / SCENE / TEXT sections as needed, using the normal 9-block discipline.]

PARAMS: size=<WxH> · quality=<low|medium|high> · input_fidelity=high [· background=opaque]
CONSTRAINTS: no watermark, no added logos or trademarks; render each text string once, verbatim.
```

## Workflow templates

| Workflow | Change → Preserve | Key params |
|---|---|---|
| Identity-preserving hero / character-in-poster | build a poster around the person in Image 1; add costume/scene → **preserve exact face, features, skin tone, likeness** | input_fidelity=high, quality=high |
| Insert person into a scene | place the Image 1 person into a described scene → preserve their likeness; grounded photo look | input_fidelity=high |
| Multi-image composite | move the element from Image 2 into Image 1, matching lighting/perspective/scale/shadows → preserve the rest of the scene | input_fidelity=high |
| Style transfer | apply Image 1's style (palette, texture, brushwork, grain) to new content → keep style cues, change subject; no extra elements | quality per detail |
| Background / scene swap | replace the background → **preserve the subject exactly**; match new lighting + contact shadows | input_fidelity=high |
| Lighting / weather transform | change only environmental conditions (time of day, weather, mood) → preserve identity, geometry, camera, placement | input_fidelity=high |
| Product on clean white | extract product to a plain opaque background; crisp silhouette, no halos; light polish + subtle contact shadow → **preserve geometry + label legibility** | background=opaque |
| Marketing text / billboard mockup | place the product into a scene + add the exact tagline (in quotes, once, legible) → preserve product + label | quality=high |
| Object add / remove | remove or add only X → keep everything else the same | input_fidelity=high |
| Interior / object swap | replace only object X (e.g. the chairs) → preserve camera, room lighting, floor shadows, surrounding objects | quality=medium/high |
| Translate / localize | translate the in-image text verbatim to <language> → preserve typography, placement, spacing, hierarchy; don't touch logos, icons, imagery, layout | quality=high |
| Sketch / wireframe → render | turn the drawing into a photoreal image or shipped UI → preserve layout, proportions, perspective; add plausible materials/lighting; add no new elements or text | quality=high |

## Notes

- Detect edit intent from cues: "add me to…", "change the background", "in this photo",
  "turn this sketch into…", "same style as this", "remove the…", "put X into Y", "localize /
  translate this", "extract the product", "make it night / snowy".
- If the idea is a poster/ad built around a supplied person or product, that is the
  identity-preserving hero workflow (see the "The Deep" movie one-sheet exemplar).
- Keep IP-safety: original design, no added logos/trademarks/watermark; for likenesses, only
  the person the user supplied — do not invent recognizable real people.
