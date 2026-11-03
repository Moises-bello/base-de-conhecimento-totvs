---
article_id: 360038885833
category: ADVPL - Ponto de Entrada
content_hash: 6b2b8b0c5ab070afa5e7b4134da69d504538e20349e4df613b3091eeb11e869c
fetched_at: '2026-06-28T22:40:12.973476+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MVC LOJA070
type: support-article
updated_at: '2021-12-30T18:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038885833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-LOJA070
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**Quais são os pontos de entrada MVC para a rotina **Administradoras Financeiras** (**LOJA070**)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.8

**Solução**  
A ideia de ponto de entrada, para fontes desenvolvidos utilizando-se o conceito de MVC e suas classes, é um pouco diferente dos fontes desenvolvidos de maneira convencional.

Em MVC criamos um único ponto de entrada e este é chamado em vários momentos dentro do fonte desenvolvido.

Este ponto de entrada único deve ser uma função de usuário e ter como nome o id (identificador) do modelo de dados (*model*) do fonte.

Ao se escrever um fonte em MVC que será uma *User Function,* cuidado ao se atribuir o *ID* do modelo de dados (*model*), pois ele não poderá ter o mesmo nome do fonte. Se o fonte tiver o nome FONT001.

**Exemplo**

```
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
User Function LOJA070 ()  
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

**Saiba mais**  
[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=208345968)

[MP - ADVPL - Como validar se uma rotina está em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572-MP-ADVPL-Como-validar-se-uma-rotina-est%C3%A1-em-MVC)
