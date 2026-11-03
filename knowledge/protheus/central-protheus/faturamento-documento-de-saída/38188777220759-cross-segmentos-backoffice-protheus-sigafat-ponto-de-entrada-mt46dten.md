---
article_id: 38188777220759
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2cccfb6205c5f899795aebe3f3991aa659b6c9c9f96863cc70eb5a7baf399a5d
fetched_at: '2026-06-28T22:38:44.121817+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de Entrada MT46DTEN
type: support-article
updated_at: '2026-02-10T12:07:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38188777220759-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-Entrada-MT46DTEN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38188748011671) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Exemplo de uso do Ponto de Entrada MT46DTEN.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.  
  
**Solução**  
O Ponto de Entrada é executado na rotina "**Documentos de Saída (MATA461)"** e no "**Pedido de Vendas (MATA410)",** permitindo definir a data de entrega no momento de preparar o **Documento de Saída**, conforme a exibição dopergunte abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38188710098199)

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'
#INCLUDE 'TOTVS.CH'

User Function MT46DTEN()

    Local dDtEntrega    := cTod("//")
    Local lMata410      := ProcName(2) == "MA410PVNFS" //Pedido de Vendas
    Local lMata461      := ProcName(2) == "MA460NOTA"  //Documento de Saída

    If lMata410 //Pedido de Vendas
        If MsgYesNo("Confirma o preenchimento customizado do parametro 'Data de entrega?'", "PE MT46DTEN")
            dDtEntrega := cTod("30/01/2026") //Data customizada
            Alert("Parametro 'Data de entrega?' foi preenchido com a data customizada") //Clicou no Sim
        Else
            Alert("Parametro 'Data de entrega?' nao foi preenchido com a data customizada") //Clicou no Não
        EndIf
    EndIf
  
    If lMata461 //Documento de Saída
        If MsgYesNo("Confirma o preenchimento customizado do parametro 'Data de entrega?'", "PE MT46DTEN")
            dDtEntrega := cTod("30/12/2027") //Data customizada
            Alert("Parametro 'Data de entrega?' foi preenchido com a data customizada") //Clicou no Sim
        Else
            Alert("Parametro 'Data de entrega?' nao foi preenchido com a data customizada") //Clicou no Não
        EndIf
    EndIf
  
Return dDtEntrega
```

**Saiba Mais**

[**PE MT46DTEN Definir data de entrega nos Documentos de Saída**](https://tdn.totvs.com/x/FyaFPQ)
