---
article_id: 9016530784023
category: ADVPL - Rotina Automática
content_hash: 5353ddcc00c65dd3322194bcb8d1d8a9104593ecba067464bd63dfbed71babb9
fetched_at: '2026-06-28T22:40:25.144525+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAATF - ExecAuto  ATFA036 -
  Cancelamento de Baixa de Ativos Imobilizados
type: support-article
updated_at: '2023-01-23T16:42:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9016530784023-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAATF-ExecAuto-ATFA036-Cancelamento-de-Baixa-de-Ativos-Imobilizados
---

**Dúvida**ExecAuto para cancelamento de baixa de Ativos - TUFUWY  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Todas as versões  
  
**Solução**Rotina Automática: TUFUWY

Exemplo de ExecAuto para cancelamento de baixa de Ativos Imobilizados (ATFA036).

**PoC**

```
#INCLUDE"Protheus.ch"  
  
User Function MyATF036()  
  
Local aArea  := GetArea()  
Local cBase  :="0000000005"  
Local cItem  :="0001"  
Local cTipo  :="01"  
Local cTpSaldo :="1"  
Local cBaixa  :="1"  
Local cSeq   :="001"  
Local cSeqReav :=""  
Local cFilOri  :="D MG 01"  
Local cMotivo  :="08"  
Local cMetDepr := GetMV('MV_ATFDPBX')  
Local aCab   := {}  
Local aAtivo  := {}  
Local aParam  := {}  
Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
  
  
  
aCab := { {"FN6_FILIAL",XFilial("FN6") ,NIL},;     
  
{"FN6_CBASE",cBase    ,NIL},;     
  
{"FN6_CITEM",cItem    ,NIL},;     
  
{"FN6_MOTIVO",cMotivo   ,NIL},;     
  
{"FN6_DEPREC",cMetDepr   ,NIL}}  
  
  
aAtivo := {{"N3_FILIAL",XFilial("SN3") ,NIL},;     
  
{"N3_CBASE",cBase    ,NIL},;      
  
{"N3_ITEM",cItem    ,NIL},;      
  
{"N3_TIPO",cTipo    ,NIL},;      
  
{"N3_BAIXA",cBaixa   ,NIL},;      
  
{"N3_TPSALDO",cTpSaldo   ,NIL},;      
  
{"N3_SEQ",cSeq    ,NIL},;      
  
{"N3_SEQREAV",cSeqReav   ,NIL},;      
  
{"N3_FILORIG",cFilOri   ,NIL}}  
  
//Array contendo os parametros do F12  
  
aAdd( aParam, {"MV_PAR01",1} )//Pergunta 01 - Mostra Lanc. Contab? 1 = Sim ; 2 = Não  
  
aAdd( aParam, {"MV_PAR02",2} )//Pergunta 02 - Aglutina Lancamento Contabil ? 1 = Sim ; 2 = Não  
  
aAdd( aParam, {"MV_PAR03",1} )//Pergunta 03 - Contabaliza On-Line? 1 = Sim ; 2 = Não  
  
aAdd( aParam, {"MV_PAR04",1} )//Pergunta 04 - Visualização ? 1 = Baixas de Ativo  // deve se usar obrigatoriamente o número 1  
  
  
Begin Transaction    
  
MsExecAuto({|a,b,c,d,e,f|ATFA036(a,b,c,d,e,f)},aCab,aAtivo,5,,.T./*lBaixaTodos*/,aParam)    
  
  
If lMsErroAuto    
  
  
MostraErro()     
  
DisarmTransaction()    
  
  
EndIf  
  
  
End Transaction  
  
RestArea(aArea)  
  
Return
```

Exemplo:

Saiba mais:

[Exemplo de baixa de Ativos Imobilizados.](https://tdn.totvs.com/pages/releaseview.action?pageId=223912171)
