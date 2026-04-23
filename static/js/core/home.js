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