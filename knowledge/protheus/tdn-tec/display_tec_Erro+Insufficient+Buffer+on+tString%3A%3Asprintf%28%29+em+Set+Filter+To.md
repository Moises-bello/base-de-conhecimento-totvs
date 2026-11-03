---
content_hash: 87f1046bcf4438524022bf5d4cb588b21127cd9d3c36882296b917e808dc281d
fetched_at: '2026-07-02T19:24:21.576376+00:00'
page_id: '268591822'
product: protheus
source: tdn-tec
title: Erro Insufficient Buffer on tString::sprintf() em Set Filter To
type: documentation
url: https://tdn.totvs.com/display/tec/Erro+Insufficient+Buffer+on+tString%3A%3Asprintf%28%29+em+Set+Filter+To
version: 2
---

Erro Insufficient Buffer on tString::sprintf() em Set Filter To

|  |  |
| --- | --- |
| Situação | Erro Insufficient Buffer on tString::sprintf() em Set Filter To |
| Ocorrência | Ao utilizar um filtro muito grande com um erro, mesmo que esse erro fosse tratado posteriormente o erro acima era exibido. O erro ocorria por não ser possível imprimir o filtro na mensagem de erro. |
| Correção | Alteração de como a mensagem de erro é montada. |
| Informações adicionais | * Referente ao chamado: SSIM-1269 * Referente à ocorrência: TTEC-947 * Disponível em builds superiores a 7.00.131227a - 1.3.1 |
