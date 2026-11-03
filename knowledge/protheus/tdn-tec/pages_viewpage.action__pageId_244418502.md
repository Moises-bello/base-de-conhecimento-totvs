---
content_hash: f441f95d68a26e9584f4cc07d0ff14586959990fe3799c1c91e8e3d83afa00a9
fetched_at: '2026-07-02T19:24:19.730687+00:00'
page_id: '244418502'
product: protheus
source: tdn-tec
title: Componente MSWorkTime deixando alterar mesmo desabilitado (2.3.4)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244418502
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

Componente MSWorkTime deixando alterar mesmo desabilitado

|  |  |
| --- | --- |
| Ocorrência | É possível alterar o componente MSWorkTime mesmo utilizando a propriedade lReadOnly como .T. e os métodos Disable() e SetDisable(.T.)  oMsWorkTime:lReadOnly := .T.  oMsWorkTime:Disable()  oMsWorkTime:SetDisable(.T.) |
| Correção | Corrigido o componente MSWorkTime para não permitir alteração quando estiver desabilitado. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-430 * Disponível a partir da build 7.00.131227A - 2.3.4 |
