---
content_hash: 722aac51689ca787e77bd904417da899e396c8d6dabe9961ce4ca1bff5710262
fetched_at: '2026-07-02T19:24:28.697353+00:00'
page_id: '808480442'
product: protheus
source: tdn-tec
title: Correção - Impressão de relatório em SmartView
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808480442
version: 1
---

|  |  |
| --- | --- |
| Situação | Tentar imprimir um relatório ou exportar em SmartView não funciona |
| Ocorrência | Problema começou a ocorrer na nova versão (20.3.2.0) devido a mudança do componente de renderização HTML/JS |
| Correção | Correção efetuada para abrir uma janela do próprio Smartclient (não mais do browser) e permitir carregar a impressão e exportar os outros tipos de arquivos |
| Informações adicionais | * Referente ao chamado: [Ticket #18597530](https://totvssuporte.zendesk.com/agent/tickets/18597530 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4443 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.2.2 |
