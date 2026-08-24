# -*- coding: utf-8 -*-
import json

m4 = {
    "id": "mod-code",
    "badge": "Módulo 4",
    "title": "Claude Code em Ação",
    "subtitle": "Claude Code in Action",
    "desc": "Rodar sessões longas e pouco supervisionadas com confiança: direcionar, configurar, automatizar e verificar o trabalho do Claude Code em escala.",
    "lessons": [],
    "glossary": [],
    "keywords": [
        "plan mode", "compactação de resumo", "menu de retrocesso (rewind)", "CLAUDE.md", "permission modes",
        "hooks (PreToolUse/PostToolUse)", "verification skills", "rotinas / headless mode", "claude -p",
        "GitHub Actions", "code review automatizado", "verificação proporcional", "plugins", "marketplace de plugins",
    ],
    "attention": [
        "As 4 fases do curso formam a espinha dorsal da prova: <strong>Steer → Configure → Automate → Verify</strong> — direcionar, configurar, automatizar, verificar.",
        "<strong>Plan mode</strong> restringe o Claude Code a só planejar (sem editar arquivos) até você aprovar o plano — essencial para sessões longas onde você quer revisar antes de qualquer mudança.",
        "O <strong>menu de retrocesso</strong> (rewind/checkpoint) permite voltar a um estado anterior da sessão quando o Claude tomou um caminho errado, sem precisar reiniciar do zero.",
        "Um <strong>CLAUDE.md eficiente</strong> é enxuto e específico — regras vagas ('escreva bom código') são ignoradas na prática; regras concretas ('nunca faça commit direto na main') são seguidas.",
        "<strong>Permission modes</strong> controlam o quanto o Claude Code pode agir sem pedir confirmação — do mais restrito (perguntar sempre) ao mais autônomo (aceitar edições automaticamente).",
        "<strong>Hooks</strong> disparam em eventos do ciclo de vida (antes/depois de uma tool ser usada, por exemplo) e são o mecanismo certo para regras não-negociáveis (ex.: sempre rodar o linter antes de um commit).",
        "<strong>Modo headless</strong> (<code>claude -p</code>) permite rodar o Claude Code sem interface interativa — a base de rotinas automatizadas e pipelines de CI/CD.",
        "Verificação de execuções não supervisionadas deve ser <strong>proporcional ao risco</strong> — testes reais (rodar a suíte, checar o build) validam melhor do que o Claude apenas dizer que terminou.",
        "<strong>Plugins</strong> empacotam uma configuração (Skills, hooks, comandos) para reuso e distribuição — o mesmo mecanismo de compartilhamento visto no Módulo 1 de Agent Skills.",
    ],
}

