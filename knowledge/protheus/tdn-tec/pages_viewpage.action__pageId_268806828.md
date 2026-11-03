---
content_hash: 2661d610d71f97d4f51b360a67de636bfeeebda3de9f719b75c0442bb9eb31b9
fetched_at: '2026-07-02T19:24:21.624933+00:00'
page_id: '268806828'
product: protheus
source: tdn-tec
title: Correção no comportamento da função HTTPSPost.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268806828
version: 1
---

Comportamento indevido na função HTTPSPost no tratamento de post SSL.

|  |  |
| --- | --- |
| Situação | Correção no comportamento da função HTTPSPost |
| Ocorrência | A função não verificava o início da URL para identificar o post com SSL. |
| Correção | Correção no tratamento da URL para uso do post SSL |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - 1.0.7 |
