---
content_hash: 078e12108eb8ad388b98c738f75ddb532f1054d649630d6422a69d5cd3e30f25
fetched_at: '2026-06-29T00:09:28.044189+00:00'
page_id: '423938633'
product: rm
source: tdn-rm
title: Alteração de Máscara Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938633
version: 2
---

Neste processo poderemos alterar a máscara das contas contábeis cadastradas no RM Saldus.

**Campos**

Grupo: Informe qual grupo de contas terá a sua máscara alterada.

Máscara Atual: Será preenchida pelo sistema ao selecionar o grupo desejado.

Nova Máscara: Informe a nova máscara que este grupo estará assumindo.

**Exemplo**

Conta com máscara antiga (#.#.#.#.###) 1.1.1.1.001

Se você aumentar um nível no plano de contas ficando (#.#.#.#.###.###), você não poderá criar a conta 1.1.1.1.001.001, pois a 1.1.1.1.001 é Analítica. Para cadastrar a conta 1.1.1.1.000.001 você terá que primeiro criar a 1.1.1.1.000 como Sintética e depois criar a 1.1.1.1.000.001 como Analítica.

Conta com máscara antiga (#.#.#.#.###) 1.1.1.1.001

Se você aumentar o nº de caracteres de um nível existente (#.##.##.##.#####) o sistema completará o nº da conta com "0" (1.01.01.01.00001).

**Observação**

Cada grupo de contas contábeis poderá ter uma máscara diferente. Após o cadastramento das máscaras contábeis o sistema permitirá que você aumente ou diminua o número de dígitos e níveis das máscaras, desde que você ainda não tenha cadastrado nenhuma conta no grupo que deseja alterar. Caso já tenha sido cadastrada alguma conta no grupo que deseja alterar, o sistema permitirá apenas o aumento de dígitos e/ou níveis das máscaras.
