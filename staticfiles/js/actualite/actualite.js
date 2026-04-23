(function () {
    'use strict';
    var revealObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
            if (e.isIntersecting) { e.target.classList.add('visible'); revealObs.unobserve(e.target); }
        });
    }, { threshold: 0.10 });
    document.querySelectorAll('.reveal').forEach(function (el) { revealObs.observe(el); });

    var newsCounter = 0;
    var newsObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
            if (e.isIntersecting) {
                var idx = newsCounter++;
                setTimeout(function () { e.target.classList.add('visible'); }, idx * 100);
                newsObs.unobserve(e.target);
            }
        });
    }, { threshold: 0.08 });
    document.querySelectorAll('.news-item').forEach(function (el) { newsObs.observe(el); });

    var evObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
            if (e.isIntersecting) { e.target.classList.add('visible'); evObs.unobserve(e.target); }
        });
    }, { threshold: 0.12 });
    document.querySelectorAll('.tl-event-row').forEach(function (el) { evObs.observe(el); });

    var nlWrap  = document.querySelector('.sb-newsletter');
    var nlToast = document.querySelector('.sb-toast');
    if (nlWrap && nlToast) {
        var toastTimer = null;
        function showToast(msg, type) {
            clearTimeout(toastTimer);
            nlToast.textContent = msg;
            nlToast.className = 'sb-toast ' + type + ' show';
            toastTimer = setTimeout(function () { nlToast.classList.remove('show'); }, 5000);
        }
        nlWrap.querySelector('.sb-newsletter-btn').addEventListener('click', function () {
            var input = nlWrap.querySelector('input[type="email"]');
            var email = input ? input.value.trim() : '';
            if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                showToast('Veuillez entrer une adresse e-mail valide.', 'error');
                return;
            }
            showToast('Merci\u00a0! Votre inscription a été prise en compte.', 'success');
            input.value = '';
        });
    }
})();