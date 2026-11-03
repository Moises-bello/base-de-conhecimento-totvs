---
article_id: 8350409075223
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 09b0121873c8236e95291c95835322148dff9ec841ee0adf15ca2d1de07dc351
fetched_at: '2026-06-28T22:38:42.429275+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MAAVCRPR
type: support-article
updated_at: '2022-12-27T17:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8350409075223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MAAVCRPR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MAAVCRPR - Liberação de Crédito.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Este ponto de entrada pertence à rotina de **avaliação de crédito de clientes**, MaAvalCred() – FATXFUN(). Ele permite que, após a avaliação padrão do sistema, o usuário possa fazer a sua própria.

//ParamIxb[1]= Código do cliente

//ParamIxb[2]= Código da filial

//ParamIxb[3]= Valor da venda

//ParamIxb[4]= Moeda da venda

//ParamIxb[5]= Considera acumulados de Pedido de Venda do SA1

//ParamIxb[6]= Tipo de crédito (“L” - Código cliente + Filial; “C” - código do cliente)

//ParamIxb[7]= Indica se o credito será liberado (Lógico)

//ParamIxb[8]= Indica o código de bloqueio do credito (Caracter)  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
  
User Function MAAVCRPR()  
  
    Local aParam := ParamIXB  
    Local lRet := aParam[7]  
  
    //Desenvolvimento/regra de negócio a ser desenvolvida pelo cliente, abaixo contém as informações de cada parâmetro  
    //ParamIxb[1]= Código do cliente  
    //ParamIxb[2]= Código da filial  
    //ParamIxb[3]= Valor da venda  
    //ParamIxb[4]= Moeda da venda  
    //ParamIxb[5]= Considera acumulados de Pedido de Venda do SA1  
    //ParamIxb[6]= Tipo de crédito (“L” - Código cliente + Filial; “C” - código do cliente)  
    //ParamIxb[7]= Indica se o credito será liberado (Lógico)  
    //ParamIxb[8]= Indica o código de bloqueio do credito (Caracter)  
  
    If MsgYesNo("PE MAAVCRPR - Liberar o credito?")  
        lRet := .T.  
        Help("PE MAAVCRPR",1,"Avaliacao de credito padrão substituída, Credito Liberado")  
    EndIf  
  
Return lRet
```

**Observação:**

O ponto MAAVCRPR somente é executado caso não tenha o P.E [MAAVCRED](https://tdn.totvs.com/display/public/PROT/MAAVCRED) e **MV\_CREDCLI**=**C**.

O procedimento padrão para analise de credito via ponto de entrada é utilizar um ou outro.

**Saiba Mais: [MAAVCRPR - LIBERAÇÃO DE CRÉDITO](https://tdn.totvs.com/x/LYVn)**
