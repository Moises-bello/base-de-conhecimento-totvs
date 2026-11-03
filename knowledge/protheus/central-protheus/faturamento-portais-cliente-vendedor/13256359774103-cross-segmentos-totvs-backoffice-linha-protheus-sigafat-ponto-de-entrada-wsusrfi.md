---
article_id: 13256359774103
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 4d47d2491d32da360d0ea18261e1a52219aa6b12b68af2618c026c82ac42a61a
fetched_at: '2026-06-28T22:38:24.094610+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  WSUSRFIELD
type: support-article
updated_at: '2023-03-21T18:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256359774103-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-WSUSRFIELD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **WSUSRFIELD - Reconhece os campos fora do padrão no sistema**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Este Ponto de Entrada tem por objetivo **reconhecer os campos do sistema** que não estão configurados como padrão no Portal do Fornecedor (campos de usuário).  
  
**Exemplo**

```
#INCLUDE "RWMAKE.CH"  
  
User Function WsUsrField()  
  
    Local cAlias := PARAMIXB[1]  
    Local aReturn := {}  
  
    Do Case  
        Case cAlias == "SC5"  
            aAdd(aReturn,"C5_TESTE") //Campo customizado adicionado do cabeçalho do pedido SC5     
        Case cAlias == "SC6"  
            aAdd( aReturn,"C6_TESTE") //Campo customizado adicionado do item do pedido SC6  
    EndCase  
  
Return aReturn
```

**Saiba Mais**

* **[WSUSRFIELD - Reconhece os campos fora do padrão no sistema](https://tdn.totvs.com/x/9dtc)**
* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada PEV044](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256359193239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-PEV044)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como adicionar campos no Portal do Vendedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256360067991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-adicionar-campos-no-Portal-do-Vendedor)**
