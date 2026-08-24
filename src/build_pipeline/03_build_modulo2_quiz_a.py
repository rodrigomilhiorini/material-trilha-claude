# -*- coding: utf-8 -*-
import json

quiz2 = []
def add(lesson, q, options, correct, note, source="real"):
    quiz2.append({"lesson": lesson, "q": q, "options": options, "correct": correct, "note": note, "source": source})

# Section 1 - Lesson 1 (5)
add("1", "Which Claude model offers the highest level of intelligence?",
    ["Claude Haiku","Claude Sonnet","Claude Opus","They are all equally intelligent","Claude Instant"], 2,
    "Opus é o mais inteligente da família.")
add("1", "Which model is described as the most cost-efficient and latency-optimized, and does NOT support reasoning?",
    ["Claude Opus","Claude Sonnet","Claude Haiku","All support reasoning equally","Claude Opus and Sonnet tie"], 2,
    "Haiku é o mais barato/rápido e não suporta reasoning.")
add("1", "On the intelligence-vs-cost/speed spectrum, where does Claude Sonnet sit?",
    ["At the pure intelligence end","At the pure cost/speed end","A strong balance in the middle of intelligence, cost, and speed","It is not on the spectrum","It is the slowest and most expensive"], 2,
    "Sonnet é o equilíbrio do meio.")
add("1", "A team needs to architect a large-scale software system with sustained, multi-step reasoning and can accept higher cost. Which model best fits?",
    ["Claude Haiku","Claude Sonnet","Claude Opus","Any model, cost is irrelevant","None supports architecting"], 2,
    "Arquitetura em larga escala com raciocínio sustentado = Opus.")
add("1", "For a high-volume, straightforward text-processing task where speed and low cost matter most, which model is the best default choice?",
    ["Claude Opus","Claude Haiku","The most expensive model available","Whichever has the highest latency","Reasoning-heavy Opus only"], 1,
    "Alto volume, tarefa simples = Haiku.")

# Section 2 - 7 lessons x5
add("2.1", "Why should you never call the Anthropic API directly from client-side code?",
    ["It would be too slow","The secret API key would be exposed, a serious security vulnerability","Client code cannot send HTTP requests","The API only accepts requests from mobile apps","It would use more tokens"], 1,
    "Expor a chave é uma falha de segurança grave.")
add("2.1", "Which of these is NOT one of the four essential request fields?",
    ["API Key","Model","Messages","Max Tokens","Stop Reason"], 4,
    "Stop Reason é parte da resposta, não da requisição.")
add("2.1", "What is the correct order of Claude's four processing stages?",
    ["Embedding → Tokenization → Generation → Contextualization","Tokenization → Embedding → Contextualization → Generation","Generation → Embedding → Tokenization → Contextualization","Tokenization → Contextualization → Embedding → Generation","Contextualization → Tokenization → Embedding → Generation"], 1,
    "Tokenization → Embedding → Contextualization → Generation.")
add("2.1", "During generation, how does Claude choose the next word?",
    ["It always picks the single highest-probability word","It mixes probability with controlled randomness for natural, varied responses","It picks a word at random with no probabilities","It reuses the previous word","It asks the server to choose"], 1,
    "Mistura de probabilidade com aleatoriedade controlada.")
add("2.1", "In which stage does Claude use surrounding words to resolve a token's most likely meaning?",
    ["Tokenization","Embedding","Contextualization","Generation","Usage"], 2,
    "Contextualization resolve a ambiguidade usando as palavras vizinhas.")

add("2.2", "Why should the API key be stored in a .env file instead of directly in the notebook code?",
    ["It makes the code run faster","It keeps the secret key out of your source code and out of version control","The API only accepts keys read from .env files","It reduces the number of tokens used per request","The anthropic package cannot be imported without a .env file"], 1,
    "Mantém a chave fora do código-fonte e do versionamento.")
add("2.2", "Which three parameters does client.messages.create() require?",
    ["api_key, model, temperature","model, max_tokens, messages","role, content, model","client, model, prompt","messages, temperature, top_p"], 1,
    "model, max_tokens e messages.")
