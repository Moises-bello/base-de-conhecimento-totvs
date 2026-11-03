---
article_id: 360007158332
category: NFe - Nota Fiscal Eletrônica
content_hash: e922ea347dbba31aff8299009c3c2f2fe41c88572c02d1ed4d0f851c617a0dcf
fetched_at: '2026-06-28T22:39:59.881371+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  461 Rejeição
  : Informado campos de percentual de GLP e/ou GLGNn e/ou GLGNi para produto diferente
  de GLP'
type: support-article
updated_at: '2021-07-01T14:12:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007158332--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-461-Rejei%C3%A7%C3%A3o-Informado-campos-de-percentual-de-GLP-e-ou-GLGNn-e-ou-GLGNi-para-produto-diferente-de-GLP
---

**Dúvida**Como solucionar a rejeição abaixo ?

461 Rejeição : Informado campos de percentual de GLP e/ou GLGNn e/ou GLGNi para produto diferente de GLP?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Preencher os campos abaixo no complemento de combustível:**

* CD6\_PGLP
* CD6\_PGNN
* CD6\_PGNI

Lembrando que só devem ser preenchidos se o CODANP no campo CD6\_CODANP = **210203001**

Para os demais códigos para que não gere a rejeição devem ficar em branco os três campos ao fazer o complemento de combustível.
