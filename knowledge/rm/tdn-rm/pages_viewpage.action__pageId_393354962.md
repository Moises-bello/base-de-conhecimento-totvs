---
content_hash: 24db8fea05c605d8551c1962e299bd27970ca74bfc58c985cfa9ad2eda92dedd
fetched_at: '2026-06-29T00:09:09.232675+00:00'
page_id: '393354962'
product: rm
source: tdn-rm
title: DT Aumento de períodos do projeto com índices de Análise de Valor Agregado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393354962
version: 1
---

# AUMENTO DE PERÍODO DO PROJETO COM ÍNDICES DE ANÁLISE DE VALOR AGREGADO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetros de Projeto | Parâmetros de Projeto |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Períodos do Cronograma | Períodos do Cronograma | | Análise de Valor Agregado | Análise de Valor Agregado | |
| **Cadastros Iniciais:** | Projeto, Períodos de Cronograma, Tarefas. |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-3615](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-3615) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Validação de existência de Análise de Valor Agregado quando alterados os períodos do cronograma.

## Procedimento para Utilização

Na tela de Parâmetros de Projeto ao alterar ou incluir novos períodos do cronograma, é realizado uma validação para verificar se existem informações geradas para a Análise de Valor Agregado, sendo elas de Tarefas, Centros de Custo ou Recursos. No caso de existir tais informações duas regras são consideradas, em caso de violação das mesmas, os períodos não poderão ser alterados:

* Consistir se algum dos períodos presente na AVA teve o seu intervalo de datas alterado;
* Consistir se algum dos períodos presente na AVA foi excluído nos parâmetros do projeto.
