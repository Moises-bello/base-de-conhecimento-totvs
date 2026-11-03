---
article_id: 360026905931
category: ADVPL - Rotina Automática
content_hash: 4f7faa184956e6c5a3492813805ac54e14afb8b44ff7aa54488e160504686efc
fetched_at: '2026-06-28T22:40:24.961086+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Exemplo de rotina
  automática MATA410  - exclusão de item e inclusão de outro
type: support-article
updated_at: '2021-05-12T12:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026905931-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exemplo-de-rotina-autom%C3%A1tica-MATA410-exclus%C3%A3o-de-item-e-inclus%C3%A3o-de-outro
---

**Dúvida**Estou tentando alterar um pedido com base em outro, porem ao exclui o primeiro item do pedido e tento replicar os mesmo itens restantes no segundo não é possível.

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Segue exemplo de exclusão de um item na rotina automática Mata410

```
#Include 'Protheus.ch'  
#include 'TBICONN.CH'  
  
User Function Mata410Wil() //Exemplo de rotina Mata410 excluindo um item  
   
Local aCabec := {}  
Local aItens := {}  
Local nX := {}  
Private cDoc := 'A01908'  
Private lMsErroAuto := .F.  
  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01' MODULO "FAT" TABLES "SC5","SC6","SA1","SA2","SB1","SB2","SF4"  
  
  
 aCabec := {}  
 aItens := {}  
 aadd(aCabec,{"C5_NUM",cDoc,Nil})  
 aadd(aCabec,{"C5_TIPO","N",Nil})  
 aadd(aCabec,{"C5_CLIENTE",SA1->A1_COD,Nil})  
 aadd(aCabec,{"C5_LOJACLI",SA1->A1_LOJA,Nil})  
 aadd(aCabec,{"C5_LOJAENT",SA1->A1_LOJA,Nil})  
 aadd(aCabec,{"C5_CONDPAG",SE4->E4_CODIGO,Nil})  
   
 For nX := 1 To 3  
 aLinha := {}  
   
 If nX == 1  
 aadd(aLinha,{"LINPOS","C6_ITEM",StrZero(nX,2)})  
 aadd(aLinha,{"AUTDELETA","S",Nil})  
 Else  
 aadd(aLinha,{"AUTDELETA","N",Nil})  
 EndIf   
 aadd(aLinha,{"C6_ITEM",StrZero(nX,2),Nil})  
 aadd(aLinha,{"C6_PRODUTO","PROD00000000000",Nil})  
 aadd(aLinha,{"C6_QTDVEN",3,Nil})  
 aadd(aLinha,{"C6_PRCVEN",100,Nil})  
 aadd(aLinha,{"C6_PRUNIT",100,Nil})  
 aadd(aLinha,{"C6_VALOR",300,Nil})  
 aadd(aLinha,{"C6_TES","501",Nil})  
   
 aadd(aItens,aLinha)  
 Next nX  
 ConOut(PadC("Teste de alteracao",80))  
 ConOut("Inicio: "+Time())  
 MSExecAuto({|x,y,z|mata410(x,y,z)},aCabec,aItens,4)  
 ConOut("Fim : "+Time())  
 ConOut(Repl("-",80))  
  
If !lMsErroAuto  
  
ConOut("Incluido com sucesso! ")   
Else   
 ConOut("Erro na inclusao!")  
 Mostraerro()  
EndIf  
  
RESET ENVIRONMENT   
  
  
Return
```
