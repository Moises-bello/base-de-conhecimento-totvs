---
content_hash: 048cbafde0bcf8f4d8cf804192e748c48f9320c684a4d73b06fd39436a647523
fetched_at: '2026-07-02T19:24:27.912125+00:00'
page_id: '695603309'
product: protheus
source: tdn-tec
title: LatencyPercent (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=695603309
version: 1
---

## LatencyPercent

Porcentagem de ciclos (dentro de LatencyHit) acima do LatencyWarning para que o usuário receba o aviso de problema devido a alta latência. Por exemplo, caso LatencyHit seja 100 e LatencyPercent seja 30, o Smartclient só vai avisar caso aconteça 30 (dentro de 100) pulsos acima do valor definido por LatencyWarning.  
Se não for informado, o valor padrão é 10.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
PingInterval=1000  
MaxPingCount=1000  
LatencyHit=60  
**LatencyPercent=10**