add("2.2", "What happens if Claude's natural response would be longer than the max_tokens value you set?",
    ["Claude raises an error and refuses to respond","Generation simply stops once it hits that limit, even if Claude had more to say","max_tokens is ignored and Claude always finishes its thought","Claude automatically raises max_tokens for you","The request is queued until more tokens become available"], 1,
    "max_tokens é um limite de segurança, não uma meta.")
add("2.2", "In the messages list, what two keys make up each message dictionary?",
    ["\"sender\" and \"text\"","\"user\" and \"assistant\"","\"role\" and \"content\"","\"input\" and \"output\"","\"prompt\" and \"response\""], 2,
    "role e content.")
add("2.2", "After calling client.messages.create() and storing the result in message, how do you extract just the generated text?",
    ["message.text","message[\"content\"]","message.content[0].text","message.output","message.get_text()"], 2,
    "message.content[0].text.")

add("2.3", "Why does Claude have no memory of a previous exchange when you send a new, separate API request?",
    ["Claude deliberately forgets messages after 60 seconds","The Anthropic API and Claude do not store any conversation history — each request is independent","Claude only remembers the very last message you sent","Memory is disabled unless you are on a premium plan","The server caches only the first message of the day"], 1,
    "A API é stateless.")
add("2.3", "What two things must you do to maintain conversation context across multiple turns?",
    ["Increase max_tokens and lower the temperature","Manually maintain a list of messages and send the complete history with every request","Store the API key inside every message","Call a separate \"remember\" endpoint before each request","Use a different model for each turn of the conversation"], 1,
    "Manter e reenviar a lista completa de mensagens.")
add("2.3", "What is the correct order of steps in a working multi-turn flow?",
    ["Add the follow-up question, send the history, send the initial message, add the response","Send the initial user message → add Claude's reply as an assistant message → add the follow-up as a user message → send the entire history","Send the entire history first, then add a user message, then discard the history","Add an assistant message, add a user message, then discard both before sending","Send the follow-up question before the initial message"], 1,
    "Ordem: user → assistant → user → reenviar tudo.")
add("2.3", "In the helper function add_assistant_message(messages, text), what does it actually do?",
    ["It sends a new request to Claude","It appends {\"role\": \"assistant\", \"content\": text} to the messages list","It deletes the previous user message from the list","It converts the text into tokens","It prints Claude's response to the console"], 1,
    "Só faz append de um dict à lista.")
add("2.3", "What does the chat(messages) helper function return?",
    ["The full response object, including all metadata","A new, empty messages list","The generated text — message.content[0].text","The role of the most recent message","Nothing; it only prints the response"], 2,
    "Retorna só o texto gerado.")

add("2.4", "What is the main purpose of a system prompt?",
    ["To increase the maximum number of tokens Claude can generate","To give Claude guidance on how to respond, shaping its tone, style and approach","To store the conversation history so Claude remembers previous turns","To authenticate the request in place of the API key","To translate the user's question into English before sending it"], 1,
    "Orienta como responder, não o que responder.")
add("2.4", "How is a system prompt passed to the API?",
    ["As a message with role \"system\" appended to the messages list","As a plain string passed to create() in its own \"system\" parameter","As a separate request made before the main one","As a field inside the user message's content","As an environment variable named SYSTEM_PROMPT"], 1,
    "Parâmetro system separado, string simples.")
add("2.4", "In the math tutor example, which behaviour does the system prompt try to PREVENT?",
    ["Giving the student hints before the full solution","Walking the student through the problem step by step","Immediately giving a direct answer to the student's question","Showing a solution to a similar problem as an example","Asking the student a guiding question"], 2,
    "Impede a resposta direta imediata.")
