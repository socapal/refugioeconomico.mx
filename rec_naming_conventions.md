# Convenciones de Naming - Refugio Económico Policy

**Versión:** 1.0  
**Fecha:** Enero 2026

Este documento establece las convenciones oficiales de naming, URLs y versionado para todas las publicaciones de Refugio Económico Policy.

---

## 🌐 Dominios base

### Dominio principal (marca / divulgación)
```
https://refugioeconomico.mx
```
**Uso:** Lectura, narrativa, ensayos, Punto Común

### Sección policy (repositorio institucional)
```
https://policy.refugioeconomico.mx
```
**Uso:** Archivo serio, PDFs citables, investigación técnica

**Regla de oro:**
- `refugioeconomico.mx` = Lectura y reflexión
- `policy.refugioeconomico.mx` = Citación académica

---

## 🗂️ Estructura de URLs

### Home del repositorio
```
https://policy.refugioeconomico.mx/
```

### Secciones principales
```
https://policy.refugioeconomico.mx/policy-briefs/
https://policy.refugioeconomico.mx/working-papers/
https://policy.refugioeconomico.mx/datasets/
https://policy.refugioeconomico.mx/projects/
https://policy.refugioeconomico.mx/about/
```

### URLs de proyectos
```
Formato: https://policy.refugioeconomico.mx/projects/<slug>-v#/

Ejemplo: https://policy.refugioeconomico.mx/projects/anps-v1/
```

### URLs de documentos
```
https://policy.refugioeconomico.mx/assets/pdfs/<FILENAME>.pdf
```

---

## 📦 Series de publicaciones

### 1️⃣ Policy Briefs (REC-PB)

**Formato de archivo:**
```
REC-PB-###-<slug>-vX.Y.pdf
```

**Componentes:**
- `REC-PB` = Identificador de serie (fijo)
- `###` = Número secuencial (001, 002, 003...)
- `<slug>` = Identificador corto del tema
- `vX.Y` = Versión (v1.0, v1.1, v2.0)

**Ejemplo:**
```
Archivo: REC-PB-001-anps-v1.0.pdf
URL: https://policy.refugioeconomico.mx/assets/pdfs/REC-PB-001-anps-v1.0.pdf
Landing: https://policy.refugioeconomico.mx/policy-briefs/REC-PB-001/
```

---

### 2️⃣ Working Papers (REC-WP)

**Formato de archivo:**
```
REC-WP-YYYY-##-<slug>-vX.Y.pdf
```

**Componentes:**
- `REC-WP` = Identificador de serie (fijo)
- `YYYY` = Año de publicación
- `##` = Número secuencial dentro del año (01, 02, 03...)
- `<slug>` = Identificador corto del tema
- `vX.Y` = Versión

**Ejemplo:**
```
Archivo: REC-WP-2026-01-anps-v1.0.pdf
URL: https://policy.refugioeconomico.mx/assets/pdfs/REC-WP-2026-01-anps-v1.0.pdf
Landing: https://policy.refugioeconomico.mx/working-papers/REC-WP-2026-01/
```

---

### 3️⃣ One-pagers institucionales (REC-OP)

**Formato de archivo:**
```
REC-OP-###-<slug>-vX.Y.pdf
```

**Uso:** Resúmenes ejecutivos para tomadores de decisión

**Ejemplo:**
```
Archivo: REC-OP-001-anps-v1.0.pdf
URL: https://policy.refugioeconomico.mx/assets/pdfs/REC-OP-001-anps-v1.0.pdf
```

---

### 4️⃣ Datasets (REC-DS)

**Formato de archivo:**
```
REC-DS-###-<slug>-vX.Y.(zip|csv|xlsx)
```

**Ejemplo:**
```
Archivo: REC-DS-001-anps-v1.0.zip
URL: https://policy.refugioeconomico.mx/datasets/REC-DS-001-anps-v1.0.zip
```

**Nota:** Si los datos están en repositorio externo (GitHub, Zenodo), la página de datasets incluye el link.

---

## 🏷️ Convención de slugs

### Reglas obligatorias:
1. ✅ Todo en minúsculas
2. ✅ Sin acentos ni diéresis
3. ✅ Sin espacios (usar guiones `-`)
4. ✅ Máximo 3-4 palabras
5. ✅ Semánticos y descriptivos

