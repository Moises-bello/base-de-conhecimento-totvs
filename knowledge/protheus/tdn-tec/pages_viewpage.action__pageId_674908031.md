---
content_hash: 0dbcb0ec78342e0b221639d3fdce6fdb5a038c91a52c2a75bfcce3baaf5516fc
fetched_at: '2026-07-02T19:24:27.686428+00:00'
page_id: '674908031'
product: protheus
source: tdn-tec
title: Correção - Acento é substituído por ponto de interrogação em rotinas 4GL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=674908031
version: 1
---

Correção realizada no componente de entrada para que caracteres acentuados apareçam normalmente.

|  |  |
| --- | --- |
| Situação | Em campos de entrada nas rotinas 4GL quando é digitado um caractere acentuado, aparece um ponto de interrogação no lugar. |
| Ocorrência | Havia uma falha no tratamento de encoding nas rotinas 4GL. |
| Correção | A conversão de encoding foi corrigida. |
| Informações adicionais | * Referente ao chamado: #LOGIX-54 * Referente à ocorrência: DTCLIENT01-3277 * Disponível em builds superiores a 20.3.0.3 |
