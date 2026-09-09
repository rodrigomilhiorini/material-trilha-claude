# Material Trilha Claude — Certificação Anthropic (CCAR-F)

Material de estudo bilíngue (português/inglês) para a certificação **Claude Certified Architect – Foundations (CCAR-F)**, organizado por Rodrigo Milhiorini (Faiston).

Página publicada e sempre atualizada: https://claude.ai/code/artifact/4d4e0a65-9b30-4f84-b364-3f4190a94d97

## O que tem aqui

- **`material-trilha.html`** — o material completo, para abrir direto no navegador (funciona offline, sem servidor). Todo o conteúdo é bilíngue: português sempre à esquerda, inglês sempre à direita (itálico). Tema escuro por padrão, com botão para alternar para claro.
- **7 módulos**: Introdução às Habilidades de Agente, Construindo com a API Claude (com addendum "Claude em outras nuvens" — Vertex AI e Amazon Bedrock), Introdução ao Model Context Protocol, Claude Code em Ação, Fundamentos de Arquitetura Claude, AI Fluency: Framework e Fundamentos, e Claude 101.
- **Simulados completos**: 68 questões interativas organizadas em 9 áreas — resposta correta fica oculta até você responder, e sinaliza se você acertou ou errou.
- **347 questões por aula + 68 de simulado**, todas com gabarito/dica comentado nos dois idiomas.
- **92 termos de glossário**, **164 palavras-chave**, pontos de atenção para a prova em cada módulo.

## Resumos em áudio

Os áudios com os resumos falados de cada módulo **não ficam dentro do repositório** (são arquivos grandes, entre 37MB e 56MB cada). Eles estão disponíveis para download na aba **[Releases](../../releases)** deste repositório:

- `CPN_Aula1_Habilidades_de_Agente.m4a`
- `CPN_Aula2_API_Claude.m4a`
- `CPN_3___Protocolo_de_Contexto_do_Modelo.m4a`
- `CPN_4___Claude_Code_em_acao.m4a`
- `CPN_5___Revisao_Final_e_Glossario.m4a`
- `Os_bastidores_técnicos_da_API_Claude.m4a`
- `Traduções_absurdas_no_material_da_Anthropic.m4a`
- `Workflows_ou_Agentes_na_arquitetura_do_Claude.m4a`

Se algum áudio novo for adicionado, publique uma nova versão em Releases em vez de commitar o arquivo direto no git.

## Estrutura do repositório

```
material-trilha-claude/
├── material-trilha.html   ← abra este arquivo para estudar
├── data/
│   └── DATA_final3.json   ← todo o conteúdo estruturado (o material.html só renderiza isto)
├── src/
│   ├── skeleton.html      ← estrutura/CSS da página, sem os dados
│   ├── render.js          ← lógica de renderização (JS puro, sem dependências)
│   └── build_pipeline/    ← scripts Python que geraram data/DATA_final3.json, na ordem em que foram executados
└── sources/
    ├── Claude_Architecture_Blueprint.pptx        ← guia visual de arquitetura (fonte do Módulo 5)
    ├── guia-de-simulados-anthropic.docx          ← guia de simulados original (46 questões)
    ├── guiasimuladoscertificacaoccaf.docx        ← segundo guia de simulados (8 questões novas incorporadas)
    └── guiasimuladosarquiteturaccarfv2.docx      ← terceiro guia de simulados, "v2" (14 questões novas incorporadas + 1 duplicada descartada)
```

## Módulos 6 e 7 — origem do conteúdo

Os módulos **AI Fluency: Framework e Fundamentos** (Módulo 6) e **Claude 101** (Módulo 7), além do addendum "Claude em outras nuvens" dentro do Módulo 2, foram extraídos dos cursos oficiais do Anthropic Partner Network (Skilljar), a partir da página [Claude Certified Architect Foundations — Prep Courses](https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses):

- **AI Fluency: Framework & Foundations** (Prof. Rick Dakan e Prof. Joseph Feller, licença CC BY-NC-SA 4.0) — 15 aulas em texto, extraídas na íntegra.
- **Claude 101** — 14 aulas em texto, extraídas na íntegra.
- **Claude on Google Cloud** (93 aulas) e **Claude with Amazon Bedrock** (83 aulas) — investigados e considerados ~95% duplicados do Módulo 2 (mesma ementa de API Claude) e majoritariamente em vídeo sem transcrição disponível. Por isso, em vez de virarem módulos completos, apenas o conteúdo genuinamente novo (configuração de acesso via Vertex AI e via Bedrock) foi incorporado como addendum ao Módulo 2. A parte de Vertex AI vem de uma aula em texto real do curso ("Vertex AI Setup"); a parte de Bedrock foi sintetizada com base em conhecimento geral consolidado sobre AWS Bedrock, já que o curso não tinha aula equivalente em texto — isso está sinalizado no próprio material com a etiqueta <span>complementar</span>.

Os scripts em `src/build_pipeline/` têm caminhos de arquivo fixos da sessão original em que foram gerados — servem como documentação de como o conteúdo foi montado (extração de docx/pptx, tradução, geração de quiz), não para rodar direto sem ajustar os caminhos.

## Como atualizar

1. Edite `data/DATA_final3.json` (ou os scripts em `src/build_pipeline/`, se preferir regenerar por lá).
2. Junte `src/skeleton.html` + `<script type="application/json" id="data-json">` com o conteúdo de `data/DATA_final3.json` + `<script>` com `src/render.js`, nessa ordem, para gerar um novo `material-trilha.html`.
3. Abra o `material-trilha.html` resultante no navegador para conferir.

## Fontes usadas

- [Claude Partner Network Learning Path](https://anthropic-partners.skilljar.com/page/claude-partner-network-learning-path) (trilha oficial)
- [Guia de estudos em português (comunidade)](https://lulippe4-hub.github.io/guia-estudos-anthropic/)
- [Repositório claude-certification (comunidade)](https://github.com/MateusBurkle/claude-certification)
- Guia visual de arquitetura e guia de simulados fornecidos pelo autor (`sources/`)

Questões e materiais marcados como "banco real" vêm do repositório da comunidade acima; "complementar" foi elaborado com base na ementa oficial; "guia de simulados" vem do docx em `sources/`.

---

*Material pessoal de estudo — não é material oficial da Anthropic nem da Faiston.*
