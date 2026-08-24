# -*- coding: utf-8 -*-
import json

m5 = {
    "id": "mod-arch",
    "badge": "Módulo 5",
    "title": "Fundamentos de Arquitetura Claude",
    "subtitle": "Claude Architecture Fundamentals",
    "desc": "O domínio de maior peso na prova (Arquitetura Agêntica & Orquestração) não tem curso introdutório dedicado na trilha oficial — este módulo consolida o conteúdo visual do seu guia de arquitetura (família de modelos, fluxo de requisição, prompt caching e orquestração de agentes) no mesmo formato dos outros módulos.",
    "figures_note": "Este módulo inclui os diagramas originais do seu material de referência.",
}

m5["lessons"] = [
  {"n": 1, "title": "A jornada do arquiteto (visão geral)",
   "topics": ["O motor: família de modelos", "A fiação: fluxo de requisição", "A otimização: prompt caching", "A estrutura final: fluxos e agentes"],
   "figures": ["slide02"],
   "material": "<p>A arquitetura de uma solução com Claude pode ser vista como uma jornada em quatro etapas. Primeiro, <strong>o motor</strong>: escolher a família de modelos certa (Opus, Sonnet ou Haiku) — o \"cérebro\" da aplicação. Segundo, <strong>a fiação</strong>: o fluxo de requisição que conecta a aplicação à API de forma seguraem cinco saltos. Terceiro, <strong>a otimização</strong>: usar prompt caching para não reprocessar (e não pagar de novo por) o mesmo contexto repetidamente. Quarto, <strong>a estrutura final</strong>: orquestrar tarefas complexas através de fluxos de trabalho e agentes de forma confiável. Este módulo percorre essas quatro etapas em detalhe — é o domínio de maior peso na prova (Arquitetura Agêntica & Orquestração, ~27%) e o que menos tem curso oficial dedicado.</p>"},
  {"n": 2, "title": "Família de modelos: Opus, Sonnet e Haiku",
   "topics": ["A metáfora do Service Desk", "Nível 1 (Haiku): triagem", "Nível 2 (Sonnet): o equilíbrio", "Nível 3 (Opus): o especialista sênior", "Matriz de decisão: velocidade x inteligência x caso de uso"],
   "figures": ["slide03", "slide04"],
   "material": "<p>Uma forma útil de decidir qual modelo usar é a <strong>metáfora do Service Desk</strong>: <strong>Haiku</strong> é o atendimento de triagem — o mais rápido e barato, ideal para volume altíssimo e baixa complexidade (ex.: status de um chamado). <strong>Sonnet</strong> é o analista pleno — o equilíbrio perfeito de velocidade e inteligência, que resolve a vasta maioria dos casos do dia a dia (chatbots, análise de código, RAG diário). <strong>Opus</strong> é o especialista sênior — o mais inteligente, reservado para tarefas que exigem raciocínio profundo e análise complexa (planejamento estratégico, análise de contexto extenso). A arquitetura ideal roteia cada tarefa para o modelo mais adequado à sua prioridade, otimizando custo, velocidade e inteligência ao mesmo tempo — nunca use Opus para tudo \"por segurança\", nem Haiku para tudo \"por economia\".</p>"},
  {"n": 3, "title": "O fluxo de requisição em 5 passos (segurança e rota)",
   "topics": ["Cliente (app) → nunca fala direto com a API", "Servidor dev: onde a API Key vive em segredo", "API Anthropic recebe a requisição", "Processamento pelo modelo", "Retorno: texto + usage + stop_reason"],
   "figures": ["slide05"],
   "material": "<p>Toda requisição segura segue 5 passos: <strong>(1) Cliente (app)</strong> — o usuário final envia o texto, mas o app <strong>nunca</strong> fala diretamente com a API Anthropic (essa é a proteção da API Key); <strong>(2) Servidor dev</strong> — é onde a API Key vive em segredo, e o servidor monta o pacote da requisição; <strong>(3) API Anthropic</strong> — recebe a requisição já validada; <strong>(4) Processamento</strong> — o modelo processa até o limite de tokens ou até terminar naturalmente; <strong>(5) Retorno</strong> — devolve o texto gerado, mais os campos <code>usage</code> (consumo de tokens) e <code>stop_reason</code> (motivo da parada). O ponto de atenção de arquitetura mais cobrado na prova é o passo 1→2: a API Key nunca deve estar acessível no cliente/front-end.</p>"},
  {"n": 4, "title": "Dentro da caixa preta: os 4 estágios de geração",
   "topics": ["1. Tokenização", "2. Embedding", "3. Contextualização", "4. Geração", "max_tokens como teto de segurança", "stop_reason como sinal vital"],
   "figures": ["slide06"],
   "material": "<p>Internamente, o modelo processa cada requisição em 4 estágios: <strong>(1) Tokenização</strong> — quebra o texto em partes numéricas menores; <strong>(2) Embedding</strong> — mapeia o significado de cada token; <strong>(3) Contextualização</strong> — analisa a relação entre os tokens vizinhos; <strong>(4) Geração</strong> — prevê a resposta palavra por palavra. Dois campos monitoram esse processo de fora: <code>max_tokens</code> é o <strong>teto de segurança</strong> — não é o tamanho exato da resposta, é um limite máximo de gastos, e a geração pode terminar naturalmente bem antes de atingir esse teto. Já <code>stop_reason</code> é o <strong>sinal vital</strong> — diz ao servidor se o modelo terminou naturalmente (<code>end_turn</code>) ou se foi cortado abruptamente ao bater no teto de <code>max_tokens</code>.</p>"},
  {"n": 5, "title": "Prompt caching: conceito, anatomia e regras",
   "topics": ["O problema: pagar repetidamente pelo mesmo texto estático", "A solução: cache_control (crachá temporário, TTL de 5 min)", "Regra 1: tamanho mínimo do prefixo cacheado", "Regra 2: máximo de 4 breakpoints por requisição", "Regra 3: renovação gratuita do TTL a cada cache hit"],
   "figures": ["slide07", "slide08"],
   "material": "<p>O problema que o <strong>prompt caching</strong> resolve: enviar um manual extenso (instruções, tools, contexto longo) em toda requisição consome tokens e tempo à toa, já que você paga repetidamente pelo mesmo texto estático. A solução é marcar blocos de conteúdo com <code>cache_control: {\"type\": \"ephemeral\"}</code> — o modelo processa esse texto estático uma vez e emite um \"crachá temporário\" com TTL padrão de 5 minutos; requisições subsequentes que reaproveitam esse prefixo pagam apenas uma fração do custo de processamento. Três regras da anatomia do cache: <strong>(1) tamanho mínimo</strong> — o prefixo cacheado precisa atingir um mínimo de tokens (por exemplo, 1024+); abaixo disso, o processamento ocorre normalmente, mas sem desconto; <strong>(2) breakpoints</strong> — no máximo 4 marcações de <code>cache_control</code> por requisição; <strong>(3) renovação do TTL</strong> — cada leitura bem-sucedida do cache (\"cache hit\") reseta gratuitamente o TTL de 5 minutos, mantendo o cache \"quente\" com uso constante.</p>"},
  {"n": 6, "title": "A regra de ouro do cache: hierarquia e invalidação",
   "topics": ["Hierarquia: Tools → System → Messages", "Uma alteração em uma camada invalida o cache dessa camada e das inferiores", "Prática ideal: alterar só a ponta final (pergunta do usuário)"],
   "figures": ["slide09"],
   "material": "<p>O cache segue uma <strong>hierarquia de destruição</strong> em 3 camadas, de cima para baixo: <strong>(1) Tools (ferramentas)</strong>, <strong>(2) System (instruções)</strong>, <strong>(3) Messages (histórico)</strong>. A regra de ouro: uma alteração em qualquer camada <strong>queima e invalida</strong> o cache dessa camada e de <strong>todas as camadas abaixo dela</strong>. Mudar as tools invalida tudo. Mudar o system prompt preserva o cache das tools, mas destrói o cache das messages abaixo. A prática ideal de arquitetura é alterar apenas a ponta final — a pergunta do usuário — preservando o processamento pesado de tools e system prompt acima, que raramente mudam entre requisições.</p>"},
  {"n": 7, "title": "Orquestração: agentes vs. fluxos de trabalho",
   "topics": ["O problema: tarefas que um único prompt não resolve", "Fluxos de trabalho (workflows): a rota predeterminada", "Agentes: a rota autônoma"],
   "figures": ["slide10"],
   "material": "<p>Quando um problema é complexo demais para um único prompt resolver, existem dois caminhos de orquestração. <strong>Fluxos de trabalho (workflows)</strong> são a <em>rota predeterminada</em>: uma sequência fixa de chamadas em que o arquiteto dita exatamente a ordem e o fluxo dos passos — previsível e testável. <strong>Agentes</strong> são a <em>rota autônoma</em>: o modelo recebe um objetivo e um conjunto de ferramentas, e descobre por conta própria como navegar até a solução, decidindo iterativamente os próprios passos. A escolha entre workflows e agentes é o núcleo do domínio de Arquitetura Agêntica na prova — não é uma escolha de \"qual é melhor\", é uma escolha de \"qual o problema exige\".</p>"},
  {"n": 8, "title": "Padrões de fluxos de trabalho: chaining, parallelization, routing",
   "topics": ["Encadeamento (chaining): rascunho e revisão", "Paralelização (parallel): chamadas simultâneas", "Roteamento (routing): classifica e distribui"],
   "figures": ["slide11"],
   "material": "<p>Três padrões cobrem a maioria dos fluxos de trabalho: <strong>Encadeamento (chaining)</strong> — o padrão \"rascunho e revisão\", mantém o modelo focado em resolver e refinar uma tarefa por vez, em sequência (A → B → C); <strong>Paralelização (parallel)</strong> — executa chamadas simultâneas, útil para avaliar múltiplos critérios independentes ao mesmo tempo antes de sintetizar os resultados; <strong>Roteamento (routing)</strong> — atua como um PABX: classifica a requisição inicial e a envia para apenas um pipeline especializado e otimizado, em vez de um único prompt genérico tentar cobrir todos os casos.</p>"},
  {"n": 9, "title": "Agentes: o ciclo autônomo (observar, pensar, agir)",
   "topics": ["O ciclo Observar → Pensar → Agir", "Objetivo definido, não passos definidos", "O poder oculto: ferramentas genéricas"],
   "figures": ["slide12"],
   "material": "<p>Diferente de um fluxo fixo, um <strong>agente</strong> opera em um ciclo contínuo: <strong>Observar</strong> (analisar o ambiente/resultado mais recente) → <strong>Pensar</strong> (planejar a próxima ação) → <strong>Agir</strong> (chamar uma ferramenta) → observar de novo, e assim por diante, até concluir o objetivo. O agente decide qual ferramenta usar, executa a ação, avalia o resultado retornado e decide iterativamente se precisa de mais dados ou se já pode compor a resposta final. O \"poder oculto\" desse desenho é equipar o agente com ferramentas <strong>genéricas</strong> (buscar dados, ler arquivos) — isso permite que ele resolva problemas inéditos e imprevistos no design inicial, algo que um workflow fixo não consegue fazer.</p>"},
  {"n": 10, "title": "Matriz de diagnóstico e a regra de produção",
   "topics": ["Previsibilidade, escalabilidade, flexibilidade: workflows x agentes", "A regra de ouro da Anthropic para produção", "Quando escalar de workflow para agente"],
   "figures": ["slide13", "slide14"],
   "material": "<p>Comparando os dois caminhos em quatro eixos: <strong>previsibilidade</strong> (altíssima em workflows, moderada em agentes, por causa de rotas variáveis por inferência), <strong>escalabilidade e testes</strong> (fácil em workflows — etapas isoladas e reproduzíveis — difícil em agentes, por caminhos imprevisíveis), <strong>flexibilidade e UX</strong> (rígida em workflows, máxima em agentes) e <strong>carga de design prévio</strong> (workflows exigem planejamento estrutural minucioso; agentes exigem design focado nas ferramentas disponíveis). A <strong>regra de ouro da Anthropic</strong> para produção: <em>sempre priorize fluxos de trabalho para soluções de produção; escale a complexidade para agentes autônomos apenas quando a variedade de tarefas e a necessidade de flexibilidade tornarem os passos rígidos inviáveis</em>. Na prova, a resposta certa quase sempre segue essa regra — comece simples (workflow), suba para agente só quando necessário.</p>"},
  {"n": "RR", "title": "Revisão geral — checklist de síntese do módulo",
   "topics": ["Modelos: Haiku/Sonnet/Opus", "Requisição: rota segura, max_tokens, stop_reason", "Cache: TTL, limites, hierarquia de destruição", "Orquestração: workflows x agentes"],
   "figures": ["slide15"],
   "material": "<p>Fechando o módulo, um checklist de síntese em quatro blocos: <strong>(1) Modelos</strong> — Haiku (rápido, barato, alto volume), Sonnet (o equilíbrio ouro para RAG/chat), Opus (especialista, raciocínio profundo); <strong>(2) Requisição</strong> — rota segura app → servidor proxy → API, <code>max_tokens</code> como teto (não tamanho fixo), <code>stop_reason</code> como motivo vital da parada; <strong>(3) Cache</strong> — TTL de 5 minutos (resetável a cada hit), limites (mínimo de tokens, máximo de 4 breakpoints), hierarquia de destruição Tools → System → Messages; <strong>(4) Orquestração</strong> — fluxos de trabalho (sequenciais, paralelos, roteados; confiáveis e fixos) e agentes (autônomos, iterativos, flexíveis; use só quando necessário). Esses quatro blocos, junto com a regra de ouro \"priorize workflows, escale para agentes só quando preciso\", resumem o domínio de maior peso da prova.</p>"},
]

