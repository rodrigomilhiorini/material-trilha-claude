# -*- coding: utf-8 -*-
import json

MODULES = []

# ======================================================================
# MODULE 1 — Introdução às Habilidades de Agente (Agent Skills)
# ======================================================================
m1 = {
    "id": "mod-skills",
    "badge": "Módulo 1",
    "title": "Introdução às Habilidades de Agente",
    "subtitle": "Introduction to Agent Skills",
    "desc": "Como ensinar Claude Code a fazer algo uma vez e reaplicar automaticamente — Skills, sua estrutura, prioridade, compartilhamento e diagnóstico de problemas.",
    "lessons": [],
    "glossary": [],
    "keywords": [
        "SKILL.md", "frontmatter", "name", "description", "allowed-tools", "model (campo)",
        "progressive disclosure", "scripts/", "references/", "assets/", "semantic matching",
        "~/.claude/skills", ".claude/skills", "enterprise managed settings", "strictKnownMarketplaces",
        "subagent", "hook", "slash command", "CLAUDE.md", "claude --debug", "skills validator", "chmod +x"
    ],
    "attention": [
        "O campo <strong>name</strong> aceita só letras minúsculas, números e hífens, no máximo 64 caracteres, e deve bater com o nome da pasta.",
        "O campo <strong>description</strong> tem no máximo 1.024 caracteres e é o mais importante: é ele que o Claude usa para decidir quando ativar a Skill (matching semântico, não por palavra-chave exata).",
        "No startup, o Claude Code carrega <strong>apenas name e description</strong> de cada Skill — o conteúdo completo só entra em contexto quando a Skill é ativada (economia de contexto).",
        "Ordem de prioridade quando duas Skills têm o mesmo nome: <strong>Enterprise &gt; Personal &gt; Project &gt; Plugins</strong>.",
        "<strong>Subagents não herdam Skills automaticamente</strong> — precisam listá-las explicitamente no campo <em>skills</em> do frontmatter do agente, e elas carregam quando o subagent inicia (não sob demanda).",
        "Os agentes embutidos <strong>Explorer, Plan e Verify nunca acessam Skills</strong>, mesmo custom subagents podem.",
        "O arquivo deve se chamar exatamente <strong>SKILL.md</strong> (maiúsculo SKILL, minúsculo md) e estar dentro de uma pasta com nome próprio — nunca direto na raiz de skills/.",
        "Regra de decisão entre as 5 opções de customização: CLAUDE.md = sempre ativo; Skills = sob demanda (request-driven); Hooks = disparados por evento; Subagents = contexto isolado; MCP = ferramentas/integrações externas.",
        "allowed-tools restringe o que o Claude pode usar enquanto a Skill está ativa; se omitido, não restringe nada (permissão normal).",
    ],
}

