---
article_id: 15441677840151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3c19450ad49dc27690a71f2e17395c0735f80d35c7f0e8945ad60da062dc158f
fetched_at: '2026-06-28T22:38:42.781337+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MT460EST
type: support-article
updated_at: '2023-06-20T14:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15441677840151-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MT460EST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15441663428503) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MT460EST - Antes do estorno do SC9.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de Entrada é chamado **antes do estorno do SC9**, o arquivo posicionado no momento é o SC9.  
Se retornar **.T.** ou **NIL**(nulo), indica que **continua** com o estorno da liberação dos itens do Pedido de Vendas. Se retornar **.F.**, indica que **não continua** com o estorno.

**Exemplo**

```
#INCLUDE "TOTVS.CH"  
  
User Function MT460EST()  
  
    Local lRet := .T. // .T. = Estorna SC9 / .F. = Não Estorna SC9  
  
    MsgAlert("Passou pelo Ponto de Entrada MT460EST")  
  
Return lRet
```

**Saiba Mais**

**[MT460EST - Antes do estorno do SC9](https://tdn.totvs.com/x/d4Vn)**
