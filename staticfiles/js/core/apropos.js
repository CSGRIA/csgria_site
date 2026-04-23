    (function () {
        const obs = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    obs.unobserve(e.target);
                }
            });
        }, { threshold: 0.10, rootMargin: '0px 0px -30px 0px' });

        document.querySelectorAll('.reveal, .section-h2').forEach(el => obs.observe(el));

        const tlObs = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    tlObs.unobserve(e.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -20px 0px' });

        document.querySelectorAll('.timeline-row').forEach(el => tlObs.observe(el));

        const govObs = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    govObs.unobserve(e.target);
                }
            });
        }, { threshold: 0.15 });

        document.querySelectorAll('.gov-card').forEach(el => govObs.observe(el));
    })();