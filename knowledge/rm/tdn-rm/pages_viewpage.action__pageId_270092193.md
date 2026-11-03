---
content_hash: a149c4a467419f88ecc9b727c31ee609c5f6057e04777e6bcf5144620d52987d
fetched_at: '2026-06-29T00:08:23.801585+00:00'
page_id: '270092193'
product: rm
source: tdn-rm
title: TWDMZ5 MCP-1078 DT Buscar Unidade Pedido - TOTVS Colaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270092193
version: 119
---

# BUSCAR UNIDADE DO PEDIDO - TOTVS COLABORAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Totvs Gestão de Estoque Compras e Faturamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB 008 | *TOTVS COLAB FATURAMENTO MOVIMENTO A PARTIR DE XML* | |
| **Tickets relacionados** | *TWDMZ5* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oriacle* |
| **Tabelas Utilizadas:** | *TPARFILIAL - Parâmetros da Filial* |
| **Sistema(s) Operacional(is):** | *Windows* |

## 

## Descrição

Implementação de novo parâmetro (campo BUSCAUNIDADEPEDIDOCOLAB da tabela TPARFILIAL), para permitir que o usuário opte por buscar as unidades do pedido e não do XML durante o processo de tradução de itens no Totvs Colaboração..

Esse procedimento somente afeta o processo de faturamento via totvs colaboração.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.13.129* deste chamado.

## Procedimento para Utilização

       1.            O parâmetro foi implementado no seguinte caminho: **Ambiente > Parametros > Totvs Gestão de Estoque, Compras e Faturamento > Integrações > Dados Fiscais > aba Informações Totvs Colaboração.**

       2.            Após selecionar esse parâmetro, execute o processo de faturamento, e, após selecionar o XML, as unidades de Medida serão buscadas do Movimento de Origem (Pedido) e não mais do XML.

divs
