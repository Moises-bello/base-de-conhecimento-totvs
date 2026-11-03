---
content_hash: d12cbb7181a3af3459b6968e4b85a818f3d036f5f1ef5e25a8b0a4eac3ee0ba5
fetched_at: '2026-06-29T00:11:25.716962+00:00'
page_id: '715145236'
product: rm
source: tdn-rm
title: Considerar Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715145236
version: 19
---

---

Existe parâmetros dentro do contrato e serviço que devem ser marcados para que o Desconto por Antecipação seja considerado, são eles:

Cadastro de Serviço

Para que o desconto por antecipação seja considerado, o 'serviço' deverá ser configurado para considerar o desconto por antecipação através do campo "Considera desconto por antecipação".

Para que um desconto por antecipação seja considerado na geração de lançamentos, os campos "Considera desconto por antecipação" deverão estar marcados no contrato e no serviço. Caso não esteja marcado em algum desses lugares, o desconto por antecipação será desconsiderado.

Cadastro de Contrato

Para que o desconto por antecipação seja considerado, o 'contrato' deverá ser configurado para considerar o desconto por antecipação através do campo "Considera desconto por antecipação".

Para que um desconto por antecipação seja considerado na geração de lançamentos, os campos "Considera desconto por antecipação" deverão estar marcados no contrato e no serviço. Caso não esteja marcado em algum desses lugares, o desconto por antecipação será desconsiderado.

**=> Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)**

Quando o sistema estiver parametrizado para que a aplicação de Bolsa seja por contrato (Educacional >> Integração >> Financeiro >> Educacional >> Fin – Geral 4/4), e o tipo de classificação do contrato, seja igual a, “Somar Bolsa” ou “Maior Bolsa”, será disponibilizada no contrato a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”.***

A opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”*** ficará disponível somente se o sistema estiver parametrizado para que a aplicação de bolsa seja por contrato.

Considerando o tipo de bolsa “Somar” ou “Maior Bolsa”, por padrão ao calcular o valor de uma bolsa o sistema considera como valor base o valor da parcela.

Exemplo: Valor da parcela: R$1.000 | Desconto por antecipação: 10% (100,00) | Bolsa: 20% (200,00).

Caso a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)***” esteja marcada, o valor base para o cálculo da bolsa levara em consideração o maior valor do desconto por antecipação.

(Exemplo 1 - valor base para o cálculo da bolsa)

* Valor da parcela: R$1.000
* Desconto por antecipação: 10% (R$100,00)
* Bolsa: 20% (R$180,00)

O valor base do cálculo da bolsa será: valor da parcela (R$1.000,00) – maior desconto por antecipação (R$100,00) = R$900,00.

(Exemplo 2 - valor base para o cálculo da bolsa)

* Valor da parcela: R$1.000
* Desconto por antecipação 1º vencimento: 30% (R$300,00)
* Desconto por antecipação 2º vencimento: 5% (R$50,00)
* Bolsa: 50% (R$350,00)

O valor base do cálculo da bolsa será: valor da parcela (R$1.000,00) – maior desconto por antecipação (R$300,00) = R$700,00.

**Como no cálculo base considera o maior desconto por antecipação independente da data que for efetuada o pagamento. Neste caso, o valor da bolsa do segundo desconto por antecipação está considerando o maior desconto por antecipação que corresponde aos 30% do primeiro desconto. O comportamento será aplicado em todos os demais itens do desconto por antecipação.**

**Novos contratos**

Sempre ao incluir um novo contrato a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”***será preenchida conforme o parâmetro “Considerar desconto por antecipação para Somar Bolsa” ou “Considerar desconto por antecipação para Maior Bolsa”, disponível em Educacional >> Integrações >> Financeiro >> Educacional >> Fin-Geral 4/4, estes parâmetros tem a função de indicar o comportamento padrão para os contratos.
