---
content_hash: 48931162de4015c14fe5da44da3382921022532af3ade20844705c4397cbcd8a
fetched_at: '2026-07-02T19:24:22.232852+00:00'
page_id: '269084337'
product: protheus
source: tdn-tec
title: ShowFullLog
type: documentation
url: https://tdn.totvs.com/display/tec/ShowFullLog
version: 4
---

BLOCK

ShowFullLog

## ShowFullLog

```
Define se o conteúdo das variáveis serão exibidos no arquivo de log (error.log).
```

| Abrangência |
| --- |
| ERP 11 e 12 |

### Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Valores de variáveis não serão exibidos no log. |
| 1 | Valores de variáveis serão exibidos no log. Valor padrão. |

### Exemplo

```
[General]  
ShowFullLog=0
```
