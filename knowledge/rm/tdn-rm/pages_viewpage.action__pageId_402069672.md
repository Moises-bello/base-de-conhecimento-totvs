---
content_hash: d9891eebad40c40673da5e9822c8a2f3ed3be751a202212f547f6432d5f97695
fetched_at: '2026-06-29T00:09:10.644232+00:00'
page_id: '402069672'
product: rm
source: tdn-rm
title: DT_Uso_de_expressão_na_fórmula_COMPIMSDERIVADO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=402069672
version: 2
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fórmulas | Informe o nome técnico da rotina. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Não se aplica |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPORCAPLAN001-2881 |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | Todos |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Não se aplica |
| **Pacote:** | Não se aplica |

## Descrição

  A função de fórmula COMPIMSDERIVADO passa a permitir que o parâmetro da mesma seja, além de um campo da tabela MRECCMP, uma expressão utilizando estes campos.

  Esta expressão deve ser uma expressão utilizando as operações matemáticas (+, -, \* ,/) entre os campos da tabela MRECCMP que retorne um valore inteiro ou decimal.

  Exemplos:

 - COMPIMSDERIVADO('QUANTIDADE / 10000 \* COEFICIENTEPRODUTIVO')

 - COMPIMSDERIVADO('VALORTOTAL \* 2 / 100')
