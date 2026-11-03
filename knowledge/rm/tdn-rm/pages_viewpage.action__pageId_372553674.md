---
content_hash: 1167ffb6d4347c7ec0a6fb80b5862cc319f88ea359d26a2d8b1d29980a0aef3d
fetched_at: '2026-06-29T00:09:01.192793+00:00'
page_id: '372553674'
product: rm
source: tdn-rm
title: 3154744 FISCAL01-5083 DT Evento de cancelamento - Cancelar o movimento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372553674
version: 2
---

# NF-e (Estadual) - Evento de Cancelamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | NF-e (Estadual) - Evento de Cancelamento |
| **Situação/Requisito:** | Ao solicitar o cancelamento de uma NF-E Estadual, o movimento referente a esta NF-E não está sendo cancelado, apresentando a mensagem de erro "Referencia de Objeto não definida para uma instância de um objeto". |
| **Solução/Implementação:** | Foi  ajustado o processo de consulta de autorização de eventos para que ao realizar a consulta do evento o sistema realize o cancelamento da NF-e e do movimento atrelado a mesma. |
