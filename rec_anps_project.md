---
layout: page
title: "Proyecto: Áreas Naturales Protegidas y Bienestar Local"
permalink: /projects/anps-v1/
---

# Áreas Naturales Protegidas y bienestar local en México
## Un análisis de impacto causal

<div class="publication-meta">
  <span class="code">Proyecto ANPs v1.0</span> · 
  Sebastián Ocampo Palacios · 
  Diciembre 2025
</div>

---

## Resumen

Esta investigación evalúa el impacto causal de las Áreas Naturales Protegidas (ANPs) sobre indicadores de bienestar local en México, utilizando un diseño de diferencias en diferencias con tratamiento escalonado. El análisis cubre el período 2000-2020 y examina localidades en un radio de 50km de las ANPs, comparando su evolución en marginación, ingreso per cápita y acceso a servicios básicos.

---

## 📊 En una mirada

- **Efecto promedio:** Las ANPs mejoran marginación e ingreso en localidades cercanas
- **Heterogeneidad por categoría:** Categorías restrictivas (Reservas de la Biosfera) muestran efectos negativos
- **Mecanismo:** Tensión entre conservación estricta y desarrollo económico local
- **Implicación:** La política de ANPs requiere mayor diferenciación por categoría y contexto local

---

## 📥 Descargas

<div class="publication-links">
  <a href="../../assets/pdfs/REC-WP-2026-01-anps-v1.0.pdf" class="btn">📄 Working Paper (PDF)</a>
  <a href="../../assets/pdfs/REC-PB-001-anps-v1.0.pdf" class="btn btn-secondary">📋 Policy Brief</a>
  <a href="../../assets/pdfs/REC-OP-001-anps-v1.0.pdf" class="btn btn-secondary">📊 One-pager</a>
  <a href="https://refugioeconomico.mx/anps-bienestar" class="btn btn-secondary">📝 Post divulgativo</a>
</div>

---

## 🔬 Metodología

### Diseño de investigación

