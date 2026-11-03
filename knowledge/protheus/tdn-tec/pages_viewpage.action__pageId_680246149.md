---
content_hash: b568397d7ab002dcdb045a0305439967e2d4d6a22e00f6c2c82e4c33bec25df5
fetched_at: '2026-07-02T19:24:27.749608+00:00'
page_id: '680246149'
product: protheus
source: tdn-tec
title: PingInterval (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680246149
version: 1
---

## PingInterval

Define o valor, em milissegundos, entre um ping e outro que o Smartclient deve disparar. O valor mínimo desse campo é 100, qualquer valor abaixo disso o Smartclient considera como 100.  
Se não for informado, o valor padrão é 1000.

### Exemplo

[NetTest]  
Enable=1  
Warning=1  
LatencyWarning=100  
**PingInterval=1000**
