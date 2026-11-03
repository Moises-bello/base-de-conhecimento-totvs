---
content_hash: 87cd42b0d220bd3ea22a30a8539a32cf56a75e810037b44b07044e294d77be40
fetched_at: '2026-06-29T00:09:09.803405+00:00'
page_id: '394207853'
product: rm
source: tdn-rm
title: 3364382 DSAUGHSCC-947 UTILIZAR MOVIMENTAÇÃO DE ESTOQUE NO RM, MESMO INTEGRADO
  COM PROTHEUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394207853
version: 3
---

# UTILIZAR MOVIMENTAÇÃO DE ESTOQUE NO RM, MESMO INTEGRADO COM PROTHEUS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação de Estoque | | Mapa de Dispensação | | Etiquetas de Código de Barras | | Monta/Desfaz kit pré-montado | | CME | |
| **Parâmetro(s):** | Utiliza movimentação de estoque do Backoffice RM |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

A implementação consiste em possibilitar movimentar estoque no Backoffice RM, mesmo integrado com o Protheus. Somente a parte as rotinas de Movimentação de Estoque, Mapa de dispensação, Etiquetas de Código de Barras, Monta/Desfa Kit Pré-montado e CME, serão afetadas.

A entrada de nota fiscal de compras é feita no Protheus e sincronizada com o RM para que o saldo dos produtos sejam atualizados. As movimentações financeiras são integradas com o Protheus conforme produto padrão.

## Procedimento para Utilização

1. Parametrizar o sistema para utilizar o Backoffice RM somente para a movimentação de estoque. Acesse o menu Opções / Parâmetros / Parâmetros de Integração
2. Na mesma tela, porém na página Tipos de mov. Estoque, será necessário informar os tipos de movimento relacionados ao RM Nucleus
3. Com esta parametrização, o sistema passará a movimentar estoque somente no RM, ou seja, nas telas de Movimentação de Estoque, Mapa de dispensação, Etiquetas de Códigos de Barras, CME, Monta/Desfaz Kit pré-montado, funcionarão como se o sistema não tivesse integração com o Protheus
4. É necessário parametrizar os Tipos de Movimento do Backoffice para movimentar estoque.
