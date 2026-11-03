---
content_hash: 2e4149fce8d8f48e83b94f88f921884b9dc5ec0ed0ef208dd0c99da40836e5ac
fetched_at: '2026-06-29T00:09:10.024047+00:00'
page_id: '394223936'
product: rm
source: tdn-rm
title: DT - Alteração na Geração de Pedido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394223936
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Pedido de Material. | Geração de Pedido de Material. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Insumo. | Cadastro de Insumo. | | Alteração Geral de Insumo. | Alteração Geral de Insumo. | |
| **Cadastros Iniciais:** | Projeto, Tarefa, Insumo, Pedido de Material. |
| **Parâmetro(s):** | Não se Aplica. |
| **Ponto de Entrada:** | Não se Aplica. |
| **Tickets relacionados** | Não se Aplica. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPORCAPLAN001-4502. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | Não se Aplica. |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | Não se Aplica. |

## Cadastro de Insumo

Devido a necessidade de realizar o Pedido de Material completo em apenas um Pedido por se tratar de Insumos cujo devem ser comprados de um mesmo Lote minimizando a possibilidade de diferença do material Ex.: Cor, tamanho etc.. Foi incluído no Cadastro de Insumo as opções Tipo de Compra:

* Padrão: Insumos pedidos conforme o Cronograma.
* Não Compra Fracionado: Insumos cujo Pedido não poderá ser feito em quantidade fracionada, exemplo: 1,5 sacos de cimento;
* Compra Única: Insumo cujo Pedido de Material será criado com a necessidade total do mesmo no Projeto, exemplo: Materiais fabricados em Lote, tinta, cerâmicas etc..

## Geração de Pedido de Material

A criação de um novo Pedido de Material passa a obedecer o Tipo da Compra cadastrada no Insumo.

## Alteração Geral de Insumo

Foi incluído na Alteração Geral de Insumo na opção de Fracionamento o Tipo da Compra, com ele o usuário poderá alterar o Tipo da compra no cadastro de insumo.
