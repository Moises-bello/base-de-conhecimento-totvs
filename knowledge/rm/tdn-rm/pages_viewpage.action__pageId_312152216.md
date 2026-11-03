---
content_hash: 43a08d5406bc5cb2d7194c3699cfec931980e035f20b959bbd30a11ad134c3b3
fetched_at: '2026-06-29T00:08:45.653535+00:00'
page_id: '312152216'
product: rm
source: tdn-rm
title: 1593359 FINANCEIRO01-3619 Baixa por acordo de lançamento baixado parcialmente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312152216
version: 92
---

# BAIXA POR ACORDO DE LANÇAMENTO BAIXADO PARCIALMENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa por acordo financeiro. |
| **Situação/Requisito:** | Valores do acordo (Juros, Desconto e Acréscimo) não eram salvos no item de baixa do lançamento baixado por acordo quando o mesmo possuía status "Parcialmente Baixado". |
| **Solução/Implementação:** | Em lançamentos financeiros baixados por acordo, quando o parâmetro **Detalhar Valores do Acordo no Lançamento Gerado (Desconto, Acréscimo, Juros)** está desmarcado (valores do acordo salvos nos lançamentos origem) os valores do acordo (Desconto, Juros e Acréscimo) devem compor o item de baixa e o somatório da composição fechar com o valor baixado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1593359. |
| **Requisito:** | FINANCEIRO01-3619. |

divs
