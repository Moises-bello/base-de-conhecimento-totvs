---
article_id: 4408542930839
category: Metrologia (SIGAQMT)
content_hash: cdbdcac8e51b46fe578fd5447d69819122a32ea88b44333427636167904031bd
fetched_at: '2026-06-28T22:42:24.811159+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Instrumento sem legenda
type: support-article
updated_at: '2021-09-14T19:54:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408542930839-Manufatura-Linha-Protheus-SIGAQMT-Instrumento-sem-legenda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Por quê alguns instrumentos estão sem legenda na rotina **QMTA010 - Cadastro de Instrumentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**Na rotina **QMTA010** o instrumento não terá legenda quando a data de validade da calibração registrada no campo **QM2\_VALDAF - Validade da Calibração** é exatamente igual a data base, ou seja, igual à data logada no **Protheus**.  
Por exemplo, supondo que a data que o usuário realizou a consulta é 09/09/2021 e a data de validade da calibração estivesse com a data de 08/09/2021, a legenda do instrumento ficará na cor vermelha indicando que o instrumento está descalibrado e ativo.  
Mas se a data de validade for maior do que a data de 09/09/2021, a cor da legenda deste instrumento será verde - calibrado e ativo.
