---
article_id: 40505194044183
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 2a59993bc6b839819af73b77b5f4e438ddf35546ae1359b00d86b2a0215aa1b3
fetched_at: '2026-06-28T22:37:24.094336+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Qual a melhor forma
  de deixar obrigatória a digitação de Centro de Custos na Medição de Contratos ?
type: support-article
updated_at: '2026-05-15T18:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40505194044183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Qual-a-melhor-forma-de-deixar-obrigat%C3%B3ria-a-digita%C3%A7%C3%A3o-de-Centro-de-Custos-na-Medi%C3%A7%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40505194032151) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Qual a melhor forma de deixar obrigatório o preenchimento de Centro de Custos na Medição de Contratos ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

No momento da Medição existe a possibilidade de informação de Centro de Custos tanto no Item da Medição (Tabela CNE), como também na aba de "Rateio Contábil do item" (Tabela CNZ).

Porém, pelo conceito do módulo caso essa informação do centro de custo seja realizada em um desses locais, o outro local necessita ficar vazio,

Dessa forma, a utilização de obrigatoriedade colocando do campo de "C. Custo" de uma dessas tabelas como obrigatório no SIGACFG não é orientado ser realizado.

Sendo assim, o mais recomendado para essa utilização de obrigatoriedade da entidade contábil na medição, é por meio de customização da rotina de Medição, visto que, hora pode ser informado C. Custo no Item, e outra hora pode ser informado na Aba de Rateio, inserindo assim validações customizadas conforme a necessidade específica da empresa.

Abaixo artigo com os pontos de entrada disponíveis da rotina de medição para que se possa avaliar o  que melhor possa atender conforme a necessidade:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
