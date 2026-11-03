---
article_id: 23234880265239
category: Materiais - Compras (SIGACOM)
content_hash: a904254b8f4c6c3a62ac4f58766960325da033fe6cab29118fb61d5a8fedc6b7
fetched_at: '2026-06-28T22:41:25.287075+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Exclusão Documento de Entrada
type: support-article
updated_at: '2024-05-03T14:43:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234880265239-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Exclus%C3%A3o-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23234885316759) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para Exclusão do Documento de Entrada?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//EXCLUSÃO DE DOCUMENTO DE ENTRADA (SEM ABERTURA DE TELA)**

#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
   
User Function EXEC103()  
   
    Local   nOpc := 5  
    Local   aCab        := {}  
    Local   aItens      := {}  
    Local   aLinha      := {}  
    Local   aAuxDKD     := {}

    Private lMsErroAuto := .F.  
      
    PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "COM" FUNNAME "MATA103"

    aadd(aCab,{"F1\_TIPO" ,"N" ,NIL})  
    aadd(aCab,{"F1\_FORMUL" ,"N" ,NIL})  
    aadd(aCab,{"F1\_DOC" ,"M103STELA",NIL})  
    aadd(aCab,{"F1\_SERIE" ,"001" ,NIL})  
    aadd(aCab,{"F1\_EMISSAO" ,dDataBase,NIL})  
    aadd(aCab,{"F1\_DTDIGIT" ,dDataBase,NIL})  
    aadd(aCab,{"F1\_FORNECE" ,"000001" ,NIL})  
    aadd(aCab,{"F1\_LOJA" ,"01" ,NIL})  
    aadd(aCab,{"F1\_ESPECIE" ,"NFE" ,NIL})  
    aadd(aCab,{"F1\_COND" ,"000" ,NIL})  
    aAdd(aCab,{"F1\_STATUS","A",NIL})  
     
    aItens := {}  
    aAdd(aItens,{'D1\_DOC',"M103STELA",NIL})  
    aAdd(aItens,{'D1\_SERIE',"0001",NIL})  
    aAdd(aItens,{'D1\_FORNECE',"000001",NIL})  
    aAdd(aItens,{'D1\_LOJA',"01",NIL})  
    aAdd(aLinha,aItens)    
      
      
    MSExecAuto({|x,y,z,b,a| MATA103(x,y,z,b,,,,,,,,,,,a)},aCab,aLinha,nOpc,.F.,aAuxDKD)  
      
      
    If lMsErroAuto  
        MostraErro()  
    Else  
        Alert("Execauto MATA103 de exclusão sem tela executado com sucesso!")  
    EndIf  
       
    RESET ENVIRONMENT  
    
Return

**//EXCLUSÃO DE DOCUMENTO DE ENTRADA (COM ABERTURA DE TELA)**

#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
   
User Function EXEC103()   
    Local cNumDoc := "M103CTELA"  
    Local cSerie    := "001"  
    Local cForn     := "000001"  
    Local cLoja     := "01"  
      
    Local nOpc      := 5  
    Local   aCab    := {}  
    Local   aItens  := {}  
    Local   aLinha  := {}  
      
    Private lMsErroAuto := .F.  
      
      
    DbSelectArea("SF1")  
    SF1->(DbSetOrder(1))  
    SF1->(DbSeek(xFilial("SF1") + cNumDoc + cSerie + cForn + cLoja ))

    aadd(aCab,{"F1\_TIPO" ,      "N" ,NIL})  
    aadd(aCab,{"F1\_FORMUL" ,    "N" ,NIL})  
    aadd(aCab,{"F1\_DOC" ,       SF1->F1\_DOC,NIL})  
    aadd(aCab,{"F1\_SERIE" ,     SF1->F1\_SERIE ,NIL})  
    aadd(aCab,{"F1\_EMISSAO" ,   dDataBase,NIL})  
    aadd(aCab,{"F1\_DTDIGIT" ,   dDataBase,NIL})  
    aadd(aCab,{"F1\_FORNECE" ,   SF1->F1\_FORNECE ,NIL})  
    aadd(aCab,{"F1\_LOJA" ,      SF1->F1\_LOJA ,NIL})  
    aadd(aCab,{"F1\_ESPECIE" ,   SF1->F1\_ESPECIE ,NIL})

    dbSelectArea("SD1")  
    SD1->(dbSetOrder(1))  
    SD1->(DbSeek(xFilial("SD1")+SF1->F1\_DOC+SF1->F1\_SERIE+SF1->F1\_FORNECE+SF1->F1\_LOJA))  
      
    While !Eof() .And. SD1->D1\_FILIAL+SD1->D1\_DOC+SD1->D1\_SERIE+SD1->D1\_FORNECE+SD1->D1\_LOJA == ;  
    SF1->F1\_FILIAL+SF1->F1\_DOC+SF1->F1\_SERIE+SF1->F1\_FORNECE+SF1->F1\_LOJA           
        aItens := {}  
        aAdd(aItens,{'D1\_DOC',SD1->D1\_DOC       ,NIL})  
        aAdd(aItens,{'D1\_SERIE',SD1->D1\_SERIE   ,NIL})  
        aAdd(aItens,{'D1\_FORNECE',SD1->D1\_FORNECE,NIL})  
        aAdd(aItens,{'D1\_LOJA',SD1->D1\_LOJA     ,NIL})  
        aadd(aItens,{"D1\_ITEM",SD1->D1\_ITEM     ,NIL})  
        aadd(aItens,{"D1\_COD" ,SD1->D1\_COD      ,NIL})  
        aadd(aItens,{"D1\_UM"  ,SD1->D1\_UM       ,NIL})  
        aadd(aItens,{"D1\_LOCAL",SD1->D1\_LOCAL   ,NIL})  
        aadd(aItens,{"D1\_QUANT",SD1->D1\_QUANT   ,NIL})  
        aadd(aItens,{"D1\_VUNIT",SD1->D1\_VUNIT   ,NIL})  
        aadd(aItens,{"D1\_TOTAL",SD1->D1\_TOTAL   ,NIL})  
        aadd(aItens,{"D1\_TES"  ,SD1->D1\_TES     ,NIL})  
              
        aAdd(aLinha,aItens)  
        SD1->(dbSkip())  
    EndDo   
        
      
    MSExecAuto({|x,y,z,b,a| MATA103(x,y,z,b,,,,,,,,,,,a)},aCab,aLinha,nOpc,.T.,)  
      
    If lMsErroAuto  
        MostraErro()  
    EndIf

Return

**Saiba Mais:**

* [PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