m5["glossary"] = [
    {"t": "cache_control", "d": "Parâmetro que marca um bloco de conteúdo para ser cacheado (ex.: {\"type\": \"ephemeral\"}), evitando reprocessamento pago do mesmo texto estático."},
    {"t": "ephemeral (cache)", "d": "Tipo de cache com tempo de vida curto (TTL padrão de 5 minutos), renovado gratuitamente a cada acerto de cache (\"cache hit\")."},
    {"t": "TTL (time-to-live)", "d": "Tempo que um bloco cacheado permanece válido antes de expirar — 5 minutos por padrão no prompt caching da Anthropic."},
    {"t": "breakpoint de cache", "d": "Cada marcação de cache_control em uma requisição; o limite é de no máximo 4 breakpoints por chamada."},
    {"t": "hierarquia de destruição do cache", "d": "Ordem Tools → System → Messages: alterar uma camada invalida o cache dela e de todas as camadas abaixo."},
    {"t": "cache hit", "d": "Quando uma requisição reaproveita com sucesso um prefixo já cacheado, pagando apenas uma fração do custo de processamento."},
    {"t": "ciclo agente (Observar-Pensar-Agir)", "d": "O loop contínuo com que um agente autônomo opera: observa o ambiente, planeja a próxima ação, age chamando uma ferramenta, e repete até concluir o objetivo."},
    {"t": "regra de ouro da Anthropic (produção)", "d": "Priorizar fluxos de trabalho para produção; só escalar para agentes autônomos quando a variedade de tarefas tornar os passos fixos inviáveis."},
    {"t": "matriz de decisão de modelos", "d": "Framework que compara Haiku, Sonnet e Opus em velocidade, inteligência e caso de uso ideal para escolher o modelo certo por tarefa."},
]

