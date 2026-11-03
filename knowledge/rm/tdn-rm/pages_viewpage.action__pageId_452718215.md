---
content_hash: 699ad4f16f3ab3e82d3359302f7703ee2d9a892eaed5a42523a9c43d8ef63357
fetched_at: '2026-06-29T00:09:58.853871+00:00'
page_id: '452718215'
product: rm
source: tdn-rm
title: Código de Cálculo 3 - INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718215
version: 2
---

Desconto do tipo valor com incidência no líquido. O sistema somará os proventos do mês que "incidem INSS" e encontrará o valor de INC. INSS. O sistema somará os descontos do mês que "estornam bases", encontrará o valor de "estorna bases" e deduzirá do valor de "inc. INSS" para o cálculo deste desconto. Para os funcionários semanalistas, o sistema buscará o total já descontado no mesmo mês e deduzirá este valor do total de INSS que deverá ser descontado. Não será calculado INSS para os funcionários aposentados.   
 O cálculo será feito da seguinte forma:

(((INC. INSS - ESTORNA BASES) \* TAXA) / 100) - JÁ DESCONTOU

O sistema calculará: INC. INSS - ESTORNA BASES.

O valor encontrado será aplicado à tabela de INSS (informada em Cadastros | Cálculos | Tabelas de Cálculo) e multiplicado pela taxa da faixa encontrada, respeitando o teto.

O valor resultante dessa operação será dividido por 100 e será subtraído o valor de "JÁ DESCONTOU" (código de cálculo 82 + código de cálculo 11).

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
