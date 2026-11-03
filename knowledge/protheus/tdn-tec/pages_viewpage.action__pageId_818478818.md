---
content_hash: f7b625df3a72f1f9cf8bfaa4f7fbc6765bac5ea27300bd5c2bd02525743e2cdd
fetched_at: '2026-07-02T19:24:28.720600+00:00'
page_id: '818478818'
product: protheus
source: tdn-tec
title: Correção - TWebEngine com HTML drag-and-drop parou de funcionar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=818478818
version: 2
---

Ao tentar fazer um drag and drop em um componente HTML com esse recurso, usando o TWebEngine, nada acontecia.

|  |  |
| --- | --- |
| Situação | Drag and Drop nao funciona no componente TWebEngine |
| Ocorrência | O problema acontecia pois após a troca do motor para o CEF, este não tinha a implementação de Drag and Drop de forma nativa. |
| Correção | Implementado a funcionalidade de Drag and Drop. |
| Informações adicionais | * Referente ao chamado: 18513008 * Referente à ocorrência: DTCLIENT01-4424 * Disponível em builds superiores a 20.3.2.4 |
