# -*- coding: utf-8 -*-
import json
with open("/home/claude/quiz2_partA.json", "r", encoding="utf-8") as f:
    quiz2 = json.load(f)
def add(lesson, q, options, correct, note, source="real"):
    quiz2.append({"lesson": lesson, "q": q, "options": options, "correct": correct, "note": note, "source": source})

# Section 5 - Tool Use (6 lessons x5)
add("5.1", "Why can't Claude answer a question about current weather by default?",
    ["Weather questions are blocked by the API","Claude only knows information from its training data, which has no real-time data","Weather requires a system prompt to be set","Claude can only answer questions about coding","The temperature parameter must be set to 0 first"], 1,
    "Só conhece dados de treinamento, sem tempo real.")
add("5.1", "What is the correct order of the tool use flow?",
    ["Tool Request → Initial Request → Final Response → Data Retrieval","Initial Request → Tool Request → Data Retrieval → Final Response","Data Retrieval → Initial Request → Tool Request → Final Response","Final Response → Data Retrieval → Tool Request → Initial Request","Initial Request → Data Retrieval → Tool Request → Final Response"], 1,
    "Initial→Tool Request→Data Retrieval→Final Response.")
add("5.1", "In the tool use flow, who actually runs the code that fetches external data?",
    ["Claude, directly","The user's browser","Your server","The weather API itself, unprompted","A separate model dedicated to tool calls"], 2,
    "Seu servidor executa o código, nunca Claude.")
add("5.1", "In the weather example, what does Claude do after receiving the current weather data back from the server?",
    ["It ignores the data and answers from training knowledge","It asks for a second, unrelated piece of data","It generates a final response combining the original question with the fresh data","It stores the data for the next unrelated conversation","It ends the conversation without responding"], 2,
    "Combina a pergunta original com o dado fresco.")
add("5.1", "Which of the following is listed as a key benefit of tool use?",
    ["Lower max_tokens usage","Guaranteed deterministic output at any temperature","External system integration — connecting Claude to databases, APIs, and other services","Removing the need for a system prompt","Automatically translating the user's question"], 2,
    "Integração com sistemas externos.")

add("5.2", "What is the target interaction this project aims to support?",
    ["Claude answering trivia questions about dates","A natural-language reminder request that Claude confirms it will handle","Claude translating dates between time zones","Claude generating a calendar UI","Claude summarizing a list of appointments"], 1,
    "Pedido em linguagem natural + confirmação do lembrete.")
add("5.2", "Which of the following is NOT listed as a reason this project is challenging for Claude?",
    ["Claude might not know the exact current time","Claude doesn't always handle time-based addition well","Claude has no built-in mechanism to set a reminder","Claude cannot understand natural language date references","None of the above — all are listed reasons"], 3,
    "Entender linguagem natural NÃO é listado como limitação nesta lição.")
add("5.2", "How many custom tools will this project implement in total?",
    ["One","Two","Three","Five","It's left open-ended"], 2,
    "Três tools: data/hora, somar duração, salvar lembrete.")
add("5.2", "What is the purpose of the \"add duration to date time\" tool?",
    ["To translate the reminder into another language","To reliably calculate a future date/time, since Claude isn't perfect at this addition","To store the reminder permanently","To fetch the current weather for context","To validate the user's input format"], 1,
    "Cálculo confiável de datas futuras.")
add("5.2", "What approach does the lesson recommend for building the three tools?",
    ["Build all three simultaneously to save time","Build them in a random order","Build them one at a time, starting with the simplest","Only build the most complex one first","Skip tool-by-tool testing and test everything at the end"], 2,
    "Uma por vez, da mais simples à mais complexa.")

add("5.3", "What is a tool function?",
    ["A function that runs automatically on a schedule","A plain Python function that gets executed when Claude decides it needs extra information","A built-in Claude API endpoint","A function that only formats JSON","A function that replaces the system prompt"], 1,
    "Função Python comum, chamada quando necessário.")
add("5.3", "Why is input validation considered a best practice for tool functions?",
    ["It makes the function run faster","Claude can see error messages and may retry with corrected parameters","It is required by the Claude API to register a tool","It prevents the function from being called more than once","It removes the need for a JSON schema"], 1,
    "Claude vê o erro e pode tentar de novo corrigido.")
