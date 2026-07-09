#!/usr/bin/env python3
"""
Optional image generator for the image-prompt skill.

Prompt-only is the skill's default; this script is the OPT-IN "generate" step. It calls a
provider's image API and saves a PNG. Keys come from environment variables (never committed).
Generation costs money — run it only on the user's explicit request.

Usage:
  python3 generate.py --provider openrouter --prompt-file p.txt --out out.png \
      --model google/gemini-3-pro-image --aspect 16:9 --resolution 2K
  python3 generate.py --provider openai --prompt "a red panda astronaut" \
      --size 1024x1536 --quality high --out out.png

Providers: openai | openrouter | gemini | ideogram | recraft | bfl | reve
(Midjourney has no official API — not supported.)
"""
import argparse
import base64
import os
import sys
import time

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install requests")

# provider -> env var(s) holding the API key (first found wins)
ENV = {
    "openai": ["OPENAI_API_KEY"],
    "openrouter": ["OPENROUTER_API_KEY"],
    "gemini": ["GEMINI_API_KEY", "GOOGLE_API_KEY"],
    "ideogram": ["IDEOGRAM_API_KEY"],
    "recraft": ["RECRAFT_API_KEY"],
    "bfl": ["BFL_API_KEY"],
    "reve": ["AIMLAPI_KEY"],  # via AI/ML API aggregator (native Reve API unconfirmed)
}
DEFAULT_MODEL = {
    "openai": "gpt-image-2",
    "openrouter": "google/gemini-3-pro-image",
    "gemini": "gemini-3-pro-image",
    "ideogram": "v3",                    # endpoint version: v3 (stable) | v4
    "recraft": "recraftv3",              # safe default; recraftv4_1 also available
    "bfl": "flux-2-pro",                 # or flux-2-flex (best text)
    "reve": "reve/create-image",
}
TIMEOUT = 300
# aspect -> (w, h) fallback for width/height-only APIs (BFL)
ASPECT_WH = {"1:1": (1024, 1024), "16:9": (1344, 768), "9:16": (768, 1344),
             "3:2": (1216, 832), "2:3": (832, 1216), "4:3": (1152, 896),
             "3:4": (896, 1152), "21:9": (1536, 640)}


def get_key(provider):
    for var in ENV[provider]:
        if os.environ.get(var):
            return os.environ[var]
    sys.exit(f"No API key for '{provider}'. Set one of: {', '.join(ENV[provider])}")


def write_png(data: bytes, out: str):
    with open(out, "wb") as f:
        f.write(data)
    print(out)


def download(url: str, out: str):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    write_png(resp.content, out)


def gen_openai(a):
    key = get_key("openai")
    body = {"model": a.model or DEFAULT_MODEL["openai"], "prompt": a.prompt,
            "size": a.size or "1024x1024", "quality": a.quality or "high", "n": 1}
    r = requests.post("https://api.openai.com/v1/images/generations",
                      headers={"Authorization": f"Bearer {key}"}, json=body, timeout=TIMEOUT)
    r.raise_for_status()
    write_png(base64.b64decode(r.json()["data"][0]["b64_json"]), a.out)


def gen_openrouter(a):
    key = get_key("openrouter")
    body = {"model": a.model or DEFAULT_MODEL["openrouter"], "prompt": a.prompt}
    if a.aspect:
        body["aspect_ratio"] = a.aspect
    if a.resolution:
        body["resolution"] = a.resolution
    if a.quality:
        body["quality"] = a.quality
    r = requests.post("https://openrouter.ai/api/v1/images",
                      headers={"Authorization": f"Bearer {key}",
                               "HTTP-Referer": "https://github.com/veryCoolTimo/imagegen-skills",
                               "X-Title": "imagegen-skills"},
                      json=body, timeout=TIMEOUT)
    r.raise_for_status()
    write_png(base64.b64decode(r.json()["data"][0]["b64_json"]), a.out)


