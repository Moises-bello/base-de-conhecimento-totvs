---
article_id: 360018033892
category: ADVPL - Rotina Automática
content_hash: 46e3455092ca5a721faba0d0a26820146f42e73b2a9631e368d1f4eab505e782
fetched_at: '2026-06-28T22:40:24.948653+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execauto OMSA010 '
type: support-article
updated_at: '2026-04-17T19:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018033892-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execauto-OMSA010
---

**Dúvida**Como realizar Alteração ou Exclusão na **ExecAuto** da rotina **OMSA010**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Para Alteração e exclusão de um item da rotina automática deve-se utilizar **LINPOS** e **AUTDELETA**

Quando existir a necessidade de alterar um item especifico da Getdados, existem dois campos que podem ser utilizados, os campos são: LINPOS e AUTDELETA. O primeiro deve ser utilizado para localizar o item do aCols que sofrerá alteração, o segundo instruí a rotina automática para deletar a linha. Caso não seja utilizado o LINPOS esta função irá reconstruir todo o aCols.

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#INCLUDE "TBICONN.CH"  
  
user function EOSA010()  
  
local aCab := {}  
local aItem := {}  
local nOpc := 4  
local i  
local cCodTab := "007"  
local cNomeTab := "TESTE2 "  
local cHoraDe := "00:00"  
local cHoraAte := "23:59"  
local cTpHorario := "1"  
local cTabAtiv := "1"  
local cItem := "0003"  
local cProduto := "TB0000000000001"  
local nPrcVen := 22  
local nPrcVen2 := 20  
local cAtivo := "1"  
local aItens :={}  
PRIVATE lMsErroAuto := .F.  
  
   
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'  
  
aAdd(aCab, {"DA0_CODTAB" , cCodTab , NIL})  
aAdd(aCab, {"DA0_DESCRI" , cNomeTab , NIL})  
aAdd(aCab, {"DA0_DATDE" , dDatabase , NIL})  
aAdd(aCab, {"DA0_HORADE" , cHoraDe , NIL})  
aAdd(aCab, {"DA0_TPHORA" , cTpHorario, NIL})  
aAdd(aCab, {"DA0_ATIVO" , cTabAtiv , NIL})  
  
//aItem:={}  
  
aAdd(aItem,{ {"DA1_ITEM" , cItem , NIL},;  
{"DA1_CODPRO" , cProduto , NIL},;  
{"DA1_PRCVEN" , nPrcVen , NIL}})  
  
// Para incluir um unico item não é necessario os itens LINPOS e AUTDELETA usa-se somente na Alteração ou exclusão  
  
{"LINPOS","DA1_ITEM" ,'0001'},;  
{"AUTDELETA","N" ,Nil}})  
  
//aadd(aItens, aItem)  
//aItem:={}  
/* aAdd(aItem,{ {"DA1_ITEM" , "0004" , NIL},;  
{"DA1_CODPRO" , "TB0000000000002" , NIL},;  
{"DA1_PRCVEN" ,nPrcVen2 , NIL}})  
  
// Para excluir um unico item é os itens LINPOS e AUTDELETA sendo que o Autdeleta receberá o valor "N"  
  
//{"LINPOS","DA1_ITEM" ,'0002'},;  
//{"AUTDELETA","S" ,Nil}})*/  
  
//aadd(aItens, aItem)  
  
Omsa010(aCab,aItem,nOpc)  
  
If lMsErroAuto  
  
DisarmTransaction()  
Mostraerro()  
Else  
conout("ALterado com sucesso.")  
EndIf  
RESET ENVIRONMENT  
Return(.T.)  
  
Obs Verifique nOpc := 4 - Alteração / 3 - Inclusão
```

**Saiba Mais**

[**MsGetDAuto**](http://tdn.totvs.com/display/public/PROT/MsGetDAuto)

**[OMSA010 rotina automática da tabela de preços](https://tdn.totvs.com/display/public/PROT/ADV0024_ROT_EXECAUTO_OMSA010)**