add("5.3", "In get_current_datetime(date_format=\"%Y-%m-%d %H:%M:%S\"), what does the date_format parameter control?",
    ["The time zone used","Whether the function raises an error","The format of the returned date/time string","The number of retries Claude can attempt","Whether the function returns a string or an integer"], 2,
    "Controla o formato da string retornada.")
add("5.3", "What happens if get_current_datetime is called with an empty string as date_format?",
    ["It silently returns None","It raises a ValueError","It uses the default format automatically","It returns the current date with no time","It crashes the entire application"], 1,
    "Levanta ValueError por validação.")
add("5.3", "According to the lesson, what comes right after writing the tool function?",
    ["Deploying the application to production","Writing a JSON schema that describes the function to Claude","Deleting the function and starting over","Training a new model","Writing unit tests only, with no further integration"], 1,
    "Em seguida vem o JSON Schema.")

add("5.4", "What are the three main parts of a complete tool specification?",
    ["name, input_schema, and output_schema","name, description, and input_schema","function, arguments, and return_type","title, body, and footer","type, format, and default"], 1,
    "name, description e input_schema.")
add("5.4", "Is JSON Schema specific to AI or tool calling?",
    ["Yes, it was invented for AI tool calling","No, it's a widely-used data validation spec the AI community adopted","Yes, but only for Anthropic's API","No, it only works with Python","Yes, it was created by Anthropic"], 1,
    "Não é exclusivo de IA — foi adotado pela comunidade.")
add("5.4", "According to the lesson, roughly how many sentences should a tool description be?",
    ["1 sentence","3-4 sentences","10+ sentences","No limit is suggested","Exactly 2 words"], 1,
    "3-4 frases recomendadas.")
add("5.4", "What is the recommended \"easy way\" to generate a JSON schema for a tool function?",
    ["Write it manually with no reference material","Ask Claude to generate it, providing the function code and the tool-use documentation as context","Copy a random schema from the internet","Use a schema from an unrelated tool","Skip the schema and only rely on the docstring"], 1,
    "Pedir ao Claude, com código + docs como contexto.")
add("5.4", "What is the purpose of importing ToolParam from the Anthropic library?",
    ["It is required for the function to run at all","It adds type safety and prevents type errors when using the schema with Claude's API","It automatically generates the tool function's code","It replaces the need for a description field","It converts the schema into YAML format"], 1,
    "Adiciona segurança de tipos.")

add("5.5", "What parameter must be included in the API call to let Claude use tools?",
    ["functions","tools","schema","actions","callables"], 1,
    "Parâmetro tools na chamada.")
add("5.5", "What does a multi-block assistant message typically contain when Claude decides to use a tool?",
    ["Only a ToolUse block","A Text block and a ToolUse block","Only an error block","A single plain string","A list of previous user messages"], 1,
    "Text block + ToolUse block.")
add("5.5", "Which of the following is NOT part of a ToolUse block?",
    ["An ID for tracking the tool call","The name of the function to call","Input parameters formatted as a dictionary","The type designation \"tool_use\"","The full conversation history"], 4,
    "O histórico completo não faz parte do bloco.")
add("5.5", "Why must the entire response.content be preserved when appending the assistant message to history?",
    ["It's optional and only improves formatting","It preserves both the text and tool use blocks, which Claude needs for context in later calls","It reduces the number of tokens used","It automatically triggers the tool to run","It replaces the need for the tools parameter in future calls"], 1,
    "Preserva texto + tool use para contexto futuro.")
add("5.5", "Why do helper functions like add_assistant_message() typically need to be updated for tool use?",
    ["Because tool calls require a different model","Because they usually only support single text blocks, not multi-block content","Because Claude no longer needs conversation history with tools","Because tool use disables all previous messages","Because the API key format changes when tools are used"], 1,
    "Só suportavam blocos de texto único.")

