---
article_id: 360020432511
category: ADVPL - Ponto de Entrada
content_hash: 85443689de4ead6f5bc0aef8970be78482a88dfd8d28f3dabf1d78b6417d04e3
fetched_at: '2026-06-28T22:40:11.696867+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - GP010AGRV
type: support-article
updated_at: '2022-06-21T17:55:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020432511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-GP010AGRV
---

**Dúvida**Através do ponto de entrada GP010AGRV, como saber qual operação a rotina está realizando.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**O ponto de entrada **GP010AGRV** traz por **PARAMIXB** o "**nopc**", contendo a operação realizada no momento(3 - Incluir, 4 - Alterar, 5 - Excluir).  
Exemplo do Ponto de Entrada **GP010AGRV**

```
#Include 'Protheus.ch'  
  
User Function GP010AGRV()  
  
 Local nOpc   :=Paramixb[1]  
 Local lGrava :=Paramixb[2]  
  
 Alert("GP010AGRV")  
  
Return
```
