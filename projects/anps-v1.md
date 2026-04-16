---
layout: page
title: "Proyecto: Áreas Naturales Protegidas y Bienestar Local"
permalink: /projects/anps-v1/
---

# Áreas Naturales Protegidas y bienestar local en México
## Impacto de las áreas naturales protegidas en la marginación y el ingreso municipal

<div class="publication-meta">
  <span class="code">Proyecto ANPs V.1.0</span> · 
  Sebastián Ocampo Palacios · 
  Septiembre 2022
</div>

---

## Resumen

En este trabajo analizamos el impacto de las Áreas Naturales Protegidas en los ingresos per cápita y el índice de marginación de la población cercana. Los resultados están construidos en dos capítulos: en el primero, presentamos un panorama actual sobre las áreas protegidas y ofrecemos herramientas teóricas para su análisis. En el segundo capítulo presentamos un análisis empírico que identifica los efectos de las ANPs en la marginación y el ingreso de los municipios que están a una distancia de 10 kilómetros. El **resultado principal sugiere que  la cercanía a estos espacios genera una reducción de la marginación y  un aumento en los ingresos, pero este efecto está sujeto a la categoría de conservación.**
Estos resultados permiten interpretar a las ANPs no solo como instrumentos de conservación ambiental, sino como **intervenciones territoriales con efectos económicos medibles sobre el bienestar** de la población.


---

## 📥 Descargas

<div class="publication-links">
  <a href="{{ '/downloads/anps-v1/' | relative_url }}" class="btn">📄 Working Paper (PDF)</a>
  <a href="{{ '/downloads/anps-v1/' | relative_url }}" class="btn btn-secondary">📋 Policy Brief</a>
  <a href="{{ '/downloads/anps-v1/' | relative_url }}" class="btn btn-secondary">📊 One-pager</a>
  <a href="https://refugioeconomico.mx/anps-bienestar" class="btn btn-secondary">📝 Post divulgativo</a>
</div>

---

## 🔬 Metodología

### Diseño de investigación

**Método:** Emparejamiento.

**Tratamiento:** Cercanía con Áreas Naturales Protegidas, que a su vez modifican el uso de recursos localmente. Estos espacios protegidos son  creados  bajo  un  decreto que  agrupa  consideraciones técnicas, políticas y sociales respecto de su valor para la identidad (nacional e  indígena) y su valor ambiental. En consecuencia,  las áreas suelen establecerse en territorios  que comparten características según la categoría bajo la que se establecerá su protección

**Unidad de análisis:** Localidad-año

**Período:** 2020

**Variables de medición:**
- Índice de marginación (CONAPO)
- Ingreso per cápita ajustado

**Supuestos clave:** Identificamos evidencia de soporte común e inconfundibilidad (las características del municipio no afectan municipio).

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

---

## 💾 Datos y código {#datos}

### Fuentes de datos

