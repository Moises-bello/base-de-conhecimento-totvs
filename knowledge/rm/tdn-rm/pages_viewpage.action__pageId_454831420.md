---
content_hash: 827efeab886302fd8f0e4c896181b2cafffe3c9787921e45c93fc74855b42b66
fetched_at: '2026-06-29T00:10:12.625332+00:00'
page_id: '454831420'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-611 DT Geração de parcela com mais de um responsável financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454831420
version: 75
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos financeiros |
| **Situação/Requisito:** | Ao gerar lançamentos para uma parcela que possua mais de um responsável financeiro, sendo pelo pelo menos um deles do tipo "Fornecedor", o sistema gerava lançamentos para os responsáveis do tipo "Ambos" e "Cliente" e não gerava para os do tipo "Fornecedor", ficando assim, a soma do valor das lançamentos gerados, abaixo do valor da parcela, devido a falta dos lançamentos que deram erro. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que, ao gerar lançamentos para uma parcela, caso a lista de responsáveis financeiros, possua pelo menos um responsável do tipo "Fornecedor", o sistema deixará de gerar todos os lançamentos da parcela em questão, reportando erro ao usuário.    . |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
