---
content_hash: 95d79262fd7e7acca523371432d92dc49c1ed7fbd5b0d4e9da9c2f102b390372
fetched_at: '2026-07-02T19:24:23.212911+00:00'
page_id: '271185594'
product: protheus
source: tdn-tec
title: Leak de memória no uso de objetos JSON.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271185594
version: 1
---

Leak de memória em objetos JSON

|  |  |
| --- | --- |
| Situação | No uso de objetos do tipo J (JSON) a memória não era liberada após o uso. |
| Ocorrência |  |
| Correção | Correção na liberação de memória do objeto JSON |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227a - 2.3.6 |