m1["lessons"] = [
  {
    "n": 1, "title": "O que são Skills (matching e onde vivem)",
    "topics": ["Definição de Skill", "Estrutura do SKILL.md", "Matching por description", "Skills pessoais vs. de projeto", "Skills vs. CLAUDE.md vs. slash commands"],
    "material": "<p>Uma <strong>Skill</strong> é uma pasta de instruções e recursos que o Claude Code descobre e usa para executar uma tarefa com mais precisão. O núcleo de toda Skill é o arquivo <strong>SKILL.md</strong>, com um frontmatter (metadados) contendo <em>name</em> e <em>description</em>, seguido das instruções propriamente ditas.</p><p>O campo <em>description</em> é o mecanismo de correspondência: o Claude compara o seu pedido com as descrições de todas as Skills disponíveis e ativa as que combinam. Por isso uma descrição clara e específica é o que faz a Skill disparar no momento certo. Apenas name e description são carregados de início — o conteúdo completo só é lido quando a Skill é ativada, o que mantém a janela de contexto eficiente.</p><p><strong>Skills pessoais</strong> vivem em <code>~/.claude/skills</code> e acompanham você em todos os projetos (estilo de commit, formato de explicação de código). <strong>Skills de projeto</strong> vivem em <code>.claude/skills</code> na raiz do repositório e são compartilhadas com todo o time via versionamento.</p><p>Comparando as três formas de customizar o Claude Code: CLAUDE.md carrega em toda conversa (regras sempre válidas, como \"use TypeScript strict mode\"); Skills carregam sob demanda, só quando combinam com o pedido; slash commands exigem digitação explícita — Skills não precisam ser invocadas, o Claude as aplica automaticamente ao reconhecer a situação.</p>",
  },
  {
    "n": 2, "title": "Criando sua primeira Skill",
    "topics": ["Criando o diretório e o SKILL.md", "Testando a Skill (restart necessário)", "Matching semântico em detalhe", "Prioridade: Enterprise > Personal > Project > Plugins", "Atualizando e removendo Skills"],
    "material": "<p>Para criar uma Skill pessoal, o nome do diretório deve bater com o nome da Skill: <code>mkdir -p ~/.claude/skills/pr-description</code>. Dentro, o SKILL.md tem duas partes separadas pelas cercas de frontmatter (<code>---</code>): metadados no topo, instruções abaixo.</p><p>O Claude Code carrega Skills na inicialização, então é preciso <strong>reiniciar a sessão</strong> depois de criar, editar ou remover uma. Ao enviar um pedido, o Claude compara sua mensagem com as descrições disponíveis usando <strong>matching semântico</strong> (por significado e intenção, não por palavra exata) — \"explique o que essa função faz\" pode ativar uma Skill descrita como \"explicar código com diagramas visuais\" porque a intenção se sobrepõe. Depois de encontrar uma correspondência, o Claude pede confirmação antes de carregar a Skill por completo.</p><p>Quando duas Skills têm o mesmo nome, a ordem de prioridade — da mais alta para a mais baixa — é: <strong>Enterprise (managed settings) → Personal (~/.claude/skills) → Project (.claude/skills) → Plugins</strong>. Isso permite que a organização imponha padrões via Skills enterprise, sem impedir customização individual. Para evitar conflitos, prefira nomes descritivos (\"frontend-review\" em vez de \"review\").</p>",
  },
  {
    "n": 3, "title": "Configuração e Skills multi-arquivo",
    "topics": ["Campos do frontmatter (name, description, allowed-tools, model)", "Escrevendo descrições eficazes", "Restringindo ferramentas com allowed-tools", "Progressive disclosure (scripts/, references/, assets/)", "Executar script vs. ler script"],
    "material": "<p>O padrão aberto de Agent Skills define 4 campos no frontmatter: <strong>name</strong> (obrigatório, minúsculas/números/hífens, até 64 caracteres) e <strong>description</strong> (obrigatório, até 1.024 caracteres — o campo mais importante para o matching) são os únicos obrigatórios; <strong>allowed-tools</strong> (opcional) restringe quais ferramentas o Claude pode usar enquanto a Skill está ativa; e <strong>model</strong> (opcional) especifica qual modelo Claude usar para essa Skill.</p><p>Uma boa descrição responde a duas perguntas: o que a Skill faz, e quando o Claude deve usá-la. Se uma Skill não está disparando quando esperado, o conserto recomendado é adicionar mais palavras-chave que reflitam como você realmente formula os pedidos.</p><p><strong>Progressive disclosure</strong> resolve o problema de Skills grandes competirem pelo mesmo espaço de contexto da conversa: mantenha o essencial no SKILL.md (regra prática: menos de 500 linhas) e coloque referências, exemplos e scripts em arquivos separados dentro de <code>scripts/</code> (código executável), <code>references/</code> (documentação adicional) e <code>assets/</code> (imagens, templates). O SKILL.md aponta para esses arquivos e explica quando carregá-los — como um sumário em vez do documento inteiro.</p><p>Scripts podem <strong>executar sem que seu conteúdo entre em contexto</strong> — só a saída consome tokens. A instrução certa no SKILL.md é dizer ao Claude para <em>rodar</em> o script, não para <em>ler</em> o script.</p>",
  },
  {
    "n": 4, "title": "Skills vs. outros recursos do Claude Code",
    "topics": ["CLAUDE.md vs. Skills", "Skills vs. Subagents", "Skills vs. Hooks", "MCP servers (categoria diferente)", "Combinando os cinco recursos"],
    "material": "<p>Claude Code oferece cinco formas de customização, cada uma com sua especialidade — a ideia central é combiná-las, não forçar tudo em uma só:</p><ul><li><strong>CLAUDE.md</strong> — carrega em toda conversa; use para padrões sempre válidos do projeto (\"nunca altere o schema do banco\").</li><li><strong>Skills</strong> — carregam sob demanda; use para conhecimento específico de tarefa que não precisa estar sempre presente.</li><li><strong>Hooks</strong> — disparados por evento (ex.: rodar um linter a cada salvamento de arquivo), não por pedido.</li><li><strong>Subagents</strong> — rodam em contexto isolado, separado da conversa principal; use quando quiser delegar com acesso a ferramentas diferente ou isolamento do trabalho.</li><li><strong>MCP servers</strong> — categoria totalmente diferente: fornecem ferramentas e integrações externas, enquanto Skills adicionam conhecimento ao raciocínio do Claude.</li></ul><p>Diferença-chave entre Skills e Subagents: Skills somam conhecimento à conversa atual; Subagents recebem uma tarefa, trabalham isolados e retornam resultado, sem compartilhar o contexto principal.</p>",
  },
  {
    "n": 5, "title": "Compartilhando Skills",
    "topics": ["Commit no repositório (.claude/skills)", "Distribuição via plugins/marketplace", "Enterprise managed settings e strictKnownMarketplaces", "Skills e subagents (não herdam automaticamente)", "Configurando subagents customizados com skills"],
    "material": "<p>Existem três formas de distribuir Skills. <strong>Commit no repositório</strong> — colocar em <code>.claude/skills</code> e versionar: qualquer pessoa que clona o repo ganha as Skills automaticamente, ideal para padrões de time e workflows específicos do projeto. <strong>Plugins</strong> — uma pasta skills dentro do projeto do plugin, distribuída por um marketplace; melhor quando a Skill é útil além do seu time imediato. <strong>Enterprise managed settings</strong> — administradores implantam Skills para toda a organização; elas têm a <strong>prioridade mais alta</strong>, sobrepondo Skills pessoais, de projeto e de plugin com o mesmo nome — a opção certa para padrões obrigatórios, segurança e compliance. O campo <code>strictKnownMarketplaces</code> nas managed settings controla de onde plugins podem ser instalados.</p><p>Um detalhe que surpreende: <strong>subagents não veem suas Skills automaticamente</strong> — começam com contexto limpo. Agentes embutidos (Explorer, Plan, Verify) nunca acessam Skills. Subagents customizados podem usar Skills, mas só as que forem listadas explicitamente no campo <code>skills</code> do frontmatter do arquivo em <code>.claude/agents</code> — e elas carregam quando o subagent inicia, não sob demanda como na conversa principal.</p>",
  },
  {
    "n": 6, "title": "Solucionando problemas com Skills",
    "topics": ["Validador de Skills", "Skill não dispara (description)", "Skill não carrega (nome/local do arquivo)", "Skill errada é usada (descrições parecidas)", "Conflito de prioridade", "Plugins não aparecem", "Erros em tempo de execução"],
    "material": "<p>O primeiro passo diante de qualquer problema é rodar o <strong>validador de Skills</strong>, que pega problemas estruturais antes de qualquer outra investigação.</p><p><strong>Não dispara:</strong> quase sempre é a description não sobrepondo o jeito como você realmente pede. Teste variações (\"me ajuda a otimizar isso\", \"por que está lento?\") e adicione as que falharem como palavras-chave.</p><p><strong>Não carrega:</strong> confira se o SKILL.md está dentro de uma pasta nomeada (não na raiz de skills/) e se o nome do arquivo é exatamente <code>SKILL.md</code> (maiúsculo SKILL, minúsculo md). Rode <code>claude --debug</code> para ver erros de carregamento.</p><p><strong>Skill errada:</strong> descrições parecidas demais — torne-as mais distintas.</p><p><strong>Conflito de prioridade:</strong> uma Skill enterprise com o mesmo nome sempre vence uma pessoal — o caminho mais fácil é renomear a sua.</p><p><strong>Plugin sem Skills aparecendo:</strong> limpe o cache, reinicie o Claude Code e reinstale.</p><p><strong>Erros de execução:</strong> dependências não instaladas, scripts sem permissão de execução (rode <code>chmod +x</code>), ou separadores de caminho — use sempre barra normal (/), mesmo no Windows.</p>",
  },
  {
    "n": "RR", "title": "Rodada de reforço — revisão geral do Módulo 1",
    "topics": ["Estrutura de pastas e papel de cada arquivo", "Regras de nome e sintaxe", "Comportamento de carregamento (sessão principal vs. subagent)", "Revisão dos pontos mais errados por quem já fez a prova"],
    "material": "<p>Fechando o Módulo 1, esta rodada de reforço revisita os pontos que mais geram confusão na prática: onde cada tipo de Skill mora (pessoal, projeto, enterprise, plugin), a diferença entre o conteúdo de <code>scripts/</code> (código executável) e <code>references/</code> (documentação passiva), a regra de que existe <strong>um único SKILL.md por Skill</strong>, na raiz da própria pasta, e o comportamento de carregamento em subagents (no início da execução, não sob demanda). Também reforça que <strong>nenhum agente embutido</strong> (Explorer, Plan, Verify) acessa Skills — só subagents customizados, e só as listadas explicitamente.</p>",
  },
]
MODULES.append(m1)

