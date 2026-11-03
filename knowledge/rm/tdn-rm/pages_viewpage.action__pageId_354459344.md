---
content_hash: c8b2d993c0201501c0c4ae669e9a13a12a12e5232f82f31e3c1c5ef82f991a36
fetched_at: '2026-06-29T00:08:57.373539+00:00'
page_id: '354459344'
product: rm
source: tdn-rm
title: 1548336 RMSAU-3348 - Número da Guia de Solicitação duplicada no atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354459344
version: 1
---

# NÚMERO DA GUIA DE SOLICITAÇÃO E AUTORIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar. |
| **Função:** | Inserir guias em Atendimentos Externos previamente agendados. |
| **Situação/Requisito:** | Ao realizar um Registro de Atendimento Externo previamente agendado, as guias de solicitação e autorização são automaticamente geradas quando há integração com WebService.  Nestes casos, o número da guia gerado para a guia de solicitação era igual ao da autorização, o que corresponde ao funcionamento correto.  Porém, ao se inserir e autorizar uma guia por dentro do Registro de Atendimento Externo os números da guia de solicitação e autorização ficavam diferentes. |
| **Solução/Implementação:** | Realizado atualização do número da guia de solicitação após a autorização da mesma com o número retornado pelo WebService, deixando ambas as rotinas com o mesmo funcionamento. |
| **Requisito:** | RMSAU-3348 |
| **Tickets relacionados:** | [1548336](https://totvssuporte.zendesk.com/agent/tickets/1548336 "Open ticket in Zendesk Support") |
