---
content_hash: 54ae57adfedfb5d27fb1b31ee7a182536b6fa2179e1c1923c58ca08740b30578
fetched_at: '2026-06-29T00:10:25.176263+00:00'
page_id: '502439764'
product: rm
source: tdn-rm
title: Documento Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502439764
version: 1
---

## Configuração NginX

Documentação oficial em <https://nginx.org/en/docs/>

nginx.conf

* server
  + proxy\_Connect\_Timeout
    - tempo de espera do nginx para obter o handshake de um host, caso não retorne, procura outro host
  + proxy\_Timeout
    - tempo de espera do nginx para retornar a requisição pro client
* upstream
  + max\_fails
    - quantidade de falhas do servidor durante um determinado tempo (fail\_timeout) para que ele seja considerado indisponível
  + fail\_timeout
    - quantidade de tempo que o servidor será considerado indisponível
    - quantidade de tempo que o servidor poderá falhar por determinadas vezes (max\_fails), para ser considerado indisponível
