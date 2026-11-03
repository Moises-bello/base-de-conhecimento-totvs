---
content_hash: d39e34ef832ec52dcd067eb205745208f80f6db5d409db82394104b507ba3342
fetched_at: '2026-06-28T21:35:24.568306+00:00'
page_id: '270921008'
product: fluig
source: tdn-fluig
title: Tratamento de exceções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270921008
version: 5
---

As exceções podem ser tratadas nos seguintes eventos: *beforeStateEntry, beforeTaskSave* e *beforeCancelProcess*. O tratamento de exceção no evento *beforeStateEntry* pode ser utilizado na inicialização de solicitações, pois ele impede que a solicitação seja iniciada. Em contrapartida o tratamento de exceção no evento *beforeTaskSave* pode ser utilizado somente se a solicitação já estiver inicializada.

Abaixo é apresentado os modelos para utilização em cada um dos eventos:

jstrue

É possível consultar o campo Observação de uma solicitação de processo, verificando se ele foi preenchido ou não. Para isto, é necessário validar a propriedade *WKUserComment* no evento *beforeTaskSave* ou no evento *beforeCancelProcess*.

**Exemplo:**

jstrue
