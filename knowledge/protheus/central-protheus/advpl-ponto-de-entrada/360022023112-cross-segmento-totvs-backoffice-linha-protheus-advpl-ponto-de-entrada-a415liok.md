---
article_id: 360022023112
category: ADVPL - Ponto de Entrada
content_hash: 600285698edea62a557a5e8979f1dbf7e631665d771a8100c2b35551c707c33d
fetched_at: '2026-06-28T22:40:11.597142+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL -  Ponto de entrada
  A415LIOK
type: support-article
updated_at: '2022-05-04T12:00:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022023112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-A415LIOK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como faço para validar os dados das tabelas SCK, SCL e SCJ por meio do ponto de entrada A415LIOK?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÕES PRINCIPAIS  
User Function A415LIOK()  
    Local lValid    := .T.                    // CONTROLE DE VALIDAÇÃO  
    Local cAliasSCK := aHeaderSCK[1][9]       // ITENS DA TABELA SCK  
    Local cAliasSCL := aHeaderSCL[1][9]       // ITENS DA TABELA SCL  
    Local aAreaSCK  := (cAliasSCK)->GetArea() // ARMAZENA A ÁREA CORRENTE DA SCK  
    Local aAreaSCL  := (cAliasSCL)->GetArea() // ARMAZENA A ÁREA CORRENTE DA SCL  
  
    // EXEMPLO DE VALIDAÇÃO NA TABELA SCK  
    If (AllTrim((cAliasSCK)->CK_PRODUTO) == "PRDT0001")  
        lValid := .F.  
        Help(NIL, NIL, "SCK_PRDT_DENIED", NIL, "Produto Indisponível",;  
            1, 0, NIL, NIL, NIL, NIL, NIL, {"Utilize outro produto."})  
    EndIf  
  
    // EXEMPLO DE VALIDAÇÃO NA TABELA SCJ  
    If (CJ_TIPOCLI =="J" .Or. AllTrim(CJ_PROSPE) == "PRP002")  
        lValid := .F.  
        Help(NIL, NIL, "SCJ_PROSPCT_DENIED", NIL, "Prospect ou Tipo do Cliente não permitido",;  
            1, 0, NIL, NIL, NIL, NIL, NIL, {"Entre em contato com o responsável de faturamento."})  
    EndIf  
  
    // EXEMPLO DE VALIDAÇÃO NA TABELA SCL  
    If (AllTrim((cAliasSCL)->CL_PRODUTO) == "PRDT0005")  
        lValid := .F.  
        Help(NIL, NIL, "SCL_PRDT_DENIED", NIL, "Produto Indisponível",;  
            1, 0, NIL, NIL, NIL, NIL, NIL, {"Utilize outro produto."})  
    EndIf  
      
    // RESTAURA O ESTADO ANTERIOR  
    RestArea(aAreaSCK)  
    RestArea(aAreaSCL)  
Return (lValid)
```

**Saiba mais**  
[A415LIOK - Validação do processo de orçamento de venda](http://tdn.totvs.com/pages/releaseview.action?pageId=6784038)
