---
content_hash: 133d028268c7341b49f1a2234da941f307b71dc3c687653b32555556314f80d9
fetched_at: '2026-06-29T00:09:08.249414+00:00'
page_id: '385860256'
product: rm
source: tdn-rm
title: 3215564 DEDUINTEGRACOES-2981 DT Retorno da baixa na integração financeira TOTVS
  x Pergamum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385860256
version: 82
---

# RETORNO DA BAIXA NA INTEGRAÇÃO FINANCEIRA TOTVS X PERGAMUM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Integração com o Pergamum* |
| **Situação/Requisito:** | Ao tentar baixar um título no Pergamum, o sistema retorna a mensagem de erro abaixo:  “Procedure or function 'sp\_per\_baixa\_automatica\_deb' expects parameter '@cod\_empresa', which was not supplied.”. |
| **Solução/Implementação:** | Alterações dos nomes de parâmetros a serem passados para a procedure sp\_per\_baixa\_automatica\_deb a fim de notificar o pergamum da baixa de lançamentos |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
