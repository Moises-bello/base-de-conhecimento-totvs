---
content_hash: 1cd9531e411b7f1658b649f3cfacf128a2f2731a13316d7b244fea2e7056394c
fetched_at: '2026-06-29T00:08:51.663635+00:00'
page_id: '337357356'
product: rm
source: tdn-rm
title: Tratamento de Baixa com Extrato não Compensado como Previsão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337357356
version: 2
---

# Considera Baixa não Compensada como Previsão no Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Fluxo de Caixa |
| **Parâmetro(s):** | Considera Baixa não Compensada como Previsão |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000255 |
| **País(es):** | Brasil |

## Descrição

Implementada opção para visualizar a baixa não compensada como valor previsto ou valor realizado. Hoje, o fluxo de caixa considera a baixa sempre como valor realizado. Caso a opção para que a baixa não compensada seja considerada como prevista, a compensação deverá ser verificada através do extrato criado para a baixa. Se o valor previsto estiver parametrizado para ser calculado pelo valor original, deve ser considerado o próprio valor original baixado.

## Procedimento para Implantação

O recurso é habilitado por meio de configuração do Fluxo de Caixa:

## Procedimento para Utilização

Considere um lançamento inicial de $1000:

Este lançamento será representado no fluxo de caixa como uma previsão de $1000:

Executando-se uma baixa parcial de $250:

O efeito no fluxo de caixa convencional, será identificar $250 como realizado:

Mas, se o sistema estiver configurado para não gerar o extrato da baixa já compensado, modificando-se o parâmetro "Considera Baixa não Compensada como Previsão", o efeito no fluxo de caixa ainda será apenas uma previsão:

O extrato poderá ser compensado em data diferente da data de baixa:

Com efeito, o fluxo de caixa representará a realização em função da data da compensação:
