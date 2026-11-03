---
content_hash: 54d1c5d88668416298d6e21ba344da1aa92acd0cd2984bb06a2854292022d6a8
fetched_at: '2026-06-29T00:08:31.257461+00:00'
page_id: '273297579'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-150 Inclusão do campo "Assunto" no cadastro de mensagens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273297579
version: 113
---

# Cadastro de Mensagens

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Mensagens* | *MovMenAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Mensagens* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | MovMenAction |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-150 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TMEN* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O Cadastro de Mensagens foi evoluído com o objetivo de controlar também mensagens de E-mail.

Na tela de edição do cadastro de Mensagens foi incluída uma nova classificação com o nome "E-mail", ao selecionar a mesma, o sistema exibe o campo "Assunto" e altera o nome do campo "Descrição" para "Mensagem".

**Nova Classificação:**

**Campo Assunto:**

**Consistência:**

Ao salvar uma mensagem, caso o registro possua a classificação "E-mail" e o campo "Assunto" esteja vazio, o sistema exibirá a seguinte mensagem de erro:

divs
