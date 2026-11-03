---
article_id: 360050095334
category: ADVPL - Classe e Função
content_hash: 93e4f1a959640b995576e849c861ff593b89c94356797c543e0179a81fe75275
fetched_at: '2026-06-28T22:40:20.488871+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Limite de dado
  numérico em AdvPL
type: support-article
updated_at: '2022-01-11T20:59:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050095334-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Limite-de-dado-num%C3%A9rico-em-AdvPL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe alguma solução para salvar um campo tipo numérico com um valor maior que 15 posições?   
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**A linguagem ADVPL entende apenas os 15 primeiros dígitos, esse limite é interno do *Application Server* devido o tipo de dado utilizado.  
Campos maior que 15 posições, podem ser registrados convertendo para o tipo string.  
  
**Saiba mais**[Limite de dado numérico em AdvPL](https://tdn.totvs.com/pages/viewpage.action?pageId=6063071)