m5["keywords"] = [
    "Opus", "Sonnet", "Haiku", "cache_control", "ephemeral", "TTL", "breakpoint",
    "hierarquia de destruição de cache", "cache hit", "max_tokens (teto)", "stop_reason (sinal vital)",
    "rota segura (app → servidor → API)", "chaining", "parallelization", "routing",
    "ciclo Observar-Pensar-Agir", "regra de ouro (workflows antes de agentes)", "matriz de diagnóstico",
]

m5["attention"] = [
    {"pt": "A escolha de modelo é sobre <strong>rotear cada tarefa</strong> para o nível certo (Haiku/Sonnet/Opus) — usar Opus para tudo não é \"mais seguro\", é desperdício de custo e latência."},
    {"pt": "<strong>max_tokens não é o tamanho da resposta</strong> — é um teto de segurança. A geração pode (e costuma) terminar naturalmente bem antes de atingir esse limite."},
    {"pt": "A API Key <strong>nunca</strong> deve estar acessível no cliente/app/front-end — ela vive apenas no servidor backend, que atua como intermediário seguro com a API Anthropic."},
    {"pt": "<code>stop_reason</code> distingue uma resposta que terminou naturalmente (<code>end_turn</code>) de uma que foi cortada por bater no teto de <code>max_tokens</code> — cenário clássico de prova."},
    {"pt": "Prompt caching tem <strong>3 regras numéricas</strong> que a prova cobra: tamanho mínimo do prefixo, máximo de 4 breakpoints por requisição, e TTL de 5 minutos renovável a cada cache hit."},
    {"pt": "A <strong>hierarquia de destruição do cache</strong> é Tools → System → Messages: mudar uma camada superior invalida o cache de tudo que está abaixo dela — nunca o contrário."},
    {"pt": "Workflows vs. Agentes não é uma escolha de qualidade, é uma escolha de <strong>encaixe com o problema</strong>: previsibilidade e teste fácil (workflow) vs. flexibilidade máxima para problemas inéditos (agente)."},
    {"pt": "A <strong>regra de ouro da Anthropic</strong> para cenários de prova: comece com fluxo de trabalho; só suba a complexidade para um agente autônomo quando a variedade de tarefas tornar passos fixos inviáveis."},
]

with open("/home/claude/module5_pt.json", "w", encoding="utf-8") as f:
    json.dump(m5, f, ensure_ascii=False, indent=1)
print("MODULE 5 -> lessons:", len(m5["lessons"]), "glossary:", len(m5["glossary"]), "keywords:", len(m5["keywords"]), "attention:", len(m5["attention"]))
