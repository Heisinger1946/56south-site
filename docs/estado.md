# Estado del sitio go56south.com

Actualizado: 19 nov 2026.

## Cómo se trabaja

- Los cambios van a la rama `borrador`; `main` es la página real y cada push a `main` cuesta 15 créditos de Netlify (plan Personal, 1.000 créditos/mes, período 13 nov – 12 dic).
- La vista previa de `borrador` en Netlify (branch deploys) **no está activada**: hoy los cambios se revisan en local (ver la skill `56south-web`). Si Jhon la activa, se verá gratis en https://borrador--go56south.netlify.app.

## En `borrador`, sin publicar

- Nada pendiente (solo este archivo, que no se ve en la web).

## Publicado el 19 nov 2026

- Plan 23°S Atacama reescrito con la propuesta de contenidos (PDF `56S_Atacama_Propuesta_Completa_Helicopteros.pdf`): descripción nueva, 8 experiencias destacadas (antes 4), temporada, estadía, exigencia y cómo llegar actualizados, con helicóptero privado "a pedido". No se publicaron los operadores de helicópteros ni sus teléfonos (el PDF dice que requieren reconfirmación). Traducciones ES/RU al día.

## Publicado el 18 nov 2026 (undécimo envío)

- Titular de la sección de expediciones: "Seven latitudes…" pasó a "Six latitudes. One country. No one else on the route.", con sus traducciones ("Seis latitudes…", "Шесть широт…"), porque con el 47°S fuera quedan seis expediciones. Verificado en el sitio real en inglés y español.

## Publicado el 18 nov 2026 (décimo envío)

- Se quitó la expedición **47°S Fjords & ice**, la ruta premium: su pin en el mapa de la portada, su fila de latitud con el plan, la insignia dorada "Premium" y la opción del formulario. Jhon pidió eliminarla. Con ella se fue todo el estilo premium (`.is-premium`, `.lat-premium`, `.plan-premium`, `.pin-premium` y la animación `premium-shine`) y sus tres traducciones en `i18n/`. Quedan seis latitudes: 23, 33, 34, 35, 39 y 51°S. La foto de Fitz Roy que se usaba ahí ya no se muestra en ninguna parte.
- Contacto: el botón rectangular de Instagram se cambió por un botón redondo (52 px, círculo negro con borde `line-2` y el ícono de Instagram en blanco; al pasar el mouse sube 2 px y se pone ámbar). Pedido por Jhon con una imagen de referencia. El enlace del pie de página sigue igual.

## Publicado el 14 nov 2026 (noveno envío)

- Unión entre la portada y la sección de latitudes: la sección clara ahora es una hoja de esquinas redondeadas (34 px; 24 px en celular) que sube sobre la portada, con sombra hacia arriba y un filo de luz en el borde. Las esquinas de abajo también van redondeadas sobre la sección oscura siguiente. Jhon dejó a criterio elegir entre una difuminación o este resalte con sombra; se probaron los dos y se eligió este.

## Publicado el 14 nov 2026 (octavo envío)

- Mapa de la portada con más vida (14 nov 2026): oleaje que sigue la costa y llega a la orilla, una franja de luz que recorre el relieve, surfistas frente a Pichilemu (bajo el pin 34°S), una manada de tres orcas en el sur, cóndores vistos desde arriba con su sombra (norte, Andes centrales y Patagonia; pueden coincidir dos) y ballenas más grandes y frecuentes. Después se cambió el estilo de la ola del surfista (ahora es una ola llena, con espuma en la cresta, que se levanta y avanza) y se agregó una orca que salta entera del agua cerca de la manada, más o menos en la mitad de las pasadas. Todo dibujado en SVG propio, sin imágenes nuevas. Medido en el sitio real: 100 cuadros por segundo, sin errores, y se pausa cuando el mapa no está a la vista.

## Publicado el 13 nov 2026 (séptimo envío)

- Arreglo: las curvas de nivel se habían publicado quietas (la duración de la animación quedaba en 0 s por un choque de reglas CSS). Ya se mueven en el sitio real: medido a 8 px/s y 100 cuadros por segundo. Lección: comprobar que el dibujo avanza, no solo que la animación figure activa.

## Publicado el 13 nov 2026 (sexto envío)

