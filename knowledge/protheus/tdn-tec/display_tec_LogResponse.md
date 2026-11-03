---
content_hash: 164aeddbb9344a4e0b890967d78208830505c9623bb93cb1b50edd93978f9327
fetched_at: '2026-07-02T19:24:26.051641+00:00'
page_id: '520103564'
product: protheus
source: tdn-tec
title: LogResponse
type: documentation
url: https://tdn.totvs.com/display/tec/LogResponse
version: 2
---

BLOCK

LogResponse

## LogResponse

```

```

Habilita a escritas de todas as mensagens enviadas pelo AppServer na porta http no arquivo console.log.

### Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (padrão) | Desabilita |
| 1 | Habilita |

### Exemplo

```
[HTTP]  
Enable=1  
Port=80  
Path=D:\ERP\Html  
LogResponse=1
```
