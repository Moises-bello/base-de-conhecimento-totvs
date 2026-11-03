---
content_hash: 368c9d7d996ee029bf1641e7189974c56ba27442047db205751d8c6fadbc97ee
fetched_at: '2026-07-02T19:24:28.828494+00:00'
page_id: '859579838'
product: protheus
source: tdn-tec
title: Correção - Falha no carregamento do SmartView em Smartclient 32 bits
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859579838
version: 1
---

|  |  |
| --- | --- |
| Situação | Abrir qualquer rotina em Smartview com o Smartclient 32 bits entrava em loop e não carregava a tela |
| Ocorrência | Problema acontece devido a estouro da pilha e apenas em smartclient 32 bits porque a pilha tinha um tamanho menor disponível |
| Correção | Problema já tinha sido identificado no passado e solução foi aumentar o tamanho da pilha para o Smartclient 32 bits |
| Informações adicionais | * Referente ao chamado: [#20518825](https://totvssuporte.zendesk.com/agent/tickets/20518825 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4911 * Disponível em builds iguais ou superiores a 20.3.2.8 |
