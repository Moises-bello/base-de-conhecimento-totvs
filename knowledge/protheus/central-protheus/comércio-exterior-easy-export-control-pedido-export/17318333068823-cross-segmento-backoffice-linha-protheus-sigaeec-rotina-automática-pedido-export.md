---
article_id: 17318333068823
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 6d8e9e603a1127682731e3e09c33edf24cdccec3222ec7d10a1d6366fd8a0987
fetched_at: '2026-06-28T22:36:59.162893+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAEEC - Rotina Automática Pedido
  Exportação "EECAP100".
type: support-article
updated_at: '2023-09-06T14:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17318333068823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEEC-Rotina-Autom%C3%A1tica-Pedido-Exporta%C3%A7%C3%A3o-EECAP100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17318295735319) Tempo aproximado para leitura: **05:00 min** **Dúvida**Preciso por gentileza de um exemplo de Rotina Automática para Alteração do Pedido de Exportação.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -*Easy Export Control*- Todas as versões  
  
**Solução**Para um melhor entendimento segue abaixo um *RDMake* com a inclusão, alteração e exclusão de um pedido e seus auxiliares.

```
#INCLUDE "TOTVS.CH"   
  
User Function MyEECAP100()  
Local lRot := .T.  
Local cPedido := "0000000001"  
Private aPDocs       := {}  
Private aPPedidos    := {}  
Private aPAgentes    := {}  
Private aPNotifys    := {}  
Private aPProdutos   := {}  
Private aCondPag    := {}  
Private aEmb        := {}  
  
/************************  
//Inicializa o ambiente  
*************************/  
RpcSetEnv("99", "01")  
nModulo := 29  
cModulo := "EEC"  
__CUSERID := "000000"  
  
while lRot  
    //Executa a integração para Incluir o Pedido  
    If MsgYesNo("Deseja Incluir o Pedido e Auxiliares?", "Aviso")  
        IncAP100(cPedido, 3, 3)  
    //Executa a Alteração Alterando o Pedido e Reenviando os Auxiliares  
    elseIf MsgYesNo("Deseja Alterar o Pedido e Auxiliares?", "Aviso")  
        IncAP100(cPedido, 4, 4)  
    //Executa a Alteração Alterando o Pedido e Excluindo os Auxiliares  
    elseIf MsgYesNo("Deseja Alterar o Pedido e Excluir Auxiliares?", "Aviso")  
        IncAP100(cPedido, 4, 5)  
    //Executa a Alteração Excluindo o Pedido  
    elseIf MsgYesNo("Deseja Excluir o Pedido?", "Aviso")  
        IncAP100(cPedido, 5, 5)  
    elseIf MsgYesNo("Deseja parar a rotina?", "Aviso")  
        lRot := .F.  
    EndIf  
  
enddo  
  
Return Nil  
/*****************************************************************  
******************************************************************/  
Static Function IncAP100(cPedido, nOpc, nOpcDet)  
Local aCab := {}, aItens := {}, aAux := {}  
Local nP := 0, nI, nN, nD  
Local cFornece := ""  
Local cFoLoja := ""  
Private lMsErroAuto := .f.  
  
aPDocs       := {}  
aPPedidos    := {}  
aPAgentes    := {}  
aPNotifys    := {}  
aPProdutos   := {}  
aCondPag     := {}  
aEmb         := {}  
  
aItens := {}  
aItem := {}  
  
if nOpc == 3  
  
      aCab := {}  
      aadd( aCab , {'EE7_PEDIDO'   , cPedido                 , NIL} )  
      aadd( aCab , {'EE7_IMPORT'   , "000001"                , NIL} )  
      aadd( aCab , {'EE7_IMLOJA'   , "01"                    , NIL} )  
      aadd( aCab , {'EE7_IMPODE'   , "NOME CLIENTE"          , NIL} )  
      aadd( aCab , {'EE7_FORN'     , "000001"                , NIL} )  
      aadd( aCab , {'EE7_FOLOJA'   , "01"                    , NIL} )  
      aadd( aCab , {'EE7_IDIOMA'   , "INGLES-INGLES"         , NIL} )  
      aadd( aCab , {'EE7_CONDPA'   , "00001"                 , NIL} )  
      aadd( aCab , {'EE7_MPGEXP'   , "003"                   , NIL} )  
      aadd( aCab , {'EE7_INCOTE'   , 'FOB'                   , NIL} )  
      aadd( aCab , {'EE7_FRPPCC'   , "CC"                    , NIL} )  
      aadd( aCab , {'EE7_MOEDA'    , 'US$'                   , NIL} )  
      aadd( aCab , {'EE7_CALCEM'   , '1'                     , NIL} )  
      aadd( aCab , {'EE7_VIA'      , "001"                   , NIL} )  
  
//Enviando o ATUEMB igual a S, o sistema realizará a integração automática do Embarque de Exportação.  
aAdd(aCab, {"ATUEMB", "S", Nil})   
  
      aAdd(aItem, {'EE8_SEQUEN'    , str(1)                  , NIL} )  
      aAdd(aItem, {'EE8_COD_I'     , "0000000001"            , NIL} )  
      aAdd(aItem, {'EE8_FORN'      , "000001"                , NIL} )  
      aAdd(aItem, {'EE8_FOLOJA'    , "01"                    , NIL} )  
      aAdd(aItem, {'EE8_SLDINI'    , 100                     , NIL} )  
      aAdd(aItem, {'EE8_EMBAL1'    , "001"                   , NIL} )  
      aAdd(aItem, {'EE8_QE'        , 1                       , NIL} )  
      aAdd(aItem, {'EE8_PRECO '    , 100                     , NIL} )  
      aAdd(aItem, {'EE8_PSLQUN'    , 1                       , NIL} )  
      aAdd(aItem, {'EE8_TES'       , "501"                   , NIL} )  
      aAdd(aItem, {'EE8_POSIPI'    , "00000000"              , NIL} )  
      aAdd(aItem, {"AUTDELETA"     , "N"                     , Nil} )  
      AADD( aItens, aClone(aItem))  
      aItem := {}  
  
Elseif nOpc == 4  
      aadd( aCab , {'EE7_PEDIDO'   , cPedido                 , NIL} )  
      aadd( aCab , {'EE7_IMPORT'   , "000001"                , NIL} )  
      aadd( aCab , {'EE7_IMLOJA'   , "01"                    , NIL} )  
      aadd( aCab , {'EE7_IMPODE'   , "NOME CLIENTE"          , NIL} )  
      aadd( aCab , {'EE7_FORN'     , "000001"                , NIL} )  
      aadd( aCab , {'EE7_FOLOJA'   , "01"                    , NIL} )  
      aadd( aCab , {'EE7_IDIOMA'   , "INGLES-INGLES"         , NIL} )  
      aadd( aCab , {'EE7_CONDPA'   , "00002"                 , NIL} )  
      aadd( aCab , {'EE7_MPGEXP'   , "003"                   , NIL} )  
      aadd( aCab , {'EE7_INCOTE'   , 'FOB'                   , NIL} )  
      aadd( aCab , {'EE7_FRPPCC'   , "CC"                    , NIL} )  
      aadd( aCab , {'EE7_MOEDA'    , 'US$'                   , NIL} )  
      aadd( aCab , {'EE7_CALCEM'   , '1'                     , NIL} )  
      aadd( aCab , {'EE7_VIA'      , "002"                   , NIL} )   
  
      aAdd(aItem, {'EE8_SEQUEN'    , str(1)                  , NIL} )  
      aAdd(aItem, {'EE8_COD_I'     , "0000000001"            , NIL} )  
      aAdd(aItem, {'EE8_FORN'      , "000001"                , NIL} )  
      aAdd(aItem, {'EE8_FOLOJA'    , "01"                    , NIL} )  
      aAdd(aItem, {'EE8_SLDINI'    , 100                     , NIL} )  
      aAdd(aItem, {'EE8_EMBAL1'    , "001"                   , NIL} )  
      aAdd(aItem, {'EE8_QE'        , 1                       , NIL} )  
      aAdd(aItem, {'EE8_PRECO '    , 100                     , NIL} )  
      aAdd(aItem, {'EE8_PSLQUN'    , 1                       , NIL} )  
      aAdd(aItem, {'EE8_TES'       , "501"                   , NIL} )  
      aAdd(aItem, {'EE8_POSIPI'    , "00000000"              , NIL} )  
      aAdd(aItem, {"AUTDELETA"     , "S"                     , Nil} )  
      AADD( aItens, aClone(aItem))  
      aItem := {}  
  
      aAdd(aItem, {'EE8_SEQUEN'    , str(1)                  , NIL} )  
      aAdd(aItem, {'EE8_COD_I'     , "0000000002"            , NIL} )  
      aAdd(aItem, {'EE8_FORN'      , "000001"                , NIL} )  
      aAdd(aItem, {'EE8_FOLOJA'    , "01"                    , NIL} )  
      aAdd(aItem, {'EE8_SLDINI'    , 200                     , NIL} )  
      aAdd(aItem, {'EE8_EMBAL1'    , "002"                   , NIL} )  
      aAdd(aItem, {'EE8_QE'        , 2                       , NIL} )  
      aAdd(aItem, {'EE8_PRECO '    , 200                     , NIL} )  
      aAdd(aItem, {'EE8_PSLQUN'    , 2                       , NIL} )  
      aAdd(aItem, {'EE8_TES'       , "501"                   , NIL} )  
      aAdd(aItem, {'EE8_POSIPI'    , "00000000"              , NIL} )  
      aAdd(aItem, {"AUTDELETA"     , "N"                     , Nil} )  
      AADD( aItens, aClone(aItem))  
      aItem := {}  
  
elseIf nOpc == 5  
      aadd( aCab , {'EE7_PEDIDO'   , cPedido                 , NIL} )  
      aadd( aCab , {'EE7_IMPORT'   , "000001"                , NIL} )  
      aadd( aCab , {'EE7_IMLOJA'   , "01"                    , NIL} )  
      aadd( aCab , {'EE7_FORN'     , "000001"                , NIL} )  
      aadd( aCab , {'EE7_FOLOJA'   , "01"                    , NIL} )  
      aAdd( aCab , {"AUTDELETA"    ,"S"                      , Nil})   
  
      aAdd(aItem, {'EE8_SEQUEN'    , str(1)                  , NIL} )  
      aAdd(aItem, {'EE8_COD_I'     , "0000000002"            , NIL} )  
      aAdd(aItem, {'EE8_FORN'      , "000001"                , NIL} )  
      aAdd(aItem, {'EE8_FOLOJA'    , "01"                    , NIL} )  
      aAdd(aItem, {"AUTDELETA"     ,"S"                      , Nil} )  
      AADD( aItens, aClone(aItem))  
      aItem := {}  
  
EndIf  
  
// Complementos dos pedido Notifys, Documentos e Agentes  
If alltrim(str(nOpcDet)) $ "3|4|5" .and. nOpc <> 5  
   aAux := {}  
  
   // Notifys  
   aNotifys := {}  
   aNotify := {}  
  
   if nOpcDet == 3 // inclusão dos notifys   
  
         aAdd(aNotify, {"EEN_IMPORT", "000001"        , Nil})  
         aAdd(aNotify, {"EEN_IMLOJA", "01"            , Nil})  
  
   elseif nOpcDet == 4 // alteração dos notifys  
  
         aAdd(aNotify, {"EEN_IMPORT", "000001"        , Nil})  
         aAdd(aNotify, {"EEN_IMLOJA", "01"            , Nil})  
         aAdd(aNotify, {"AUTDELETA" , "S"             , Nil})   
  
         aAdd(aNotify, {"EEN_IMPORT", "000002"        , Nil})  
         aAdd(aNotify, {"EEN_IMLOJA", "01"            , Nil})  
         aAdd(aNotify, {"AUTDELETA" , "N"             , Nil})   
  
   elseIf nOpcDet == 5 // exclusão do notify  
  
         aAdd(aNotify, {"EEN_IMPORT", "000001"        , Nil})  
         aAdd(aNotify, {"EEN_IMLOJA", "01"            , Nil})  
         aAdd(aNotify, {"AUTDELETA" , "S"             , Nil})  
  
 EndIf  
  
   aAdd(aNotifys, aNotify)  
   aAdd(aAux, {"EEN", aNotifys})  
  
   // Documentos  
   aDocs := {}  
   aDoc := {}  
   if nOpcDet == 3 // inclusão dos Documentos   
  
         aAdd(aDoc, {"EXB_TIPO"  , "1"           , Nil})  
         aAdd(aDoc, {"EXB_CODATV", "01"          , Nil})   
  
   elseif nOpcDet == 4 // alteração dos Documentos  
  
         aAdd(aDoc, {"EXB_TIPO"  , "1"           , Nil})  
         aAdd(aDoc, {"EXB_CODATV", "01"          , Nil})  
         aAdd(aDoc, {"AUTDELETA" , "S"           , Nil})   
  
         aAdd(aDoc, {"EXB_TIPO"  , "1"           , Nil})  
         aAdd(aDoc, {"EXB_CODATV", "02"          , Nil})  
         aAdd(aDoc, {"AUTDELETA" ,"N"            , Nil})   
  
   elseIf nOpcDet == 5  // exclusão do documento  
  
         aAdd(aDoc, {"EXB_TIPO"  , "1"           , Nil})  
         aAdd(aDoc, {"EXB_CODATV", "02"          , Nil})  
         aAdd(aDoc, {"AUTDELETA" , "S"           , Nil})   
  
   EndIf  
   aAdd(aDocs, aDoc)  
   aAdd(aAux, {"EXB", aDocs})   
  
   // Agentes  
   aAgentes := {}  
   aAgente := {}  
   if nOpcDet == 3 // inclusão dos Agentes   
  
         aAdd(aAgente, {"EEB_CODAGE", "001"           , Nil})  
         aAdd(aAgente, {"EEB_TIPCOM", "1"             , Nil}) // 1-A Remeter | 2-Conta Grafcica | 3-Deduzir da Fatura  
         aAdd(aAgente, {"EEB_TIPCVL", "2"             , Nil}) // 1-Percentual | 2-Valor Fixo | 3-Percentual por item  
         aAdd(aAgente, {"EEB_VALCOM", 10           , Nil})  
         aAdd(aAgente, {"EEB_REFAGE", "NOME AGENTE"   , Nil})  
  
   elseif nOpcDet == 4 // alteração dos Agentes  
  
         aAdd(aAgente, {"EEB_CODAGE", "001"           , Nil})  
         aAdd(aAgente, {"EEB_TIPCOM", "1"             , Nil}) // 1-A Remeter | 2-Conta Grafcica | 3-Deduzir da Fatura  
         aAdd(aAgente, {"EEB_TIPCVL", "2"             , Nil}) // 1-Percentual | 2-Valor Fixo | 3-Percentual por item  
         aAdd(aAgente, {"EEB_VALCOM", 10           , Nil})  
         aAdd(aAgente, {"EEB_REFAGE", "NOME AGENTE"   , Nil})  
         aAdd(aAgente, {"AUTDELETA" ,"S" , Nil})  
  
         aAdd(aAgente, {"EEB_CODAGE", "002"           , Nil})  
         aAdd(aAgente, {"EEB_TIPCOM", "1"             , Nil}) // 1-A Remeter | 2-Conta Grafcica | 3-Deduzir da Fatura  
         aAdd(aAgente, {"EEB_TIPCVL", "2"             , Nil}) // 1-Percentual | 2-Valor Fixo | 3-Percentual por item  
         aAdd(aAgente, {"EEB_VALCOM", 10           , Nil})  
         aAdd(aAgente, {"EEB_REFAGE", "NOME AGENTE"   , Nil})  
         aAdd(aAgente, {"AUTDELETA" ,"N" , Nil})  
  
   elseIf nOpcDet == 5  // exclusão do agente  
  
         aAdd(aAgente, {"EEB_CODAGE", "002"           , Nil})  
         aAdd(aAgente, {"EEB_TIPCOM", "1"             , Nil}) // 1-A Remeter | 2-Conta Grafcica | 3-Deduzir da Fatura  
         aAdd(aAgente, {"EEB_TIPCVL", "2"             , Nil}) // 1-Percentual | 2-Valor Fixo | 3-Percentual por item  
         aAdd(aAgente, {"AUTDELETA" ,"S" , Nil})  
  
   EndIf  
   aAdd(aAgentes, aAgente)  
   aAdd(aAux, {"EEB", aAgentes})  
  
EndIf  
  
   // execução DA rotina automática  
   MsAguarde({|| MSExecAuto( {|X,Y,Z,Aux| EECAP100(X,Y,Z,Aux)},aCab ,aItens, nOpc, aAux) }, "Integrando Pedido Automático")  
  
If lMsErroAuto  
        MostraErro()  
        lMsErroAuto := .F.  
    Else  
        cAcao := iif( nOpc == 3 , " incluido",iif(nOpc==4," alterado"," excluido"))  
        MsgInfo("Pedido " + cAcao + " com sucesso!", "Aviso")  
    EndIf  
  
Return
```

**Saiba Mais****[EECAP100 - MsExecAuto Rotina Automática de Pedido de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=394219396)**
