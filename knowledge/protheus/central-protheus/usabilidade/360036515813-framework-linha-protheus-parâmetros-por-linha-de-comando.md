---
article_id: 360036515813
category: Usabilidade
content_hash: 6dae3a309918a886591580ae6371734a1baaf80828c081471603aae95ad4c500
fetched_at: '2026-06-28T22:42:17.262567+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: Framework - Linha Protheus - PARÂMETROS POR LINHA DE COMANDO
type: support-article
updated_at: '2026-01-26T19:42:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036515813-Framework-Linha-Protheus-PAR%C3%82METROS-POR-LINHA-DE-COMANDO
---

**DÚVIDA**  
Como passar parâmetros para um programa executado via linha de comando?  
  
**AMBIENTE**  
Protheus – ADVPL – A partir da versão 11.8  
  
**SOLUÇÃO**  
Sempre que executada uma função via linha de comando, os parâmetros devem ser enviados via `-A`  e o programa informado em `-P` deve estar sem os parâmetros:

```
start c:\protheus\bin\smartclient\smartclient.exe -M -Q -P=U_T234CLI -E=P1217_X32A -C=LOCAL -A=COD000
```

**EXEMPLO**  
Para este exemplo, utilizaremos a sequência de parâmetros abaixo:

```
-A=COD001 -A=.T. -A=131.21 -A=29/09/2019 -A={|x|MsgInfo(x)} -A={"A",1,.T.,{||JsonObject():New()},"27/01/2019"}
```

**ATENÇÃO**  
Veja que todos os parâmetros não têm espaço entre seu início e fim e serão enviados como caractere.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047080114)  
  
**FONTE**

```
// BIBLIOTECAS NECESSÁRIAS
#Include "TOTVS.ch"

//------------------------------------------------------
// RECEBE PARÂMETROS VIA LINHA DE COMANDO
//------------------------------------------------------
User Function T234CLI(uPar1, uPar2, uPar3, uPar4, uPar5, uPar6)
    Local cCode   As Character
    Local lValid  As Logical
    Local nAmount As Numeric
    Local dToday  As Date
    Local bExec   As CodeBlock
    Local aInfo   As Array

    Default uPar1 := Space(0)
    Default uPar2 := ".F."
    Default uPar3 := "0"
    Default uPar4 := Date()
    Default uPar5 := "{|| NIL}"
    Default uPar6 := "{ }"

    cCode   := uPar1
    lValid  := &(uPar2)
    nAmount := Val(uPar3)
    dToday  := CToD("29/09/2019", "DDMMYYYY")
    bExec   := &(uPar5)
    aInfo   := Parse1DArr(uPar6)
Return (NIL)

//------------------------------------------------------
// CONVERTE VETORES DE UM UMA DIMENSÃO ENVIADOS
// POR MEIO DE LINHA DE COMANDO
//------------------------------------------------------
Static Function Parse1DArr(cArray)
    Local aArray As Array
    Local lValid As Logical
    Local nX     As Numeric

    // TRATA AS POSIÇÕES DO VETOR
    cArray := AllTrim(SubStr(cArray, 2, Len(cArray) - 2))
    If (!Empty(cArray))
        aArray := StrTokArr(cArray, ",")
        lValid := .T.
    Else
        aArray := Array(0)
        lValid := .F.
    EndIf

    // PERCORRE AS POSIÇÕES DO VETOR
    If (lValid .And. Len(aArray) > 0)
        For nX := 1 To Len(aArray)
            Do Case
                // LOGICO
                Case (Len(aArray[nX]) == 3 .And. SubStr(aArray[nX], 1, 1) == "." .And. SubStr(aArray[nX], 3, 3) == ".")
                    aArray[nX] := &(aArray[nX])
                // BLOCO DE CÓDIGO
                Case (SubStr(aArray[nX], 1, 2) == "{|")
                    aArray[nX] := &(aArray[nX])
                // DATA
                Case (Len(aArray[nX]) == 10 .And. SubStr(aArray[nX], 3, 1) == "/" .And. SubStr(aArray[nX], 6, 1) == "/")
                    aArray[nX] := CToD(aArray[nX], "DDMMYYYY")
                // NUMÉRICO
                Case (!IsAlpha(aArray[nX]))
                    aArray[nX] := Val(aArray[nX])
                // CARACTERE MANTÉM-SE NO ESTADO ATUAL
            EndCase
        Next nX
    EndIf
Return (aArray)
```

**SAIBA MAIS**  
[SMARTCLIENT - PARÂMETROS DE LINHA](https://tdn.totvs.com/pages/viewpage.action?pageId=6066051)
