---
article_id: 8365877440023
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: e8aab72f9e1419e875d0d730777274c6a265e5dcf76bc51f38798f23dbf89f8a
fetched_at: '2026-06-28T22:39:48.848967+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Não alterar o
  título do financeiro
type: support-article
updated_at: '2022-08-23T13:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8365877440023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-N%C3%A3o-alterar-o-t%C3%ADtulo-do-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como fazer para que quando for alterada a taxa do frete no desembaraço o título do financeiro não seja alterado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**

É possível utilizar o ponto de entrada EICFI400 ([https://tdn.totvs.com/pages/releaseview.action?pageId=51249877](https://tdn.totvs.com/pages/releaseview.action?pageId=51249877 "https://tdn.totvs.com/pages/releaseview.action?pageId=51249877")) utilizando o parâmetro 'ALTERA\_SE2' para manter a variável lAlteraSE2 := .T.. Dessa forma o título do financeiro não será alterado após a alteração da taxa no desembaraço.
