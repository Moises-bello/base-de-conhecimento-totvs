---
content_hash: 296ddb668d676a49f2d110cef8d83bf9219604b359085095932a1016c74d615b
fetched_at: '2026-06-29T00:09:09.056117+00:00'
page_id: '390418773'
product: rm
source: tdn-rm
title: DT Backup e Restore de Projetos - Composições e Insumos não utilizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390418773
version: 3
---

# BACKUP E RESTORE DE PROJETOS - COMPOSIÇÕES E INSUMOS NÃO UTILIZADOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Backup e Restore de Projetos | Backup e Restore de Projetos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Exclusão de Insumos não utilizados no Projeto | Exclusão de Insumos não utilizados no Projeto | | Exclusão de Composições não utilizados no Projeto | Exclusão de Composições não utilizados no Projeto | |
| **Cadastros Iniciais:** | Projeto, Grupo de Custo, Insumo, Composição, Recurso de Composição e Tarefa. |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-4371](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4371) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Mudança no comportamento do parâmetro do processo “Não Restaurar Composições e Insumos não utilizados no Projeto”.

## Procedimento para Utilização

Em busca de uma melhor performance no processo de Backup/Restore de Projetos o comportamento do parâmetro “Não Restaurar Composições e Insumos não utilizados no Projeto” foi alterado. Anteriormente, ao marcar o parâmetro no restore, após todo o projeto ter sido restaurado, os insumos e composições não utilizados no projeto eram excluídos, fazendo com que a finalização da execução demorasse. Afim de melhorar esse desempenho, algumas melhorias foram realizadas.

* Ao fazer o backup do projeto, é verificado a utilização de composições e insumos no mesmo, e estes são marcados no arquivo ".xml" correspondente. O campo "NAOUTILIZADOPRJ" armazena essa informação:
* Ao realizar a restauração com o parâmetro marcado, insumos, composições não utilizados e todas as suas dependências, como recursos, preços de insumos, produtos associados, funções, etc, serão desconsiderados ao salvar as informações na base de dados, fazendo com o que todo o processo seja executado de forma mais rápida.
* Esse novo comportamento do restore pode ser utilizado à partir de novos backups realizados, isto é, para backups existentes antes desse ajuste, a exclusão de insumos e composições não utilizados será realizado da forma antiga.
* Um comparativo de performance, considerando antes da alteração e após a mesma, foi realizado em um projeto relativamente grande, onde foi possível observar que o backup demorou mais tempo por ter mais dados a serem analizados, porém o restore teve sua performance melhorada.
