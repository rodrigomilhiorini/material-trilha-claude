# -*- coding: utf-8 -*-
import json

with open("/home/claude/module1.json", "r", encoding="utf-8") as f:
    m1 = json.load(f)
with open("/home/claude/module2_final.json", "r", encoding="utf-8") as f:
    m2 = json.load(f)
with open("/home/claude/module3_final.json", "r", encoding="utf-8") as f:
    m3 = json.load(f)
with open("/home/claude/module4_final.json", "r", encoding="utf-8") as f:
    m4 = json.load(f)

m1["glossary"] = [
    {"t": "SKILL.md", "d": "Arquivo central de uma Skill: frontmatter (name, description e opcionais) + instruções."},
    {"t": "frontmatter", "d": "Bloco de metadados no topo do SKILL.md, delimitado por ---."},
    {"t": "name", "d": "Campo obrigatório: minúsculas/números/hífens, até 64 caracteres, deve bater com o nome da pasta."},
    {"t": "description", "d": "Campo obrigatório e mais importante: até 1.024 caracteres, é o que o Claude usa para o matching."},
    {"t": "allowed-tools", "d": "Campo opcional que restringe quais ferramentas o Claude pode usar enquanto a Skill está ativa."},
    {"t": "progressive disclosure", "d": "Prática de manter o SKILL.md enxuto e mover detalhe para scripts/, references/ e assets/, carregados só quando necessário."},
    {"t": "semantic matching", "d": "Comparação por significado/intenção (não palavra exata) entre o pedido do usuário e a description da Skill."},
    {"t": "~/.claude/skills", "d": "Local das Skills pessoais, válidas em todos os projetos do usuário."},
    {"t": ".claude/skills", "d": "Local das Skills de projeto, versionadas e compartilhadas via repositório."},
    {"t": "enterprise managed settings", "d": "Configuração administrada pela organização; Skills daqui têm a prioridade mais alta."},
    {"t": "strictKnownMarketplaces", "d": "Configuração enterprise que restringe de onde plugins podem ser instalados."},
    {"t": "subagent", "d": "Execução em contexto isolado; não herda Skills automaticamente, só as listadas em seu frontmatter."},
    {"t": "hook", "d": "Automação disparada por evento (ex.: salvar arquivo), não por pedido do usuário."},
]

m2["glossary"] = [
    {"t": "max_tokens", "d": "Limite de segurança para o tamanho da resposta — não é uma meta a ser atingida."},
    {"t": "stop_reason", "d": "Campo da resposta que explica por que a geração parou (max_tokens, fim natural, stop sequence)."},
    {"t": "system prompt", "d": "String passada no parâmetro system, separada de messages, que molda tom/comportamento."},
    {"t": "temperature", "d": "Decimal 0–1 que controla a aleatoriedade na etapa de Sampling da geração."},
    {"t": "prefilling", "d": "Adicionar você mesmo uma mensagem assistant parcial para guiar a continuação do Claude."},
    {"t": "stop_sequences", "d": "Strings que, ao aparecerem, encerram a geração imediatamente."},
    {"t": "eval dataset", "d": "Conjunto de casos de teste usados para medir objetivamente a qualidade de um prompt."},
    {"t": "grader", "d": "Mecanismo (código, modelo ou humano) que atribui uma nota de 1 a 10 a uma resposta."},
    {"t": "tool_use block", "d": "Bloco na resposta do Claude pedindo a execução de uma função externa, com id, name e input."},
    {"t": "tool_result block", "d": "Bloco enviado de volta (em mensagem user) com o resultado da execução, referenciando tool_use_id."},
    {"t": "JSON Schema", "d": "Especificação de validação de dados usada para descrever os parâmetros de uma tool (input_schema)."},
    {"t": "RAG", "d": "Retrieval Augmented Generation: buscar e incluir só os trechos relevantes de documentos grandes."},
    {"t": "chunking", "d": "Dividir um documento em pedaços menores antes da busca — por tamanho, estrutura, sentença ou semântica."},
    {"t": "embedding", "d": "Vetor numérico que representa o significado de um texto, usado para busca semântica."},
    {"t": "cosine similarity", "d": "Medida de -1 a 1 do quão parecidos dois embeddings são (1 = idêntico, 0 = sem relação)."},
    {"t": "BM25", "d": "Algoritmo de busca lexical que pesa termos raros mais que termos comuns."},
    {"t": "reciprocal rank fusion (RRF)", "d": "Técnica para combinar rankings de métodos de busca diferentes de forma justa."},
    {"t": "extended thinking", "d": "Recurso que dá ao Claude um bloco de raciocínio (thinking block) antes da resposta final."},
    {"t": "signature", "d": "Token criptográfico que garante que o texto de um thinking block não foi alterado."},
    {"t": "workflow (agêntico)", "d": "Caminho previsível e pré-definido (parallelization, chaining, routing), em contraste com um agente que decide os próprios passos."},
]

