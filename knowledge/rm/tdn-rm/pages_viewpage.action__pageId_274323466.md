---
content_hash: 7943300194ff633fb1708e8b675502e9aa309726e05535d15645fae5bc875567
fetched_at: '2026-06-29T00:08:33.496918+00:00'
page_id: '274323466'
product: rm
source: tdn-rm
title: 722404 CONTROLADORIA01-48 DT Alteração Múltiplos Patrimônios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274323466
version: 104
---

# Alteração de Múltiplos Patrimônios

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Alteração de múltiplos patrimônios |
| **Situação/Requisito:** | Ao realizar o processo de Alteração de múltiplos patrimônios é enviada uma mensagem informando que o número máximo de expressões em uma lista e de 1000. |
| **Solução/Implementação:** | O processo de alteração de múltiplos patrimônios não estava preparado para modificar mais de 1000 registros em bases Oracle. Ele foi alterado para que sejam executados blocos de, no máximo, 900 patrimônios por vez. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