add("5.6", "How do you call a tool function using the input from a ToolUse block?",
    ["get_current_datetime(response.content[1].input)","get_current_datetime(**response.content[1].input)","get_current_datetime.run(response)","response.content[1].call()","get_current_datetime(response)"], 1,
    "Desempacotamento com **input.")
add("5.6", "Which field of a tool_result block must match the id of the originating ToolUse block?",
    ["content","is_error","tool_use_id","type","name"], 2,
    "tool_use_id deve bater com o id do ToolUse.")
add("5.6", "If Claude requests two tool calls in one response, how does your code know which result belongs to which request?",
    ["By the order the results are sent, always","By matching each tool_use_id to the corresponding ToolUse block's id","It doesn't matter, Claude re-matches them automatically","By the tool's name only","By timestamp"], 1,
    "Casamento por id, não por ordem.")
add("5.6", "What role does the message containing a tool_result block have?",
    ["assistant","system","user","tool","function"], 2,
    "tool_result vai numa mensagem user.")
add("5.6", "Why must the tools parameter still be included in the final follow-up request, even though Claude isn't expected to call a tool again?",
    ["It isn't required — this is a common mistake","Claude needs the schema to understand the tool references already in the conversation history","It forces Claude to always call the tool one more time","It reduces the token count of the request","It replaces the need for the tool_result block"], 1,
    "Precisa do schema para entender referências já no histórico.")

# Section 6 - RAG (7 lessons x5)
add("6.1", "What problem does RAG primarily solve?",
    ["Claude forgetting the system prompt","Working with documents too large to fit into a single prompt","Claude's inability to call external tools","Formatting JSON responses","Reducing the number of API calls per session"], 1,
    "Documentos grandes demais para um prompt só.")
add("6.1", "Which of the following is NOT listed as a limitation of stuffing the entire document into the prompt?",
    ["There's a hard limit on prompt length","Claude gets less effective with very long prompts","Larger prompts cost more to process","Larger prompts take longer to process","It makes Claude ignore the user's question entirely"], 4,
    "Ignorar a pergunta não é uma limitação listada.")
add("6.1", "In the RAG approach, when does document chunking happen?",
    ["After Claude generates its final answer","During a preprocessing step, before any question is asked","Only if the user explicitly requests it in the prompt","It happens inside Claude's context window automatically","During model training"], 1,
    "No pré-processamento, antes da pergunta.")
add("6.1", "Asked \"What risks does this company face?\", what would a RAG system do?",
    ["Include the entire 800-page document in the prompt","Search the chunks, find the relevant one (e.g. Risk Factors), and include only that","Ignore the question and summarize the whole document","Ask the user to upload a shorter document","Always return the first chunk in the document"], 1,
    "Busca e inclui só o chunk relevante.")
add("6.1", "According to the lesson, what does RAG trade off in exchange for scalability and efficiency?",
    ["Answer accuracy, always","Upfront simplicity — RAG requires more technical decisions and preprocessing work","The ability to use JSON schemas","Support for multiple documents","Claude's context window size"], 1,
    "Troca simplicidade inicial por escala/eficiência.")

add("6.2", "Why can poor chunking cause a RAG system to give wrong answers?",
    ["It makes the API calls too slow","It can insert irrelevant context into the prompt, like an unrelated section that happens to share a keyword","It always exceeds the token limit","It disables the tools parameter","It prevents Claude from receiving any chunk at all"], 1,
    "Pode trazer contexto irrelevante por coincidência de palavra.")
add("6.2", "What is the simplest chunking strategy?",
    ["Semantic-based chunking","Structure-based chunking","Size-based chunking","Sentence-based chunking","Random chunking"], 2,
    "Size-based é a mais simples.")
add("6.2", "What problem does adding overlap between chunks help solve?",
    ["It removes the need for a search mechanism","It prevents words, sentences, and headers from being cut off between chunks","It makes chunking computationally cheaper","It guarantees semantic relevance","It eliminates the need for preprocessing"], 1,
    "Evita cortar palavras/cabeçalhos na fronteira dos chunks.")
add("6.2", "When does structure-based chunking work best?",
    ["On any plain text with no formatting","Only on scanned PDF images","When there are guarantees about the document's structure, like Markdown headers","Only when overlap is disabled","Only for code files"], 2,
    "Quando há garantia de estrutura (ex.: Markdown).")
