---
content_hash: 5d1d84e3c581479e0b778aa52328c76dcff3e6740fb5cab9fcac0e44c4873730
fetched_at: '2026-06-29T00:08:48.604968+00:00'
page_id: '327324627'
product: rm
source: tdn-rm
title: 1687564 EDUCACIONAL01-1191 DT Geração de lançamentos com valor duplicado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327324627
version: 93
---

# GERAÇÃO DE LANÇAMENTOS COM VALOR DUPLICADO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Sistema está gerando lançamentos com o valor duplicado quando se gera para um número grande de alunos  . |
| **Solução/Implementação:** | Ajuste no filtro de parcelas a serem consideradas por crédito acrescentando uma cláusula DISTINCT. Ajuste na quebra em pacotes na obtenção de parcelas e bolsas para que o sistema não considere registros de alunos que não foram selecionados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