def gen_gemini(a):
    key = get_key("gemini")
    model = a.model or DEFAULT_MODEL["gemini"]
    img_cfg = {}
    if a.aspect:
        img_cfg["aspectRatio"] = a.aspect
    if a.resolution:
        img_cfg["imageSize"] = a.resolution
    gen_cfg = {"responseModalities": ["TEXT", "IMAGE"]}
    if img_cfg:
        gen_cfg["imageConfig"] = img_cfg
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    r = requests.post(url, headers={"x-goog-api-key": key},
                      json={"contents": [{"parts": [{"text": a.prompt}]}],
                            "generationConfig": gen_cfg}, timeout=TIMEOUT)
    r.raise_for_status()
    for p in r.json()["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            write_png(base64.b64decode(p["inlineData"]["data"]), a.out)
            return
    sys.exit("No image part in Gemini response.")


def gen_ideogram(a):
    key = get_key("ideogram")
    ver = (a.model or DEFAULT_MODEL["ideogram"]).lstrip("v")
    aspect = (a.aspect or "1:1").replace(":", "x")  # Ideogram wants 16x9, not 16:9
    fields = {"prompt": (None, a.prompt), "aspect_ratio": (None, aspect),
              "rendering_speed": (None, "DEFAULT")}
    if a.style:
        fields["style_type"] = (None, a.style.upper())
    r = requests.post(f"https://api.ideogram.ai/v1/ideogram-v{ver}/generate",
                      headers={"Api-Key": key}, files=fields, timeout=TIMEOUT)
    r.raise_for_status()
    download(r.json()["data"][0]["url"], a.out)


def gen_recraft(a):
    key = get_key("recraft")
    body = {"prompt": a.prompt, "model": a.model or DEFAULT_MODEL["recraft"],
            "style": a.style or "realistic_image", "size": a.size or "1024x1024",
            "n": 1, "response_format": "url"}
    r = requests.post("https://external.api.recraft.ai/v1/images/generations",
                      headers={"Authorization": f"Bearer {key}"}, json=body, timeout=TIMEOUT)
    r.raise_for_status()
    download(r.json()["data"][0]["url"], a.out)


def gen_bfl(a):
    key = get_key("bfl")
    model = a.model or DEFAULT_MODEL["bfl"]
    if a.size and "x" in a.size:
        w, h = (int(x) for x in a.size.lower().split("x"))
    else:
        w, h = ASPECT_WH.get(a.aspect or "1:1", (1024, 1024))
    sub = requests.post(f"https://api.bfl.ai/v1/{model}", headers={"x-key": key},
                        json={"prompt": a.prompt, "width": w, "height": h,
                              "output_format": "png"}, timeout=60).json()
    polling_url = sub.get("polling_url")
    if not polling_url:
        sys.exit(f"BFL submit failed: {sub}")
    deadline = time.time() + TIMEOUT
    while time.time() < deadline:
        res = requests.get(polling_url, headers={"x-key": key}, timeout=30).json()
        status = res.get("status")
        if status == "Ready":
            download(res["result"]["sample"], a.out)  # signed URL expires in ~10 min
            return
        if status not in ("Pending", "Processing", None):
            sys.exit(f"BFL failed: {status} {res.get('details')}")
        time.sleep(1.5)
    sys.exit("BFL timed out.")


def gen_reve(a):
    # Native Reve API is login-gated/unconfirmed; use the AI/ML API aggregator path.
    key = get_key("reve")
    body = {"model": a.model or DEFAULT_MODEL["reve"], "prompt": a.prompt,
            "aspect_ratio": a.aspect or "3:2", "convert_base64_to_url": True}
    r = requests.post("https://api.aimlapi.com/v1/images/generations",
                      headers={"Authorization": f"Bearer {key}"}, json=body, timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()["data"][0]
    if d.get("url"):
        download(d["url"], a.out)
    else:
        write_png(base64.b64decode(d["b64_json"]), a.out)


DISPATCH = {"openai": gen_openai, "openrouter": gen_openrouter, "gemini": gen_gemini,
            "ideogram": gen_ideogram, "recraft": gen_recraft, "bfl": gen_bfl, "reve": gen_reve}


def main():
    ap = argparse.ArgumentParser(description="Optional image generator for image-prompt.")
    ap.add_argument("--provider", required=True, choices=sorted(DISPATCH))
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--model", help="override model/version (see DEFAULT_MODEL)")
    ap.add_argument("--out", default="generated.png")
    ap.add_argument("--size", help="WxH (openai/recraft/bfl), e.g. 1024x1536")
    ap.add_argument("--aspect", help="e.g. 16:9 (openrouter/gemini/ideogram/reve/bfl)")
    ap.add_argument("--resolution", help="1K|2K|4K (openrouter/gemini)")
    ap.add_argument("--quality", help="low|medium|high (openai/openrouter)")
    ap.add_argument("--style", help="style hint (ideogram style_type / recraft style)")
    a = ap.parse_args()
    if a.prompt_file:
        with open(a.prompt_file, encoding="utf-8") as f:
            a.prompt = f.read().strip()
    if not a.prompt:
        sys.exit("Provide --prompt or --prompt-file")
    DISPATCH[a.provider](a)


if __name__ == "__main__":
    main()
