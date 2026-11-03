---
content_hash: 4d57a74735114584808b0262313f5d6a14b49f7f2c037d2a9603abc09681a51a
fetched_at: '2026-06-29T00:08:57.007040+00:00'
page_id: '351390486'
product: rm
source: tdn-rm
title: DEDUANALYTICS-80 DT Migração das consultas de dimensão para o Fast Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351390486
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional. |
| **Módulo:** | Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração de Dimensões. | Extração de Dimensões. | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | Parâmetros que precisa ser configurados no arquivo my.properties:  1) Instância do Produto:  param.GERAL\_INSTANCIA='RM'  2): Definição dos cursos que serão exportados:  param.CURSOEDUCACIONAL\_PARAMS="CÓDIGO DOS CURSOS".  3)Definição dos períodos letivos que serão exportados:  param.PERIODOLETTIVO\_PARAM="ID DOS PERÍODOS LETIVOS". |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUANALYTICS-80 |
| **País(es):** | Todos. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | N/A. |

## Descrição

Criação das consultas para extração de dimensões para utilização no Fast Analytics.
