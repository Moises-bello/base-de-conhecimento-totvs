---
content_hash: aba9be2d3979dfbc56b6cf27de341f3d482bc38588670198a18d8a3d80e79d42
fetched_at: '2026-06-29T00:11:16.138693+00:00'
page_id: '662421716'
product: rm
source: tdn-rm
title: Transmissão de evento REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662421716
version: 4
---

Ao transmitir um evento REINF é realizada uma integração com o TSS através do  através do retorno do TSS para o RM, o evento pode ser Pendente ou Inconsistente.

Para múltiplos eventos, a transmissão é feita fracionada, com lotes de 50 eventos transmitidos. Isso permite realizar a transmissão de qualquer quantidade de eventos.

Ex.: *Se eu transmitir 500 eventos de uma só vez, internamente irá fracionar com 10 lotes de 50 eventos para transmitir todos.*

**Se eu consultar 103 eventos de uma só vez, internamente irá fracionar com 2 lotes de 50 eventos e 1 lote de 3 eventos.**
