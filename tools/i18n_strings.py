"""Lista los textos traducibles de index.html (versión en inglés)."""
import html, json, re, sys
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style"}
ATTRS = {"alt", "aria-label", "placeholder"}
META = {"description", "og:title", "og:description"}

def translatable(s):
    s = s.strip()
    return bool(s) and re.search(r"[A-Za-z]{2,}", s) and s not in {"EN", "ES", "RU"}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.out = [], []
    def add(self, s):
        s = " ".join(s.split())
        if translatable(s) and s not in self.out:
            self.out.append(s)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in {"meta", "link", "img", "input", "br", "source"}:
            self.stack.append(tag)
        for k in ATTRS:
            if a.get(k): self.add(a[k])
        if tag == "meta" and (a.get("name") in META or a.get("property") in META):
            self.add(a.get("content", ""))
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag: self.stack.pop()
    def handle_data(self, d):
        if not (set(self.stack) & SKIP_TAGS): self.add(d)

def strings(path="index.html"):
    p = P(); p.feed(open(path, encoding="utf-8").read()); return p.out

if __name__ == "__main__":
    json.dump(strings(), sys.stdout, ensure_ascii=False, indent=1)
