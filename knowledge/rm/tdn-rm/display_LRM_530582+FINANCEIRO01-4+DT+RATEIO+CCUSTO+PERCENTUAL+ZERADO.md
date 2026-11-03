---
content_hash: 7eff40c9803158a715d5483a0a8bce22a5d38824dd29827ecb0fdc670fce6b7e
fetched_at: '2026-06-29T00:08:30.975526+00:00'
page_id: '272709507'
product: rm
source: tdn-rm
title: 530582 FINANCEIRO01-4 DT RATEIO CCUSTO PERCENTUAL ZERADO
type: documentation
url: https://tdn.totvs.com/display/LRM/530582+FINANCEIRO01-4+DT+RATEIO+CCUSTO+PERCENTUAL+ZERADO
version: 109
---

# Rateio por centro de custo com percentual zerado.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Contabilização de Baixa |
| **Situação/Requisito:** | Ao realizar a contabilização de um lançamento que possui 607 rateios alguns valores do rateio não estão sendo carregados e o sistema apresenta mensagem de erro dizendo que não carregou valor para o centro de custo x. |
| **Solução/Implementação:** | Ajustado o sistema para recalcular o percentual do rateio caso o mesmo tenha sido salvo na base com valor 0. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
