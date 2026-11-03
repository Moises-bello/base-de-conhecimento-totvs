---
article_id: 360026661472
category: NFe - Nota Fiscal Eletrônica
content_hash: c4806994e73d8baff7f16003f74a37273b8c07eced1835bb031b886397b474f5
fetched_at: '2026-06-28T22:40:01.630024+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como configurar
  o motivo de cancelamento para nota fiscal eletrônica'
type: support-article
updated_at: '2021-10-11T18:23:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661472--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-o-motivo-de-cancelamento-para-nota-fiscal-eletr%C3%B4nica
---

**Dúvida***Como configurar o motivo de cancelamento para nota fiscal eletrônica ?*

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **MV\_INFXJUS**

(Parâmetro para justificativa do cancelamento por evento não é obrigatório, pois gera um texto padrão no XML caso não habilite).

**Habilitado = S**

**Desabilitado = N**

**IMPORTANTE:**

Para que a justificativa pare de aparecer para a nota cancelada ou Inutilizada e necessário realizar a consulta em monitor -> faixa.
