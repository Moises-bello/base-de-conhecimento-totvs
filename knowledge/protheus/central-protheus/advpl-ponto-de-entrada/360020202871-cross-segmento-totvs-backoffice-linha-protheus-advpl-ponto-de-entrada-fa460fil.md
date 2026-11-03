---
article_id: 360020202871
category: ADVPL - Ponto de Entrada
content_hash: a1a3fd0f3a5273c9af76a1198a7923b4dbd5c856c149ab4653dfaf97b275e274
fetched_at: '2026-06-28T22:40:11.812770+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  FA460FIL
type: support-article
updated_at: '2021-12-29T19:53:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020202871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-FA460FIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Gostaria de um exemplo do ponto FA460FIL.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Exemplo de Customização

```
User Function FA460FIL()  
  LOCAL CRET := "AND E1_CLIENTE = 'CL0003' AND E1_TIPO = 'BOL'"  
  ALERT("***PASSOU NO PE FA460FIL")  
Return CRET
```

**Saiba mais**[FA460FIL](http://tdn.totvs.com/pages/viewpage.action?pageId=6071231)
