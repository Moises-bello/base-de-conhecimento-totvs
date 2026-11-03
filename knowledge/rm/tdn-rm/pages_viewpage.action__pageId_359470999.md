---
content_hash: f079544643c469e1e5577d1aaece4243c753ad148fa6f69a0737a6ea269fad6d
fetched_at: '2026-06-29T00:08:58.091429+00:00'
page_id: '359470999'
product: rm
source: tdn-rm
title: 2668680 RMSAU-3580 DT Sistema trava apos registrar uma Internação SUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359470999
version: 1
---

# Registro de Internação SUS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Registro de Internações. |
| **Situação/Requisito:** | Apos realizar uma internação SUS, na rotina de Registro de Internações, e clicar em registrar, o sistema causa travamento e impede a inclusão do registro. |
| **Solução/Implementação:** | Remoção da FK FKSZSUSAIHPROD\_SZPARCIALATEND no banco de dados. |
| **Tickets relacionados:** | [2668680](https://totvssuporte.zendesk.com/agent/tickets/2668680) |
| **Requisito:** | RMSAU-3580 |