with open("/home/claude/module1.json", "w", encoding="utf-8") as f:
    json.dump(m1, f, ensure_ascii=False, indent=1)
print("module1 lessons:", len(m1["lessons"]))

# ---- QUIZ for Module 1 (Agent Skills) — extracted from community repo, answers derived from lesson text ----
quiz1 = []

def add(lesson, q, options, correct, note, source="real"):
    quiz1.append({"lesson": lesson, "q": q, "options": options, "correct": correct, "note": note, "source": source})

# Lesson 1
add(1, "What is the primary problem that Skills are designed to solve in Claude Code?",
    ["Reducing the size of the Claude model itself",
     "Repeatedly explaining the same instructions to Claude for recurring tasks",
     "Encrypting source code before it is committed to a repository",
     "Translating code from one programming language to another",
     "Replacing the need for a version control system"], 1,
    "Skills existem para você não ter que reexplicar a mesma coisa toda vez.")
add(1, "Which file is at the core of every Skill?",
    ["CLAUDE.md","config.yaml","SKILL.md","skill.json","README.md"], 2,
    "SKILL.md é o arquivo central, com frontmatter + instruções.")
add(1, "Which two fields are contained in a Skill's frontmatter?",
    ["title and author","path and version","name and description","trigger and priority","id and scope"], 2,
    "name e description são os dois campos citados na Lição 1 (depois a Lição 3 mostra que são os únicos obrigatórios).")
