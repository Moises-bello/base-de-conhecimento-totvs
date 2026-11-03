---
content_hash: 694f62df6b3c3bffa0c37af07acc5edf26344c0be422f38872aa6b1da0a3182e
fetched_at: '2026-06-29T00:08:19.275072+00:00'
page_id: '266982294'
product: rm
source: tdn-rm
title: TVALCI_DT_Diferenca_Base_Fgts_Afastados
type: documentation
url: https://tdn.totvs.com/display/LRM/TVALCI_DT_Diferenca_Base_Fgts_Afastados
version: 1
---

# DIFERENÇA DA BASE DE FGTS DE AFASTADOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Diferença* | *Diferença Salarial* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Folha Mensal** | *Cálculo da Folha Mensal* | | *Diferença Salarial* | *Diferença Salarial* | |
| **Cadastros Iniciais:** | *Eventos* |
| **Parâmetro(s):** | *Código de Cálculo* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TVALCI* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PEVENTO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Cliente solicita a criação de código de cálculo específico para a diferença do CC 315 - BASE DE FGTS DE AFASTADOS, para os casos em que o funcionário teve reajuste salarial retroativo e ainda esteja afastado.

Nesta situação o valor da diferença deverá compor a base de FGTS.

Foi criado o código de cálculo 354 - DIFERENÇA DA BASE DE FGTS DE AFASTADOS..
