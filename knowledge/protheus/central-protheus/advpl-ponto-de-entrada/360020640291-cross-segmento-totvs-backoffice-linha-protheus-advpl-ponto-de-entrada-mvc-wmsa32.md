---
article_id: 360020640291
category: ADVPL - Ponto de Entrada
content_hash: 5d612ed535b0548d68da65ce6b952afbd9daecab450383b44b8770e26100c008
fetched_at: '2026-06-28T22:40:12.729264+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MVC WMSA320 '
type: support-article
updated_at: '2021-08-20T13:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020640291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-WMSA320
---

**Dúvida**Quais são os pontos de entrada **MVC** para a rotina WMSA320 ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Modelo **WMSA320A** para acessar o ponto de entrada **MVC** na **Montagem**.

Modelo **WMSA320** para acessar o ponto de entrada **MVC** ao **Excluir**.

A ideia de ponto de entrada, para fontes desenvolvidos utilizando-se o conceito de **MVC** e suas classes, é um pouco diferente dos fontes desenvolvidos de maneira convencional.

Em **MVC** criamos um único ponto de entrada e este é chamado em vários momentos dentro do fonte desenvolvido.

Este ponto de entrada único deve ser uma função de usuário e ter como nome o id (identificador) do modelo de dados (*model*) do fonte.

Ao se escrever um fonte em **MVC** que será uma *User Function,* cuidado ao se atribuir o *ID* do modelo de dados (Model), pois ele não poderá ter o mesmo nome do fonte. Se o fonte tiver o nome **FONT001**, o *ID* do Modelo de Dados (*Model*) não poderá ser também **FONT001**,

```
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
User Function WMSA320 ()//Modelo de Dados  
 Local aParam := PARAMIXB  
 Local xRet := .T.  
 Local oObj := ""  
 Local cIdPonto := ""  
 Local cIdModel := ""  
 Local lIsGrid := .F.  
 Local nLinha := 0  
 Local nQtdLinhas := 0  
 Local cMsg := ""  
 Local nOp  
  
If (aParam <> NIL)  
 oObj := aParam[1]  
 cIdPonto := aParam[2]  
 cIdModel := aParam[3]  
 lIsGrid := (Len(aParam) > 3)  
  
nOpc := oObj:GetOperation() // PEGA A OPERAÇÃO  
  
If (cIdPonto == "MODELPOS")  
 cMsg := "Chamada na validação total do modelo." + CRLF  
 cMsg += "ID " + cIdModel + CRLF  
 IF nOp == 3  
 Alert('inclusão')  
 ENDIF  
  
xRet := MsgYesNo(cMsg + "Continua?")  
 ElseIf (cIdPonto == "MODELVLDACTIVE")  
 cMsg := "Chamada na ativação do modelo de dados."  
  
xRet := MsgYesNo(cMsg + "Continua?")  
 ElseIf (cIdPonto == "FORMPOS")  
 cMsg := "Chamada na validação total do formulário." + CRLF  
 cMsg += "ID " + cIdModel + CRLF  
  
If (lIsGrid == .T.)  
 cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
 cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
 Else  
 cMsg += "É um FORMFIELD" + CRLF  
 EndIf  
  
xRet := MsgYesNo(cMsg + "Continua?")  
 ElseIf (cIdPonto =="FORMLINEPRE")  
 If aParam[5] =="DELETE"  
 cMsg := "Chamada na pré validação da linha do formulário." + CRLF  
 cMsg += "Onde esta se tentando deletar a linha" + CRLF  
 cMsg += "ID " + cIdModel + CRLF  
 cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
 cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
  
xRet := MsgYesNo(cMsg + " Continua?")  
 EndIf  
 ElseIf (cIdPonto =="FORMLINEPOS")  
 cMsg := "Chamada na validação da linha do formulário." + CRLF  
 cMsg += "ID " + cIdModel + CRLF  
 cMsg += "É um FORMGRID com " + Alltrim(Str(nQtdLinhas)) + " linha(s)." + CRLF  
 cMsg += "Posicionado na linha " + Alltrim(Str(nLinha)) + CRLF  
  
xRet := MsgYesNo(cMsg + " Continua?")  
 ElseIf (cIdPonto =="MODELCOMMITTTS")  
 MsgInfo("Chamada após a gravação total do modelo e dentro da transação.")  
 ElseIf (cIdPonto =="MODELCOMMITNTTS")  
 MsgInfo("Chamada após a gravação total do modelo e fora da transação.")  
 ElseIf (cIdPonto =="FORMCOMMITTTSPRE")  
 MsgInfo("Chamada após a gravação da tabela do formulário.")  
 ElseIf (cIdPonto =="FORMCOMMITTTSPOS")  
 MsgInfo("Chamada após a gravação da tabela do formulário.")  
 ElseIf (cIdPonto =="MODELCANCEL")  
 cMsg := "Deseja realmente sair?"  
  
xRet := MsgYesNo(cMsg)  
 ElseIf (cIdPonto =="BUTTONBAR")  
 xRet := {{"Botão", "BOTÃO", {|| MsgInfo("Buttonbar")}}}  
 EndIf  
 EndIf  
Return (xRet)
```

**SAIBA MAIS**  
[Ponto de entrada padrão do MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968%20)   
[Como validar se a rotina protheus já esta no padrão MVC?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572-MP-ADVPL-Como-validar-se-uma-rotina-est%C3%A1-em-MVC)
