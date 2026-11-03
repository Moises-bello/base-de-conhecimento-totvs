---
content_hash: 202803a5fa500a6d45a41f03c636abab5eaed3d7c32fe7df78e9694513b249d4
fetched_at: '2026-07-02T19:24:25.674772+00:00'
page_id: '499106593'
product: protheus
source: tdn-tec
title: EchoConsoleLog
type: documentation
url: https://tdn.totvs.com/display/tec/EchoConsoleLog
version: 2
---

EchoConsoleLog

# EchoConsoleLog

```
Define se as mensagens de log devem ser exibidas no console.
```

### Valores válidos

| Valores | Descrição |
| --- | --- |
| 0 | Mensagens não serão exibidas no console quando o  está ativo. |
| 1 (Padrão) | Mensagens serão exibidas no console quando o  está ativo. |

| Observação |
| --- |
| Esta chave pode ser utilizada quando o recurso de  estiver ativado no Application Server.  Para sabe sobre o . |

### Exemplo

```
[General]  
EchoConsoleLog=1
```
