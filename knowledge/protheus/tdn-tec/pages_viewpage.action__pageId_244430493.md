---
content_hash: f7f589f611b09b1f58dcf0bd4d45b582797980dedf9173f5384121d8d2b04057
fetched_at: '2026-07-02T19:24:19.802167+00:00'
page_id: '244430493'
product: protheus
source: tdn-tec
title: Melhoria na propriedade cTooltip dos componentes para aceitar tags HTML (3.1.8)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244430493
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

Melhoria na propriedade cTooltip dos componentes para aceitar tags HTML

|  |  |
| --- | --- |
| Ocorrência | Ao utilizar a propriedade cTooltip informando tags HTML, o texto apresentado não ficava formatado.  Exemplo:  oButton1:cToolTip := "Tooltip oButton1 <i>Italic</i>"  É apresentado o texto conforme o informado e não substituindo a tag <i> |
| Melhoria | Alteração na propriedade tooltip de todos os componentes para aceitar tags HTML. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-401 * Disponível a partir da build 7.00.131227A - 3.1.8 |
