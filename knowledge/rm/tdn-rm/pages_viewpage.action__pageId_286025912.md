---
content_hash: a919e2ca263460be6c018f4ae78b27621046cdb2082d036bed7d6a75c0b16011
fetched_at: '2026-06-29T00:08:39.934246+00:00'
page_id: '286025912'
product: rm
source: tdn-rm
title: 978139 FINANCEIRO01-1061 Erro em Encerramento Mensal de Aplicação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286025912
version: 102
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Aplicação Financeira |
| **Função:** | Encerramento Mensal |
| **Situação/Requisito:** | O saldo real fica incorreto no encerramento mensal caso seja feita uma aplicação inicial, um resgate parcial e um encerramento mensal no mesmo dia. |
| **Solução/Implementação:** | Removido by-pass que desconsiderava a regra de cálculo de impostos e saldo real, caso o resgate ocorra na mesma data da aplicação. |
| **Conversores e Parâmetros:** | N/D |
| **Tickets relacionados:** | N/D |
| **Requisito:** | FIN000091 |

divs
