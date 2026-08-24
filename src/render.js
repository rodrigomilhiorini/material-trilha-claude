(function(){
  "use strict";
  var DATA = JSON.parse(document.getElementById('data-json').textContent);
  var MODULES = DATA.modules;
  var STATS = DATA.stats;

  function el(tag, cls, html){ var e=document.createElement(tag); if(cls) e.className=cls; if(html!==undefined) e.innerHTML=html; return e; }
  function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

  // ---------- Theme toggle ----------
  var themeBtn = document.getElementById('themeToggle');
  var themeIcon = document.getElementById('themeIcon');
  var themeLabel = document.getElementById('themeLabel');
  function currentTheme(){
    return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }
  function paintToggle(t){
    if (t === 'light'){ themeIcon.textContent = '☼'; themeLabel.textContent = 'Claro'; }
    else { themeIcon.textContent = '☾'; themeLabel.textContent = 'Escuro'; }
  }
  paintToggle(currentTheme());
  themeBtn.addEventListener('click', function(){
    var next = currentTheme() === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next);
    try{ localStorage.setItem('trilha-theme', next); }catch(e){}
    paintToggle(next);
  });

  // ---------- Bilingual helpers ----------
  function blCap(iconChar, lblPt, lblEn){
    return '<div class="bl-cap"><span class="ico">'+iconChar+'</span><span class="lbl-pt">'+esc(lblPt)+'</span><span class="sep">·</span><span class="lbl-en">'+esc(lblEn)+'</span></div>';
  }
  // htmlPt/htmlEn are trusted HTML strings (already contain the tags we want); label strings are escaped.
  function blGrid(htmlPt, htmlEn){
    return '<div class="bl-grid">'
      + '<div class="bl-col bl-pt"><span class="mini-tag">PT</span>' + htmlPt + '</div>'
      + '<div class="bl-divider" aria-hidden="true"></div>'
      + '<div class="bl-col bl-en"><span class="mini-tag">EN</span>' + htmlEn + '</div>'
      + '</div>';
  }
  function wrapP(html){
    // ensure plain-text fallback still renders as a paragraph
    if (!/^\s*<p/i.test(html || '')) return '<p>' + (html || '') + '</p>';
    return html;
  }

  // ---------- Stat row ----------
  var statHost = document.getElementById('statrow');
  var statDefs = [
    {n: STATS.modules || MODULES.length, l: "Módulos"},
    {n: STATS.lessons, l: "Tópicos/aulas"},
    {n: STATS.quiz, l: "Questões por aula"},
    {n: STATS.simulados_questions || 0, l: "Questões de simulado"},
    {n: STATS.glossary, l: "Termos no glossário"},
  ];
  statDefs.forEach(function(s){
    var box = el('div','stat');
    box.innerHTML = '<div class="n">'+s.n+'</div><div class="l">'+s.l+'</div>';
    statHost.appendChild(box);
  });

  // ---------- Modules ----------
  var modulesRoot = document.getElementById('modules-root');
  var letters = ["A","B","C","D","E"];

  MODULES.forEach(function(mod, modIdx){
    var section = el('section');
    section.id = mod.id;

    var head = el('div','section-head');
    head.innerHTML = '<span class="section-num">'+mod.badge+'</span><h2 class="h">'+esc(mod.title)+'</h2>';
    head.style.scrollMarginTop = '110px';
    section.appendChild(head);

    var lede = el('p','lede');
    lede.innerHTML = '<em>'+esc(mod.subtitle)+'</em> — '+esc(mod.desc);
    section.appendChild(lede);

    // Lessons accordion
    mod.lessons.forEach(function(lesson, li){
      var det = el('details','lesson');
      if (modIdx === 0 && li === 0) det.open = true; // first lesson open by default
      var sum = el('summary');
      sum.innerHTML = '<span class="lesson-n">'+esc(lesson.n)+'</span><span class="lesson-ttl">'+esc(lesson.title)+'</span><span class="chev">&#8250;</span>';
      det.appendChild(sum);

      var body = el('div','lesson-body');

      // figures (reference diagrams, when present) — shown once, above the bilingual text
      (lesson.figures || []).forEach(function(fig){
        var figEl = el('figure','lesson-fig');
        figEl.innerHTML = '<img src="'+fig.src+'" alt="Diagrama do guia de arquitetura" loading="lazy">'
          + '<figcaption><span class="chip-pt">Diagrama do guia de arquitetura</span><span class="chip-sep">·</span><span class="chip-en">Diagram from the architecture guide</span></figcaption>';
        body.appendChild(figEl);
      });

      // topics — every chip bilingual
      body.insertAdjacentHTML('beforeend', blCap('i','Tópicos e subtópicos','Topics & subtopics'));
      var subtopics = el('div','subtopics');
      (lesson.topics||[]).forEach(function(t, ti){
        var tEn = (lesson.topics_en || [])[ti] || '';
        var chip = el('span', null);
        var same = tEn.trim().toLowerCase() === String(t).trim().toLowerCase();
        chip.innerHTML = '<span class="chip-pt">'+esc(t)+'</span>' + (same || !tEn ? '' : '<span class="chip-sep">·</span><span class="chip-en">'+esc(tEn)+'</span>');
        subtopics.appendChild(chip);
      });
      body.appendChild(subtopics);

      // material — bilingual
      body.insertAdjacentHTML('beforeend', blCap('§','Material de estudo','Study material'));
      body.insertAdjacentHTML('beforeend', blGrid(wrapP(lesson.material || ''), wrapP(lesson.material_en || '')));

      // quiz for this lesson
      var lessonQuiz = (mod.quiz||[]).filter(function(q){ return String(q.lesson) === String(lesson.n); });
      if (lessonQuiz.length){
        body.insertAdjacentHTML('beforeend', blCap('?','Quiz desta aula ('+lessonQuiz.length+' questões, com tradução) — o enunciado é em inglês, como na prova','Lesson quiz ('+lessonQuiz.length+' questions, with translation) — wording is in English, as in the exam'));
        lessonQuiz.forEach(function(q, qi){
          body.appendChild(buildQuizItem(q, mod.id+'-'+lesson.n+'-'+qi));
        });
      }

      det.appendChild(body);
      section.appendChild(det);
    });

    // Glossary
    if (mod.glossary && mod.glossary.length){
      var gHead = el('div','section-head');
      gHead.innerHTML = '<span class="section-num">Gloss.</span><h2 class="h" style="font-size:18px;">Glossário — '+esc(mod.title)+'</h2>';
      section.appendChild(gHead);
      var dl = el('dl','glossary');
      mod.glossary.forEach(function(g){
        var termDiv = el('div','term');
        var tEn = (g.t_en && g.t_en.trim().toLowerCase() !== String(g.t).trim().toLowerCase()) ? ' <span class="t-en">— '+esc(g.t_en)+'</span>' : '';
        termDiv.innerHTML = '<dt>'+esc(g.t)+tEn+'</dt><dd>'+blGrid(wrapP(esc(g.d)), wrapP(esc(g.d_en||'')))+'</dd>';
        dl.appendChild(termDiv);
      });
      section.appendChild(dl);
    }

    // Keywords — bilingual chips
    if (mod.keywords && mod.keywords.length){
      var kHead = el('div','section-head');
      kHead.innerHTML = '<span class="section-num">Chaves</span><h2 class="h" style="font-size:18px;">Palavras-chave <span style="font-style:italic;font-weight:400;color:var(--ink-muted);font-size:14px;">· Keywords</span></h2>';
      section.appendChild(kHead);
      var kwrow = el('div','kwrow');
      mod.keywords.forEach(function(k, ki){
        var kEn = (mod.keywords_en || [])[ki] || '';
        var same = kEn.trim().toLowerCase() === String(k).trim().toLowerCase();
        var chip = el('span', null);
        chip.innerHTML = '<span class="chip-pt">'+esc(k)+'</span>' + (same || !kEn ? '' : '<span class="chip-sep">·</span><span class="chip-en">'+esc(kEn)+'</span>');
        kwrow.appendChild(chip);
      });
      section.appendChild(kwrow);
    }

    // Attention points — bilingual
    if (mod.attention && mod.attention.length){
      var aHead = el('div','section-head');
      aHead.innerHTML = '<span class="section-num">&#9888;</span><h2 class="h" style="font-size:18px;">Pontos de atenção para a prova <span style="font-style:italic;font-weight:400;color:var(--ink-muted);font-size:14px;">· Points of attention for the exam</span></h2>';
      section.appendChild(aHead);
      mod.attention.forEach(function(a){
        var box = el('div','attn');
        var ptHtml = typeof a === 'string' ? a : (a.pt || '');
        var enHtml = typeof a === 'string' ? '' : (a.en || '');
        box.innerHTML = blGrid(wrapP(ptHtml), wrapP(enHtml));
        section.appendChild(box);
      });
    }

    modulesRoot.appendChild(section);
  });

  // ---------- Simulados completos (mock exams, by topic) ----------
  var SIMULADOS = DATA.simulados || [];
  if (SIMULADOS.length){
    var simRoot = document.getElementById('simulados-root');
    SIMULADOS.forEach(function(sim, si){
      var det = el('details','lesson simulado');
      var sum = el('summary');
      sum.innerHTML = '<span class="lesson-n">'+esc(sim.num)+'</span><span class="lesson-ttl">'+esc(sim.title_pt)
        + ' <span class="sim-ttl-en">· '+esc(sim.title_en)+'</span></span><span class="chev">&#8250;</span>';
      det.appendChild(sum);

      var body = el('div','lesson-body');
      body.insertAdjacentHTML('beforeend', blGrid(wrapP('<p>'+esc(sim.desc_pt)+'</p>'), wrapP('<p>'+esc(sim.desc_en)+'</p>')));
      body.insertAdjacentHTML('beforeend', blCap('#', sim.questions.length+' questões deste simulado', sim.questions.length+' questions in this mock exam'));
      sim.questions.forEach(function(q, qi){
        body.appendChild(buildQuizItem(q, 'sim-'+sim.num+'-'+qi, '💡', 'Dica (justificativa)', 'Hint (rationale)'));
      });
      det.appendChild(body);
      simRoot.appendChild(det);
    });
  }

  function buildQuizItem(q, uid, capIcon, capPt, capEn){
    var item = el('div','quiz-item');
    var srcBadge = q.source === 'synth'
      ? '<span class="quiz-src" title="Questão elaborada com base na ementa oficial, sem fonte extraída">complementar · supplementary</span>'
      : (q.source === 'guide'
        ? '<span class="quiz-src" title="Questão do guia de simulados fornecido pelo usuário">guia de simulados · mock exam guide</span>'
        : '<span class="quiz-src" title="Questão extraída do banco de estudos da comunidade">banco real · real bank</span>');
    // PT is always the left/primary column, EN always the right/muted column — same order everywhere on the page.
    item.innerHTML = '<div class="quiz-q">'+srcBadge+blGrid('<p>'+esc(q.q_pt||'')+'</p>', '<p>'+esc(q.q)+'</p>')+'</div>';
    var opts = el('div','quiz-opts');
    q.options.forEach(function(optText, oi){
      var optPt = (q.options_pt || [])[oi] || '';
      var opt = el('div','quiz-opt');
      opt.innerHTML = '<span class="lbl">'+letters[oi]+'</span><div class="opt-body">'+blGrid('<p>'+esc(optPt)+'</p>', '<p>'+esc(optText)+'</p>')+'</div>';
      opt.setAttribute('data-idx', oi);
      opt.setAttribute('tabindex','0');
      opt.setAttribute('role','button');
      opts.appendChild(opt);
    });
    item.appendChild(opts);

    var note = el('div','quiz-note');
    var notePtHtml = '<p><strong>Resposta correta: '+letters[q.correct]+'.</strong> '+esc(q.note)+'</p>';
    var noteEnHtml = '<p><strong>Correct answer: '+letters[q.correct]+'.</strong> '+esc(q.note_en || '')+'</p>';
    note.innerHTML = blCap(capIcon || '✓', capPt || 'Gabarito', capEn || 'Answer key') + blGrid(notePtHtml, noteEnHtml);
    item.appendChild(note);

    function reveal(chosenIdx){
      var optEls = opts.querySelectorAll('.quiz-opt');
      optEls.forEach(function(oEl){
        var idx = parseInt(oEl.getAttribute('data-idx'),10);
        if (idx === q.correct) oEl.classList.add('correct');
        else if (idx === chosenIdx) oEl.classList.add('wrong');
      });
      note.classList.add('show');
    }
    opts.querySelectorAll('.quiz-opt').forEach(function(oEl){
      oEl.addEventListener('click', function(){
        if (note.classList.contains('show')) return; // already answered
        reveal(parseInt(oEl.getAttribute('data-idx'),10));
      });
      oEl.addEventListener('keydown', function(e){
        if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); oEl.click(); }
      });
    });
    return item;
  }

  // ---------- Global glossary ----------
  var allTerms = [];
  MODULES.forEach(function(mod){
    (mod.glossary||[]).forEach(function(g){ allTerms.push({t: g.t, t_en: g.t_en, d: g.d, d_en: g.d_en, mod: mod.badge}); });
  });
  allTerms.sort(function(a,b){ return a.t.localeCompare(b.t, 'pt-BR', {sensitivity:'base'}); });
  var ggHost = document.getElementById('global-glossary');
  allTerms.forEach(function(g){
    var termDiv = el('div','term');
    var tEn = (g.t_en && g.t_en.trim().toLowerCase() !== String(g.t).trim().toLowerCase()) ? ' <span class="t-en">— '+esc(g.t_en)+'</span>' : '';
    termDiv.innerHTML = '<dt>'+esc(g.t)+tEn+' <span style="color:var(--ink-muted);font-weight:400;">— '+esc(g.mod)+'</span></dt><dd>'+blGrid(wrapP(esc(g.d)), wrapP(esc(g.d_en||'')))+'</dd>';
    ggHost.appendChild(termDiv);
  });

  // ---------- Sources ----------
  var SOURCES = [
    {label: "Trilha oficial — Claude Partner Network Learning Path", url: "https://anthropic-partners.skilljar.com/page/claude-partner-network-learning-path"},
    {label: "Curso — Introduction to Agent Skills (syllabus oficial)", url: "https://anthropic-partners.skilljar.com/introduction-to-agent-skills"},
    {label: "Curso — Building with the Claude API (syllabus oficial)", url: "https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api"},
    {label: "Curso — Introduction to Model Context Protocol (syllabus oficial)", url: "https://anthropic-partners.skilljar.com/introduction-to-model-context-protocol"},
    {label: "Curso — Claude Code in Action (syllabus oficial)", url: "https://anthropic-partners.skilljar.com/claude-code-in-action"},
    {label: "Guia de estudos em português (comunidade)", url: "https://lulippe4-hub.github.io/guia-estudos-anthropic/"},
    {label: "Repositório de estudo claude-certification (comunidade)", url: "https://github.com/MateusBurkle/claude-certification"},
  ];
  var srcHost = document.getElementById('sources');
  SOURCES.forEach(function(s){
    var row = el('div','res');
    row.innerHTML = '<span><a href="'+s.url+'" target="_blank" rel="noopener">'+esc(s.label)+'</a></span>';
    srcHost.appendChild(row);
  });

  // ---------- Search filter (matches PT and EN text) ----------
  var searchbox = document.getElementById('searchbox');
  var debounceTimer = null;
  searchbox.addEventListener('input', function(){
    clearTimeout(debounceTimer);
    var query = searchbox.value.trim().toLowerCase();
    debounceTimer = setTimeout(function(){ applyFilter(query); }, 120);
  });

  function applyFilter(query){
    var lessonEls = document.querySelectorAll('details.lesson');
    var termEls = document.querySelectorAll('#modules-root .term, #global-glossary .term');
    var kwEls = document.querySelectorAll('.kwrow span');

    if (!query){
      lessonEls.forEach(function(e){ e.classList.remove('hidden-by-search'); });
      termEls.forEach(function(e){ e.classList.remove('hidden-by-search'); });
      kwEls.forEach(function(e){ e.classList.remove('hidden-by-search'); });
      return;
    }
    lessonEls.forEach(function(e){
      var match = e.textContent.toLowerCase().indexOf(query) !== -1;
      e.classList.toggle('hidden-by-search', !match);
      if (match) e.open = true;
    });
    termEls.forEach(function(e){
      var match = e.textContent.toLowerCase().indexOf(query) !== -1;
      e.classList.toggle('hidden-by-search', !match);
    });
    kwEls.forEach(function(e){
      var match = e.textContent.toLowerCase().indexOf(query) !== -1;
      e.classList.toggle('hidden-by-search', !match);
    });
  }
})();
