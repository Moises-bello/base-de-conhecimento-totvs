---
article_id: 13256359193239
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 9bdb1b6907fd7665e2e1ebdbf2449c462b11450faf2819b5fb9bd323305c88c5
fetched_at: '2026-06-28T22:38:24.088875+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  PEV044
type: support-article
updated_at: '2023-03-21T18:46:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256359193239-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-PEV044
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **PEV044 - Inclusão de pedidos de vendas.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada **PEV044** é utilizado na rotina **PWSV040.PRW**, para alteração dos **campos** na tela de inclusão de **pedidos de vendas**. Está localizado no Portal do Vendedor\Vendas e Distribuição\Pedidos de Venda.  
  
**Exemplo**

```
User Function PEV044()  
  
    Local nParam    := PARAMIXB[1]  
    Local aReturn   := {}  
  
    Do Case  
  
        Case nParam == 1          
  
            AAdd( aReturn, { "ORDERID", "D" } )  
            AAdd( aReturn, { "CUSTOMERCODE", "N", { "BRWCUSTOMER", ;  
            { "CCUSTOMERCODE", "CCODE" }, ;  
            { "CCUSTOMERUNIT", "CUNIT" } ;  
            }, ;  
            { "CCODE", "CUNIT", "CDESCRIPTION" } } )  
            AAdd( aReturn, "CUSTOMERUNIT" )  
            AAdd( aReturn, { "DELIVERYCUSTOMER", "N", { "BRWCUSTOMER", ;  
            { "CDELIVERYCUSTOMER", "CCODE" }, ;  
            { "CDELIVERYUNITCODE", "CUNIT" } ;  
            }, ;  
            { "CCODE", "CUNIT", "CDESCRIPTION" } } )  
            AAdd( aReturn, "DELIVERYUNITCODE" )  
            AAdd( aReturn, { "CARRIERCODE", "N", { "GETCARRIER", ;  
            { "CCARRIERCODE", "CCODE" } ;  
            }, ;  
            { "CCODE", "CDESCRIPTION" } } )  
            AAdd( aReturn, { "PAYMENTPLANCODE", "N", { "BRWPAYMENTPLAN", ;  
            { "CPAYMENTPLANCODE", "CPAYMENTPLANCODE" } ;  
            }, ;  
            { "CPAYMENTPLANCODE", "CDESCRIPTIONPAYMENTPLAN" } } )  
            AAdd( aReturn, "PRICELISTCODE" )  
            AAdd( aReturn, "DISCOUNT1" )  
            AAdd( aReturn, "DISCOUNT2" )  
            AAdd( aReturn, "DISCOUNT3" )  
            AAdd( aReturn, "DISCOUNT4" )  
            AAdd( aReturn, "BANKCODE" )  
            AAdd( aReturn, { "FINANCIALDISCOUNT", "D" } )  
            AAdd( aReturn, { "REGISTERDATE", "D" } )  
            AAdd( aReturn, "BIDNUMBER" )  
            AAdd( aReturn, { "FREIGHTVALUE", "D" } )  
            AAdd( aReturn, { "INSURANCEVALUE", "D" } )  
            AAdd( aReturn, { "ADDITIONALEXPENSEVALUE", "D" } )  
            AAdd( aReturn, { "INDEPENDENTFREIGHT", "D" } )  
            AAdd( aReturn, { "ADJUSTMENTTYPE", "D" } )  
            AAdd( aReturn, { "SALESORDERCURRENCY", "D" } )  
            AAdd( aReturn, { "NETWEIGHT", "D" } )  
            AAdd( aReturn, { "GROSSWEIGHT", "D" } )  
            AAdd( aReturn, { "REDELIVERYCARRIERCODE", "D" } )  
            AAdd( aReturn, { "FINANCIALINCREASE", "D" } )  
            AAdd( aReturn, { "INVOICEMESSAGE", "D" } )  
            AAdd( aReturn, { "STANDARDMESSAGE1", "D" } )  
            AAdd( aReturn, { "INDEMNITYVALUE", "D" } )  
            AAdd( aReturn, { "INDEMNITYPERCENTAGE", "D" } )  
            AAdd( aReturn, { "C5_TESTE", "N", 2, .T. } ) //Campo adicionado do cabeçalho do pedido SC5  
  
        Case nParam == 2  
  
            AAdd( aReturn, { "ORDERITEM", "D", 2 } )  
            AAdd( aReturn, { "PRODUCTID", "N", { "GETCATALOG", ;  
            { "CPRODUCTID", "CPRODUCTCODE" } ;  
            }, ;  
            { "CPRODUCTCODE", "CDESCRIPTION" }, 13 } )  
            AAdd( aReturn, { "PRODUCTDESCRIPTION", "N", 0, .F. } )  
            AAdd( aReturn, { "QUANTITY", "N", 3 } )  
            AAdd( aReturn, { "NETUNITPRICE", "N", 9, .T. } )  
            AAdd( aReturn, { "DISCOUNTPERCENTAGE", "N", 3 } )  
            AAdd( aReturn, { "CUSTOMERORDERNUMBER", "N", 5 } )  
            AAdd( aReturn, { "NETTOTAL", "N", 0, .F. } )  
            AAdd( aReturn, { "C6_TESTE", "N", 2, .T. } ) //Campo adicionado do item do pedido SC6  
  
    EndCase  
  
Return aReturn
```

**Saiba Mais**

* **[PEV044 - Inclusão de pedidos de vendas](https://tdn.totvs.com/x/HKhn)**
* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada WSUSRFIELD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256359774103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-WSUSRFIELD)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como adicionar campos no Portal do Vendedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13256360067991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-adicionar-campos-no-Portal-do-Vendedor)**
