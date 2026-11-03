---
content_hash: 447cd64fb5fbc81c45f849d1da40b310ed9d3c04a49711e8c3302a8b220b1137
fetched_at: '2026-06-29T00:08:57.241281+00:00'
page_id: '353286085'
product: rm
source: tdn-rm
title: 743538 RMSAU-3349 DT Listar exames de acordo com a ordem de lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353286085
version: 4
---

# Listar exames de acordo com a ordem de lançamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Unidades Diagnóstico / Registro de Atendimentos Externos | Registro de Atendimentos Externos | |
| **Tickets relacionados** | [Ticket #743538](https://totvssuporte.zendesk.com/agent/tickets/743538 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-3349 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server@ e ORACLE@ |
| **Tabelas Utilizadas:** | SZPEDEXAMEITEM |
| **Sistema(s) Operacional(is):** | Windows@ |

## Descrição

Adicionado o campo Ordenar na aba Exames Solicitados para visualizar os exames já lançados pela ordem de lançamento, para facilitar a visualização e conferência do lançamento, quando estiver realizando os pedidos de exame, na rotina de registro de atendimento externo.

1. Acessar o RM Saúde, menu Unidades de Diagnóstico / Registro de Atendimentos Externos, aba Exames Solicitados
2. Selecionar uma opção no campo ordenar, entre elas:  
   Departamento  
   Código Exame  
   Ordem Lançamento (Seq. Exame)  
   Descrição  
   Previsão de Execução  
   Observação

   *O campo Previsão de Execução está disponível a partir da versão 12.1.20*
