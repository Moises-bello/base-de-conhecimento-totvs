---
content_hash: 5affbec3d24d918377cc48ff6ae8f01a7600988a7d6d841a7524566875055f45
fetched_at: '2026-07-02T19:24:23.980104+00:00'
page_id: '454826080'
product: protheus
source: tdn-tec
title: Correção - SmartClient aborta ao tentar imprimir algum relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454826080
version: 1
---

Foi feita uma proteção pra que o problema não ocorra e a impressão funcione normalmente.

|  |  |
| --- | --- |
| Situação | SmartClient aborta ao tentar imprimir algum relatório. |
| Ocorrência | Devido a um colateral em outra implementação, o SmartClient faz um acesso indevido nas informações de impressão que causam o aborto. |
| Correção | Feita a proteção pra que o acesso indevido não aconteça e a impressão seja feita corretamente. |
| Informações adicionais | * Referente ao chamado: PP-646 PP-643 * Referente à ocorrência: ITEC-404 * Disponível em builds superiores a 17.3.0.5 |
