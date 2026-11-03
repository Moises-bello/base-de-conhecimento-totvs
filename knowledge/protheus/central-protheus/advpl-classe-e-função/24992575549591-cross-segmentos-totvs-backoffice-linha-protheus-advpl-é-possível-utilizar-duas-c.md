---
article_id: 24992575549591
category: ADVPL - Classe e Função
content_hash: 35425cdcdb5c1348103924234c1ee43c2efd1377f8b8112bf382707a0fa0ac6d
fetched_at: '2026-06-28T22:40:21.609338+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível utilizar
  duas colunas de legenda na FWMBrowse?
type: support-article
updated_at: '2024-07-18T17:14:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24992575549591-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-utilizar-duas-colunas-de-legenda-na-FWMBrowse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24992575533207) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível utilizar duas colunas de legenda na FWMBrowse?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Com o método AddLegend é possível passar o 4º parâmetro determinando um ID, informando ID´s diferentes será considerado uma nova legenda.

```
#INCLUDE "TOTVS.CH"  
  
USER Function FwBrwQry()  
Local oBrowse  
Local oColumn  
  
oBrowse := FWMBrowse():New()  
oBrowse:SetAlias('ZA0')  
oBrowse:SetDescription('Cadastro de Autor/Interprete')  
oColumn := oBrowse:AddMarkColumns({||If(.T./*Função de Marca/desmaca*/,'LBOK','LBNO')},;  
{|oBrowse|/*Função de DOUBLECLICK*/},{|oBrowse|/* Função de HEADERCLICK*/})  
oBrowse:AddLegend( "ZA0_TIPO=='1'", "YELLOW", "Autor","001" )  
oBrowse:AddLegend( "ZA0_CODIGO=='000002'", "BLUE" , "Interprete","002" )  
  
oBrowse:SetMenuDef("COMP011_MVC")  
  
oBrowse:Activate()
```

**Saiba mais:**

[FWMBrowse](https://tdn.totvs.com/pages/releaseview.action?pageId=62390842)
