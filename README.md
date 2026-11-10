# 56°S — sitio web

Sitio de Fifty Six South (56°S), expediciones privadas en Chile. Es un sitio estático: no tiene base de datos ni servidor, solo archivos.

## Archivos

| Archivo | Qué contiene |
| --- | --- |
| `index.html` | Toda la página: textos, estilos y el script del formulario |
| `assets/hero.mp4`, `assets/hero-poster.jpg` | Video de fondo de la portada (20 s, sin sonido) y la imagen que se ve mientras carga |
| `assets/routes/` | Foto de referencia de cada expedición (960×640) |
| `assets/chile.png` | Silueta de Chile que usa el mapa 3D de la portada |
| `assets/logo-light.png`, `assets/logo-mark-light.png` | Logo para fondo oscuro: completo (pie de página) y sin el lema (menú) |
| `assets/logo-dark.png` | Logo para fondo claro, sin fondo, para otros usos |
| `favicon.png`, `apple-touch-icon.png` | Ícono de la pestaña y del acceso directo en el celular |
| `assets/fonts/` | Tipografías (Space Grotesk, Inter, JetBrains Mono), alojadas en el mismo sitio |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual |

Las fuentes van dentro del sitio y no se cargan desde Google. Así se evitan problemas de privacidad con visitantes europeos (RGPD) y la página no depende de servicios que pueden fallar en Rusia.

## Cómo actualizar

**Opción 1: pedírselo a Claude.** Basta con decir qué cambiar, por ejemplo "agrega el precio de la expedición 23°S" o "suma una expedición a Rapa Nui". Claude edita el archivo y publica el cambio.

**Opción 2: editar en GitHub.** Abre `index.html` en el repositorio, toca el lápiz ("Edit"), cambia el texto y presiona "Commit changes". El sitio se actualiza solo en uno o dos minutos.

Cada cambio queda en el historial del repositorio y se puede deshacer.

Dentro de `index.html`, los comentarios en español (`<!-- ... -->`) marcan cada sección. Los colores de la marca están todos juntos al inicio, en `:root`.

## Mapa y animaciones

El mapa de la portada es `assets/chile.png` apilado en capas para dar volumen. Cada expedición tiene un marcador (`<a class="pin">`) cuya posición se ajusta con `--x` y `--y`, en porcentaje del mapa. Las animaciones se desactivan solas para quien tiene "reducir movimiento" activado en su equipo.

## Antes del lanzamiento

- [ ] Reemplazar todo lo que está entre corchetes: `[PRICE]`, `[DAYS]`, `[YOUR-DOMAIN]`, `[YOUR-NUMBER]`, `[YOUR-HANDLE]`, `[LEGAL NAME]`, `[CITY]`, y los textos de 51°S, 56°S, seguridad e idiomas
- [ ] Comprar el dominio y conectarlo (ver abajo)
- [ ] Borrar la línea `<meta name="robots" content="noindex">` para que Google indexe el sitio
- [ ] Configurar el formulario (ver abajo)
- [ ] Agregar fotos propias de las expediciones
- [ ] Probar que el sitio cargue desde Rusia y desde Europa

## Conectar el dominio propio

1. En el repositorio: Settings › Pages › Custom domain, escribir el dominio (por ejemplo `56south.travel`) y guardar. GitHub crea un archivo `CNAME`.
2. En el registrador del dominio, crear estos registros DNS:
   - Cuatro registros `A` para el dominio raíz: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Un `CNAME` para `www` que apunte a `<usuario>.github.io`
3. Cuando GitHub muestre el dominio como verificado, activar "Enforce HTTPS".

Direcciones según la [documentación de GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), revisada en noviembre de 2026.

## Formulario de contacto

En `index.html`, el formulario (`<form id="enquiry">`) tiene dos atributos:

- `data-email`: el correo que recibe las consultas.
- `data-endpoint`: la dirección de un servicio de formularios, como Formspree. Si queda vacío, el formulario abre el programa de correo del visitante con el mensaje ya escrito.

Con un servicio de formularios, las consultas llegan directo a tu correo sin que el visitante tenga que enviar nada por su cuenta. Para eso, crea el formulario en el servicio y pega su dirección en `data-endpoint`.
