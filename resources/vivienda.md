---
layout: page
title: Recursos de vivienda
permalink: /resources/vivienda/
description: Directorio de indicadores, informes y análisis externos sobre vivienda en México y perspectivas internacionales.
---

{% assign catalog = site.data.indicadores_vivienda %}
{% assign resources = catalog.resources | where: "status", "activo" %}
{% assign tags = resources | map: "tags" | join: "," | split: "," | uniq | sort %}

<div class="hero">
  <h1>{{ catalog.title | escape }}</h1>
  <p>Refugio Económico reúne indicadores, informes y análisis para facilitar el estudio de la vivienda y la discusión de políticas públicas. Esta selección se centra en México e incorpora perspectivas internacionales.</p>
</div>

<div id="vivienda-filter" class="card" hidden>
  <label for="vivienda-tag">Filtrar por etiqueta</label>
  <select id="vivienda-tag">
    <option value="">Todas las etiquetas</option>
    {% for tag in tags %}<option value="{{ tag | escape }}">{{ tag | escape }}</option>{% endfor %}
  </select>
  <p id="vivienda-count" role="status" aria-live="polite">{{ resources.size }} recursos</p>
</div>

<div id="vivienda-catalog">
{% for resource in resources %}
  <article class="card vivienda-resource" data-tags="{{ resource.tags | jsonify | escape }}">
    <h2>{{ resource.title | escape }}</h2>
    <dl>
      <dt>Autoría</dt><dd>{{ resource.authors | default: "No consignada en la fuente" | escape }}</dd>
      <dt>Casa editora</dt><dd>{{ resource.publisher | default: "No consignada en la fuente" | escape }}</dd>
      <dt>Fecha de publicación</dt><dd>{% if resource.date %}<time datetime="{{ resource.date | escape }}">{{ resource.date | date: "%d/%m/%Y" }}</time>{% else %}No consignada en la fuente{% endif %}</dd>
    </dl>
    <p>{% for tag in resource.tags %}<span class="badge">{{ tag | escape }}</span> {% endfor %}</p>
    <a class="btn" href="{{ resource.url | escape }}" rel="external">Consultar recurso externo<span class="visually-hidden">: {{ resource.title | escape }}</span> →</a>
  </article>
{% endfor %}
</div>

<div class="info-box">
  <h2>Nota metodológica</h2>
  <p>Esta colección es una curaduría de recursos externos. Los materiales enlazados pertenecen a sus autores o instituciones originales; su inclusión no implica autoría ni respaldo editorial de Refugio Económico. Las etiquetas y los datos bibliográficos proceden de la colección original y pueden revisarse mediante contribuciones al repositorio. Los campos ausentes se identifican sin inferir información.</p>
  <p>Fuente original: <a href="{{ catalog.source_url | escape }}">colección de Notion</a>, curada por Sebastián Ocampo-Palacios desde 2023. La exportación inicial contiene nueve recursos; no se verificó la vigencia de todos los enlaces externos.</p>
  <p>La fuente pública canónica y versionada es el <a href="https://github.com/socapal/refugioeconomico.mx/blob/main/_data/indicadores_vivienda.yml">catálogo en GitHub</a>. Última actualización del catálogo: <time datetime="{{ catalog.last_updated | escape }}">{{ catalog.last_updated | date: "%d/%m/%Y" }}</time>.</p>
</div>

<script src="{{ '/assets/js/vivienda.js' | relative_url }}" defer></script>
