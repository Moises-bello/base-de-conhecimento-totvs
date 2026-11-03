---
content_hash: 78a08d24ab486b7c75269256c837224b95fc57dd0403d30534ac0f30a8c20ccc
fetched_at: '2026-06-29T00:08:56.580571+00:00'
page_id: '351383188'
product: rm
source: tdn-rm
title: Stop
type: documentation
url: https://tdn.totvs.com/display/LRM/Stop
version: 1
---

Esta operação força a parada do JobServer informado nos parâmetros **jobServer** e **alias**.

**Endpoint**: [http://host:port/RMSJobServerApi/stop/{jobServer}/{alias}](http://hostport)

Exemplo:

<http://localhost:8051/RMSJobServerApi/stop/server1:1219/local>

retorno:

**http 200**