add(1, "How does Claude decide whether a particular Skill applies to a request?",
    ["It runs every Skill and keeps whichever finishes first",
     "It compares the request against each Skill's description and activates the matches",
     "It always loads the most recently edited Skill",
     "It asks the user to manually select a Skill each time",
     "It matches based on the file size of each SKILL.md"], 1,
    "O matching é feito comparando o pedido com a description de cada Skill.")
add(1, "Where do personal skills live so that they follow you across all your projects?",
    [".claude/skills inside the repository root","~/.claude/skills in your home directory",
     "/etc/claude/skills","The CLAUDE.md file at the project root","A cloud-only location managed by Anthropic"], 1,
    "Skills pessoais ficam em ~/.claude/skills, no diretório home.")
add(1, "What is a key benefit of Skills loading their full instructions on demand rather than upfront?",
    ["They can be written in any programming language",
     "They keep the context window efficient by not loading everything at once",
     "They automatically encrypt the repository","They remove the need for a description field",
     "They guarantee the Skill never needs to be updated"], 1,
    "Só name/description carregam de início; o resto só quando a Skill ativa — economiza contexto.")
add(1, "Which statement best describes how CLAUDE.md differs from a Skill?",
    ["CLAUDE.md must be invoked with a slash command; Skills load automatically",
     "CLAUDE.md loads into every conversation; Skills load on demand when matched",
     "CLAUDE.md can only store images; Skills store text",
     "CLAUDE.md is stored in the home directory; Skills cannot be",
     "CLAUDE.md and Skills are identical in behavior"], 1,
    "CLAUDE.md é sempre carregado; Skills carregam só quando combinam com o pedido.")
add(1, "How do slash commands differ from Skills in terms of activation?",
    ["Slash commands load into every conversation automatically",
     "Slash commands must be explicitly typed, while Skills activate automatically when matched",
     "Slash commands cannot be used in Claude Code at all",
     "Slash commands are stored only in project repositories",
     "Slash commands and Skills are both triggered only by file size"], 1,
    "Slash commands exigem digitação explícita; Skills não precisam de invocação manual.")
add(1, "Why are project skills useful for a team working from the same repository?",
    ["They are hidden from everyone except the repository owner",
     "They are committed to version control, so anyone who clones the repo shares them",
     "They automatically rewrite teammates' code without review",
     "They disable CLAUDE.md for all collaborators",
     "They prevent the repository from being cloned by others"], 1,
    "Skills de projeto ficam em .claude/skills e são versionadas com o código.")
add(1, "Which of the following is the best rule of thumb for recognizing a task that should become a Skill?",
    ["Any task that involves more than five files","Any task that Claude has never seen before",
     "A situation where you keep explaining the same thing to Claude repeatedly",
     "Only tasks that must run without an internet connection",
     "Only tasks that involve editing the CLAUDE.md file"], 2,
    "A regra prática do curso: repetição de explicação é sinal de que vale criar uma Skill.")

# Lesson 2
add(2, "When creating a Skill, what should the Skill's directory name match?",
    ["The name of the repository","The skill name","The current git branch",
     "The user's home directory name","The description field's first word"], 1,
    "O diretório deve ter o mesmo nome da Skill (ex.: pr-description).")
add(2, "In a SKILL.md file, what separates the metadata from the instructions?",
    ["A blank line","A pair of curly braces","Frontmatter dashes (---)","An XML tag","A markdown heading"], 2,
    "As cercas --- delimitam o frontmatter das instruções.")
