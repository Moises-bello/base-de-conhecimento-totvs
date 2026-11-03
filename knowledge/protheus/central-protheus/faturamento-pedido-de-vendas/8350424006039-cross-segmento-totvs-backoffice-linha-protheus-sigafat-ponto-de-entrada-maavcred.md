---
article_id: 8350424006039
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3404b56292e4621a12a98fa722bbaadc650558dec061122722450963de6b387c
fetched_at: '2026-06-28T22:38:42.421367+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MAAVCRED
type: support-article
updated_at: '2022-08-22T20:05:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8350424006039-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MAAVCRED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MAAVCRED - Liberação de Crédito.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Este ponto de entrada **substitui a avaliação de credito padrão** do sistema.  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
  
User Function MAAVCRED()  
  
    Local xRet := .F.       //.T. Liberado / .F. Bloqueado  
  
    If MsgYesNo("PE MAAVCRED - Liberar o credito?")  
        xRet := .T.  
        Help("PE MAAVCRED",1,"Avaliacao de credito padrao substituida, Credito Liberado")  
    EndIf  
  
    If xRet == .F.  
        Help("PE MAAVCRED",2,"Avaliacao de credito padrao substituida, Credito Bloqueado")  
    EndIf  
  
Return xRet
```

**Saiba Mais: [MAAVCRED - LIBERACAO DE CREDITO](https://tdn.totvs.com/x/LIVn)**
