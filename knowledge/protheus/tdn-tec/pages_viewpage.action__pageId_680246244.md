---
content_hash: fdbe51db73e1985197d8c9588951bfc7010f5bf92cede09327addc7ad50d9b88
fetched_at: '2026-07-02T19:24:27.757083+00:00'
page_id: '680246244'
product: protheus
source: tdn-tec
title: Shortcut (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246244
version: 2
---

## Shortcut

Define se registra o atalho Control-Alt-N para abrir a tela do NetTest. Essa será a única maneira de abrir essa tela caso não seja identificado um problema de latência.  
Se não informado, o valor padrão é 1.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
PingInterval=1000  
MaxPingCount=1000  
ChartRange=100  
**Shortcut=1**
