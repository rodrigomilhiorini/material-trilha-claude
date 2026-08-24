# -*- coding: utf-8 -*-
import json

m2 = {
    "id": "mod-api",
    "badge": "Módulo 2",
    "title": "Construindo com a API Claude",
    "subtitle": "Building with the Claude API",
    "desc": "O curso mais extenso da trilha: 11 seções, da primeira requisição à API até avaliação de prompts, tool use, RAG, recursos avançados e padrões de agentes.",
    "lessons": [],
    "glossary": [],
    "keywords": [],
    "attention": [],
}

L = []  # lessons list

L.append({
    "n": "1", "title": "Visão geral dos modelos Claude (Opus / Sonnet / Haiku)",
    "topics": ["Claude Opus — inteligência máxima", "Claude Sonnet — equilíbrio", "Claude Haiku — custo/velocidade", "Espectro inteligência vs. custo/velocidade"],
    "material": "<p>A família Claude se organiza em torno de um trade-off entre <strong>inteligência</strong> de um lado e <strong>custo/velocidade</strong> do outro.</p><p><strong>Claude Opus</strong> — maior inteligência da família, custo alto, latência moderada, suporta reasoning. Ideal para arquitetura de software em larga escala, tarefas longas que exigem foco sustentado e planejamento estratégico multi-etapas.</p><p><strong>Claude Sonnet</strong> — equilíbrio entre qualidade, velocidade e custo (médio), latência rápida, suporta reasoning. Ideal para codificação comum, criação/edição de documentos, copywriting, análise de dados e automação de processos.</p><p><strong>Claude Haiku</strong> — mais eficiente em custo e latência, mas <strong>não suporta reasoning</strong>. Ideal para autocompletar código, moderação de conteúdo, extração/categorização de dados e tarefas de alto volume.</p><p>Regra prática: vá para Opus quando a tarefa exige raciocínio máximo e você aceita custo/latência maiores; vá para Haiku quando velocidade e volume importam mais que raciocínio profundo; Sonnet é o equilíbrio para o dia a dia.</p>",
})

L.append({
    "n": "2.1", "title": "O fluxo de requisição e como o Claude processa o texto",
    "topics": ["Fluxo de 5 passos (App→Servidor→API→Modelo→Resposta)", "Por que nunca chamar a API do client-side", "4 campos essenciais da requisição", "4 estágios internos: Tokenization, Embedding, Contextualization, Generation", "Condições de parada (max tokens, EOS, stop sequence)"],
    "material": "<p>Toda interação segue um fluxo previsível de 5 passos: <strong>Requisição ao servidor → Requisição à API Anthropic → Processamento pelo modelo → Resposta ao servidor → Resposta ao cliente</strong>. Seu app nunca chama a API diretamente — a chave secreta de API fica no seu servidor; chamar a API do lado do cliente expõe a chave, uma falha de segurança grave.</p><p>Os quatro campos essenciais de uma requisição: <strong>API Key, Model, Messages e Max Tokens</strong> (Stop Reason é parte da resposta, não da requisição).</p><p>Dentro da Anthropic, o texto passa por 4 estágios: <strong>Tokenization</strong> (quebra em tokens — a unidade que você paga), <strong>Embedding</strong> (cada token vira uma lista de números representando seus significados possíveis), <strong>Contextualization</strong> (o significado é ajustado pelas palavras vizinhas — é aqui que a ambiguidade se resolve) e <strong>Generation</strong> (calcula probabilidades para o próximo token e usa uma mistura de probabilidade + aleatoriedade controlada para escolher, token a token).</p><p>A geração para quando: atinge o <strong>max_tokens</strong>, gera um token de fim de sequência (EOS) natural, ou encontra uma <strong>stop sequence</strong> definida por você. A resposta final chega com: a mensagem (texto), o usage (tokens de entrada+saída) e o stop_reason (por que parou).</p>",
})

L.append({
    "n": "2.2", "title": "Fazendo sua primeira requisição",
    "topics": [".env e API key (nunca no código)", "client.messages.create(): model, max_tokens, messages", "Estrutura de uma message (role + content)", "Extraindo o texto: message.content[0].text"],
    "material": "<p>Antes de qualquer chamada: instale <code>anthropic</code> e <code>python-dotenv</code>, guarde a chave em um arquivo <code>.env</code> (nunca direto no código, sempre no .gitignore), e carregue com <code>load_dotenv()</code> — assim <code>Anthropic()</code> encontra a chave automaticamente.</p><p><code>client.messages.create()</code> exige exatamente três parâmetros: <strong>model</strong> (qual modelo usar), <strong>max_tokens</strong> (um limite de segurança, não uma meta — se a resposta natural do Claude for maior, a geração simplesmente para nesse limite) e <strong>messages</strong> (o histórico da conversa, como lista).</p><p>Cada mensagem é um dicionário com <strong>role</strong> (\"user\" ou \"assistant\") e <strong>content</strong> (o texto). O texto gerado é acessado em <code>message.content[0].text</code>.</p>",
})

