# Estado del sitio go56south.com

Actualizado: 13 nov 2026.

## Cómo se trabaja

- Los cambios van a la rama `borrador`; `main` es la página real y cada push a `main` cuesta 15 créditos de Netlify (plan Personal, 1.000 créditos/mes, período 13 nov – 12 dic).
- La vista previa de `borrador` en Netlify (branch deploys) **no está activada**: hoy los cambios se revisan en local (ver la skill `56south-web`). Si Jhon la activa, se verá gratis en https://borrador--go56south.netlify.app.

## En `borrador`, sin publicar

- Se quitó la sección "Combine latitudes in one journey" (rutas Essential Chile, End to end y Andean winter) bajo la lista de latitudes. Sus traducciones siguen en `i18n/` por si se recupera.

## Publicado el 13 nov 2026

- Tipografía nueva: titulares y latitudes en Oswald (500/600), texto en IBM Plex Sans (300/400/600), ambas con cirílico. Cormorant Garamond + Inter se probó y no le gustó a Jhon.
- Barra superior "Waterline": gota de agua (WebGL) que marca la sección activa y el idioma; sin WebGL queda el vidrio anterior.
- `_redirects` bloquea en la web los archivos internos (`docs/`, `tools/`, `i18n/`, `.claude/`, `CLAUDE.md`, `README.md`): siguen en el repo pero responden 404. Si se agrega otra carpeta interna, sumarla ahí.

## Pendiente

1. Textos sin completar: "[YOUR SAFETY AND LOGISTICS STANDARD — vehicles, guides, support crew, insurance]" y "[LANGUAGES SPOKEN]".
2. Lanzamiento: quitar `<meta name="robots" content="noindex">` cuando los textos estén completos.
3. Ruta premium 47°S: confirmar "cabinas hasta 8 huéspedes" y "regreso en avioneta desde Laguna San Rafael".
4. Fotos: confirmar licencias antes de uso comercial. La foto de Fitz Roy (premium) no corresponde a la ruta; se puede cambiar.
5. Instagram @go56south: subir la foto de perfil (`docs/marca/56south-instagram-perfil.png`) y el enlace go56south.com desde la app del celular.
6. Sistema de diseño en claude.ai (https://claude.ai/artifact/GDsdkypnFfC6pwJfijZdYd): sigue con Space Grotesk; actualizarlo cuando se publique la nueva tipografía.
7. Opcional: activar Branch deploys para `borrador` en Netlify.

## Ya listo (no repetir)

- Formulario con reCAPTCHA (tema oscuro, idioma de cada página) y aviso por correo a concierge@go56south.com; probado y funcionando.
- Vista previa con logo al compartir el enlace (WhatsApp/redes).
- Correo de Google Workspace con DKIM, DMARC, alias y firma; distintivo "Powered by Netlify" desactivado.
- Netlify filtra como spam los envíos que parecen texto al azar (no avisa por correo).
