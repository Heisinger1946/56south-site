# 56°S — Sistema de diseño (resumen)

Copia de trabajo de las reglas del sistema de diseño de claude.ai (https://claude.ai/artifact/GDsdkypnFfC6pwJfijZdYd). Los valores reales viven en el `:root` y el CSS de `index.html`; si hay diferencia, manda el sitio.

## Contenido y voz

- Todo lo que ve el cliente va en **inglés**. El sitio se traduce a español y ruso, pero el nombre, los números y "°S" nunca se traducen ni se transliteran: en ruso el nombre va en letras latinas.
- Las experiencias son **"Private Expeditions"**, nunca "packs", "tours" ni "paquetes".
- Frases cortas y afirmativas, en segunda persona ("you") con un "we" discreto. Sin signos de exclamación, sin emojis, sin superlativos de folleto.
- Copia que marca el tono: "Where the map runs out." · "Not a tour. An expedition built for one party." · "Tell us which latitude." / "We reply personally."
- Formas del nombre: en textos y web, **56 South**; logo, **56°S**; descriptor, **56°S — Private Expeditions, Chile**. Cada expedición se nombra por su latitud: "23°S Atacama".
- Botones con verbo primero y mayúscula solo inicial: "Plan your expedition", "Send enquiry", "Enquire about 23°S".

## Color

| Token | Valor | Uso |
| --- | --- | --- |
| `ink` | #0A1317 | Fondo base |
| `ink-2` | #101C21 | Campos, superficies |
| `paper` | #EEF2F1 | Texto sobre ink; fondo de la sección de expediciones (`.light`) |
| `text-dim` / `text-mute` | #C9D3D4 / #9FB0B3 | Texto secundario / terciario |
| `text-on-paper` | #3B4A4E | Texto secundario sobre paper |
| `line` / `line-2` | #25353A / #5B6E72 | Divisores decorativos / bordes que deben verse |
| `accent` | #E3A857 | Único acento: un botón principal por vista, eyebrow, pines, números de pilares, foco. Texto encima siempre ink; nunca como texto sobre paper |

Colores de zona (solo en elementos de su expedición, pasados con `--z:var(--zone-NN)`): `zone-23` #B4531F, `zone-33` #1F6FA3, `zone-34` #0E7C78, `zone-35` #8E3B5E, `zone-39` #2F7A4A, `zone-47` #8A5A1C (ruta premium, píldora dorada "Premium"), `zone-51` #2F5FA8.

## Tipografía

Nueva tipografía en la rama `borrador` (13 nov 2026, sin publicar todavía):

- `display`: **Oswald** 500 (h1, h2, latitudes y correo de contacto) y 600 (h3, títulos de plan y rutas). Sans condensada, estilo aventura/alpino; sin cursiva. Cifras de línea (`lining-nums`). Trae cirílico. Elegida por Jhon el 13 nov 2026 (antes: Cormorant Garamond, que no le gustó).
- `body`: **IBM Plex Sans** 300 (lead), 400 (texto) y 600 (énfasis, botones). Trae cirílico.
- `mono`: **JetBrains Mono** para coordenadas, números y rótulos (eyebrow, kicker, fact-label), en mayúsculas con interletrado amplio.

Hasta que se publique, `main` sigue con Space Grotesk 700 en titulares (Manrope para cirílico).

## Espaciado y diagramación

- Contenido centrado con ancho máximo `wrap` (1240px) y márgenes de 32px, 20px bajo 640px.
- Secciones con 104px arriba y abajo (72px en móvil).
- Cortes: 1000px (planes y rutas a una columna), 768px (la lista de latitudes deja de abrirse con hover) y 640px (móvil).

## Formas, bordes y sombras

- Botones, selector de idioma e insignias en píldora. Tarjetas con radios 16px (rutas) y 20px (ficha del plan, foto de fila abierta). Campos y fotos chicas, 6px.
- Sombras largas, suaves, color ink con dispersión negativa, solo sobre fondos claros. Sobre ink no hay sombras, salvo el halo ámbar del botón principal.
- Foco: contorno sólido accent de 2px separado 3px.

## Movimiento

- Curva de marca `cubic-bezier(.2,.7,.2,1)`, 0.3–0.9 s. Hover: botones suben 2px, tarjetas 4px, fotos se acercan levemente.
- Lista de latitudes: `cubic-bezier(.25,1,.5,1)` en 0.7 s; la fila crece hasta 400px y la foto pasa de 110% a 100%.
- Portada: mapa 3D de Chile que se mece, paralelos que avanzan detrás y vida sutil (ballenas, gaviotas, cóndor, viento), nunca todo a la vez.
- Sección de latitudes: curvas de nivel en tinta (13 % y 6 % de opacidad) que derivan de lado en 150–260 s, con cumbres de Chile rotuladas en mono. Solo `transform`; nada de fotos de fondo ni capas 3D (el fondo de montañas en capas se quitó por pesado).
- Los bloques entran al hacer scroll. Con "reducir movimiento" se apaga toda animación.

## Imágenes e iconografía

- Fotos reales de cada destino, en paisaje, con degradado ink para que el texto se lea.
- Sin set de íconos ni emojis. Marcas gráficas: el logo, el pin (punto blanco con anillo accent que late) y la flecha de la lista de latitudes (SVG de trazo 1.8px en círculo de 44px).
- Logos PNG claros y oscuros; no se recolorean.

## Componentes del sitio

`btn` (solid, line, ghost, ink), `langs`, `site-header`, `section-head`, `pin`, `lat-list`, `plan`, `route`, `pillar`, `field`, `site-footer`. Las piezas de una expedición reciben su color con `--z`.
