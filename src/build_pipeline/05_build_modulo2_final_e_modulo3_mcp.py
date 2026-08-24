# -*- coding: utf-8 -*-
import json

with open("/home/claude/module2_lessons.json", "r", encoding="utf-8") as f:
    m2 = json.load(f)
with open("/home/claude/quiz2_full.json", "r", encoding="utf-8") as f:
    m2["quiz"] = json.load(f)

m2["keywords"] = [
    "Claude Opus","Claude Sonnet","Claude Haiku","max_tokens","stop_reason","tokenization","embedding",
    "contextualization","generation","system prompt","temperature","stream=True","ContentBlockDelta",
    "prefilling","stop_sequences","eval dataset","grader (code/model/human)","statistics.mean",
    "clear & direct","output guidelines","process steps","tags XML","one-shot / multi-shot",
    "tool_use block","tool_result block","tool_use_id","JSON Schema","input_schema","ToolParam",
    "RAG","chunking (size/structure/semantic/sentence)","embeddings (VoyageAI)","vector database",
    "cosine similarity","cosine distance","BM25","reciprocal rank fusion (RRF)","extended thinking",
    "thinking_budget","signature","redacted_thinking","image block","base64","workflows vs. agents",
    "parallelization","chaining","routing",
]
m2["attention"] = [
    "Os 4 campos essenciais de uma requisição são <strong>API Key, Model, Messages, Max Tokens</strong> — Stop Reason é da resposta, não da requisição.",
    "Ordem dos 4 estágios internos: <strong>Tokenization → Embedding → Contextualization → Generation</strong>.",
    "A API é <strong>stateless</strong>: não existe memória entre requisições — o app precisa reenviar o histórico completo a cada turno.",
    "<code>system=None</code> não é aceito pela API — o parâmetro deve ser adicionado condicionalmente.",
    "Temperature age só na etapa de <strong>Sampling</strong>, nunca na Prediction — não muda o que o modelo prediz, só como escolhe.",
    "Faixas de temperature: <strong>0.0–0.3</strong> factual/código, <strong>0.4–0.7</strong> equilíbrio, <strong>0.8–1.0</strong> criativo.",
    "Em streaming, só o evento <strong>ContentBlockDelta</strong> carrega texto — os outros cinco são estrutura/controle.",
    "Prefilling + stop sequence é a técnica-chave para saída limpa (JSON, código, listas) sem comentário do Claude.",
    "No fluxo de avaliação, pedir <strong>strengths/weaknesses/reasoning antes do score</strong> evita que o grader converja para uma nota mediana (~6).",
    "Ganho real medido no curso: claro+direto levou de 2,32→3,92; adicionar guidelines levou de 3,92→7,86.",
    "Tool use: quem executa o código é sempre o <strong>seu servidor</strong>, nunca o Claude diretamente.",
    "O <code>tool_use_id</code> do resultado deve bater exatamente com o <code>id</code> do bloco ToolUse original — crítico com múltiplas tool calls.",
    "RAG troca simplicidade inicial por escala e eficiência — vale a pena com documentos grandes/múltiplos.",
    "Cosine similarity vai de -1 a 1 (1 = idêntico, 0 = sem relação, -1 = oposto); cosine distance = 1 − similaridade.",
    "BM25 (lexical) resolve o que a busca semântica sozinha erra: termos exatos raros, como IDs de incidente.",
    "Extended thinking deve ser ativado só depois de avaliação mostrar que o prompt já otimizado ainda não é preciso o bastante — não é padrão para toda chamada.",
    "Limites de imagem: até 100 imagens por requisição, 5MB cada, 8000px (uma imagem) ou 2000px (múltiplas); custo = (largura×altura)/750 tokens.",
    "Workflows (parallelization, chaining, routing) são previsíveis e de custo controlado; agentes decidem os próprios passos — a escolha entre os dois é o núcleo do domínio de Arquitetura Agêntica na prova.",
]

