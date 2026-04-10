---
layout: default
title: Inicio
---

<div class="hero">
  <h1>Economía pública para el bien común.</h1>
  <p>Investigaciones breves y accesibles sobre políticas públicas, vivienda, trabajo y bienestar social—con rigor, datos y vocación cívica.</p>
</div>

<div class="card">
  <strong>Leer en Substack:</strong>
  <a href="{{ site.substack_rec }}">Refugio Económico</a> ·
  <a href="{{ site.substack_pc }}">Punto Común</a>
</div>

<div class="card">
  <strong>Archivo y código:</strong>
  <a href="{{ site.github_profile }}">GitHub</a> ·
  <a href="{{ site.notion_publications }}">Publicaciones (Notion)</a>
</div>

# Refugio Económico · Policy

Portal de publicaciones de investigación aplicada para decisiones públicas.

🌐 **Sitio:** https://policy.refugioeconomico.mx/

---

## 📚 Contenido

Este repositorio contiene:

- **Policy Briefs:** Documentos ejecutivos (4-6 páginas) con hallazgos y recomendaciones
- **Working Papers:** Investigaciones técnicas con metodología detallada
- **Datasets:** Bases de datos curadas y documentadas
- **Código:** Scripts de replicación en R/Python

---

## 🗂️ Estructura

```
refugio-economico-policy/
├── README.md                      # Este archivo
├── NAMING.md                     # Convenciones oficiales (LEER PRIMERO)
├── _config.yml                    # Configuración Jekyll
├── index.md                       # Página principal
├── policy_briefs.md              # Lista de policy briefs
├── working_papers.md             # Lista de working papers
├── about.md                      # Sobre REC
├── projects/                     # Páginas de proyectos
│   └── anps-v1.md               # Proyecto ANPs v1.0
├── assets/
│   ├── css/
│   │   └── style.css            # Estilos personalizados
│   ├── pdfs/                    # PDFs de publicaciones
│   │   ├── REC-PB-001-*.pdf
│   │   └── REC-WP-2025-01-*.pdf
│   └── img/                     # Imágenes y figuras
├── data/                        # Datasets o links
└── code/                        # Código replicable o links
```

---

## 🚀 Activar GitHub Pages

### Paso 1: Crear el repositorio

1. Ve a GitHub y crea un nuevo repositorio
2. Nómbralo: `policy` (o el nombre que prefieras)
3. Hazlo público
4. Inicializa con README

### Paso 2: Subir los archivos

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/policy.git
cd policy

# Copiar todos los archivos de este proyecto
# (Los archivos que te proporcioné)

# Commit y push
git add .
git commit -m "Initial commit: Portal REC Policy"
git push origin main
```

### Paso 3: Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Click en `Settings` (Configuración)
3. En el menú lateral, click en `Pages`
4. En "Source", selecciona:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click en `Save`
6. Espera 1-2 minutos

### Paso 4: Configurar dominio personalizado

**Para usar `policy.refugioeconomico.mx`:**

1. En GitHub Pages settings, agrega: `policy.refugioeconomico.mx`
2. En tu proveedor DNS (donde compraste refugioeconomico.mx), agrega:
   ```
   Tipo: CNAME
   Nombre: policy
   Valor: tu-usuario.github.io
   ```
3. Espera 10-30 minutos para propagación DNS
4. Activa "Enforce HTTPS" en GitHub
5. Tu sitio estará en: `https://policy.refugioeconomico.mx/`

---

## ✍️ Agregar nuevas publicaciones

### Policy Brief (Ejemplo: REC-PB-002)

**1. Agrega el PDF:**
```bash
# Coloca el PDF en assets/pdfs/
assets/pdfs/REC-PB-002-[slug]-v1.0.pdf
```

**2. Actualiza `policy-briefs.md`:**

