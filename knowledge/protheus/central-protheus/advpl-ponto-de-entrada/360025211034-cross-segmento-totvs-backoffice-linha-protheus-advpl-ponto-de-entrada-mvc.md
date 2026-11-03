---
article_id: 360025211034
category: ADVPL - Ponto de Entrada
content_hash: 7c352a3a7371a247683bcf1298ca41cbc52628e3af3ce982c13ddec8041d528a
fetched_at: '2026-06-28T22:40:12.703187+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MVC
type: support-article
updated_at: '2026-01-27T18:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025211034-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18703313786007)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Pontos de entrada **MVC**   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A ideia de ponto de entrada, para fontes desenvolvidos utilizando-se o conceito de **MVC** e suas classes, é um pouco diferente dos fontes desenvolvidos de maneira convencional.  
Em **MVC** criamos um único ponto de entrada e este é chamado em vários momentos dentro do fonte desenvolvido.  
Este ponto de entrada único deve ser uma função de usuário e ter como nome o id (identificador) do modelo de dados (*model*) do fonte.  
Ao se escrever um fonte em **MVC** que será uma *User Function,* cuidado ao se atribuir o *ID* do modelo de dados (Model), pois ele não poderá ter o mesmo nome do fonte. Se o fonte tiver o nome **FONT001**, o *ID* do Modelo de Dados (*Model*) não poderá ser também **FONT001**,

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#INCLUDE 'FWMVCDEF.CH'  
  
User Function GPEA010()  
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
 xRet := {{"Salvar", "SALVAR", {||u_GP020()}}}  
 EndIf  
 EndIf  
Return xRet  
   
User Function GP020()  
 Alert("Buttonbar")  
Return NIL
```

**Saiba mais**  
[PONTO DE ENTRADA PADRÃO DO MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968)  
[COMO VALIDAR SE A ROTINA PROTHEUS JÁ ESTÁ NO PADRÃO MVC?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572-MP-ADVPL-Como-validar-se-uma-rotina-est%C3%A1-em-MVC)
