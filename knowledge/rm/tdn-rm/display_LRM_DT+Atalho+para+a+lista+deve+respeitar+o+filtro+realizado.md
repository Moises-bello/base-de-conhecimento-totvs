---
content_hash: 97a70f5862a35b4f878235f821e25db5f1ed4f97d9686159e6bb9ab6bde6fea1
fetched_at: '2026-06-29T00:09:52.454802+00:00'
page_id: '439366620'
product: rm
source: tdn-rm
title: DT Atalho para a lista deve respeitar o filtro realizado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Atalho+para+a+lista+deve+respeitar+o+filtro+realizado
version: 2
---

# FILTROS - DASHBOARD e LISTA DE ALUNOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Retenção de Alunos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Filtros | Filters.component.ts |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Filtros - Dashboard | Filters.component.ts | | Filtros - Lista de Alunos | Filters.component.ts | |
| **Cadastros Iniciais:** | Lista de alunso evasores deve estar populada. |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | /#/dashboard  /#/students |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [DEDUANALYTICS-676](http://jiraproducao.totvs.com.br/browse/DEDUANALYTICS-676 "Atalho para a lista respeitar o filtro realizado") |
| **País(es):** | Todos os países |
| **Banco(s) de Dados:** | N/A |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | N/A |
| **Pacote:** | N/A |

## Descrição

O Dashboard e a lista de alunos evasores foram ajustados para armazenarem o último filtro em memória. Com isso, ao acessar a tela os últimos filtros realizados sempre serão carregados automaticamente.

Também foi realizado um outro ajuste para copiar os filtros do dashboard para a lista de alunos, quando o usuário clicar no link "Prováveis evasões".
