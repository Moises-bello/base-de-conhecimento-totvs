---
content_hash: 0e25e17a585690288d647156ec0ea352a41095f1a0576dcba63d9782679def9a
fetched_at: '2026-06-29T00:08:31.913177+00:00'
page_id: '273975207'
product: rm
source: tdn-rm
title: 724360 DUCACIONAL01-120 Filtro SQL na geração de lançamento não considera a
  variavel :$CODFILIAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273975207
version: 108
---

# Geração de Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOT VS Gestão Educacional |
| **Função:** | Seleção de alunos através da consulta SQL na geração de Lançamentos Financeiros |
| **Situação/Requisito:** | Ao selecionar os alunos através da opção consulta SQL e utilizar uma consulta SQL que contenha a variável :$CODFILIAL ou outras qualquer permitida pelo recurso de consulta SQL do RM o sistema estava apresentando erro e não identificando corretamente o a informação de forma automática. |
| **Solução/Implementação:** | Alguns processos no educacional permitem que os usuários utilizem consultas SQL previamente cadastradas no RM para carregar informações que serão processadas.  Realizamos um ajuste para que as variáveis documentadas no link abaixo sejam interpretadas caso sejam utilizadas em uma das consultas SQL.  <http://tdn.totvs.com/pages/viewpage.action?pageId=63275590> |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 724360 |
| **Requisito:** |  |

divs