L.append({
    "n": "2.3", "title": "Conversas multi-turno",
    "topics": ["A API é stateless (sem memória)", "Manter e reenviar a lista de mensagens completa", "Fluxo de 4 passos de uma conversa", "Funções helper: add_user_message, add_assistant_message, chat()"],
    "material": "<p>A API da Anthropic é <strong>stateless</strong>: Claude não guarda nada do histórico — cada requisição é totalmente independente. Para simular uma \"conversa\", o seu código precisa manter uma lista de mensagens crescente e reenviá-la <strong>completa</strong> a cada novo turno.</p><p>Fluxo que funciona: enviar a mensagem inicial do usuário → adicionar a resposta do Claude como mensagem assistant → adicionar a pergunta de acompanhamento como nova mensagem user → reenviar todo o histórico. É por isso que Claude parece \"lembrar\": ele está lendo a transcrição inteira de novo, não recordando algo.</p><p>Três funções helper simplificam isso: <code>add_user_message(messages, text)</code>, <code>add_assistant_message(messages, text)</code> — ambas só appendam um dict à lista — e <code>chat(messages)</code>, que chama <code>client.messages.create()</code> com o modelo e max_tokens padrão e retorna só o texto gerado.</p>",
})

L.append({
    "n": "2.4", "title": "System prompts",
    "topics": ["Papel do system prompt (como responder, não o quê)", "Passado como parâmetro system, fora de messages", "system=None não é aceito — adicionar condicionalmente", "Chat function flexível com **params"],
    "material": "<p>Um <strong>system prompt</strong> molda o tom, estilo e abordagem do Claude — é orientação sobre <em>como</em> responder, não sobre <em>o quê</em> responder (isso continua vindo da pergunta do usuário). É passado como uma string simples no parâmetro <strong>system</strong> do create(), separado da lista de messages.</p><p>Exemplo clássico: um tutor de matemática que dá dicas em vez de resolver direto — o mesmo pedido do aluno produz respostas completamente diferentes dependendo só do system prompt.</p><p>Detalhe importante de implementação: a API do Claude <strong>não aceita system=None</strong>. Uma função chat() reutilizável deve montar um dicionário de parâmetros e só adicionar a chave \"system\" condicionalmente (<code>if system: params[\"system\"] = system</code>), depois desempacotar com <code>**params</code> dentro de create().</p>",
})

L.append({
    "n": "2.5", "title": "Temperature",
    "topics": ["3 passos da geração: Tokenization, Prediction, Sampling", "Temperature atua só na Sampling", "Baixa = determinístico; alta = variado/criativo", "Faixas por tipo de tarefa (0.0–0.3 / 0.4–0.7 / 0.8–1.0)"],
    "material": "<p><strong>Temperature</strong> é um valor decimal entre 0 e 1 que influencia as probabilidades de seleção do próximo token. A geração de texto passa por três passos: Tokenization, Prediction (calcula probabilidades) e <strong>Sampling</strong> (escolhe o token) — é só nesse último passo que a temperature age; ela não muda o que o modelo prediz, só como a escolha é feita.</p><p>Temperature baixa (perto de 0) = determinístico, Claude quase sempre escolhe o token de maior probabilidade. Temperature alta (perto de 1) = probabilidade distribuída mais uniformemente, saída mais variada e criativa.</p><p>Faixas recomendadas: <strong>0.0–0.3</strong> (baixa) para respostas factuais, código, extração de dados; <strong>0.4–0.7</strong> (média) para resumo, conteúdo educacional; <strong>0.8–1.0</strong> (alta) para brainstorm e criação de conteúdo criativo.</p>",
})

L.append({
    "n": "2.6", "title": "Streaming de respostas",
    "topics": ["Problema: 10-30s de espera sem feedback", "stream=True e iteração sobre eventos", "6 tipos de evento (só ContentBlockDelta traz texto)", "stream.get_final_message()"],
    "material": "<p>Sem streaming, o servidor espera a resposta completa (10-30s) antes de mandar qualquer coisa ao cliente — uma tela de carregamento sem feedback. Com <strong>stream=True</strong>, o create() retorna um stream iterável de eventos, todos pertencentes a uma única requisição.</p><p>Seis tipos de evento: MessageStart, ContentBlockStart, <strong>ContentBlockDelta</strong> (o único que carrega o texto real, em pedaços), ContentBlockStop, MessageDelta, MessageStop.</p><p>A interface simplificada do SDK (<code>client.messages.stream(...)</code> com <code>stream.text_stream</code>) já filtra só o texto. Depois de consumir o stream, <code>stream.get_final_message()</code> devolve a mensagem completa montada — útil para guardar no histórico ou ler usage/stop_reason.</p>",
})

L.append({
    "n": "2.7", "title": "Dados estruturados (prefilling + stop sequences)",
    "topics": ["Problema: Claude embrulha JSON em texto/markdown", "Assistant message prefilling", "Stop sequences", "Generalização para Python, CSV, listas"],
    "material": "<p>Por padrão, ao pedir JSON, Claude devolve o conteúdo certo, mas embrulhado em cercas de markdown (```json ... ```) e com uma frase de explicação — o que quebra qualquer código que espera fazer <code>json.loads()</code> direto.</p><p>A solução combina duas técnicas: <strong>prefilling</strong> (você mesmo adiciona uma mensagem assistant com a abertura da cerca, ex.: <code>\"```json\"</code>, fazendo Claude \"pensar\" que já começou o bloco) e <strong>stop sequence</strong> (a API para a geração assim que Claude tenta fechar a cerca com <code>```</code>). O resultado é o JSON puro, sem comentário. Sempre limpe com <code>.strip()</code> antes de <code>json.loads()</code>.</p><p>A técnica generaliza: identifique o que o Claude naturalmente usaria para embrulhar o conteúdo (```python, ```csv, marcador de lista) e use isso como prefill/stop.</p>",
})

