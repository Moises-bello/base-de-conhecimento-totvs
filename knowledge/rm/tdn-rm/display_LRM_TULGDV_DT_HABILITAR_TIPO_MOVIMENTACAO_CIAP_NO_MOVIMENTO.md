---
content_hash: 0df9f5c50a9582d1e89e2d6b75b8b43f5fc26e272cf16e92f4e8ed6be1877971
fetched_at: '2026-06-29T00:06:30.349840+00:00'
page_id: '235320068'
product: rm
source: tdn-rm
title: TULGDV_DT_HABILITAR_TIPO_MOVIMENTACAO_CIAP_NO_MOVIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/TULGDV_DT_HABILITAR_TIPO_MOVIMENTACAO_CIAP_NO_MOVIMENTO
version: 118
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=219695506) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PAR.014 | PARAMETRIZACAO - TIPO DE MOVIMENTO. | |
| **Chamados Relacionados** | TUGTAX |
| **Requisito (ISSUE):** | MOV000003 - Movimento |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *TITMMOVFISCAL* |

## Descrição

Implementação do campo "Tipo Movimentação CIAP" no Tipo de Movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado 11.82.42.133 ou superior

## Procedimento para Utilização

Verifique a aba fiscal do item de Movimento e verifique o campo "Tipo de Movimentação do Bem ou Componente".

divs
