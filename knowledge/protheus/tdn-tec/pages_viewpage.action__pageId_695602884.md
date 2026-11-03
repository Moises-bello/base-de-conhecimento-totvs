---
content_hash: 9714640603ca4298edc2f371c83c6dcb803239afc69924be3068c026f934dd6b
fetched_at: '2026-07-02T19:24:27.907042+00:00'
page_id: '695602884'
product: protheus
source: tdn-tec
title: LatencyHit (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=695602884
version: 1
---

## LatencyHit

Número de ciclos que deve ser analisado para considerar um problema de alta latência.  
Se não for informado, o valor padrão é 60.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
PingInterval=1000  
MaxPingCount=1000  
**LatencyHit=60**
