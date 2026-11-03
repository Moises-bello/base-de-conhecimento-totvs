---
article_id: 4411233452183
category: Call Center - Dúvidas Gerais
content_hash: 1f05aea1c6430620b790376cc5c470ccf69b107b5780bcbdb5421df9dc31d53e
fetched_at: '2026-06-28T22:41:26.582182+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Bloqueio na
  alteração de parcelas utilizando condição de pagamento tipo 9  no Televendas
type: support-article
updated_at: '2021-10-21T18:20:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411233452183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Bloqueio-na-altera%C3%A7%C3%A3o-de-parcelas-utilizando-condi%C3%A7%C3%A3o-de-pagamento-tipo-9-no-Televendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Bloqueio na alteração de parcelas utilizando condição de pagamento tipo 9  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**Ao tentar alterar as parcelas da condição de pagamento tipo 9 no televendas depois de salvar é bloqueado conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411225143319/mceclip0.png)

Para que essa **alteração** seja possível é necessário alterar manualmente a condição de pagamento tipo 9 para outra condição de pagamento também do tipo 9, dessa forma o sistema libera a alteração:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411225274135/mceclip1.png)

Segue abaixo passo a passo do processo realizado:

![Processo-altera__o-de-condi__o-tipo-9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411225375767/Processo-altera__o-de-condi__o-tipo-9.gif)

Ponto de entrada para tratar essa rotina na chamada da tela de condição de pagamento:

[TMKCPG - Condição de pagamento  :](http://tdn.totvs.com/pages/releaseview.action?pageId=6787781) : P.E. executado antes da abertura da tela de pagamento para que se possa mudar a variável lHabilAux