L.append({
    "n": "3.1", "title": "Avaliação de prompts (conceito)",
    "topics": ["Engenharia de prompt vs. avaliação de prompt", "As 3 opções depois de escrever um prompt", "Por que opções 1 e 2 são armadilhas", "Abordagem evaluation-first"],
    "material": "<p><strong>Engenharia de prompt</strong> é o conjunto de técnicas para escrever prompts melhores; <strong>avaliação de prompt</strong> é testagem automatizada para medir o quão bem eles funcionam — são complementares, não alternativas.</p><p>Depois de escrever um prompt, há 3 caminhos: (1) testar uma vez e considerar bom o suficiente — risco alto de quebrar em produção; (2) testar algumas vezes e ajustar casos de borda — ainda insuficiente, usuários reais trazem inputs muito mais variados do que se imagina; (3) rodar por um <strong>pipeline de avaliação</strong> com métricas objetivas — mais trabalho, mas dá confiança real. O objetivo é pegar problemas durante o desenvolvimento, não depois que o usuário encontrar.</p>",
})

L.append({
    "n": "3.2", "title": "Fluxo típico de avaliação (eval workflow)",
    "topics": ["5 passos: Draft → Dataset → Claude → Grader → Repetir", "O prompt como template ({question})", "Grader nota de 1 a 10", "Média = medida objetiva do baseline"],
    "material": "<p>O fluxo de avaliação tem 5 passos: <strong>(1) Draft a Prompt</strong> — escreva um template com um placeholder (ex.: {question}); <strong>(2) Create an Eval Dataset</strong> — junte perguntas de exemplo que representem o que o prompt vai enfrentar em produção (à mão ou geradas pelo próprio Claude); <strong>(3) Feed Through Claude</strong> — combine cada registro do dataset com o template e envie; <strong>(4) Feed Through a Grader</strong> — um avaliador dá uma nota de 1 a 10 olhando pergunta+resposta; a média das notas é sua medida objetiva (ex.: 7,66); <strong>(5) Change Prompt and Repeat</strong> — altere o prompt e rode tudo de novo para comparar a nova média com a antiga.</p>",
})

L.append({
    "n": "3.3", "title": "Gerando datasets de teste com Claude",
    "topics": ["Definir Goal (Input/Output) antes do prompt", "Meta-prompt para gerar o dataset", "Usar Haiku para gerar dados (tarefa simples e barata)", "chat() com stop_sequences condicional"],
    "material": "<p>Em vez de escrever casos de teste à mão, você pode pedir ao próprio Claude para gerar o dataset com um <strong>meta-prompt</strong>: descreva o objetivo, mostre um exemplo do formato JSON exato desejado, adicione restrições (tarefas pequenas, sem exigir muito código) e diga quantos objetos quer. Combine com prefill + stop sequence para receber JSON limpo, parseável com <code>json.loads()</code>.</p><p>Como gerar dados de teste é uma tarefa simples e de alto volume, é um bom lugar para usar um modelo mais rápido e barato como o <strong>Haiku</strong> em vez do modelo completo.</p>",
})

L.append({
    "n": "3.4", "title": "Rodando a avaliação (pipeline)",
    "topics": ["3 funções: run_prompt, run_test_case, run_eval", "Score hardcoded (placeholder) antes do grader real", "Por que a primeira rodada é lenta (requisições sequenciais)", "Saída verbosa sem instrução de formato"],
    "material": "<p>O pipeline se resume a 3 funções, cada uma com uma responsabilidade: <strong>run_prompt</strong> (um caso → interpola no template → chama chat() → retorna a saída), <strong>run_test_case</strong> (chama run_prompt e depois atribui uma nota — no início, um placeholder <code>score = 10</code> com comentário <code>#TODO - Grading</code>, para testar o pipeline de ponta a ponta antes de existir lógica de nota real), e <strong>run_eval</strong> (carrega o dataset, roda run_test_case em cada caso e junta os resultados numa lista).</p><p>Como as requisições correm uma atrás da outra, mesmo com Haiku uma rodada completa pode levar ~30 segundos. Sem instruções de formatação no prompt, as respostas do Claude tendem a ser mais verbosas do que o necessário — exatamente o tipo de problema que a avaliação deveria revelar.</p>",
})

L.append({
    "n": "3.5", "title": "Grading por modelo (model-based grading)",
    "topics": ["3 tipos de grader: código, modelo, humano", "Critérios determinísticos vs. de julgamento", "Pedir strengths/weaknesses/reasoning ANTES do score", "Integrando no run_test_case + statistics.mean"],
    "material": "<p>Existem três tipos de grader: <strong>código</strong> (checagens programáticas — comprimento, presença de palavras, validação de sintaxe), <strong>modelo</strong> (outro modelo julga qualidade, seguimento de instrução, completude) e <strong>humano</strong> (revisão manual). Para o exemplo de gerar código, três critérios: <em>Format</em> e <em>Valid Syntax</em> vão para um grader de código (são determinísticos); <em>Task Following</em> vai para um grader de modelo (exige julgamento).</p><p>O insight-chave: pedir ao grader <strong>strengths, weaknesses e reasoning antes do score</strong> — sem esse contexto, o modelo tende a jogar tudo perto de uma nota 6, medíocre e sem poder discriminativo. Colocar \"score\" por último no JSON pedido faz o modelo se comprometer com a nota só depois de já ter articulado o que é bom e o que é fraco.</p><p><code>run_test_case</code> passa a chamar o grader real em vez do placeholder, e <code>run_eval</code> calcula a média com <code>statistics.mean</code>.</p>",
})

