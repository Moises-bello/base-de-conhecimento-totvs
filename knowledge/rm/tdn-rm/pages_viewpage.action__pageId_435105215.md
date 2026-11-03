---
content_hash: 3cb4d3da7441b04df22608fbd3c9c026a8e34b734ff89bb332fdf0ac268e617f
fetched_at: '2026-06-29T00:09:48.667836+00:00'
page_id: '435105215'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total
  de Subunidade da Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105215
version: 6
---

O valor do rateio linear por total de subunidade por unidade é calculado através da divisão da despesa pela quantidade de subunidades da unidade definida:

|  |
| --- |
| **Valor Total da Despesa / Quantidade Subunidades da Unidade** |

Com o valor do rateio calculado, o sistema percorre todas as subunidades da unidade aplicando o valor.

Neste modelo o usuário pode definir a seguinte associação:

* **Uma ou mais unidades:** Rateio será realizado para todas as subunidades da(s) unidade(s) definida(s);

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio Linear por Total de Subunidades do Empreendimento |  | X |  |

Caso o usuário informe mais de uma unidade, então o sistema obtém o valor total de subunidades para as unidades informadas.

**Exemplo:**

* Valor da despesa: R$1.000,00
* Associação da despesa
  + Unidade A (possui 10 subunidades)
  + Unidade B (possui 15 subunidades)
  + Valor do rateio = 1.000,00 / 25

**Observação:**

* Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.

Veja Também

---

* Condomínio
