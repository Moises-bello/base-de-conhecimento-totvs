---
content_hash: e0a6aa969792dd32a1f197f4db593608875d4d65148497d63696e41aaa3781f3
fetched_at: '2026-07-02T19:24:22.262150+00:00'
page_id: '269085663'
product: protheus
source: tdn-tec
title: COMPILADOR 4GL - Consistência do tipo WARNING para elementos de record não
  definidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085663
version: 1
---

Elemento RECORD não definido causa erro.

|  |  |
| --- | --- |
| Situação | Elemento RECORD não definido causa erro. |
| Ocorrência |  |
| Correção | Foi corrigido a consistência onde DEFINE <<var>> RECORD LIKE <<sch>>.\* onde posterior uso de <<var>>.<<coluna\_do\_sch>> possa ser corretamente consistida. |
| Informações adicionais | * Referente à ocorrência: TTEC-923 * Disponível em builds superiores a 7.00.131227a - 1.3.1 |
