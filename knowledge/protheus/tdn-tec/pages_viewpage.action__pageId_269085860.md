---
content_hash: 656e67e5d9b1ad52a4254a8cab0d422731a25932027648c4081277e4ea8b9436
fetched_at: '2026-07-02T19:24:22.287136+00:00'
page_id: '269085860'
product: protheus
source: tdn-tec
title: Erro Insufficient Buffer on tString::sprintf() em Set Filter To.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085860
version: 1
---

Erro Insufficient Buffer on tString::sprintf() em Set Filter To

|  |  |
| --- | --- |
| Situação | Erro Insufficient Buffer on tString::sprintf() em Set Filter To |
| Ocorrência | Ao utilizar um filtro muito grande com um erro, mesmo que esse erro fosse tratado posteriormente o erro acima era exibido. O erro ocorria por não ser possível imprimir o filtro na mensagem de erro. |
| Correção | Alteração de como a mensagem de erro é montada. |
| Informações adicionais | * Referente ao chamado: SSIM-1269 * Referente à ocorrência: TTEC-947 * Disponível em builds superiores a 7.00.131227a - 2.3.1 |
