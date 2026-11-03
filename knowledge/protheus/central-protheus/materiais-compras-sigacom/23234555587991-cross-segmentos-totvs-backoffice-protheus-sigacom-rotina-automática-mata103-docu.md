---
article_id: 23234555587991
category: Materiais - Compras (SIGACOM)
content_hash: 8d36b1f226ff54673ff98c70f7b826d162f982c5b9cfb3ec55beab12405e6189
fetched_at: '2026-06-28T22:41:25.257768+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Guarda Fiscal para futura classificação
type: support-article
updated_at: '2024-05-03T18:04:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234555587991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Guarda-Fiscal-para-futura-classifica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23234563721495) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento de Guarda Fiscal para futura classificação?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Versão 12

**Solução**

Siga o exemplo abaixo:

**//GUARDA FISCAL - GRAVAR DADOS DA CLASSIFICAÇÃO DO DOCUMENTO PARA FUTURA FINALIZAÇÃO DA CLASSIFICAÇÃO**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCab := {}  
Local aItem := {}  
Local aItens := {}  
Local nOpc := 3  
Local cNum := ""  
Local nI := 0  
Local nX := 0  
Local nReg := 1  
Local cInicio := Time()

Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
Private lTemF1GFE := .F.

PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01 " MODULO "COM" FUNNAME "MATA103"

Conout( Replicate( '=', 30 ))  
Conout("Inicio: " + cInicio)

For nI := 1 To nReg  
    lMsErroAuto := .F.    
    aCab := {}  
    aItem := {}  
    aItens := {}

    nOpc := 3  
      
    If nOpc == 3   
        cNum := GetSxeNum("SF1","F1\_DOC")      
        SF1->(dbSetOrder(1))          
        While SF1->(dbSeek(xFilial("SF1")+cNum))              
            ConfirmSX8()              
            cNum := GetSxeNum("SF1","F1\_DOC")          
        EndDo  
    ElseIf nOpc == 4 .Or. nOpc == 5  
        cNum := "COMSP137 "   
    EndIf

    Conout("Documento: " + cNum)

    aadd( aCab, { "F1\_FORMUL"      , "N"         ,NIL } )  
    aadd( aCab, { "F1\_DOC"        , cNum        ,NIL } )  
    aadd( aCab, { "F1\_SERIE"      , "1  "          ,NIL } )  
    aadd( aCab, { "F1\_FORNECE"    , "000001"    ,NIL } )  
    aadd( aCab, { "F1\_LOJA"       , "01"      ,NIL } )  
    aadd( aCab, { "F1\_EMISSAO"    , DDATABASE    ,NIL } )  
    aadd( aCab, { "F1\_DTDIGIT"    , DDATABASE    ,NIL } )  
    aadd( aCab, { "F1\_TIPO"       , "N"         ,NIL } )  
    aadd( aCab, { "F1\_ESPECIE"     , "NFE"        ,NIL } )  
    aadd( aCab, { "F1\_COND"       , "000"     ,NIL } )   
  
    cProd1 := "000001"  
    cItem := StrZero(nX,TamSx3("D1\_ITEM")[1])  
    aItem := {}  
    aadd( aItem, { "D1\_ITEM"    , cItem                                , NIL } )  
    aadd( aItem, { "D1\_COD"       , PadR(cProd1,TamSx3("D1\_COD")[1])  , NIL } )  
    aadd( aItem, { "D1\_UM"      , "UN"                                , NIL } )  
    aadd( aItem, { "D1\_LOCAL"      , "01"                              , NIL } )  
    aadd( aItem, { "D1\_QUANT"     , 10                                  , NIL } )  
    aadd( aItem, { "D1\_VUNIT"      , 1000                                , NIL } )  
    aadd( aItem, { "D1\_TOTAL"      , 10000                                , NIL } )

    aAdd(aItens,aItem)  
      
    MSExecAuto( { |x,y,z| MATA140( x, y, z ) }, aCab, aItens, nOpc ) **// Inclusão Pré Nota**  
      
    If !lMsErroAuto   
        ConOut( "Incluido Pre Nota: " + cNum )  
        aItens := {}  
        aItem := {}  
        aadd( aItem, { "D1\_ITEM"    , cItem                                , NIL } )  
        aadd( aItem, { "D1\_COD"       , PadR(cProd1,TamSx3("D1\_COD")[1])  , NIL } )  
        aadd( aItem, { "D1\_UM"      , "UN"                                , NIL } )  
        aadd( aItem, { "D1\_LOCAL"      , "01"                              , NIL } )  
        aadd( aItem, { "D1\_QUANT"     , 10                                  , NIL } )  
        aadd( aItem, { "D1\_VUNIT"      , 1500                                , NIL } )  
        aadd( aItem, { "D1\_TOTAL"      , 15000                                , NIL } )  
        aadd( aItem, { "D1\_TES"       , "001"                             , NIL } )

        aAdd(aItens,aItem)

        nOpc := 4 **//Classificação**  
        lGrvGF := .T.

        MSExecAuto( { |a, b, c, d| MATA103( a, b, c, , , , , , , , , , , , , d ) }, aCab, aItens, nOpc, lGrvGF ) **// Realiza a gravação dos dados alterados sem finalizar a Classificação**

        If !lMsErroAuto   
            ConOut( "Classificado Documento Fiscal: " + cNum )  
        Else  
            MostraErro()

            ConOut( "Erro na inclusao!" )   
            Exit  
        EndIf  
    Else  
        MostraErro()

        ConOut( "Erro na inclusao!" )   
        Exit  
    EndIf  
Next nI

ConOut("Fim: " + Time())  
Conout( Replicate( '=', 30 ))

RESET ENVIRONMENT

Return .T.

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