m4["lessons"] = [
  {"n": "1.1", "title": "Direcionando sessões longas (Steering Long Sessions)",
   "topics": ["Escopo com plan mode", "Compactação de resumo direta", "Menu de retrocesso (rewind)", "Direcionamento manual vs. execução autônoma"],
   "material": "<p>Sessões longas e pouco supervisionadas de Claude Code exigem mecanismos de <strong>direcionamento</strong> diferentes de uma sessão curta e interativa. O <strong>plan mode</strong> restringe a sessão a só planejar — sem editar nada — até você revisar e aprovar, o que dá escopo claro antes de qualquer mudança real. A <strong>compactação de resumo</strong> condensa o histórico da conversa quando ele cresce demais, preservando o essencial sem perder o contexto de trabalho. O <strong>menu de retrocesso</strong> permite voltar a um checkpoint anterior da sessão quando o caminho tomado não foi o certo, evitando recomeçar do zero. Por fim, a escolha entre <strong>direcionamento manual</strong> (você aprova cada passo) e <strong>execução autônoma</strong> (o Claude segue sem pausar) é uma decisão de risco/confiança que muda conforme a tarefa. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "2.1", "title": "Um CLAUDE.md que funciona",
   "topics": ["Regras concretas vs. vagas", "O que colocar (e o que não colocar) no CLAUDE.md", "Escopo por projeto vs. por usuário"],
   "material": "<p>Um CLAUDE.md eficaz contém regras <strong>concretas e verificáveis</strong> — \"nunca altere migrations já aplicadas\" funciona; \"escreva código de qualidade\" não. É o lugar certo para padrões que devem valer em <strong>toda</strong> sessão daquele projeto (ou, em nível de usuário, em todos os seus projetos). Regras muito longas ou genéricas competem por atenção com o que realmente importa — o mesmo princípio de progressive disclosure visto nas Skills (Módulo 1) se aplica aqui: o CLAUDE.md deve ser enxuto, com detalhe adicional em arquivos referenciados quando necessário. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "2.2", "title": "Modos de permissão (Permission Modes)",
   "topics": ["Espectro de autonomia (perguntar sempre → aceitar edições automaticamente)", "Quando usar cada modo", "Risco vs. velocidade"],
   "material": "<p>Os <strong>modos de permissão</strong> definem o quanto o Claude Code pode agir sem parar para confirmar com você — de um extremo em que toda ação sensível (editar arquivo, rodar comando) pede aprovação, até um extremo em que edições são aceitas automaticamente. A escolha do modo é uma decisão de arquitetura de confiança: sessões exploratórias em código de produção crítico pedem mais confirmação; tarefas repetitivas e já validadas em um sandbox seguro toleram mais autonomia. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "2.3", "title": "Hooks",
   "topics": ["Disparo por evento do ciclo de vida (PreToolUse, PostToolUse etc.)", "Regras não-negociáveis via hooks", "Hooks vs. Skills vs. CLAUDE.md"],
   "material": "<p><strong>Hooks</strong> disparam automaticamente em eventos do ciclo de vida de uma sessão — antes ou depois do uso de uma tool, por exemplo — e são o mecanismo certo para regras <strong>não-negociáveis</strong> que não dependem de o Claude \"lembrar\" de segui-las: rodar um linter a cada edição de arquivo, bloquear um comando perigoso, validar um formato antes de aceitar uma tool call. Diferem de Skills (que ativam por correspondência de pedido) e de CLAUDE.md (que é lido, não executado): hooks são código que roda garantidamente, no momento certo. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "2.4", "title": "Verification Skills",
   "topics": ["Empacotar procedimentos de verificação como Skills", "Verificação como parte do fluxo, não uma etapa extra"],
   "material": "<p>Procedimentos de verificação (checar se os testes passam, se o build está limpo, se um padrão foi seguido) podem ser empacotados como <strong>Skills de verificação</strong> — reaproveitando exatamente o mecanismo do Módulo 1: uma Skill que o Claude ativa sempre que a tarefa envolve validar um resultado, garantindo que a verificação aconteça de forma consistente, e não dependa do Claude lembrar de fazê-la a cada vez. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "3.1", "title": "Rotinas e modo headless",
   "topics": ["Agendar prompts como rotinas", "claude -p (modo headless, sem interface interativa)", "Pipelines próprios (fora de uma sessão de chat)"],
   "material": "<p><strong>Rotinas</strong> agendam um prompt para rodar automaticamente (uma verificação diária, um relatório semanal), e o <strong>modo headless</strong> (invocado com uma flag como <code>claude -p</code>) executa o Claude Code sem a interface interativa normal — devolvendo o resultado programaticamente. É a base para integrar o Claude Code em pipelines próprios: um script de CI, um cron job, qualquer processo automatizado que precise da capacidade do Claude Code sem um humano na tela. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "3.2", "title": "GitHub Actions e revisão de código",
   "topics": ["Integração com pull requests", "Revisão de código automatizada", "Claude Code como etapa de um workflow de CI/CD"],
   "material": "<p>Integrar o Claude Code a <strong>GitHub Actions</strong> permite que ele participe do ciclo de vida de um pull request — revisando código automaticamente, sinalizando problemas ou sugerindo mudanças como parte do pipeline de CI/CD, sem exigir que alguém dispare a revisão manualmente a cada PR. É uma aplicação direta do modo headless: o Claude Code roda como mais uma etapa automatizada do workflow. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "4.1", "title": "Confiando: verificando execuções não supervisionadas",
   "topics": ["Verificação proporcional ao risco", "Testes reais como validadores (não a palavra do Claude)", "Construindo confiança em automações"],
   "material": "<p>Confiar em uma execução não supervisionada exige <strong>verificação proporcional</strong> ao risco da tarefa: para mudanças triviais, uma checagem leve basta; para mudanças críticas, é preciso validação real — rodar a suíte de testes, checar o build, comparar contra um resultado esperado — em vez de aceitar apenas a afirmação do Claude de que \"terminou com sucesso\". A confiança em automações se constrói incrementalmente, expandindo o escopo autônomo conforme a verificação real confirma que o processo é robusto. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "4.2", "title": "Plugins",
   "topics": ["Empacotar Skills, hooks e comandos como plugin", "Distribuição via marketplace", "Reuso entre projetos e times"],
   "material": "<p><strong>Plugins</strong> empacotam uma configuração completa — Skills, hooks, comandos — em uma unidade distribuível, publicável em um marketplace para reuso por outros times ou pela comunidade. É o mesmo mecanismo de compartilhamento visto no Módulo 1 (Skills via plugin), agora estendido a todo o conjunto de customizações do Claude Code, permitindo que uma configuração testada seja instalada em segundos em outro projeto. <span class='badge synth'>complementar</span></p>",
  },
]

