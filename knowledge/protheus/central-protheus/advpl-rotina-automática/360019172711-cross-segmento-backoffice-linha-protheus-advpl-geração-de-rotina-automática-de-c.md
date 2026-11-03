---
article_id: 360019172711
category: ADVPL - Rotina Automática
content_hash: 9578b5a00b08d9fdf44087faff1b1c43b2d4e29c9009593614fb9665c8cee214
fetched_at: '2026-06-28T22:40:25.117943+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Geração de rotina automática
  de custo médio MATA338
type: support-article
updated_at: '2022-06-21T17:39:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019172711-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gera%C3%A7%C3%A3o-de-rotina-autom%C3%A1tica-de-custo-m%C3%A9dio-MATA338
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Estamos fazendo alguns lançamentos automáticos de alguns custo médio via uma rotina desenvolvida que utiliza o execauto da mata338.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.80  
  
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
AAdd(aItem,{"DQ_CM1",150 ,Nil})  
AAdd(aItem,{"DQ_CM1",150 ,Nil})  
AAdd(aItem,{"DQ_CM1",150 ,Nil})  
AAdd(aItem,{"DQ_CM1",150 ,Nil})  
   
   
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