add(2, "Within the frontmatter, what is the specific role of the description field?",
    ["It sets the file's permissions","It is the matching criteria that tells Claude when to use the skill",
     "It stores the git diff output","It defines which folder the skill is saved in",
     "It lists the files the skill is allowed to edit"], 1,
    "description é o critério de correspondência usado pelo Claude.")
add(2, "At startup, what does Claude Code load from each available Skill?",
    ["The complete SKILL.md content","Only the name and description",
     "Only the instructions below the frontmatter","The entire skills directory as one file",
     "Nothing until the user types a slash command"], 1,
    "No startup só name/description são carregados.")
add(2, "What type of matching does Claude use to compare a request against skill descriptions?",
    ["Exact keyword matching only","Alphabetical ordering","Semantic matching based on intent",
     "File-size comparison","Random selection among available skills"], 2,
    "É matching semântico (significado/intenção), não palavra exata.")
add(2, "What happens immediately after Claude finds a skill that matches your request?",
    ["It silently applies the skill with no notice","It deletes the conflicting skills",
     "It asks you to confirm loading the skill","It restarts Claude Code automatically",
     "It commits the skill to the repository"], 2,
    "Claude pede confirmação antes de carregar a Skill completa.")
add(2, "Why is the confirmation step before loading a skill useful?",
    ["It compresses the skill file to save space","It keeps you aware of what context Claude is pulling in",
     "It encrypts the skill before use","It permanently disables all other skills",
     "It converts the skill into a slash command"], 1,
    "Mantém você consciente do contexto que está sendo carregado.")
add(2, "Which is the correct skill priority order, from highest to lowest?",
    ["Personal → Enterprise → Plugins → Project","Plugins → Project → Personal → Enterprise",
     "Enterprise → Personal → Project → Plugins","Project → Personal → Enterprise → Plugins",
     "Enterprise → Project → Personal → Plugins"], 2,
    "Enterprise > Personal > Project > Plugins.")
add(2, "If an enterprise \"code-review\" skill and a personal \"code-review\" skill share the same name, which one takes precedence?",
    ["The personal skill","The enterprise skill","Whichever was created most recently",
     "Both run at the same time","Neither; Claude ignores both"], 1,
    "Enterprise sempre vence em caso de nome igual.")
add(2, "What must you always do after updating or removing a skill for the change to take effect?",
    ["Re-clone the repository","Rename the SKILL.md file","Restart Claude Code",
     "Clear the git diff","Delete the CLAUDE.md file"], 2,
    "Skills carregam no startup — é preciso reiniciar a sessão.")

# Lesson 3
add(3, "Which two SKILL.md frontmatter fields are required?",
    ["name and model","description and allowed-tools","name and description","model and allowed-tools","name and allowed-tools"], 2,
    "Só name e description são obrigatórios.")
add(3, "What is the maximum length of the description field?",
    ["64 characters","256 characters","500 characters","1,024 characters","2,000 characters"], 3,
    "Até 1.024 caracteres.")
add(3, "Which characters are allowed in the name field?",
    ["Uppercase letters and spaces","Lowercase letters, numbers, and hyphens only","Any Unicode character","Only numbers","Letters and underscores only"], 1,
    "Minúsculas, números e hífens, no máximo 64 caracteres.")
add(3, "A good skill description should answer which two questions?",
    ["Who wrote it and when was it updated?","What does the skill do and when should Claude use it?",
     "Which model and which repository?","How long is it and where is it stored?",
     "What tools are blocked and what is the file size?"], 1,
    "O que a Skill faz + quando o Claude deve usá-la.")
add(3, "If a skill is not triggering when expected, what is a recommended fix?",
    ["Delete the description field","Add more keywords that match how you phrase your requests",
     "Convert the skill into a slash command","Reduce the name to one character",
     "Move the skill to the plugins folder"], 1,
    "Adicionar palavras-chave que reflitam como você realmente pede.")
add(3, "What does the allowed-tools field do when set on a skill?",
    ["Grants the skill access to every possible tool","Restricts which tools Claude can use while the skill is active",
     "Chooses which model runs the skill","Sets the maximum file size","Automatically writes the instructions for you"], 1,
    "allowed-tools restringe as ferramentas disponíveis durante a Skill.")
add(3, "With allowed-tools set to \"Read, Grep, Glob, Bash,\" what can Claude NOT do while the skill is active?",
    ["Read files","Search with Grep","Edit or write files","Run Bash commands","List files with Glob"], 2,
    "Sem Edit/Write na lista, Claude não pode editar ou escrever arquivos.")
add(3, "If you omit the allowed-tools field entirely, what happens?",
    ["The skill refuses to load","The skill blocks all tools by default",
     "The skill does not restrict anything and Claude uses its normal permission model",
     "Claude can only read files","The skill requires a slash command to run"], 2,
    "Sem allowed-tools, não há restrição — vale o modelo de permissão normal.")
