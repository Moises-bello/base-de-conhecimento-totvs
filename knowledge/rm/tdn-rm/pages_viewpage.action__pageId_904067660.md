---
content_hash: f4f38d89942fa17be1def64d5f09d849dec138de3517234d55de2d103e9f280b
fetched_at: '2026-06-29T00:12:03.164361+00:00'
page_id: '904067660'
product: rm
source: tdn-rm
title: Período da Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904067660
version: 12
---

LayoutCampos

O **"Período de Apuração"** no layout do **MIT (Módulo de Inclusão de Tributos)** define o mês e o ano de referência para a apuração dos tributos declarados. Essas informações são obrigatórias e estruturadas no formato JSON.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo** | **Nível** | **Tipo** | **Obrigatório** | **Descrição** | **Origem dos Dados** | **Observação** |
| **Período Apuração** | **1** | **Object** | **Sim** | **Período da apuração.** |  |  |
| MesApuracao | 2 | Number | Sim | Mês da apuração. | Gerado com  o Mês informado no campo Início Período da Rotina. | mínimo: 1, máximo: 12 |
| AnoApuracao | 2 | Number | Sim | Ano da apuração | Gerado com  o Ano informado no campo Início Período da Rotina. | formato AAAA. mínimo: 2025. |

ExemplojsPeríodo de Apuraçãotrue