L.append({
    "n": "3.6", "title": "Grading por código (code-based grading)",
    "topics": ["Validadores: validate_json, validate_python, validate_regex", "Campo \"format\" no dataset", "Prefill genérico ```code (múltiplos formatos)", "Score final = (model_score + syntax_score) / 2"],
    "material": "<p>Para saída de código, checar se \"faz sentido\" não basta — é preciso confirmar que é sintaticamente válida. Três funções validadoras compartilham a mesma forma: tentam fazer o parsing e retornam 10 se funcionar, 0 se lançar exceção — <code>validate_json</code> usa <code>json.loads()</code>, <code>validate_python</code> usa <code>ast.parse()</code>, <code>validate_regex</code> usa <code>re.compile()</code>.</p><p>Cada caso de teste precisa de um campo <strong>\"format\"</strong> (ex.: \"python\") para o grader de código saber qual validador rodar. Como o mesmo template de prompt serve para Python, JSON e Regex, o prefill usado é o genérico <code>```code</code> em vez de um específico como <code>```json</code>. O score final combina os dois sinais: <code>(model_score + syntax_score) / 2</code> — o peso pode ser ajustado conforme o caso de uso.</p>",
})

L.append({
    "n": "4.1", "title": "Engenharia de prompt (ciclo iterativo)",
    "topics": ["Ciclo: goal → prompt inicial → avaliar → aplicar técnica → reavaliar", "PromptEvaluator e max_concurrent_tasks", "generate_dataset() com num_cases baixo em desenvolvimento", "Score baixo inicial é normal (baseline)"],
    "material": "<p>Engenharia de prompt é pegar um prompt já escrito e melhorá-lo por um ciclo repetível: definir objetivo → escrever prompt inicial → avaliar → aplicar uma técnica → reavaliar para confirmar que ajudou (os dois últimos passos repetem até o desempenho ficar bom o bastante).</p><p>A classe <code>PromptEvaluator</code> encapsula geração de dataset e grading; <code>max_concurrent_tasks</code> limita quantos casos rodam em paralelo (comece com 3 para evitar rate limit). Durante o desenvolvimento, mantenha <code>num_cases</code> baixo (2-3) para cada iteração ser rápida. O primeiro prompt é deliberadamente fraco — existe só para dar um baseline a superar; uma nota inicial baixa (ex.: 2,3/10) é normal e esperada.</p>",
})

L.append({
    "n": "4.2", "title": "Sendo claro e direto",
    "topics": ["Clear = linguagem simples e inequívoca", "Direct = instrução com verbo de ação (não pergunta)", "A primeira linha é a mais importante do prompt", "Caso real: 2,32 → 3,92"],
    "material": "<p>A primeira linha de um prompt define o tom de tudo que segue. <strong>Ser claro</strong> significa usar linguagem simples, dizer exatamente o que você quer, liderando com a tarefa. <strong>Ser direto</strong> significa formular como instrução, abrindo com um verbo de ação (\"Gere\", \"Crie\", \"Escreva\") em vez de uma pergunta.</p><p>Exemplo real do curso: reescrever \"What should this person eat?\" para \"Generate a one-day meal plan for an athlete that meets their dietary restrictions.\" — só essa mudança na abertura moveu a nota de avaliação de <strong>2,32 para 3,92</strong>, sem alterar mais nada no prompt.</p>",
})

L.append({
    "n": "4.3", "title": "Sendo específico",
    "topics": ["Output quality guidelines (o que a saída deve ter)", "Process steps (como Claude deve raciocinar)", "Quando usar cada um", "Caso real: 3,92 → 7,86"],
    "material": "<p><strong>Guidelines de qualidade de saída</strong> listam as qualidades que o resultado deve ter — comprimento, estrutura, elementos específicos, tom. Use-as em quase todo prompt, são a rede de segurança de baixo custo para consistência.</p><p><strong>Process steps</strong> dão ao Claude uma sequência para seguir antes de responder — úteis para troubleshooting, decisões, pensamento crítico ou forçar uma visão mais ampla em vez de fixar na primeira ideia.</p><p>No exemplo do plano de refeição, adicionar só um bloco de guidelines (calorias exatas, macros, horários, restrições, porções em gramas) elevou a nota de <strong>3,92 para 7,86</strong> — mais que o dobro, apenas por especificidade. Prompts profissionais costumam combinar as duas técnicas: guidelines para consistência de forma, steps para garantir raciocínio completo.</p>",
})

L.append({
    "n": "4.4", "title": "Estruturando com tags XML",
    "topics": ["Delimitadores claros para conteúdo interpolado", "Nomes de tag descritivos, não genéricos", "Quando usar (contexto grande, tipos mistos, várias variáveis)"],
    "material": "<p>Quando um prompt tem muito conteúdo, Claude pode ter dificuldade em saber o que pertence junto. Embrulhar partes distintas — dados, código, documentação — em <strong>tags XML descritivas</strong> cria delimitadores claros: <code>&lt;sales_records&gt;</code> é melhor que <code>&lt;data&gt;</code>; <code>&lt;athlete_information&gt;</code> é melhor que um bloco de estatísticas sem rótulo.</p><p>São mais úteis com contexto grande, tipos de conteúdo misturados (código + documentação), ou várias variáveis interpoladas ao mesmo tempo — mas ajudam mesmo em conteúdo curto, porque deixam a estrutura explícita.</p>",
})

