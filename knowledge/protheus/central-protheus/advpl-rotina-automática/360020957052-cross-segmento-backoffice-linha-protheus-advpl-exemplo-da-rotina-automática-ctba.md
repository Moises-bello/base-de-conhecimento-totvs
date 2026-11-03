---
article_id: 360020957052
category: ADVPL - Rotina Automática
content_hash: df107178080f7cfc76f27d62af701b593fb5468ccb0eb09699d4280637468471
fetched_at: '2026-06-28T22:40:24.064032+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo da Rotina automática
  CTBA060
type: support-article
updated_at: '2021-12-29T15:02:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020957052-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-da-Rotina-autom%C3%A1tica-CTBA060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Cliente esta solicitando exemplo de utilização de rotina automática da CTBA060

**Ambiente**Protheus – Contábil – A partir da versão 11.80  
  
**Solução**Exemplo

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function xCTBA060()  
  
local aClass := {}  
PRIVATE lMsErroAuto := .F.  
  
//-------------------------------------------------------------------//  
//*{Protheus.doc}CTBA060 //  
//*Programa de Classe de Valores //  
//*@author Totvs //  
//*@since 20/12/2018 //  
//*@version 12 //  
//-------------------------------------------------------------------//  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
  
aadd(aClass,{"CTH_CLVL","003 ",NIL})  
aadd(aClass,{"CTH_CLASSE","2",NIL})  
aadd(aClass,{"CTH_DESC01","REAL ",NIL})  
  
CTBA060(aClass,3)  
If !lMsErroAuto  
 ConOut("Incluido com sucesso! ")  
 Else  
 ConOut("Erro na inclusao!")  
 MOSTRAERRO()  
 EndIf  
 ConOut("Fim : "+Time())  
 RESET ENVIRONMENT  
Return
```
