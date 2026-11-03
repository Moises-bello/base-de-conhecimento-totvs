---
content_hash: 9b95a88623f7835a3821dc3395d79e2793cd2849a868effe7312eef955aa42e8
fetched_at: '2026-07-02T19:24:28.837241+00:00'
page_id: '860255205'
product: protheus
source: tdn-tec
title: AllowMethods
type: documentation
url: https://tdn.totvs.com/display/tec/AllowMethods
version: 6
---

## AllowMethods

Permite habilitar métodos Http específicos. Sem essa chave, por padrão, todos métodos ficam habilitados.

### Exemplo

Neste exemplo, os unicos metodos http habilitados são Get e Post, todos outros ficam desabilitados.

```
[HTTP]  
Enable=1  
Port=80  
AllowMethods=GET,OPTIONS
```
