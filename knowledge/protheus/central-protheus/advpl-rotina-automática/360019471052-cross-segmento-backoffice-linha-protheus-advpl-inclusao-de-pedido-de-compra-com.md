---
article_id: 360019471052
category: ADVPL - Rotina Automática
content_hash: 2c604968817c07aff147fdebcf79b2f8a97ece7f336d21ec5944f83a58365f8b
fetched_at: '2026-06-28T22:40:23.889006+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL -  Inclusao de Pedido de
  compra com rateio de centro de custo(Execauto)
type: support-article
updated_at: '2021-12-29T13:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019471052-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Inclusao-de-Pedido-de-compra-com-rateio-de-centro-de-custo-Execauto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Exemplo de **Execauto** de inclusão de pedidos de venda com rateio de centro de custo  
   
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**

```
#INCLUDE "RWMAKE.CH"  
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "tbiconn.CH"  
  
User Function MyMata120()  
  
Local aCabec := {}  
Local aItens := {}  
Local aLinha := {}  
Local aLinRat := {}  
Local aRatCC := {}  
Local aItemCC := {}  
Local aRateio := {}  
Local nX := 0  
Local nY := 0  
Local cDoc := ""  
Local lOk := .T.  
  
PRIVATE lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FAT" TABLES "SC7","SCH"  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Abertura do ambiente |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
ConOut(Repl("-",80))  
  
ConOut(PadC("Teste de Inclusao de 10 pedidos de compra com 30 itens cada",80))  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Verificacao do ambiente para teste |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
dbSelectArea("SB1")  
dbSetOrder(1)  
  
If !SB1->(MsSeek(xFilial("SB1")+"PA0001 "))  
  
lOk := .F.  
  
ConOut("Cadastrar produto: PA0001 ")  
  
EndIf  
  
dbSelectArea("SF4")  
  
dbSetOrder(1)  
  
If !SF4->(MsSeek(xFilial("SF4")+"001"))  
  
lOk := .F.  
  
ConOut("Cadastrar TES: 001")  
  
EndIf  
  
dbSelectArea("SE4")  
dbSetOrder(1)  
  
If !SE4->(MsSeek(xFilial("SE4")+"001"))  
  
lOk := .F.  
  
ConOut("Cadastrar condicao de pagamento: 001")  
  
EndIf  
  
If !SB1->(MsSeek(xFilial("SB1")+"PA0001 "))  
  
lOk := .F.  
  
ConOut("Cadastrar produto: PA0001 ")  
  
EndIf  
  
dbSelectArea("SA2")  
dbSetOrder(1)  
  
If !SA2->(MsSeek(xFilial("SA2")+"000001"))  
  
lOk := .F.  
  
ConOut("Cadastrar fornecedor: 000001")  
  
EndIf  
  
If lOk  
  
ConOut("Inicio: "+Time())  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Verifica o ultimo documento valido para um fornecedor |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
dbSelectArea("SC7")  
dbSetOrder(1)  
MsSeek(xFilial("SC7")+"zzzzzz",.T.)  
dbSkip(-1)  
  
cDoc := SC7->C7_NUM  
  
For nY := 1 To 1  
  
aCabec := {}  
aItens := {}  
  
If Empty(cDoc)  
  
cDoc := StrZero(1,Len(SC7->C7_NUM))  
  
Else  
  
cDoc := Soma1(cDoc)  
  
EndIf  
  
aadd(aCabec,{"C7_NUM" ,cDoc})  
aadd(aCabec,{"C7_EMISSAO" ,dDataBase})  
aadd(aCabec,{"C7_FORNECE" ,"000001"})  
aadd(aCabec,{"C7_LOJA" ,"01"})  
aadd(aCabec,{"C7_COND" ,"001"})  
aadd(aCabec,{"C7_CONTATO" ,"AUTO"})  
aadd(aCabec,{"C7_FILENT" ,cFilAnt})  
  
For nX := 1 To 1  
  
aLinha := {}  
aadd(aLinha,{"C7_PRODUTO" ,"PA0001",Nil})  
aadd(aLinha,{"C7_QUANT" ,1 ,Nil})  
aadd(aLinha,{"C7_PRECO" ,100 ,Nil})  
aadd(aLinha,{"C7_TOTAL" ,100 ,Nil})  
aadd(aLinha,{"C7_TES" ,"001" ,Nil})  
aadd(aItens,aLinha)  
  
Next nX  
  
// Monta itens rateio  
aAdd(aRatCC,{"0001",{ }})  
  
// Primeiro item do rateio  
aAdd(aItemCC,{"CH_ITEM",StrZero(1,Len(SCH->CH_ITEM)),NIL})  
aAdd(aItemCC,{"CH_PERC",100,NIL}) // Percentual a ser ratiado.  
aAdd(aItemCC,{"CH_CC","000000001",NIL}) //centro de custo do primeiro Item.  
aAdd(aRatCC[1][2],aItemCC)  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Teste de Inclusao |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
MSExecAuto({|k,v,w,x,y,z| MATA120(k,v,w,x,y,z)},1,aCabec,aItens,3,,aRatCC)  
  
If !lMsErroAuto  
  
ConOut("Incluido com sucesso! "+cDoc)  
  
Else  
  
ConOut("Erro na inclusao!")  
  
MostraErro()  
  
EndIf  
  
Next nY  
  
ConOut("Fim : "+Time())  
  
EndIf  
  
RESET ENVIRONMENT  
  
Return (.T.)
```

**Saiba Mais:**

[Pedido de Compras - ExecAuto](http://tdn.totvs.com/pages/viewpage.action?pageId=6089279)
