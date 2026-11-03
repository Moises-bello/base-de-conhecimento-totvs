---
content_hash: 1b233374455d613e1e0d13784cbf09b029287c360e3a9144104f9de1ae4b3471
fetched_at: '2026-07-02T19:24:21.613518+00:00'
page_id: '268802877'
product: protheus
source: tdn-tec
title: Correção - TPaintPanel blinkers duplicados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268802877
version: 1
---

Implementado tratamento para evitar a adição de blinkers duplicados.

|  |  |
| --- | --- |
| Situação | É possível inserir mais de uma vez o mesmo blinker. |
| Ocorrência | Com blinkers repetidos, ao excluir um ID ele não exclui todas as repetições, ocasionando do shape ainda ser um blinker. |
| Correção | Implementado tratamento para que não seja adicionado novamente um blinker para o mesmo ID. |
| Informações adicionais | * Referente ao chamado: TWGG50 * Referente à ocorrência: SSIM-1270 * Disponível em builds superiores a 7.00.131227A 2.3.0 |