**Áreas Naturales Protegidas:**
- CONANP - Comisión Nacional de Áreas Naturales Protegidas
- Shapefile de polígonos de ANPs (1900-2020)
- [Descargar datos](https://github.com/sebasdepapel/anps-impacto)

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
.
├── README.md
├── MAPA_DEL_REPO.md
├── LICENSE
├── anps.csv
├── docs/
│   ├── DIARIO_INVESTIGACION.md
│   ├── DECISION_LOG.md
│   ├── OPEN_QUESTIONS.md
│   ├── CHANGELOG_NARRATIVO.md
│   └── CONVENCIONES.md
├── datasets-brutas/
│   ├── dummies-cercanas.csv
│   ├── misc.xlsx
│   ├── agebs/
│   │   ├── _conjunto_de_datos/
│   │   ├── _metadatos/
│   │   └── _diccionario_de_datos/
│   └── shp/
│       ├── anps/
│       └── mun/
├── datos-procesados/
│   ├── tablas-r/
│   ├── datos.xlsx
│   └── summary.csv
├── parques-recreacion_código/
│   ├── 0. Procesamiento-datos.R
│   ├── 1. Estadística-descriptiva.R
│   ├── 2. Matching-Regresiones.r
│   └── 3. Visualizaciones-y-mapas.R
├── ilustraciones/
│   └── Ilustraciones-finales/
├── presentacion-final/
└── scripts/
    └── utils/
        └── generate_repo_map.sh
```

**Requerimientos:**
- R 4.1+
- Paquetes: `sf`, `tidyverse`, `MatchIt`, `stargazer`, `clubSandwich`. 
- Tiempo de ejecución: ~45 minutos

---

## 📄 Documentos del proyecto

### Publicaciones

1. **Documentación de Investigación** (REC-DI-2022-09)  
   [Descargar PDF]( http://hdl.handle.net/11651/5294)

3. **One-pager institucional** (REC-OP-001)  
 En desarrollo. 

### Materiales adicionales

4. **Post divulgativo** (Refugio Económico)  
 En desarrollo. 

5. **Ficha técnica de datos**  
 En desarrollo. 

6. **Presentación ejecutiva**  
  [Ver en GitHub](https://github.com/socapal/impactos-anps_2020/blob/main/presentacion-final/examen-de-titulacion_21.09.22.pdf)

---



## 🔄 Versiones y cambios

### v1.0 (Septiembre 2022) - Actual
- Versión inicial.
- Análisis con información de 2020.
- Todas las categorías de ANPs

### Próximas versiones

**v2.0 (en diseño durante  2026-2027):**
- Incorporar una discusión conceptual sobre la diferencia entre gasto presupuestal e impacto económico, retomada a partir de un seminario de investigación reciente: revalorizar la discusión hacia los beneficios que generan estos tipos de intervención respecto del gasto que requiere su implementación y operación. 
- Desarrollar una interpretación económica de las ANPs como bienes públicos territoriales que generan externalidades sobre el bienestar local.
- Explorar el concepto de costo de oportunidad del uso del suelo como elemento central para entender la conservación.
- Introducir de forma exploratoria el enfoque de curvas de costo marginal de conservación (MAC) como herramienta para evaluar decisiones de política pública.
- Integrar los resultados empíricos existentes dentro de una narrativa más amplia sobre evaluación económica de políticas públicas territoriales.

---

## 📖 Cómo citar

### Documento de Investigación
```
Ocampo Palacios, Sebastián. "Impacto de las áreas naturales protegidas en la marginación y el ingreso municipal". Tesis de licenciatura. Centro de Investigación y Docencia Económicas, 2022. http://hdl.handle.net/11651/5294
``````

### Código
```
Ocampo Palacios, S. (2026). Código replicable para  "Impacto de las áreas naturales protegidas en la marginación y el ingreso municipa". Repositorio de Github. 
https://github.com/socapal/impactos-anps_2020
```

---

## 🧩 Knowledge Brick: Conceptos clave

### ¿Qué son las Áreas Naturales Protegidas?

Las ANPs son porciones terrestres o acuáticas del territorio nacional representativas de los diversos ecosistemas, destinadas a conservación, investigación científica y educación ambiental.

**Categorías principales en México:**
- Reservas de la Biosfera
- Parques Nacionales
- Monumentos Naturales
- Áreas de Protección de Recursos Naturales
- Áreas de Protección de Flora y Fauna
- Santuarios

## 💬 Comentarios y contacto

Se agradecen comentarios, sugerencias y preguntas sobre este proyecto.

**Contacto:** [socapal@outlook.com](mailto:socapal@outlook.com)

**Discusión:** Abre un issue en el [repositorio de GitHub](https://github.com/socapal/impactos-anps_2020/issues)

---

<small>[← Volver a Working Papers]({{ '/working-papers/' | relative_url }}) | [Ver todos los proyectos]({{ '/' | relative_url }})</small>
