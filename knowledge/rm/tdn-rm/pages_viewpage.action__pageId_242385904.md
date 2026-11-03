---
content_hash: 87d96d48a186263cfcf3bb0f9d3e14a41b30f2b7bc21cb36bbab515ef47c9e5a
fetched_at: '2026-06-29T00:08:11.221207+00:00'
page_id: '242385904'
product: rm
source: tdn-rm
title: TVAMG0_DT_Lançamento_Inclusão_Alteração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242385904
version: 111
---

# Lançamento - Inclusão/Alteração

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Lançamento - Inclusão/Alteração |
| **Situação/Requisito:** | Sistema não esta convertendo as partidas contabeis para real, quando o lançamento tem moeda diferente de real. Acontece  durante a contabilização de inclusão. |
| **Solução/Implementação:** | Ajustado a contabilidade de inclusão para passar o código da moeda do lançamento e a data de cotação. Dessa forma, o serviço de evento contábil converte o lançamento contábil para real de acordo com a cotação da data informada. |
| **Conversores e Parâmetros:** | NA. |
| **Chamados relacionados:** | NA. |
| **Requisito (ISSUE):** | FIN000022. |

divs
