---
content_hash: 423f0aeeb9b35a32588630e320ed59b4d0248716dcfcc91ae7a6b4074f3b5bde
fetched_at: '2026-07-02T19:24:19.799196+00:00'
page_id: '244430486'
product: protheus
source: tdn-tec
title: Melhoria na propriedade cTooltip dos componentes para aceitar tags HTML (2.3.4)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244430486
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

Melhoria na propriedade cTooltip dos componentes para aceitar tags HTML

|  |  |
| --- | --- |
| Ocorrência | Ao utilizar a propriedade cTooltip informando tags HTML, o texto apresentado não ficava formatado.  Exemplo:  oButton1:cToolTip := "Tooltip oButton1 <i>Italic</i>"  É apresentado o texto conforme o informado e não substituindo a tag <i> |
| Melhoria | Alteração na propriedade tooltip de todos os componentes para aceitar tags HTML. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-401 * Disponível a partir da build 7.00.131227A - 2.3.4 |
