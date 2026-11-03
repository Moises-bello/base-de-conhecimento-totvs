---
content_hash: 2801f54a8c99da98f8418c4e2772f27722c684351b9c05a8c7668a686e720d1d
fetched_at: '2026-06-29T00:10:14.373621+00:00'
page_id: '458777399'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-7101 DT Recebimento de Cancelamento de CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-7101+DT+Recebimento+de+Cancelamento+de+CT-e
version: 80
---

# RECEBIMENTO DE CANCELAMENTO DE CT-e

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Backoffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB006 | TOTVS COLAB - VALIDAÇÃO DE XML | |
| **Tickets relacionados** | N/A |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** | TNFEENTRADA, TMOV |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Os XMLs de CT-e deverão ser disponibilizados para o RM com Prefixos (**383** para evento de cancelamento e **214** para CT-e cancelado).

O TOTVS Gestão de Estoque, Compras e Faturamento irá, através da chave de acesso, buscar este documento na tabela TNFEENTRADA e executar a seguinte regra:

* Caso o XML exista e o mesmo esteja vinculado a um movimento, o sistema deve cancelar ambos os registros.
* Caso o XML exista, mas não possua vínculo com movimento, o sistema fará uma pesquisa na tabela de movimentos filtrando a chave de acesso do XML, caso encontre algum registro, este será cancelado.
* Caso NÃO exista XML, o sistema fará uma pesquisa na tabela de movimentos filtrando a chave de acesso do XML, caso a pesquisa retorne um registro, o sistema irá cancelar o movimento e incluir o XML com status "Cancelado".

Obs:  
Durante o cancelamento do movimento, todas as consistências serão realizadas. Se por algum motivo o registro não puder ser cancelado, o XML será incluído/Atualizado normalmente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos pacote de atualizações abaixo:

* 12.1.22 ou superiores.

## Procedimento para Utilização

Conforme descrição acima.

divs
