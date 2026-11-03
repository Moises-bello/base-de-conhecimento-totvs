---
content_hash: 3703ae693a702797cf40ce15a13b2f271ad109b628730e3787eb68f39e46723d
fetched_at: '2026-06-29T00:09:19.422832+00:00'
page_id: '421389129'
product: rm
source: tdn-rm
title: DSAUGHFATF-2585 - Layout do arquivo AIH gerado está errado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421389129
version: 1
---

# Layout do arquivo AIH gerado está errado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Função:** | Faturamento de AIH |
| **Situação/Requisito:** | O sistema estava apresentando erro na geração do arquivo quando era realizado o faturamento de um lote com mais de 1000 AIHs |
| **Solução/Implementação:** | Quando o lote de AIHs tiver mais de 1000 itens, o arquivo gerado será dividido em 2 para não comprometer o layout esperado pelo SISAIH01 |
| **Tickets relacionados:** | <https://totvssuporte.zendesk.com/agent/tickets/3994356> |
