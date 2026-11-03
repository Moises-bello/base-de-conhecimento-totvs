---
content_hash: 7f0ea1abe78cf360c8fd4f8ffab6e0de2495a25eaf497dfe579df114d8bfedc5
fetched_at: '2026-06-29T00:10:15.404873+00:00'
page_id: '464970174'
product: rm
source: tdn-rm
title: Parâmetros Férias Portal - Ajuste nos parâmetros de férias para configurar
  a solicitação de abono.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464970174
version: 2
---

# 

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parâmetros Férias Portal |
| **Situação/Requisito:** | Ao marcar simultaneamente os parâmetros 'Permite até 10 dias de abono pecuniário' e  'Limite de Abono é 1/3 do Saldo de Férias' , apenas o primeiro era considerado, limitando desta forma a quantidade de dias de abono como 10 dias. |
| **Solução/Implementação:** | Os parâmetros 'Permite até 10 dias de abono pecuniário' e  'Limite de Abono é 1/3 do Saldo de Férias' não devem funcionar simultaneamente uma vez que uma parametrização anula a outra. Desta forma foi implementada uma validação para que ao marcar um destes parâmetros o outro será bloqueado e desmarcado. |
| **Tickets relacionados:** | 5210058 — FOPROTINAS01-7778 |
