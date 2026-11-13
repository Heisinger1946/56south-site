---
name: 56south-web
description: Úsala para cualquier cambio, página o pieza visual de Fifty Six South (56°S, go56south.com) - estilo de marca, componentes del sitio y cómo editar, traducir, probar y publicar la web.
---

# Fifty Six South (56°S) — sitio y marca

Antes de diseñar, lee `docs/marca/sistema-de-diseno.md` (reglas de marca) y `docs/estado.md` (qué está pendiente y qué hay en `borrador`). El brief completo está en `docs/marca/brief-de-marca.md`.

## Marca en una pantalla

- Clientes: todo en **inglés**; el sitio se genera también en español y ruso. Nombre, números y "°S" nunca se traducen; en ruso el nombre va en letras latinas.
- Son **"Private Expeditions"**, nunca "packs" ni "tours". Frases cortas y afirmativas, "you" + un "we" discreto, sin signos de exclamación ni emojis.
- Base oscura `ink` #0A1317 con texto `paper` #EEF2F1; un solo acento `accent` #E3A857; cada latitud con su color de zona vía `--z`, solo en elementos de esa expedición.
- Tipografía: Cormorant Garamond (titulares y latitudes), Inter (texto), JetBrains Mono (coordenadas, rótulos, números).
- Botones en píldora; tarjetas con radios 16–20px; foco con contorno `accent` de 2px. Toda animación nueva se apaga con `prefers-reduced-motion`.

## Mapa del sitio (index.html)

- Secciones: header (logo, menú, EN·ES·RU), portada con mapa 3D de Chile (pines `a.pin` con `data-plan`), `#expeditions` (fondo claro: `div.lat-list` con una fila `button.lat-row#tab-NN` por latitud y su `article.plan#plan-NN` debajo, luego rutas `.route`), `#approach` (pilares), `#name`, `#contact` (botones de correo e Instagram; formulario Netlify `enquiry` con trampa `.hp` y reCAPTCHA de Netlify en `div.captcha`), footer.
- Netlify filtra como spam los envíos que parecen texto al azar; para probar el formulario usa un mensaje realista. El reCAPTCHA lo marca Jhon, nunca Claude.
- Scripts al final: animaciones generales, "Vida en el mapa" y "Lista de latitudes".
- Quedan marcadores entre corchetes y `<meta name="robots" content="noindex">` hasta el lanzamiento: no los inventes; pregunta.

## Cómo hacer un cambio

1. Trabaja en la rama `borrador` (`git checkout borrador && git pull`).
2. Edita solo `index.html` (inglés). Nunca edites `es/` ni `ru/` a mano. Lee solo las partes que vas a cambiar (grep por sección).
3. Si agregas o cambias texto visible (o `alt`, `aria-label`, `placeholder`), agrega su traducción en `i18n/es.json` e `i18n/ru.json` (clave = texto en inglés) y corre `python3 tools/build_i18n.py`. Si falla, lista los textos sin traducir: complétalos.
4. Imágenes en `assets/` con rutas `assets/...`; el script las corrige para `/es/` y `/ru/`.
5. Prueba en local: `python3 -m http.server 8756 --bind 127.0.0.1` y abre http://127.0.0.1:8756 (y /es/, /ru/). Revisa errores de consola y que no haya scroll horizontal en escritorio (1440×900) y celular (390×844).
6. Si cambia la estructura, actualiza `README.md`; al terminar, actualiza `docs/estado.md`.
7. Commit en español con `git -c user.name="Jhon Heisinger" -c user.email="noreply@56south.invalid" commit` y `git push origin borrador`. Nunca hagas push a `main` sin la orden de Jhon.
8. Cuando Jhon diga "publica": `git push origin borrador:main` (un solo push con todo junto), espera ~1 minuto y verifica en https://go56south.com. Cuesta 15 créditos; si Netlify ya no publica (créditos agotados), avisa y no lo intentes de nuevo.

## Plantillas de terceros (21st.dev, shadcn, Aceternity…)

Vienen en React/Next.js con Tailwind; el sitio es HTML, CSS y JS simples. No migres el sitio: rehace el efecto en `index.html` con los tokens y clases de la marca, fotos propias y accesibilidad (botones reales, `aria-expanded`, foco visible, versión táctil sin hover).

## Límites

- No cambies configuraciones de Netlify, Porkbun, GitHub ni Google Workspace sin preguntar antes.
- No escribas contraseñas de Jhon; él inicia sesión.
- Antes de usar fotos en material comercial, recuerda que sus licencias están por confirmar.