add(3, "What problem does progressive disclosure primarily solve?",
    ["It encrypts the skill directory","It keeps SKILL.md small and context-efficient by loading detail only when needed",
     "It forces every skill to use the same model","It removes the need for a description",
     "It automatically merges conflicting skills"], 1,
    "Mantém o SKILL.md pequeno, carregando detalhe só quando necessário.")
add(3, "Why is telling Claude to run a script (rather than read it) more context-efficient?",
    ["Because scripts are always shorter than documentation",
     "Because only the script's output consumes tokens, not its full contents",
     "Because scripts disable the context window","Because running a script deletes it afterward",
     "Because scripts never produce any output"], 1,
    "Só a saída do script consome tokens, não o código inteiro.")

# Lesson 4
add(4, "What is the defining characteristic of CLAUDE.md compared to Skills?",
    ["It loads only when explicitly invoked","It loads into every conversation, always",
     "It runs in an isolated context","It fires on file-save events","It provides external tool integrations"], 1,
    "CLAUDE.md é sempre carregado, em toda conversa.")
add(4, "Which is the best use case for CLAUDE.md?",
    ["A rarely used PR review checklist","Project-wide standards that always apply",
     "Delegating a task to an isolated context","Running a linter on every file save",
     "Connecting to an external API"], 1,
    "Padrões de projeto que sempre valem pertencem ao CLAUDE.md.")
add(4, "How do Skills differ from subagents in terms of context?",
    ["Skills run in isolation; subagents share context",
     "Skills add knowledge to the current conversation; subagents run in a separate isolated context",
     "Both always run in the same shared context","Skills fire on events; subagents fire on requests",
     "Skills provide external tools; subagents provide knowledge"], 1,
    "Skills somam à conversa atual; subagents rodam isolados.")
add(4, "When is a subagent the most appropriate choice?",
    ["When you need knowledge applied throughout the current conversation",
     "When you want to delegate work to a separate execution context with possibly different tool access",
     "When you want an instruction present in every conversation",
     "When you want to run something on every file save","When you need to connect to an MCP server"], 1,
    "Subagent = delegar para um contexto isolado, possivelmente com ferramentas diferentes.")
add(4, "What best describes how hooks are triggered?",
    ["They are request-driven based on what you ask","They are event-driven, firing on events like file saves or tool calls",
     "They load into every conversation automatically","They run only in isolated subagent contexts",
     "They must be typed as slash commands"], 1,
    "Hooks disparam por evento, não por pedido.")
add(4, "Skills, in contrast to hooks, are best described as:",
    ["Event-driven","Request-driven, activating based on what you are asking","Always-on in every conversation",
     "External integrations","Isolated execution contexts"], 1,
    "Skills são request-driven (ativam com base no pedido).")
add(4, "Which feature would you use to run a linter automatically every time Claude saves a file?",
    ["A Skill","CLAUDE.md","A hook","A subagent","An MCP server"], 2,
    "Automação por evento de salvamento = hook.")
add(4, "What category do MCP servers belong to relative to Skills?",
    ["The same category as Skills","A different category entirely — external tools and integrations",
     "A subtype of CLAUDE.md","A kind of event-driven hook","A replacement for subagents"], 1,
    "MCP é uma categoria própria: ferramentas e integrações externas.")
add(4, "What is the overall recommended approach to these five features?",
    ["Force everything into Skills for simplicity","Pick only one and ignore the rest",
     "Combine them, letting each handle its own specialty","Use MCP servers for every task",
     "Avoid CLAUDE.md whenever Skills exist"], 2,
    "A recomendação é combinar os cinco recursos, cada um em sua especialidade.")
add(4, "Which pairing of feature and purpose is correct?",
    ["Hooks — always-on project standards","Subagents — external tools and integrations",
     "CLAUDE.md — isolated execution contexts","Skills — automatic task-specific expertise that loads on demand",
     "MCP servers — validation before every file save"], 3,
    "Skills = conhecimento automático e específico, carregado sob demanda.")

# Lesson 5
add(5, "What is the simplest method for sharing skills with a team?",
    ["Emailing the SKILL.md files","Committing skills to .claude/skills in the repository",
     "Publishing them to npm manually","Storing them in each user's home directory",
     "Pasting them into CLAUDE.md"], 1,
    "Commitar em .claude/skills é o método mais simples.")
add(5, "When skills are committed to a repository, how do teammates get them?",
    ["They must install a separate plugin","Anyone who clones the repo gets them automatically",
     "An administrator must push them to each machine","They receive them only via enterprise settings",
     "They must copy them to ~/.claude/skills"], 1,
    "Clonar o repositório já traz as Skills automaticamente.")
