---
article_id: 23233715771031
category: Materiais - Compras (SIGACOM)
content_hash: 5297906501c9fd9e3e5c6ae91d8dac59902cc4d67b30b8eee8e6d651caf4815e
fetched_at: '2026-06-28T22:41:25.188352+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Beneficiamento  Terceiros
type: support-article
updated_at: '2024-05-03T14:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23233715771031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Beneficiamento-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23233708325143) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento de Beneficiamento Terceiros?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - A partir da 12.1.2210 **Solução**

Siga o exemplo abaixo:

**//DOCUMENTO BENEFICIAMENTO - Terceiros**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCab          := {}  
Local aItem         := {}  
Local aItens        := {}  
Local nOpc          := 3  
Local cNum          := ""  
Local nI            := 0  
Local nX            := 0  
Local nReg          := 1  
Local cInicio       := Time()

Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "1001" MODULO "COM" FUNNAME "MATA103"  
  
For nI := 1 To nReg  
    lMsErroAuto := .F.    
    aCab := {}  
    aItem := {}  
    aItens := {}  
     
    If nOpc == 3  
        cNum := GetSxeNum("SF1","F1\_DOC")    
        SF1->(dbSetOrder(1))          
        While SF1->(dbSeek(xFilial("SF1")+cNum))              
            ConfirmSX8()              
            cNum := GetSxeNum("SF1","F1\_DOC")        
        EndDo  
    Endif        
  
    aadd(aCab,{"F1\_DOC"         ,cNum       ,NIL})  
    aadd(aCab,{"F1\_SERIE"       ,"1  "      ,NIL})  
    aadd(aCab,{"F1\_FORNECE"     ,"001   "   ,NIL})  
    aadd(aCab,{"F1\_LOJA"        ,"01"       ,NIL})  
    aadd(aCab,{"F1\_EMISSAO"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_DTDIGIT"     ,DDATABASE  ,NIL})  
    **aadd(aCab,{"F1\_TIPO"        ,"B"        ,NIL})**  
    aadd(aCab,{"F1\_FORMUL"      ,"N"        ,NIL})  
    aadd(aCab,{"F1\_ESPECIE"     ,"NFE"      ,NIL})  
    aadd(aCab,{"F1\_COND"        ,"001"      ,NIL})  
    aadd(aCab,{"F1\_DESPESA" , 0 , Nil})  
    aadd(aCab,{"F1\_DESCONT" , 0 , Nil})  
    aadd(aCab,{"F1\_SEGURO" , 0 , Nil})  
    aadd(aCab,{"F1\_FRETE" , 0 , Nil})  
    aadd(aCab,{"F1\_MOEDA" , 1 , Nil})  
    aadd(aCab,{"F1\_TXMOEDA" , 1 , Nil})  
    aadd(aCab,{"F1\_STATUS" , "A" , Nil})  
    aadd(aCab,{"F1\_VOLUME1",0, Nil})  
    aadd(aCab,{"F1\_PLIQUI",0, Nil})  
    aadd(aCab,{"F1\_PBRUTO",0, Nil})  
     
    For nX := 1 To 1  
        cProd1 := "0001           "  
         
        aItem := {}  
        aadd(aItem,{"D1\_ITEM"       ,"0001" ,NIL})  
        aadd(aItem,{"D1\_COD"        ,PadR(cProd1,TamSx3("D1\_COD")[1]) ,NIL})  
        aadd(aItem,{"D1\_UM"         ,"UN"   ,NIL})  
        aadd(aItem,{"D1\_LOCAL"      ,"01"   ,NIL})  
        aadd(aItem,{"D1\_QUANT"      ,10     ,NIL})  
        aadd(aItem,{"D1\_VUNIT"      ,10     ,NIL})  
        aadd(aItem,{"D1\_TOTAL"      ,100        ,NIL})  
        **aadd(aItem,{"D1\_NFORI"      ,"000132   ",NIL})**  
**aadd(aItem,{"D1\_SERIORI"    ,"1  " ,NIL})**  
**aadd(aItem,{"D1\_ITEMORI"    ,"01" ,NIL})**  
**aadd(aItem,{"D1\_IDENTB6"    ,"000755" ,NIL})**  
**aadd(aItem,{"D1\_TES"        ,"022"  ,NIL}) //TES DEVOLUCAO - Poder3**  
        aAdd(aItens,aItem)  
         
    Next nX  
     
    /\*If nOpc == 3  
        aItem := {}  
        aAdd(aItensRat, Array(2))  
        aItensRat[Len(aItensRat)][1] := "0001"  
        aItensRat[Len(aItensRat)][2] := {}  
     
        aAdd(aItem, {"DE\_FILIAL"    , xFilial("SDE")                    , Nil})  
        aAdd(aItem, {"DE\_ITEM"      , StrZero(1,TamSx3("DE\_ITEM")[1])   , Nil})  
        aAdd(aItem, {"DE\_DOC"       , cNum                              , Nil})  
        aAdd(aItem, {"DE\_SERIE"     , "1"                               , Nil})  
        aAdd(aItem, {"DE\_FORNECE"   , "001   "                          , Nil})  
        aAdd(aItem, {"DE\_LOJA"      , "01"                              , Nil})  
        aAdd(aItem, {"DE\_ITEMNF"    , "0001"                            , Nil})  
        aAdd(aItem, {"DE\_PERC"      , 100                               , Nil})  
        aAdd(aItem, {"DE\_CC"        , "01"                              , Nil})  
        aAdd(aItensRat[Len(aItensRat)][2], aClone(aItem))  
    Endif \*/  
  
    MSExecAuto({|x,y,z,a| MATA103(x,y,z)},aCab,aItens,nOpc)

    If !lMsErroAuto  
        ConOut("    Incluido NF: " + cNum)    
    Else  
        MostraErro()  
        ConOut("Erro na inclusao!")  
        Exit  
    EndIf  
Next nI  
  
Conout("Inicio: " + cInicio)  
ConOut("Fim: " + Time())  
  
RESET ENVIRONMENT  
  
Return

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
