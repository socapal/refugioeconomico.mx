---
layout: page
title: Vivienda
permalink: /resources/vivienda/
description: "Recursos sobre vivienda y políticas urbanas: Radar Urbano e Indicadores e informes sobre la vivienda."
---

{% assign catalog = site.data.indicadores_vivienda %}
{% assign resources = catalog.resources | where: "status", "activo" %}
{% assign tags = resources | map: "tags" | join: "," | split: "," | uniq | sort %}

<nav aria-label="Ruta de navegación"><a href="{{ '/resources/' | relative_url }}">Recursos</a> / <span aria-current="page">Vivienda</span></nav>

<div class="hero">
  <h1>Vivienda</h1>
  <p>Recursos de Refugio Económico para estudiar la vivienda y las políticas urbanas, con énfasis en México y perspectivas internacionales.</p>
</div>

<section class="card" aria-labelledby="radar-urbano">
  <h2 id="radar-urbano">Radar Urbano</h2>
  <p>Curaduría semanal de investigación, informes y análisis sobre mercados de vivienda, resiliencia urbana, planeación y gobernanza urbana, y evaluación de políticas públicas.</p>
</section>

<section aria-labelledby="indicadores">
<h2 id="indicadores">{{ catalog.title | escape }}</h2>
<p>Un directorio de recursos externos para consultar indicadores, informes y análisis sobre vivienda. Esta selección se centra en México e incorpora perspectivas internacionales.</p>

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
    <h3>{{ resource.title | escape }}</h3>
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
  <h3>Nota metodológica</h3>
  <p>Esta colección es una curaduría de recursos externos. Los materiales enlazados pertenecen a sus autores o instituciones originales; su inclusión no implica autoría ni respaldo editorial de Refugio Económico.
  
  </p>
  <p>Fuente original: <a href="{{ catalog.source_url | escape }}">colección de Notion</a>, curada por Sebastián Ocampo-Palacios desde 2023.  Para citar este recurso: Refugio Económico. Indicadores e informes sobre la vivienda. Disponible en: https://policy.refugioeconomico.mx/resources/vivienda/. 
 Última actualización del catálogo: <time datetime="{{ catalog.last_updated | escape }}">{{ catalog.last_updated | date: "%d/%m/%Y" }}</time>.</p>
</div>

</section>

<p><a href="{{ '/resources/' | relative_url }}">← Volver a Recursos</a></p>

<script src="{{ '/assets/js/vivienda.js' | relative_url }}" defer></script>
