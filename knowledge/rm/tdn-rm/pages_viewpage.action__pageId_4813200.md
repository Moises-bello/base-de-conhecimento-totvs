---
content_hash: f73816989e20ba21ac0524b790483f971e33a5de3f40ec5c6dbe46ae6a9edb70
fetched_at: '2026-06-29T00:10:19.280470+00:00'
page_id: '4813200'
product: rm
source: tdn-rm
title: Condição de Pagamento não é apresentada na Movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813200
version: 4
---

BLOCK

Condição de Pagamento não é apresentada na Movimentação

FAQ: **Condição de Pagamento não é apresentada na Movimentação**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

Condição de Pagamento não é apresentada na Movimentação.

Causa

* **Causas**

1- A condição de pagamento esta “Inativa”.

2- A condição de pagamento tem um “Tipo de Plano” diferente do utilizado na movimentação, ou seja, Compra ou Venda.

3- O parâmetro “Editar Condição de Pagamento do Cliente/Fornecedor” esta marcado no tipo de movimento, mas a condição em questão não esta informada para o Cliente/Fornecedor.

Solução

* **Solução**

1- Acessar o cadastro de condição de pagamento, editar a condição de pagamento e desmarcar a opção de “Inativo”.

2- Se o movimento é de entrada a condição de pagamento deve ter o tipo de plano marcado como “Compra”, se o movimento for de venda, o tipo de plano deverá ser “Venda”.

3- Acessar o parâmetro do tipo de movimento confirmar se o parâmetro “Editar Condição de Pagamento do Cliente/Fornecedor” esta marcado, caso esteja, acesse o cadastro do Cliente/Fornecedor utilizado no movimento e informe a condição que deseja utilizar, caso não utilize Cliente/Fornecedor na movimentação desmarque o parâmetro do tipo de movimento.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-condicao-de-pagamento-nao-e.html>
