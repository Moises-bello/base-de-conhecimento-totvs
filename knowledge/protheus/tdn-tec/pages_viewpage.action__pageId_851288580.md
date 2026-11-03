---
content_hash: ad49c209b9bbb3e21327e45bc182c319b3381d57e05bf785728cec4a6828158f
fetched_at: '2026-07-02T19:24:28.764910+00:00'
page_id: '851288580'
product: protheus
source: tdn-tec
title: Correção - Função PrintPDF com layout incorreto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=851288580
version: 2
---

|  |  |
| --- | --- |
| Situação | Ao usar a função PrintPDF, o tamanho de cada página é diferente de A4 |
| Ocorrência | A função PrintPDF estava com valor padrão incorreto de tamanho de página, o que causava problemas de posicionamento do conteúdo de uma impressão |
| Correção | O Framework de impressão usava dados em polegadas, o que causou a distorção de comportamento. Foi feito o ajuste, passando as medidas corretas de filha A4 |
| Informações adicionais | * Referente ao chamado: [20081838](https://totvssuporte.zendesk.com/agent/tickets/20081838 "View ticket on the Zendesk portal") * Referente à ocorrência: [DTCLIENT01-4765](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-4765) * Disponível em builds superiores a 20.3.2.8 |
