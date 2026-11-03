---
content_hash: e08b434b47203f3bfd3091b3b69170e9b53bb5c486ba40913f6faea4a04bd4d0
fetched_at: '2026-07-02T19:24:28.839552+00:00'
page_id: '860255477'
product: protheus
source: tdn-tec
title: Seção [HTTPS], chave AllowMethods
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=860255477
version: 6
---

## AllowMethods

Permite habilitar métodos Http específicos. Sem essa chave, por padrão, todos métodos ficam habilitados.

### Exemplo

Neste exemplo, os unicos metodos http habilitados são Get e Post, todos outros ficam desabilitados.

```
[HTTPS]  
Enable=1  
Port=443  
AllowMethods=GET,OPTIONS
```
