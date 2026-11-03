---
content_hash: ae059388027097c7e16175bcdd89690ed32a0679387d7248a454f54838542a3c
fetched_at: '2026-06-29T00:09:47.885949+00:00'
page_id: '435105093'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total
  de Subunidades
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105093
version: 7
---

O valor do rateio linear por total de subunidades é calculado através da divisão da despesa pela quantidade de subunidades informadas:

|  |
| --- |
| **Valor Total da Despesa / Quantidade Subunidades** |

Com o valor do rateio calculado, o sistema percorre todas as subunidades informadas aplicando o valor.

Neste modelo o usuário pode definir a seguinte associação:

**Um ou mais subunidades:** Rateio será realizado para todas as subunidades definidas;

| Rateio | Empreendimento | Unidade | Subunidade |
| --- | --- | --- | --- |
| Rateio Linear por Total de Subunidades |  |  | X |

**Observação:** Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.

Veja Também

---
