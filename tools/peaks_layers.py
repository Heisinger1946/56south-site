"""Corta assets/hero.jpg (Cuernos del Paine) en capas para el parallax: cielo, montañas, cerro con guanacos y nieblas."""
import sys, os
import numpy as np, cv2
from PIL import Image, ImageFilter

src, out, dbg = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
img = cv2.imread(src)  # BGR 1740x1160
H, W = img.shape[:2]

def grab(poly_fg, sure_in=35, sure_out=45, extra_fg_boxes=()):
    m = np.zeros((H, W), np.uint8)
    cv2.fillPoly(m, [np.array(poly_fg, np.int32)], 1)
    k_in = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (sure_in * 2 + 1,) * 2)
    k_out = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (sure_out * 2 + 1,) * 2)
    inner = cv2.erode(m, k_in)
    outer = cv2.dilate(m, k_out)
    gc = np.full((H, W), cv2.GC_BGD, np.uint8)
    gc[outer == 1] = cv2.GC_PR_BGD
    gc[m == 1] = cv2.GC_PR_FGD
    gc[inner == 1] = cv2.GC_FGD
    for (x0, y0, x1, y1) in extra_fg_boxes:
        sub = gc[y0:y1, x0:x1]
        sub[sub == cv2.GC_BGD] = cv2.GC_PR_BGD
        sub[sub == cv2.GC_PR_BGD] = cv2.GC_PR_FGD
    bg, fg = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(img, gc, None, bg, fg, 6, cv2.GC_INIT_WITH_MASK)
    res = np.where((gc == cv2.GC_FGD) | (gc == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    # quedarse con la región grande y suavizar el borde
    n, lab, stats, _ = cv2.connectedComponentsWithStats(res)
    keep = np.zeros_like(res)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] > 1500:
            keep[lab == i] = 255
    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    return cv2.GaussianBlur(keep, (0, 0), 1.6)

# Contorno aproximado de los Cuernos (todo lo que está bajo esta línea es montaña o primer plano)
ridge = [(0, 705), (40, 690), (90, 672), (140, 662), (190, 660), (222, 690), (290, 650), (360, 590), (405, 530),
         (410, 410), (450, 360), (490, 310), (540, 262), (600, 242), (680, 245), (725, 270), (770, 240), (850, 195),
         (905, 158), (935, 98), (965, 100), (1005, 130), (1020, 230), (1065, 300), (1095, 340), (1130, 450),
         (1160, 545), (1178, 520), (1195, 380), (1230, 330), (1300, 255), (1345, 238), (1390, 222), (1425, 250),
         (1455, 300), (1520, 345), (1560, 400), (1620, 445), (1690, 455), (1740, 470)]
mount_poly = ridge + [(W, H), (0, H)]
guanacos = [(320, 675, 435, 830), (760, 770, 905, 862), (880, 800, 985, 862), (1215, 845, 1275, 880)]

# Línea del cerro: por columna, primera fila (desde 760) con vegetación (oscura, saturada, tono oliva/café)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
veg = ((hsv[..., 2] < 150) & (hsv[..., 1] > 45) & (hsv[..., 0] > 8) & (hsv[..., 0] < 40)).astype(np.uint8)
veg = cv2.morphologyEx(veg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
top = np.zeros(W, int)
for x in range(W):
    col = veg[760:, x]
    run = np.convolve(col, np.ones(12), "valid")  # 12 px seguidos de vegetación
    idx = np.argmax(run >= 10) if (run >= 10).any() else H - 760
    top[x] = 760 + idx
top = cv2.medianBlur(top.astype(np.uint8 if top.max() < 256 else np.uint16).reshape(1, -1).astype(np.float32), 5).ravel().astype(int) if False else top
top = np.array(np.convolve(np.pad(top, 15, mode="edge"), np.ones(31) / 31, "valid"), int)
hill_poly = [(x, int(top[x]) - 6) for x in range(0, W, 6)] + [(W - 1, int(top[-1]) - 6), (W, H), (0, H)]

m_mount = grab(mount_poly)
m_hill = grab(hill_poly, sure_in=25, sure_out=25, extra_fg_boxes=guanacos)
# guanacos: el recorte de GrabCut dentro de sus cajas
m_mount = np.maximum(m_mount, m_hill)  # la montaña incluye todo lo de abajo

def inpaint(mask, scale=4, grow=25):
    """Rellena la zona tapada por la capa de delante (se ve solo en los bordes cuando las capas se mueven)."""
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (grow * 2 + 1,) * 2)
    mk = cv2.dilate((mask > 40).astype(np.uint8) * 255, k)
    small = cv2.resize(img, (W // scale, H // scale), interpolation=cv2.INTER_AREA)
    ms = cv2.resize(mk, (W // scale, H // scale), interpolation=cv2.INTER_NEAREST)
    fill = cv2.inpaint(small, ms, 9, cv2.INPAINT_TELEA)
    fill = cv2.GaussianBlur(fill, (0, 0), 3)
    fill = cv2.resize(fill, (W, H), interpolation=cv2.INTER_CUBIC)
    a = (cv2.GaussianBlur(mk, (0, 0), 6) / 255.0)[..., None]
    return (img * (1 - a) + fill * a).astype(np.uint8)

sky = inpaint(m_mount)
mount_rgb = inpaint(m_hill, grow=18)

S = 2200 / W  # se escala a 2200 px de ancho para dejar margen al movimiento
def save_rgb(arr, name, q=80):
    im = Image.fromarray(cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)).resize((2200, round(H * S)), Image.LANCZOS)
    im.save(os.path.join(out, name), quality=q, method=6)
def save_rgba(arr, alpha, name, q=82):
    rgba = np.dstack([cv2.cvtColor(arr, cv2.COLOR_BGR2RGB), alpha])
    im = Image.fromarray(rgba, "RGBA").resize((2200, round(H * S)), Image.LANCZOS)
    bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop((0, bbox[1], im.width, im.height))  # recorta el aire de arriba
    im.save(os.path.join(out, name), quality=q, method=6)
    return bbox[1]

save_rgb(sky, "sky.webp")
ym = save_rgba(mount_rgb, m_mount, "mountains.webp")
yh = save_rgba(img, m_hill, "hill.webp")

# Nieblas: ruido suave, blanco con alfa, horizontal
rng = np.random.default_rng(56)
def fog(name, w, h, blobs, seed_scale):
    a = np.zeros((h, w), np.float32)
    for _ in range(blobs):
        cx, cy = rng.uniform(0.05, 0.95) * w, rng.uniform(0.35, 0.7) * h
        rx, ry = rng.uniform(0.08, 0.22) * w, rng.uniform(0.12, 0.3) * h
        yy, xx = np.ogrid[:h, :w]
        a += np.exp(-(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)) * rng.uniform(0.4, 1)
    noise = cv2.resize(rng.random((h // seed_scale, w // seed_scale)).astype(np.float32), (w, h), interpolation=cv2.INTER_CUBIC)
    noise = cv2.GaussianBlur(noise, (0, 0), 6)
    a = a * (0.55 + 0.9 * noise)
    edge = np.minimum(np.linspace(0, 1, h)[:, None] * 4, 1) * np.minimum(np.linspace(1, 0, h)[:, None] * 4, 1)
    a = np.clip(a / a.max() * edge * 235, 0, 255).astype(np.uint8)
    rgba = np.dstack([np.full((h, w, 3), (236, 242, 244), np.uint8), a])
    Image.fromarray(rgba, "RGBA").save(os.path.join(out, name), quality=70, method=6)

fog("fog-1.webp", 2400, 420, 14, 24)
fog("fog-2.webp", 1800, 360, 10, 20)
fog("fog-3.webp", 1400, 300, 8, 16)

# Vista de control
prev = img.copy()
prev[m_mount < 128] = (prev[m_mount < 128] * 0.3 + np.array([255, 0, 255]) * 0.7).astype(np.uint8)
hm = (m_hill > 128) & (m_mount >= 128)
prev[hm] = (prev[hm] * 0.6 + np.array([0, 255, 255]) * 0.4).astype(np.uint8)
cv2.imwrite(dbg, cv2.resize(prev, (1160, 773)))
print("offsets (px en 2200 de ancho):", "montañas", ym, "cerro", yh, "alto total", round(H * S))
for f in sorted(os.listdir(out)):
    print(f, os.path.getsize(os.path.join(out, f)) // 1024, "KB")