with open("/home/claude/module2_final.json", "w", encoding="utf-8") as f:
    json.dump(m2, f, ensure_ascii=False, indent=1)
print("MODULE 2 -> lessons:", len(m2["lessons"]), "quiz:", len(m2["quiz"]), "keywords:", len(m2["keywords"]))

# ======================================================================
# MODULE 3 — Introdução ao Model Context Protocol
# ======================================================================
m3 = {
    "id": "mod-mcp",
    "badge": "Módulo 3",
    "title": "Introdução ao Model Context Protocol",
    "subtitle": "Introduction to Model Context Protocol",
    "desc": "Construir servidores e clientes MCP do zero em Python — os três primitivos do protocolo (tools, resources, prompts) e como Claude se conecta a serviços externos de forma padronizada.",
    "lessons": [],
    "glossary": [],
    "keywords": [
        "MCP (Model Context Protocol)", "servidor MCP", "cliente MCP", "tools (MCP)", "resources (MCP)",
        "prompts (MCP)", "MCP Inspector", "transporte agnóstico", "stdio", "JSON-RPC", "capabilities negotiation",
        "MIME type", "decorators (Python SDK)", "autocomplete de recursos", "injeção de contexto",
    ],
    "attention": [
        "MCP tem <strong>três primitivos centrais</strong>: <em>tools</em> (ações que o modelo pode invocar), <em>resources</em> (dados que podem ser lidos/referenciados) e <em>prompts</em> (templates reutilizáveis de interação) — memorize os três, é a base de qualquer questão sobre MCP na prova.",
        "MCP é <strong>agnóstico de transporte</strong>: o mesmo protocolo funciona sobre stdio (processo local) ou por rede — o que importa é a troca de mensagens estruturadas, não o meio de transporte.",
        "Um <strong>servidor MCP</strong> expõe tools/resources/prompts; um <strong>cliente MCP</strong> consome esses recursos e os apresenta ao modelo — a relação é sempre cliente→servidor, nunca o contrário.",
        "O <strong>MCP Inspector</strong> é a ferramenta oficial para testar e depurar um servidor MCP durante o desenvolvimento, sem precisar de um cliente completo.",
        "Diferente de uma Skill (que soma conhecimento/instruções à conversa), um servidor MCP fornece <strong>ferramentas e integrações executáveis</strong> com sistemas externos — categorias diferentes, não concorrentes.",
        "Prova de arquiteto: pense em MCP como a camada de <strong>integração padronizada</strong> entre o modelo e o mundo externo — a pergunta típica de cenário é \"qual a forma correta de expor esta capacidade ao Claude: uma Skill, uma tool custom, ou um servidor MCP?\"",
    ],
}
m3["lessons"] = [
  {"n": 1, "title": "Introdução ao MCP",
   "topics": ["O que é o Model Context Protocol", "Por que um protocolo padronizado (em vez de integrações ad-hoc)", "Visão geral do curso"],
   "material": "<p>O <strong>Model Context Protocol (MCP)</strong> é um protocolo aberto que padroniza como aplicações fornecem contexto e capacidades para modelos de linguagem — em vez de cada integração externa (banco de dados, API, sistema de arquivos) exigir seu próprio código proprietário de conexão, um servidor MCP expõe suas capacidades de um jeito que qualquer cliente MCP compatível (incluindo o Claude Desktop, Claude Code ou uma aplicação própria) sabe consumir. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 2, "title": "Clientes MCP",
   "topics": ["O papel do cliente na arquitetura", "Descoberta de capacidades do servidor", "Como o cliente apresenta tools/resources/prompts ao modelo"],
   "material": "<p>Um <strong>cliente MCP</strong> é a ponta que se conecta a um ou mais servidores, descobre quais tools, resources e prompts eles oferecem (uma etapa de <em>capabilities negotiation</em>) e apresenta essas capacidades ao modelo durante a conversa. O Claude Desktop e o Claude Code já atuam como clientes MCP nativos — é por isso que você consegue \"plugar\" um servidor MCP e ele passa a estar disponível nas suas conversas. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 3, "title": "Configuração do projeto (hands-on)",
   "topics": ["Estrutura inicial de um servidor MCP em Python", "SDK oficial de Python para MCP", "Preparando o ambiente de desenvolvimento"],
   "material": "<p>A parte prática do curso usa o <strong>SDK oficial de Python</strong> para MCP, que oferece decorators para registrar funções como tools, resources e prompts sem lidar manualmente com o protocolo de mensagens subjacente. A configuração inicial do projeto segue o mesmo padrão de outros SDKs Python do ecossistema Claude: ambiente virtual, instalação do pacote MCP, e um arquivo de entrada que instancia o servidor. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 4, "title": "Definindo tools com MCP",
   "topics": ["Registrar uma função como tool via decorator", "Schema de entrada gerado automaticamente", "Boas práticas (mesmas de tool use na API: nomes claros, validação, erros úteis)"],
   "material": "<p>Assim como no tool use da API Claude (Módulo 2, Seção 5), uma tool MCP é uma função com um nome, descrição e schema de parâmetros — a diferença é que, no MCP, o servidor expõe essa tool para <strong>qualquer cliente compatível</strong>, não só para uma integração específica. O SDK Python costuma usar decorators para marcar uma função Python comum como tool, inferindo boa parte do schema a partir das anotações de tipo. As mesmas boas práticas de tool use se aplicam: nomes descritivos, validação de entrada e mensagens de erro que o modelo consiga interpretar. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 5, "title": "O inspetor de servidores (MCP Inspector)",
   "topics": ["Testar tools/resources/prompts sem um cliente completo", "Ciclo de desenvolvimento: editar → inspecionar → ajustar", "Pesquisa de satisfação do curso (checkpoint)"],
   "material": "<p>O <strong>MCP Inspector</strong> é uma interface (geralmente web) que se conecta ao seu servidor MCP em desenvolvimento e permite listar e testar manualmente tools, resources e prompts, sem precisar de um cliente completo como o Claude Desktop. É a ferramenta de diagnóstico equivalente ao <code>claude --debug</code> do universo de Skills — o primeiro lugar para verificar se o servidor está expondo o que você espera. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 6, "title": "Implementando um cliente",
   "topics": ["Exercício prático: escrever um cliente MCP simples", "Conectar ao servidor construído nas lições anteriores", "Listar capacidades e invocar uma tool"],
   "material": "<p>Depois de construir o servidor, o curso inverte a perspectiva: implementar um <strong>cliente MCP</strong> simples que se conecta a esse mesmo servidor, lista suas capacidades (tools, resources, prompts disponíveis) e invoca uma tool programaticamente — fechando o ciclo cliente↔servidor de ponta a ponta. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 7, "title": "Definindo e acessando resources",
   "topics": ["O que são resources (dados endereçáveis, não ações)", "Diferença entre resource e tool", "Como um cliente lista e lê um resource", "MIME types"],
   "material": "<p><strong>Resources</strong> são o segundo primitivo do MCP: representam dados que podem ser lidos ou referenciados (um arquivo, um registro de banco, o conteúdo de uma página) — diferente de uma <em>tool</em>, que representa uma ação/efeito. Cada resource tem um identificador (geralmente uma URI) e um <strong>MIME type</strong> que diz ao cliente como interpretar o conteúdo retornado. Um cliente primeiro lista os resources disponíveis no servidor, depois lê o conteúdo de um resource específico quando necessário para a conversa. <span class='badge synth'>complementar</span></p>",
  },
  {"n": 8, "title": "Definindo prompts e usando-os no cliente",
   "topics": ["Prompts MCP como templates reutilizáveis", "Diferença entre prompt MCP e system prompt da API", "Como o cliente expõe prompts ao usuário/modelo", "Revisão final do módulo"],
   "material": "<p><strong>Prompts</strong> são o terceiro primitivo: templates de interação reutilizáveis que o servidor expõe (por exemplo, um prompt \"revisar-pull-request\" que já vem com a estrutura certa de instrução). Diferem do <em>system prompt</em> da API Claude — aqui, é o <strong>servidor MCP</strong> quem define e oferece o prompt, e o cliente decide quando apresentá-lo ao usuário ou injetá-lo na conversa. A lição final do curso revisa os três primitivos (tools, resources, prompts) e como eles se combinam para dar a um servidor MCP uma superfície completa de integração. <span class='badge synth'>complementar</span></p>",
  },
  {"n": "Geral", "title": "Revisão geral — MCP vs. Skills e outros recursos do Claude",
   "topics": ["MCP vs. Agent Skills: quando usar cada um", "Transporte agnóstico — revisão do conceito", "Como situar o MCP no panorama geral da certificação"],
   "material": "<p>Fechando o Módulo 3, esta revisão cruza o MCP com o restante da trilha: uma <strong>Skill</strong> soma conhecimento e instruções ao raciocínio do Claude (Módulo 1), enquanto um <strong>servidor MCP</strong> fornece ferramentas e integrações executáveis com sistemas externos — são categorias complementares, não concorrentes, e a prova gosta de testar exatamente essa distinção em formato de cenário (\"qual a forma correta de expor esta capacidade ao Claude?\"). Vale também reforçar o conceito de <strong>transporte agnóstico</strong>: o protocolo MCP troca mensagens estruturadas da mesma forma independentemente do meio de transporte (stdio local ou rede), então a pergunta certa nunca é \"por qual cabo isso passa\", e sim \"que mensagens estão sendo trocadas\". <span class='badge synth'>complementar</span></p>",
  },
]

