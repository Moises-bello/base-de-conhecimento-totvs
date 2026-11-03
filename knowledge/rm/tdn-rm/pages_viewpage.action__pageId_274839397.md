---
content_hash: 15f4b1ab10e7616e7e16c1a8765fb02e0da94d61515d5c9e7cedad01fe7e78cb
fetched_at: '2026-06-29T00:08:34.753887+00:00'
page_id: '274839397'
product: rm
source: tdn-rm
title: 811261 MATFATCMPCRM01-444 Motivo de Referência para Devolução por Recusa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274839397
version: 110
---

# Motivo de Referência para Devolução por Recusa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Construção e Projetos** |
| **Módulo:** | **T**OTVS Gestão de Estoque Compras e Faturamento**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | NF 01 0045 | *NF E ENVIO* | |
| **Cadastros Iniciais:** | *.* |
| **Parâmetro(s):** | *.* |
| **Ponto de Entrada:** | *.* |
| **Tickets relacionados** | *[811261](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22811261%22 "811261")* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | **MATFATCMPCRM01-444** |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TMOTIVOREFMOV* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Criado um novo motivo de referência chamado "Devolução por Recusa". Esse motivo é similar ao "Devolução por Venda" mas sem exigir o preenchimento do Cliente/Fornecedor.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.16.117*

## Procedimento para Utilização

       1.  Acessar o cadastro de Motivo de Referência (Cadastros -> mais -> Tabelas Auxiliares -> Motivo Referência) e executar o processo "Inclusão de Motivo de Referência".

            Isso irá criar o novo Motivo de Referência.

       2.  Após isso, haverá o novo Motivo de referência (30 - Devolução por Recusa) que não mais exigirá o Cliente/Fornecedor igual ao do Movimento de origem

.

divs