add(5, "Which sharing method is best when your skills can be useful to the broader community beyond your immediate team?",
    ["Repository commits","Plugins distributed through a marketplace","Enterprise managed settings",
     "Personal skills in the home directory","CLAUDE.md entries"], 1,
    "Plugins via marketplace alcançam além do time imediato.")
add(5, "What priority do enterprise skills deployed via managed settings have?",
    ["The lowest priority","The same priority as personal skills",
     "The highest priority, overriding same-named personal, project, and plugin skills",
     "They only apply if no other skill exists","Priority equal to plugins"], 2,
    "Enterprise tem a prioridade mais alta de todas.")
add(5, "Enterprise managed settings are the right choice primarily for:",
    ["Experimental personal preferences","Mandatory standards, security, and compliance that must be consistent org-wide",
     "One-off project scripts","Skills you are still testing","Reducing the size of SKILL.md files"], 1,
    "Certo para padrões obrigatórios, segurança e compliance.")
add(5, "What does the strictKnownMarketplaces setting control?",
    ["Which model each skill uses","Where plugins are allowed to be installed from",
     "How many skills can load at once","The maximum length of a description",
     "Which tools a skill may call"], 1,
    "Controla as fontes permitidas para instalação de plugins.")
add(5, "What surprising behavior do subagents have regarding skills?",
    ["They load every skill automatically","They do not automatically see your skills; they start with a fresh context",
     "They can only use enterprise skills","They convert skills into hooks",
     "They share the main conversation's context"], 1,
    "Subagents começam com contexto limpo, sem ver suas Skills.")
add(5, "Which built-in agents can access skills?",
    ["Explorer only","Plan and Verify only","None of the built-in agents (Explorer, Plan, Verify) can access skills",
     "All built-in agents can","Only the Verify agent"], 2,
    "Nenhum agente embutido acessa Skills.")
add(5, "How do you make a custom subagent use specific skills?",
    ["Skills load automatically once created","Explicitly list them in the agent's frontmatter skills field",
     "Add them to CLAUDE.md","Rename the skills to match the agent","Install them as plugins first"], 1,
    "Liste-as no campo skills do frontmatter do subagent.")
add(5, "For subagents, when are the listed skills loaded?",
    ["On demand, the same way as the main conversation","When the subagent starts",
     "Only after the task completes","Never — they must be typed in","Randomly during execution"], 1,
    "Carregam quando o subagent inicia, não sob demanda.")

# Lesson 6
add(6, "What is the recommended first step when a skill isn't working?",
    ["Reinstall Claude Code","Run the skills validator tool to catch structural problems",
     "Delete the skill and rewrite it","Switch to a different model","Move the skill to the plugins folder"], 1,
    "Sempre comece pelo validador de Skills.")
add(6, "If a skill exists and passes validation but doesn't trigger, what is almost always the cause?",
    ["A corrupted SKILL.md file","The description doesn't overlap enough with how you phrase requests",
     "The wrong Claude model","Missing execute permissions","An expired plugin license"], 1,
    "É quase sempre a description não combinar semanticamente com o pedido.")
add(6, "Which of these is a correct fix for a skill that doesn't trigger?",
    ["Delete the description field","Add trigger phrases and keywords that match how you actually ask",
     "Rename SKILL.md to skill.txt","Move it to the skills root","Restrict its allowed-tools"], 1,
    "Adicionar frases/keywords que combinem com seu jeito de pedir.")
add(6, "For a skill to load, where must the SKILL.md file be placed?",
    ["At the root of the skills folder","Inside a named directory, not at the skills root",
     "Inside CLAUDE.md","In the home directory only","Anywhere, as long as it's committed"], 1,
    "Precisa estar dentro de uma pasta nomeada, não na raiz de skills/.")
add(6, "What is the exact required file name for a skill's main file?",
    ["skill.md","Skill.Md","SKILL.md (all caps SKILL, lowercase md)","SKILL.MD","skill.markdown"], 2,
    "Exatamente SKILL.md — maiúsculo SKILL, minúsculo md.")
add(6, "Which command helps you see skill loading errors?",
    ["claude --validate","claude --debug","claude --skills","claude --reload","claude --check"], 1,
    "claude --debug mostra erros de carregamento.")
add(6, "If Claude keeps using the wrong skill, what is the likely problem?",
    ["The descriptions are too similar to each other","The skills are in the wrong model",
     "There are too few skills installed","The YAML uses tabs","The scripts lack execute permission"], 0,
    "Descrições parecidas demais causam confusão entre Skills.")