quiz3 = []
def add3(lesson, q, options, correct, note, source="synth"):
    quiz3.append({"lesson": lesson, "q": q, "options": options, "correct": correct, "note": note, "source": source})

add3(1, "What are the three core primitives of the Model Context Protocol?",
    ["Servers, clients, and transports","Tools, resources, and prompts","Requests, responses, and errors","Models, agents, and workflows","Skills, hooks, and subagents"], 1,
    "Tools, resources e prompts são os três primitivos centrais do MCP.")
add3(1, "Why does MCP exist as a standardized protocol instead of ad-hoc integrations?",
    ["To make every integration require custom, one-off code","So any compatible client can consume any compatible server's capabilities the same way","To replace the Claude API entirely","To eliminate the need for API keys","To force every server to use Python"], 1,
    "Padroniza a forma como clientes consomem capacidades de servidores.")
add3(2, "What is the relationship direction between an MCP client and an MCP server?",
    ["The server consumes the client's capabilities","The client consumes the capabilities exposed by the server","They are interchangeable and symmetrical","The client trains the server","There is no defined relationship"], 1,
    "O cliente consome o que o servidor expõe.")
add3(2, "What does \"capabilities negotiation\" refer to in MCP?",
    ["Negotiating the price of API usage","The client discovering which tools, resources, and prompts a server offers","A human negotiating a contract with Anthropic","Choosing which Claude model to use","Setting the temperature parameter"], 1,
    "É a descoberta, pelo cliente, do que o servidor oferece.")
