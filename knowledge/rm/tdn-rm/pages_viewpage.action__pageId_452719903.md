---
content_hash: b6ca9823e1903c1d90b19d1b614f4336c8ee5d8622064b4979168372f8d2089b
fetched_at: '2026-06-29T00:10:10.674237+00:00'
page_id: '452719903'
product: rm
source: tdn-rm
title: Código de Cálculo 55 - Salário Família Retroativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719903
version: 4
---

Provento do tipo valor com as mesmas incidências do Cód. de Cálculo 5 - Salário Família.   
O pagamento dos valores de Salário Família retroativo poderá feito através do seguinte roteiro:

**Passo a Passo**

1) Deve ser criada uma fórmula com a nova função de fórmula NDEPSFAMRET, que recebe um parâmetro numérico (0 ou 1) e que, de acordo com esse parâmetro, retornará um dos seguintes valores:

* Parâmetro 0 - retorna o total de dependentes com direito ao salário família.
* Parâmetro 1 - retorna o valor monetário relativo ao pagamento devido de salário família dos dependentes que não entregaram o cartão de vacina e/ou atestado de frequência escolar.

2) Deve-se criar um evento do tipo BASE com código de cálculo zero e chave desativada que utilize a fórmula citada no passo anterior, de forma que se registre na ficha financeira do funcionário o total de dependentes ou os valores devidos mas não pagos relativos a dependentes de salário-família que não entregaram documentação.

**Atenção**

Caso a fórmula NDEPSFAMRET utilize o parâmetro 1 este evento deve ter prioridade alta, pois o cálculo deste evento dependerá de valores prévios de salário bruto ou liquido.

3) Na época de pagar o salário-família retroativo deverá ser utilizado o evento com código de cálculo 55 - Salário Família Retroativo. O sistema não calculará automaticamente o valor deste evento. Este evento deverá ser será calculado por uma fórmula em função do pagamento do salário-família retroativo ser diferenciado para cada funcionário de acordo com o período desejado. A fórmula deste evento deverá recuperar ou calcular todos os valores devidos de salário família não pagos a partir dos valores previamente registrados na ficha financeira (vide passo anterior).

**Observação**

1) O evento de Código de Cálculo 55 – Salário Família Retroativo, será considerado nos cálculos do SEFIP e GPS, do mesmo modo como é tratado Código de Cálculo 5 - Salário Família.

2) Para funcionário que recebe salário acima do teto para pagamento de salário família o tratamento pode ser feito na fórmula.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
