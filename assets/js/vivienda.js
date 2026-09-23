// Mejora progresiva: las tarjetas completas siguen disponibles sin JavaScript.
(() => {
  const filter = document.getElementById('vivienda-filter');
  const select = document.getElementById('vivienda-tag');
  const count = document.getElementById('vivienda-count');
  const cards = Array.from(document.querySelectorAll('.vivienda-resource'));
  if (!filter || !select || !count) return;
  const entries = cards.map(card => ({ card, tags: JSON.parse(card.dataset.tags) }));
  select.addEventListener('change', () => {
    let visible = 0;
    entries.forEach(({ card, tags }) => {
      card.hidden = Boolean(select.value) && !tags.includes(select.value);
      if (!card.hidden) visible += 1;
    });
    count.textContent = visible === 0 ? 'No hay recursos para esta etiqueta.' : `${visible} recursos`;
  });
  filter.hidden = false;
})();
