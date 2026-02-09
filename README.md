# Refugio Económico · Policy

Repositorio del portal académico y de política pública de **Refugio Económico**. El sitio está construido con Jekyll y se despliega en GitHub Pages. El objetivo es presentar publicaciones (policy briefs, working papers y proyectos) con una estructura editorial clara y consistente.

## Propósito del proyecto

- Mantener un portal estable y ligero para publicaciones de investigación aplicada.
- Facilitar la navegación por series, proyectos y documentos.
- Conservar una estética editorial sobria (tipografía, color y jerarquía visual) sin frameworks externos.

## Estructura del repositorio

```
refugioeconomico.mx/
├── _config.yml            # Configuración del sitio Jekyll
├── _layouts/
│   └── default.html        # Layout base (header, contenido, footer)
├── assets/
│   ├── css/
│   │   └── style.css       # Estilos globales
│   ├── img/                # Imágenes (logo e ilustraciones)
│   └── pdfs/               # Publicaciones en PDF
├── index.md                # Página principal
├── about.md                # Página sobre el proyecto
├── policy_briefs.md        # Índice de policy briefs
├── working_papers.md       # Índice de working papers
├── projects/               # Páginas de proyectos
└── NAMING.md               # Convenciones de nombres
```

## Organización de layout y estilos

- El layout base vive en `_layouts/default.html` y define la estructura de **header**, **contenido** y **footer**.
- El contenedor compartido `.site-shell` asegura la misma alineación horizontal en todas las secciones.
- Los estilos globales están en `assets/css/style.css` y mantienen tipografía, colores y espaciado editorial.
- Los componentes editoriales principales (hero, cards, navegación) se estilizan desde el mismo archivo CSS para evitar dependencias externas.

## Changelog (resumen)

Para cambios detallados, consulta `CHANGELOG.md`.
