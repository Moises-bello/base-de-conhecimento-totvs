---
article_id: 360021047852
category: ADVPL - Ponto de Entrada
content_hash: 6615532c91a3a2d69af1996c8e1169aa40bf56326d1c01be84da0ba9de446c67
fetched_at: '2026-06-28T22:40:12.709790+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MVC Gpea020
type: support-article
updated_at: '2022-11-08T20:05:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021047852-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-Gpea020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**  
Quais são os pontos de entrada **MVC** para a rotina **GPEA020?**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8

**Solução**  
A ideia de ponto de entrada, para fontes desenvolvidos utilizando-se o conceito de **MVC** e suas classes, é um pouco diferente dos fontes desenvolvidos de maneira convencional.  
Em **MVC** criamos um único ponto de entrada e este é chamado em vários momentos dentro do fonte desenvolvido.  
Este ponto de entrada único deve ser uma função de usuário e ter como nome o id (identificador) do modelo de dados (*model*) do fonte.  
Ao se escrever um fonte em **MVC** que será uma *User Function,* cuidado ao se atribuir o *ID* do modelo de dados (*Model*), pois ele não poderá ter o mesmo nome do fonte. Se o fonte tiver o nome **FONT001**, o *ID* do Modelo de Dados (*Model*) não poderá ser também **FONT001**,

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#INCLUDE 'FWMVCDEF.CH'  
  
user function GPEA020()  
Local aParam := PARAMIXB  
Local xRet := .T.  
Local oObj := ''  
Local cIdPonto := ''  
Local cIdModel := ''  
Local lIsGrid := .F.  
  
Local nLinha := 0  
Local nQtdLinhas := 0  
Local cMsg := ''  
local nome  
   
If aParam <> NIL  
  
oObj := aParam[1]  
cIdPonto := aParam[2]  
cIdModel := aParam[3]  
lIsGrid := ( Len( aParam ) > 3 )  
  
/*If lIsGrid  
 nQtdLinhas := oObj:GetQtdLine()  
 nLinha := oObj:nLine  
EndIf */  
  
If cIdPonto == 'FT300ORC'  
cMsg := 'Chamada na validação total do modelo FT300ORC FT300ORC FT300ORC.' + CRLF  
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
  
oModelx := FWModelActive() //Carregando Model Ativo  
oModelxDet := oModelx:GetModel('GPEA020_SRB') //Carregando grid de dados a partir o ID que foi instanciado no fonte.  
nome := oModelxDet:getValue('RB_NOME')  
IF (nome <> 'TESTE')  
   
 xRet := ApMsgYesNo('dESEJA ALTERAR O NOME '+nome+' ?' )  
 IF (xRet)  
 oModelxDet:setValue('RB_NOME','TESTE')  
 ENDIF  
ENDIF  
  
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
  
ElseIf cIdPonto == 'MODELVLDCATIVE'  
xRet := { {'Salvar', 'SALVAR', { || u_TESTEX() } } }  
EndIf  
EndIf  
Return xRet
```

**Saiba mais**  
[Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968)  
[Cross Segmento - Backoffice Linha Protheus - ADVPL - Como validar se uma rotina está em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572)
