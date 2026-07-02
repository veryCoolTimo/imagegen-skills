# Fonts & palettes — style anchors

Naming a real font family and giving every color a hex code are two of the strongest,
cheapest quality levers. Use both in every prompt.

---

## Font library, by vibe

Pick fonts whose vibe matches the aesthetic, then name them in Block 5 ("a bold condensed
grotesk like Druk Wide"). The model uses them as style anchors, not exact renders.

| Vibe | Use for | Named references |
|---|---|---|
| Chunky slab / arcade display | playful wordmarks, Y2K, cereal-box energy | Bungee Slab, Bungee Inline, Hardcore Slab |
| Heavy condensed grotesk | punchy headlines, sports, punk, posters | Druk Wide Bold, Knockout Heavyweight, Tungsten Bold |
| High-contrast elegant serif | editorial headlines, luxury, magazine | Tiempos Headline, Canela, Playfair Display Black |
| Italic serif | accent lines, body copy, refined subtitles | Tiempos Text Italic, Garamond Italic, DM Serif Text Italic |
| Clean modern sans | landing/UI body, product, minimalist wordmarks | Inter, Söhne, Aeonik, Neue Haas Grotesk |
| Geometric / rounded | friendly brands, homeware, soft tech | Circular, Poppins, Aeonik Rounded |
| Pixel / retro game | Y2K UI, 8/16-bit, arcade | Press Start 2P, chunky pixel/LCD mono |
| Mono / technical | code, HUD readouts, spec labels | monospace, LCD/segment display |
| Hand-drawn / marker | stickers, brand glyphs, DIY collage | rough hand-scrawled lowercase, marker script |
| CJK display | manga/kaiji edges & headlines | bold katakana/kanji, chunky hand-drawn kanji |

Rules:
- Always give each text role its own font (wordmark ≠ body ≠ meta). See Block 7.
- Describe **weight · tracking · case · effects** alongside the name (bevel, chrome
  highlight, 3D shadow, outline, ink imperfection).

---

## Palette discipline

- **4-6 colors**, each written as a hex code and **mapped to an element**.
- One dominant background, 1-2 accents, one ink/text color, plus natural tones (skin) if
  people are present.
- State gradients as "A → B" with both hexes.
- Match palette to mood: high-contrast + limited = punk/graphic; warm creams = editorial;
  saturated candy = Y2K; icy + one warm accent = sport-tech.

Template:
> Palette: [bg] (#XXXXXX → #XXXXXX), [accent 1] #XXXXXX, [accent 2] #XXXXXX,
> [ink] #XXXXXX, natural skin tones.

---

## Ready-made palettes (lift or adapt)

**Y2K streetwear (LOUD KIDS)**
royal-blue→navy #2E5BAC → #1A2D4F · marigold #F4C542 · shadow #C98A1E · cream #F5EFE3 ·
charcoal #1A1A1A · pop-red #D44A3A

**Editorial cream (Cereal/Kinfolk)**
warm cream paper · cobalt duotone #2E5BFF · rust-orange #D1623A · charcoal #1A1A1A

**Punk silkscreen (limited flat)**
vermilion #E4401C · saturated yellow #FFD500 · charcoal #141414 · cream #F4EDD8
(no gradients, flat, halftone only)

**90s manga (AKAI)**
pure white bg · crimson #C81E2E · midnight blue #10214A · silver chrome · warm orange accent

**Warm homeware (kiln & co.)**
blush-pink #F5D6CC · charcoal #1A1A1A · terracotta · sage-green · cobalt · dusty-pink ·
butter-yellow · warm brown-grey text #6B5A52

**Icy sport-tech (APEX)**
icy-blue→snow-white #D8E5EC → #F0F5F8 · amber→magenta lens #E89A3A → #C14A6E · white #FFFFFF

**Y2K aqua UI (DRESSR)**
aqua-cyan #0A4A6B → #5BC0D8 · magenta-pink #FF3D8E · cyan #4FE5FF · chrome silver #D4E4EC ·
LCD green #7FFF7F

**Warm kraft ad (milk POV)**
kraft-brown #B8916B · cerulean sky #A8C8E4 · cloud white · charcoal #1A1A1A · grey #6B6B6B

**Kaiju graphic (panda)**
electric teal #0D7377 · cream fur · magenta tongue · acid-yellow eyes · coral accents ·
black patches

**Cold winter game (God of War)**
desaturated blue-grey · cold 6500K · stone-grey · tarnished bronze UI · deep red health bar

---

## Anti-generic guardrails

- Never leave a color as a word only ("blue") — give the hex.
- Never leave typography as "nice font" — name a family + weight.
- Add a real-texture / finish cue (grain, halftone, brushwork, pores) — it's what separates
  gold prompts from flat AI output.
