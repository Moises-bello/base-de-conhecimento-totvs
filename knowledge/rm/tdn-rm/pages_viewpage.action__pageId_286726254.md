---
content_hash: 8671bf4df4da8e2182bad1a1d809345a8f1e46390bcc43a4e65b68fda6e48e90
fetched_at: '2026-06-29T00:08:41.418126+00:00'
page_id: '286726254'
product: rm
source: tdn-rm
title: 1109600 MSAU-12646 DT Parametrizar Alertas de Mensagens Não Impeditivas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286726254
version: 102
---

# Parametrizar Alertas de Mensagens nao Impeditivas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Elaboração de Contas | Lançamento na Conta do Paciente | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZPARAMGERALC |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Na tela "Elaboração de Contas", ao encerrar uma conta o sistema deve apresentar o relatório só com mensagens impeditivas caso o parâmetro "Mostrar Relatório com Mensagens não Impeditivas" estiver marcado.

## Procedimento para Utilização

Menu: Tesouraria / Lançamento na Conta do Paciente Buscar um Paciente com registro de internação.

Ao marcar o parâmetro "Mostrar Relatório de Mensagens Não Impeditivas" no Menu Cadastro Geral Aba Faturamento II

O sistema deve imprimir o relatório de Mensagens Não Impeditivas

Ao desmarcar o parâmetro "Mostrar Relatório de Mensagens Não Impeditivas" no Menu Cadastro Geral Aba Faturamento II

O sistema não deverá imprimir o relatório.

divs
