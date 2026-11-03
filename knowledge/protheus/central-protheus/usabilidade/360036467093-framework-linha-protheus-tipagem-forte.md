---
article_id: 360036467093
category: Usabilidade
content_hash: 903c836cf98ff55e72ed75bdd7b11286010b076c320050ae629a35365d2768ec
fetched_at: '2026-06-28T22:42:17.286173+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: Framework - Linha Protheus - TIPAGEM FORTE
type: support-article
updated_at: '2026-01-26T19:43:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036467093-Framework-Linha-Protheus-TIPAGEM-FORTE
---

**DÚVIDA**  
É possível utilizar tipagem forte em ADVPL?  
  
**AMBIENTE**  
Protheus – ADVPL – A partir da versão 11.8  
  
**SOLUÇÃO**  
Sim, contudo é necessário o uso da biblioteca PARMTYPE.ch.  
  
**EXEMPLO**

```
#Include "PARMTYPE.ch"
#Include "TOTVS.ch"

User Function T102PARAM()
    Local cVar := "TOTVS"
    Local nVar := 1987
    Local lVar := .F.
    Local dVar := Date()
    Local bVar := {|| MsgInfo("CODEBLOCK")}
    Local uVar := 50 // OU "50"
    Local aVar := {}
    Local oVar := TWSDLManager():New()

    ParamType(cVar, nVar, lVar, dVar, bVar, uVar, aVar, oVar)
Return (NIL)

Static Function ParamType(cVar, nVar, lVar, dVar, bVar, uVar, aVar, oVar)
    PARAMTYPE 1 VAR cVar AS CHARACTER          OPTIONAL DEFAULT ""
    PARAMTYPE 2 VAR nVar AS NUMERIC            OPTIONAL DEFAULT 0
    PARAMTYPE 3 VAR lVar AS LOGICAL            OPTIONAL DEFAULT .T.
    PARAMTYPE 4 VAR dVar AS DATE               OPTIONAL DEFAULT Date()
    PARAMTYPE 5 VAR bVar AS BLOCK              OPTIONAL DEFAULT { || .F. }
    PARAMTYPE 6 VAR uVar AS CHARACTER, NUMERIC OPTIONAL DEFAULT "0"
    PARAMTYPE 7 VAR aVar AS ARRAY              OPTIONAL DEFAULT Array(0)
    PARAMTYPE 8 VAR oVar AS OBJECT             OPTIONAL DEFAULT JsonObject():New()
Return (NIL)
```
