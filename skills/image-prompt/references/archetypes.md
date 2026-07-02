# Archetypes — pick one, then fill the 9-block skeleton

Detect the archetype from the user's idea, then use its defaults (aspect → size,
quality, which blocks matter, a zone template). Sizes are gpt-image-2 values; see
`models/gpt-image-2.md` for the full aspect→size map and constraints.

When the idea is ambiguous between two archetypes, prefer the one that makes the
richest layout, and note the choice in the assumptions line.

---

## 1. Poster
Editorial, silkscreen/punk, manga, kaiju/graphic, gig/exhibition, typographic.

- **Default size:** `1024x1536` (vertical 2:3). Manga/portrait also 2:3.
- **Default quality:** `high` (dense typography + texture).
- **Blocks that matter most:** 2, 3, 5, 6, 8, 9. Strong texture/finish is signature.
- **Zone template:** top banner (vol/date tag or intro line) → dominant central subject
  (photo/illustration/silkscreen portrait) → floating badge/sticker overlays → massive
  wordmark or artist name → thin footer meta strip.
- **Subtype cues:**
  - *Editorial* (Cereal/Apartamento/Kinfolk): cream paper, halftone, duotone subject,
    3-column justified serif body, page-number "№ 04", refined high-contrast serif.
  - *Silkscreen/punk*: limited flat palette, heavy halftone grain, ink misregistration,
    scratchy hand-drawn border, condensed heavy sans, rough DIY energy.
  - *Manga*: pure white bg, arched slanted italic wordmark, cel-shaded portrait,
    vertical katakana/kanji on edges, halftone in shadows.
  - *Kaiju/graphic*: bold black outlines, flat color blocks, zero gradients, halftone,
    kanji headline with offset shadow, 70s Japanese underground energy.
- Gold refs: LOUD KIDS CLUB, furniture/corgi editorial, punk exhibition, AKAI manga,
  panda kaiju.

## 2. Landing hero (web)
Desktop or mobile marketing hero section.

- **Default size:** desktop `1536x1024` (16:9); mobile `864x1536` (9:16).
- **Default quality:** `high`.
- **Blocks that matter most:** 1 (say "landing page hero"), 2, 3, 5, 6.
- **Zone template:** thin top nav (wordmark left · 3-4 links center · account/cart right)
  → dominant hero (photo or floating 3D product renders, ~60-75%) → left/lower content
  column (price, 2-3 line description, pill CTA button) → pagination "01 / 08" + collection
  tag → bottom strip (shipping/returns · brand est.).
- **Style cues:** real interface structure, "looks like a shipped site", generic
  unbranded UI glyphs, soft cast shadows on floating renders.
- Gold refs: kiln & co. homeware, APEX & SUMMIT eyewear, DRESSR Y2K (game-UI subtype).

## 3. Product ad / marketing creative
Poster-format advertising with a concept + tagline.

- **Default size:** `1024x1536` (3:4/2:3) or `1536x1024` if the concept is horizontal.
- **Default quality:** `medium` (bump to `high` if lots of in-image text).
- **Blocks that matter most:** 1 (write it like a creative brief), 3, 4, 5, 8, 9.
- **Zone template:** conceptual hero image (often a visual pun or surreal POV) →
  headline (short, bold, 2 lines) → 2-line sub-headline → brand logo lockup (fictional)
  → small info blocks in corners → thin footer meta strip.
- **Style cues:** state the concept clearly; commercial photography finish; exact tagline
  in quotes, rendered once; Shutterstock / Cannes-Lion quality tag.
- Gold refs: milk "OUT OF THE BOX" POV, gpt-image-2 guide "Thread" streetwear ad.

## 4. UI mockup (product interface)
App or web UI shown as a designed screen, optionally in a device frame.

- **Default size:** `1024x1536` (mobile in iPhone frame) or `1536x1024` (desktop/web app).
- **Default quality:** `high` (small UI text).
- **Blocks that matter most:** 1 ("realistic UI mockup, looks shipped"), 2, 3, 5.
- **Zone template:** header/nav → primary content list or dashboard cards → secondary
  section → tab/nav bar. Describe real components (lists, cards, toggles, charts), spacing,
  hierarchy. Avoid concept-art language.
- **Style cues:** "practical, easy to use, well-designed", clean typography (Inter/Söhne),
  subtle accent color, minimal decoration. Put it in a device frame if mobile.
- Gold refs: gpt-image-2 guide farmers-market app, DRESSR (stylized game-UI variant).

