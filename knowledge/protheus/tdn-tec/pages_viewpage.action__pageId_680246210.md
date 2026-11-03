---
content_hash: 004de72690c4ec18f048e827b3f4203fbe257cba381c83249b4310ab2c39fd81
fetched_at: '2026-07-02T19:24:27.754653+00:00'
page_id: '680246210'
product: protheus
source: tdn-tec
title: ChartRange (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246210
version: 1
---

## ChartRange

Define o número máximo de amostras que devem ser plotadas no gráfico.  
Se não for informado, o valor padrão é 100.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
PingInterval=1000  
MaxPingCount=1000  
**ChartRange=100**
