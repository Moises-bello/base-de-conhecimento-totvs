---
content_hash: 7baece870ff96bcde0f8af518ebc78d327504b42c11b39cab6f990364a039289
fetched_at: '2026-07-02T19:24:27.664526+00:00'
page_id: '666820292'
product: protheus
source: tdn-tec
title: Melhoria - Parâmetros -USEGPU e -FORCEGPU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=666820292
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Alto consumo de CPU em renderização de páginas HTML/JS dentro do QtWebEngine. |
| Correção | Adicionado -USEGPU para ligar renderização via Hardware e -FORCEGPU para forçar o uso de renderização mesmo se GPU estiver na blocklist do Chromium. |
| Informações adicionais | * Referente ao chamado: DTCLIENT01-3169 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.0.2 |