add3(3, "Which official SDK does the hands-on portion of the MCP course use to build a server?",
    ["The Anthropic Python SDK for the Messages API","An official Python SDK for MCP, with decorators for tools/resources/prompts","A JavaScript-only SDK","No SDK — raw JSON-RPC only","The VoyageAI SDK"], 1,
    "O SDK oficial de Python para MCP, com decorators.")
add3(4, "How is a Python function typically turned into an MCP tool in the official SDK?",
    ["By renaming the file to tool.py","By using a decorator that registers the function and infers its schema","By manually writing raw JSON-RPC messages","By adding it to CLAUDE.md","By calling client.messages.create() with the function as a string"], 1,
    "Um decorator registra a função e infere o schema.")
add3(4, "Which best practice from Claude API tool use also applies to defining MCP tools?",
    ["Avoid input validation to keep things simple","Use descriptive names and validate inputs with useful error messages","Never provide a description","Always use temperature 1.0","Only use tools with no parameters"], 1,
    "As mesmas boas práticas de tool use da API valem para tools MCP.")
add3(5, "What is the MCP Inspector primarily used for?",
    ["Deploying a server to production","Manually testing and debugging a server's tools, resources, and prompts during development","Training a new embedding model","Replacing the need for a client entirely in production","Encrypting server traffic"], 1,
    "É a ferramenta de teste/diagnóstico durante o desenvolvimento.")
