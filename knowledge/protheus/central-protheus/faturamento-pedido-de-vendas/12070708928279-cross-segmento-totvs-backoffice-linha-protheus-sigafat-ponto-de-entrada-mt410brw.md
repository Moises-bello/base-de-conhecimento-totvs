---
article_id: 12070708928279
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5dbb815b18f7aff29db1ecee2ea597798ceb6c6860bfabc3b4e2b9c6100ad503
fetched_at: '2026-06-28T22:38:42.438239+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MT410BRW
type: support-article
updated_at: '2023-01-31T17:40:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12070708928279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MT410BRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MT410BRW**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Este ponto de entrada é chamado **antes da apresentação da** ***mbrowse*** da rotina de **Pedidos de Venda**.  
  
**Exemplo**

```
#Include "rwmake.ch"  
#Include "protheus.ch"   
  
    User Function MT410BRW()      
  
    Local aAreaSC5 := SC5->(GetArea())  
    Local aAreaSA3 := SA3->(GetArea())  
    Local cCodUser := RetCodUsr()      //Retorna o código do usuário  
    Local cCodVen  := ""      
  
    SA3->(dbSetOrder(7))  
    If SA3->(dbSeek(xFilial("SA3")+cCodUser)) // Localiza Vendedor pelo código do usuário  
        cCodVen := SA3->A3_COD  
    EndIf      
  
    If !Empty(cCodVen)  
        //Filtra somente os pedidos do vendedor  
        dbSelectArea("SC5")  
        Set Filter To &("SC5->C5_VEND1 == '" + cCodVen + "'")  
    Else  
        //Mostra todos os pedidos  
        dbSelectArea("SC5")  
        Set Filter To  
    EndIf      
  
    RestArea(aAreaSC5)  
    RestArea(aAreaSA3)   
  
Return
```

**Saiba Mais**

**[Ponto de Entrada MT410BRW](https://tdn.totvs.com/x/XIVn)**
