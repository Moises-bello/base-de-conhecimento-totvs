---
article_id: 4411473418263
category: TAF - REINF
content_hash: 5adfd7a5833936e878f49504dc117f84b6e61295426d723625d2e4fb9128ceb4
fetched_at: '2026-06-28T22:41:33.692974+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como Gerar o R-2060 manualmente
  no TAF
type: support-article
updated_at: '2024-08-15T15:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411473418263-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2060-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2060 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2060 no TAF.**

**Rotina: Atualizações > Movimentos Reinf > Cont Prev Rec Brut**

**R-2060 - Contribuição Previdenciária sobre a Receita Bruta - CPRB**

 Capa

* + Inicial (C5M\_DTINI): O mês/ano selecionado para apuração deve corresponder ao mês/ano de competência da atividade;
  + Final (C5M\_DTFIM): O mês/ano selecionado para apuração deve corresponder ao mês/ano de competência da atividade;
* Processos Referenciados
  + Proc Ref (C5O\_NUMPRO): O ID do processo referenciado;
  + Suspensão (C5O\_CODSUS): O código da exigibilidade suspensa;
* Tipo de Ajuste
  + Tipo Ajuste (T9T\_TPAJUS): O tipo de ajuste;
  + Ajuste (T9T\_CODAJU): O código de ajuste;
  + Valor Ajuste (T9T\_VLRAJU): Valor do Ajuste;
  + Ajuste (T9T\_DESCAJ): Descrição do ajuste;
  + Data Ajuste (T9T\_DTAJUS): Data do Ajuste.
