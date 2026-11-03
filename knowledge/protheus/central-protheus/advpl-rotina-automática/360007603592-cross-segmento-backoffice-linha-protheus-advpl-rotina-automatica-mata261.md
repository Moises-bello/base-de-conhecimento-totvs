---
article_id: 360007603592
category: ADVPL - Rotina Automática
content_hash: fc32fe6e6f00a5d6ec98f82a8ad6191b9741f81be86cbd4dd3423be633322a12
fetched_at: '2026-06-28T22:40:24.210407+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - ROTINA AUTOMATICA MATA261
type: support-article
updated_at: '2023-07-27T20:17:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007603592-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-ROTINA-AUTOMATICA-MATA261
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao executar a rotina automática MATA261 ocorre essa inconsistência.

AJUDA:OCORRENCIA   
A ocorrência informada não foi encontrada no cadastro de ocorrências.   
Array aheader com inconsistencia de dados.Favor verificar o layout do array enviado   
O Campos necessários são:   
Titulo Campo Tipo Tamanho Decimal 

**Ambiente**Serviços – Materiais – A partir da versão 11.80

**Solução**

```
#INCLUDE "PROTHEUS.CH"   
#include "rwmake.ch"   
#include "TbiConn.ch"  
  
User Function MyMata261()   
local aAuto := {}  
Local aItem := {}   
Local aLinha := {}  
local alista := {'4091','7390','9266','9377','9368MP','9368PA'}  
local nX  
  
Private lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "EST"   
  
//Cabecalho a Incluir   
aadd(aAuto,{GetSxeNum("SD3","D3_DOC"),dDataBase}) //Cabecalho   
  
//Itens a Incluir   
aItem := {}  
  
for nX := 1 to len(alista) step 2  
aLinha := {}  
//Origem   
SB1->(MsSeek(xFilial("SB1")+PadR(alista[nX], tamsx3('D3_COD') [1])))  
aadd(aLinha,{"ITEM",'00'+cvaltochar(nX),Nil})   
aadd(aLinha,{"D3_COD", SB1->B1_COD, Nil}) //Cod Produto origem   
aadd(aLinha,{"D3_DESCRI", SB1->B1_DESC, Nil}) //descr produto origem   
aadd(aLinha,{"D3_UM", SB1->B1_UM, Nil}) //unidade medida origem   
aadd(aLinha,{"D3_LOCAL", SB1->B1_LOCPAD, Nil}) //armazem origem   
aadd(aLinha,{"D3_LOCALIZ", "", Nil}) //endereço origem  
  
//Destino   
SB1->(MsSeek(xFilial("SB1")+PadR(alista[nX+1], tamsx3('D3_COD') [1])))   
aadd(aLinha,{"D3_COD", SB1->B1_COD, Nil}) //cod produto destino   
aadd(aLinha,{"D3_DESCRI", SB1->B1_DESC, Nil}) //descr produto destino   
aadd(aLinha,{"D3_UM", SB1->B1_UM, Nil}) //unidade medida destino   
aadd(aLinha,{"D3_LOCAL", SB1->B1_LOCPAD, Nil}) //armazem destino   
aadd(aLinha,{"D3_LOCALIZ", "", Nil}) //endereço destino  
  
aadd(aLinha,{"D3_NUMSERI", "", Nil}) //Numero serie  
aadd(aLinha,{"D3_LOTECTL", "", Nil}) //Lote Origem  
aadd(aLinha,{"D3_NUMLOTE", "", Nil}) //sublote origem  
aadd(aLinha,{"D3_DTVALID", dDataBase, Nil}) //data validade   
aadd(aLinha,{"D3_POTENCI", 0, Nil}) // Potencia  
aadd(aLinha,{"D3_QUANT", 1, Nil}) //Quantidade  
aadd(aLinha,{"D3_QTSEGUM", 0, Nil}) //Seg unidade medida  
aadd(aLinha,{"D3_ESTORNO", "", Nil}) //Estorno   
aadd(aLinha,{"D3_NUMSEQ", "", Nil}) // Numero sequencia D3_NUMSEQ  
  
aadd(aLinha,{"D3_LOTECTL", "", Nil}) //Lote destino  
aadd(aLinha,{"D3_NUMLOTE", "", Nil}) //sublote destino   
aadd(aLinha,{"D3_DTVALID", dDataBase, Nil}) //validade lote destino  
aadd(aLinha,{"D3_ITEMGRD", "", Nil}) //Item Grade  
  
aadd(aLinha,{"D3_CODLAN", "TESTE", Nil}) //cat83 prod origem  
aadd(aLinha,{"D3_CODLAN", "TESTE2", Nil}) //cat83 prod destino   
  
aAdd(aAuto,aLinha)  
  
Next nX  
  
MSExecAuto({|x,y| mata261(x,y)},aAuto,3)   
  
if lMsErroAuto   
MostraErro()   
EndIf  
  
RESET ENVIRONMENT   
  
Return Nil
```

**Saiba mais:****[MATA261 - MsExecAuto Transferência Múltipla](http://tdn.totvs.com/pages/viewpage.action?pageId=379292916)**
