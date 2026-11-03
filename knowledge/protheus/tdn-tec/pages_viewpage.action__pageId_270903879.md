---
content_hash: 5cbccea4604709bbf28406fea028a5544c8a8b4e897c450357c453c58fa0f824
fetched_at: '2026-07-02T19:24:22.539942+00:00'
page_id: '270903879'
product: protheus
source: tdn-tec
title: COMPILADOR 4GL - Compilação acusa erro de variável tipo Record não definida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270903879
version: 2
---

|  |  |
| --- | --- |
| Situação | COMPILADOR 4GL - Compilação acusa erro de variável tipo Record não definida. |
| Ocorrência | Na compilação de um fonte com duas funções distintas onde em cada uma havia a declaração de uma variável RECORD LIKE com mesmo nome, ocorria o erro de compilação "The symbol does not represent a defined variable". |
| Correção | Correção aplicada para consultar corretamente a integridade da variável. |
| Informações adicionais | * Referente à ocorrência: TTEC-1106 * Disponível a partir do build 7.00.131227a - 1.3.3 |