m3["glossary"] = [
    {"t": "MCP (Model Context Protocol)", "d": "Protocolo aberto que padroniza como aplicações fornecem contexto/capacidades a modelos de linguagem."},
    {"t": "servidor MCP", "d": "Processo que expõe tools, resources e/ou prompts para clientes compatíveis."},
    {"t": "cliente MCP", "d": "Aplicação (ex.: Claude Desktop, Claude Code) que descobre e consome as capacidades de um servidor MCP."},
    {"t": "tools (MCP)", "d": "Ações que o modelo pode invocar através do servidor — o mesmo conceito de tool use da API, padronizado."},
    {"t": "resources (MCP)", "d": "Dados endereçáveis (por URI) que podem ser lidos/referenciados, com um MIME type associado."},
    {"t": "prompts (MCP)", "d": "Templates de interação reutilizáveis, definidos pelo servidor e oferecidos ao cliente."},
    {"t": "MCP Inspector", "d": "Ferramenta oficial para testar/depurar manualmente um servidor MCP durante o desenvolvimento."},
    {"t": "capabilities negotiation", "d": "Etapa em que o cliente descobre quais tools/resources/prompts um servidor oferece."},
    {"t": "transporte agnóstico", "d": "O protocolo funciona sobre diferentes meios de transporte (ex.: stdio local, rede) sem mudar sua estrutura."},
]

m4["glossary"] = [
    {"t": "plan mode", "d": "Modo em que Claude Code só planeja, sem editar arquivos, até você aprovar."},
    {"t": "menu de retrocesso (rewind)", "d": "Mecanismo para voltar a um checkpoint anterior da sessão."},
    {"t": "CLAUDE.md", "d": "Arquivo de regras sempre carregadas na sessão daquele projeto (ou usuário)."},
    {"t": "permission modes", "d": "Espectro de autonomia: de pedir confirmação sempre até aceitar edições automaticamente."},
    {"t": "hooks", "d": "Automação disparada por eventos do ciclo de vida (ex.: antes/depois de uma tool ser usada)."},
    {"t": "verification skill", "d": "Skill que empacota um procedimento de verificação para ser aplicado de forma consistente."},
    {"t": "modo headless", "d": "Execução do Claude Code sem interface interativa (ex.: claude -p), para scripts e pipelines."},
    {"t": "rotina", "d": "Prompt agendado para rodar automaticamente em recorrência."},
    {"t": "verificação proporcional", "d": "Profundidade de verificação que casa com o risco da mudança, em vez de aceitar só a palavra do Claude."},
    {"t": "plugin", "d": "Pacote reutilizável de Skills, hooks e comandos, distribuível via marketplace."},
]

MODULES = [m1, m2, m3, m4]

stats = {
    "lessons": sum(len(m["lessons"]) for m in MODULES),
    "quiz": sum(len(m["quiz"]) for m in MODULES),
    "glossary": sum(len(m["glossary"]) for m in MODULES),
    "keywords": sum(len(m["keywords"]) for m in MODULES),
}
print("STATS:", stats)

DATA = {"modules": MODULES, "stats": stats}

with open("/home/claude/DATA_final.json", "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False)

size_kb = len(json.dumps(DATA, ensure_ascii=False)) / 1024
print(f"DATA size: {size_kb:.1f} KB")
