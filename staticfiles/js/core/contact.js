(function () {
    const obs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
        });
    }, { threshold: 0.10, rootMargin: '0px 0px -30px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

    const toggle = document.getElementById('chatbotToggle');
    const win    = document.getElementById('chatbotWindow');
    const close  = document.getElementById('chatbotClose');
    const msgs   = document.getElementById('chatMessages');
    const input  = document.getElementById('chatInput');
    const send   = document.getElementById('chatSend');
    const qr     = document.getElementById('quickReplies');

    const replies = {
        'Devenir membre'  : 'Pour devenir membre du CSGR-IA, contactez-nous à contact@csgr-ia.ga 📩',
        'Nos publications': 'Retrouvez nos publications dans Recherche > Publications 📚',
        'Nous contacter'  : 'Email : contact@csgr-ia.ga — Tél : +241 01 00 00 00 📞',
        'default'         : 'Merci ! Notre équipe vous répondra très prochainement. 😊'
    };

    function addMsg(text, type) {
        const d = document.createElement('div');
        d.className = 'chat-msg ' + type;
        d.textContent = text;
        msgs.appendChild(d);
        msgs.scrollTop = msgs.scrollHeight;
    }

    function botReply(text) {
        setTimeout(() => addMsg(replies[text] || replies['default'], 'bot'), 600);
    }

    toggle.addEventListener('click', () => win.classList.toggle('open'));
    close.addEventListener('click',  () => win.classList.remove('open'));

    qr.querySelectorAll('.quick-reply').forEach(btn => {
        btn.addEventListener('click', () => {
            const msg = btn.dataset.msg;
            addMsg(msg, 'user');
            botReply(msg);
            qr.style.display = 'none';
        });
    });

    function sendMsg() {
        const txt = input.value.trim();
        if (!txt) return;
        addMsg(txt, 'user');
        botReply(txt);
        input.value = '';
        qr.style.display = 'none';
    }

    send.addEventListener('click', sendMsg);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') sendMsg(); });
})();