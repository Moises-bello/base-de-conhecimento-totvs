---
article_id: 23215228960023
category: Materiais - Compras (SIGACOM)
content_hash: cd896755987bfc87a279d870d014269f0950750ee3713e78be0f18c6dbe88bf1
fetched_at: '2026-06-28T22:41:25.230775+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento de Cobertura
type: support-article
updated_at: '2024-05-02T18:46:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23215228960023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-de-Cobertura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23215228934807) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento de Cobertura?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras- Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO COBERTURA**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

#Include "Coverege[.ch](http://tbiconn.ch/)"

User Function EXECCOB()

Local cDocDef   := "200001   "  
Local cSerDef   := "1  "  
Local cForn     := "001   "  
Local cLoja     := "01"  
Local cProduto  := "0001"  
Local nQuantidad:= 2 

Local cDocOri   := "000130   "  
Local cSerOri   := "1  "  
Local cSeqOri   := ""  
Local cTpMov    := "1"  
Local cCodCli   := ""  
Local cLojCli   := ""  
Local cDHOper   := "1"  
Local aCab103   := {}  
Local aDadosCob := {}  
Local cTes      := "001"  
Local nOpcX     := 3 //3-Inclui / 5-Exclui  
  
Private lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "1001" MODULO "COM" FUNNAME "MATA103"  
  
cDocDef     := Padr(cDocDef,TamSX3("DH\_DOC")[1])  
cSerDef     := Padr(cSerDef,TamSX3("DH\_SERIE")[1])  
cForn       := Padr(cForn,TamSX3("DH\_FORNECE")[1])  
cLoja       := Padr(cLoja,TamSX3("DH\_LOJAFOR")[1])  
cProduto    := Padr(cProduto,TamSX3("DH\_PRODUTO")[1])  
  
cDocOri     := Padr(cDocOri,TamSX3("DH\_DOC")[1])  
cSerOri     := Padr(cSerOri,TamSX3("DH\_SERIE")[1])  
cSeqOri     := Padr("0001",TamSX3("DH\_ITEM")[1])  
cCodCli     := Padr(cCodCli,TamSX3("DH\_CLIENTE")[1])  
cLojCli     := Padr(cLojCli,TamSX3("DH\_LOJACLI")[1])  
cTpMov      := Padr('1',TamSX3("DH\_TPMOV")[1])  
cDHOper     := Padr( cDHOper,        TamSX3("DH\_OPER")[1] )  
  
DbSelectArea("SDH")  
SDH->(DbSetOrder(2))  
If SDH->(DbSeek(xFilial('SDH')+cTpMov+cSerDef+cDocDef+cSeqOri+cCodCli+cLojCli+cForn+cLoja+cDHOper))  
                              
    aAdd(aCab103,{"F1\_DOC"    , cDocDef     , Nil})  
    aAdd(aCab103,{"F1\_SERIE"  , cSerDef     , Nil})  
    aAdd(aCab103,{"F1\_TIPO"   , "N"         , Nil})  
    aAdd(aCab103,{"F1\_FORNECE", cForn       , Nil})  
    aAdd(aCab103,{"F1\_LOJA"   , cLoja   , Nil})  
    aAdd(aCab103,{"F1\_EMISSAO", dDataBase, Nil})  
    aAdd(aCab103,{"F1\_DTDIGIT", dDataBase, Nil})  
    aAdd(aCab103,{"F1\_FORMUL" , "N"         , Nil})  
    aAdd(aCab103,{"F1\_ESPECIE", "NFE"   , Nil})  
    aAdd(aCab103,{"F1\_COND"   , "001"   , Nil})  
  
    aAdd(aDadosCob,Array(CB\_MAXCOL))    
                                                                      
    aTail(aDadosCob)[CB\_DOC]        := cDocOri  
    aTail(aDadosCob)[CB\_SERIE]      := cSerOri  
    aTail(aDadosCob)[CB\_SEQ]        := cSeqOri  
    aTail(aDadosCob)[CB\_VLRUNIT]    := 1000  
    aTail(aDadosCob)[CB\_TES]        := cTes  
    aTail(aDadosCob)[CB\_REGSDH]     := SDH->(Recno())  
    aTail(aDadosCob)[CB\_PRODUTO]    := cProduto        
    aTail(aDadosCob)[CB\_QUANT]      := nQuantidad        
    aTail(aDadosCob)[CB\_BASIPI]     := 0          
    aTail(aDadosCob)[CB\_TAXIPI]     := 0          
    aTail(aDadosCob)[CB\_VALIPI]     := 0          
    aTail(aDadosCob)[CB\_BASICM]     := 0          
    aTail(aDadosCob)[CB\_TAXICM]     := 0          
    aTail(aDadosCob)[CB\_VALICM]     := 0          
    aTail(aDadosCob)[CB\_VALDES]     := 0         
    aTail(aDadosCob)[CB\_CFOP]       := GetAdvFVal("SF4","F4\_CF",xFilial("SF4") + cTes)  
    aTail(aDadosCob)[CB\_LOCAL]      := GetAdvFVal("SB1","B1\_LOCPAD",xFilial("SB1") + cProduto)  
  
    MSExecAuto({|a,b,c,d,e,f,g| NfeNfeCob(a,b,c,d,e,f,g)},,,nOpcX,,aCab103,aDadosCob)  
      
    If lMsErroAuto   
        MostraErro()  
    Else  
        Conout("Inserido Cobertura: " + cDocDef)  
    Endif  
Endif  
  
RESET ENVIRONMENT  
  
Return

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)
