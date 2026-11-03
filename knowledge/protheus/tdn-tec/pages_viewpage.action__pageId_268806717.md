---
content_hash: 79714bd23272980826af659ddb8d9c8b003fcb27a3666fd5d32573b85eabc78d
fetched_at: '2026-07-02T19:24:21.622144+00:00'
page_id: '268806717'
product: protheus
source: tdn-tec
title: Correção no comportamento da função HTTPSPost
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268806717
version: 1
---

```
Comportamento indevido na função HTTPSPost no tratamento de post SSL.
```

|  |  |
| --- | --- |
| Situação | Correção no comportamento da função HTTPSPost |
| Ocorrência | A função não verificava o início da URL para identificar o post com SSL. |
| Correção | Correção no tratamento da URL para uso do post SSL |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - NG 2.0.7 |
