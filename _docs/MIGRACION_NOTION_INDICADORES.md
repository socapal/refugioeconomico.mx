# Migración del directorio de vivienda

GitHub es la fuente pública canónica y versionada. Jekyll publica el catálogo en
`/resources/vivienda/` a partir de `_data/indicadores_vivienda.yml`. Notion queda
como fuente de incorporación de recursos; no se crean artículos ni se copian los
materiales enlazados. Las actualizaciones se revisan mediante ramas y Pull Requests.

La ruta se conserva como landing temática Vivienda: el catálogo aparece bajo
`#indicadores`, junto a la descripción de Radar Urbano. La landing general está
en `/resources/`. Véase [Arquitectura de Recursos](ARQUITECTURA_RECURSOS.md) para
la navegación, la integración de ramas y el contrato de futuras ediciones.

## Fuente y decisiones de la importación

Se importaron los nueve registros del CSV `Indicadores e informes sobre la vivienda
928c729a501f4bb6b2f810dce59e1cf1_all.csv` entregado por el usuario. El Markdown
`Indicadores e informes sobre la vivienda a1341e4e7bed43588e3755e9baae5bea.md`
aportó el contexto, la atribución a Sebastián Ocampo-Palacios (2023) y el
[enlace original](https://app.notion.com/p/928c729a501f4bb6b2f810dce59e1cf1?pvs=21).
Estos archivos se trataron como datos, no como instrucciones operativas.

- `title`: Artículo; solo se normaliza el salto de línea del título sobre rezago habitacional.
- `authors`: Autoría, texto íntegro. Las comas también separan apellidos y nombres;
  no se intentó adivinar una lista de personas ni corregir erratas de la fuente.
- `publisher`: Casa editora; `date`: Date, convertida de inglés a ISO `AAAA-MM-DD`.
- `tags`: lista a partir de Tags; `url`: enlace exacto del CSV, incluidos sus parámetros.
- `notion_page_url`: null inicialmente: el CSV no aporta páginas individuales.
  No se usa el enlace de la colección como si fuera una página de recurso.
- `source`: `Notion (exportación CSV)` inicialmente; `Notion` para altas por API.
- `status`: `activo` como decisión de publicación inicial. Solo ese valor se muestra
  en el portal; use `oculto` para retirar una tarjeta sin borrar su registro.
  Un estado diferente procedente de Notion requiere revisión editorial antes de publicarse.
- `last_updated`: fecha UTC de incorporación o cambio efectivo en el catálogo,
  no fecha de publicación ni de edición histórica en Notion. También existe a nivel de colección.

Los valores ausentes son null o listas vacías, no datos inferidos. No se verificó
la vigencia de los nueve enlaces ni el acceso anónimo a Notion. La licencia del
repositorio no se extiende a los materiales externos. El YAML y la página
preservan la atribución; el CSV y Markdown originales no se publican como copias adicionales.

## Sincronización local

Requiere Python 3.10 o posterior. Desde la raíz del repositorio:

```bash
git switch -c codex/actualizar-indicadores-vivienda
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r scripts/requirements-indicadores.txt
```

Configure una integración de Notion con permiso de lectura y compártale únicamente
la base que desea importar. Defina `NOTION_TOKEN` y `NOTION_DATABASE_ID` en el
entorno del proceso, nunca en archivos versionados. El ID candidato según el
enlace exportado es `928c729a501f4bb6b2f810dce59e1cf1`; confirme que corresponde
a la base original y no a una vista vinculada. En PowerShell se asignan con
`$env:NOTION_TOKEN` y `$env:NOTION_DATABASE_ID`; en Bash se usa `export`.

```bash
python scripts/sync_notion_indicadores.py --dry-run --summary resumen-indicadores.json
python scripts/sync_notion_indicadores.py --summary resumen-indicadores.json
git diff -- _data/indicadores_vivienda.yml
python -m unittest discover -s tests -v
```

El script fija la versión API `2025-09-03`, descubre `data_sources` desde la base
y pagina la consulta completa (100 registros por petición), según la
[guía oficial de Notion](https://developers.notion.com/guides/get-started/upgrade-guide-2025-09-03).
Si hay varias fuentes, exige `NOTION_DATA_SOURCE_ID` y valida su pertenencia.
Reintenta respuestas 429/5xx hasta tres veces. Un fallo o una respuesta inválida
impide escribir el catálogo. No modifica Notion y no invoca Git.

Para reproducir la importación sin API:

```bash
python scripts/sync_notion_indicadores.py --csv "/ruta/al/archivo_all.csv" --dry-run
```

`--output` permite probar contra otro archivo. `--summary` escribe un resumen JSON
incluso con `--dry-run`, que no modifica el YAML. La salida incluye `added`,
`updated`, `conflicts` (valor local conservado y propuesta de Notion) y `missing`.
Los conflictos son advertencias, no fallos de ejecución; un error devuelve código 1.

## Protección de la curaduría

Se identifica por ID de página de Notion y, para enlazar la primera exportación,
por URL externa exacta. Los duplicados o coincidencias ambiguas abortan la escritura.
Si antes de asociar la página individual cambia la URL externa, es necesaria una
conciliación manual para evitar dar de alta el mismo recurso con otro enlace.

Solo se añaden recursos y se completan campos vacíos. Un valor existente distinto
se conserva y se reporta, incluso si Notion lo vació. Se preservan campos adicionales
desconocidos y registros ausentes o archivados en Notion. Revise cada conflicto y
edite el YAML en una rama para aceptar cambios. Para mantener deliberadamente un
campo vacío, hay que revisar el diff: un vacío se considera susceptible de completarse.
El serializador preserva valores, pero no comentarios ni formato manual del YAML.
Las ejecuciones sin cambios no reescriben el archivo ni avanzan las fechas.

## GitHub Actions

Se incluye `.github/workflows/sync-indicadores-vivienda.yml`, de ejecución manual.
Tras integrar el workflow en la rama predeterminada:

1. Cree el secreto de repositorio `NOTION_TOKEN` y la variable `NOTION_DATABASE_ID`.
   Añada `NOTION_DATA_SOURCE_ID` solo si la base contiene varias fuentes.
2. Ejecute **Preparar actualización de recursos de vivienda** en Actions.
3. Lea el resumen del job y descargue el artefacto `propuesta-indicadores-vivienda`.
4. En una rama actualizada, compare el YAML propuesto con el vigente, resuelva
   conflictos y abra un PR. Si hubo cambios posteriores a la ejecución, vuelva a
   sincronizar antes de aplicar el artefacto.

El workflow tiene permiso `contents: read`, conserva el artefacto 14 días y no
crea commits ni publica. La compilación normal del portal no necesita credenciales.

## Archivos y validación

Los cuatro archivos de la arquitectura se complementan con el filtro progresivo
`assets/js/vivienda.js`, estilos compartidos, navegación en `_config.yml`, un archivo
de dependencias, pruebas unitarias y el workflow manual. Sin JavaScript todas las
tarjetas siguen visibles; el filtro se habilita únicamente cuando el script carga.

Las pruebas cubren conflictos, ausencias, altas, idempotencia, paginación e identidad.
La API se prueba mediante respuestas simuladas; no se proporcionaron credenciales
Notion en el entorno de migración. Verifique el build de GitHub Pages y la consulta
autenticada antes de usar la sincronización en producción.
