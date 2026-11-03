---
content_hash: b3dccacbb76c79990bb4d2d564ddca15bd6b8e113f49632541b1cf226a67fda5
fetched_at: '2026-07-02T19:24:27.746918+00:00'
page_id: '680246105'
product: protheus
source: tdn-tec
title: LatencyWarning (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246105
version: 2
---

## LatencyWarning

Define o valor, em milissegundos, que deve ser considerado como latência alta, um valor de ping acima desse valor gera um aviso no Smartclient.  
Se não for informado, o valor padrão é 100.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
**LatencyWarning=100**
