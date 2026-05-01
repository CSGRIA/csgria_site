(function () {
    const track    = document.getElementById('heroTrack');
    const carousel = document.getElementById('heroCarousel');
    const DUR = 5000, SPEED = 900;

    const orig  = Array.from(track.querySelectorAll('.hero-slide'));
    const TOTAL = orig.length;
    let li = 0, busy = false, timer;

    function goTo(idx) {
        if (busy) return;
        busy = true;
        const prev = track.querySelector('.hero-slide.active');
        if (prev) prev.classList.remove('active');
        li = (idx % TOTAL + TOTAL) % TOTAL;
        orig[li].classList.add('active');
        setDots();
        setTimeout(() => { busy = false; }, SPEED);
    }

    function setDots() {
        document.querySelectorAll('.hero-dot').forEach((d, i) => {
            d.classList.toggle('active', i === li);
        });
    }

    function next() { goTo(li + 1); }

    document.querySelectorAll('.hero-dot').forEach((d, i) => {
        d.addEventListener('click', () => {
            clearInterval(timer);
            goTo(i);
            start();
        });
    });

    function start() {
        clearInterval(timer);
        timer = setInterval(next, DUR);
    }

    carousel.addEventListener('mouseenter', () => clearInterval(timer));
    carousel.addEventListener('mouseleave', start);

    setDots();
    start();

    const obs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                obs.unobserve(e.target);
            }
        });
    }, { threshold: 0.10, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
})();



//section animation - réseau de points
(function () {
  const carousel = document.getElementById('heroCarousel');
  const canvas = document.getElementById('netCanvas');
  const ctx = canvas.getContext('2d');

  const PALETTES = [
    { node: '#4fc3f7', line: '#1565c0', pulse: '#81d4fa' },
    { node: '#b39ddb', line: '#512da8', pulse: '#ce93d8' },
    { node: '#80cbc4', line: '#00695c', pulse: '#a5d6a7' },
  ];

  const COUNT = 55, CONN_DIST = 130;
  let W, H, nodes, pal = PALETTES[0];
  const MOUSE = { x: -999, y: -999 };

  function resize() {
    W = canvas.width = carousel.clientWidth;
    H = canvas.height = carousel.clientHeight;
  }

  function makeNodes() {
    nodes = Array.from({ length: COUNT }, () => ({
      x: Math.random() * W, y: Math.random() * H,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      r: Math.random() * 1.8 + 1.2,
      pulse: Math.random() * Math.PI * 2,
    }));
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    const t = Date.now() * 0.001;

    for (let i = 0; i < COUNT; i++) {
      const a = nodes[i];
      a.x += a.vx; a.y += a.vy;
      if (a.x < 0 || a.x > W) a.vx *= -1;
      if (a.y < 0 || a.y > H) a.vy *= -1;

      // Répulsion souris
      const dx = MOUSE.x - a.x, dy = MOUSE.y - a.y;
      const md = Math.sqrt(dx * dx + dy * dy);
      if (md < 120) { a.x -= dx * 0.015; a.y -= dy * 0.015; }

      // Connexions
      for (let j = i + 1; j < COUNT; j++) {
        const b = nodes[j];
        const ex = a.x - b.x, ey = a.y - b.y;
        const d = Math.sqrt(ex * ex + ey * ey);
        if (d < CONN_DIST) {
          const alpha = (1 - d / CONN_DIST) * 0.45;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = pal.line + Math.round(alpha * 255).toString(16).padStart(2, '0');
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }

    // Points + halo pulsé
    for (let i = 0; i < COUNT; i++) {
      const n = nodes[i];
      const pulse = 0.5 + 0.5 * Math.sin(t * 1.5 + n.pulse);
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r + pulse * 2.5, 0, Math.PI * 2);
      ctx.fillStyle = pal.pulse + '18';
      ctx.fill();
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fillStyle = pal.node;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  // Changement de slide → change la palette
  let current = 0;
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');

  function goTo(next) {
    if (next === current) return;
    slides[current].classList.remove('active');
    current = next;
    slides[current].classList.add('active');
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
    pal = PALETTES[current % PALETTES.length];
  }

  dots.forEach(d => d.addEventListener('click', () => goTo(parseInt(d.dataset.index))));

  // Répulsion souris
  carousel.addEventListener('mousemove', e => {
    const r = canvas.getBoundingClientRect();
    MOUSE.x = e.clientX - r.left;
    MOUSE.y = e.clientY - r.top;
  });
  carousel.addEventListener('mouseleave', () => { MOUSE.x = -999; MOUSE.y = -999; });

  window.addEventListener('resize', resize);

  resize();
  makeNodes();
  draw();

  // Auto-play
  setInterval(() => goTo((current + 1) % slides.length), 4500);
})();