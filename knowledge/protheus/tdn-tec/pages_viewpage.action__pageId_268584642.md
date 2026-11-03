---
content_hash: ad8695557fca3de212b8312af6c987928da0ccb90559ccee75627cd17c8a7324
fetched_at: '2026-07-02T19:24:21.556553+00:00'
page_id: '268584642'
product: protheus
source: tdn-tec
title: Correção de GPF na inicialização de thread na carga do CTREE Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268584642
version: 2
---

GPF na inicialização de thread na carga do CTREE Server

|  |  |
| --- | --- |
| Situação | Quando da inicialização da thread com o uso do CTREE Server a função GetUUID poderia causar uma exceção |
| Ocorrência |  |
| Correção | Correção na função GETUUID para prevenir a exceção. |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - 1.0.6 |
