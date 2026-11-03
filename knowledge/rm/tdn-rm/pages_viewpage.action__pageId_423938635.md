---
content_hash: 7dcb070886462fb93bc35e02f431ab465f70e9e07b12fdd4a0346f5a0d3a9ce8
fetched_at: '2026-06-29T00:09:28.045925+00:00'
page_id: '423938635'
product: rm
source: tdn-rm
title: Alteração de Máscara Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938635
version: 4
---

Neste processo poderemos alterar a máscara das contas gerenciais cadastradas no RM Saldus.

**Campos**

Grupo: Informe qual grupo de contas terá a sua máscara alterada.

Máscara Atual: Será preenchida pelo sistema ao selecionar o grupo desejado.

Nova Máscara: Informe a nova máscara que este grupo estará assumindo.

**Exemplo**

Conta com máscara antiga (#.##) 5.01

Se você aumentar um nível no plano de contas ficando (#.##.##), você não poderá criar a conta 5.01.01, pois a 5.01 é Analítica. Para cadastrar a conta 5.00.01, você terá que primeiro criar a 5.00 como Sintética e depois criar a 5.00.01 como Analítica.

Conta com máscara antiga (#.##) 5.01

Se você aumentar o nº de caracteres de um nível existente (#.###) o sistema completará o nº da conta com "0" (5.001).

**Observação**

Cada grupo de contas gerenciais poderá ter uma máscara diferente. Após o cadastramento das máscaras gerenciais, o sistema permitirá que você aumente ou diminua o número de dígitos e níveis das máscaras, desde que você ainda não tenha cadastrado nenhuma conta no grupo que deseja alterar. Caso já tenha sido cadastrada alguma conta no grupo que deseja alterar, o sistema permitirá apenas o aumento de dígitos e/ou níveis das máscaras.
