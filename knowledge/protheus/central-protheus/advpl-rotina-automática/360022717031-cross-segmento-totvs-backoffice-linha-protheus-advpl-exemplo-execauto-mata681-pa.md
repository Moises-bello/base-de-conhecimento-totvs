---
article_id: 360022717031
category: ADVPL - Rotina Automática
content_hash: 474edf1b486a0a9be1e9b083add8a34d86b092491aac040cd87313f86f01da91
fetched_at: '2026-06-28T22:40:24.991098+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Exemplo execauto
  MATA681 para inclusão e estorno
type: support-article
updated_at: '2022-07-21T20:02:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022717031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exemplo-execauto-MATA681-para-inclus%C3%A3o-e-estorno
---

**Dúvida**Preciso de um exemplo da ExecAuto para estorno e inclusão de apontamento da rotina **MATA681**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.  
  
**Solução**

**Inclusão**

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
User Function RMATA681()  
  
    Local aVetor := {}  
    Local dData  
    Local nOpc   := 3 //Incluir  
    Private lMsErroAuto :=.F.  
    Private lMsHelpAuto :=.T.  
  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM" TABLES "SH6"  
  
    dData:=dDataBase  
    aVetor := {;  
        {"H6_OP"      ,"00001601001   "         ,NIL},;  
        {"H6_PRODUTO" ,"01             "        ,NIL},;  
        {"H6_OPERAC"  ,"01"                     ,NIL},;  
        {"H6_DTAPONT" ,dData                    ,NIL},;  
        {"H6_DATAINI" ,dData                    ,NIL},;  
        {"H6_HORAINI" ,"19:11"                  ,NIL},;  
        {"H6_DATAFIN" ,dData                    ,NIL},;  
        {"H6_HORAFIN" ,"19:20"                  ,NIL},;  
        {"H6_PT"      ,'P'                      ,NIL},;  
        {"H6_LOCAL"   ,"01"                     ,NIL},;  
        {"H6_QTDPROD" ,7                        ,NIL}}  
  
        MSExecAuto({|x| mata681(x)},aVetor, nOpc)  
  
    If lMsErroAuto  
        If (!IsBlind())  
            MostraErro()  
        Else // EM ESTADO DE JOB  
            cError := MostraErro("/dirdoc", "error.log") // ARMAZENA A MENSAGEM DE ERRO  
  
        ENDIF  
    Else  
  
        ConOut(Repl("-", 80))  
        ConOut(PadC("Teste MATA681 finalizado com sucesso!", 80))  
        ConOut(PadC("Fim: " + Time(), 80))  
        ConOut(Repl("-", 80))  
    EndIf  
Return  
```

**Estorno**

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
User Function TMATA681()  
  
Local nOpc :=5// estorno  
Local aCabec := {}  
  
Private lMsErroAuto :=.F.  
Private lMsHelpAuto :=.T.  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM" TABLES "SH6"  
  
   // INÍCIO: estorno //  
If nOpc ==5  
  
DBSelectArea("SH6")  
DBSetOrder(3)//H6_FILIAL, H6_PRODUTO, H6_OP, H6_OPERAC, H6_LOTECTL, H6_NUMLOTE, R_E_C_N_O_, D_E_L_E_T_  
MsSeek(xFilial("SH6") +"SERV0001 "+"00001901001 "+"01"+"LOTE0004 ")  
aCabec := { {"H6_OP", SH6->H6_OP   , NIL},;  
  
{"H6_PRODUTO", SH6->H6_PRODUTO , NIL},;  
{"H6_OPERAC", SH6->H6_OPERAC , NIL},;  
{"H6_RECURSO", SH6->H6_RECURSO , NIL},;  
{"H6_DTAPONT", SH6->H6_DTAPONT , NIL},;  
{"H6_DATAINI", SH6->H6_DATAINI , NIL},;  
{"H6_HORAINI", SH6->H6_HORAINI , NIL},;  
{"H6_DATAFIN", SH6->H6_DATAFIN , NIL},;  
{"H6_HORAFIN", SH6->H6_HORAFIN , NIL},;  
{"H6_PT", SH6->H6_PT   , NIL},;  
{"H6_LOCAL", SH6->H6_LOCAL   , NIL},;  
{"H6_LOTECTL", SH6->H6_LOTECTL , NIL},;  
{"H6_QTDPROD", SH6->H6_QTDPROD , NIL},;  
{"AUTRECNO", SH6->(Recno()) , Nil}}  
  
EndIf  
  
   // FIM: estorno //  
MsExecAuto({|x, y| MATA681(x, y)}, aCabec, nOpc)
```

```
   If lMsErroAuto  
        If (!IsBlind())  
            MostraErro()  
        Else // EM ESTADO DE JOB  
            cError := MostraErro("/dirdoc", "error.log") // ARMAZENA A MENSAGEM DE ERRO  
        ENDIF  
    Else  
        ConOut(Repl("-", 80))  
        ConOut(PadC("Teste MATA681 finalizado com sucesso!", 80))  
        ConOut(PadC("Fim: " + Time(), 80))  
        ConOut(Repl("-", 80))  
    EndIf  
  
    RESET ENVIRONMENT  
Return NIL
```

**Saiba Mais  
[MATA681 - Apontamento de Produção baseado no Roteiro de Operações](http://tdn.totvs.com/pages/releaseview.action?pageId=6089272)**
