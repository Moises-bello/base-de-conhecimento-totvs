---
article_id: 9016254677527
category: ADVPL - Rotina Automática
content_hash: 0ea0bf7083f0b609bcb5aaf5cdf71ce975b0b95e8d0496e4413d71da4217407b
fetched_at: '2026-06-28T22:40:25.183854+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAATF - ExecAuto ATFA036 -
  Baixa de Ativos Imobilizados
type: support-article
updated_at: '2023-05-05T20:24:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9016254677527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAATF-ExecAuto-ATFA036-Baixa-de-Ativos-Imobilizados
---

**Dúvida**ExecAuto para baixa de Ativos - TUFUWY  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Todas as versões  
  
**Solução**Rotina Automática: TUFUWY

Exemplo de ExecAuto para baixa de Ativos Imobilizados (ATFA036).

**PoC**

|  |
| --- |
| ``` #INCLUDE"Protheus.ch"   User Function MyATF036()  Local aArea := GetArea()  Local cBase :="0000000005"  Local cItem :="0001"  Local cTipo :="01"  Local cTpSaldo :="1"  Local cBaixa :="0"  Local nQtdAtu :=1  Local nQtdBaixa :=1  Local cMotivo :="08"  Local cMetDepr := GetMV('MV_ATFDPBX')  Local cNumNF :=""  Local cSerieNF :=""  Local nValNF :=0   Local aCab := {}  Local aAtivo := {}  Local aParam := {}   Private lMsErroAuto := .F.  Private lMsHelpAuto := .T.    aCab := { {"FN6_FILIAL",XFilial("FN6") ,NIL},;  {"FN6_CBASE",cBase ,NIL},;  {"FN6_CITEM",cItem ,NIL},;  {"FN6_MOTIVO",cMotivo ,NIL},;  {"FN6_BAIXA",100,NIL},;  {"FN6_QTDBX",nQtdBaixa ,NIL},;  {"FN6_DTBAIX",dDatabase ,NIL},;  {"FN6_DEPREC",cMetDepr ,NIL}}   aAtivo := {{"N3_FILIAL",XFilial("SN3") ,NIL},;  {"N3_CBASE",cBase ,NIL},;  {"N3_ITEM",cItem ,NIL},;  {"N3_TIPO",cTipo ,NIL},;  {"N3_BAIXA",cBaixa ,NIL},;  {"N3_TPSALDO",cTpSaldo ,NIL}}   //Array contendo os parametros do F12  aAdd( aParam, {"MV_PAR01",1} )//Pergunta 01 - Mostra Lanc. Contab? 1 = Sim ; 2 = Não  aAdd( aParam, {"MV_PAR02",2} )//Pergunta 02 - Aglutina Lancamento Contabil ? 1 = Sim ; 2 = Não  aAdd( aParam, {"MV_PAR03",1} )//Pergunta 03 - Contabaliza On-Line? 1 = Sim ; 2 = Não  aAdd( aParam, {"MV_PAR04",2} )//Pergunta 04 - Visualização ? 2 = Tipos de Ativos   // deve se usar obrigatoriamente o número 2   Begin Transaction  MsExecAuto({|a,b,c,d,e,f|ATFA036(a,b,c,d,e,f)},aCab,aAtivo,3,,.T./*lBaixaTodos*/,aParam)  If lMsErroAuto  MostraErro()  DisarmTransaction()  EndIf  End Transaction  RestArea(aArea)  Return ``` |

Exemplo:

Saiba mais:

[Exemplo de baixa de Ativos Imobilizados.](https://tdn.totvs.com/pages/releaseview.action?pageId=223912171)
