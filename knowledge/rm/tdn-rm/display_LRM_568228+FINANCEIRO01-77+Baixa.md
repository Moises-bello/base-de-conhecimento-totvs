---
content_hash: c9efcae70dd26037d798cdefdd969413e06572acc9efeed04ff26182b047d82e
fetched_at: '2026-06-29T00:08:31.079335+00:00'
page_id: '272715964'
product: rm
source: tdn-rm
title: 568228 FINANCEIRO01-77 Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/568228+FINANCEIRO01-77+Baixa
version: 108
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa. |
| **Situação/Requisito:** | Ao realizar a baixa de vários lançamentos financeiros simultaneamente, se os mesmos estiverem inclusos em um Borderô, é exibido o erro:  "O processo de baixa foi concluído com ressalvas.  A baixa dos lançamentos [591655] foi concluída com sucesso.  Não foi possível concluir o processo de baixa para o(s) lançamento(s) [591656].  Violação de concorrência: DeleteCommand afetou 0 dos registros 1 esperados." |
| **Solução/Implementação:** | Melhoria no serviço de baixa para concluir o processo de baixa de lançamentos com borderô que possuem rateios quando o sistema estiver parametrizado para baixa one log (parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa” habilitado). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
