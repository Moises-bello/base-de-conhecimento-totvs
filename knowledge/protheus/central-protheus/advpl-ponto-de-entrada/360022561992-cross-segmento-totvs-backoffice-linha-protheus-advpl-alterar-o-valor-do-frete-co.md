---
article_id: 360022561992
category: ADVPL - Ponto de Entrada
content_hash: 94a24d238131febae236efb3f9251cca7a0422ea0945db665a61fcb894fe928e
fetched_at: '2026-06-28T22:40:11.631416+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar o valor
  do frete contratado no ponto de entrada MT120ISC
type: support-article
updated_at: '2022-06-21T18:02:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022561992-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-o-valor-do-frete-contratado-no-ponto-de-entrada-MT120ISC
---

**Dúvida**Ao utilizar o ponto de entrada MT120ISC para manipular os campos C7\_FRETCON, C7\_TRANSP e C7\_TRANSLJ, foi notado que os mesmos não estavam contidos nos vetores aHeader e aCols.  
Assim sendo, como fazer para manipular esses campos após escolher o contrato de parceria (F4)  na rotina de Autorização de Entrega (MATA122) por meio do ponto de entrada MT120ISC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Após efetuada a criação dos campos e aplicado o patch correto (vide SAIBA MAIS), as variáveis abaixo devem ser utilizadas no ponto de entrada MT120ISC:

1. nFreteCon para C7\_FRETCON
2. cTransLj para C7\_TRANSLJ
3. cTransp para C7\_TRANSP

**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// ALTERA DADOS VISUAIS NA MATA120 E MATA122  
User Function MT120ISC()  
    nFreteCon := 1651.21  // C7_FRETCON  
    cTransLj  := "01"     // C7_TRANSLJ  
    cTransp   := "FNC012" // C7_TRANSP   
Return (NIL)
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020101832/mceclip0.png)  
**Saiba mais**  
[MELHORIA - VALOR DO FRETE CONTRATADO E TRANSPORTADORA NO PEDIDO DE COMPRA](http://tdn.totvs.com/display/PROT/3137398+DMANMAT02-9983+Valor+Frete+Contratado+e+Transportadora+no+Pedido+de+Compra)  
[MT120ISC - MANIPULA O ACOLS DO PEDIDO DE COMPRAS](http://tdn.totvs.com/display/PROT/MT120ISC+-++Manipula+o+acols+do+pedido+de+compras)
