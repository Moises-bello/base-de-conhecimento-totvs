---
content_hash: c4f72aece1100551df77fcca824bc45ec68af26cf70a39722f24e478d823fdca
fetched_at: '2026-06-29T00:10:19.306748+00:00'
page_id: '4813260'
product: rm
source: tdn-rm
title: Lote do Produto não é apresentado na movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813260
version: 4
---

BLOCK

Lote do Produto não é apresentado na movimentação

FAQ: **Lote do Produto não é apresentado na movimentação**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

Lote do produto não é apresentado na movimentação

Causa

* **Causas**

1- Se o tipo de movimento é de entrada deverá ser verificado se o parâmetro “*Consiste Fornecedor do Lote*” estar marcado e se o fornecedor da movimentação é o mesmo do lote.

2- O status do lote do produto movimentado que pretende utilizar, não esta marcado/selecionado dentro do tipo de movimento etapa *Item - Lote /Grade Numerada / Número de Série.*

3- No cadastro de “Status do Lote do Produto” no *menu / Cadastros / Tabelas Auxiliares* a opção “*Bloqueada*” esta marcado.

4- Se efeito sobre os saldos físicos (*saldos do balanço, saldo atual, pedido a fornecedor, pedido a cliente, saldo 5 ao saldo10 que podem ter seus nomes definidos pelo usuário*) estiverem como ***DIMINUI*** para alguns saldo no tipo de movimento, o lote só será apresentado se existir quantidade em estoque para o saldo parametrizado. Lembrando que se existir efeito de saldo para mais de um produto, o sistema só irá apresentar o lote se existir saldo para os dois saldos parametrizados.

Solução

* **Solução**

1- Se realmente o parâmetro “*Consiste Fornecedor do Lote*” tiver que ficar marcado, os lotes devem ser associados ao fornecedor da movimentação, lembrando que só é possível associar um fornecedor por lote, caso contrario desmarque o parâmetro.

2- Verificar qual o “Status” do lote que não esta sendo apresentado e marcar o mesmo dentro do tipo de movimento etapa *Item - Lote /Grade Numerada / Número de Série.*

3- Verificar qual o “Status” do lote que não esta sendo apresentado na movimentação e desmarcar a opção “*Bloqueada*” no cadastro de “Status do Lote do Produto” se for o caso.

4- Verificar se existe saldo para a Filial, para Local de Estoque e para o Lote do produto em relação ao saldo parametrizado no tipo de movimento como ***DIMINUI,*** *pois só são apresentados os lotes caso exista saldo em estoque para os “Saldos Definidos” no tipo de movimento,* (*saldos do balanço, saldo atual, pedido a fornecedor, pedido a cliente, saldo 5 ao saldo10 que podem ter seus nomes definidos pelo usuário*)

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-lote-do-produto-nao-e-apresentado.html>
