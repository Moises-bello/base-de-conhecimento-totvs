---
article_id: 115011659247
category: ADVPL - Ponto de Entrada
content_hash: 61f614b98c83f83df9f7db20ceecbb416b8154ac7cc296932967b46185e20e29
fetched_at: '2026-06-28T22:40:11.716991+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Lista com os pontos
  de entrada em MVC
type: support-article
updated_at: '2022-06-21T17:55:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011659247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Lista-com-os-pontos-de-entrada-em-MVC
---

**Dúvida**Há uma lista com os pontos de entrada MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**

Não temos ainda uma lista completa de pontos de entrada na versão 12, mas esse documento estará sempre em atualização informando algumas rotina com ponto de entrada no padrão MVC:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MATA131 | FATA300 | FATA600 | OMSA010 | CNTA300 | MATA094 | TECA930 | TECA890 | JURA109 |
| MATA311 | TECA440 | FINM010 | ~~ATFA010~~ ATFA012 | GPEA240 | MNTA080 | GPEA020 | ~~ATFA030~~ ATFA036 | ~~FINA460~~ FINA460A |
| ~~MATA010~~ ITEM | ~~MATA020~~ CUSTOMERVENDOR | GPEA020 | MATA014 | FISA010 | CNTA300 | ~~EECAT140~~  EXPP013 | ~~MATA960 MATA960MOD~~ | MATA019 |

**Observação**  
o nome do arquivo.prw não poderá ser o mesmo da user function.  
  
Exemplo

```
#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'FWMVCDEF.CH'  
  
User Function MATA311()//Nome o ID do Modelo de Dados (Model) ou Nome da rotina  
Local aParam := PARAMIXB  
Local xRet := .T.  
Local oObj := ''  
Local cIdPonto := ''  
Local cIdModel := ''  
Local lIsGrid := .F.  
Local nLinha := 0  
Local nQtdLinhas := 0  
Local cMsg := ''  
  
If aParam <> NIL  
oObj := aParam[1]  
cIdPonto := aParam[2]  
cIdModel := aParam[3]  
lIsGrid := ( Len( aParam ) > 3 )  
//If lIsGrid  
// nQtdLinhas := oObj:GetQtdLine()  
// nLinha := oObj:nLine  
//EndIf  
If cIdPonto == 'MODELPOS'  
cMsg := 'Chamada na validação total do modelo.' + CRLF  
cMsg += 'ID ' + cIdModel + CRLF  
xRet := ApMsgYesNo( cMsg + 'Continua ?' )  
ElseIf cIdPonto == 'FORMPOS'  
cMsg := 'Chamada na validação total do formulário.' + CRLF  
cMsg += 'ID ' + cIdModel + CRLF  
If lIsGrid  
cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
Else  
cMsg += 'É um FORMFIELD' + CRLF  
EndIf  
xRet := ApMsgYesNo( cMsg + 'Continua ?' )  
ElseIf cIdPonto == 'FORMLINEPRE'  
If aParam[5] == 'DELETE'  
cMsg := 'Chamada na pre validação da linha do formulário. ' + CRLF  
cMsg += 'Onde esta se tentando deletar a linha' + CRLF  
cMsg += 'ID ' + cIdModel + CRLF  
cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
xRet := ApMsgYesNo( cMsg + 'Continua ?' )  
EndIf  
ElseIf cIdPonto == 'FORMLINEPOS'  
cMsg := 'Chamada na validação da linha do formulário.' + CRLF  
cMsg += 'ID ' + cIdModel + CRLF  
cMsg += 'É um FORMGRID com ' + Alltrim( Str( nQtdLinhas ) ) + ' linha(s).' + CRLF  
cMsg += 'Posicionado na linha ' + Alltrim( Str( nLinha ) ) + CRLF  
xRet := ApMsgYesNo( cMsg + 'Continua ?' )  
ElseIf cIdPonto == 'MODELCOMMITTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e dentro da transação.')  
ElseIf cIdPonto == 'MODELCOMMITNTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e fora da transação.')  
ElseIf cIdPonto == 'FORMCOMMITTTSPRE'  
ApMsgInfo('Chamada apos a gravação da tabela do formulário.')  
ElseIf cIdPonto == 'FORMCOMMITTTSPOS'  
ApMsgInfo('Chamada apos a gravação da tabela do formulário.')  
ElseIf cIdPonto == 'MODELCANCEL'  
cMsg := 'Deseja Realmente Sair ?'  
xRet := ApMsgYesNo( cMsg )  
ElseIf cIdPonto == 'BUTTONBAR'  
xRet := { {'Salvar', 'SALVAR', { || u_TESTEX() } } }  
  
EndIf  
EndIf  
Return xRet  
  
User Function TESTEX()  
ALert ("passou")  
Return
```

**Saiba mais**  
[ADV0032 Ponto de entrada MVC](http://tdn.totvs.com/display/PROT/ADV0032_PE_MVC_NA_P12)