L.append({
    "n": "4.5", "title": "Fornecendo exemplos (one-shot / multi-shot)",
    "topics": ["One-shot vs. multi-shot", "Casos de borda (ex.: sarcasmo)", "Tags <sample_input> / <ideal_output>", "Minerar exemplos das suas melhores avaliações"],
    "material": "<p>Dar ao Claude pares de exemplo (entrada/saída ideal) mostra o que uma boa resposta parece, em vez de só descrever. <strong>One-shot</strong> = um único exemplo, suficiente para estabelecer um padrão dominante. <strong>Multi-shot</strong> = vários exemplos cobrindo cenários distintos — necessário quando há mais de um jeito de errar, como um tweet sarcástico que parece positivo pelas palavras mas é negativo na intenção.</p><p>Combine com tags XML (<code>&lt;sample_input&gt;</code> / <code>&lt;ideal_output&gt;</code>), explique <strong>por que</strong> a saída é ideal (não só mostre), e prefira minerar os exemplos das suas <strong>saídas de avaliação com nota mais alta</strong> em vez de inventá-los.</p>",
})

L.append({
    "n": "5.1", "title": "Introdução ao Tool Use",
    "topics": ["Limite: Claude só conhece dados de treinamento", "Fluxo de 4 passos: Initial Request → Tool Request → Data Retrieval → Final Response", "Quem executa o código (seu servidor, nunca Claude)", "Benefícios do tool use"],
    "material": "<p>Por padrão, Claude só conhece seus dados de treinamento — sem eventos atuais, dados em tempo real ou sistemas externos. <strong>Tool use</strong> é um vai-e-vem estruturado: Claude pede os dados extras de que precisa, seu servidor os busca, e Claude finaliza a resposta usando essa informação fresca.</p><p>Fluxo de 4 passos: <strong>Initial Request</strong> (você envia a pergunta + instruções de como obter dados extras) → <strong>Tool Request</strong> (Claude pede os dados específicos) → <strong>Data Retrieval</strong> (seu servidor executa o código e busca em uma API/banco) → <strong>Final Response</strong> (Claude combina os dados com a pergunta original). Claude nunca chama sistemas externos diretamente — quem executa é sempre o seu servidor.</p>",
})

L.append({
    "n": "5.2", "title": "Projeto: ferramenta de lembretes",
    "topics": ["Objetivo: lembrete em linguagem natural", "3 limitações do Claude que motivam as tools", "As 3 tools do projeto (data/hora, somar duração, salvar lembrete)", "Construir uma tool por vez, da mais simples à mais complexa"],
    "material": "<p>Projeto prático: fazer Claude aceitar \"Set a reminder for my doctor's appointment. It's a week from Thursday\" e responder \"OK, I will remind you.\" Três limitações motivam a criação de tools: Claude nem sempre sabe a hora exata, não lida bem com soma de datas muitos dias no futuro, e não tem mecanismo nativo para de fato registrar um lembrete.</p><p>Três tools resolvem cada limitação, uma por vez: <strong>get_current_datetime</strong> (data/hora precisas), <strong>add_duration_to_datetime</strong> (cálculo confiável de datas futuras) e <strong>set_reminder</strong> (registra o lembrete). A recomendação é construir a mais simples primeiro para entender o mecanismo antes de somar complexidade.</p>",
})

L.append({
    "n": "5.3", "title": "Função da tool (tool function)",
    "topics": ["Função Python comum, chamada quando Claude decide", "Boas práticas: nomes descritivos, validação de input, mensagens de erro úteis", "Exemplo: get_current_datetime com validação"],
    "material": "<p>Uma <strong>tool function</strong> é uma função Python comum que roda automaticamente quando Claude decide que precisa de informação extra. Boas práticas: nomes descritivos (função e parâmetros), <strong>validar os inputs</strong> (checar se parâmetros obrigatórios não estão vazios/inválidos, levantando erro quando estão) e fornecer <strong>mensagens de erro significativas</strong> — Claude vê essas mensagens e pode tentar de novo com parâmetros corrigidos.</p><p>Exemplo: <code>get_current_datetime(date_format=\"%Y-%m-%d %H:%M:%S\")</code> levanta <code>ValueError</code> se o formato vier vazio, e usa <code>datetime.now().strftime(...)</code> para formatar.</p>",
})

L.append({
    "n": "5.4", "title": "Schemas de tools (JSON Schema)",
    "topics": ["3 partes: name, description, input_schema", "JSON Schema não é exclusivo de IA", "Descrição com 3-4 frases, quando usar, o que retorna", "Pedir ao próprio Claude para gerar o schema"],
    "material": "<p>Depois da função, o próximo passo é um <strong>JSON Schema</strong> que documenta a tool para o Claude decidir quando e como chamá-la. JSON Schema não foi criado para IA — é uma especificação de validação de dados amplamente usada, adotada pela comunidade de IA porque descreve bem parâmetros de função.</p><p>A especificação completa tem 3 partes: <strong>name</strong> (nome claro, ex. \"get_weather\"), <strong>description</strong> (o que faz, quando usar, o que retorna — recomenda-se 3-4 frases) e <strong>input_schema</strong> (o esquema JSON dos argumentos). Um jeito prático de gerar o schema é pedir ao próprio Claude, fornecendo o código da função e a documentação de tool use como contexto.</p>",
})