add("6.2", "Which chunking strategy is described as computationally expensive but producing the most relevant chunks?",
    ["Size-based chunking","Structure-based chunking","Semantic-based chunking","Sentence-based chunking","Fixed-token chunking"], 2,
    "Semantic-based: cara, porém mais relevante.")

add("6.3", "What kind of problem is finding the most relevant chunks for a user's question?",
    ["A formatting problem","A search problem","A billing problem","A tokenization problem","A translation problem"], 1,
    "É um problema de busca.")
add("6.3", "How does semantic search differ from keyword-based search?",
    ["It only works with numeric data","It uses text embeddings to understand meaning, instead of matching exact words","It requires no preprocessing at all","It replaces the need for chunking","It only works with structure-based chunks"], 1,
    "Usa embeddings para significado, não palavra exata.")
add("6.3", "What is a text embedding?",
    ["A summary of the text written by Claude","A numerical representation of the meaning contained in some text","A compressed version of the original text file","A list of keywords extracted from the text","The chunk's character count"], 1,
    "Representação numérica do significado.")
add("6.3", "According to the lesson, do we know precisely what each number in an embedding represents?",
    ["Yes, each number always represents a fixed, documented quality","No — we don't know precisely; conceptual examples like \"how happy the text is\" are illustrative, not literal","Yes, but only for VoyageAI's embedding models","No, embeddings don't contain numbers at all","Yes, the number of dimensions tells us exactly what each one means"], 1,
    "Não sabemos exatamente — exemplos são só ilustrativos.")
add("6.3", "Which provider does the lesson recommend for generating embeddings, since Anthropic doesn't offer this directly?",
    ["OpenAI","Google","VoyageAI","Hugging Face","Cohere"], 2,
    "VoyageAI é o provedor recomendado.")

add("6.4", "What is the correct order of the full RAG pipeline described in this lesson?",
    ["Embed query → chunk text → store in vector database → generate embeddings","Chunk text → generate embeddings → store in vector database → embed user query → find similar embeddings → build final prompt","Build final prompt → chunk text → generate embeddings → store in vector database","Store in vector database → chunk text → embed user query → generate embeddings","Generate embeddings → build final prompt → chunk text → store in vector database"], 1,
    "Chunk→Embed→Store→Embed query→Find→Prompt.")
add("6.4", "What is normalization doing to an embedding vector?",
    ["Removing all negative numbers","Scaling the vector so its magnitude equals 1.0","Converting the vector into text again","Reducing the vector to a single number","Sorting the vector's values from smallest to largest"], 1,
    "Escala o vetor para magnitude 1.0.")
add("6.4", "In the worked example, why does the software engineering chunk end up as the best match for the user's query?",
    ["It was stored first in the vector database","It has the highest cosine similarity to the query embedding","It is alphabetically first","The medical research chunk was deleted","It's the shortest chunk"], 1,
    "Maior cosine similarity com a query.")
add("6.4", "What does a cosine similarity close to 0 indicate between two embeddings?",
    ["They are nearly identical in meaning","They are perpendicular — essentially no relationship","They are completely opposite in meaning","One of the embeddings is invalid","The vectors weren't normalized correctly"], 1,
    "Perto de 0 = perpendicular, sem relação.")
add("6.4", "How is cosine distance calculated from cosine similarity?",
    ["cosine similarity squared","1 − cosine similarity","cosine similarity × 2","The absolute value of cosine similarity","1 / cosine similarity"], 1,
    "1 menos a similaridade.")

add("6.5", "What is the correct order of the five-step RAG implementation in this lesson?",
    ["Search store → chunk text → generate embeddings → embed query → create vector store","Chunk text → generate embeddings → create vector store → embed user query → search store","Create vector store → embed user query → chunk text → generate embeddings → search store","Generate embeddings → search store → chunk text → create vector store → embed user query","Embed user query → search store → chunk text → generate embeddings → create vector store"], 1,
    "Chunk→Embed→Store→Embed query→Search.")
