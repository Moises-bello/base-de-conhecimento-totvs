---
content_hash: 648c67d7d37e0bdb4fd2414da49dae15b525b3c35e7b1cff1cce2adf92769104
fetched_at: '2026-07-02T19:24:28.822173+00:00'
page_id: '859579825'
product: protheus
source: tdn-tec
title: Correção - AutoUpdate no MacOS falhando
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859579825
version: 2
---

|  |  |
| --- | --- |
| Situação | Auto-Update do Smartclient no MacOS falha |
| Ocorrência | Ao configurar a chave update no appserver para atualizar o Smartclient MacOS, devido a um link simbólico no .app o update falhava |
| Correção | Corrigido para considerar corretamente o link simbólico e não falhar o update |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4635 * Disponível em builds iguais ou superiores a 20.3.2.9 |
