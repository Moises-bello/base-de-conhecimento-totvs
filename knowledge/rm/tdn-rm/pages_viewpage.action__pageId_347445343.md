---
content_hash: 31d019196bc10e9c2f4eb605859b526f0ef18630ea36e96e678d6f093cf4a250
fetched_at: '2026-06-29T00:08:54.913599+00:00'
page_id: '347445343'
product: rm
source: tdn-rm
title: 2331652 EDUCACIONAL01-4252 DT Renovação de exemplares no mesmo dia do empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=347445343
version: 91
---

# RENOVAÇÃO DE EXEMPLARES NO MESMO DIA DO EMPRÉSTIMO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão bibliotecária |
| **Função:** | Renovação de exemplares |
| **Situação/Requisito:** | Ao realizar a renovação de um exemplar, onde não há restrição de renovação para o dia de devolução, o sistema apresenta uma mensagem de restrição informando que a operação não é possível porque ela está sendo realizada no mesmo dia do empréstimo. |
| **Solução/Implementação:** | Foi identificada uma validação incorreta que impedia a renovação caso o parâmetro para a restrição de renovação apenas no dia de devolução estivesse desmarcado e correção foi realizada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2535104 / 2398425 |
| **Requisito:** | N/A |

divs
