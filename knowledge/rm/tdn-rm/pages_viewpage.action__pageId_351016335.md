---
content_hash: 235a1d5ebf3605c4e02cde56f0492bc43f403422cb6568087acd61f7322c911a
fetched_at: '2026-06-29T00:08:55.513891+00:00'
page_id: '351016335'
product: rm
source: tdn-rm
title: DT Extrato financeiro do aluno - Valores de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351016335
version: 1
---

# Visualização do extrato financeiro no portal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Financeiro. | Extrato financeiro. | |
| **Cadastros Iniciais:** | Parametrização dos valores de integração.([Valores de Integração](http://tdn.totvs.com.br/pages/viewpage.action?pageId=320375713)) |
| **Parâmetro(s):** | Informe os parâmetros utilizados. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PORTALMOBILE01-2909 |
| **País(es):** | Todos os países. |
| **Banco(s) de Dados:** | Todos. |
| **Tabelas Utilizadas:** | N/A. |
| **Sistema(s) Operacional(is):** | Todos. |

## Descrição

Dando continuidade na implementação dos valores de integração foi realizada uma adequação dos portais do aluno para visualizar os valores de integração na visão de extrato financeiro do aluno.  
Após esta alteração, o usuário não selecionará mais quais campos serão visíveis no portal do aluno(Ex.: VALOROP1, VALOROP2, etc...) e sim qual "valor de funcionalidade" será exibido (Ex.: Exibir bolsa condicional e/ou bolsa incondicional).  
A visualização dos valores é "transparente" para o usuário, ou seja, se o valor vem de um campo opcional ou de integração não é exibido para o usuário, exibindo apenas o valor da funcionalidade selecionada.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. A criação e utilização dos valores de integração podem ser visualizadas na documentação ([Valores de Integração](http://tdn.totvs.com.br/pages/viewpage.action?pageId=320375713))
2. A parametrização da visualização destes valores, no portal do aluno, deve ser realizada no parâmetro: Parâmetros | RM Portal | Gerais | Portal - Geral 8/12 |  Valores a exibir.
