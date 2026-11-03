---
article_id: 23214559184407
category: Materiais - Compras (SIGACOM)
content_hash: 7eec83fe48dc6a9cdc49ba3e11a044eda2a999d24e250e07085681844a0dc20b
fetched_at: '2026-06-28T22:41:25.278438+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Tipo Normal Vinculado ao Pedido de Compras
type: support-article
updated_at: '2024-05-02T18:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23214559184407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Tipo-Normal-Vinculado-ao-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23214559167511) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento do Tipo Normal Vincualdo ao Pedido de Compras?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO TIPO NORMAL VINCULADO AO PEDIDO DE COMPRAS**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCab := {}  
Local aItem := {}  
Local aItens := {}  
Local aAutoImp := {}  
Local aItensRat := {}  
Local aCodRet := {}  
Local aParamAux := {}  
Local nOpc := 3  
Local cNum := ""  
Local nI := 0  
Local nX := 0  
Local nReg := 1

Conout("Inicio: " + Time())

Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.

PREPARE ENVIRONMENT EMPRESA "32" FILIAL "6597" MODULO "COM" FUNNAME "MATA103"

cNum := GetSxeNum("SF1","F1\_DOC")  
SF1->(dbSetOrder(1))  
While SF1->(dbSeek(xFilial("SF1")+cNum))  
ConfirmSX8()  
cNum := GetSxeNum("SF1","F1\_DOC")  
EndDo

**//Cabeçalho**  
aadd(aCab,{"F1\_TIPO" ,"N" ,NIL})  
aadd(aCab,{"F1\_FORMUL" ,"N" ,NIL})  
aadd(aCab,{"F1\_DOC" ,cNum ,NIL})  
aadd(aCab,{"F1\_SERIE" ,"1 " ,NIL})  
aadd(aCab,{"F1\_EMISSAO" ,DDATABASE ,NIL})  
aadd(aCab,{"F1\_DTDIGIT" ,DDATABASE ,NIL})  
aadd(aCab,{"F1\_FORNECE" ,"001 " ,NIL})  
aadd(aCab,{"F1\_LOJA" ,"01" ,NIL})  
aadd(aCab,{"F1\_ESPECIE" ,"CTE" ,NIL})  
aadd(aCab,{"F1\_COND" ,"001" ,NIL})  
aadd(aCab,{"F1\_DESPESA" ,10 ,NIL})  
aadd(aCab,{"F1\_DESCONT" , 0 ,Nil})  
aadd(aCab,{"F1\_SEGURO" , 0 ,Nil})  
aadd(aCab,{"F1\_FRETE" , 0 ,Nil})  
aadd(aCab,{"F1\_MOEDA" , 1 ,Nil})  
aadd(aCab,{"F1\_TXMOEDA" , 1 ,Nil})  
aadd(aCab,{"F1\_STATUS" , "A" ,Nil})

**//Itens**  
For nX := 1 To 1  
          aItem := {}  
          aadd(aItem,{"D1\_ITEM" ,StrZero(nX,4) ,NIL})  
          aadd(aItem,{"D1\_COD" ,PadR("0001",TamSx3("D1\_COD")[1]) ,NIL})  
          aadd(aItem,{"D1\_UM" ,"UN" ,NIL})  
          aadd(aItem,{"D1\_LOCAL" ,"01" ,NIL})  
          aadd(aItem,{"D1\_QUANT" ,1 ,NIL})  
          aadd(aItem,{"D1\_VUNIT" ,7508.33 ,NIL})  
          aadd(aItem,{"D1\_TOTAL" ,7508.33 ,NIL})  
          aadd(aItem,{"D1\_TES" ,"001" ,NIL})  
          aadd(aItens,aItem)  
          aadd(aItens[Len(aItens)], {'D1\_PEDIDO ', '000034' ,}) // Número do Pedido de Compras  
          aadd(aItens[Len(aItens)], {'D1\_ITEMPC ', '0001' ,}) // Item do Pedido de Compras

         if(nOpc == 4)//Se for classificação deve informar a variável **LINPOS**

              aAdd(aItem, {"LINPOS" , "D1\_ITEM",  StrZero(nX,4)}) //ou SD1->D1\_ITEM  se estiver posicionado.

         endIf

Next nX

**//3-Inclusão / 4-Classificação / 5-Exclusão**  
MSExecAuto({|x,y,z,k,a,b| MATA103(x,y,z,,,,k,a,,,b)},aCab,aItens,nOpc,aParamAux,aItensRat,aCodRet)

If !lMsErroAuto  
ConOut(" Incluido NF: " + cNum)  
Else  
MostraErro()  
ConOut("Erro na inclusao!")  
EndIf

ConOut("Fim: " + Time())

RESET ENVIRONMENT

Return

**Saiba Mais:**

**[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)**