add("2.4", "Why does the flexible chat function add the system key conditionally, inside an if statement?",
    ["Because system prompts are billed separately and must be opted into","Because Claude's API does not accept system=None, so the key must be omitted when no prompt is given","Because the system parameter can only be used on the very first request","Because Python dictionaries cannot hold more than three keys","Because the system prompt must always be added after the response is returned"], 1,
    "A API não aceita system=None.")
add("2.4", "In the flexible chat function, what does **params do in client.messages.create(**params)?",
    ["It converts the dictionary into a list of messages","It unpacks the dictionary into keyword arguments for the create() call","It multiplies the max_tokens value by two","It marks the parameters as optional so the API can ignore them","It sends the parameters as a raw JSON string instead of keyword arguments"], 1,
    "Desempacota o dict como kwargs.")

add("2.5", "What are the three key steps in Claude's text generation process?",
    ["Embedding, Contextualization, Generation","Tokenization, Prediction, Sampling","Request, Response, Retry","Encoding, Decoding, Formatting","Prediction, Validation, Sampling"], 1,
    "Tokenization, Prediction, Sampling.")
add("2.5", "What is temperature?",
    ["An integer between 1 and 100 that sets the maximum response length","A decimal value between 0 and 1 that influences the token selection probabilities","A setting that chooses which model version handles the request","The number of tokens Claude processes per second","A flag that turns the system prompt on or off"], 1,
    "Decimal 0-1 que influencia a seleção do próximo token.")
add("2.5", "What happens at a temperature near 0?",
    ["Claude distributes probability evenly across all candidate tokens","Claude becomes very deterministic and almost always picks the highest-probability token","Claude stops generating after a single token","Claude ignores the messages list entirely","Claude produces its most creative and varied output"], 1,
    "Perto de 0 = determinístico.")
add("2.5", "Which temperature range is most appropriate for data extraction and coding assistance?",
    ["0.0 - 0.3","0.4 - 0.7","0.8 - 1.0","1.5 - 2.0","Temperature has no effect on these tasks"], 0,
    "0.0-0.3 para tarefas factuais/código.")
add("2.5", "In the updated chat function, how is temperature added to the request?",
    ["It is appended to the messages list as its own message","It is included as \"temperature\": temperature in the params dictionary","It must be set inside the system prompt text","It is passed only when it is different from None, inside an if statement","It is configured once in the .env file and never passed to create()"], 1,
    "Vai direto no dict de params, sempre (não é condicional como system).")

add("2.6", "What user experience problem does response streaming solve?",
    ["Responses exceed the max_tokens limit and get cut off","Responses can take 10-30 seconds, leaving users staring at a loading spinner","The API key is exposed to the client","Claude forgets the conversation history between turns","The model picks low-probability tokens too often"], 1,
    "Resolve a espera de 10-30s sem feedback.")
add("2.6", "Which stream event type contains the actual generated text?",
    ["MessageStart","ContentBlockStart","ContentBlockDelta","MessageDelta","MessageStop"], 2,
    "Só ContentBlockDelta carrega texto.")
add("2.6", "How do you enable streaming on a messages.create call?",
    ["By setting temperature=0.0","By adding stream=True to the create call","By passing a system prompt that requests streaming","By calling create() once per chunk you want back","By setting max_tokens to a very small value"], 1,
    "stream=True habilita.")
add("2.6", "How many requests to Claude do all the streamed events belong to?",
    ["One request per event","One request per content block","A single request — all the events are parts of it","Two requests: one for the initial response, one for the text","It depends on the temperature setting"], 2,
    "Uma única requisição.")
add("2.6", "What does stream.get_final_message() give you?",
    ["Only the last text chunk that was streamed","The complete assembled message object, after the stream has been consumed","A new empty message ready for the next turn","The number of events that were received","Nothing — it only closes the connection"], 1,
    "A mensagem completa montada.")

add("2.7", "What problem does this lesson's technique solve?",
    ["Claude generates JSON that is syntactically invalid","Claude wraps generated content in markdown fences and adds explanatory text","Claude cannot generate JSON at all without a system prompt","Claude forgets the conversation history between requests","Claude takes too long to generate a response"], 1,
    "Resolve o embrulho em markdown + explicação.")
