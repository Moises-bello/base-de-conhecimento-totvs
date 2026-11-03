---
content_hash: 1b466dfab786c5de6e94bde9a90c5054e09daf02c04530327517796568ef3ad1
fetched_at: '2026-06-29T00:09:48.532098+00:00'
page_id: '435105183'
product: rm
source: tdn-rm
title: Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por Fração Ideal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105183
version: 4
---

O rateio por fração ideal irá utilizar o valor da fração ideal cadastrado na subunidade.

|  |
| --- |
| **Valor Total da Despesa \* Fração Ideal** |

Para cada subunidade o sistema irá obter a fração ideal e calcular o valor do rateio. Neste modelo o usuário pode definir a seguinte associação:

**Um empreendimento:** Rateio será realizado para todas as subunidades do empreendimento definido;

|  |  |  |  |
| --- | --- | --- | --- |
| Rateio | Empreendimento | Unidade | Subunidade |
| Rateio por Fração Ideal | X |  |  |

**Observações:**

* Portanto quando a despesa estiver associada a uma unidade ou subunidade, e o modelo de cálculo for do tipo Fração Ideal, o sistema não irá executar a apuração.
* Caso pelo menos uma das subunidades estiver associada a um imóvel do módulo de Aluguel , tendo como Tipo de Locação "Áreas Fracionadas" ou "Áreas Unificadas", a apuração não será executada para a despesa relacionada.

Veja Também

---