L.append({
    "n": "5.5", "title": "Lidando com blocos de mensagem (multi-block)",
    "topics": ["Parâmetro tools na chamada", "Mensagem assistant com Text Block + ToolUse Block", "Preservar response.content inteiro no histórico", "Atualizando os helpers para múltiplos blocos"],
    "material": "<p>Para habilitar tools, inclua o parâmetro <strong>tools</strong> na chamada (lista de schemas). Quando Claude decide usar uma tool, a mensagem assistant vem com múltiplos blocos: um <strong>Text Block</strong> (texto explicando o que está fazendo) e um <strong>ToolUse Block</strong> (id, nome da função, input como dicionário, type \"tool_use\").</p><p>Como a API não guarda histórico, é essencial preservar a <strong>estrutura completa</strong> de <code>response.content</code> ao adicionar a mensagem assistant de volta à lista — incluindo o bloco de tool use, crucial para o contexto nas chamadas seguintes. Helpers como add_assistant_message() precisam ser atualizados para aceitar conteúdo multi-bloco, não só texto simples.</p>",
})

L.append({
    "n": "5.6", "title": "Enviando resultados de tools",
    "topics": ["Rodar a função com **input", "Tool result block (tool_use_id, content, is_error)", "Múltiplas chamadas de tool em uma resposta", "Reenviar o schema na requisição final"],
    "material": "<p>Depois de receber um ToolUse block, você extrai <code>response.content[1].input</code> e chama a função com desempacotamento: <code>get_current_datetime(**input)</code>. O resultado volta em um <strong>tool_result block</strong>, dentro de uma mensagem <em>user</em>, com três campos: <strong>tool_use_id</strong> (deve bater com o id do ToolUse original), <strong>content</strong> (a saída, como string) e <strong>is_error</strong> (se algo deu errado).</p><p>Se Claude pedir várias tools na mesma resposta, cada uma tem um id único, e os resultados precisam bater por id, mesmo que cheguem fora de ordem. Importante: a requisição final ainda precisa incluir o parâmetro <strong>tools</strong>, mesmo sem esperar uma nova chamada — Claude precisa do schema para entender as referências de tool já presentes no histórico.</p>",
})

L.append({
    "n": "6.1", "title": "Introdução a RAG (Retrieval Augmented Generation)",
    "topics": ["Problema: documentos grandes demais para o prompt", "Opção 1 (tudo no prompt) vs. Opção 2 (chunking + busca)", "Benefícios: foco, escala, eficiência", "Desafios: preprocessamento, busca, contexto perdido, estratégia de chunking"],
    "material": "<p>RAG resolve o problema de documentos grandes demais para caber em um único prompt (ex.: um relatório financeiro de 800 páginas). Em vez de colocar tudo no prompt (limite rígido de tamanho, menor eficácia, maior custo e latência), RAG quebra o documento em <strong>chunks</strong> durante um pré-processamento e, no momento da pergunta, busca só os chunks mais relevantes para incluir no prompt.</p><p>Benefícios: foco (Claude trabalha só com o conteúdo relevante), escala (funciona com documentos grandes ou múltiplos) e eficiência (prompts menores custam menos e são mais rápidos). Desafios: é preciso decidir a estratégia de chunking, montar um mecanismo de busca, e aceitar que chunks incluídos podem não conter tudo que falta.</p>",
})

L.append({
    "n": "6.2", "title": "Estratégias de chunking",
    "topics": ["Size-based (tamanho fixo, com overlap)", "Structure-based (headers/seções — melhor para Markdown)", "Semantic-based (agrupa frases relacionadas)", "Sentence-based (meio-termo prático)"],
    "material": "<p>Chunking ruim pode inserir contexto irrelevante no prompt — ex.: perguntar sobre \"bugs corrigidos por engenheiros\" pode trazer uma seção de pesquisa médica que menciona \"bug\" em outro sentido.</p><p><strong>Size-based</strong>: divide em strings de tamanho igual — simples, funciona com qualquer tipo de documento, mas corta palavras/cabeçalhos no meio (o overlap entre chunks reduz esse problema). <strong>Structure-based</strong>: segue a estrutura natural do documento (cabeçalhos Markdown) — chunks mais limpos, mas só funciona quando a estrutura é garantida. <strong>Semantic-based</strong>: agrupa frases relacionadas por significado via NLP — o mais sofisticado e caro computacionalmente, produz os chunks mais relevantes. <strong>Sentence-based</strong>: meio-termo prático, divide por frases e agrupa em blocos com overlap.</p><p>Não existe \"a melhor\" estratégia — depende do documento e do trade-off complexidade vs. qualidade do chunk.</p>",
})

L.append({
    "n": "6.3", "title": "Embeddings de texto",
    "topics": ["Busca semântica vs. busca por palavra-chave", "O que é um embedding (vetor numérico de significado)", "Cada número não é interpretável diretamente", "VoyageAI (Anthropic não gera embeddings)"],
    "material": "<p>Encontrar os chunks mais relevantes é um <strong>problema de busca</strong>. A <strong>busca semântica</strong> usa <strong>embeddings de texto</strong> — uma representação numérica do significado de um texto — em vez de bater palavra por palavra. Cada número do vetor é conceitualmente uma \"nota\" de alguma qualidade do texto, mas o que cada dimensão representa exatamente não é interpretável por humanos — é aprendido pelo modelo durante o treinamento.</p><p>A Anthropic não oferece geração de embeddings diretamente; o provedor recomendado no curso é a <strong>VoyageAI</strong> (conta e API key separadas, gratuita para começar), usando o modelo <code>voyage-3-large</code>.</p>",
})