add("6.5", "What does store.add_vector(embedding, {\"content\": chunk}) store alongside the embedding?",
    ["Nothing else — only the embedding is stored","The original chunk text, so it can be returned later","The user's question","The API key used to generate the embedding","A cosine similarity score"], 1,
    "Guarda o texto original do chunk.")
add("6.5", "Why is it important to store the original chunk text alongside its embedding?",
    ["It speeds up the embedding model","Because querying the vector store alone only returns numbers, not usable text","It's required by the embedding API","It reduces the size of the vector database","It removes the need for normalization"], 1,
    "Só números não são úteis sem o texto original.")
add("6.5", "In the example query results, what does a lower distance value mean?",
    ["Lower relevance to the query","Higher similarity to the query","The chunk is shorter","The chunk was stored earlier","The embedding failed to normalize"], 1,
    "Distância menor = mais similar.")
add("6.5", "What does store.search(user_embedding, 2) return?",
    ["The 2 chunks stored first in the database","The 2 most similar chunks to the query, with their distances","A single merged chunk of exactly 2 sentences","The 2 chunks with the lowest word count","2 randomly selected chunks"], 1,
    "Os 2 chunks mais similares, com distâncias.")

add("6.6", "Why might semantic search alone fail to find a specific incident ID?",
    ["Semantic search can't process numbers","It optimizes for conceptual similarity, so it can miss or over-include content based on meaning rather than exact terms","Semantic search always returns zero results for IDs","Semantic search requires a BM25 index first","The vector database doesn't support text at all"], 1,
    "Otimiza por similaridade conceitual, não termo exato.")
add("6.6", "What does BM25 stand for/represent in this lesson?",
    ["A type of embedding model","A popular algorithm for lexical search in RAG systems","A vector database provider","A chunking strategy","A cosine similarity threshold"], 1,
    "Algoritmo popular de busca lexical.")
add("6.6", "In BM25, how are terms weighted?",
    ["All terms get equal weight","Terms that appear less frequently across documents get higher importance","Longer terms always get higher importance","Only terms in the title get weighted","Terms are weighted alphabetically"], 1,
    "Termos raros pesam mais.")
add("6.6", "What is the first step BM25 performs on a search query?",
    ["Generating an embedding","Tokenizing the query into individual terms","Normalizing the vector","Calling the vector database","Ranking documents by length"], 1,
    "Tokeniza a query em termos.")
add("6.6", "What is the benefit of a hybrid search strategy over semantic search alone?",
    ["It removes the need for chunking","It combines conceptual matching with exact term matching for better overall accuracy","It eliminates the need for a vector database","It always returns fewer results","It replaces cosine similarity with word count entirely"], 1,
    "Combina correspondência conceitual e literal.")

add("6.7", "What makes it easy to combine VectorIndex and BM25Index into a single Retriever?",
    ["They both run on the same server","They share nearly identical APIs (add_document() and search())","BM25Index is a subclass of VectorIndex","They both use cosine similarity internally","They were trained on the same embedding model"], 1,
    "APIs quase idênticas entre os dois índices.")
add("6.7", "Why can't you just concatenate the result lists from VectorIndex and BM25Index?",
    ["The lists are always the same length","Each method uses a different scoring system, so scores aren't directly comparable","Concatenating lists is not supported in Python","BM25Index never returns more than one result","VectorIndex results are always better and should be used alone"], 1,
    "Sistemas de pontuação diferentes, não comparáveis direto.")
add("6.7", "In the RRF formula 1/(k + rank), what happens to a document's score contribution as its rank number gets higher (worse)?",
    ["The score contribution increases","The score contribution decreases","The score becomes negative","The rank is ignored entirely","The formula becomes undefined"], 1,
    "Rank pior (maior) → contribuição menor.")
add("6.7", "In the worked example, why does Section 2 end up with the highest final RRF score?",
    ["It was the only chunk returned by both indexes","It ranked well (had good rank positions) in both VectorIndex and BM25Index","It has the most characters","It was manually pinned to first place","BM25Index ignored it entirely"], 1,
    "Bom ranking nos dois índices simultaneamente.")
