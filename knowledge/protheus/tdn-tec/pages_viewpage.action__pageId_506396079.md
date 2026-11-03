---
content_hash: 6fc04cbd7953f0e71b581350f1fc05d1fca3dafb5c2f937d6c263b8499461cfb
fetched_at: '2026-07-02T19:24:25.793759+00:00'
page_id: '506396079'
product: protheus
source: tdn-tec
title: Correção - TWebEngine não recebe foco diretamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506396079
version: 1
---

Consertada a política de foco do componente TWebEngine pra que assim que receba foco propague pra página web.

|  |  |
| --- | --- |
| Situação | Ao dar foco no componente TWebEngine não é possível digitar informações em campos da página HTML. |
| Ocorrência | Os campos de formulário da página HTML carregada pelo TWebEngine não recebem foco ao mesmo tempo que o componente recebe foco. |
| Correção | Corrigida a política de foco do componente pra propagar à página HTML. |
| Informações adicionais | * Referente à ocorrência: MTEC-3091 * Disponível em builds superiores a 17.3.0.10 |
