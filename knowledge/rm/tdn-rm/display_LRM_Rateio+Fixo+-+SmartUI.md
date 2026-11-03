---
content_hash: de28376454eed6d858fa8263546fe2e90b5410f7d5924de04c6df7b6e3e7a657
fetched_at: '2026-06-29T00:12:07.167887+00:00'
page_id: '919070854'
product: rm
source: tdn-rm
title: Rateio Fixo - SmartUI
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+Fixo+-+SmartUI
version: 2
---

O cadastro de Rateio Fixo permite a definição dos percentuais ou valores fixos de rateio, de acordo com a parametrização definida em Parametrizador | Configurações | 06.01.03 - Folha Normal (Utiliza Cálculo por Centro de Custo). Este cadastro deve ser efetuado para cada funcionário, considerando todos os centros de custo onde atuou durante o mês, de modo que os dados informados sejam utilizados pelo sistema para efetuar o rateio no cálculo por centro de custo.

No anexo do cadastro do funcionário, informe o percentual ou valor de rateio fixo correspondente ao centro de custo em que ele atuou.

Ao utilizar percentuais, a soma total deve ser igual a 100%, pois o sistema realizará a divisão por 100 no cálculo.

 Caso o parâmetro "Rateio fixo por valor" estiver marcado, o campo acima será renomeado para "Valor" e deverão ser informados valores brutos para se chegar aos percentuais usados no rateio.

**Exemplo:**  
O rateio fixo do funcionário está preenchido com os seguintes dados:

| Centro de Custo | Valor |
| --- | --- |
| XXXX | 54,00 |
| YYYY | 66,00 |
| **Total do Rateio** | **120,00** |

Ao ratear um evento/verba, o sistema fará o seguinte cálculo:

* + Valor = R$29,68
  + Centro de custo XXXX = R$29,68 \* 54 / 120 = R$13,36
  + Centro de custo YYYY = R$29,68 \* 66 / 120 = R$16,32

**OBSERVAÇÃO:**

1. O sistema validará se a soma dos percentuais dos rateios fixos é igual a 100% somente quando o parâmetro "Rateio fixo por valor" não estiver marcado.
2. Os Centros de Custos com a opção "Ativo" desmarcada (ou seja, inativos) não serão exibidos na tela de cadastro de "Rateios Fixos".

---

Funcionários