## 5. Photoreal scene (candid photography)
A believable real photograph, not a poster.

- **Default size:** `1024x1536` (portrait) or `1536x1024` (landscape).
- **Default quality:** `high`.
- **Use the photoreal variant** of the skeleton (SCENE / SUBJECT / LIGHTING / CAMERA /
  TECHNICAL). Minimal or no typography.
- **Style cues:** include "photorealistic"; photography language (35mm, 50mm lens, shallow
  DoF, film grain); real texture (pores, wear, imperfections); avoid studio-polish words;
  "honest, unposed". No cinematic grading unless asked.
- Gold refs: gpt-image-2 guide sailor / Yosemite-bear; milk-ad cows (photoreal hero).

## 6. Game screenshot
AAA in-engine look with HUD.

- **Default size:** `1536x864` (16:9) or `2560x1440` (premium wide, experimental).
- **Default quality:** `high`.
- **Use the photoreal variant** + the **HUD block** (corner-by-corner UI: portrait +
  health/stamina, boss bar, minimap, item slots, button prompts, quest text).
- **Style cues:** engine/technical tags (Unreal Engine 5.3, Lumen GI, Nanite, path-traced,
  ray-traced AO, ACES filmic, chromatic aberration minimal); "feels like paused real
  gameplay"; fidelity references (God of War + Ghost of Tsushima + Horizon).
- Gold ref: God of War-style Cyclops screenshot.

## 7. Infographic / diagram / slide / chart
Structured information visual.

- **Default size:** `1024x1536` (poster infographic) or `1536x1024`/`1536x864` (slide/deck).
- **Default quality:** `high` (dense labels + small text).
- **Blocks that matter most:** 1 (name the exact deliverable + audience + objective), 3
  (layout + hierarchy), 5 (labels/data verbatim), 6.
- **Style cues:** write like an artifact spec; provide real numbers/labels in the prompt;
  clean flat icon system, clear arrows, readable labels, generous white space; "no clip
  art, no stock photos, no decorative clutter". Landscape for decks.
- Gold refs: gpt-image-2 guide coffee-machine infographic, cellular-respiration diagram,
  "Market Opportunity" pitch slide.

## 8. Logo
Single clean brand mark.

- **Default size:** `1024x1024`.
- **Default quality:** `medium` (offer `n=4` variations conceptually — but v1 outputs a
  prompt only; mention variations in the assumptions line).
- **Blocks that matter most:** 1 (brand personality + use case), 8 (mood), CONSTRAINTS.
- **Style cues:** "original, non-infringing"; clean vector-like shapes, strong silhouette,
  balanced negative space, scalable, flat, minimal strokes, plain background, generous
  padding, no watermark. Favor simplicity over detail.
- Gold ref: gpt-image-2 guide "Field & Flour" bakery logo.

## 9. Illustration
Comic strip, children's-book art, character/mascot, editorial illustration, album cover.

- **Default size:** `1024x1536` (vertical) or `1024x1024`.
- **Default quality:** `medium` (high for text-heavy comics).
- **Blocks that matter most:** 1 (name the illustration style), 4 (character anchor), 8.
- **Style cues:** name the illustration medium (hand-painted watercolor, flat vector,
  risograph, 3D Blender render, folk-art naive). For multi-panel: define beats one per
  panel. For character consistency: lock outfit + proportions + palette as a reusable anchor.
  Original characters only, no copyrighted characters.
- Gold refs: gpt-image-2 guide comic reel, children's-book forest hero; kiln & co. mug
  characters (folk-art illustration style).

---

## Default routing table

| User idea contains… | Archetype | Size | Quality |
|---|---|---|---|
| poster, plakat, gig, exhibition, cover | Poster | 1024x1536 | high |
| landing, lending, hero, homepage, website | Landing hero | 1536x1024 (mobile→864x1536) | high |
| ad, реклама, campaign, billboard, product shot | Product ad | 1024x1536 | medium |
| app, UI, интерфейс, dashboard, screen, mockup | UI mockup | 1024x1536 / 1536x1024 | high |
| photo, фото, portrait, candid, realistic scene | Photoreal scene | 1024x1536 | high |
| game, игра, screenshot, RPG, in-engine | Game screenshot | 1536x864 | high |
| infographic, diagram, slide, chart, схема | Infographic | 1024x1536 | high |
| logo, логотип, brand mark | Logo | 1024x1024 | medium |
| illustration, comic, mascot, персонаж, album | Illustration | 1024x1536 | medium |

If nothing matches, default to **Poster** (richest layout) and note it.
