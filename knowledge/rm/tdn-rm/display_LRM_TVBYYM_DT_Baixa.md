---
content_hash: 6cde9b2e4889d2bb630c9e053b064bcb7cdd5485eebd0369b8f2da2acccbf737
fetched_at: '2026-06-29T00:08:10.736663+00:00'
page_id: '240979335'
product: rm
source: tdn-rm
title: TVBYYM_DT_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBYYM_DT_Baixa
version: 116
---

# BAIXA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Educacional* |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa |
| **Situação/Requisito:** | Ao baixar um lançamento na segunda moeda, cuja conta caixa é também na segunda moeda, o sistema não respeita a descrição da moeda no wizard de baixa. |
| **Solução/Implementação:** | Incluída a validação de moeda para aba de meio de pagamento da baixa de lançamentos. A moeda a ser apresentada é a moeda referente ao lookup de moeda do processo de baixa de lançamentos. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000040 |

divs
