---
article_id: 360021505711
category: ADVPL - Rotina Automática
content_hash: e32f63e1308dc0ed0310bd848101e7bc4127ce55116797171cf397bf2abaa175
fetched_at: '2026-06-28T22:40:25.044029+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  MVC MATA020
type: support-article
updated_at: '2025-02-04T13:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021505711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-MVC-MATA020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Exemplo de utilização da execauto da **MATA020** em **MVC****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução****Exemplo:**

```
#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
#INCLUDE 'Protheus.ch'  
#INCLUDE 'FWMVCDef.ch'  
  
//------------------------------------------------------------------------  
/*   EXEMPLO DE INCLUSÃO  
//------------------------------------------------------------------------  
  
User Function MT020MVC()  
  
Local oModel := Nil  
Private lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"   
  
oModel := FwLoadModel ("MATA020")  
oModel:SetOperation(MODEL_OPERATION_INSERT)  
oModel:Activate()  
oModel:SetValue("SA2MASTER","A2_COD" ,"F00005")  
oModel:SetValue("SA2MASTER","A2_LOJA" ,"01")  
oModel:SetValue("SA2MASTER","A2_NOME" ,"FORN TESTE MVC")  
oModel:SetValue("SA2MASTER","A2_NREDUZ" ,"F TESTE MVC")  
oModel:SetValue("SA2MASTER","A2_END" ,"RUA MVC TESTE")  
oModel:SetValue("SA2MASTER","A2_EST" ,"SP")  
oModel:SetValue("SA2MASTER","A2_MUN" ,"SAO PAULO")  
oModel:SetValue("SA2MASTER","A2_TIPO" ,"F")  
  
If oModel:VldData()  
  oModel:CommitData()  
   MsgInfo("Registro INCLUIDO!", "Atenção")  
Else  
   VarInfo("",oModel:GetErrorMessage())  
EndIf  
  
oModel:DeActivate()  
oModel:Destroy()  
oModel := NIL  
  
RESET ENVIRONMENT  
  
Return Nil
```