add("2.7", "What is assistant message prefilling?",
    ["Sending the same user message twice to reinforce the instruction","Adding an assistant message to the list yourself, so Claude continues from it","Setting temperature to 0.0 so the output is deterministic","Caching Claude's previous response on your server","Passing the desired output format inside the system parameter"], 1,
    "Você mesmo adiciona a mensagem assistant.")
add("2.7", "In the example, what are the prefill and the stop sequence?",
    ["Prefill \"{\", stop sequence \"}\"","Prefill \"```json\", stop sequence \"```\"","Prefill \"json\", stop sequence \"end\"","Prefill \"```\", stop sequence \"```json\"","There is no prefill — only a stop sequence is used"], 1,
    "```json abre, ``` fecha/para.")
add("2.7", "What happens when Claude tries to close the code block?",
    ["Claude keeps going and adds an explanation after the fence","The stop sequence matches and generation immediately ends","The request fails with an error","The closing fence is returned but the JSON is discarded","Claude restarts the response from the beginning"], 1,
    "A stop sequence encerra a geração na hora.")
add("2.7", "According to the lesson, how do you apply this technique to content other than JSON?",
    ["You cannot — it only works for JSON","Identify what Claude naturally wants to wrap the content in, and use that as the prefill and stop sequence","Always prefill with \"```json\" regardless of the content type","Raise max_tokens until the commentary no longer fits","Add a stop sequence for every English word you want to avoid"], 1,
    "Generaliza para qualquer wrapper natural do conteúdo.")

# Section 3 (6 lessons x5)
add("3.1", "What is the difference between prompt engineering and prompt evaluation?",
    ["Engineering is for production, evaluation is only for development","Engineering is a set of techniques for writing better prompts; evaluation measures how well those prompts work","Engineering applies to system prompts, evaluation applies to user messages","They are two names for the same practice","Engineering is automated, evaluation is manual"], 1,
    "Engenharia escreve; avaliação mede.")
add("3.1", "Which of the following is an activity of prompt evaluation rather than prompt engineering?",
    ["Multishot prompting","Structuring the prompt with XML tags","Testing outputs against expected answers","Rewriting the prompt to be clearer","Choosing a role for the system prompt"], 2,
    "Testar contra respostas esperadas é avaliação.")
add("3.1", "What is the main risk of Option 1 — testing the prompt once and deciding it's good enough?",
    ["It uses too many tokens during development","It risks breaking in production when users provide unexpected inputs","It makes the prompt too long for the context window","It forces you to use a more expensive model","It prevents you from using a system prompt later"], 1,
    "Risco de quebrar em produção.")
add("3.1", "According to the lesson, why is Option 2 — testing a few times and fixing a corner case — still not enough?",
    ["Because Claude's responses change every time regardless of the prompt","Because users will often provide very unexpected inputs you haven't considered","Because corner cases can only be fixed by lowering the temperature","Because manual testing is not allowed in production applications","Because a prompt can only be edited a limited number of times"], 1,
    "Usuários reais trazem inputs muito mais variados.")
add("3.1", "What is the stated goal of the evaluation-first approach?",
    ["To reduce the cost of every API request","To remove the need for prompt engineering entirely","To catch problems during development rather than after users encounter them","To make Claude's outputs completely deterministic","To replace human review with a single automated test"], 2,
    "Pegar problemas antes do usuário encontrar.")

add("3.2", "What is the correct order of the five steps in a typical eval workflow?",
    ["Create an eval dataset → Draft a prompt → Feed through a grader → Feed through Claude → Repeat","Draft a prompt → Create an eval dataset → Feed through Claude → Feed through a grader → Change prompt and repeat","Draft a prompt → Feed through a grader → Feed through Claude → Create an eval dataset → Repeat","Feed through Claude → Draft a prompt → Create an eval dataset → Feed through a grader → Repeat","Create an eval dataset → Feed through Claude → Feed through a grader → Draft a prompt → Repeat"], 1,
    "Draft → Dataset → Claude → Grader → Repetir.")
