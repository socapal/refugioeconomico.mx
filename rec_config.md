# Configuración del sitio
title: "Refugio Económico · Policy"
description: "Investigación aplicada y replicable para decisiones públicas"
author: "Sebastián Ocampo Palacios"
email: "contacto@refugioeconomico.mx"
baseurl: ""
url: "https://policy.refugioeconomico.mx"

# Build settings
theme: minima
markdown: kramdown
permalink: pretty

# Colores de Refugio Económico
colors:
  verde: "#013D1F"
  rosa: "#DB647F"
  fondo: "#F6F5EE"
  oscuro: "#16161d"

# Navegación
header_pages:
  - index.md
  - policy-briefs.md
  - working-papers.md
  - about.md

# Plugins
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# Exclude
exclude:
  - README.md
  - Gemfile
  - Gemfile.lock