---
article_id: 23233946973719
category: Materiais - Compras (SIGACOM)
content_hash: add5e33432d6f18a1ed29e919e9939274e6c8bbfb8dcd1884fd4d5fcef78c965
fetched_at: '2026-06-28T22:41:25.218589+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Complemento ICMS ou IPI
type: support-article
updated_at: '2024-05-03T14:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23233946973719-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Complemento-ICMS-ou-IPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23233954491287) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento de Complemento ICMS ou IPI?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO COMPLEMENTO ICMS ou IPI**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCab          := {}  
Local aItem         := {}  
Local aItens        := {}  
Local nOpc          := 3  
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

    aadd(aCab,{"F1\_SERIE"       ,"1  "      ,NIL})  
    aadd(aCab,{"F1\_FORNECE"     ,"001   "   ,NIL})  
    aadd(aCab,{"F1\_LOJA"        ,"01"       ,NIL})  
    aadd(aCab,{"F1\_EMISSAO"     ,DDATABASE  ,NIL})  
    aadd(aCab,{"F1\_DTDIGIT"     ,DDATABASE  ,NIL})  
    **aadd(aCab,{"F1\_TIPO"        ,"I"        ,NIL}) // I - Complemento ICMS / P - Complemento IPI**  
    aadd(aCab,{"F1\_FORMUL"      ,"S"        ,NIL})  
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
        **aadd(aItem,{"D1\_VUNIT"      ,10     ,NIL})**  
**aadd(aItem,{"D1\_TOTAL"      ,100        ,NIL})**  
        **aadd(aItem,{"D1\_NFORI"      ,"000132   ",NIL})**  
**aadd(aItem,{"D1\_SERIORI"    ,"1  " ,NIL})**  
**aadd(aItem,{"D1\_ITEMORI"    ,"01" ,NIL})**  
aadd(aItem,{"D1\_TES"        ,"066"  ,NIL})   
        aAdd(aItens,aItem)  
         
    Next nX

    MSExecAuto({|x,y,z,a| MATA103(x,y,z)},aCab,aItens,nOpc)

    If !lMsErroAuto  
        ConOut("   NF\_incluída)    
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
