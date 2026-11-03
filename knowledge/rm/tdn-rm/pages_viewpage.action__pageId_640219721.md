---
content_hash: 7628d4b13fdcdc3809d0c5f8ce67b9b640054463f8c8b6a28ebff60ec8c48c53
fetched_at: '2026-06-29T00:11:09.567626+00:00'
page_id: '640219721'
product: rm
source: tdn-rm
title: Exemplo de lançamento de empréstimo consignado nas férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640219721
version: 3
---

Se o número de dias de férias no mês for superior a 15 dias.

* No caso de férias partidas, verifica mais de 15 dias em cada mês

Verificar existência de desconto de empréstimos na competência anterior da folha de pagamento:

* Busca em Folha Mensal / Consulta / Consulta Movimento Integração / Anexo Parcelas de empréstimo consignado (tabela PFMOVTEMPCONSIG) parcela de empréstimo no mês/ano anterior a competência atual da folha.

Se ainda existem parcelas pendentes daquele empréstimo para o funcionário nas competências referentes às férias:

* NROPARCELA + número de meses entre competência atual e a data de inicio das férias.

Se NROPARCELA for menor que TOTALPARCELAS, acumula valor (pode existir mais de um empréstimo).

Se NROPARCELA ou TOTALPARCELAS estiver com valor zerado na PFMOVTEMPCONSIG, não será lançado o desconto, e irá exibir mensagem de Aviso (finaliza Amarelo).

**Observação:**  O líquido do recibo de férias será pago com o valor subtraído do empréstimo consignado e ao lançar as férias o valor será somado novamente no código de cálculo 43 – Adiantamento conforme recibo, com isso ao lançar o desconto do empréstimo atual o valor do envelope de pagamento ficará correto.

Foram criados os seguintes códigos de cálculo:

453 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 1o. MÊS (Desconto)

454 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 2o. MÊS (Desconto)

455 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 1o. MÊS ENVELOPE (Provento)

456 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 2o. MÊS ENVELOPE (Provento)

**CENÁRIO 1**

Competência atual da base 06/2021

Férias mês integral em 06/2021

Valor empréstimo lançado no mês 05/2021 – 1000,00

Total de parcelas do empréstimo – 10

Número de parcelas pagas até 05/2021 – 2

**CENÁRIO 2**

Competência atual da base 06/2021

Férias mês partidas com dias de gozo maior que 15 em 06/2021

Valor empréstimo lançado no mês 05/2021 – 1000,00

Valor empréstimo lançado no mês 06/2021 – 1232,00

Valor empréstimo lançado no mês 07/2021 – 1232,00

Total de parcelas do empréstimo – 10

Número de parcelas pagas até 05/2021 – 2

**CENÁRIO 3**

Competência atual da base 06/2021

Férias mês partidas com dias de gozo maior que 15 em 07/2021

Valor empréstimo lançado no mês 05/2021 – 1000,00

Valor empréstimo lançado no mês 06/2021 – 1232,00

Valor empréstimo lançado no mês 07/2021 – 1232,00

Total de parcelas do empréstimo – 10

Número de parcelas pagas até 05/2021 – 2