add("3.2", "What does the eval dataset contain?",
    ["The scores assigned by the grader","Sample input questions that will be interpolated into the prompt template","Several finished versions of the prompt to choose from","Claude's responses from a previous evaluation run","The system prompts used by the grader"], 1,
    "Perguntas de exemplo que serão interpoladas no template.")
add("3.2", "According to the lesson, how can an eval dataset be assembled?",
    ["Only by hand, since generated questions are not valid test cases","By hand, or generated by Claude","Only by exporting real production logs","Automatically by the grader after the first run","It is provided by the Anthropic API on request"], 1,
    "À mão ou gerado pelo Claude.")
add("3.2", "What information does the grader examine when scoring?",
    ["Only Claude's answer","Only the original question","Both the original question and Claude's answer","The prompt template and the temperature setting","The token usage reported in the response"], 2,
    "Pergunta e resposta.")
add("3.2", "In the example, the scores were 10, 4 and 9. What was the resulting objective measurement?",
    ["10 — the highest score obtained","4 — the lowest score obtained","23 — the sum of all scores","7.66 — the average of the scores","8.7 — the score of the improved prompt"], 3,
    "A média (7,66) é a medida objetiva.")

add("3.3", "In this lesson's goal, what three types of output must the prompt produce?",
    ["Markdown, HTML and CSS","Python code, JSON configuration files and regular expressions","SQL queries, shell scripts and YAML files","Summaries, translations and explanations","Unit tests, documentation and diagrams"], 1,
    "Python, JSON e regex para casos AWS.")
add("3.3", "Why does the lesson suggest using Haiku to generate the eval dataset?",
    ["Haiku is the only model that can output valid JSON","Generating test data is a simple job, so a faster and cheaper model is enough","Haiku produces longer tasks than the other models","The grader requires the dataset to come from Haiku","Only Haiku supports stop sequences"], 1,
    "Tarefa simples e de alto volume → modelo mais barato.")
add("3.3", "Why does the meta-prompt include an \"Example output\" block?",
    ["To reduce the number of tokens the request consumes","To fix the exact JSON shape Claude should produce","To give Claude the answers it should generate","Because the API rejects prompts without an example","To set the temperature used for the request"], 1,
    "Fixa a forma exata do JSON esperado.")
add("3.3", "Which technique does the lesson reuse to get clean, parseable JSON from the generation call?",
    ["Setting temperature to 1.0","Response streaming with get_final_message()","Assistant message prefilling combined with a stop sequence","Sending the request several times and picking the best result","A system prompt instructing Claude to be concise"], 2,
    "Prefill + stop sequence, técnica da Seção 2.")
add("3.3", "In the updated chat() helper, how is stop_sequences handled?",
    ["It is always added to the params dictionary, like temperature","It is added to the params dictionary only if a value was provided","It is appended to the messages list as an assistant message","It replaces the system parameter when both are given","It is passed directly to json.loads()"], 1,
    "Condicional, só se fornecido — como system.")

add("3.4", "What does run_prompt() do?",
    ["Loads the dataset from disk and loops over every record","Merges one test case with the prompt template, sends it to Claude and returns the output","Grades Claude's response on a scale from 1 to 10","Averages the scores of all test cases","Saves the results into dataset.json"], 1,
    "Interpola um caso, envia e retorna a saída.")
add("3.4", "Which three keys does run_test_case() return?",
    ["\"prompt\", \"response\", \"average\"","\"task\", \"answer\", \"grade\"","\"output\", \"test_case\", \"score\"","\"input\", \"output\", \"duration\"","\"role\", \"content\", \"score\""], 2,
    "output, test_case e score.")
add("3.4", "Why is the score hardcoded to 10 at this stage?",
    ["Because 10 is the average score the prompt actually achieves","Because it is a placeholder that lets the whole pipeline be tested before grading logic exists","Because the API returns the score automatically and 10 is its default","Because scores below 10 would make the evaluation fail","Because graders can only be used on datasets created by hand"], 1,
    "Placeholder para testar o pipeline de ponta a ponta.")
