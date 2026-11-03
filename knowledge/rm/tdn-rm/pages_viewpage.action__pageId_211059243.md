---
content_hash: 041108a7347ff9f9ae823ba6b63f1eec8c376f818cc62e7212bc7d831e555437
fetched_at: '2026-06-29T00:06:15.552307+00:00'
page_id: '211059243'
product: rm
source: tdn-rm
title: TSUBRU_DT_Performance_Exibição_Lançamentos_Matrícula_Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211059243
version: 1
---

# Melhoria de performance na exibição de lançamentos da Matrícula Online.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula Online* | *Matrícula Online no Portal Educacional* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Exibição de lançamentos na Matrícula Online** | Matrícula Online | | **Exibição de Lançamentos e Boletos na tela de Extrato Financeiro do aluno** | Extrato Financeiro | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *"Gerar Lançamentos" nas parametrizações da Matrícula no Portal* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8, 8.1 e 10* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.41.105* |
| **Versão Expedida:** | *11.82.41.106* |

## Descrição

Foi realizado uma melhoria de performance na consulta que exibe os lançamentos financeiros e detalhes de boleto na tela de Extrato Financeiro, que também é exibida no final do processo da Matrícula Online, caso parametrizado, exibindo apenas os lançamentos financeiros gerados durante o processo de matrícula.

divs
