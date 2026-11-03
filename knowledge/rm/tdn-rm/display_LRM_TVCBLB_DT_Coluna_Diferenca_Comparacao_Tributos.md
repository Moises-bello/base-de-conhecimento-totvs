---
content_hash: af28f7a907e489b3199ad2e214587a99c3b6b5b98b10bf92eabb5fcf3de3206e
fetched_at: '2026-06-29T00:08:12.939275+00:00'
page_id: '243655249'
product: rm
source: tdn-rm
title: TVCBLB_DT_Coluna_Diferenca_Comparacao_Tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCBLB_DT_Coluna_Diferenca_Comparacao_Tributos
version: 109
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB.007 | TOTVS COLAB - INCLUSAO MOVIMENTO A PARTIR DE XML | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TVCBLB |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |
| **País(es):** | *Bra* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | - |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Na tela de comparação de tributos da inclusão de movimentos através de XML foi acrescentada uma coluna onde será apresentada para cada tributo a diferença do valor do imposto constante do XML e do valor do imposto calculado conforme a parametrização do tipo de movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.12*

## Procedimento para Utilização

       1.            Parametrize o tipo de movimento para buscar tributos no tipo de movimento.

       2.            Inclua um movimento com XML que contenha os tributos parametrizados e que os valores desses tributos sejam diferentes dos parametrizados no tipo de Movimento para que o sistema exiba a tela de comparação de tributos.

       3.            A coluna "Diferença de Valores" deve ser exibida conforme abaixo:

divs
