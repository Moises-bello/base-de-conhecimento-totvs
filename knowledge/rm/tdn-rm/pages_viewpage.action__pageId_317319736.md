---
content_hash: 08397a789cfdc3259f4eefcd1cb77a7ecbccb00b93fd51e0ac59c3b7b22e59c1
fetched_at: '2026-06-29T00:08:47.014196+00:00'
page_id: '317319736'
product: rm
source: tdn-rm
title: DT Seleção de plano de pagamento na matrícula do ensino básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317319736
version: 1
---

# SELEÇÃO DE PLANO DE PAGAMENTO NA MATRÍCULA DO ENSINO BÁSICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Totvs Gestão Educacional* |
| **Módulo:** | *Matrícula do ensino básico* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rematrícula* | *Seleção de plano de pagamento* | |
| **Cadastros Iniciais:** | *Planos de pagamento;*  *Default de plano de pagamento na parametrização por curso;*  *Plano de pagamento no contrato do aluno;* |
| **Parâmetro(s):** | RM Portal - Matrícula | Portal - Contrato Financeiro 1/3 | Visualizar/Alterar plano de pagamento |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [PORTALMOBILE01-12](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-12) |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

A seleção de plano de pagamento da matrícula do ensino básico leva em consideração a seguinte regra:

Caso o parâmetro 'Visualizar/Alterar plano de pagamento' esteja marcado, ao acessar o portal, o usuário terá a possibilidade de alterar o plano de pagamento, essa alteração seguirá a seguinte condição:

* Aluno possui contrato e já possui algum lançamento gerado:
  + Será exibido no portal apenas o plano de pagamento definido no contrato.
* Aluno possui contrato SEM lançamento gerado:
  + Serão exibidos no portal todos os planos de pagamento disponíveis para o período letivo, sendo que o plano definido no contrato já virá marcado como padrão.
* Aluno NÃO possui contrato:
  + Nesse caso será verificado o plano de pagamento default definido na parametrização por curso. Serão exibidos no portal todos os planos de pagamento disponíveis para o período letivo, sendo que o plano definido na parametrização por curso já virá marcado como padrão.
* Aluno NÃO possui contrato e não existe plano de pagamento default informado na parametrização por curso:
  + Serão exibidos no portal todos os planos de pagamento disponíveis para o período letivo, mas nenhum deles estará marcado por padrão. O usuário precisará selecionar para prosseguir com a matrícula.

Caso o parâmetro 'Visualizar/Alterar plano de pagamento' NÃO esteja marcado, ao acessar o portal, o usuário não verá a etapa de plano de pagamento durante a matrícula.
