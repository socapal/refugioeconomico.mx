---
layout: page
title: Radar Urbano
permalink: /resources/vivienda/radar/
description: "Curaduría semanal de investigación, informes y análisis sobre vivienda, resiliencia urbana, planeación, gobernanza y evaluación de políticas públicas."
---

<nav aria-label="Ruta de navegación">
  <a href="{{ '/resources/' | relative_url }}">Recursos</a> /
  <a href="{{ '/resources/vivienda/' | relative_url }}">Vivienda</a> /
  <span aria-current="page">Radar Urbano</span>
</nav>

<div class="hero">
  <h1>Radar Urbano</h1>
  <p>Curaduría semanal de investigación, informes y análisis sobre mercados de vivienda, resiliencia urbana, planeación y gobernanza, y evaluación de políticas públicas.</p>
</div>

{% assign editions = site.radar | sort: 'date' | reverse %}

{% if editions.size > 0 %}
  {% assign latest = editions.first %}
  <section class="card" aria-labelledby="ultima-edicion">
    <p>Última edición</p>
    <h2 id="ultima-edicion"><a href="{{ latest.url | relative_url }}">{{ latest.title | escape }}</a></h2>
    <p><time datetime="{{ latest.date | date: '%Y-%m-%d' }}">{{ latest.date | date: '%d/%m/%Y' }}</time></p>
    {% if latest.insight %}
      <p><strong>Insight:</strong> {{ latest.insight | escape }}</p>
    {% endif %}
    <p>{% for tag in latest.tags %}<span class="badge">{{ tag | escape }}</span> {% endfor %}</p>
    <a class="btn" href="{{ latest.url | relative_url }}">Leer edición →</a>
  </section>

  <section aria-labelledby="archivo-radar">
    <h2 id="archivo-radar">Archivo</h2>
    <div class="series-grid">
    {% for edition in editions %}
      <article class="series-card">
        <p><time datetime="{{ edition.date | date: '%Y-%m-%d' }}">{{ edition.date | date: '%d/%m/%Y' }}</time></p>
        <h3><a href="{{ edition.url | relative_url }}">{{ edition.title | escape }}</a></h3>
        {% if edition.insight %}
          <p>{{ edition.insight | escape }}</p>
        {% endif %}
        <p>{% for tag in edition.tags %}<span class="badge">{{ tag | escape }}</span> {% endfor %}</p>
      </article>
    {% endfor %}
    </div>
  </section>
{% else %}
  <p>No hay ediciones publicadas todavía.</p>
{% endif %}

<p><a href="{{ '/resources/vivienda/' | relative_url }}">← Volver a Vivienda</a></p>