### Ejemplos válidos:
```
✅ anps
✅ vivienda-social
✅ desastres-sismicos
✅ mercado-laboral
✅ evaluacion-impacto
```

### Ejemplos inválidos:
```
❌ ANPs (mayúsculas)
❌ vivienda_social (guión bajo)
❌ desastres sísmicos (espacio y acento)
❌ evaluación-de-impacto-de-políticas-públicas (muy largo)
```

---

## 🔄 Versionado

### Formato: `vX.Y`

**X = Versión mayor** (cambios sustanciales)
- Nueva estimación
- Cambio metodológico
- Datos completamente distintos
- Ejemplo: `v1.0 → v2.0`

**Y = Versión menor** (correcciones y mejoras)
- Corrección de errores
- Actualización de datos (mismo método)
- Mejoras de redacción
- Ejemplo: `v1.0 → v1.1`

### Ejemplos de cambios de versión:

| Cambio | De → A |
|--------|--------|
| Corrección tipográfica | v1.0 → v1.1 |
| Actualización de datos 2020→2023 | v1.0 → v1.1 |
| Nueva especificación econométrica | v1.0 → v2.0 |
| Cambio de metodología (DiD → RDD) | v1.0 → v2.0 |

### Regla de oro:
**Nunca se borra un PDF publicado.** Las versiones antiguas permanecen accesibles.

```
Ejemplo:
REC-PB-001-anps-v1.0.pdf (original, siempre disponible)
REC-PB-001-anps-v1.1.pdf (corrección menor)
REC-PB-001-anps-v2.0.pdf (nueva versión mayor)
```

---

## 🔗 Enlaces cortos (difusión)

### Uso de acortadores (Bit.ly, Short.io)

**Solo para difusión en redes sociales**, nunca como URL canónica.

**Ejemplos:**
```
bit.ly/REC-ANPs        → https://policy.refugioeconomico.mx/projects/anps-v1/
bit.ly/REC-PB-001      → https://policy.refugioeconomico.mx/assets/pdfs/REC-PB-001-anps-v1.0.pdf
```

**Regla:** Siempre redirigen a `policy.refugioeconomico.mx`

---

## 📋 Changelog de versiones

Cada proyecto debe mantener un registro de cambios en su página de landing.

**Formato:**
```markdown
## Versiones

### v1.1 (Febrero 2026)
- Actualización con datos 2023
- Corrección en Tabla 3
- Mejora en claridad de Figura 2

### v1.0 (Diciembre 2025)
- Versión inicial publicada
```

---

## 📖 Plantillas de citación

### Policy Brief
```
Ocampo Palacios, S. (YYYY). [Título]. Refugio Económico Policy Brief 
REC-PB-###. https://policy.refugioeconomico.mx/assets/pdfs/REC-PB-###-[slug]-vX.Y.pdf
```

### Working Paper
```
Ocampo Palacios, S. (YYYY). [Título]. Refugio Económico Working Paper 
REC-WP-YYYY-##. https://policy.refugioeconomico.mx/assets/pdfs/REC-WP-YYYY-##-[slug]-vX.Y.pdf
```

### Working Paper (con RePEc)
```
Ocampo Palacios, S. (YYYY). [Título]. Refugio Económico Working Paper 
REC-WP-YYYY-##. RePEc:rec:wpaper:YYYY-##
```

### Dataset
```
Ocampo Palacios, S. (YYYY). [Título del dataset]. Refugio Económico Dataset 
REC-DS-###. https://policy.refugioeconomico.mx/datasets/REC-DS-###-[slug]-vX.Y.zip
```

---

## ✅ Checklist pre-publicación

Antes de publicar cualquier documento, verifica:

- [ ] Naming sigue el formato oficial
- [ ] Slug es válido (minúsculas, sin acentos, corto)
- [ ] Versión documentada (v1.0 para publicación inicial)
- [ ] URL es estable y citable
- [ ] Página de proyecto creada (si aplica)
- [ ] Changelog iniciado
- [ ] Plantilla de citación incluida

---

## 🔄 Actualizaciones de este documento

Este documento puede actualizarse. Cambios mayores se documentarán aquí.

**Historial:**
- v1.0 (Enero 2026): Versión inicial

---

**Contacto:** Para dudas sobre naming: contacto@refugioeconomico.mx