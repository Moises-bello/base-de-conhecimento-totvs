---
content_hash: ec1c1156113fbf44a4b4740d512c767b7339950847a6f5609fb32d00f220d784
fetched_at: '2026-07-02T19:24:24.866282+00:00'
page_id: '490638306'
product: protheus
source: tdn-tec
title: WsdlParser Exception Error parsing schema types com WSDL do Serasa
type: documentation
url: https://tdn.totvs.com/display/tec/WsdlParser+Exception+Error+parsing+schema+types+com+WSDL+do+Serasa
version: 3
---

|  |  |
| --- | --- |
| Ocorrência | WsdlParser Exception ao tentar fazer parser do WSDL do Serasa |
| Correção | Inserido proteção schemas já parseados não sejam parseados novamente o que gerava recursão infinita. |
| Informações adicionais | * Referente ao chamado: MTEC-2498 * Disponível em builds iguais ou superiores a [13.1.3.43](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.43) e [13.2.3.43](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.43). |
