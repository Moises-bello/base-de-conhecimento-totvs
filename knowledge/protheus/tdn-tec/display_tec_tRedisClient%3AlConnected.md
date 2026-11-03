---
content_hash: 5d4e9205e8a88480774ec79e93b7d84bcd1d7912c248c9bfdec8c8a0ea8f786b
fetched_at: '2026-07-02T19:24:24.065642+00:00'
page_id: '454835777'
product: protheus
source: tdn-tec
title: tRedisClient:lConnected
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AlConnected
version: 10
---

Contém Verdadeiro (`.T.`) se o cliente está conectado a um servidor Redis, ou `.F.` caso contrário.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| lógico | N/A | Sim |

## Sintaxe

## Observações

* A propriedade `::lConnected()` é alterada pelo método `::Connect()`, que a torna verdadeira (`.T.`) caso tenha sido possível realizar uma conexão ao servidor; e `.F.` caso contrário.

* O método `::Disconnect()` altera a propriedade `::lConnected()` para `.F.`

## Veja também
