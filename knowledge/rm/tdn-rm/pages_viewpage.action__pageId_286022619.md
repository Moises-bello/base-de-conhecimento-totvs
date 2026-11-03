---
content_hash: d1b670cee2dfbe61ac2b0bd2f499a74982ddc247b60c711d66eeb5319619467d
fetched_at: '2026-06-29T00:08:39.844683+00:00'
page_id: '286022619'
product: rm
source: tdn-rm
title: RMFIN00008_E_Funcional_Relatórios de boletos buscando dados do ERP Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286022619
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Versões:** | 12.1.17 e 12.1.18 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** |  |

## Objetivo

Possibilitar que sejam emitidos os relatórios de boletos (banco Bradesco, Caixa, Santander e Itaú) buscando as informações que se encontram no Protheus.

## Definição da Regra de Negócio

Eu, como analista financeiro, preciso utilizar relatórios de boletos que buscam informações do Protheus para os bancos Bradesco, Caixa, Santander e Itaú.

Ex: O cliente possui o portal do TIN  necessita emitir um boleto, ocorre que o backoffice do cliente é Protheus, desta maneira o relatório para funcionar irá verificar as informações das tabelas do Protheus.

Para buscar as informações será necessário criar os relatórios no RM Reports utilizando o recurso de fonte de dados externo. Desta maneira seria possível pelo "De-Para" identificar os campos necessários.

6
incomplete
**Critérios de aceitação:**

* Utilizando como base os relatórios existentes no book, devem ser elaborados novos relatórios buscando os dados dos boletos do Protheus.
* Deverá ser disponibilizada a documentação desta funcionalidade: documento técnico e novidades.
* Deverá ser disponibilizado nas versões 12.1.17 e 12.1.18.

 Verificar se ao utilizar uma fonte de dados externo, o relatório não irá perder as informações quando o banco de dados externo for alterado, ou seja, precisamos verificar se é possível construir relatórios genéricos utilizando como fonte de dados um banco externo considerando que cada cliente tem seu banco de dados.
