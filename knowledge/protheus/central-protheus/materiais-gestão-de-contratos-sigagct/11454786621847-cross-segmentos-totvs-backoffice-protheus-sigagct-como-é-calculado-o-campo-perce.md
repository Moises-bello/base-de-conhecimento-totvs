---
article_id: 11454786621847
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fde399e1f1d0f7fe969c496d9bad6558a29f0c9877469d5da92b5c8b65410fba
fetched_at: '2026-06-28T22:37:21.485725+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é calculado o
  campo Percentual ( CNE_PERC ) do Item em uma Medição
type: support-article
updated_at: '2023-01-05T12:19:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11454786621847-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-calculado-o-campo-Percentual-CNE-PERC-do-Item-em-uma-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como o sistema calcula o campo Percentual ( CNE\_PERC ) em uma Medição

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**Na rotina de Medição CNTA121, no campo de Percentual do Item (CNE\_PERC) é trazida a informação do percentual que esta medição que está sendo realizada (CNE\_QUANT) representa na Quantidade Solicitada (CNE\_SOLIC) do Item em questão.  
No caso, no exemplo em que a quantidade digitada da medição (CNE\_QUANT) for 1, e a quantidade solicitada (CNE\_SOLIC) do Item é 3, é trazido o valor de 33,33, referente a 1 dividido por 3 (33,33%).

***Saiba Mais:***

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
