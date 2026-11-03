---
article_id: 360026869172
category: ADVPL - Rotina Automática
content_hash: a72001318611b1b3cd2891fff238ff061b4c23a71ba27f750f63bfe6236ed791
fetched_at: '2026-06-28T22:40:23.983679+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - EICPO400 Pedido de Importação
  exemplo de rotina automática
type: support-article
updated_at: '2021-12-29T14:03:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026869172-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-EICPO400-Pedido-de-Importa%C3%A7%C3%A3o-exemplo-de-rotina-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**

Exemplo de ExecAuto na rotina Purchase Order - PO ExecAuto. Funcionalidade disponível a partir do Microsiga Protheus 11.  
  
**Ambiente**Protheus – SIGAEIC – A partir da versão 11.80  
  
**Solução**

Exemplo de ExecAuto

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
  
User Function EXECAUTOEICPO400X2()  
  
  
//ExecAuto na rotina de Purchase Order   
 //*-------------------------*/  
//User Function POExecAuto()  
 //*-------------------------*/  
  
Local aCab := {}  
 Local aItem := {}  
 local cItem   
 Private lMsErroAuto := .F.  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Abertura do ambiente |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "01" MODULO "EIC"  
  
ConOut(Repl("-",80))  
 ConOut(" TESTE DA ROTINA AUTOMATICA EICPO400 - Pedido de Importacao P11")  
 ConOut(Repl("-",80))  
  
ConOut(Repl("*",80))  
 ConOut("Inicio da Inclusao: "+Time())  
 ConOut(Repl("*",80))  
  
SW2->(DbSelectArea("SW2"))//posicionamento da tabela  
SW2->(DbSetOrder(1))//setando a ordem   
SW2->(MsSeek(xFIlial("SW2")+"W2_PO_NUM",.T.))//posicionando onde ele vai iniciar  
SW2->(DbSkip(-1))//pegando o ultimo item da tabela  
  
cItem :=SW2->W2_PO_NUM  
  
cItem :=soma1(cItem)  
   
 AADD(aCab,{"W2_PO_NUM" ,cItem ,NIL})  
 AADD(aCab,{"W2_PO_DT" ,dDatabase ,NIL})  
 AADD(aCab,{"W2_FORN" ,"0001 " ,NIL})  
 AADD(aCab,{"W2_FORLOJ" ,"01" ,NIL})  
 //AADD(aCab,{"W2_CLIENTE" ,"01 " ,NIL})  
 AADD(aCab,{"W2_COMPRA" ,"01 " ,NIL})  
 AADD(aCab,{"W2_IMPORT" ,"01" ,NIL})  
 AADD(aCab,{"W2_AGENTE" ,"001" ,NIL})  
 AADD(aCab,{"W2_TIPO_EM" ,"00" ,NIL})  
 AADD(aCab,{"W2_ORIGEM" ,"EX " ,NIL})  
 AADD(aCab,{"W2_DEST" ,"BLM" ,NIL})  
 AADD(aCab,{"W2_INCOTER" ,"FOB" ,NIL})  
 AADD(aCab,{"W2_FREPPCC" ,"PP" ,NIL})  
 AADD(aCab,{"W2_COND_PA" ,"001 " ,NIL})  
 AADD(aCab,{"W2_MOEDA" ,"US$" ,NIL})  
 AADD(aCab,{"W2_DT_PAR" ,dDatabase ,NIL})  
 AADD(aCab,{"W2_PARID_U" ,1,000000 ,NIL})  
 AADD(aCab,{"W2_E_LC" ,"2" ,NIL})  
  
  
 aAdd(aItem,{ {"W3_COD_I" , "001 ",NIL},;  
 {"W3_CC" , "001 " ,NIL},;  
 {"W3_REG" , 1 ,NIL},;  
 {"W3_PRECO" , 2.00000 ,NIL},;  
 {"W3_FABR" , "0001 " ,NIL},;  
 {"W3_FORN" , "0001 " ,NIL},;  
 {"W3_QTDE" , 100.000 ,NIL},;  
 {"W3_DT_EMB" , dDatabase ,NIL},;  
 {"W3_DT_ENTR" , dDatabase+2 ,NIL},;  
 {"W3_SALDO_Q" , 0.000 ,NIL} })  
  
  
/* aAdd(aItem,{ {"W3_COD_I" , "PRODUTO 02 ",NIL},;  
 {"W3_CC" , "01 " ,NIL},;  
 {"W3_REG" , 1 ,NIL},;  
 {"W3_PRECO" , 2,00000 ,NIL},;  
 {"W3_FABR" , "01 " ,NIL},;  
 {"W3_FORN" , "01 " ,NIL},;  
 {"W3_QTDE" , 300,00000 ,NIL},;  
 {"W3_DT_EMB" , dDatabase ,NIL},;  
 {"W3_DT_ENTR" , dDatabase+2 ,NIL},;  
 {"W3_SALDO_Q" , 300,00000 ,NIL} })  
  
*/ ConOut("Começo da execauto")  
 MSExecAuto({|a,b,c,d| EICPO400(a,b,c,d)},NIL,aCab,aItem,3)  
  
If lMsErroAuto  
 Alert("Erro na inclusao ")  
 MOSTRAERRO()  
 Else  
 Alert(" Incluido com sucesso!")  
 Endif  
 RESET ENVIRONMENT  
  
ConOut("Fim da execauto!: "+Time())  
  
Return
```

**Saiba Mais**

**[EICPO400 - Rotina Automática do Purchase Order](https://tdn.totvs.com/pages/releaseview.action?pageId=397378759)**