quiz4 = []
def add4(lesson, q, options, correct, note, source="synth"):
    quiz4.append({"lesson": lesson, "q": q, "options": options, "correct": correct, "note": note, "source": source})

add4("1.1", "What does \"plan mode\" restrict Claude Code to doing before you approve?",
    ["Only reading documentation, never writing code","Planning only — no file edits — until the plan is reviewed and approved","Running tests but not making commits","Using only one tool at a time","Working exclusively in headless mode"], 1,
    "Plan mode restringe a só planejar, sem editar, até aprovação.")
add4("1.1", "What is the purpose of the \"rewind\" menu in a long Claude Code session?",
    ["To permanently delete the session history","To let you return to an earlier checkpoint when the session took a wrong turn","To switch to a different Claude model mid-session","To automatically approve all pending edits","To generate a summary email of the session"], 1,
    "Permite voltar a um checkpoint anterior sem recomeçar do zero.")
add4("1.1", "Why does context compaction matter in long, hands-off sessions?",
    ["It permanently deletes irrelevant files from disk","It condenses a growing conversation history so essential context isn't lost as the session runs long","It disables all hooks automatically","It converts the session into headless mode","It requires switching to Claude Haiku"], 1,
    "Condensa o histórico crescente sem perder o essencial.")
add4("2.1", "Which CLAUDE.md rule is more likely to actually be followed in practice?",
    ["\"Write good quality code\"","\"Never modify migrations that have already been applied\"","\"Be helpful\"","\"Do your best\"","\"Try to be efficient\""], 1,
    "Regras concretas e verificáveis funcionam; regras vagas não.")
add4("2.1", "What kind of standards belong in CLAUDE.md rather than in a Skill?",
    ["Standards that should always apply in every session for that project","Knowledge that is only relevant sometimes, on specific request","A checklist that should load on demand","A procedure meant to stay out of context until needed","A troubleshooting guide for rare edge cases"], 0,
    "CLAUDE.md é para o que deve valer sempre, em toda sessão do projeto.")
add4("2.2", "What do Permission Modes primarily control in Claude Code?",
    ["Which Claude model is used","How much Claude Code can act without stopping to ask for confirmation","The maximum context window size","Which programming language is used","The pricing tier of the account"], 1,
    "Controlam o grau de autonomia sem confirmação.")
