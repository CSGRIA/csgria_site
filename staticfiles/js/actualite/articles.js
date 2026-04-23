(function () {
    'use strict';

    /* Reveal au scroll */
    var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                obs.unobserve(e.target);
            }
        });
    }, { threshold: 0.10 });

    document.querySelectorAll('.reveal, .section-h2')
        .forEach(function (el) { obs.observe(el); });

    /* Newsletter */
    var nlForm  = document.querySelector('.sb-newsletter');
    var nlToast = document.querySelector('.sb-toast');

    if (nlForm && nlToast) {
        nlForm.addEventListener('submit', function (e) {
            e.preventDefault();
            var input = nlForm.querySelector('input[type="email"]');
            var email = input ? input.value.trim() : '';
            var toastTimer;

            function showToast(msg, type) {
                clearTimeout(toastTimer);
                nlToast.textContent = msg;
                nlToast.className = 'sb-toast ' + type + ' show';
                toastTimer = setTimeout(function () {
                    nlToast.classList.remove('show');
                }, 5000);
            }

            if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                showToast('Veuillez entrer une adresse e-mail valide.', 'error');
                return;
            }

            var url = nlForm.getAttribute('action');
            if (!url || url === '#') {
                showToast('Merci ! Votre inscription sera prise en compte.', 'success');
                input.value = '';
                return;
            }

            fetch(url, {
                method: 'POST',
                body: new FormData(nlForm),
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            })
            .then(function (res) {
                if (res.ok) {
                    showToast('Merci ! Vous êtes inscrit(e) à la newsletter.', 'success');
                    input.value = '';
                } else {
                    return res.json().then(function (d) { throw new Error(d.error || 'Erreur serveur.'); });
                }
            })
            .catch(function (err) {
                showToast(err.message || 'Une erreur est survenue.', 'error');
            });
        });
    }
})();