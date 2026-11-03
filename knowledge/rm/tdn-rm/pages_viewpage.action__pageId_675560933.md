---
content_hash: 67ff39be1431cfb13c6fd154cbc0b50f659c4da7dc5cbfba339e0afcac0af1f4
fetched_at: '2026-06-29T00:11:17.005384+00:00'
page_id: '675560933'
product: rm
source: tdn-rm
title: Transferência de Gastos Particulares para MatMed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=675560933
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O processo de transferência para matmed tem a finalidade de transferir os itens que foram lançados erroneamente e devem ser pagos pelo convênio.

**Somente será possível transferir itens se a parcial estiver com o status "Em Elaboração".**

## **02. EXEMPLO DE UTILIZAÇÃO**

Para se transferir itens basta selecionar os itens e executar o processo "Transfere itens selecionados para MatMed"

Os itens serão estornados da aba de gastos particulares e serão lançados na aba de MatMed.

Caso selecione um item que esteja estornado o mesmo não poderá ser transferido.

        Caso informe uma quantidade de transferência incorreta, será informado o erro.

Não será permitido nenhuma movimentação no item de débito que já teve uma Nota Fiscal Gerada Por Item de Débito, do Gasto Particular.

Vide item "05. Validações para múltiplas notas fiscais em Gastos Particulares" no link <https://tdn.totvs.com/x/pObAI>

## **03. TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDDIARIAS
* SZATENDTAXASERV
* SZATENDSADT
* SZATENDMATMED
* SZATENDGASTOPARTIC
