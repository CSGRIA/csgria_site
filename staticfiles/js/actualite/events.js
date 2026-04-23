(function () {
    'use strict';

    /* ── Reveal au scroll ── */
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

    /* ── Compte à rebours ── */
    var cdEl = document.getElementById('evCountdown');
    if (cdEl) {
        var target = new Date(cdEl.dataset.date + 'T00:00:00');

        function pad(n) { return String(n).padStart(2, '0'); }

        function tick() {
            var now  = new Date();
            var diff = target - now;

            if (diff <= 0) {
                cdEl.style.display = 'none';
                return;
            }

            var days  = Math.floor(diff / 86400000);
            var hours = Math.floor((diff % 86400000) / 3600000);
            var mins  = Math.floor((diff % 3600000)  / 60000);
            var secs  = Math.floor((diff % 60000)    / 1000);

            document.getElementById('cd-days').textContent  = pad(days);
            document.getElementById('cd-hours').textContent = pad(hours);
            document.getElementById('cd-min').textContent   = pad(mins);
            document.getElementById('cd-sec').textContent   = pad(secs);
        }

        tick();
        setInterval(tick, 1000);
    }

    /* ── Newsletter ── */
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
                    showToast('Merci ! Vous êtes inscrit(e).', 'success');
                    input.value = '';
                } else {
                    return res.json().then(function (d) {
                        throw new Error(d.error || 'Erreur serveur.');
                    });
                }
            })
            .catch(function (err) {
                showToast(err.message || 'Une erreur est survenue.', 'error');
            });
        });
    }
})();