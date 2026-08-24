# Material Trilha Claude — Certificação Anthropic (CCAR-F)

Material de estudo bilíngue (português/inglês) para a certificação **Claude Certified Architect – Foundations (CCAR-F)**, organizado por Rodrigo Milhiorini (Faiston).

Página publicada e sempre atualizada: https://claude.ai/code/artifact/4d4e0a65-9b30-4f84-b364-3f4190a94d97

## O que tem aqui

- **`material-trilha.html`** — o material completo, para abrir direto no navegador (funciona offline, sem servidor). Todo o conteúdo é bilíngue: português sempre à esquerda, inglês sempre à direita (itálico). Tema escuro por padrão, com botão para alternar para claro.
- **5 módulos**: Introdução às Habilidades de Agente, Construindo com a API Claude, Introdução ao Model Context Protocol, Claude Code em Ação, e Fundamentos de Arquitetura Claude.
- **Simulados completos**: 46 questões interativas organizadas por área — resposta correta fica oculta até você responder, e sinaliza se você acertou ou errou.
- **300 questões por aula + 46 de simulado**, todas com gabarito/dica comentado nos dois idiomas.
- **61 termos de glossário**, **116 palavras-chave**, pontos de atenção para a prova em cada módulo.

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
    ├── Claude_Architecture_Blueprint.pptx   ← guia visual de arquitetura (fonte do Módulo 5)
    └── guia-de-simulados-anthropic.docx     ← guia de simulados (fonte da seção de Simulados)
```

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
