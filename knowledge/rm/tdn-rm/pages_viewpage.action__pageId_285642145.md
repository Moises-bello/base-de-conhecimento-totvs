---
content_hash: 77ec777db94889b5ab9c0b5ee0a600e1fdb0aae9ced7ef8913732f202b9c1d87
fetched_at: '2026-06-29T00:08:38.234459+00:00'
page_id: '285642145'
product: rm
source: tdn-rm
title: EDUCACIONAL01-1610 DT Desfazer inclusão de bolsa retroativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285642145
version: 101
---

# DESFAZER INCLUSÃO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Desfazer inclusão de bolsa retroativa |
| **Situação/Requisito:** | Sistema não consegue desfazer a inclusão de bolsa quando são incluídas mais de uma bolsa e os vínculos são feitos somente para uma parcela. Isso ocorre porque, o serviço de exclusão de vínculos  de lançamentos está excluindo todas as rastreabilidades de bolsas retroativas por lançamento  fazendo com que, ao processar a segunda bolsa, o vínculo não seja desfeito e, ao cancelar o lançamento  de crédito, é emitida a mensagem de que o lançamento está vinculado. |
| **Solução/Implementação:** | Ajuste na rotina de exclusão de vínculos do financeiro a fim de informar o lançamento de crédito (IdLanRel) a ser considerado.  Ajuste na rotina de cancelamento de aproveitamento de crédito retroativo no Educacional para excluir somente os lançamentos participantes do vínculo que está sendo desfeito. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
