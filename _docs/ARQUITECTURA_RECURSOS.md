# Arquitectura editorial de Recursos

La navegación pública es **Policy Briefs · Working Papers · Recursos · Acerca de**.
La portada reúne los tres primeros bajo Publicaciones. Los enlaces externos
existentes a Substack se conservan como otros espacios; no existe sección pública
Newsletter ni un lector de RSS activo.

## Rutas y contenido

- `/resources/`: landing Recursos, por ahora con una sola categoría: Vivienda.
- `/resources/vivienda/`: landing temática con descripción de Radar Urbano y el
  catálogo completo bajo `#indicadores`. Se conserva la URL citable del catálogo.
- No se generan índices vacíos de Radar ni categorías sin contenido.

Ambas landings usan HTML generado por Jekyll y funcionan sin JavaScript.
Solo el filtro de etiquetas del catálogo es una mejora progresiva.
Las nuevas categorías se incorporarán como páginas Markdown con su propio
permalink y una tarjeta en Recursos; no dependen de la plataforma de origen.

## Radar Urbano: contrato para futuras ediciones

La colección `radar` está configurada con `output: true` y layout `radar`, que
hereda de `page` y `default`. Actualmente no tiene documentos. Cuando exista una
fuente fiable, cada edición será `_radar/YYYY-MM-DD.md`, con front matter:

```yaml
title: Título editorial de la edición
date: YYYY-MM-DD
tags: [Vivienda, Políticas urbanas]
source_url: https://fuente-original-de-la-edicion
```

El nombre ISO del archivo determina la URL estable
`/resources/vivienda/radar/YYYY-MM-DD/`; la fecha declarada debe coincidir con él.
El cuerpo contendrá la edición revisada en Markdown. Este ejemplo documenta el
contrato y no se publica como contenido. Al incorporar ediciones reales, se podrá
añadir el índice `/resources/vivienda/radar/` y enlazarlo desde Vivienda.

La futura sincronización requiere identificar la fuente original en Notion,
propiedades y permisos, así como reglas de selección, revisión, actualización e
identidad de ediciones. No se crean por ahora sincronizadores ni workflows nuevos.

## Integración de ramas

Se compararon las referencias remotas antes de modificar:

- `main` (`7305a0e`): conserva la base del portal.
- `codex/migracion-indicadores-vivienda` (`44041dc`): conserva los nueve recursos,
  script, workflow manual, pruebas y revisiones recientes de nota y cita.
- `newsletter` (`3ba1f67`): recupera únicamente su página, lector y CSS específico
  en `_archive/newsletter/`, excluido del build. No se toman versiones antiguas
  de configuración, portada ni estilos compartidos.

Se preservan los cambios locales de la URL de Notion y la corrección editorial
de Policy Briefs. La copia local `resources/resources.md`, que duplicaba el
permalink de Vivienda, pasa a ser la landing general.

## Google tag

El fragmento solicitado está inmediatamente después de `<head>` en el layout
común. No se inserta en Markdown ni se repite en layouts hijos. La comprobación
esperada por página es una carga de `gtag.js` y una llamada de configuración con
`G-DW1VWDW44B`: dos apariciones literales del ID dentro de una única integración.

## Validación reproducible

Con Ruby/Jekyll disponibles, construir en un destino temporal mediante
`jekyll build --destination RUTA_TEMPORAL --disable-disk-cache --strict_front_matter`.
Para la sincronización, ejecutar `python -m unittest discover -s tests -v` con las
dependencias indicadas en la guía de migración.

Verificar en el HTML generado: navegación y retornos, nueve tarjetas, el ancla
`indicadores`, ausencia de destinos duplicados, de Newsletter y del archivo de
referencia; revisar también Google tag dentro de cada `<head>`. Probar ambas
landings sin JavaScript y el filtro con JavaScript. No cambiar los datos o reglas
del sincronizador como parte de la reorganización editorial.

### Resultado de la integración (23 de septiembre de 2026)

- Jekyll 3.10.0 sobre Ruby portátil 3.3.12: diez páginas compiladas, sin destinos
  duplicados. Se ejecutó `Jekyll::Site#process` con front matter estricto; no se
  necesitó el servidor LiveReload ni se añadieron dependencias al repositorio.
- Nueve pruebas del sincronizador aprobadas; YAML, script y workflow intactos.
- Edge en modo headless: ambas landings navegables sin JavaScript, nueve tarjetas
  visibles; filtro Infonavit con tres resultados y restablecimiento a nueve.
- Diez documentos HTML comprobados: una carga de Google tag y una configuración
  por documento, dentro de `head`. Peticiones externas bloqueadas durante las pruebas.
- Sin enlaces internos a archivos inexistentes; sin publicación de Newsletter,
  `_archive`, categorías vacías o índice de Radar. Sin desbordamiento a 390 px;
  revisión visual de Vivienda en móvil completada.
- Una edición sintética, creada solo en una copia temporal, confirmó la URL por
  fecha de Radar y la herencia de Google tag. No se agregó al repositorio.

La verificación no comprueba disponibilidad de enlaces externos ni recepción de
eventos en la propiedad de Google Analytics. La API autenticada de Notion sigue
pendiente de credenciales; no se necesitó para estos cambios editoriales.
