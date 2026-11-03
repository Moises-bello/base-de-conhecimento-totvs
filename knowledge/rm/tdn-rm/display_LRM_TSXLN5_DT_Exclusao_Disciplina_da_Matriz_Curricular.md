---
content_hash: 745a2445046eab7255657670dba4cd6cb852c1a729c390019dd057c5a89e2c77
fetched_at: '2026-06-29T00:06:12.204946+00:00'
page_id: '205914614'
product: rm
source: tdn-rm
title: TSXLN5_DT_Exclusao_Disciplina_da_Matriz_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXLN5_DT_Exclusao_Disciplina_da_Matriz_Curricular
version: 3
---

# Validação na exclusão de disciplinas da matriz curricular

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matriz Curricular* | *Matriz Curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Disciplinas da Matriz Curricular* | *Disciplinas da Matriz Curricular* | |
| **Cadastros Iniciais:** | *1) Disciplina cadastrada para uma matriz curricular;*  *2) Disciplina associada à uma turma* |
| **Parâmetro(s):** | *N/A**.* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server* |
| **Tabelas utilizadas:** | *SDISCGRADE, SPERIODO.* |
| **Sistema(s) operacional(is):** | *Windows 7* |
| **Versões/Release:** | *11.82.42* |

## Descrição

Validação ao excluir uma disciplina da matriz curricular. Caso a disciplina que esteja sendo excluída já esteja associada à uma turma, é lançada uma exceção bloqueando a exclusão.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.82.42)* deste chamado.

## Procedimento para Utilização

1. Cadastrar uma disciplina para a matriz.
2. Associar essa disciplina à uma turma.
3. Selecionar a ação de exclusão na visão de disciplinas da matriz curricular;
4. Como a disciplina já está associada à uma turma será levantada uma exceção e bloqueada a ação de exclusão.
