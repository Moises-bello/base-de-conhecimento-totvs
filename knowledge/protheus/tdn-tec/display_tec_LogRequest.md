---
content_hash: e183a5faa97ba99e3a11959df9427436ecf7e47ccf2718cddd040ffeecae3923
fetched_at: '2026-07-02T19:24:26.048426+00:00'
page_id: '520103542'
product: protheus
source: tdn-tec
title: LogRequest
type: documentation
url: https://tdn.totvs.com/display/tec/LogRequest
version: 4
---

BLOCK

LogRequest

## LogRequest

Habilita a escritas de todas as mensagens recebidas na porta http no arquivo console.log.

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
LogRequest=1
```
