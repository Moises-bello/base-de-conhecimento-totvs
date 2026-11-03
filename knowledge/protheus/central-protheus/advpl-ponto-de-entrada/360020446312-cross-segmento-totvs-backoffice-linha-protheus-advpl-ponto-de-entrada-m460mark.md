---
article_id: 360020446312
category: ADVPL - Ponto de Entrada
content_hash: f11b6a4ab734c395e88c0719d938bdad93f6ddcc0767cd054e915ba58267e053
fetched_at: '2026-06-28T22:40:11.840961+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  M460mark
type: support-article
updated_at: '2022-04-25T16:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020446312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M460mark
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como utilizar o ponto de entrada M460MARK da rotina MATA460?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Este ponto de entrada envia por PARAMIXB duas posições, sendo a primeira a marca utilizada e a segunda uma variável lógica informando se foi clicado em "Marcar Todos" ou não.  
Caso esteja como .T. (*true*), será necessário inverter a ordem, considerando os marcados como os que não têm marcação.  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIOS  
#Include "TOTVS.ch"  
  
// PONTO DE ENTRADA M460MARK  
User Function M460MARK()  
    Local cMark   := PARAMIXB[1] // MARCA UTILIZADA  
    Local lInvert := PARAMIXB[2] // SELECIONOU "MARCA TODOS"  
    Local aArea   := GetArea("SC9")  
  
    SC9->(DbGoTop())  
  
    While (SC9->(!EOF()))  
        If (lInvert) // "CHECK ALL" OPTION SELECTED  
            If (SC9->C9_OK == cMark)  
                MsgInfo("Unmarked: " + SC9->C9_PEDIDO, "Entry Point M460MARK")  
            Else  
                MsgInfo("Marked: " + SC9->C9_PEDIDO, "Entry Point M460MARK")  
            EndIf  
        Else // "CHECK ALL" OPTION NOT SELECTED  
            If (SC9->C9_OK == cMark)  
                MsgInfo("Marked: " + SC9->C9_PEDIDO, "Entry Point M460MARK")  
            Else  
                MsgInfo("Unmarked: " + SC9->C9_PEDIDO, "Entry Point M460MARK")  
            EndIf  
        EndIf  
  
        SC9->(DbSkip())  
    End  
  
    RestArea(aArea)  
Return (MsgYesNo("Continue the current process?", "Entry Point M460MARK"))
```