add("3.4", "Why does a full evaluation run take around 30 seconds even with Haiku?",
    ["Because the grader model is slower than Haiku","Because the requests are sent one at a time, sequentially","Because dataset.json has to be re-saved after each case","Because temperature is set to 1.0","Because streaming is disabled in the chat helper"], 1,
    "Requisições sequenciais, uma por vez.")
add("3.4", "Why does Claude return verbose responses in this first run?",
    ["Because max_tokens was set too high","Because the prompt includes no formatting instructions yet","Because the dataset tasks were generated by Claude instead of by hand","Because run_eval sends the whole dataset in a single request","Because the hardcoded score of 10 encourages longer answers"], 1,
    "Sem instrução de formatação no prompt.")

add("3.5", "What are the three main types of graders?",
    ["Format, Syntax and Task graders","Code, model and human graders","Automatic, manual and hybrid graders","Strengths, weaknesses and reasoning graders","Haiku, Sonnet and Opus graders"], 1,
    "Código, modelo e humano.")
add("3.5", "Why is the Task Following criterion better suited to a model grader than a code grader?",
    ["Because code graders cannot return a number between 1 and 10","Because judging whether a response genuinely addresses a task requires flexibility that a programmatic check cannot provide","Because model graders are always cheaper than code graders","Because task following can only be measured by a human","Because code graders cannot read the original test case"], 1,
    "Exige julgamento, não checagem determinística.")
add("3.5", "What happens if the grader prompt asks only for a score, with no reasoning?",
    ["The API rejects the request as incomplete","The model tends to default to middling scores around 6","The model always returns 10","The score is returned as text instead of a number","The grader becomes faster but more accurate"], 1,
    "Sem contexto, as notas convergem para ~6.")
add("3.5", "In the grader's JSON specification, where does \"score\" appear?",
    ["First, so the model commits to a number immediately","Last, after strengths, weaknesses and reasoning","It is not part of the JSON — it is returned separately","Twice: once before and once after the reasoning","Inside the \"reasoning\" field as plain text"], 1,
    "Score por último, comprometendo-se só depois do raciocínio.")
add("3.5", "Which of these is a typical use for a CODE grader rather than a model grader?",
    ["Judging the helpfulness of a response","Assessing the safety of an answer","Validating that produced JSON has correct syntax","Deciding whether the response is complete","Measuring how well instructions were followed"], 2,
    "Sintaxe válida é checagem determinística.")

add("3.6", "Which criterion for evaluating code output is checked by the model grader rather than the code grader?",
    ["Format","Valid Syntax","Task Following","Token count","Response length"], 2,
    "Task Following exige julgamento → grader de modelo.")
add("3.6", "What does validate_python use to confirm that a string is syntactically valid Python?",
    ["exec()","compile()","ast.parse()","eval()","tokenize.tokenize()"], 2,
    "ast.parse() dentro de um try/except.")
add("3.6", "Why must every test case in the dataset include a \"format\" field?",
    ["To set the temperature for that test case","To tell the code grader which validator to run","To limit max_tokens","To choose which model generates the response","It is optional and only used for logging"], 1,
    "Indica qual validador (json/python/regex) usar.")
add("3.6", "Why is the assistant pre-fill for code grading a generic \"```code\" instead of a format-specific fence like \"```json\"?",
    ["Generic fences are shorter and save tokens","Claude ignores format-specific fences","The same prompt template is reused across Python, JSON, and Regex tasks, so the format isn't known ahead of time","Stop sequences only work with generic fences","\"```json\" is deprecated"], 2,
    "O mesmo template serve para os três formatos.")
add("3.6", "What is the actual purpose of computing a baseline (model_score + syntax_score) / 2 before editing the prompt?",
    ["To pass the eval on the first try","To have a quantitative reference point for measuring whether later prompt changes help","To determine which model to switch to","To set the dataset size","To decide the stop sequence"], 1,
    "Um baseline quantitativo para medir melhorias futuras.")

