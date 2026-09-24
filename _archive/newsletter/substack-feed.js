(function () {
  const defaults = {
    posts: 3,
    showImages: true,
    showDates: true,
    timeoutMs: 12000
  };

  const containers = document.querySelectorAll(".substack-feed-embed");
  if (!containers.length) return;

  function normalizeSubstackUrl(url) {
    if (!url) return "";

    let clean = url.trim();
    if (!/^https?:\/\//i.test(clean)) clean = "https://" + clean;

    return clean.replace(/\/+$/, "");
  }

  function formatDate(value) {
    if (!value) return "";

    try {
      return new Intl.DateTimeFormat("es-MX", {
        year: "numeric",
        month: "short",
        day: "2-digit"
      }).format(new Date(value));
    } catch (error) {
      return "";
    }
  }

  function stripHtml(html) {
    if (!html) return "";

    const doc = new DOMParser().parseFromString(html, "text/html");
    return doc.body.textContent || "";
  }

  function truncate(text, max) {
    const limit = max || 165;
    const clean = (text || "").replace(/\s+/g, " ").trim();

    return clean.length > limit ? clean.slice(0, limit).trim() + "…" : clean;
  }

  function extractFirstImage(html) {
    if (!html) return null;

    const match = html.match(/<img[^>]+src=["']([^"']+)["']/i);
    return match ? match[1] : null;
  }

  function fetchWithTimeout(url, ms) {
    const controller = new AbortController();
    const timeout = window.setTimeout(function () {
      controller.abort();
    }, ms);

    return fetch(url, { signal: controller.signal }).finally(function () {
      window.clearTimeout(timeout);
    });
  }

  function buildCard(post, options) {
    const link = document.createElement("a");
    link.className = "substack-card";
    link.href = post.link || "#";
    link.target = "_blank";
    link.rel = "noopener noreferrer";

    const article = document.createElement("article");
    article.className = "substack-post";

    if (options.showImages) {
      const imageUrl = extractFirstImage(post.content || post.description);
      if (imageUrl) {
        const image = document.createElement("img");
        image.className = "substack-thumbnail";
        image.src = imageUrl;
        image.loading = "lazy";
        image.alt = post.title || "Imagen del post";
        article.appendChild(image);
      }
    }

    const body = document.createElement("div");
    body.className = "substack-body";

    const title = document.createElement("h3");
    title.className = "substack-title";
    title.textContent = post.title || "Sin título";
    body.appendChild(title);

    if (options.showDates && post.pubDate) {
      const date = document.createElement("p");
      date.className = "substack-date";
      date.textContent = formatDate(post.pubDate);
      body.appendChild(date);
    }

    const desc = document.createElement("p");
    desc.className = "substack-desc";
    desc.textContent = truncate(stripHtml(post.description || post.content || ""));
    body.appendChild(desc);

    article.appendChild(body);
    link.appendChild(article);

    return link;
  }

  async function renderFeed(container) {
    const substackUrl = normalizeSubstackUrl(container.dataset.substackUrl);
    const posts = parseInt(container.dataset.posts, 10) || defaults.posts;
    const showImages = (container.dataset.showImages || String(defaults.showImages)) !== "false";
    const showDates = (container.dataset.showDates || String(defaults.showDates)) !== "false";

    if (!substackUrl) {
      container.innerHTML = '<p class="substack-error">No se especificó un Substack.</p>';
      return;
    }

    const feedUrl = substackUrl + "/feed";
    const apiUrl = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent(feedUrl);

    container.innerHTML = '<div class="substack-skeleton">Cargando publicaciones recientes…</div>';

    try {
      const response = await fetchWithTimeout(apiUrl, defaults.timeoutMs);
      if (!response.ok) throw new Error("HTTP " + response.status);

      const data = await response.json();
      if (data.status !== "ok" || !Array.isArray(data.items)) {
        throw new Error(data.message || "No se pudo leer el feed.");
      }

      const items = data.items.slice(0, Math.max(1, posts));
      if (!items.length) {
        container.innerHTML = '<p class="substack-empty">No hay publicaciones disponibles.</p>';
        return;
      }

      container.innerHTML = "";
      items.forEach(function (post) {
        container.appendChild(buildCard(post, { showImages: showImages, showDates: showDates }));
      });
    } catch (error) {
      console.error("Substack feed error:", error);
      container.innerHTML = '<p class="substack-error">No fue posible cargar el feed. Puedes visitar Substack directamente.</p>';
    }
  }

  containers.forEach(function (container) {
    renderFeed(container);
  });
})();
