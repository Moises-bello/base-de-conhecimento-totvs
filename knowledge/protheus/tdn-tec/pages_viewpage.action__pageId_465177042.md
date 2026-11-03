---
content_hash: 91d73e9de629a7ffdf5a9dbf528a62056e5fb1d951d7c87b8a780a7bf4d82414
fetched_at: '2026-07-02T19:24:24.196943+00:00'
page_id: '465177042'
product: protheus
source: tdn-tec
title: Correção - TDialog mostra botão de fechar mesmo quando DS_MODALFRAME definido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465177042
version: 1
---

Correção efetuada pra que a TDialog não tenha botão de fechar quando definido pra não ter (DS\_MODALFRAME).

|  |  |
| --- | --- |
| Situação | TDialog mostra botão de fechar |
| Ocorrência | Na versão Lobo-Guará, as TDialog definidas com a propriedade DS\_MODALFRAME acabam com um botão de fechar, ao contrário do previsto com a propriedade. |
| Correção | Corrigido o comportamento pra se adequar ao software |
| Informações adicionais | * Referente ao chamado: 5103920 * Referente à ocorrência: MTEC-2435 * Disponível em builds superiores a 17.3.0.7 |
