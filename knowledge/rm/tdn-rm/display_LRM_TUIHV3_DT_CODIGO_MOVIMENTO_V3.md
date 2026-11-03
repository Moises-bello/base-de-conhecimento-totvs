---
content_hash: da2054388053facf0ee23e2843c05b584b4cbc066072bf6eba7576700bd2f09b
fetched_at: '2026-06-29T00:08:20.600798+00:00'
page_id: '268578806'
product: rm
source: tdn-rm
title: TUIHV3_DT_CODIGO_MOVIMENTO_V3
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIHV3_DT_CODIGO_MOVIMENTO_V3
version: 114
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Emissão campo Código do Movimento Registro 32.* |
| **Situação/Requisito:** | *No registro 32 do SEFIP campo Código do Movimento deve ter o valor V3 para funcionário comissionista com movimento após ao término de contrato. Neste caso a data de movimentação deverá corresponder ao último dia do vínculo.* |
| **Solução/Implementação:** | No Registro 32 do SEFIP campo Código do Movimento o sistema passa a levar V3 para funcionário Comissionista tipo "O" em que a competência do SEFIP seja posterior a data de demissão. A data do Movimento passa a ser a data do desligamento. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUIHV3 |
| **Requisito (ISSUE):** |  |

divs