# Section 4 (5 lessons x5)
add("4.1", "In the iterative improvement cycle, which two steps repeat until you're satisfied with performance?",
    ["Set a goal and write an initial prompt","Write an initial prompt and evaluate the prompt","Apply a prompt engineering technique and re-evaluate","Evaluate the prompt and set a goal","None — each step runs exactly once"], 2,
    "Aplicar técnica e reavaliar repetem em loop.")
add("4.1", "What is the recommended starting value for max_concurrent_tasks?",
    ["1","3","10","50","There is no default guidance"], 1,
    "Comece com 3 para evitar rate limit.")
add("4.1", "Why should num_cases stay low (2–3) during development?",
    ["The API rejects larger datasets","It keeps the iteration cycle fast while you're still refining the prompt","Model graders can only grade 3 cases at a time","It reduces the max_tokens needed","It's required for the HTML report to render"], 1,
    "Mantém cada iteração rápida durante o refinamento.")
add("4.1", "What is the purpose of extra_criteria in run_evaluation()?",
    ["To set the grading temperature","To limit tokens the model can generate","To tell the grading model about requirements specific to your use case","To choose which model grades the output","To select the stop sequence"], 2,
    "Informa requisitos específicos do caso de uso ao grader.")
add("4.1", "Why is a first-attempt score like 2.3/10 considered normal?",
    ["The grading model is deliberately harsh on the first run","The baseline prompt is intentionally naive, so a low score just gives room to measure improvement","Scores under 5 aren't counted","It means the dataset was generated incorrectly","It indicates the API key lacks billing"], 1,
    "O baseline é proposital fraco, só para medir evolução.")

add("4.2", "Which part of a prompt is described as the most important part of the entire request?",
    ["The system prompt","The last sentence","The first line","The list of constraints","The examples section"], 2,
    "A primeira linha define o tom de tudo o resto.")
add("4.2", "Which pair correctly matches \"clear\" and \"direct\" to what each governs?",
    ["Clear = structure; Direct = vocabulary","Clear = simple, unambiguous language; Direct = phrasing as an instruction with an action verb","Clear = length; Direct = temperature","Clear = XML tags; Direct = examples","They mean the same thing"], 1,
    "Clear = linguagem simples; Direct = instrução com verbo de ação.")
add("4.2", "Which of these is an example of being \"direct\" rather than just \"clear\"?",
    ["Using simple vocabulary","Avoiding jargon","Starting with an action verb like \"Generate\" instead of asking a question","Keeping the prompt short","Writing in complete sentences"], 2,
    "Abrir com verbo de ação é ser direto.")
add("4.2", "What three things does \"Generate a one-day meal plan for an athlete that meets their dietary restrictions\" communicate in one line?",
    ["Temperature, model, and max_tokens","Grader, dataset, and score","The action to take, what to create, and the key constraints","System prompt, user message, and pre-fill","Goal, dataset, and extra_criteria"], 2,
    "Ação, o que criar e restrições-chave.")
add("4.2", "Applying only the clear-and-direct rewrite moved the evaluation score from:",
    ["2.32 to 3.92","0 to 10","3.92 to 7.86","1 to 2.32","5 to 8"], 0,
    "2,32 → 3,92 só com a reescrita clara e direta.")

add("4.3", "Which type of guideline controls the length, structure, and tone of Claude's output?",
    ["Process steps","Output quality guidelines","System prompts","Stop sequences","Assistant pre-fill"], 1,
    "Guidelines de qualidade de saída controlam forma/tom.")
add("4.3", "Which type of guideline should be included in almost every prompt you write?",
    ["Process steps","Output quality guidelines","Neither is needed","Only steps, never guidelines","Only for creative writing"], 1,
    "Guidelines quase sempre valem a pena.")
