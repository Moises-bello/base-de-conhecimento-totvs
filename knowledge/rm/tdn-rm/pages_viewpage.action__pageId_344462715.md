---
content_hash: c414180780e4d1ba37f9b66c84d8b9b140b349552d8abff3732a84a7d65971da
fetched_at: '2026-06-29T00:08:53.196402+00:00'
page_id: '344462715'
product: rm
source: tdn-rm
title: 859660 DEDUINTEGRACOES-1503 DT Erro na contabilização de inclusão ao regerar
  parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344462715
version: 92
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Regeração de lançamentos |
| **Situação/Requisito:** | Ao incluir uma bolsa de crédito e regerar uma parcela, cujo serviço seja contábil, e caso, o evento contábil possua uma fórmula que dependa do campo IDLANBOLSACREDITO da tabela SBOLSALAN, o resultado da contabilização pode ficar inconsistente, pois o valor do campo não era preenchido antes da contabilização ocorrer. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, permitindo que seja executada fórmula, que dependa do valor do campo IDLANBOLSACREDITO da tabela SBOLSALAN, para lançamentos contábeis durante a geração do lançamento financeiro. Como ocorre por exemplo, quando uma bolsa de crédito é adicionada a parcela e esta é regerada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
