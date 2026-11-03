---
article_id: 360018987432
category: ADVPL - Rotina Automática
content_hash: 4dfe599a766e7b7557b437149af86df687f2cefc913efa21bce4e4c925447b79
fetched_at: '2026-06-28T22:40:24.173337+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina automática csaa100
  (departamentos)
type: support-article
updated_at: '2021-12-29T19:06:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018987432-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-csaa100-departamentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível executar a rotina CSAA100 (Departamentos) por meio de execução automática?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 12.1.17  
  
**Solução**Sim, é possível.  
  
**Fonte**

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
User Function TCSAA100()  
    Local nOpr    := 3  
    Local aHeader := {}  
    Local aArea   := {}  
   
    Private lMsErroAuto := .F.  
    Private lMsHelpAuto := .T.  
  
    RPCSetEnv("99", "01", NIL, NIL, "TMK", NIL, {"SQB"})   
        aArea := GetArea()  
  
        // BEGIN: CREATE //  
        If (nOpr == 3)  
            AAdd(aHeader, {"QB_DEPTO",      "DEPT00003"})  
            AAdd(aHeader, {"QB_DESCRIC",    "QUALITY ASSURANCE"})  
            AAdd(aHeader, {"QB_CC",         ""})  
            AAdd(aHeader, {"QB_FILRESP",    ""})  
            AAdd(aHeader, {"QB_MATRESP",    ""})  
            AAdd(aHeader, {"QB_DEPSUP",     ""})  
            AAdd(aHeader, {"QB_ARELIN",     ""})  
        EndIf  
        // END: CREATE //  
   
        MsExecAuto({|w, x, y, z| CSAA100(w, x, y, z)}, NIL, NIL, aHeader, nOpr)  
  
        If (lMsErroAuto == .T.)  
            MostraErro()  
  
            ConOut(Repl("-", 80))  
            ConOut(PadC("CSAA100 automatic routine ended with error", 80))  
            ConOut(PadC("Ends at: " + Time(), 80))  
            ConOut(Repl("-", 80))  
        Else  
            ConOut(Repl("-", 80))  
            ConOut(PadC("CSAA100 automatic routine successfully ended", 80))  
            ConOut(PadC("Ends at: " + Time(), 80))  
            ConOut(Repl("-", 80))  
        EndIf  
   
        RestArea(aArea)  
    RPCClearEnv()  
Return (NIL)
```
