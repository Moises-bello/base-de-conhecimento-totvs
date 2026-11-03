---
article_id: 360016417792
category: ADVPL - Web Service
content_hash: 154fe60092cc362ec0f6fc973da63b8df7b0347912d5bbb7f5142ebc27e60c21
fetched_at: '2026-06-28T22:40:10.463784+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execução da Rotina
  no Web Service / Mata240 Via Rotina Automática
type: support-article
updated_at: '2021-12-29T13:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016417792-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-da-Rotina-no-Web-Service-Mata240-Via-Rotina-Autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: ****00:01:00 min****

**Dúvida**Como Utilizar a rotina Mata240 pelo *Web Service*?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL  – A partir da versão 12.1.17  
  
**Solução**

```
#include "protheus.ch"  
#include "tbiconn.ch"  
#include "totvs.ch"  
#include "apwebsrv.ch"  
  
//WSSTRUCT Stru040 //EXEMPLO DE WS COM EXECAUTO Mata240  
  
WSSERVICE JOB_WS_01010101  
  
WSDATA ccod AS string  
WSDATA cRet AS string  
  
WSMETHOD cMata240  
  
ENDWSSERVICE  
  
  
WSMETHOD cMata240 WSRECEIVE ccod WSSEND cRet WSSERVICE JOB_WS_01010101  
  
local aItem := {}  
local cDoc := '000000028'  
local dDatav:= CTOD("2018/10/02")  
local cProd := "P11 "  
local nOpc := 3  
Local nQtd := 10  
local dEmissao := dDataBase  
  
Private lAutoErrNoFile := .T.  
  
private lMsErroAuto := .F.  
  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Movimentacoes Internas",80))  
ConOut("Inicio: "+Time())  
  
aadd(aItem,{"D3_FILIAL","01", NIL})  
aadd(aItem,{"D3_TM", "502",NIL})  
aadd(aItem,{"D3_COD",cProd ,NIL})  
aadd(aItem,{"D3_UM","" ,NIL})  
aadd(aItem,{"D3_QUANT",nQtd ,NIL})  
aadd(aItem,{"D3_LOCAL","01" ,NIL})  
aadd(aItem,{"D3_CONTA","002 " ,NIL})  
aadd(aItem,{"D3_DOC",cDoc, NIL})  
aadd(aItem,{"D3_EMISSAO",dEmissao ,NIL})  
aadd(aItem,{"D3_NUMSEQ","000017" ,NIL})  
aadd(aItem,{"D3_LOCALIZ","RUA 002 " ,NIL})  
aadd(aItem,{"D3_LOTECTL ","1012 " ,NIL})  
aadd(aItem,{"D3_DTVALID ",dDatav ,NIL})  
  
MSExecAuto({|x,y| mata240(x,y)},aItem,nOpc)  
  
if lMsErroAuto  
aLog := GetAutoGRLog()  
::cRet := "erro"  
for i := 1 to len(aLog)  
::cRet += aLog[i]  
next i  
else  
::cRet := "ok"  
endIf
```
