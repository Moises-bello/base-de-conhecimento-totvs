---
content_hash: 18584be72d8a328e6e297475ff5069806dae053e4b203844f5f205b04baa1aab
fetched_at: '2026-07-02T19:24:27.751955+00:00'
page_id: '680246192'
product: protheus
source: tdn-tec
title: MaxPingCount (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246192
version: 1
---

## MaxPingCount

Define o número máximo de amostras de ping que o Smartclient deve manter em memória.  
Se não for informado, o valor padrão é 1000.

Com os valores no padrão isso gasta 0,15mb (em memória RAM) e salva os últimos 16 minutos com 1 ping por segundo.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
PingInterval=1000  
**MaxPingCount=1000**
