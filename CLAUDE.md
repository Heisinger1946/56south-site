# Fifty Six South (56°S) — proyecto completo

Este repositorio es la casa del proyecto 56°S: el sitio go56south.com y todo el contexto de la marca. Lo mantiene Jhon Heisinger, el fundador. Háblale en español; todo lo que ve el cliente va en inglés.

## Qué es 56°S

Una empresa propia que vende expediciones privadas y no convencionales por Chile (un rally por el desierto, moto de agua hasta los glaciares) a viajeros extranjeros de alto patrimonio, sobre todo europeos y rusos. Opera solo en Chile. Idea de marca: +56 es el código de Chile y el paralelo 56 sur es donde se acaba el mapa. Todo se ordena por latitud, de norte a sur.

- Sitio: https://go56south.com (Netlify, plan Personal, proyecto `go56south`). Dominio en Porkbun.
- Correo: Google Workspace, cuenta principal concierge@go56south.com.
- Instagram: @go56south.
- Ubicación pública: Las Condes, Chile. Decidió no publicar razón social, WhatsApp ni Telegram.

## Dónde está cada cosa

| Ruta | Qué es |
| --- | --- |
| `index.html` | El sitio en inglés (HTML, CSS y JS en un solo archivo). Es lo único que se edita a mano. |
| `es/`, `ru/` | Versiones generadas por `tools/build_i18n.py`. No se editan. |
| `i18n/es.json`, `i18n/ru.json` | Traducciones (clave = texto en inglés). |
| `assets/` | Fotos, mapa, logos y tipografías. |
| `docs/estado.md` | Estado del sitio y pendientes. Léelo al empezar y actualízalo al terminar. |
| `docs/marca/brief-de-marca.md` | Brief: concepto, nombre, catálogo por latitud, mensajes, correos. |
| `docs/marca/sistema-de-diseno.md` | Reglas de color, tipografía, formas, movimiento e imágenes. |
| `docs/marca/56south-instagram-perfil.png` | Foto de perfil de Instagram (el logo no se modifica). |
| `.claude/skills/56south-web/` | Skill con el paso a paso para cambiar, traducir, probar y publicar el sitio. |

## Reglas que no se rompen

- **Publicar cuesta créditos.** Cada push a `main` publica en go56south.com y gasta 15 de los 1.000 créditos mensuales de Netlify. Se trabaja en la rama `borrador` y se publica solo cuando Jhon dice "publica", con un único push que junte todos los cambios.
- Nunca cambies configuraciones de Netlify, Porkbun, GitHub ni Google Workspace sin preguntar antes. No escribas contraseñas; él inicia sesión.
- Antes de usar fotos en material comercial, recuerda que sus licencias están por confirmar.
- No inventes los textos marcados entre corchetes (`[LANGUAGES SPOKEN]`, etc.): pregunta.
- Commits en español, con autor `Jhon Heisinger <noreply@56south.invalid>`.

## Preferencias de Jhon

- Respuestas cortas: qué cambió y dónde verlo.
- No quiere que los PDF ni los Excel salgan siempre con el mismo formato: estilos variados que no se vean hechos con una plantilla.