- Se quitó el fondo de montañas en capas de la sección de latitudes (y `assets/wilderness/`): la sección vuelve a fondo claro. Jhon avisó que la página "se caía" al rato de tenerla abierta; ese fondo sumaba 93 MB de imágenes en memoria (17 capas, cada una con su propia capa 3D), de 48 MB a 141 MB en total. No se pudo reproducir la caída en este PC (16 GB), así que es la causa probable, no confirmada. Si se sigue cayendo, lo siguiente a revisar es la barra Waterline y el mapa 3D de la portada.
- Se mantiene el resalte de las filas de latitudes (sombra y filo de luz), ajustado al fondo claro.
- Barra "Waterline": el agua ya no se dibuja sin parar; se mece unos segundos tras cada movimiento y se detiene.
- Fondo nuevo en la sección de latitudes: curvas de nivel (carta topográfica de la cordillera) en tinta sobre papel, en dos planos, con seis cumbres de Chile y su altura de norte a sur (Licancabur, Tupungato, Villarrica, San Valentín, Paine Grande, Cabo de Hornos; alturas por confirmar). Dibujos propios: `assets/topo.svg` y `assets/topo-peaks.svg`, generados con `tools/topo_svg.py` (88 KB, sin fotos ni licencias). Solo usa `transform`, se pausa fuera de pantalla y se apaga con "reducir movimiento".

## Publicado el 13 nov 2026 (quinto envío)

- Arreglo: los títulos dentro de los planes desplegables (fondo blanco) habían quedado en blanco al oscurecer la sección de latitudes; vuelven a tinta oscura. Ojo al cambiar el color de una sección: los planes (`.plan`) fijan su propio color de texto.

## Publicado el 13 nov 2026 (cuarto envío)

- Transición más suave entre la portada y las latitudes (y entre las latitudes y "Not a tour…"): fundidos largos a `ink`, sin el corte ni la franja oscura.

## Publicado el 13 nov 2026 (tercer envío)

- Sección de latitudes con fondo oscuro y paisaje en capas (montañas y niebla) que se mueve con el cursor o con el scroll; queda fijo mientras se recorre la lista. Las 17 capas están en `assets/wilderness/` (WebP, 2,2 MB). **Vienen de un componente de 21st.dev ("wilderness"): no son de Chile y su licencia no está confirmada.** Jhon las eligió así, sin el texto grande.
- Filas de latitudes con sombra y filo de luz en el borde (dorado en la premium).
- En local, sin subir al repo: `assets/peaks/` y `tools/peaks_layers.py` (alternativa con los Cuernos del Paine recortados de `hero.jpg`, descartada por ahora).

## Publicado el 13 nov 2026 (segundo envío)

- Se quitó la sección "Combine latitudes in one journey" (rutas Essential Chile, End to end y Andean winter) bajo la lista de latitudes. Sus traducciones siguen en `i18n/` por si se recupera.

## Publicado el 13 nov 2026

- Tipografía nueva: titulares y latitudes en Oswald (500/600), texto en IBM Plex Sans (300/400/600), ambas con cirílico. Cormorant Garamond + Inter se probó y no le gustó a Jhon.
- Barra superior "Waterline": gota de agua (WebGL) que marca la sección activa y el idioma; sin WebGL queda el vidrio anterior.
- `_redirects` bloquea en la web los archivos internos (`docs/`, `tools/`, `i18n/`, `.claude/`, `CLAUDE.md`, `README.md`): siguen en el repo pero responden 404. Si se agrega otra carpeta interna, sumarla ahí.

## Pendiente

1. Textos sin completar: "[YOUR SAFETY AND LOGISTICS STANDARD — vehicles, guides, support crew, insurance]" y "[LANGUAGES SPOKEN]".
2. Lanzamiento: quitar `<meta name="robots" content="noindex">` cuando los textos estén completos.
3. Fotos: confirmar licencias antes de uso comercial, incluidas las capas de `assets/wilderness/`.
4. Instagram @go56south: subir la foto de perfil (`docs/marca/56south-instagram-perfil.png`) y el enlace go56south.com desde la app del celular.
5. Sistema de diseño en claude.ai (https://claude.ai/artifact/GDsdkypnFfC6pwJfijZdYd): sigue con Space Grotesk; actualizarlo cuando se publique la nueva tipografía.
6. Opcional: activar Branch deploys para `borrador` en Netlify.

## Ya listo (no repetir)

- Formulario con reCAPTCHA (tema oscuro, idioma de cada página) y aviso por correo a concierge@go56south.com; probado y funcionando.
- Vista previa con logo al compartir el enlace (WhatsApp/redes).
- Correo de Google Workspace con DKIM, DMARC, alias y firma; distintivo "Powered by Netlify" desactivado.
- Netlify filtra como spam los envíos que parecen texto al azar (no avisa por correo).