add("4.3", "Process steps are most useful for which of the following?",
    ["Simple factual lookups","Formatting a response as JSON","Troubleshooting, decision-making, and critical-thinking tasks","Setting the temperature parameter","Reducing token usage"], 2,
    "Steps para tarefas de raciocínio mais amplo.")
add("4.3", "Adding a guidelines block to the meal-plan prompt moved the score from:",
    ["0 to 2.32","2.32 to 3.92","3.92 to 7.86","7.86 to 10","1 to 5"], 2,
    "3,92 → 7,86 com o bloco de guidelines.")
add("4.3", "Why do professional prompts often combine guidelines with process steps?",
    ["The API requires both parameters","Guidelines give consistent format while steps ensure thorough reasoning","Steps alone always outperform guidelines","To reduce tokens used","They're the same technique with different names"], 1,
    "Guidelines = forma consistente; steps = raciocínio completo.")

add("4.4", "What core problem do XML tags solve when a prompt interpolates a lot of content?",
    ["They reduce token usage","They give Claude clear delimiters for what belongs together and what each section represents","They lower the temperature automatically","They replace the system prompt","They validate JSON syntax"], 1,
    "Delimitadores claros para o conteúdo interpolado.")
add("4.4", "In the code-and-documentation example, what made the \"Not Great\" version hard to parse?",
    ["A syntax error in the code","The documentation was in a different language","Code and documentation were mixed with no separation","It exceeded max_tokens","It used the wrong model"], 2,
    "Código e docs misturados sem separação.")
add("4.4", "Which tag name is preferable for a block of sales data?",
    ["<data>","<content>","<info>","<sales_records>","<block1>"], 3,
    "Nomes descritivos como <sales_records> são preferíveis.")
add("4.4", "Which of these is NOT listed as a situation where XML tags are most useful?",
    ["Large amounts of context or data","Mixing content types like code and documentation","Wanting extra clarity on boundaries","Prompts interpolating multiple variables","Lowering the max_tokens parameter"], 4,
    "Reduzir max_tokens não tem relação com tags XML.")
add("4.4", "What does wrapping height, weight, goal, and restrictions in <athlete_information> communicate to Claude?",
    ["They must be validated as JSON first","They're one related unit to consider together for the meal plan","They should be excluded from the response","A different model should process this section","The values are optional"], 1,
    "Sinaliza que são uma unidade relacionada.")

add("4.5", "What is the term for giving Claude a single sample input/output pair to establish a pattern?",
    ["Multi-shot prompting","One-shot prompting","Zero-shot prompting","Chain-of-thought prompting","Structured output prompting"], 1,
    "Um único exemplo = one-shot.")
add("4.5", "Why does the sarcastic tweet about \"Plan 9 from Outer Space\" require a special example rather than just a clearer instruction?",
    ["It contains a spelling error","It's sarcastic, so it reads as positive on the surface but is actually negative","It exceeds max_tokens","It contains a movie title that must be censored","It's written in a different language"], 1,
    "Sarcasmo: parece positivo mas é negativo.")
add("4.5", "Where should you look to find good candidate examples for a prompt?",
    ["Randomly generated test cases","The lowest-scoring outputs, to show what to avoid","The highest-scoring outputs from your evaluation","An unrelated prompt","The system prompt documentation"], 2,
    "Minerar as saídas com nota mais alta da sua avaliação.")
add("4.5", "What should accompany an <ideal_output> example, per best practices?",
    ["A stop sequence","A temperature value","A short explanation of why that output is ideal","The model's confidence score","A second, contradictory example"], 2,
    "Uma explicação curta do porquê é ideal.")
add("4.5", "Which combination does the lesson highly recommend for structuring examples?",
    ["Examples with a lower temperature","Examples with XML tags","Examples with a longer system prompt","Examples with extended thinking","Examples with stop sequences only"], 1,
    "Exemplos combinados com tags XML.")

print("part A quiz2 so far:", len(quiz2))
with open("/home/claude/quiz2_partA.json", "w", encoding="utf-8") as f:
    json.dump(quiz2, f, ensure_ascii=False, indent=1)
