// Screenshot viewer with zoom (project demo pages)
//   mouse wheel / + / - buttons : zoom      drag : move      double-click : zoom in/out
//   pinch (touch) : zoom      arrows : previous / next      Esc : close
(() => {
  const items = [...document.querySelectorAll("[data-shot]")];
  const dlg = document.getElementById("lightbox");
  if (!dlg || !items.length || !dlg.showModal) return;

  const stage = dlg.querySelector(".lb-stage");
  const img = stage.querySelector("img");
  const title = dlg.querySelector(".lb-title");
  const cap = dlg.querySelector(".lb-text");
  const level = dlg.querySelector(".lb-zoom-level");
  const MAX = 4;                       // 400% of the image's real size
  let i = 0, fit = 1, s = 1, x = 0, y = 0;

  const apply = () => {
    img.style.transform = `translate(${x}px, ${y}px) scale(${s})`;
    level.textContent = Math.round(s * 100) + "%";
  };
  const clamp = () => {                // keep the image from being dragged out of view
    const w = img.naturalWidth * s, h = img.naturalHeight * s;
    const W = stage.clientWidth, H = stage.clientHeight;
    x = w <= W ? (W - w) / 2 : Math.min(0, Math.max(W - w, x));
    y = h <= H ? (H - h) / 2 : Math.min(0, Math.max(H - h, y));
  };
  const reset = () => {                // fit the whole image on screen
    if (!img.naturalWidth) return;
    fit = Math.min(stage.clientWidth / img.naturalWidth, stage.clientHeight / img.naturalHeight, 1);
    s = fit; clamp(); apply();
  };
  const zoomAt = (target, cx, cy) => { // zoom keeping the point (cx, cy) fixed
    target = Math.min(MAX, Math.max(fit, target));
    const k = target / s;
    x = cx - (cx - x) * k;
    y = cy - (cy - y) * k;
    s = target; clamp(); apply();
  };
  const mid = () => [stage.clientWidth / 2, stage.clientHeight / 2];
  const local = (e) => { const r = stage.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };

  const show = (n) => {
    i = (n + items.length) % items.length;
    const d = items[i].dataset;
    title.textContent = d.title + "  (" + (i + 1) + " / " + items.length + ")";
    cap.textContent = d.caption;
    img.alt = d.title;
    img.onload = reset;
    img.src = d.full;
    if (img.complete) reset();
  };

  items.forEach((b, n) => b.addEventListener("click", () => { dlg.showModal(); show(n); }));

  // buttons
  dlg.querySelector('[data-act="in"]').addEventListener("click", () => zoomAt(s * 1.3, ...mid()));
  dlg.querySelector('[data-act="out"]').addEventListener("click", () => zoomAt(s / 1.3, ...mid()));
  level.addEventListener("click", () => (s > fit * 1.01 || fit >= 1) ? reset() : zoomAt(1, ...mid()));
  dlg.querySelector(".lb-close").addEventListener("click", () => dlg.close());
  dlg.querySelector(".lb-prev").addEventListener("click", () => show(i - 1));
  dlg.querySelector(".lb-next").addEventListener("click", () => show(i + 1));

  // mouse wheel
  stage.addEventListener("wheel", (e) => {
    e.preventDefault();
    zoomAt(s * Math.exp(-e.deltaY * 0.0016), ...local(e));
  }, { passive: false });

  // double-click: zoom in on that spot, or back to fit
  stage.addEventListener("dblclick", (e) => {
    zoomAt(s > fit * 1.01 ? fit : Math.max(fit * 2, 1), ...local(e));
  });

  // drag to move, two fingers to pinch
  const ptrs = new Map();
  let pinchDist = 0, pinchScale = 1;
  stage.addEventListener("pointerdown", (e) => {
    try { stage.setPointerCapture(e.pointerId); } catch (_) {}
    ptrs.set(e.pointerId, { x: e.clientX, y: e.clientY });
    stage.classList.add("dragging");
    if (ptrs.size === 2) {
      const [a, b] = [...ptrs.values()];
      pinchDist = Math.hypot(a.x - b.x, a.y - b.y) || 1;
      pinchScale = s;
    }
  });
  stage.addEventListener("pointermove", (e) => {
    const p = ptrs.get(e.pointerId);
    if (!p) return;
    if (ptrs.size === 2) {
      p.x = e.clientX; p.y = e.clientY;
      const [a, b] = [...ptrs.values()];
      const r = stage.getBoundingClientRect();
      zoomAt(pinchScale * Math.hypot(a.x - b.x, a.y - b.y) / pinchDist,
             (a.x + b.x) / 2 - r.left, (a.y + b.y) / 2 - r.top);
    } else {
      if (p.stale) { p.x = e.clientX; p.y = e.clientY; p.stale = false; return; }
      x += e.clientX - p.x; y += e.clientY - p.y;
      p.x = e.clientX; p.y = e.clientY;
      clamp(); apply();
    }
  });
  const end = (e) => {
    ptrs.delete(e.pointerId);
    ptrs.forEach((p) => { p.stale = true; });
    if (!ptrs.size) stage.classList.remove("dragging");
  };
  stage.addEventListener("pointerup", end);
  stage.addEventListener("pointercancel", end);

  // keyboard
  dlg.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") show(i - 1);
    else if (e.key === "ArrowRight") show(i + 1);
    else if (e.key === "+" || e.key === "=") zoomAt(s * 1.3, ...mid());
    else if (e.key === "-" || e.key === "_") zoomAt(s / 1.3, ...mid());
    else if (e.key === "0") reset();
  });

  window.addEventListener("resize", () => { if (dlg.open) reset(); });
})();