add3(6, "In the client-implementation exercise, what does the simple client do after connecting to the server?",
    ["It immediately shuts the server down","It lists the server's capabilities and invokes a tool programmatically","It only displays the server's IP address","It converts the server into a Skill","It deletes all defined resources"], 1,
    "Lista capacidades e invoca uma tool, fechando o ciclo cliente-servidor.")
add3(7, "How does an MCP resource differ from an MCP tool?",
    ["A resource represents an action; a tool represents readable/referenceable data","A tool represents an action Claude can invoke; a resource represents data that can be read or referenced","They are exactly the same thing with different names","Resources can only be used by servers, never clients","Tools are always free; resources always cost tokens"], 1,
    "Tool = ação; resource = dado referenciável/legível.")
add3(7, "What does a resource's MIME type tell the client?",
    ["The price of accessing that resource","How to interpret the content that gets returned","Which Claude model must be used","The resource's priority versus other resources","Nothing — MIME type is not part of MCP"], 1,
    "Diz como interpretar o conteúdo retornado.")
add3(8, "Who defines and offers an MCP \"prompt\" primitive — the client or the server?",
    ["The end user, manually, every time","The MCP client, hard-coded into its own source","The MCP server, which exposes it as a reusable interaction template","Anthropic, centrally, for all servers","There is no such primitive in MCP"], 2,
    "O servidor define e expõe o prompt como template reutilizável.")
add3(8, "How does an MCP \"prompt\" differ from the Claude API's \"system prompt\"?",
    ["They are identical concepts under different names","An MCP prompt is a reusable template exposed by a server; a system prompt is passed directly in an API call to shape Claude's behavior","System prompts are defined by MCP servers","MCP prompts can only be used with Claude Haiku","System prompts require a vector database"], 1,
    "MCP prompt = template do servidor; system prompt = parâmetro da chamada de API.")
add3("Geral", "Which statement correctly distinguishes an Agent Skill from an MCP server?",
    ["A Skill provides external tool integrations; an MCP server adds reasoning knowledge","A Skill adds knowledge/instructions to Claude's reasoning; an MCP server provides external tools and integrations","They are the same mechanism accessed through different commands","MCP servers only work inside Claude Code, never in Claude Desktop","Skills always require an MCP server to function"], 1,
    "Skill = conhecimento; MCP = ferramentas/integrações externas — categorias diferentes.")
add3("Geral", "MCP is described as \"transport-agnostic.\" What does that mean?",
    ["It only works over the public internet","The protocol's message exchange works over different transports (e.g. local stdio or network) without changing its structure","It requires no transport layer at all","It only works with Bluetooth","Transport must always be HTTP/2"], 1,
    "O mesmo protocolo funciona sobre transportes diferentes (ex.: stdio, rede).")

m3["quiz"] = quiz3
with open("/home/claude/module3_final.json", "w", encoding="utf-8") as f:
    json.dump(m3, f, ensure_ascii=False, indent=1)
print("MODULE 3 -> lessons:", len(m3["lessons"]), "quiz:", len(m3["quiz"]))