L.append({
    "n": "6.4", "title": "O fluxo completo de RAG (exemplo numérico)",
    "topics": ["Chunk → Embed → Vector DB → Embed da query → Buscar por similaridade → Montar prompt final", "Normalização de vetores", "Cosine similarity (e cosine distance)", "Exemplo: 0,983 vs. 0,398"],
    "material": "<p>Passo a passo com números: (1) o documento é dividido em chunks; (2) cada chunk vira um embedding (vetor de números); (3) os embeddings são guardados em um <strong>vector database</strong>, junto com o texto original (senão a busca devolve só números, não texto usável); (4) a pergunta do usuário é convertida no mesmo tipo de embedding; (5) o vector database retorna os embeddings mais parecidos, usando <strong>cosine similarity</strong> — o cosseno do ângulo entre dois vetores, de -1 a 1 (perto de 1 = muito parecido, perto de 0 = sem relação, perto de -1 = muito diferente); (6) o chunk vencedor entra no prompt final junto com a pergunta original.</p><p>No exemplo do curso, a pergunta sobre \"software engineering\" teve similaridade 0,983 com o chunk certo contra apenas 0,398 com o chunk de medicina — venceu por larga margem. <strong>Cosine distance</strong> é o inverso: (1 − cosine similarity), onde valores baixos indicam alta similaridade.</p>",
})

L.append({
    "n": "6.5", "title": "Implementando o fluxo RAG em código",
    "topics": ["5 passos: chunk, embed, vector store, embed da query, search", "store.add_vector(embedding, {content: chunk})", "Por que guardar o texto original junto", "store.search(user_embedding, k)"],
    "material": "<p>Implementação prática em 5 passos: dividir o texto em chunks (<code>chunk_by_section</code>), gerar embeddings de todos de uma vez, criar um <code>VectorIndex()</code> e adicionar cada par embedding+texto com <code>store.add_vector(embedding, {\"content\": chunk})</code>, gerar o embedding da pergunta do usuário, e buscar com <code>store.search(user_embedding, k)</code> — que retorna os k chunks mais similares com suas distâncias. É essencial guardar o texto original junto ao embedding: buscar no vector store sozinho só devolve números, não o conteúdo usável.</p>",
})

L.append({
    "n": "6.6", "title": "Busca lexical BM25",
    "topics": ["Limite da busca semântica pura (ex.: IDs exatos)", "Como o BM25 funciona (tokeniza, pesa termos raros)", "Busca híbrida: semântica + lexical em paralelo"],
    "material": "<p>A busca semântica pode falhar em encontrar um <strong>ID exato</strong> (ex.: \"INC-2023-Q4-011\"), porque otimiza para similaridade conceitual, não correspondência literal. A solução é combinar com <strong>busca lexical</strong> via <strong>BM25</strong> (Best Match 25): tokeniza a query em termos, conta a frequência de cada termo em todos os documentos, dá mais peso a termos raros (um ID de incidente pesa mais que a palavra \"a\") e retorna os chunks com mais ocorrências dos termos mais pesados.</p><p>A estratégia híbrida roda busca semântica e lexical em paralelo e combina os resultados — pegando tanto correspondências conceituais quanto literais.</p>",
})

L.append({
    "n": "6.7", "title": "Pipeline multi-índice (Reciprocal Rank Fusion)",
    "topics": ["VectorIndex e BM25Index compartilham a mesma API", "Classe Retriever unifica os dois", "Fórmula RRF: soma de 1/(k+rank)", "Extensibilidade: qualquer índice com a mesma interface"],
    "material": "<p>VectorIndex e BM25Index têm APIs quase idênticas (<code>add_document()</code> e <code>search()</code>), o que permite uni-los numa classe <strong>Retriever</strong> que encaminha a query para os dois índices e funde os rankings com <strong>Reciprocal Rank Fusion (RRF)</strong>: soma <code>1/(k + rank)</code> para cada documento em cada ranking (k costuma ser 60). Como cada método pontua de um jeito diferente, simplesmente concatenar as listas não funciona — é preciso normalizar e combinar de forma justa.</p><p>No exemplo do curso, o chunk que aparece bem posicionado em <strong>ambos</strong> os índices termina no topo do ranking final. Como todo índice implementa a mesma interface (<code>SearchIndex</code>), novos métodos de busca (baseados em grafo, por exemplo) podem ser adicionados ao Retriever sem alterar sua lógica.</p>",
})

