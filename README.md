# 56°S — sitio web

Sitio de Fifty Six South (56°S), expediciones privadas en Chile. Es un sitio estático: no tiene base de datos ni servidor, solo archivos.

## Archivos

| Archivo | Qué contiene |
| --- | --- |
| `index.html` | Toda la página: textos, estilos y el script del formulario |
| `assets/hero.jpg` | Imagen de fondo de la portada |
| `assets/routes/` | Foto de cada plan |
| `assets/chile.png` | Silueta de Chile que usa el mapa 3D de la portada |
| `assets/chile-relief.jpg` | Relieve real de Chile (Natural Earth, dominio público) ajustado a la silueta |
| `assets/logo-light.png`, `assets/logo-mark-light.png` | Logo para fondo oscuro: completo (pie de página) y sin el lema (menú) |
| `assets/logo-dark.png` | Logo para fondo claro, sin fondo, para otros usos |
| `favicon.png`, `apple-touch-icon.png` | Ícono de la pestaña y del acceso directo en el celular |
| `assets/fonts/` | Tipografías (Space Grotesk, Inter, JetBrains Mono), alojadas en el mismo sitio |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual |

Las fuentes van dentro del sitio y no se cargan desde Google. Así se evitan problemas de privacidad con visitantes europeos (RGPD) y la página no depende de servicios que pueden fallar en Rusia.

## Cómo actualizar

**Opción 1: pedírselo a Claude.** Basta con decir qué cambiar, por ejemplo "agrega el precio de la expedición 23°S" o "suma una expedición a Rapa Nui". Claude edita el archivo y publica el cambio.

**Opción 2: editar en GitHub.** Abre `index.html` en el repositorio, toca el lápiz ("Edit"), cambia el texto y presiona "Commit changes". Netlify publica el cambio en go56south.com en uno o dos minutos.

Cada cambio queda en el historial del repositorio y se puede deshacer.

Dentro de `index.html`, los comentarios en español (`<!-- ... -->`) marcan cada sección. Los colores de la marca están todos juntos al inicio, en `:root`.

## Expediciones

Hay seis planes, uno por latitud: 23°S Atacama, 33°S The Andes, 34°S Pacific, 35°S Wine valleys, 39°S Lakes & volcanoes y 51°S Patagonia. En `index.html` cada uno es un bloque `<article class="plan" id="plan-23">` (el número es la latitud) con su botón `tab-23` y su marcador en el mapa (`data-plan="23"`). Para cambiar la foto de un plan, guarda la imagen nueva en `assets/routes/` y cambia el `src` del `<img>` que está dentro de su `<div class="plan-visual">`. El `object-position` de ese `<img>` indica qué parte de la foto queda visible cuando se recorta.

## Mapa y animaciones

El mapa de la portada es `assets/chile.png` apilado en capas para dar volumen, con el relieve real encima. Cada expedición tiene un marcador (`<a class="pin">`) cuya posición se ajusta con `--x` y `--y`, en porcentaje del mapa. Las animaciones se desactivan solas para quien tiene "reducir movimiento" activado en su equipo.

## Antes del lanzamiento

- [ ] Reemplazar todo lo que está entre corchetes: `[PRICE]`, `[DAYS]`, `[YOUR-DOMAIN]`, `[YOUR-NUMBER]`, `[YOUR-HANDLE]`, `[LEGAL NAME]`, `[CITY]`, y los textos de 51°S, 56°S, seguridad e idiomas
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
