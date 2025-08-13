const form = document.getElementById("search-form");
const tbody = document.querySelector("#results-table tbody");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const pageDisplay = document.getElementById("page-display");
const resultInfo = document.getElementById("result-info");

let currentPage = 1;
let lastQuery = {};

function readForm() {
  const data = new FormData(form);
  return {
    title: data.get("title") || "",
    genre: data.get("genre") || "",
    min_year: data.get("min_year") || "",
    min_rating: data.get("min_rating") || "",
    order: data.get("order") || "year_desc",
    page_size: data.get("page_size") || 10
  };
}

async function fetchMovies(page = 1) {
  const q = new URLSearchParams({ ...lastQuery, page });
  const res = await fetch(`/api/movies?${q.toString()}`);
  const json = await res.json();
  renderResults(json);
}

function renderResults(data) {
  tbody.innerHTML = "";
  data.items.forEach(item => {
    const tr = document.createElement("tr");
    const titleTd = document.createElement("td");
    const yearTd = document.createElement("td");
    const genreTd = document.createElement("td");
    const ratingTd = document.createElement("td");

    const a = document.createElement("a");
    a.href = `/movie/${item.movie_id}`;
    a.textContent = item.title;
    titleTd.appendChild(a);

    yearTd.textContent = item.release_year;
    genreTd.textContent = item.genre;
    ratingTd.textContent = item.rating.toFixed(1);

    tr.appendChild(titleTd);
    tr.appendChild(yearTd);
    tr.appendChild(genreTd);
    tr.appendChild(ratingTd);
    tbody.appendChild(tr);
  });

  currentPage = data.page;
  pageDisplay.textContent = `Page ${data.page} of ${Math.max(1, Math.ceil(data.total / data.page_size))}`;
  resultInfo.textContent = `Found ${data.total} movie(s)`;

  prevBtn.disabled = currentPage <= 1;
  nextBtn.disabled = currentPage >= Math.ceil(data.total / data.page_size);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  lastQuery = readForm();
  currentPage = 1;
  fetchMovies(1);
});

prevBtn.addEventListener("click", () => fetchMovies(currentPage - 1));
nextBtn.addEventListener("click", () => fetchMovies(currentPage + 1));

// Initial load
lastQuery = readForm();
fetchMovies(1);
