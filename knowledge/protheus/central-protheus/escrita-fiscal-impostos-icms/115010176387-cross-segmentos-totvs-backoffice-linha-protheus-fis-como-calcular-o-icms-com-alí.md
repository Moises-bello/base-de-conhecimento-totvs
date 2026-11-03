---
article_id: 115010176387
category: Escrita Fiscal - Impostos - ICMS
content_hash: 332d9d28d18294c484831945d8026b2bf00ed164cd92e4121fdd9c02883e8cf0
fetched_at: '2026-06-28T22:39:24.385173+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como calcular o ICMS
  com alíquota de 7% sem configurar exceção fiscal
type: support-article
updated_at: '2021-07-28T14:21:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010176387-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-ICMS-com-al%C3%ADquota-de-7-sem-configurar-exce%C3%A7%C3%A3o-fiscal
---

**Duvida:**

Como calcular o ICMS com alíquota de 7% sem configurar exceção fiscal?

**Ambiente:**

Protheus - Sigafis - A partir da versão 12.1.17.

**Solução:**

Para que o sistema adote a alíquota de 7% de ICMS na operação interestadual, o estado de destino deve ser informado no parâmetro **MV\_NORTE**, fazendo com que o parâmetro MV\_ESTADO da filial de entrada (compra) seja considerado para o cálculo ou o campo A1\_EST (venda).
