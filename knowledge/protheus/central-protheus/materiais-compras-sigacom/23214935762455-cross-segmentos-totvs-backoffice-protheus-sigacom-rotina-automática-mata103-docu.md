---
article_id: 23214935762455
category: Materiais - Compras (SIGACOM)
content_hash: c425eeb63d711cec16d903992ce0ec823fdf3497d8f7c362016fdad249370808
fetched_at: '2026-06-28T22:41:25.272175+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Tipo Devolução
type: support-article
updated_at: '2024-05-02T18:09:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23214935762455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Tipo-Devolu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23214935731095) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como posso criar Rotina Automática MATA103 para documento do Tipo Devolução?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO TIPO DEVOLUÇÃO**

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
**aadd(aCab,{"F1\_TIPO" ,"D" ,NIL})**  
aadd(aCab,{"F1\_DOC" ,cNum ,NIL})  
aadd(aCab,{"F1\_SERIE" ,"1 " ,NIL})  
aadd(aCab,{"F1\_FORNECE" ,"001 " ,NIL})  
aadd(aCab,{"F1\_LOJA" ,"01" ,NIL})  
aadd(aCab,{"F1\_EMISSAO" ,DDATABASE ,NIL})  
aadd(aCab,{"F1\_DTDIGIT" ,DDATABASE ,NIL})  
aadd(aCab,{"F1\_FORMUL" ,"N" ,NIL})  
aadd(aCab,{"F1\_ESPECIE" ,"NFE" ,NIL})  
aadd(aCab,{"F1\_COND" ,"001" ,NIL})  
aadd(aCab,{"F1\_EST" ,"SP" ,NIL})  
aadd(aCab,{"F1\_DESCONT" , 0 , Nil})  
aadd(aCab,{"F1\_SEGURO" , 0 , Nil})  
aadd(aCab,{"F1\_FRETE" , 0 , Nil})  
aadd(aCab,{"F1\_MOEDA" , 1 , Nil})  
aadd(aCab,{"F1\_TXMOEDA" , 1 , Nil})  
aadd(aCab,{"F1\_STATUS" , "A" , Nil})

**//Itens**  
For nX := 1 To 1  
aItem := {}

aadd(aItem,{"D1\_ITEM" ,StrZero(nX,4) ,NIL})  
aadd(aItem,{"D1\_COD" ,PadR("0001",TamSx3("D1\_COD")[1]) ,NIL})  
aadd(aItem,{"D1\_UM" ,"UN" ,NIL})  
aadd(aItem,{"D1\_LOCAL" ,"01" ,NIL})  
**aadd(aItem,{"D1\_LOTECTL" ,"123456" ,NIL}) //Caso produto possua lote, informar o numero.**  
aadd(aItem,{"D1\_QUANT" ,1 ,NIL})  
aadd(aItem,{"D1\_VUNIT" ,1000 ,NIL})  
aadd(aItem,{"D1\_TOTAL" ,1000 ,NIL})  
aadd(aItem,{"D1\_TES" ,"001" ,NIL})  
**aadd(aItem,{"D1\_NFORI" ,"000009015" ,NIL})**  
**aadd(aItem,{"D1\_SERIORI" ,"1 " ,NIL})**  
**aadd(aItem,{"D1\_ITEMORI" ,"0001" ,NIL})**

aAdd(aItens,aItem)  
Next nX

**//3-Inclusão / 4-Classificação / 5-Exclusão**  
MSExecAuto({|x,y,z| MATA103(x,y,z)},aCab,aItens,nOpc)

If !lMsErroAuto  
ConOut(" Incluido NF: " + cNum)  
Else  
MostraErro()  
ConOut("Erro na inclusao!")  
EndIf

ConOut("Fim: " + Time())

RESET ENVIRONMENT

Return

***Saiba Mais:***

[PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)
