---
content_hash: 2b62255cae8790ba51d7fe1f16057e4e11580623428ce3e06f5c4d5b67cc54c3
fetched_at: '2026-06-29T00:09:47.881215+00:00'
page_id: '435105092'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total
  de Subunidade por Empreendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105092
version: 4
---

O valor do rateio linear por total de subunidade por empreendimento é calculado através da divisão da despesa pela quantidade de subunidades do empreendimento:

|  |
| --- |
| **Valor Total da Despesa / Quantidade Subunidades do Empreendimento** |

Com o valor do rateio calculado, o sistema percorre todas as subunidades do empreendimento aplicando o valor.  
 Neste modelo o usuário pode definir a seguinte associação:

* **Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio Linear por Total de Subunidades do Empreendimento | X |  |  |

* **Observação:** Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.

Veja Também

---

* Condomínio
