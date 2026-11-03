---
article_id: 31722958744727
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: f61687464728c376e51914c2b3162fe925eec120e1c0cf773c0e9b4e0b9c1313
fetched_at: '2026-06-28T22:38:29.834660+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Limite do tamanho de campos
  caractere no Protheus
type: support-article
updated_at: '2025-04-29T19:06:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31722958744727-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Limite-do-tamanho-de-campos-caractere-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31722958716183) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o limite do tamanho de campos caractere no Protheus?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O limite de um campo do tipo "C - Caractere" no Protheus, é de 254.

Para contornar isto, o campo pode ter o tipo "M - Memo", onde aceita mais que o limite dos campos do tipo "C - Caractere" e é gravado na tabela SYP.

Outra opção também, é criar na tabela, outro campo para descrição e, combiná-los.
