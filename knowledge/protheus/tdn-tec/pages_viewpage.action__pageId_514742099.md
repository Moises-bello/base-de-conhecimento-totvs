---
content_hash: 3e1468f48abb1ac485495aeaaa07ef4a9403956b02960966c0241b19de1ca48a
fetched_at: '2026-07-02T19:24:25.919837+00:00'
page_id: '514742099'
product: protheus
source: tdn-tec
title: Implementação - Permitir criar uma thread ADVPL na mesma aba (workspace) que
  já existe uma thread 4GL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514742099
version: 1
---

|  |  |
| --- | --- |
| Situação | Necessidade de abrir uma tela ADVPL em cima de uma thread já executando um programa 4GL |
| Ocorrência | Nunca foi possível fazer isso pois a workspace (em ambiente 4GL) era criada dentro do smartclient, portanto não era possível reaproveitar a mesma workspace para criar outra tela ADVPL |
| Implementação | Agora é possível abrir uma tela ADVPL a partir de uma mesma aba 4GL, só precisa criar manualmente um TWorkspace e garantir que esse workspace vai ser passado como parâmetro na no createsession das duas threads. |
| Informações adicionais | * Referente à ocorrência: MTEC-2813 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.11 |
