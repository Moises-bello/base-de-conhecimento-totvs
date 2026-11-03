---
content_hash: c03021c8c6fadfd63b2ce07794c1558855d8ac69832a9a6901b4ade73d15b065
fetched_at: '2026-07-02T19:24:25.688040+00:00'
page_id: '502446065'
product: protheus
source: tdn-tec
title: Correção - GPF na utilização do RunInSession
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502446065
version: 2
---

|  |  |
| --- | --- |
| Situação | Utilizar RunInSession dentro da execução de outro RunInSession causava GPF e em algumas situações, deixava o processo "travado" no Gerenciador de tarefas consumindo CPU |
| Ocorrência | Problema acontecia pois não era previsto uma execução em cascata da função RunInSession |
| Correção | RunInSession agora trata corretamente os pedidos em cascata |
| Informações adicionais | * Referente ao chamado: 5764426 * Referente à ocorrência: MTEC-2649 * Disponível em builds iguais ou superiores a 7.00.131227A - 13.2.3.42 |
