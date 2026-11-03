---
content_hash: b32994afd251d220a99fcd1c3257d457bd460900794ffa251fa96ced62c89090
fetched_at: '2026-06-29T00:08:09.301722+00:00'
page_id: '239032812'
product: rm
source: tdn-rm
title: TUXWQ5_DT_PERMITIR_TRIBUTOS_TIPO_MOV_TOTVS_COLAB
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXWQ5_DT_PERMITIR_TRIBUTOS_TIPO_MOV_TOTVS_COLAB
version: 115
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=235601862) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CLB.007* | *TOTVS COLAB - INCLUSAO MOVIMENTO A PARTIR DE XML.* | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | *TUXWQ5.* |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |
| **País(es):** | *-* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** | *TTRBTMV e TTRBMOV* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Inclusão da opção de se buscar os tributos do Tipo de Movimento ao invés de buscar do XML na inclusão de Movimento via Totvs Colaboração

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* 11.82.43.111. ou superior

## Procedimento para Utilização

       1.            Em um tipo de Movimento configurado para recebimento de NF-e, verifique que a coluna de "Verificar Valores em" foi incluída nos parametros do tributo do ITEM

       2.            Selecione a opção Tipo de Movimento para os tributos daquele tipo

       3.            Inclua um movimento de Totvs Colaboração e verifique que os tributos foram buscados do Tipo de Movimento e não no XML

divs
