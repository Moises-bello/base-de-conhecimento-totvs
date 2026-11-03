---
content_hash: e55bf6436d10647b663ad68a17e4bb934cad35ba58d346b8600cd8f80fcb3f36
fetched_at: '2026-06-29T00:12:10.377758+00:00'
page_id: '953002441'
product: rm
source: tdn-rm
title: Grupo M. Tributos incidentes no Produto ou Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953002441
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo M. Tributos incidentes no Produto ou Serviço** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Campo de Origem | Campo na Aplicação | Observação |
| 163 | M01 | imposto | Tributos incidentes no Produto ou Serviço | G | H01 | - | 1-1 | - | Grupo ISSQN mutuamente exclusivo com os grupos ICMS e II, isto é, se o grupo ISSQN for informado os grupos ICMS e II não serão informados e vice-versa. | - | - | SE o campo "CRT" (ID=C21) = "3 – Regime Normal." |
| 163a | M02 | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais. | E | M01 | N | 0-1 | 13v2 | (NT 2013/003) | DITEM.VLRTOTTRIB | - |  |
