"""Genera /es/index.html y /ru/index.html a partir de index.html (inglés).

Uso:  py tools/build_i18n.py
Las traducciones están en i18n/es.json e i18n/ru.json (texto en inglés -> traducción).
Si cambias un texto en index.html, agrega su traducción en ambos JSON y vuelve a ejecutar
este script: avisa qué textos no tienen traducción.
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from i18n_strings import strings  # noqa: E402

LANGS = {"es": "es", "ru": "ru"}
ATTR_RE = re.compile(r'\b(alt|aria-label|placeholder|content)="([^"]*)"')

def norm(s):
    return " ".join(s.split())

def translate_text(seg, T, missing):
    core = seg.strip()
    if not core:
        return seg
    key = norm(html.unescape(core))
    if key not in T:
        if key in SOURCE:
            missing.add(key)
        return seg
    lead = seg[: len(seg) - len(seg.lstrip())]
    trail = seg[len(seg.rstrip()):]
    return lead + html.escape(T[key], quote=False) + trail

def translate_tag(tag, T, missing):
    if tag.startswith("<meta") and not re.search(r'(name|property)="(description|og:title|og:description)"', tag):
        return tag
    def sub(m):
        key = norm(html.unescape(m.group(2)))
        if key in T:
            return f'{m.group(1)}="{html.escape(T[key], quote=True)}"'
        if key in SOURCE:
            missing.add(key)
        return m.group(0)
    return ATTR_RE.sub(sub, tag)

def build(lang):
    T = json.load(open(os.path.join(ROOT, "i18n", f"{lang}.json"), encoding="utf-8"))
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    missing = set()
    out, skip = [], None
    for part in re.split(r"(<[^>]+>)", src):
        if part.startswith("<"):
            low = part.lower()
            if skip and low.startswith(f"</{skip}"):
                skip = None
            elif not skip and re.match(r"<(script|style)\b", low):
                skip = re.match(r"<(script|style)", low).group(1)
            out.append(part if skip and not low.startswith("<script") and not low.startswith("<style") else translate_tag(part, T, missing))
        else:
            out.append(part if skip else translate_text(part, T, missing))
    page = "".join(out)

    # Idioma de la página, enlaces canónicos y menú de idiomas
    page = page.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    page = page.replace('<link rel="canonical" href="https://go56south.com/">', f'<link rel="canonical" href="https://go56south.com/{lang}/">', 1)
    page = page.replace(' aria-current="true" title="English">', ' title="English">', 1)
    page = re.sub(rf'(<a href="/{lang}/" hreflang="{lang}" lang="{lang}")', r'\1 aria-current="true"', page, count=1)
    page = page.replace('<input type="hidden" name="language" value="en">', f'<input type="hidden" name="language" value="{lang}">', 1)

    # Rutas relativas: la página vive un nivel más abajo
    page = re.sub(r'(src|href)="(assets/|favicon\.png|apple-touch-icon\.png)', r'\1="../\2', page)
    page = page.replace("url(assets/", "url(../assets/")

    os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
    open(os.path.join(ROOT, lang, "index.html"), "w", encoding="utf-8").write(page)
    return missing

SOURCE = set(strings(os.path.join(ROOT, "index.html")))

if __name__ == "__main__":
    ok = True
    for lang in LANGS:
        miss = build(lang)
        print(f"/{lang}/index.html generado" + (f" — faltan {len(miss)} traducciones:" if miss else ""))
        for m in sorted(miss):
            ok = False
            print("   ·", m)
    sys.exit(0 if ok else 1)
