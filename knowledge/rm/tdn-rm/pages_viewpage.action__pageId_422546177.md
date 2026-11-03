---
content_hash: 830bfa4d7e66358bcbef2c4679d27edbe0506017376b902dac7e3a367a775e35
fetched_at: '2026-06-29T00:09:23.962028+00:00'
page_id: '422546177'
product: rm
source: tdn-rm
title: Registro C197 e D197 (Código de Ajuste Distintos DIFAL e FECP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546177
version: 6
---

Para a correta geração deste registro deverão ser criados dois campos complementares no item do Lançamento Fiscal com as características abaixo. Estes campos podem ser criados no lançamento. A informação deverá constar somente no item ou somente no lançamento ou será duplicada na geração da rotina:

| Nome da Coluna | Descrição | Tamanho | Tipo | Texto |
| --- | --- | --- | --- | --- |
| CODAJUSTESPEDFECP | Código Ajuste FECP | 10 | Alfanumérico | Texto |
| CODAJUSTESPED | Código de Ajuste SPED | 10 | Alfanumérico | Texto |

***Observação***: Caso o lançamento fiscal seja proveniente do TOTVS Gestão de Estoque, Compras e Faturamento, os campos complementares acima também deverão ser criados no movimento / item do Tipo de Movimento.
