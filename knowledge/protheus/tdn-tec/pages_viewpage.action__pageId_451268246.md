---
content_hash: 61f84ac2f5f0cc1397f96c8a689605a297c95fc91c39263e7d18af7e85f24ca9
fetched_at: '2026-07-02T19:24:23.947509+00:00'
page_id: '451268246'
product: protheus
source: tdn-tec
title: Unable to receive data. Error syscall/ssl
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451268246
version: 2
---

|  |  |
| --- | --- |
| Ocorrência | Sistema apresentando erro para comunicação SOAP "Unable to receive data. Error syscall/ssl" |
| Correção | Alterado rotinas SSL para que em caso de falha seja retentado comunicação antes de retornar erro |
| Informações adicionais | * Referente ao chamado: MTEC-2086 * Disponível em builds iguais ou superiores a [13.1.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.41) e [13.2.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.41). |
