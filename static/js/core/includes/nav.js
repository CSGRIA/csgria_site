(function () {
    const burger = document.getElementById('navBurger');
    const mobile = document.getElementById('navMobile');
    const nav    = document.querySelector('#nav');

    burger.addEventListener('click', () => {
        burger.classList.toggle('open');
        mobile.classList.toggle('open');
    });

    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });

    document.querySelectorAll('.js-dropdown-toggle').forEach(btn => {
        const dropdown = btn.nextElementSibling;
        const chevron  = btn.querySelector('.nav-chevron');

        btn.addEventListener('click', e => {
            e.stopPropagation();
            const isOpen = dropdown.classList.contains('open');
            document.querySelectorAll('.nav-dropdown.open').forEach(d => {
                d.classList.remove('open');
                d.previousElementSibling.querySelector('.nav-chevron').style.transform = '';
            });
            if (!isOpen) {
                dropdown.classList.add('open');
                chevron.style.transform = 'rotate(180deg)';
            }
        });
    });

    document.addEventListener('click', () => {
        document.querySelectorAll('.nav-dropdown.open').forEach(d => {
            d.classList.remove('open');
            d.previousElementSibling.querySelector('.nav-chevron').style.transform = '';
        });
    });

    document.querySelectorAll('.js-mobile-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
            const sub     = btn.nextElementSibling;
            const chevron = btn.querySelector('.nav-chevron');
            const isOpen  = sub.classList.contains('open');

            document.querySelectorAll('.nav-mobile-sub.open').forEach(s => {
                s.classList.remove('open');
                s.previousElementSibling.querySelector('.nav-chevron').style.transform = '';
            });

            if (!isOpen) {
                sub.classList.add('open');
                chevron.style.transform = 'rotate(180deg)';
            }
        });
    });
})();