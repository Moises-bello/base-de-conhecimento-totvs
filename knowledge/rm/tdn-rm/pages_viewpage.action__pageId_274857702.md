---
content_hash: 32c5e62307729f71f201e37615f4ab2cc1d1b22be408e8f0a7ea1264c2576a9e
fetched_at: '2026-06-29T00:08:35.246380+00:00'
page_id: '274857702'
product: rm
source: tdn-rm
title: 920651 EDUCACIONAL01-983 DT Execução de Prova Offline
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274857702
version: 97
---

# EXECUÇÃO DE PROVA OFFLINE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Avaliação e Pesquisa e Totvs Executor |
| **Função:** | Geração e execução de prova offline |
| **Situação/Requisito:** | Sistema emite erro de XML inválido ao tentar executar a prova offline gerada pelo Totvs Avaliação e Pesquisa (Testis) no Totvs.Executor |
| **Solução/Implementação:** | Foi alterada a codificação de caracteres para UTF7 na geração da prova offline e importação de prova no Totvs.Executor. O erro ocorria porque no texto da questão existia o caracter unicode (0x8230) que fazia com que o xml gerado fosse inválido. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