**Método:** Diferencias en diferencias con tratamiento escalonado (Callaway-Sant'Anna, 2021)

**Tratamiento:** Declaratoria de ANP como evento que afecta localidades en un radio de 50km

**Unidad de análisis:** Localidad-año

**Período:** 2000-2020

**Outcomes:**
- Índice de marginación (CONAPO)
- Ingreso per cápita ajustado
- Acceso a servicios básicos (agua, electricidad, drenaje)

### Supuestos clave

1. **Tendencias paralelas:** Validado pre-tratamiento
2. **No anticipación:** Las declaratorias no se anticipan años antes
3. **SUTVA:** El tratamiento de una localidad no afecta a otras (validado con buffers)

### Especificación

El modelo estima efectos dinámicos por cohorte y tiempo relativo:

```
ATT(g,t) = E[Y_t(g) - Y_t(∞) | G_g = 1] - E[Y_t(g) - Y_t(∞) | G_g = 0]
```

Donde:
- `g` = cohorte de tratamiento (año de declaratoria)
- `t` = tiempo relativo al tratamiento
- `G_g` = indicador de pertenencia a cohorte

---

## 📈 Resultados principales

### Efecto promedio del tratamiento

**Marginación:** Reducción de 0.15 desviaciones estándar (p<0.05)

**Ingreso per cápita:** Incremento de 8.3% (p<0.10)

**Acceso a servicios:** Mejora de 5.2 puntos porcentuales (p<0.05)

### Heterogeneidad por categoría de ANP

| Categoría | Efecto marginación | Efecto ingreso |
|-----------|-------------------|----------------|
| Área de Protección de Flora y Fauna | -0.23** | +12.1%** |
| Parque Nacional | -0.12* | +6.8%* |
| Reserva de la Biosfera | +0.18* | -4.2% |
| Santuario | -0.08 | +3.1% |

\*p<0.10, \*\*p<0.05

### Dinámica temporal

Los efectos positivos aparecen después de 5-7 años de la declaratoria y persisten hasta el final del período de análisis (t+10).

---

## 💾 Datos y código {#datos}

### Fuentes de datos

**Áreas Naturales Protegidas:**
- CONANP - Comisión Nacional de Áreas Naturales Protegidas
- Shapefile de polígonos de ANPs (1900-2020)
- [Descargar datos](../../data/anps-v1/)

**Bienestar local:**
- INEGI - Censos de Población y Vivienda (2000, 2010, 2020)
- CONAPO - Índice de Marginación por Localidad
- CONEVAL - Indicadores de pobreza municipal

**Geoespacial:**
- INEGI - Marco Geoestadístico Nacional
- Coordenadas de localidades (ITER)

### Código replicable

El código completo para replicar todos los análisis está disponible en GitHub:

[📦 Repositorio GitHub: anps-impacto](https://github.com/sebasdepapel/anps-impacto)

**Estructura del repositorio:**
```
anps-impacto/
├── 01_data/
│   ├── raw/              # Datos originales
│   └── processed/        # Datos procesados
├── 02_code/
│   ├── 01_clean.R       # Limpieza y preparación
│   ├── 02_analysis.R    # Estimación DiD
│   ├── 03_figures.R     # Gráficas
│   └── 04_tables.R      # Tablas
├── 03_output/
│   ├── figures/
│   └── tables/
└── README.md
```

**Requerimientos:**
- R 4.1+
- Paquetes: `did`, `tidyverse`, `sf`, `fixest`, `modelsummary`
- Tiempo de ejecución: ~45 minutos

---

## 📄 Documentos del proyecto

### Publicaciones

1. **Working Paper** (REC-WP-2026-01)  
   [Descargar PDF](../../assets/pdfs/REC-WP-2026-01-anps-v1.0.pdf)

2. **Policy Brief** (REC-PB-001)  
   [Descargar PDF](../../assets/pdfs/REC-PB-001-anps-v1.0.pdf)

3. **One-pager institucional** (REC-OP-001)  
   [Descargar PDF](../../assets/pdfs/REC-OP-001-anps-v1.0.pdf)

### Materiales adicionales

4. **Post divulgativo** (Refugio Económico)  
   [Leer en línea](https://refugioeconomico.mx/anps-bienestar)

5. **Ficha técnica de datos**  
   [Ver en GitHub](https://github.com/sebasdepapel/anps-impacto/blob/main/DATA.md)

6. **Presentación ejecutiva**  
   [Descargar PPTX](../../assets/presentations/REC-ANPs-deck.pptx)

---

## 🔄 Versiones y cambios

### v1.0 (Diciembre 2025) - Actual
- Versión inicial completa
- Análisis 2000-2020
- Todas las categorías de ANPs

### Próximas versiones

**v1.1 (planeada para Febrero 2026):**
- Extensión a 2023 con datos intercensales
- Análisis de mecanismos (empleo, turismo)
- Robustez con matching espacial

---

## 📖 Cómo citar

### Working Paper
```
Ocampo Palacios, S. (2026). Áreas Naturales Protegidas y bienestar 
local en México: Un análisis de impacto causal. Refugio Económico 
Working Paper REC-WP-2026-01. 
https://policy.refugioeconomico.mx/assets/pdfs/REC-WP-2026-01-anps-v1.0.pdf
```

### Policy Brief
```
Ocampo Palacios, S. (2025). Áreas Naturales Protegidas y bienestar 
local en México. Refugio Económico Policy Brief REC-PB-001. 
https://policy.refugioeconomico.mx/assets/pdfs/REC-PB-001-anps-v1.0.pdf
```

### Código
```
Ocampo Palacios, S. (2025). Replication code for "Áreas Naturales 
Protegidas y bienestar local en México". GitHub repository. 
https://github.com/sebasdepapel/anps-impacto
```

---

## 🧩 Knowledge Brick: Conceptos clave

### ¿Qué son las Áreas Naturales Protegidas?

Las ANPs son porciones terrestres o acuáticas del territorio nacional representativas de los diversos ecosistemas, destinadas a conservación, investigación científica y educación ambiental.

**Categorías principales en México:**
- Reservas de la Biosfera (más restrictivas)
- Parques Nacionales
- Áreas de Protección de Flora y Fauna
- Santuarios

### Diferencias en diferencias escalonado

Extensión del método clásico de DiD que permite:
- Tratamientos que ocurren en distintos momentos
- Efectos heterogéneos por cohorte y tiempo
- Estimación robusta sin supuesto de efectos paralelos

**Referencia clave:** Callaway, B., & Sant'Anna, P. H. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200-230.

### Bibliografía esencial

1. Andam, K. S., et al. (2008). Measuring the effectiveness of protected area networks in reducing deforestation. *PNAS*, 105(42), 16089-16094.

2. Ferraro, P. J., & Hanauer, M. M. (2014). Quantifying causal mechanisms to determine how protected areas affect poverty through changes in ecosystem services. *PNAS*, 111(11), 4332-4337.

3. Sims, K. R. (2010). Conservation and development: Evidence from Thai protected areas. *Journal of Environmental Economics and Management*, 60(2), 94-114.

---

## 💬 Comentarios y contacto

Se agradecen comentarios, sugerencias y preguntas sobre este proyecto.

**Contacto:** [contacto@refugioeconomico.mx](mailto:contacto@refugioeconomico.mx)

**Discusión:** Abre un issue en el [repositorio de GitHub](https://github.com/sebasdepapel/anps-impacto/issues)

---

<small>[← Volver a Working Papers](../../working-papers) | [Ver todos los proyectos](../../)</small>