const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

// Mobile menu (inner pages)
const burger = $("#burger"), nav = $("#nav");
if (burger && nav) {
  burger.addEventListener("click", () => burger.setAttribute("aria-expanded", nav.classList.toggle("open")));
}

// Typed role text (home page)
const typed = $("#typed");
if (typed && !reduce) {
  const roles = ["Network Engineer", "Software Engineer", "Cybersecurity Specialist"];
  let r = 0, c = 0, del = false;
  (function tick() {
    const word = roles[r];
    typed.textContent = word.slice(0, c);
    if (!del && c === word.length) { del = true; return setTimeout(tick, 1400); }
    if (del && c === 0) { del = false; r = (r + 1) % roles.length; }
    c += del ? -1 : 1;
    setTimeout(tick, del ? 45 : 90);
  })();
}

// Counters and skill bars animate when scrolled into view
const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  io.unobserve(e.target);
  if (e.target.dataset.count) {
    const end = +e.target.dataset.count; let n = 0;
    const step = () => { e.target.textContent = reduce ? end : ++n; if (n < end && !reduce) setTimeout(step, 150); };
    step();
  } else e.target.classList.add("in");
}), { threshold: .4 });
$$("[data-count], .bar-row").forEach(el => io.observe(el));

// Project filter (projects page)
$$(".filters button").forEach(b => b.addEventListener("click", () => {
  $$(".filters button").forEach(x => x.classList.toggle("on", x === b));
  $$("#pg .proj").forEach(p => p.hidden = b.dataset.f !== "all" && !p.dataset.cat.includes(b.dataset.f));
}));
