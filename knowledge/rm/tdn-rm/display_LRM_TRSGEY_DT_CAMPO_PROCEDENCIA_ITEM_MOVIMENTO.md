---
content_hash: 0a4b5a8987fab6f56acbe02279f7b651979164c7e62f5703bd50e4fa1c970ef8
fetched_at: '2026-06-29T00:08:04.799176+00:00'
page_id: '235582024'
product: rm
source: tdn-rm
title: TRSGEY_DT_CAMPO_PROCEDENCIA_ITEM_MOVIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/TRSGEY_DT_CAMPO_PROCEDENCIA_ITEM_MOVIMENTO
version: 116
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.001 | INCLUSAO DE MOVIMENTO | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-.* |
| **Chamados Relacionados** | TRSGEY, TURZIJ |
| **Requisito (ISSUE):** | MOV000038 - Cálculo do movimento |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *TMOV, TITMMOV, .* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Habilitar campo Procedência no Item de Movimento quando for Movimento de Entrada e Cliente Optante pelo Simples.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.83.55, 11.82.43 ou 12.1.11*

## Procedimento para Utilização

       1.            Crie um Movimento de Entrada com o cliente Optante e o campo Procedência no Item de Movimento será exibido.

divs
