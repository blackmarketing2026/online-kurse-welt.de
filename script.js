const categories = document.querySelectorAll('.category');
const cards = document.querySelectorAll('.course-card');
const resetFilter = document.querySelector('.reset-filter');
const emptyState = document.querySelector('.empty-state');
let activeCategory = null;

function renderCourses() {
  let visible = 0;
  categories.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.category === activeCategory)));
  cards.forEach(card => {
    const show = !activeCategory || card.dataset.category === activeCategory;
    card.hidden = !show;
    if (show) visible++;
  });
  resetFilter.hidden = !activeCategory;
  emptyState.hidden = visible !== 0;
}

categories.forEach(button => button.addEventListener('click', () => {
  activeCategory = activeCategory === button.dataset.category ? null : button.dataset.category;
  renderCourses();
  document.querySelector('#kurse').scrollIntoView({behavior:'smooth', block:'start'});
}));
resetFilter.addEventListener('click', () => { activeCategory = null; renderCourses(); });

const dialog = document.querySelector('#info-dialog');
const dialogTitle = document.querySelector('#dialog-title');
const dialogCopy = document.querySelector('#dialog-copy');
document.querySelectorAll('[data-dialog], [data-course]').forEach(button => button.addEventListener('click', () => {
  if (button.dataset.course) {
    dialogTitle.textContent = button.dataset.course;
    dialogCopy.textContent = 'Die Kursdetails und der Link zum Anbieter werden ergänzt, sobald die Kursauswahl feststeht.';
  } else {
    dialogTitle.textContent = 'Ratgeber';
    dialogCopy.textContent = 'Der Ratgeber wird in einem späteren Schritt ergänzt.';
  }
  dialog.showModal();
}));
document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