add("6.7", "According to the lesson, how could a new search method (e.g. graph-based search) be added to the Retriever?",
    ["It's not possible without rewriting the Retriever class","By implementing the same SearchIndex interface (add_document() and search())","By replacing BM25Index entirely","Only Anthropic can add new index types","By changing the RRF formula's constant k to a negative number"], 1,
    "Basta implementar a mesma interface SearchIndex.")

# Section 7 - Features of Claude (2 lessons x6)
add("7.1", "What is extended thinking best described as?",
    ["A way to fine-tune Claude on custom data","A feature that gives Claude time to reason through a problem before the final answer, shown as a separate thinking block","A tool that lets Claude browse the web","A caching mechanism for repeated prompts","A way to reduce the number of tokens in a response"], 1,
    "Tempo de raciocínio antes da resposta final, em bloco separado.")
add("7.1", "Which of the following is NOT listed as a benefit of extended thinking?",
    ["Better reasoning on complex tasks","Increased accuracy on difficult problems","Transparency into Claude's thought process","Lower latency on every request","Often results in higher quality responses"], 3,
    "Menor latência NÃO é benefício — é o contrário (mais latência).")
add("7.1", "According to the lesson, when should a developer consider enabling extended thinking?",
    ["On every single API call, by default","Only for creative writing tasks","After running prompt evaluations without thinking and finding accuracy still isn't sufficient once the prompt is already optimized","Only when the user explicitly types \"think\" in the prompt","Never — it should be avoided in production"], 2,
    "Só depois de avaliar sem thinking e ver que não basta.")
add("7.1", "What does the signature field in a thinking block verify?",
    ["That the user's API key is valid","That the model used was Claude 4","That the thinking text is exactly what Claude generated and was not modified","That the response fits within max_tokens","That the thinking block was translated correctly"], 2,
    "Verifica que o texto do raciocínio não foi alterado.")
add("7.1", "What triggers a redacted_thinking block instead of a normal thinking block?",
    ["The thinking_budget is set too low","The user asks a factual question","Claude's internal reasoning gets flagged by safety systems","The max_tokens parameter is missing","The request does not include any tools"], 2,
    "Sinalização por sistemas de segurança.")
add("7.1", "In the redacted_thinking case, what happens to the underlying reasoning content?",
    ["It is permanently deleted and cannot be reused","It is kept in encrypted form so it can be passed back to Claude without losing context","It is shown to the developer but hidden from the end user","It is converted into a normal text block automatically","It is replaced with a generic placeholder message with no relation to the original reasoning"], 1,
    "Fica criptografado, preservando o contexto.")

add("7.2", "What is the maximum number of images allowed across all messages in a single request?",
    ["10","20","50","100","There is no limit"], 3,
    "Até 100 imagens por requisição.")
add("7.2", "When sending multiple images in a single request, what is the max height/width per image?",
    ["2000px","5000px","8000px","10000px","There is no size limit for multiple images"], 0,
    "2000px quando há múltiplas imagens (8000px se for só uma).")
add("7.2", "How is the token cost of an image calculated?",
    ["A flat 1000 tokens per image regardless of size","(width px × height px) / 750","(width px + height px) / 2","Based on file size in MB only","Images do not consume tokens"], 1,
    "(largura × altura) / 750.")
add("7.2", "Why did the simple prompt \"How many marbles are in this image?\" return an incorrect count?",
    ["Because the image exceeded the 5MB size limit","Because Claude cannot process images with more than one color","Because a simple, unstructured prompt often leads to poor results on precise visual tasks","Because the image was sent as a URL instead of base64","Because counting tasks are not supported by the vision API"], 2,
    "Prompt simples e sem estrutura → resultado impreciso.")
add("7.2", "According to the lesson, which techniques improve Claude's accuracy on image analysis tasks?",
    ["Sending only the image with no text block at all","Detailed guidelines and analysis steps, one-shot/multi-shot examples, and breaking tasks into smaller steps","Always resizing images to exactly 8000px","Repeating the same question multiple times in the same message","Removing all context and asking the shortest possible question"], 1,
    "Guidelines/steps detalhados + exemplos + decomposição.")
