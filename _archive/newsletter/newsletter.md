---
layout: default
title: Newsletter
permalink: /newsletter/
---

<div class="hero">
  <h1>Newsletter</h1>
  <p>Textos recientes de Refugio Económico publicados en Substack.</p>
</div>

<div class="card">
  <strong>Refugio Económico en Substack:</strong>
  ensayos, notas y textos breves para conectar investigación aplicada con conversación pública.
</div>

<div class="info-box">
  <strong>Enlaces directos:</strong>
  <a href="{{ site.substack_rec }}" target="_blank" rel="noopener noreferrer">Refugio Económico</a> ·
  <a href="{{ site.substack_pc }}" target="_blank" rel="noopener noreferrer">Punto Común</a>
</div>

<section class="substack-section card">
  <div class="substack-heading">
    <p class="substack-eyebrow">Substack</p>
    <h2>Últimos textos</h2>
    <p class="substack-intro">
      Publicaciones recientes de la newsletter de Refugio Económico.
    </p>
  </div>

  <div
    class="substack-feed-embed"
    data-substack-url="{{ site.substack_rec }}"
    data-posts="6"
    data-show-images="true"
    data-show-dates="true">
  </div>

  <p class="feed-fallback-link">
    <a href="{{ site.substack_rec }}" target="_blank" rel="noopener noreferrer">
      Ver todos los textos en Substack →
    </a>
  </p>
</section>

<script src="{{ '/assets/js/substack-feed.js' | relative_url }}" defer></script>
