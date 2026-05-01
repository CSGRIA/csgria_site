/* ── QUESTIONS ── */
const questions = [
  {
    q:"🤖 En quelle année le terme « Intelligence Artificielle » a-t-il été officiellement inventé ?",
    opts:["1943","1956","1969","1984"], ans:1,
    expl:"John McCarthy a forgé le terme « Artificial Intelligence » lors de la conférence de Dartmouth en 1956."
  },
  {
    q:"🧠 Quel pays investit le plus dans la recherche en IA au monde ?",
    opts:["États-Unis","Chine","Royaume-Uni","Inde"], ans:0,
    expl:"Les États-Unis dominent avec plus de 67 Mds USD d'investissements privés en IA en 2023."
  },
  {
    q:"🌍 Quelle ville africaine héberge le plus grand hub d'IA du continent ?",
    opts:["Libreville","Nairobi","Le Caire","Lagos"], ans:1,
    expl:"Nairobi (Kenya) abrite iHub et plusieurs centres de recherche reconnus mondialement en IA."
  },
  {
    q:"📊 Que signifie l'acronyme « LLM » en intelligence artificielle ?",
    opts:["Large Language Model","Linear Learning Machine","Logical Logic Module","Low Level Memory"], ans:0,
    expl:"LLM = Large Language Model. C'est la technologie derrière ChatGPT, Claude, Gemini et d'autres IA génératives."
  },
  {
    q:"⚖️ Quelle organisation africaine a adopté la première convention sur la cybersécurité et les données personnelles ?",
    opts:["CEDEAO","Union Africaine","CEMAC","SADC"], ans:1,
    expl:"L'Union Africaine a adopté la Convention de Malabo en 2014 sur la cybersécurité et la protection des données."
  },
  {
    q:"🔍 Quel algorithme est à la base du moteur de recherche Google ?",
    opts:["Neural Net","PageRank","Decision Tree","K-means"], ans:1,
    expl:"PageRank, créé par Larry Page, classe les pages web selon le nombre et la qualité des liens entrants."
  },
  {
    q:"💡 Qu'est-ce que le « deep learning » ?",
    opts:["Un réseau neuronal à plusieurs couches","Un logiciel de reconnaissance vocale","Une méthode de cryptage","Un protocole réseau"], ans:0,
    expl:"Le deep learning utilise des réseaux de neurones profonds (multi-couches) pour apprendre à partir de grandes quantités de données."
  },
  {
    q:"🇬🇦 Quelle institution gabonaise coordonne la transformation numérique de l'État ?",
    opts:["DGDDI","ANINF","BEAC","CEMAC"], ans:1,
    expl:"L'ANINF (Agence Nationale des Infrastructures Numériques et des Fréquences) est l'organe technique chargé du numérique au Gabon."
  }
];

let current = 0, score = 0, answered = false;

function loadQuestion() {
  const q = questions[current];
  document.getElementById('qnum').textContent = (current+1)+' / '+questions.length;
  document.getElementById('qtext').textContent = q.q;
  document.getElementById('feedback').className = 'feedback';
  document.getElementById('feedback').textContent = '';
  document.getElementById('nextBtn').className = 'next-btn';
  const grid = document.getElementById('optGrid');
  grid.innerHTML = '';
  q.opts.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.textContent = opt;
    btn.onclick = () => answer(i);
    grid.appendChild(btn);
  });
  answered = false;
}

function answer(idx) {
  if (answered) return;
  answered = true;
  const q = questions[current];
  const btns = document.querySelectorAll('.option-btn');
  btns.forEach(b => b.disabled = true);
  if (idx === q.ans) { score++; btns[idx].classList.add('correct'); setFeedback('ok','✓ Correct ! '+q.expl); }
  else { btns[idx].classList.add('wrong'); btns[q.ans].classList.add('correct'); setFeedback('ko','✗ Pas tout à fait. '+q.expl); }
  document.getElementById('nextBtn').className = 'next-btn show';
}

function setFeedback(type, txt) {
  const fb = document.getElementById('feedback');
  fb.textContent = txt;
  fb.className = 'feedback '+type+' show';
}

