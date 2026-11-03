---
content_hash: 19938ea8cf539f036a3023e09ea3dc0ababc96ff2b84322f15889d50a36cd63b
fetched_at: '2026-06-29T00:08:56.509692+00:00'
page_id: '351377071'
product: rm
source: tdn-rm
title: 2502610 EDUCACIONAL01-4540 DT Devolucao Multa Evento Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/2502610+EDUCACIONAL01-4540+DT+Devolucao+Multa+Evento+Contabil
version: 85
---

# MOVIMENTAÇÕES - DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão bibliotecária |
| **Função:** | Movimentações - devolução |
| **Situação/Requisito:** | Foi identificado uma inconsistência ao devolver um empréstimo que está em atraso e que irá gerar multa, o sistema emite uma mensagem não tratada e não conclui a operação. |
| **Solução/Implementação:** | Foi identificado que a inconsistência era causada pelos parâmetros de Evento Contábil, os parâmetros definidos no Biblios não existiam mais no cadastro do contabilidade, sendo assim foi incluída uma validação no momento da geração do lançamento para verificar a consistência destes parâmetros e permitir ou não a operação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
