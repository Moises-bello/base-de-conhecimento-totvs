---
content_hash: 087563d7e4535ed31897b23f17178cd66c8ac0fb40c1e786a203e1a39b7d0d6e
fetched_at: '2026-07-02T19:24:25.808200+00:00'
page_id: '507015488'
product: protheus
source: tdn-tec
title: HTTPGET não identificando modo de transmissão chunked
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507015488
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Falha na detecção de método de envio Chunked quando mais de um transfer-encoding é enviado. |
| Correção | Corrigido para que seja suportado mais de um transfer-encoding nas requisições. |
| Informações adicionais | * Referente ao chamado: MTEC-3116 * Disponível em builds iguais ou superiores a [13.1.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.45) e [13.2.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.45). |
