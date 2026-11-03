---
article_id: 25750796454295
category: ADVPL - Classe e Função
content_hash: 00f2be6c90c8b90d6289136f9c20b0336df8d5939dc7b6fa1bfae90cf1ffb64d
fetched_at: '2026-06-28T22:40:21.618656+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Existe função para
  retornar data e a hora de outros estados quando possui fuso horário?
type: support-article
updated_at: '2024-08-20T12:31:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25750796454295-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Existe-fun%C3%A7%C3%A3o-para-retornar-data-e-a-hora-de-outros-estados-quando-possui-fuso-hor%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25750767528343) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Existe função para retornar data e a hora de outros estados quando possui fuso horário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

A função genérica FwTimeUF tem por objetivo retornar a Data e a Hora do Protheus Server convertida para um Estado Brasileiro (Unidade Federativa), que possua GMT diferente do Estado onde o Protheus Server localiza-se.

**Exemplo**

```
user function teste03()  
  
local aRet := FwTimeUF("MT")  
   
alert(aRet[1])  
  
Return
```

**Saiba mais:**

[FwTimeUF](https://tdn.totvs.com/display/public/framework/FwTimeUF+-+Retornar+a+data+e+hora+do+Protheus+Server)
