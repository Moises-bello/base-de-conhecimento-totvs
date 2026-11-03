---
content_hash: a2cc781970c562eac415b38388e37dfbb566deb02f023a219f0ca5489cdf06e0
fetched_at: '2026-06-29T00:08:29.468461+00:00'
page_id: '272146002'
product: rm
source: tdn-rm
title: 94684_MCP-159_DT_Recebimento_Cancelamento_NFe
type: documentation
url: https://tdn.totvs.com/display/LRM/94684_MCP-159_DT_Recebimento_Cancelamento_NFe
version: 109
---

# RECEBIMENTO DE CANCELAMENTO DE NF-e

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB006 | TOTVS COLAB - VALIDAÇÃO DE XML | |
| **Tickets relacionados** | 94684 |
| **País(es):** | *Bra* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** | TNFEENTRADA, TMOV |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O Neogrid irá verificar no site da SEFAZ e as NFes que estiverem autorizadas e que constarem como canceladas serão disponibilizadas para o RM no **layout procNFe com status 399** e descrição evidenciando o cancelamento.

O TOTVS Gestão de Estoque, Compras e Faturamento irá, através da chave de acesso, buscar essa NF na tabela TNFEENTRADA;

Irá verificar na TNFEENTRADA se existe movimento vinculado à NFe e em caso positivo irá cancelá-lo (verificar todas as consistências de um processo de cancelamento de movimento tais como contábil, fiscal, financeiro, etc.).

Tendo encontrado o movimento ou não o sistema deverá também atualizar o status do registro da TNFEENTRADA para cancelado.

Caso o XML não seja encontrado na TNFEENTRADA, mesmo assim o sistema deverá procurar na base de dados se existe movimento com mesmo nº, série e fornecedor e cancelá-lo caso exista.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.16* deste chamado.

## Procedimento para Utilização

Conforme descrição acima.

divs
