---
article_id: 360025723313
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d3eb6146a795530d36f1c3e2fa55d83f36c9810534a49d9091d861b9099ef1c4
fetched_at: '2026-06-28T22:38:41.207023+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Despesas Não Aparecem
  na Planilha Financeira
type: support-article
updated_at: '2022-02-21T19:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025723313-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Despesas-N%C3%A3o-Aparecem-na-Planilha-Financeira
---

**Ocorrência**

Despesas Não Aparecem na Planilha Financeira.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – todas as versões  
  
**Causa**

Esse incidente ocorre, pois a parametrização do campo **Desp. Ac. ICMS**  da TES  influencia diretamente no cálculo das Despesas no nota fiscal.  
  
**Solução**

Para que apareça na nota e na planilha financeira o valor da despesa, na TES, informe o campo **Desp. Ac. ICMS (F4\_DESPICM)**= 1.
