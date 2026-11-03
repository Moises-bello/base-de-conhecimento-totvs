---
article_id: 23234373176983
category: Materiais - Compras (SIGACOM)
content_hash: 2b0134d5ec77b710c7c3ed3a74338ea55d53ae5c59152f063829bdee68c46ab6
fetched_at: '2026-06-28T22:41:25.249619+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Entrega Futura
type: support-article
updated_at: '2024-05-03T14:21:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234373176983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Entrega-Futura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23234373151511) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento de Entrega Futura?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO ENTREGA FUTURA (DHQ)**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXECFUT()

Local aCab          := {}  
Local cNum         := "COM000"  
Local cNum1        := "COM001"  
Local aItem         := {}  
Local aItens        := {}  
Local cSerie    := "100"  
Local cFornec   := "000005"  
Local cLoja     := "01"  
Local cEspecie  := "NFE  "   
Local cProd1    := "001               "  
Local nX            := 0  
Local cTes       := "043"  
Local cPedido      := "TIR469"

Local nOpc     := 3 //3-Inclui / 5-Exclui

Private lMsErroAuto := .F.

PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM" FUNNAME "MATA103"

  If nOpc == 3

***// Compra com Entrega Futura (simples faturamento)***

    aadd(aCab,{"F1\_DOC"           ,cNum            ,NIL})  
    aadd(aCab,{"F1\_SERIE"          ,cSerie            ,NIL})  
    aadd(aCab,{"F1\_FORNECE"   ,cFornec         ,NIL})  
    aadd(aCab,{"F1\_LOJA"          ,cLoja              ,NIL})  
    aadd(aCab,{"F1\_EMISSAO"   ,DDATABASE   ,NIL})  
    aadd(aCab,{"F1\_DTDIGIT"     ,DDATABASE   ,NIL})  
    aadd(aCab,{"F1\_TIPO"        ,"N"                   ,NIL})  
    aadd(aCab,{"F1\_FORMUL"      ,"N"              ,NIL})  
    aadd(aCab,{"F1\_ESPECIE"     ,cEspecie        ,NIL})  
    aadd(aCab,{"F1\_COND"        ,"001"            ,NIL})  
    aadd(aCab,{"F1\_EST"           ,"SP"               ,NIL})  
    aadd(aCab,{"F1\_DESPESA" , 0                     ,NIL})  
    aadd(aCab,{"F1\_DESCONT" , 0                   ,NIL})  
    aadd(aCab,{"F1\_SEGURO" , 0                     ,NIL})  
    aadd(aCab,{"F1\_FRETE" , 0                        ,NIL})  
    aadd(aCab,{"F1\_MOEDA" , 1                     ,NIL})  
    aadd(aCab,{"F1\_TXMOEDA" , 1                 ,NIL})  
    aadd(aCab,{"F1\_STATUS" , "A"                  ,NIL})  
    aadd(aCab,{"F1\_VOLUME1",0                   ,NIL})  
    aadd(aCab,{"F1\_PLIQUI",0                        ,NIL})  
    aadd(aCab,{"F1\_PBRUTO",0                     ,NIL})

    For nX := 1 To 1  
        cProd1 :="001             "   
          
        aItem := {}  
        aadd(aItem,{"D1\_ITEM"       ,StrZero(nX,4) ,NIL})  
        aadd(aItem,{"D1\_COD"        ,PadR(cProd1,TamSx3("D1\_COD")[1]) ,NIL})  
        aadd(aItem,{"D1\_UM"         ,"UN"   ,NIL})   
        aadd(aItem,{"D1\_LOCAL"      ,"01"   ,NIL})  
        aAdd(aItem, {"D1\_PEDIDO" ,cPedido,Nil})  
        aAdd(aItem, {"D1\_ITEMPC", "0001",Nil})  
        aadd(aItem,{"D1\_QUANT"      ,100    ,NIL})   
        aadd(aItem,{"D1\_VUNIT"      ,100     ,NIL})   
        aadd(aItem,{"D1\_TOTAL"      ,10000      ,NIL})  
        aadd(aItem,{"D1\_TES"         ,cTes  ,NIL})  
        aAdd(aItens,aItem)  
    Next nX

   MSExecAuto({|x,y,z| MATA103(x,y,z)},aCab,aItens,nOpc)  
      
    If lMsErroAuto   
        MostraErro()  
    Else  
        Conout("Entrega Futura incluída: " + cNum)  
    Endif  
Endif

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

// ***Documento de Entrada representando a remessa da mercadoria***

aCab          := {}  
aItem         := {}  
aItens        := {}  
nX            := 0

 If nOpc == 3

    aadd(aCab,{"F1\_DOC"         ,cNum1    ,NIL})  
    aadd(aCab,{"F1\_SERIE"       ,cSerie     ,NIL})  
    aadd(aCab,{"F1\_FORNECE"     ,cFornec    ,NIL})  
    aadd(aCab,{"F1\_LOJA"        ,cLoja      ,NIL})  
    aadd(aCab,{"F1\_EMISSAO"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_DTDIGIT"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_TIPO"        ,"N"        ,NIL})  
    aadd(aCab,{"F1\_FORMUL"      ,"N"        ,NIL})  
    aadd(aCab,{"F1\_ESPECIE"     ,cEspecie   ,NIL})  
    aadd(aCab,{"F1\_COND"        ,"001"      ,NIL})  
    aadd(aCab,{"F1\_EST"         ,"SP"       ,NIL})  
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
        cProd1 :="001             "   
          
        aItem := {}  
        aadd(aItem,{"D1\_ITEM"       ,StrZero(nX,4) ,NIL})  
        aadd(aItem,{"D1\_COD"        ,PadR(cProd1,TamSx3("D1\_COD")[1]) ,NIL})  
        aadd(aItem,{"D1\_UM"         ,"UN"   ,NIL})   
        aadd(aItem,{"D1\_LOCAL"      ,"01"   ,NIL})  
        aadd(aItem,{"D1\_QUANT"      ,50     ,NIL})   
        aadd(aItem,{"D1\_VUNIT"      ,100    ,NIL})   
        aadd(aItem,{"D1\_TOTAL"      ,5000   ,NIL})  
        aadd(aItem,{"D1\_TES"        ,"496"  ,NIL})  
        aadd(aItem,{"AUT\_ENTFUT", {cNum,"100","0001",0,"0001",cFornec,cLoja},Nil})**//Dados para nota fiscal de origem**

        aAdd(aItens,aItem)  
    Next nX

   MSExecAuto({|x,y,z| MATA103(x,y,z)},aCab,aItens,nOpc)  
      
    If lMsErroAuto   
        MostraErro()  
    Else  
        Conout("Remessa Entrega Futura incluida: " + cNum1)  
    Endif

Endif  
RESET ENVIRONMENT

Return

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
