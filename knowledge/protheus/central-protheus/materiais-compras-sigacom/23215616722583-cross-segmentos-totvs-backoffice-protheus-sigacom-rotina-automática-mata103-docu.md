---
article_id: 23215616722583
category: Materiais - Compras (SIGACOM)
content_hash: 0dee57630f93e6ceeef851261b63798ab2a63631d46d9ab052898977a140ea5a
fetched_at: '2026-06-28T22:41:25.207880+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento com Aposentadoria Especial
type: support-article
updated_at: '2024-05-02T18:48:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23215616722583-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-com-Aposentadoria-Especial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23215616689047) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento com Aposentadoria Especial?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras- Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO TIPO NORMAL COM APOSENTADORIA ESPECIAL**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCab          := {}  
Local aItem         := {}  
Local aItens        := {}  
Local aItensApo     := {}  
Local nOpc          := 3  
Local cNum          := ""  
Local nI            := 0  
Local nX            := 0  
Local nReg          := 1

Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "1001" MODULO "COM" FUNNAME "MATA103" 

    If nOpc == 3  
        cNum := GetSxeNum("SF1","F1\_DOC")     
        SF1->(dbSetOrder(1))          
        While SF1->(dbSeek(xFilial("SF1")+cNum))              
            ConfirmSX8()              
            cNum := GetSxeNum("SF1","F1\_DOC")         
        EndDo  
    Elseif nOpc == 5  
       cNum := "000000004"  
    Endif         
  
    aadd(aCab,{"F1\_DOC"         ,cNum       ,NIL})  
    aadd(aCab,{"F1\_SERIE"       ,"1  "      ,NIL})  
    aadd(aCab,{"F1\_FORNECE"     ,"001   " ,NIL})  
    aadd(aCab,{"F1\_LOJA"        ,"01"         ,NIL})  
    aadd(aCab,{"F1\_EMISSAO"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_DTDIGIT"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_TIPO"        ,"N"        ,NIL})  
    aadd(aCab,{"F1\_FORMUL"      ,"N"        ,NIL})  
    aadd(aCab,{"F1\_ESPECIE"     ,"NFE"      ,NIL})  
    aadd(aCab,{"F1\_COND"        ,"001"      ,NIL})  
    aadd(aCab,{"F1\_EST"         ,"SP"       ,NIL})  
    aadd(aCab,{"F1\_DESPESA" , 0 , Nil})  
    aadd(aCab,{"F1\_DESCONT" , 0 , Nil})  
    aadd(aCab,{"F1\_SEGURO" , 0 , Nil})  
    aadd(aCab,{"F1\_FRETE" , 0 , Nil})  
    aadd(aCab,{"F1\_MOEDA" , 1 , Nil})  
    aadd(aCab,{"F1\_TXMOEDA" , 1 , Nil})  
    aadd(aCab,{"F1\_STATUS" , "A" , Nil})  
    aadd(aCab,{"F1\_VOLUME1",0, Nil})  
    aadd(aCab,{"F1\_PLIQUI",0, Nil})  
    aadd(aCab,{"F1\_PBRUTO",0, Nil})  
      
    For nX := 1 To 1  
        cProd1 :="0001            "   
          
        aItem := {}  
        aadd(aItem,{"D1\_ITEM"       ,StrZero(nX,4) ,NIL})  
        aadd(aItem,{"D1\_COD"        ,PadR(cProd1,TamSx3("D1\_COD")[1]) ,NIL})  
        aadd(aItem,{"D1\_UM"         ,"UN"   ,NIL})   
        aadd(aItem,{"D1\_LOCAL"      ,"01"   ,NIL})  
        aadd(aItem,{"D1\_QUANT"      ,1      ,NIL})   
        aadd(aItem,{"D1\_VUNIT"      ,1000     ,NIL})   
        aadd(aItem,{"D1\_TOTAL"      ,1000      ,NIL})  
        aadd(aItem,{"D1\_TES"        ,"001"  ,NIL})  
        aAdd(aItens,aItem)  
    Next nX  
      
    If nOpc == 3  
        aItem := {}  
        aAdd(aItensApo, Array(2))  
        aItensApo[Len(aItensApo)][1] := "0001"  
        aItensApo[Len(aItensApo)][2] := {}  
      
        aAdd(aItem, {"DHP\_FILIAL"   , xFilial("DHP")                    , Nil})  
        aAdd(aItem, {"DHP\_DOC"      , cNum                              , Nil})  
        aAdd(aItem, {"DHP\_SERIE"    , "1"                               , Nil})  
        aAdd(aItem, {"DHP\_FORNECE"  , "001   "                          , Nil})  
        aAdd(aItem, {"DHP\_LOJA"     , "01"                              , Nil})  
        aAdd(aItem, {"DHP\_FAIXA1"   , 10                                , Nil})  
        aAdd(aItem, {"DHP\_FAIXA2"   , 20                                , Nil})  
        aAdd(aItem, {"DHP\_FAIXA3"   , 30                                , Nil})  
        aAdd(aItensApo[Len(aItensApo)][2], aClone(aItem))  
    Endif  
      
    MSExecAuto({|x,y,z,a| MATA103(x,y,z,,,,,,,,,a)},aCab,aItens,nOpc,aItensApo)  
      
    If !lMsErroAuto  
        ConOut("    Incluido NF: " + cNum)   
    Else  
        MostraErro()  
        ConOut("Erro na inclusao!")  
        Exit  
    EndIf  
Next nI  
  
RESET ENVIRONMENT

Return

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)