add4("2.2", "In which scenario would a stricter (ask-more-often) permission mode be more appropriate?",
    ["A repetitive, already-validated task in a safe sandbox","An exploratory session touching critical production code","Generating a random test dataset","Reading a public documentation page","Running a linter with no side effects"], 1,
    "Código de produção crítico pede mais confirmação, não menos.")
add4("2.3", "What triggers a hook in Claude Code?",
    ["A user typing a slash command","A matching request, the same way a Skill activates","A lifecycle event, such as before or after a tool is used","The end of the billing cycle","A change to the Claude model version"], 2,
    "Hooks disparam por evento do ciclo de vida, não por pedido.")
add4("2.3", "Why are hooks the right mechanism for \"non-negotiable\" rules, compared to relying on a prompt instruction?",
    ["Hooks run guaranteed code at the right moment, instead of depending on Claude remembering an instruction","Hooks are cheaper than any other Claude Code feature","Hooks can only be written by administrators","Hooks replace the need for CLAUDE.md entirely","Hooks require no configuration at all"], 0,
    "Hooks garantem execução no momento certo, sem depender de \"lembrar\".")
add4("2.4", "What is a \"verification skill\" in the context of Claude Code?",
    ["A Skill that Claude activates to package and run a consistent verification procedure","A hook that fires only on Fridays","A permission mode that disables all verification","A plugin that replaces the need for tests","A CLAUDE.md section about code style"], 0,
    "Empacota um procedimento de verificação como Skill reutilizável.")
add4("3.1", "What does headless mode (e.g. `claude -p`) allow you to do?",
    ["Run Claude Code without the normal interactive interface, suitable for scripts and pipelines","Hide the terminal output permanently","Disable all permission checks by default","Use Claude Code only inside a web browser","Run two Claude models simultaneously"], 0,
    "Roda sem interface interativa, ideal para scripts/pipelines.")
add4("3.1", "What is a \"routine\" in this context?",
    ["A one-time manual chat message","A scheduled prompt that runs automatically on a recurring basis","A type of hook that only fires on errors","A synonym for a Skill","A plugin marketplace category"], 1,
    "Um prompt agendado para rodar automaticamente.")
add4("3.2", "What does integrating Claude Code with GitHub Actions typically enable?",
    ["Claude Code participating in the pull request lifecycle, e.g. automated code review","Deleting old pull requests automatically","Replacing the need for a code review process entirely","Disabling CI/CD for the repository","Converting all pull requests into Skills"], 0,
    "Participação no ciclo de vida de PRs, como revisão automatizada.")
add4("4.1", "What does \"proportional verification\" mean for unsupervised Claude Code runs?",
    ["Always run the exact same verification regardless of risk","Match the depth of verification to how risky or critical the change is","Never verify autonomous runs, to save time","Verification is only needed for headless mode","Only verify changes made by Claude Opus"], 1,
    "A profundidade da verificação deve casar com o risco da mudança.")
add4("4.1", "Why is running the real test suite a better verification method than trusting Claude's own claim of success?",
    ["It is always faster than asking Claude","It provides an objective, independent check instead of relying on a self-report","Claude is incapable of running tests itself","It removes the need for CLAUDE.md","It disables hooks during verification"], 1,
    "Um teste real é um validador objetivo e independente.")
add4("4.2", "What do Claude Code plugins typically package together for distribution?",
    ["Only a single SKILL.md file","Skills, hooks, and commands as one reusable, distributable unit","A single permission mode setting","Only CLAUDE.md content","A single MCP server binary"], 1,
    "Empacotam Skills, hooks e comandos juntos para reuso/distribuição.")

m4["quiz"] = quiz4
with open("/home/claude/module4_final.json", "w", encoding="utf-8") as f:
    json.dump(m4, f, ensure_ascii=False, indent=1)
print("MODULE 4 -> lessons:", len(m4["lessons"]), "quiz:", len(m4["quiz"]))
