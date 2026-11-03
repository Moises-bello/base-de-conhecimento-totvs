---
article_id: 360004992932
category: ADVPL - Rotina Automática
content_hash: 714fd804fd22079486c3ac453f9885b582997cb0ff16c98436e437a071888f86
fetched_at: '2026-06-28T22:40:25.030355+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  MATA150
type: support-article
updated_at: '2021-05-21T17:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004992932-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-MATA150
---

**Dúvida**ExecAuto Mata150 com Error.log - Exclusão, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Neste Caso é necessário Posicionar no registro conforme o índice utilizado.

Exemplo:

```
#Include 'Protheus.ch'  
#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function RAUT150()  
Local aCabec := {}  
Local aItens := {}  
PRIVATE lMsErroAuto := .F.  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM"  
ConOut(Repl("-",80))  
ConOut("Inicio: "+Time())  
ConOut(PadC("Rotina Automática EXCLUSÃO",80))  
ConOut(Repl("-",80))  
aCabec:={}  
aItens:={}  
aLinha:={}  
dbSelectArea("SC8")  
dbSetOrder(1)  
dbSeek(xFilial("SC8")+"000004" + "F00001" +"01" + "0001" + "01")  
aadd(aCabec,{"C8_FORNECE" ,SC8->C8_FORNECE})  
aadd(aCabec,{"C8_LOJA" ,SC8->C8_LOJA })  
aadd(aLinha,{"C8_NUMPRO",SC8->C8_NUMPRO , Nil})  
aadd(aLinha,{"C8_ITEM" ,SC8->C8_ITEM , Nil})  
  
aadd(aItens,aLinha)  
MSExecAuto({|v,x,y| MATA150(v,x,y)},aCabec,aItens,5)  
If !lMsErroAuto  
ConOut("**** EXCLUIDO com sucesso! ****")  
Else  
MostraErro()  
ConOut("Erro na EXCLUSÃO!")  
EndIf  
ConOut("Fim : "+Time())  
RESET ENVIRONMENT  
Return(.T.)
```