function nextQuestion() {
  current++;
  if (current >= questions.length) { showScore(); return; }
  const card = document.getElementById('quizCard');
  card.style.opacity = '0'; card.style.transform = 'translateY(10px)';
  setTimeout(() => {
    loadQuestion();
    card.style.transition = 'all 0.3s ease';
    card.style.opacity = '1'; card.style.transform = 'translateY(0)';
  }, 200);
}

function showScore() {
  document.getElementById('quizMain').style.display = 'none';
  const sb = document.getElementById('scoreBlock');
  sb.classList.add('show');
  document.getElementById('scoreNum').textContent = score+' / '+questions.length;
  const msgs = [[0,2,"🌱 Début prometteur ! L'IA n'a plus de secrets à vous révéler… si vous continuez."],[3,5,"🔬 Bon niveau ! Vous avez l'étoffe d'un chercheur du CSGR-IA."],[6,7,"🧠 Excellent ! Votre expertise en IA est remarquable."],[8,8,"🏆 Score parfait ! Le CSGR-IA a besoin de vous !"]];
  const m = msgs.find(([a,b]) => score >= a && score <= b);
  document.getElementById('scoreMsg').textContent = m ? m[2] : '';
}

function restartQuiz() {
  current = 0; score = 0;
  document.getElementById('quizMain').style.display = '';
  document.getElementById('scoreBlock').classList.remove('show');
  loadQuestion();
}

loadQuestion();

/* ── PROGRESSION ── */
let pct = 0;
const pbar = document.getElementById('pbar');
const pctEl = document.getElementById('pct');
const iv = setInterval(() => {
  if (pct >= 73) { clearInterval(iv); return; }
  pct++;
  pbar.style.width = pct+'%';
  pctEl.textContent = pct+'%';
}, 22);

/* ── COUNTDOWN ── */
const launch = new Date();
launch.setDate(launch.getDate() + 30);
function tick() {
  const diff = launch - new Date();
  if (diff <= 0) return;
  const j = Math.floor(diff/86400000);
  const h = Math.floor((diff%86400000)/3600000);
  const m = Math.floor((diff%3600000)/60000);
  const s = Math.floor((diff%60000)/1000);
  const p = n => String(n).padStart(2,'0');
  document.getElementById('cd-j').textContent = p(j);
  document.getElementById('cd-h').textContent = p(h);
  document.getElementById('cd-m').textContent = p(m);
  document.getElementById('cd-s').textContent = p(s);
}
setInterval(tick, 1000); tick();

/* ── NOTIFY ── */
function notifyMe() {
  const v = document.getElementById('mailInput').value;
  if (!v || !v.includes('@')) { document.getElementById('mailInput').style.borderColor='rgba(231,76,60,0.5)'; return; }
  document.querySelector('.notify-form').style.display = 'none';
  document.getElementById('notifyOk').style.display = 'block';
}

/* ── CANVAS PARTICULES ── */
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let W, H, pts = [];
function resize() { W = canvas.width = innerWidth; H = canvas.height = innerHeight; }
resize(); window.addEventListener('resize', resize);
function Pt() { this.reset(); }
Pt.prototype.reset = function() {
  this.x = Math.random()*W; this.y = Math.random()*H;
  this.r = Math.random()*1.4+0.3;
  this.vx = (Math.random()-.5)*.4; this.vy = (Math.random()-.5)*.4;
  this.a = Math.random()*.5+.1;
  this.c = Math.random()>.6 ? '#f5c842' : '#2ecc71';
};
for (let i=0;i<110;i++) pts.push(new Pt());
(function loop() {
  ctx.clearRect(0,0,W,H);
  pts.forEach(p => {
    p.x += p.vx; p.y += p.vy;
    if (p.x<0||p.x>W||p.y<0||p.y>H) p.reset();
    ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctx.fillStyle = p.c; ctx.globalAlpha = p.a; ctx.fill();
  });
  for (let i=0;i<pts.length;i++) for (let j=i+1;j<pts.length;j++) {
    const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y, d=Math.sqrt(dx*dx+dy*dy);
    if (d<88) {
      ctx.beginPath(); ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y);
      ctx.strokeStyle='#2ecc71'; ctx.globalAlpha=(1-d/88)*.07; ctx.lineWidth=.5; ctx.stroke();
    }
  }
  requestAnimationFrame(loop);
})();