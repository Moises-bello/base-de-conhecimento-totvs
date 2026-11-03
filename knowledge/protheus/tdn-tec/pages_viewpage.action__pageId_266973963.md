---
content_hash: 5c1991ece0f5b60e24fcb5e142a1c733a044445b615d639f1622f2f66526e9be
fetched_at: '2026-07-02T19:24:21.349623+00:00'
page_id: '266973963'
product: protheus
source: tdn-tec
title: Access Violation ao utilizar função TCSetField
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973963
version: 2
---

Access Violation ao utilizar função TCSetField

|  |  |
| --- | --- |
| Situação | Access Violation ao utilizar função TCSetField |
| Ocorrência | Ao utilizar a função TCSetField com um campo que está em um índice da tabela ocorria Access Violation |
| Correção | Reconstrução do índice quando um TCSetField com um field do índice for feito. |
| Informações adicionais | * Referente ao chamado: TVIOKQ * Referente à ocorrência: SSIM-1094 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
