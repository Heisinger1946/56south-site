"""Genera el fondo animado de la sección de latitudes, como baldosas que se repiten sin costuras:
- assets/topo.svg: curvas de nivel (estilo carta topográfica de la cordillera).
- assets/topo-peaks.svg: cumbres de Chile con su altura, puestas sobre las cimas del dibujo, de norte a sur.

Uso:  py tools/topo_svg.py            (misma semilla = mismo dibujo)
"""
import math, os, sys
import numpy as np

SIZE = 1200          # lado de la baldosa en px
N = 200              # celdas por lado
LEVELS = 11          # cantidad de curvas
SEED = 56
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "topo.svg")

rng = np.random.default_rng(SEED)
t = np.arange(N) / N * 2 * math.pi
X, Y = np.meshgrid(t, t)

# Relieve periódico: frecuencias enteras (así calza en los bordes). Más detalle en X que en Y,
# para que los cordones queden alargados de norte a sur, como los Andes.
h = np.zeros((N, N))
for fx, fy, amp in [(1, 1, 1.0), (2, 1, .8), (3, 1, .55), (2, 2, .45), (4, 1, .32), (3, 2, .3), (5, 2, .2), (4, 3, .16), (6, 1, .14), (1, 2, .5)]:
    for sx in (1, -1):
        h += amp * rng.uniform(.6, 1) * np.sin(fx * X + sx * fy * Y + rng.uniform(0, 2 * math.pi))
h = (h - h.min()) / (h.max() - h.min())


def segments(level):
    """Marching squares sobre la grilla periódica: devuelve tramos (p, q) en coordenadas de celda."""
    segs = []
    a = h
    b = np.roll(h, -1, axis=1)                         # vecino a la derecha
    c = np.roll(np.roll(h, -1, axis=0), -1, axis=1)    # diagonal
    d = np.roll(h, -1, axis=0)                         # vecino de abajo
    for i in range(N):
        for j in range(N):
            v = (a[i, j], b[i, j], c[i, j], d[i, j])
            code = sum(1 << k for k in range(4) if v[k] > level)
            if code in (0, 15):
                continue
            def cut(k):  # punto donde la curva cruza el lado k de la celda (0 arriba, 1 derecha, 2 abajo, 3 izquierda)
                p, q = v[k], v[(k + 1) % 4]
                f = (level - p) / (q - p)
                return [(j + f, i), (j + 1, i + f), (j + 1 - f, i + 1), (j, i + 1 - f)][k]
            table = {1: [(3, 0)], 2: [(0, 1)], 3: [(3, 1)], 4: [(1, 2)], 6: [(0, 2)], 7: [(3, 2)], 8: [(2, 3)],
                     9: [(0, 2)], 11: [(1, 2)], 12: [(1, 3)], 13: [(0, 1)], 14: [(3, 0)],
                     5: [(3, 0), (1, 2)], 10: [(0, 1), (2, 3)]}
            for e0, e1 in table[code]:
                segs.append((cut(e0), cut(e1)))
    return segs


def chain(segs):
    """Une los tramos en líneas continuas."""
    key = lambda p: (round(p[0], 4), round(p[1], 4))
    ends = {}
    for idx, (p, q) in enumerate(segs):
        ends.setdefault(key(p), []).append(idx)
        ends.setdefault(key(q), []).append(idx)
    used, lines = set(), []
    for start in range(len(segs)):
        if start in used:
            continue
        used.add(start)
        line = [segs[start][0], segs[start][1]]
        for grow_end in (True, False):
            while True:
                tip = line[-1] if grow_end else line[0]
                nxt = [i for i in ends.get(key(tip), []) if i not in used]
                if not nxt:
                    break
                i = nxt[0]
                used.add(i)
                p, q = segs[i]
                other = q if key(p) == key(tip) else p
                line.append(other) if grow_end else line.insert(0, other)
        lines.append(line)
    return lines


def path(line, scale):
    pts = [(x * scale, y * scale) for x, y in line[::2]] + [(line[-1][0] * scale, line[-1][1] * scale)]
    if len(pts) < 4:
        return ""
    d = "M%.1f %.1f" % pts[0]
    for i in range(1, len(pts) - 1):  # curva suave pasando por los puntos medios
        mx, my = (pts[i][0] + pts[i + 1][0]) / 2, (pts[i][1] + pts[i + 1][1]) / 2
        d += "Q%.1f %.1f %.1f %.1f" % (pts[i][0], pts[i][1], mx, my)
    return d + "L%.1f %.1f" % pts[-1]


scale = SIZE / N
thin, bold = [], []
for k in range(LEVELS):
    level = (k + .5) / LEVELS
    for line in chain(segments(level)):
        d = path(line, scale)
        if d:
            (bold if k % 4 == 1 else thin).append(d)   # cada cuarta curva va más marcada ("curva maestra")

svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" fill="none" stroke="#0A1317" stroke-linecap="round">'
       '<path stroke-width="1" d="%s"/><path stroke-width="1.9" d="%s"/></svg>') % (SIZE, SIZE, SIZE, SIZE, "".join(thin), "".join(bold))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(svg)
print("curvas:", len(thin) + len(bold), "-", os.path.getsize(OUT) // 1024, "KB")

# Cumbres: una por latitud que ofrecemos, de norte a sur, cada una sobre una cima real del relieve dibujado.
PEAKS = [("Licancabur", 5916), ("Tupungato", 6570), ("Villarrica", 2847), ("San Valentín", 4058), ("Paine Grande", 2884), ("Cabo de Hornos", 425)]
# La baldosa se ve desde arriba y un notebook muestra unos 700 px de alto: las cumbres van en seis franjas
# dentro de esa zona, y en cada franja se elige el punto más alto del relieve que no quede pegado a otra cumbre.
Y0, Y1 = 100, 700
band = (Y1 - Y0) / len(PEAKS)
chosen = []
for n in range(len(PEAKS)):
    best = None
    for i in range(N):
        y = i * scale
        if not (Y0 + n * band + 12 <= y < Y0 + (n + 1) * band - 12):
            continue
        for j in range(N):
            x = j * scale
            if 70 < x < SIZE - 260 and all(abs(x - cx) > 260 for _, cx, cy in chosen[-2:]) and (best is None or h[i, j] > best[0]):
                best = (h[i, j], x, y)
    chosen.append(best)                                          # ya quedan de norte (arriba) a sur (abajo)
marks = ""
for (name, alt), (_, x, y) in zip(PEAKS, chosen):
    marks += ('<path d="M%.1f %.1fl5 9h-10z"/><text x="%.1f" y="%.1f">%s · %d M</text>'
              % (x, y - 6, x + 11, y + 4, name.upper(), alt))
peaks_svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" fill="#0A1317" '
             'font-family="JetBrains Mono,ui-monospace,Consolas,Menlo,monospace" font-size="10.5" letter-spacing="1.4">%s</svg>') % (SIZE, SIZE, SIZE, SIZE, marks)
OUT2 = OUT.replace("topo.svg", "topo-peaks.svg")
with open(OUT2, "w", encoding="utf-8", newline=chr(10)) as f:
    f.write(peaks_svg)
print("cumbres:", len(chosen), [(round(x), round(y)) for _, x, y in chosen])
