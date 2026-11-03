---
content_hash: 4e076859d3dd2569368c82d581755044857ee269d82ceaac6048eaf807c8cfdd
fetched_at: '2026-06-29T00:10:13.385991+00:00'
page_id: '458752852'
product: rm
source: tdn-rm
title: Grupo de Classe ABC
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+de+Classe+ABC
version: 5
---

Este cadastro é responsável por definir o percentual de cada classe A, B, C ou D.   
Considera-se em termos gerais que itens abrangendo ao total de aproximadamente 60 % do percentual calculado serão classificados como  itens A. Para os itens abrangendo a faixa de 25 % serão classificados como itens B. Os demais itens abrangentes aos 15 % serão classificados como itens C. Exemplo:

| ITEM | **CONSUMO** **(Unidade/Ano)** | CONSUMO **(R$/Unidade)** | **Custos Total (R$)** Consumido |
| --- | --- | --- | --- |
| ***1010*** | 450 | 2,35 | 1057,5 |
| ***1020*** | 23590 | 0,45 | 10615,5 |
| ***1030*** | 12025 | 2,05 | 24651,25 |
| ***1045*** | 670 | 3,6 | 2412 |
| ***1060*** | 25 | 150 | 3750 |
| ***2015*** | 6540 | 0,8 | 5232 |
| ***2035*** | 2460 | 12 | 29520 |
| ***2050*** | 3480 | 2,6 | 9048 |
| ***3010*** | 1250 | 0,08 | 100 |
| ***3025*** | 4020 | 0,5 | 2010 |
| ***3055*** | 1890 | 2,75 | 5197,5 |
| ***5050*** | 680 | 3,9 | 2652 |
| ***5070*** | 345 | 6,8 | 2346 |
| ***6070*** | 9870 | 0,75 | 7402,5 |
| ***7080*** | 5680 | 0,35 | 1988 |
| **TOTAL** | | | **107982,25** |

| Item | **Valor Consumido** | **Percentual** | **Percentual Acumulado** | **PARÂMETRO** |  |
| --- | --- | --- | --- | --- | --- |
| ***2035*** | 29520 | 27,34 | 27,34 | **A** | Até 60% Valor Total do Estoque |
| ***1030*** | 24651,25 | 22,83 | 50,17 |
| ***1020*** | 10615,5 | 9,83 | 60 |
| ***2050*** | 9048 | 8,38 | 68,38 | **B** | De 60% a 85% do Valor Total do Estoque |
| ***6070*** | 7402,5 | 6,86 | 75,23 |
| ***2015*** | 5232 | 4,85 | 80,08 |
| ***3055*** | 5197,5 | 4,81 | 84,89 |
| ***1060*** | 3750 | 3,47 | 88,36 | **C** | Restante 15% do Valor Total do Estoque |
| ***5050*** | 2652 | 2,46 | 90,82 |
| ***1045*** | 2412 | 2,23 | 93,05 |
| ***5070*** | 2346 | 2,17 | 95,23 |
| ***3025*** | 2010 | 1,86 | 97,09 |
| ***7080*** | 1988 | 1,84 | 98,93 |
| ***1010*** | 1057 | 0,98 | 99,91 |
| ***3010*** | 100 | 0,09 | **100** |  | |
| **TOTAL** | **107981,8** | **100** |
