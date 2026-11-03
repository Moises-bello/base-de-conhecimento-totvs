---
article_id: 360000110327
category: ADVPL - Ponto de Entrada
content_hash: c758c26390599118e3d1644b5301f31a7d62add3a0d05447d0daff05afe4227e
fetched_at: '2026-06-28T22:40:12.832787+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada
  MVC MATA020
type: support-article
updated_at: '2022-06-21T17:50:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000110327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entrada-MVC-MATA020
---

**Dúvida**Pontos de entrada MVC da rotina MATA020.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**O id do modelo da dados da rotina MATA020 é CUSTOMERVENDOR, assim sendo, a assinatura da função de usuário deve ser **User Function CUSTOMERVENDOR()**.

Observação  
O nome do arquivo.prw não poderá ser o mesmo da user function.  
  
Exemplo

```
#include "protheus.ch"  
#include "parmtype.ch"  
  
User Function CUSTOMERVENDOR()  
    Local aParam := PARAMIXB  
    Local xRet := .T.  
    Local oObj := ""  
    Local cIdPonto := ""  
    Local cIdModel := ""  
    Local lIsGrid := .F.  
    Local nLinha := 0  
    Local nQtdLinhas := 0  
    Local cMsg := ""  
  
    If aParam <> NIL  
        oObj := aParam[1]  
        cIdPonto := aParam[2]  
        cIdModel := aParam[3]  
        lIsGrid := (Len(aParam) > 3)  
  
        If cIdPonto == "MODELPOS"  
            cMsg := "Chamada na validação total do modelo." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
            xRet := ApMsgYesNo(cMsg + "Continua?")  
        ElseIf cIdPonto == "FORMPOS"  
            cMsg := "Chamada na validação total do formulário." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
            If lIsGrid  
                cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
                cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
            Else  
                cMsg += "É um FORMFIELD" + CRLF  
            EndIf  
            xRet := ApMsgYesNo(cMsg + "Continua?")  
        ElseIf cIdPonto == "FORMLINEPRE"  
            If aParam[5] == "DELETE"  
                cMsg := "Chamada na pré validação da linha do formulário. " + CRLF  
                cMsg += "Onde esta se tentando deletar a linha" + CRLF  
                cMsg += "ID " + cIdModel + CRLF  
                cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
                cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
                xRet := ApMsgYesNo(cMsg + " Continua?")  
            EndIf  
        ElseIf cIdPonto == "FORMLINEPOS"  
            cMsg := "Chamada na validação da linha do formulário." + CRLF  
            cMsg += "ID " + cIdModel + CRLF  
            cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
            cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
            xRet := ApMsgYesNo(cMsg + " Continua?")  
        ElseIf cIdPonto == "MODELCOMMITTTS"  
            ApMsgInfo("Chamada após a gravação total do modelo e dentro da transação.")  
        ElseIf cIdPonto == "MODELCOMMITNTTS"  
            ApMsgInfo("Chamada após a gravação total do modelo e fora da transação.")  
        ElseIf cIdPonto == "FORMCOMMITTTSPRE"  
            ApMsgInfo("Chamada após a gravação da tabela do formulário.")  
        ElseIf cIdPonto == "FORMCOMMITTTSPOS"  
            ApMsgInfo("Chamada após a gravação da tabela do formulário.")  
        ElseIf cIdPonto == "MODELCANCEL"  
            cMsg := "Deseja realmente sair?"  
            xRet := ApMsgYesNo(cMsg)  
        ElseIf cIdPonto == "BUTTONBAR"  
            xRet := {{"Salvar", "SALVAR", {||u_TSMT020()}}}  
        EndIf  
    EndIf  
Return xRet  
  
User Function TSMT020()  
    Alert("Buttonbar")  
Return NIL
```

**Saiba mais**  
[ADV0044 PE MVC MATA020](http://tdn.totvs.com/display/public/PROT/ADV0044_PE_MVC_MATA020_P12)