L.append({
    "n": "7.1", "title": "Extended thinking",
    "topics": ["Bloco de \"raciocínio\" antes da resposta final", "Benefícios: melhor reasoning, mais precisão, transparência", "Trade-offs: custo, latência, complexidade de tratamento", "Quando ativar (guiado por avaliação, não por padrão)", "Signature e redacted_thinking"],
    "material": "<p><strong>Extended thinking</strong> dá ao Claude tempo para \"rascunhar\" o raciocínio antes de escrever a resposta final. Com essa opção ativa, a mensagem assistant passa a ter um <strong>thinking block</strong> (o raciocínio) seguido do <strong>text block</strong> (a resposta).</p><p>Benefícios: melhor raciocínio e maior precisão em tarefas difíceis, e transparência sobre o processo. Trade-offs: tokens de pensamento são cobrados (custo maior), mais latência, e seu código precisa tratar o bloco extra. A decisão de ativar deve vir de <strong>avaliação</strong> — rode sem thinking primeiro, e só ative se a precisão não for suficiente depois do prompt já otimizado; não é para ligar por padrão em toda chamada.</p><p>O campo <strong>signature</strong> é um token criptográfico ligado ao texto exato do raciocínio, provando que não foi alterado antes de voltar à API. Em alguns casos o Claude retorna um bloco <strong>redacted_thinking</strong> (criptografado), quando o raciocínio interno é sinalizado por sistemas de segurança — o conteúdo é preservado de forma criptografada para manter o contexto em turnos futuros.</p><p>Implementação: dois parâmetros novos, <code>thinking</code> (flag) e <code>thinking_budget</code> (mínimo 1024 tokens); max_tokens deve ser maior que o thinking_budget.</p>",
})

L.append({
    "n": "7.2", "title": "Suporte a imagens",
    "topics": ["Limites: até 100 imagens, 5MB cada, 8000px (única) / 2000px (múltiplas)", "Image block + text block na mesma mensagem", "Custo em tokens: (largura×altura)/750", "Técnicas de precisão: passo a passo, one-shot"],
    "material": "<p>Claude pode analisar imagens: descrever, comparar, contar objetos. Limites: até <strong>100 imagens</strong> por requisição, <strong>5MB</strong> por imagem, altura/largura máxima de <strong>8000px</strong> para uma única imagem ou <strong>2000px</strong> quando há múltiplas imagens. O custo em tokens de uma imagem é <code>(largura em px × altura em px) / 750</code>.</p><p>Uma pergunta simples (\"quantas bolinhas de gude tem nesta imagem?\") pode dar uma contagem errada. A precisão melhora com: instruções e passos de análise detalhados (contar uma a uma, verificar com um segundo método), exemplos one-shot/multi-shot (uma imagem de referência com contagem conhecida antes da imagem-alvo), e quebrar tarefas complexas em passos menores — como no exemplo real de avaliação de risco de incêndio por imagem de satélite, estruturado em etapas até chegar a uma nota final de 1 (baixo) a 4 (severo).</p>",
})

L.append({
    "n": "8", "title": "Model Context Protocol (dentro do curso da API)",
    "topics": ["Introdução ao MCP, clientes MCP", "Configuração de projeto, definindo tools com MCP", "Server inspector", "Implementando um cliente, definindo/acessando resources", "Definindo prompts, prompts no cliente", "Revisão MCP"],
    "material": "<p>Esta seção do curso da API é uma introdução prática ao MCP — o mesmo protocolo coberto em profundidade no Módulo 3 (curso dedicado). Ela cobre a mesma espinha dorsal: como definir <strong>tools</strong> em um servidor MCP, inspecioná-lo com o <strong>MCP Inspector</strong>, implementar um <strong>cliente</strong> que consome esse servidor, e como <strong>resources</strong> e <strong>prompts</strong> completam os três primitivos do protocolo. Ver o Módulo 3 para o material completo e o glossário de MCP.</p>",
})

L.append({
    "n": "9", "title": "Apps Anthropic — Claude Code e Computer Use",
    "topics": ["Configuração do Claude Code", "Claude Code em ação (visão geral)", "Aprimoramentos com servidores MCP"],
    "material": "<p>Esta seção apresenta o Claude Code de forma resumida como um dos \"aplicativos Anthropic\", cobrindo a configuração inicial e como servidores MCP estendem suas capacidades. O curso dedicado do Módulo 4 (\"Claude Code em Ação\") aprofunda esse tema com sessões longas, permissões, hooks e automação.</p>",
})

L.append({
    "n": "10", "title": "Agentes e workflows",
    "topics": ["Fluxos de paralelização", "Fluxos em cadeia (chaining)", "Fluxos de roteamento (routing)", "Agentes e ferramentas", "Inspeção de ambiente", "Workflows vs. agentes"],
    "material": "<p>Esta seção fecha o curso da API introduzindo padrões de arquitetura agêntica — o tema de maior peso na prova de certificação Architect. <strong>Workflows</strong> são caminhos pré-definidos e previsíveis: <em>parallelization</em> (rodar sub-tarefas em paralelo e agregar), <em>chaining</em> (uma etapa alimenta a próxima em sequência fixa) e <em>routing</em> (direcionar a entrada para o caminho certo com base em uma classificação inicial).</p><p><strong>Agentes</strong>, por outro lado, decidem dinamicamente os próprios passos, usando ferramentas e inspecionando o ambiente para adaptar o plano. A distinção <strong>workflows vs. agentes</strong> é uma escolha de design: workflows dão previsibilidade e custo controlado para tarefas bem definidas; agentes dão flexibilidade para tarefas abertas, ao custo de menor previsibilidade. <span class='badge synth'>complementar</span></p>",
})

m2["lessons"] = L

with open("/home/claude/module2_lessons.json", "w", encoding="utf-8") as f:
    json.dump(m2, f, ensure_ascii=False, indent=1)
print("module2 lessons:", len(L))
