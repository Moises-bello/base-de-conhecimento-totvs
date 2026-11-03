---
article_id: 11455996242967
category: ADVPL - Rotina Automática
content_hash: d28e4ae4b3e54ed87c176b9660b1180ecf47a2dbbb164a5a29e14a79810c89a0
fetched_at: '2026-06-28T22:40:25.170852+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAATF - ExecAuto ATFA012 -
  Inclusão de Ativos Imobilizados
type: support-article
updated_at: '2023-01-12T15:00:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11455996242967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAATF-ExecAuto-ATFA012-Inclus%C3%A3o-de-Ativos-Imobilizados
---

**Dúvida**ExecAuto para Inclusão de Ativos Imobilizados -ATFA012  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Todas as versões  
  
**Solução**Rotina Automática:ATFA012

Exemplo de ExecAuto para Inclusão de Ativos Imobilizados (ATFA012).

**PoC**

```
#INCLUDE "Protheus.CH"  
  
#include "rwmake.ch"  
  
#include "TOTVS.ch"  
  
#include "TBICONN.ch"  
  
  
User Function MyAtfa012  
  
Local aArea :=GetArea()  
  
Local cBase :="ATFX01"//"0000000000"  
  
Local cItem :="0002"  
  
Local nQtd :=1  
  
Local cChapa :="AJEDS10"//"00000"  
  
Local cPatrim :="N"  
  
Local cTipo :="01"//"01"  
  
  
Local cGrupo :=""  
  
Local dAquisic//:=dDataBase//:=CTOD("01/06/20")//dDataBase  
  
Local dIndDepr//:=RetDinDepr(dDataBase)  
  
Local cDescric :="Teste 01"  
  
  
Local cHistor :="TESTE "  
  
Local cContab :="11101"  
  
Local cCusto :="CDL"  
  
Local cSubCon :="000000001"  
  
Local cClvlCon :="000000000"  
  
  
Local nValor :=1000  
  
Local nTaxa :=10  
  
Local nTamBase//:=TamSX3("N3_CBASE")[1]  
  
Local nTamChapa//:=TamSX3("N3_CBASE")[1]  
  
  
Local aParam :={}  
  
Local aCab :={}  
  
Local aItens :={}  
  
  
Private lMsErroAuto :=.F.  
  
Private lMsHelpAuto :=.T.  
  
  
PREPARE ENVIRONMENT EMPRESA"T1"FILIAL"D MG 01 "MODULO"ATF"TABLES"SN1","SN3"  
  
  
dAquisic :=dDataBase//:=CTOD("01/06/20")//dDataBase  
  
dIndDepr :=RetDinDepr(dDataBase)  
  
  
DBSelectArea(aArea)  
  
nTamBase :=TamSX3("N3_CBASE")[1]  
  
nTamChapa :=TamSX3("N3_CBASE")[1]  
  
  
aCab :={}  
  
AAdd(aCab,{"N1_CBASE", cBase ,NIL})  
  
AAdd(aCab,{"N1_ITEM", cItem ,NIL})  
  
AAdd(aCab,{"N1_AQUISIC", dDataBase ,NIL})  
  
AAdd(aCab,{"N1_DESCRIC", cDescric ,NIL})  
  
AAdd(aCab,{"N1_QUANTD", nQtd ,NIL})  
  
AAdd(aCab,{"N1_CHAPA", cChapa ,NIL})  
  
AAdd(aCab,{"N1_PATRIM", cPatrim ,NIL})  
  
AAdd(aCab,{"N1_GRUPO", cGrupo ,NIL})  
  
//Coloque os campos desejados aqui  
  
  
aItens :={}  
  
//--Preenche itens  
  
  
AAdd(aItens,{;  
  
{"N3_CBASE", cBase ,NIL},;  
  
{"N3_ITEM", cItem ,NIL},;  
  
{"N3_TIPO", cTipo ,NIL},;  
  
{"N3_BAIXA","0",NIL},;  
  
{"N3_HISTOR", cHistor ,NIL},;  
  
{"N3_CCONTAB", cContab ,NIL},;  
  
{"N3_CUSTBEM", cCusto ,NIL},;  
  
{"N3_CDEPREC", cContab ,NIL},;  
  
{"N3_CDESP", cContab ,NIL},;  
  
{"N3_CCORREC", cContab ,NIL},;  
  
{"N3_CCUSTO", cCusto ,NIL},;  
  
{"N3_DINDEPR", dIndDepr ,NIL},;  
  
{"N3_VORIG1", nValor ,NIL},;  
  
{"N3_TXDEPR1", nTaxa ,NIL},;  
  
{"N3_VORIG2", nValor ,NIL},;  
  
{"N3_TXDEPR2", nTaxa ,NIL},;  
  
{"N3_VORIG3", nValor ,NIL},;  
  
{"N3_TXDEPR3", nTaxa ,NIL},;  
  
{"N3_VORIG4", nValor ,NIL},;  
  
{"N3_TXDEPR4", nTaxa ,NIL},;  
  
{"N3_VORIG5", nValor ,NIL},;  
  
{"N3_SUBCCON", cSubCon ,NIL},;  
  
{"N3_CLVLCON", cClvlCon ,NIL},;  
  
{"N3_TXDEPR5", nTaxa ,NIL};  
  
})  
  
//Coloque os campos desejados aqui  
  
  
Begin Transaction  
  
  
MSExecAuto({|x,y,z| Atfa012(x,y,z)},aCab,aItens,3,aParam)  
  
If lMsErroAuto  
  
  
MostraErro()  
  
DisarmTransaction()  
  
Endif  
  
End Transaction  
  
  
RestArea(aArea)  
  
RESET ENVIRONMENT  
  
  
Return
```

Exemplo:

Saiba mais:

[ExecAuto ATFA012 exemplos](https://tdn.totvs.com/pages/releaseview.action?pageId=223912171)