add(6, "Your personal \"code-review\" skill is being ignored because an enterprise skill shares the name. What is usually the easier fix?",
    ["Delete the enterprise skill yourself","Rename your personal skill to something more distinct",
     "Reinstall Claude Code","Move your skill to a plugin","Disable semantic matching"], 1,
    "É mais fácil renomear a sua Skill pessoal.")
add(6, "A plugin is installed but its skills don't appear. What should you try first?",
    ["Rename every skill","Clear the cache, restart Claude Code, and reinstall","Switch to enterprise settings",
     "Run chmod +x on the plugin","Delete the .claude directory"], 1,
    "Limpar cache, reiniciar e reinstalar é o primeiro passo.")
add(6, "Which set of checks addresses runtime errors during skill execution?",
    ["Description keywords, file name, and YAML","Dependencies, file permissions (chmod +x), and path separators",
     "Model choice, color, and name length","Cache, marketplace, and priority","Trigger phrases and semantic overlap"], 1,
    "Erros em runtime: dependências, permissões (chmod +x) e separadores de caminho.")

# Reinforcement Round
add("RR", "In which directory do PROJECT skills live so that anyone who clones the repository gets them?",
    ["~/.claude/skills/",".claude/skills/ at the repository root",".claude/agents/","scripts/ inside the skill","A managed enterprise-only folder"], 1,
    "Skills de projeto ficam em .claude/skills/ na raiz do repo.")
add("RR", "Where do PERSONAL skills live so that they follow you across all your projects?",
    [".claude/skills/ in the repo","~/.claude/skills/ in your home directory","Inside CLAUDE.md",".claude/agents/","references/ inside the skill"], 1,
    "Pessoais ficam em ~/.claude/skills/.")
add("RR", "Which characters are valid in a skill's name field?",
    ["Uppercase letters and underscores","Lowercase letters, numbers, and hyphens only","Any Unicode character","Letters and spaces","Only digits and underscores"], 1,
    "Minúsculas, números e hífens.")
add("RR", "Within a single skill that uses progressive disclosure, what does the scripts/ folder contain?",
    ["Other skills, each with its own SKILL.md","Executable code that the skill can run","The required SKILL.md file","Only image and template assets","The subagent definition file"], 1,
    "scripts/ guarda código executável.")
add("RR", "How many SKILL.md files does a single skill have, and where does it sit?",
    ["One, inside the scripts/ folder","One, at the root of the skill's own directory","One per subfolder (scripts, references, assets)","As many as there are scripts","None — it is optional"], 1,
    "Um único SKILL.md, na raiz da pasta da própria Skill.")
add("RR", "A file like references/architecture-guide.md is best described as:",
    ["A second skill inside the first","Passive reference documentation the skill reads only when needed","An executable script the skill runs","The subagent's frontmatter","A hook that fires on save"], 1,
    "É documentação de referência, lida só quando necessário.")
add("RR", "Files placed inside a skill's scripts/ folder must follow which naming rule?",
    ["They must all be named SKILL.md","Their names are free; the SKILL.md points to them by path","They must match the skill's name exactly","They must use uppercase only","They must be named script.md"], 1,
    "Nomes livres; o SKILL.md referencia por caminho.")
add("RR", "For a CUSTOM subagent, when are the skills listed in its frontmatter loaded?",
    ["On demand, the same as the main conversation","When the subagent starts","Only after the task finishes","Never — they load via matching","Randomly during execution"], 1,
    "Carregam quando o subagent inicia.")
add("RR", "The .claude/agents/ markdown file for a subagent primarily does what with skills?",
    ["Stores the full skill instructions inline","References existing skills by name in a skills field","Creates new skills automatically","Blocks all skills from loading","Converts skills into hooks"], 1,
    "Referencia Skills existentes pelo nome, no campo skills.")
add("RR", "Which mechanism runs automatically on an event such as a file save, rather than when you make a request?",
    ["A skill","A hook","A slash command","A reference file","The SKILL.md description"], 1,
    "Hooks disparam por evento.")
add("RR", "Why is instructing Claude to RUN a script more context-efficient than having it READ the script?",
    ["Running deletes the script afterward","Only the script's output consumes tokens, not its full code","Reading is not supported in skills","Running loads the code twice for safety","Scripts never produce output"], 1,
    "Só a saída consome tokens ao executar, não o código completo.")
add("RR", "Which built-in agents can access skills?",
    ["Explorer only","Plan and Verify only","None of the built-in agents can","All of them","Only custom-named built-ins"], 2,
    "Nenhum agente embutido acessa Skills.")

print("module1 quiz count:", len(quiz1))
m1["quiz"] = quiz1

with open("/home/claude/module1.json", "w", encoding="utf-8") as f:
    json.dump(m1, f, ensure_ascii=False, indent=1)
