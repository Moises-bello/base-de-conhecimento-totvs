---
content_hash: 7b79422726c455e00448a56de947de0dce7aab1c2f5e48ad72cbdddcbcc2e721
fetched_at: '2026-07-02T19:24:19.733799+00:00'
page_id: '244418609'
product: protheus
source: tdn-tec
title: Componente MSWorkTime deixando alterar mesmo desabilitado (3.1.8)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244418609
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

Componente MSWorkTime deixando alterar mesmo desabilitado

|  |  |
| --- | --- |
| Ocorrência | É possível alterar o componente MSWorkTime mesmo utilizando a propriedade lReadOnly como .T. e os métodos Disable() e SetDisable(.T.)  oMsWorkTime:lReadOnly := .T.  oMsWorkTime:Disable()  oMsWorkTime:SetDisable(.T.) |
| Correção | Corrigido o componente MSWorkTime para não permitir alteração quando estiver desabilitado. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-430 * Disponível a partir da build 7.00.131227A - 3.1.8 |