```markdown
## 📄 REC-PB-002 · Enero 2026

### [Título del Brief]({{ '/projects/[slug]/' | relative_url }})

**Subtítulo descriptivo**

<div class="publication-meta">
  <span class="code">REC-PB-002</span> · 
  Tu Nombre · 
  Enero 2026
</div>

**En una mirada:**
- Hallazgo 1
- Hallazgo 2
- Hallazgo 3

**Temas:** Tag1 · Tag2 · Tag3  
**Metodología:** Método usado  
**JEL Codes:** X00, Y11

<div class="publication-links">
  <a href="{{ '/assets/pdfs/REC-PB-002-[slug]-v1.0.pdf' | relative_url }}" class="btn">📄 PDF</a>
  <a href="{{ '/projects/[slug]/' | relative_url }}" class="btn btn-secondary">📋 Proyecto</a>
</div>

---
```

**3. Crea página del proyecto (opcional):**
```bash
# Copia projects/anps-v1.md como plantilla
cp projects/anps-v1.md projects/[nuevo-slug].md
# Edita el contenido
```

**4. Commit y push:**
```bash
git add .
git commit -m "Add REC-PB-002: [Título]"
git push origin main
```

### Working Paper (Ejemplo: REC-WP-2026-01)

Sigue el mismo proceso pero en `working-papers.md`.

---

## 📝 Convenciones de naming

**⚠️ IMPORTANTE: Lee `NAMING.md` antes de agregar nuevas publicaciones.**

### Resumen rápido:

**Policy Briefs:**
```
REC-PB-###-<slug>-vX.Y.pdf
Ejemplo: REC-PB-001-anps-v1.0.pdf
```

**Working Papers:**
```
REC-WP-YYYY-##-<slug>-vX.Y.pdf
Ejemplo: REC-WP-2026-01-anps-v1.0.pdf
```

**Slugs:**
- Minúsculas, sin acentos, sin espacios
- Máximo 3-4 palabras
- Ejemplos: `anps`, `vivienda-social`, `desastres-sismicos`

---

## 🎨 Personalización

### Colores

Edita en `_config.yml`:
```yaml
colors:
  verde: "#013D1F"
  rosa: "#DB647F"
  fondo: "#F6F5EE"
  oscuro: "#16161d"
```

### Navegación

Edita en `_config.yml`:
```yaml
header_pages:
  - index.md
  - policy_briefs.md
  - working_papers.md
  - about.md
```

### Estilos

Edita `assets/css/style.css` para cambiar:
- Tipografía
- Espaciado
- Tamaños de texto
- Colores adicionales

---

## 🔧 Desarrollo local

Para probar el sitio localmente antes de publicar:

```bash
# Instalar Jekyll
gem install bundler jekyll

# Crear Gemfile
bundle init
bundle add jekyll

# Servir el sitio
bundle exec jekyll serve

# Abrir en navegador
open http://localhost:4000/
```

---

## 📋 Checklist pre-publicación

Antes de hacer push de una nueva publicación:

- [ ] PDF tiene naming correcto
- [ ] PDF está en `assets/pdfs/`
- [ ] Página actualizada (policy-briefs.md o working-papers.md)
- [ ] Metadata completa (autor, fecha, JEL codes)
- [ ] Links funcionan (probar localmente)
- [ ] Imágenes optimizadas (<500KB cada una)
- [ ] Ortografía revisada

---

## 🐛 Troubleshooting

**El sitio no se actualiza:**
- Espera 2-3 minutos después del push
- Revisa el tab "Actions" en GitHub para ver el build
- Verifica que no haya errores de sintaxis en los archivos .md

**Los estilos no se aplican:**
- Asegúrate de que `assets/css/style.css` existe
- Verifica que `_config.yml` use `url: "https://policy.refugioeconomico.mx"` y `baseurl: ""`

**Los links no funcionan:**
- Usa `{{ '/assets/...' | relative_url }}` para assets y `{{ '/ruta/' | relative_url }}` para navegación interna
- Verifica que exista el archivo `CNAME` con `policy.refugioeconomico.mx`

---

## 📬 Contacto

**Email:** contacto@refugioeconomico.mx  
**GitHub:** [@sebasdepapel](https://github.com/sebasdepapel)  
**Twitter:** [@sebasdepapel](https://twitter.com/sebasdepapel)

---

## 📄 Licencia

**Contenido:** CC BY 4.0 - Atribución requerida  
**Código:** MIT License

---

<small>Refugio Económico · 2025</small>
