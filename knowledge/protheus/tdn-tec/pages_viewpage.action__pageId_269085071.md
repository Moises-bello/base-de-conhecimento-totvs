---
content_hash: 930456c18ca14387593e015207a015f0740148ea10b5e7304f9e6a1811c3b956
fetched_at: '2026-07-02T19:24:22.235741+00:00'
page_id: '269085071'
product: protheus
source: tdn-tec
title: Correção - Alinhamento em TGroup
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085071
version: 2
---

|  |  |
| --- | --- |
| Situação | Utilizar alinhamento em TGroup não funciona, não alinha os widgets filhos. |
| Ocorrência | Devido ao TGroup não poder ser parent diretamente de nenhum widget, ocorre um problema na hora de controlar alinhamento |
| Correção | Correção pontual para o widget TGroup aceitar alinhamento para os widgets internos. |
| Informações adicionais | * Referente ao chamado: TVVTEO * Referente à ocorrência: SSIM-1266 * Disponível no Label 7.00.131227A, release SmartClient 2.3.3 |