add("7.2", "In the fire risk assessment example, what is the final output of the structured prompt?",
    ["A raw list of every tree detected in the image","A one-sentence summary per analysis step, ending in a numerical Fire Risk Rating from 1 to 4","A base64-encoded copy of the satellite image","A yes/no answer on whether to send an inspector","The exact GPS coordinates of the residence"], 1,
    "Resumo por etapa + nota final de 1 a 4.")

print("quiz2 total (sections 1-7):", len(quiz2))
with open("/home/claude/quiz2_full.json", "w", encoding="utf-8") as f:
    json.dump(quiz2, f, ensure_ascii=False, indent=1)

# Synthetic supplementary quiz for sections 8-10 (not covered by extracted repo material)
add("8", "Dentro da seção de MCP do curso da API, quais são os três primitivos centrais do protocolo cobertos (tools, resources e...)?",
    ["Prompts","Webhooks","Cron jobs","Databases","Containers"], 0,
    "Os três primitivos do MCP são tools, resources e prompts.", source="synth")
add("8", "Para inspecionar visualmente um servidor MCP durante o desenvolvimento, qual ferramenta a lição menciona?",
    ["O debugger do Python","O MCP Inspector","O Claude Workbench","O validador de Skills","O git diff"], 1,
    "O \"server inspector\" citado no syllabus é o MCP Inspector.", source="synth")
add("8", "Um cliente MCP, na arquitetura do protocolo, é responsável por:",
    ["Definir os tools do servidor","Consumir os serviços expostos por um servidor MCP","Treinar o modelo Claude","Armazenar embeddings","Substituir o system prompt"], 1,
    "O cliente consome (consome/chama) o que o servidor expõe.", source="synth")
add("9", "Nesta visão geral de \"Apps Anthropic\", o que complementa e estende as capacidades do Claude Code, segundo o syllabus?",
    ["Servidores MCP","O validador de Skills","O grader de código","A temperature","O BM25"], 0,
    "\"Aprimoramentos com servidores MCP\" é o tópico citado.", source="synth")
add("9", "Qual destas NÃO é uma etapa citada na configuração inicial do Claude Code segundo esta seção introdutória?",
    ["Configuração do Claude Code","Claude Code em ação (visão geral)","Aprimoramentos com servidores MCP","Definição de embeddings de texto","Todas são citadas"], 3,
    "Embeddings pertence à seção de RAG, não à de Claude Code.", source="synth")
add("10", "Qual padrão de workflow divide uma entrada entre caminhos diferentes com base em uma classificação inicial?",
    ["Chaining","Parallelization","Routing","RAG","BM25"], 2,
    "Routing = classificar e direcionar para o caminho certo.", source="synth")
add("10", "Qual padrão de workflow roda sub-tarefas simultaneamente e depois agrega os resultados?",
    ["Chaining","Parallelization","Routing","Prompt caching","Semantic chunking"], 1,
    "Parallelization = execução simultânea + agregação.", source="synth")
add("10", "A diferença central entre um \"workflow\" e um \"agente\", segundo esta seção, é que o agente:",
    ["Nunca usa ferramentas","Segue sempre um caminho fixo e pré-definido","Decide dinamicamente os próprios passos, inspecionando o ambiente","É sempre mais barato que um workflow","Não pode ser avaliado"], 2,
    "Agentes decidem dinamicamente; workflows seguem caminho fixo.", source="synth")
add("10", "Por que a arquitetura agêntica é o domínio de maior peso na prova Claude Certified Architect – Foundations?",
    ["Porque é o único domínio com questões","Porque cobre orquestração, coordenação multi-agente e confiabilidade — o núcleo do papel de arquiteto","Porque não exige conhecimento de Claude Code","Porque substitui o domínio de prompt engineering","Porque é o domínio mais fácil de estudar"], 1,
    "27% do exame — o maior peso, cobrindo orquestração e confiabilidade.", source="synth")

print("quiz2 total incl synthetic:", len(quiz2))
with open("/home/claude/quiz2_full.json", "w", encoding="utf-8") as f:
    json.dump(quiz2, f, ensure_ascii=False, indent=1)
