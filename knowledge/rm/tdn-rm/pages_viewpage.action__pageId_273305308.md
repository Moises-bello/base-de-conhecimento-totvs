---
content_hash: c622192bd599061f541125edafa53d3669d87b4561b76f06bae66abe3e2858d9
fetched_at: '2026-06-29T00:08:31.682362+00:00'
page_id: '273305308'
product: rm
source: tdn-rm
title: CONTROLADORIA01-62 DT Máscara de Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273305308
version: 111
---

# Máscara de Centro de Custo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Máscara de Centro de Custo |
| **Situação/Requisito:** | Ao acessar os parâmetros do RM Saldus e trocar a máscara do centro de custo, o sistema não atualiza a nova máscara |
| **Solução/Implementação:** | Ajuste no DataServer que faz a atualização da tabela GCCUSTO para que caso o valor anterior da máscara seja diferente de vazio e a máscara atual seja preenchida o novo valor seja atualizado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
