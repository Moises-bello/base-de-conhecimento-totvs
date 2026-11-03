---
content_hash: 40ea44cf6af97327a7c9d93129ac776bff2700485d5968d6814ef91cb68dedfb
fetched_at: '2026-06-29T00:08:50.952952+00:00'
page_id: '334350300'
product: rm
source: tdn-rm
title: 1721540 EDUCACIONAL01-3244 DT Renovação de exemplares no dia da devolução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334350300
version: 93
---

# RENOVAÇÃO DE EXEMPLARES NO DIA DA DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão bibliotecária |
| **Função:** | Renovação de exemplares |
| **Situação/Requisito:** | Ao realizar uma renovação de um exemplar com restrição de renovação fora do dia de devolução, o sistema apresenta uma mensagem de restrição informando que a operação não é possível porque ela está sendo realizada fora da data de devolução. |
| **Solução/Implementação:** | Foi identificado que quando há uma alteração na data de devolução, o sistema não considera a data original da devolução e impede a operação da renovação.  O sistema foi alterado para que a validação seja realizada baseada na data original de devolução. Dessa forma, não haverá bloqueio, caso a data seja alterada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
