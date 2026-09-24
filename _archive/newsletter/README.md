# Newsletter: referencia no publicada

Material recuperado de `origin/newsletter`, commit
`3ba1f67`, sin activar la sección pública:

- `newsletter.md`: página original.
- `substack-feed.js`: lector original del feed.
- `substack-feed.css`: únicamente el bloque de estilos añadido por esa rama.

No se importaron sus cambios a la portada o navegación. `_archive` está excluido
de Jekyll y estos archivos no se cargan en el portal. Las versiones originales
también permanecen en el historial de la rama `newsletter`.

El lector usa `api.rss2json.com` para convertir RSS de Substack a JSON en el navegador.
No es una fuente de Radar Urbano ni un mecanismo de publicación versionada.
Antes de reutilizarlo habrá que revisar disponibilidad del servicio, validación de
URLs externas y comportamiento sin JavaScript. No contiene credenciales.
