---
content_hash: fd20de66aad2e26417b39bc0874c6fcbe1babe91bb670dd79e25c4fb845fb2ce
fetched_at: '2026-07-02T19:24:28.772087+00:00'
page_id: '853924632'
product: protheus
source: tdn-tec
title: Correção - Geração de PDF com senha no linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853924632
version: 1
---

|  |  |
| --- | --- |
| Situação | Gerar PDF com senha no linux acusa erro na execução |
| Ocorrência | Chamar a printer/pdfprinter passando o parametro de senha, acusa erro, obrigando o uso do OwnerPassword (não deveria ser obrigatório) |
| Correção | Alteração feita para não ser mais obrigatório o OwnerPassword, aceitando apenas a senha |
| Informações adicionais | * Referente ao chamado: [#19535232](https://totvssuporte.zendesk.com/agent/tickets/19535232 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4660 * Disponível em builds iguais ou superiores a 2.2.4 |
