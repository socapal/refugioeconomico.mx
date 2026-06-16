# Guia tecnica para integrar Refugio Economico en RePEc

Este documento aterriza la guia del archivo "Ecosistema REC - Deliberacion" en una estructura util dentro del repositorio. La idea es que REC pueda publicar metadata ReDIF en su propio dominio sin romper las convenciones de `NAMING.md`.

Tambien incorpora una verificacion puntual contra la documentacion oficial de RePEc para respetar los nombres de archivo, la ubicacion de las series y los campos validos de ReDIF.

## Objetivo

- Preparar una ruta publica estable en `https://policy.refugioeconomico.mx/repec/`.
- Mantener los PDF en el portal de REC y separar su versionado de los handles de RePEc.
- Dejar una base clara para la serie de working papers y reservar otras series hasta que su numeracion quede cerrada.

## Decisiones operativas

- Codigo de archivo sugerido: `rec`
- Handle base del archivo: `RePEc:rec`
- Serie activa inicial: `RePEc:rec:wpaper`
- Codificacion de metadata: ASCII o Latin-1; preferir ASCII en todos los `.rdf`
- Los archivos `.rdf` solo describen metadata y ligas; no alojan el PDF
- El `Handle` RePEc nunca debe incluir la version del PDF
- Las series viven juntas en `recseri.rdf`; las carpetas como `wpaper/` guardan solo metadata de items
- El sufijo de serie debe tener exactamente seis caracteres en minusculas o numeros

## Estructura sugerida

```text
repec/
|-- guia-tecnica-repec.md
`-- rec/
    |-- recarch.rdf.template
    |-- recseri.rdf.template
    |-- pbrief/
    |   `-- README.md
    `-- wpaper/
        `-- document.rdf.template
```

Cuando REC quede listo para registrar el archivo ante RePEc, los `.template` pueden copiarse a sus nombres finales:

- `repec/rec/recarch.rdf`
- `repec/rec/recseri.rdf`
- `repec/rec/wpaper/YYYY-##.rdf`

## Flujo recomendado para un nuevo working paper

1. Publicar el PDF en `assets/pdfs/` con la convencion `REC-WP-YYYY-##-[slug]-vX.Y.pdf`.
2. Confirmar que exista una URL canonica del documento y una pagina de serie en `/working-papers/`.
3. Copiar `repec/rec/wpaper/document.rdf.template` a `repec/rec/wpaper/YYYY-##.rdf`.
4. Llenar `Title`, `Abstract`, `Keywords`, `Classification-JEL`, `Creation-Date`, `Number`, `File-URL` y `Handle`.
5. Validar el archivo antes de publicarlo.
6. Subir tanto el PDF como los `.rdf` en el mismo cambio para evitar ligas rotas.

## Regla de oro para la persistencia

El identificador de RePEc debe quedarse estable aunque el PDF cambie de version.

Ejemplo:

- PDF inicial: `REC-WP-2026-01-anps-v1.0.pdf`
- PDF corregido: `REC-WP-2026-01-anps-v1.1.pdf`
- Handle estable: `RePEc:rec:wpaper:2026-01`

Si cambia la version del PDF, se actualiza `File-URL` en el `.rdf`, pero no el `Handle`.

## Alineacion con `NAMING.md`

### Working Papers

Esta serie ya esta suficientemente definida en el repo:

- Codigo publico: `REC-WP-YYYY-##`
- PDF: `REC-WP-YYYY-##-[slug]-vX.Y.pdf`
- Number en ReDIF: `YYYY-##`
- Handle en RePEc: `RePEc:rec:wpaper:YYYY-##`

### Policy Briefs

Hoy el repo usa `REC-PB-###`, sin anio en el identificador publico. Eso vuelve ambigua una traduccion directa a RePEc si se quisiera forzar una numeracion tipo `YYYY-##`.

Por ahora la recomendacion operativa es:

- mantener `REC-PB-###` como convencion publica interna;
- reservar `repec/rec/pbrief/` sin publicar metadata final;
- decidir primero si la numeracion RePEc de briefs sera anual, absoluta o si la serie no se indexara;
- recordar que, si se activan en RePEc, tendrian que vivir bajo un tipo oficial como `ReDIF-Paper`, no como una categoria propia de policy brief.

### Datasets

Antes de publicar datasets en RePEc, REC necesita:

- decidir si RePEc es el lugar correcto para esa serie, porque los tipos oficiales disponibles no incluyen un tipo nativo para datasets;
- elegir un handle de seis caracteres para la serie, si se llegara a activar;
- crear una pagina publica y permanente para datasets;
- fijar una regla estable para citacion, versionado y formato de archivo.

## Notas sobre despliegue

- GitHub Pages sirve archivos estaticos como `.rdf`, asi que la ruta `repec/` puede convivir con el sitio Jekyll.
- RePEc acepta `.rdf` en ISO-LATIN-1 o Windows-1252 y `.redif` en UTF-8; para REC conviene mantener `.rdf` en ASCII mientras arranca la integracion.
- Evita acentos, enes con tilde y caracteres especiales dentro de los `.rdf`.
- Si un PDF aun no existe en su URL final, no publiques el `.rdf`.

## Validacion

- Tutorial RePEc: <https://ideas.repec.org/t/rdfintro.html>
- Validador RePEc: <https://ideas.repec.org/cgi-bin/validate>

## Siguiente paso recomendado

El siguiente hito razonable es crear el primer `.rdf` real para el working paper que ya tenga PDF canonico publicado en `assets/pdfs/`.
