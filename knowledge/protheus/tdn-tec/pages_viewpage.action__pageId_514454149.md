---
content_hash: 531b54f00f38bbea96ee747926baaeb19a1ef6876d60eb210116957f2cc5f894
fetched_at: '2026-07-02T19:24:25.901182+00:00'
page_id: '514454149'
product: protheus
source: tdn-tec
title: TWSDLManager erro para HTTP/1.1 302 Found
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514454149
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | TWSDLManager não redireciona para location retornado pelos erros 30x do http. |
| Correção | Inserido redirecionamento para que seja possível parsear WSDLs movidos. |
| Informações adicionais | * Referente ao chamado: MTEC-2472 * Disponível em builds iguais ou superiores a [13.1.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.45) e [13.2.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.45). |
