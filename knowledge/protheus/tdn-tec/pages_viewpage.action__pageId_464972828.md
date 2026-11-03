---
content_hash: cbec411b3b653ae9de10bf28bc78a5cb1cac58ba266ef91443a2a3aea0f174d8
fetched_at: '2026-07-02T19:24:24.190619+00:00'
page_id: '464972828'
product: protheus
source: tdn-tec
title: Correção - Processa() não pode mais ser cancelada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464972828
version: 1
---

Resolvido o problema em que a função Processa() não podia mais ser cancelada pela interface.

|  |  |
| --- | --- |
| Situação | Processa() não pode mais ser cancelada |
| Ocorrência | Devido a alterações em outras versões do SmartClient, o botão "Cancelar" da função Processa() deixou de funcionar. |
| Correção | Foi retornado o comportamento anterior em que o botão funciona corretamente. |
| Informações adicionais | * Referente ao chamado: 5242386 * Referente à ocorrência: MTEC-2465 * Disponível em builds superiores a 13.2.3.39 |
