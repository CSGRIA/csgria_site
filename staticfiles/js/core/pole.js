(function () {
    const obs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
        });
    }, { threshold: 0.08, rootMargin: '0px 0px -20px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

    const dataEl = document.getElementById('membres-data');
    if (!dataEl) return;
    const MEMBRES = JSON.parse(dataEl.textContent);
    const N = MEMBRES.length;
    if (N === 0) return;

    const PALETTE = [
        '#1a2a4a','#1a2a38','#2a1a30','#0f2a1a',
        '#2a1a1a','#1a1e30','#1a2a28','#201a2a',
    ];

    const stage   = document.getElementById('arcStage');
    const dotsEl  = document.getElementById('membresDots');
    const btnPrev = document.getElementById('membresNavPrev');
    const btnNext = document.getElementById('membresNavNext');

    let center = 0, autoTimer;
    const cards = [], dots = [];

    MEMBRES.forEach(function(m, i) {
        const bg    = PALETTE[i % PALETTE.length];
        const lines = m.name.split('\n');

        const card = document.createElement('div');
        card.className   = 'member-card';
        card.dataset.idx = i;

        const photoHTML = m.photo
            ? '<img class="card-photo" src="' + m.photo + '" alt="' + lines.join(' ') + '">'
            : '<div class="card-initials">' + m.initials + '</div>';

        card.innerHTML =
            '<div class="card-inner" style="background:' + bg + ';">'
            + photoHTML
            + '<div class="card-overlay"></div>'
            + '<div class="role-badge"><div class="role-dot"></div><span>' + m.role + '</span></div>'
            + '<div class="card-footer">'
            +   '<div class="card-name">' + lines.join('<br>') + '</div>'
            +   '<div class="card-sub">' + m.sub + '</div>'
            + '</div>'
            + '</div>';

        card.addEventListener('click', function() { goTo(i); });
        stage.appendChild(card);
        cards.push(card);

        const dot = document.createElement('button');
        dot.className = 'membres-dot';
        dot.setAttribute('aria-label', 'Aller au membre ' + (i + 1));
        dot.addEventListener('click', function() { goTo(i); });
        dotsEl.appendChild(dot);
        dots.push(dot);
    });

    function layout() {
        const stageW   = stage.offsetWidth || 800;
        const isMobile = stageW < 500;
        const isTablet = stageW < 900 && !isMobile;

        const CW = isMobile ? 170  : isTablet ? 220  : 280;
        const CH = isMobile ? 210  : isTablet ? 256  : 270;
        const SW = isMobile ? 118  : isTablet ? 158  : 204;
        const SH = isMobile ? 162  : isTablet ? 198  : 210;

        const SIDE       = isMobile ? 1 : 2;
        const ARC_DY     = [0, 18, 36, 54];
        const BRIGHTNESS = [1, 0.68, 0.40, 0.18];
        const BLUR       = [0, 0, 1.5, 3];

        cards.forEach(function(card, i) {
            let rel = ((i - center) % N + N) % N;
            if (rel > N / 2) rel = rel - N;
            const absRel = Math.abs(rel);

            if (absRel > SIDE) {
                card.style.opacity = '0';
                card.style.pointerEvents = 'none';
                card.style.zIndex = '0';
                return;
            }

            card.style.opacity       = '1';
            card.style.pointerEvents = 'auto';

            const isCenter = rel === 0;
            const w  = isCenter ? CW : SW * Math.max(0.62, 1 - (absRel - 1) * 0.14);
            const h  = isCenter ? CH : SH * Math.max(0.62, 1 - (absRel - 1) * 0.14);
            const dy = ARC_DY[Math.min(absRel, 3)];
            const br = BRIGHTNESS[Math.min(absRel, 3)];
            const bl = BLUR[Math.min(absRel, 3)];

            let xPos;
            if (isCenter) {
                xPos = stageW / 2 - w / 2;
            } else {
                const sign = rel < 0 ? -1 : 1;
                const gap  = CW / 2 + w / 2 + 12 + (absRel - 1) * (SW * 0.78 + 10);
                xPos = stageW / 2 + sign * gap - w / 2;
            }

            card.style.width  = w + 'px';
            card.style.height = h + 'px';
            card.style.left   = xPos + 'px';
            card.style.bottom = dy + 'px';
            card.style.zIndex = String(10 - absRel);
            card.style.filter = 'brightness(' + br + ')' + (bl ? ' blur(' + bl + 'px)' : '');

            card.classList.toggle('active', isCenter);
            const badge = card.querySelector('.role-badge');
            if (badge) badge.style.opacity = isCenter ? '1' : (absRel === 1 ? '0.58' : '0.28');
            dots[i].classList.toggle('active', isCenter);
        });
    }

    function goTo(idx) { center = ((idx % N) + N) % N; layout(); resetAuto(); }
    function resetAuto() { clearInterval(autoTimer); autoTimer = setInterval(function() { goTo(center + 1); }, 3600); }

    btnPrev.addEventListener('click', function() { goTo(center - 1); });
    btnNext.addEventListener('click', function() { goTo(center + 1); });

    var touchStartX = 0;
    stage.addEventListener('touchstart', function(e) { touchStartX = e.changedTouches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', function(e) {
        var dx = e.changedTouches[0].clientX - touchStartX;
        if (Math.abs(dx) > 40) goTo(dx < 0 ? center + 1 : center - 1);
    }, { passive: true });

    layout();
    window.addEventListener('resize', layout);
    resetAuto();

})();