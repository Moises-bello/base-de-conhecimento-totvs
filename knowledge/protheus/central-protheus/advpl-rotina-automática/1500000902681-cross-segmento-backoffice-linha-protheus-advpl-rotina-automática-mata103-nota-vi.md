---
article_id: 1500000902681
category: ADVPL - Rotina Automática
content_hash: 525d9985b8760fde10f2a56a2246cde8c3e4c92ff7817e63e0cddae0cdbef1ad
fetched_at: '2026-06-28T22:40:24.166266+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina Automática - MATA103
  - Nota vinculada a pedido de compras.
type: support-article
updated_at: '2021-12-29T19:05:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000902681-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-Autom%C3%A1tica-MATA103-Nota-vinculada-a-pedido-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**  
Como vincular pedido de compras tipo normal em uma nota através da Rotina Automática MATA103?

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17

**Solução**  
O vinculo é efetuado ao informar Número do Pedido de Compras (D1\_PEDIDO) e Item do Pedido de Compras (D1\_ITEMPC )

```
          aItem := {}  
          aadd(aItem,{"D1_ITEM" ,StrZero(nX,4) ,NIL})  
          aadd(aItem,{"D1_COD" ,PadR("01",TamSx3("D1_COD")[1]),NIL})  
          aadd(aItem,{"D1_UM" ,"KG"                           ,NIL})  
          aadd(aItem,{"D1_LOCAL" ,"01"                        ,NIL})   
           
          aadd(aItem,{"D1_PEDIDO"       ,"000009"             ,NIL})  
          aadd(aItem,{"D1_ITEMPC"       ,"0001"               ,NIL})  
         
          aadd(aItem,{"D1_QUANT" ,1                           ,NIL})  
          aadd(aItem,{"D1_VUNIT" ,7508.35                     ,NIL})  
          aadd(aItem,{"D1_TOTAL" ,7508.35                     ,NIL})  
          aadd(aItem,{"D1_TES" ,"002"                         ,NIL})
```

**Observação:**  
O Pedido de Compra vinculado deve estar informado antes dos dados de quantidade, valor unitário, Valor Total e TES, caso contrario serão carregados os dados informados no pedido de compras.

**Saiba mais:**  
**[MATA103](https://tdn.totvs.com/pages/viewpage.action?pageId=235592777)**
