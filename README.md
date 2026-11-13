# 56°S — sitio web

Sitio de Fifty Six South (56°S), expediciones privadas en Chile. Es un sitio estático: no tiene base de datos ni servidor, solo archivos.

## Archivos

| Archivo | Qué contiene |
| --- | --- |
| `index.html` | Toda la página en inglés: textos, estilos y el script del formulario |
| `es/`, `ru/` | Versiones en español y ruso, generadas con `tools/build_i18n.py` |
| `i18n/` | Traducciones al español y al ruso |
| `assets/hero.jpg` | Imagen de fondo de la portada |
| `assets/routes/` | Foto de cada plan |
| `assets/chile.png` | Silueta de Chile que usa el mapa 3D de la portada |
| `assets/chile-relief.jpg` | Relieve real de Chile (Natural Earth, dominio público) ajustado a la silueta |
| `assets/chile-shadow.png` | Sombra difusa del mapa, ya desenfocada (más liviana que calcularla en el navegador) |
| `assets/logo-light.png`, `assets/logo-mark-light.png` | Logo para fondo oscuro: completo (pie de página) y sin el lema (menú) |
| `assets/logo-dark.png` | Logo para fondo claro, sin fondo, para otros usos |
| `favicon.png`, `apple-touch-icon.png` | Ícono de la pestaña y del acceso directo en el celular |
| `assets/fonts/` | Tipografías (Cormorant Garamond para titulares, Inter para texto, JetBrains Mono para rótulos), alojadas en el mismo sitio |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual |
| `CLAUDE.md`, `.claude/skills/`, `docs/` | Contexto del proyecto para Claude Code: marca, estado, pendientes y cómo trabajar. No es parte de la página |

Las fuentes van dentro del sitio y no se cargan desde Google. Así se evitan problemas de privacidad con visitantes europeos (RGPD) y la página no depende de servicios que pueden fallar en Rusia.

## Cómo actualizar

**Opción 1: pedírselo a Claude.** Basta con decir qué cambiar, por ejemplo "agrega el precio de la expedición 23°S" o "suma una expedición a Rapa Nui". Claude edita el archivo y publica el cambio.

**Opción 2: editar en GitHub.** Abre `index.html` en el repositorio, toca el lápiz ("Edit"), cambia el texto y presiona "Commit changes". Netlify publica el cambio en go56south.com en uno o dos minutos.

Cada cambio queda en el historial del repositorio y se puede deshacer.

Dentro de `index.html`, los comentarios en español (`<!-- ... -->`) marcan cada sección. Los colores de la marca están todos juntos al inicio, en `:root`.

## Idiomas

El sitio está en tres idiomas, con botones EN · ES · RU en el menú:

| Idioma | Dirección | Archivo |
| --- | --- | --- |
| Inglés (original) | go56south.com | `index.html` |
| Español | go56south.com/es/ | `es/index.html` (generado) |
| Ruso | go56south.com/ru/ | `ru/index.html` (generado) |

**Solo se edita `index.html`.** Las versiones en español y ruso se generan con:

```
py tools/build_i18n.py
```

El script toma cada texto en inglés y lo reemplaza por su traducción de `i18n/es.json` e `i18n/ru.json`. Si cambias o agregas un texto en `index.html`, agrega su traducción en los dos JSON y vuelve a ejecutar el script: te avisa qué textos quedaron sin traducir. Los mensajes del formulario en los tres idiomas están en el script de la página (`var ALL = {...}`).

Cada consulta del formulario trae un campo `language` (en, es o ru), y el valor de la expedición siempre llega en inglés, para que sepas qué eligió el cliente aunque haya escrito en ruso.

Cormorant Garamond e Inter traen letras cirílicas, así que el ruso usa las mismas tipografías. (Los archivos de Space Grotesk y Manrope quedan en `assets/fonts/` pero ya no se cargan.)

## Expediciones

Hay siete planes, uno por latitud: 23°S Atacama, 33°S The Andes, 34°S Pacific, 35°S Wine valleys, 39°S Lakes & volcanoes, 47°S Fjords & ice (la ruta premium, en yate privado, marcada con `is-premium`) y 51°S Patagonia. Se muestran como una lista (`<div class="lat-list">`): cada fila es un `<button class="lat-row" id="tab-23">` (el número es la latitud) con su foto, y justo debajo va su plan, `<article class="plan" id="plan-23">`, que se despliega al hacer clic. En pantallas con mouse la fila se abre con la foto al pasar por encima. Los marcadores del mapa (`data-plan="23"`) y los tramos de las rutas abren el plan que corresponde. Para cambiar la foto de un plan, guarda la imagen nueva en `assets/routes/` y cambia el `src` del `<img>` que está dentro de su `<span class="lat-photo">`; el `object-position` de ese `<img>` indica qué parte de la foto queda visible cuando se recorta.

## Mapa y animaciones

El mapa de la portada es `assets/chile.png` apilado en capas para dar volumen, con el relieve real encima. Cada expedición tiene un marcador (`<a class="pin">`) cuya posición se ajusta con `--x` y `--y`, en porcentaje del mapa. Las animaciones se desactivan solas para quien tiene "reducir movimiento" activado en su equipo.

Sobre el mapa hay tres capas decorativas (`.map-fx`) con vida que aparece y se va sola, a ratos distintos:
ballenas que asoman en el sur (onda, lomo, soplido y cola), gaviotas que planean por la costa (a veces de a dos),
un cóndor que da vueltas sobre la cordillera del norte y ráfagas de viento que corren por los Andes.
Todo lo genera el script "Vida en el mapa" al final de `index.html`; ahí se cambian la frecuencia (`every(...)`)
y las zonas. Se pausa cuando el mapa no está en pantalla y no aparece con "reducir movimiento".

## Antes del lanzamiento

- [ ] Reemplazar todo lo que está entre corchetes: `[PRICE]`, `[DAYS]`, y los textos de 51°S, 56°S, seguridad e idiomas
- [x] Comprar el dominio y conectarlo
- [ ] Borrar la línea `<meta name="robots" content="noindex">` para que Google indexe el sitio
- [x] Configurar el formulario (Netlify Forms)
- [ ] Agregar fotos propias de las expediciones
- [ ] Probar que el sitio cargue desde Rusia y desde Europa

## Hosting y dominio

- **Sitio:** https://go56south.com (www.go56south.com redirige ahí). HTTPS automático.
- **Hosting:** Netlify, proyecto `go56south`. Publica solo cada cambio que entra a la rama `main` de este repositorio.
- **Dominio:** go56south.com, registrado en Porkbun, con renovación automática y privacidad WHOIS.
- **DNS en Porkbun:** `ALIAS` en la raíz → `apex-loadbalancer.netlify.com`; `CNAME www` → `go56south.netlify.app`. Los registros `MX` y `TXT` de Porkbun quedan para el reenvío de correo.

## Formulario de contacto

El sitio está alojado en Netlify y el formulario usa Netlify Forms (`data-netlify="true"` en `<form id="enquiry">`). Cada consulta queda guardada en Netlify (Forms › enquiry) y llega por correo a la cuenta de Netlify. Para cambiar a quién llega: Project configuration › Notifications › Emails and webhooks › Form submission notifications.

El campo oculto `website` es una trampa anti-spam: si un bot lo llena, Netlify descarta la consulta.
