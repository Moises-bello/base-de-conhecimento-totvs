---
article_id: 360019172731
category: ADVPL - Rotina Automática
content_hash: 5e4385960baee3c6c741c46a39cc8a442e9e2030e1224b4fa678b46d96a9ff87
fetched_at: '2026-06-28T22:40:24.110701+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - GERAÇÃO DE ROTINA AUTOMÁTICA
  DE CUSTO MÉDIO MATA338
type: support-article
updated_at: '2021-12-29T15:12:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019172731-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-GERA%C3%87%C3%83O-DE-ROTINA-AUTOM%C3%81TICA-DE-CUSTO-M%C3%89DIO-MATA338
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**

Boa tarde.

Estamos fazendo alguns lançamentos automáticos de alguns custo médio via uma rotina desenvolvida que utiliza o execauto da mata338.

**Ambiente**  
PROTHEUS – ADVPL – A partir da versão 11.80  
  
**Solução**

```
#include"Protheus.ch"  
#include"tbiconn.ch"  
  
function U_xMata338  
  
local aItem := {}  
PRIVATE lMsErroAuto := .F.  
 prepare environment empresa "99" filial "01"  
   
 AAdd(aItem,{"DQ_COD","P002 ",Nil})  
 AAdd(aItem,{"DQ_LOCAL","01" ,Nil})  
 AAdd(aItem,{"DQ_DATA",dDATABASE ,Nil})  
 AAdd(aItem,{"DQ_CM1",150 ,Nil})  
 AAdd(aItem,{"DQ_CM2",160 ,Nil})  
 AAdd(aItem,{"DQ_CM3",165 ,Nil})  
 AAdd(aItem,{"DQ_CM4",170 ,Nil})  
   
   
 MSExecAuto({|x,y,z| MATA338(x,y)},aItem,3)//3-Inclusão, 4-Alteração e 5-Exclusão   
 If !lMsErroAuto   
 ConOut("Incluido com sucesso! ")   
 Else   
 ConOut("Erro na inclusao!")  
 EndIf  
 ConOut("Fim : "+Time())  
 reset environment  
   
Return Nil
```
