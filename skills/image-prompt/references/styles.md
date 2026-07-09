# Style menu — the built-in style repertoire

When the user knows the deliverable but wants help with the look ("I want a poster, help me
with the style" / "в каких стилях можешь" / "what styles can you do"), present this menu:
show the **names + one-line vibe**, grouped, and let them pick one (or combine two). Then
build the prompt using that style's spec below (it fills the style layer; content comes from
the idea). The user's own private presets (`~/.claude/image-prompt/presets/`) are also
available and can be offered alongside these.

Keep the on-screen menu short (name + one-liner). Pull the full spec from here only once a
style is chosen.

---

## Graphic / poster

**1. Y2K Streetwear Sticker-Collage** — playful, irreverent, Gen-Z.
Signature: chunky slab wordmark, vinyl sticker overlays (white borders + cast shadow), film grain, CRT warmth. Palette: saturated candy + one bright accent. Best for: posters, mobile landings, drops. Ref: gold #1.

**2. Editorial / Kinfolk Duotone** — premium, refined, magazine.
Signature: cream paper + halftone, duotone photo, high-contrast serif headline, multi-column justified body, "№" marks. Palette: cream + 1-2 duotone inks. Best for: posters, product editorials. Ref: gold #2.

**3. Punk Silkscreen** — rebellious, DIY, underground.
Signature: limited flat palette, heavy halftone grain, ink misregistration, scratchy hand-drawn border, heavy condensed type. Palette: 3-4 flat colors, no gradients. Best for: gig/exhibition posters. Ref: gold #3.

**4. 90s Manga** — nostalgic, cool, cel-shaded.
Signature: pure white bg, arched slanted italic wordmark, cel-shading + halftone shadows, vertical katakana/kanji edges. Palette: white + crimson + midnight-blue + accent. Best for: character posters. Ref: gold #4.

**5. Kaiju Graphic Silkscreen** — bold, punchy, badass.
Signature: thick black outlines, flat color blocks, zero gradients, halftone, big CJK headline w/ offset shadow, corner diagram/icons. Palette: 1 saturated bg + cream + 2 accents. Best for: statement posters, merch. Ref: gold #9.

**6. Synthwave / Outrun** — nostalgic 80s neon.
Signature: neon sunset grid, chrome-bevel type, VHS scanlines, palm silhouettes, glow. Palette: magenta/indigo/cyan + sunset orange. Best for: gig/event posters, music.

**7. Warm Editorial Hand-drawn** — human, friendly, tactile (Anthropic-esque).
Signature: cream paper + one clay/terracotta accent, loose single-weight black ink line art (hands, sparks, simple forms), watercolor-textured circle nodes joined by thin lines, paper grain. Palette: cream + clay + black + white. Best for: infographics, warm brand posters, explainers.

## Landing / UI

**8. Minimal Dark Dev-Tool** — precise, calm, modern.
Signature: ink dot-grid bg, terminal chip, bold lowercase grotesk wordmark w/ subtle magenta→cyan edge, flat crisp cards, generous negative space. Palette: ink + off-white + sparing accents. Best for: dev-tool banners, social posts, launch cards.

**9. Folk-Art Character Render** — warm, joyful, artisan.
Signature: hand-painted naive faces on 3D objects (Scandinavian-children's-book meets folk pottery), soft studio light, floating with shadows. Palette: warm pastels. Best for: homeware/product landings, mascots. Ref: gold #5.

**10. Y2K Chrome Game-UI** — retro-futuristic, techy, joyful.
Signature: aqua grid, glossy chrome panels, pixel type, HUD readouts, CRT scanlines, sparkles. Palette: aqua + magenta + cyan + chrome. Best for: playful product landings, event pages. Ref: gold #8.

**11. Cinematic Sport-Tech** — premium, aspirational, high-performance.
Signature: extreme close-up beauty photo, reflection storytelling, bold condensed headline, co-brand lockup, cinematic grade. Palette: cool base + one warm accent. Best for: sport/tech landings & ads. Ref: gold #6.

## Ad / cinematic

**12. Surreal Product Ad** — clever, playful, Cannes-y.
Signature: a visual pun or impossible POV, photoreal, clean grotesk headline + tagline, corner info blocks. Palette: natural + charcoal. Best for: brand ads. Ref: gold #7.

**13. Cinematic Movie One-Sheet** — epic, dramatic, blockbuster.
Signature: heroic low-angle subject, atmospheric bg, massive metallic title, tagline, billing block, teal-gold grade. Best for: film-style character posters (great with an identity-preserving photo edit).

**14. AAA Game Screenshot** — hyperreal, cinematic, in-engine.
Signature: labeled technical blocks (scene/subject/lighting/camera/HUD/technical), engine tags, corner-by-corner HUD, "paused gameplay". Best for: game key art / screenshots. Ref: gold #10.

## Diagram / technical

**15. Technical Blueprint** — smart, engineered, anachronistic.
Signature: cyan line-art cutaway/diagram on dark, callout labels + measurements, paper grid, mono type. Palette: ink-navy + cyan + paper. Best for: product-as-machine posters, explainers.

---

## Using a chosen style

Once picked, treat the style's spec as the style layer (background/texture, palette, fonts,
motifs, mood, finish) and fill the 9-block skeleton with content from the idea — exactly like
a preset. If the user combines two, blend their palettes/motifs sensibly and say how. Offer to
**save the result as a private preset** (`save this style as <name>`) if they want to reuse it.
