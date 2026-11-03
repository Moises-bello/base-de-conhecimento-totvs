---
content_hash: 41d3a1b7aab7052c0e686b327820e57b2cb1af48a560048e3087be5eabaadd0f
fetched_at: '2026-06-29T00:09:08.486390+00:00'
page_id: '389549751'
product: rm
source: tdn-rm
title: DT - TOPORCAPLAN001-4294 - Backup e Restore de Projeto e Agendamento de Restore
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+TOPORCAPLAN001-4294+-+Backup+e+Restore+de+Projeto+e+Agendamento+de+Restore
version: 3
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Backup e Restore. | PrjBackupRestoreAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | N/A. | N/A. | |  |  | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-4294](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4294) |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | N/A. |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A. |

## Descrição

* Melhorar a tela do processo para identificar se estamos fazendo um Backup ou Restore.
* Habilitar a opção de agendamento do Restore.
* Melhorar o log do processo.

## Procedimento para Implantação

1 - Foi alterado os cabeçalhos do processo de Backup e Restore a comportar-se adequadamente de acordo com o que se está executando.

2 - No log do processo foi incluído:

* A hora de execução dos eventos.
* Detalhamento entre as etapas do processo.
* Log específico para o parâmetro 'Não Restaurar Composições e Insumos não utilizados no Projeto'.

Melhoria no log do processo, incluindo hora de execução dos eventos e detalhando o nome dos mesmos

**Backup:**

**Restore:**

Além disso o processo Restore tem agora a opção de agendamento.

Segue um exemplo de como o log foi alterado para que contenha a hora de execução dos eventos,   
além de ter diferenciação entre o as etapas do processo.
