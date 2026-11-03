---
content_hash: 4baed4aea23b786d8fe0a7b99e8bd7f87123d422e771fdec63acd10257575a5c
fetched_at: '2026-06-29T00:10:15.034672+00:00'
page_id: '463799312'
product: rm
source: tdn-rm
title: 5188626 FISCAL01-8158 DT Devolução de venda que teve partilha de 100%
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463799312
version: 2
---

# Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | Ao consultar a autorização da nota de devolução de venda a rejeição abaixo está sendo reportada:  A nota não foi autorizada.  NF-e foi rejeitada. Erro: Rejeição: Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:1]  014 - NFe não autorizada - Corrija o problema e retransmita as notas fiscais eletrônicas. 699/Rejeição: Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:1] |
| **Solução/Implementação:** | O processo da NF-e quando existe partilha de ICMS foi ajustado para preencher a tag pICMSInterPart corretamente quando o percentual da partilha for 100% para a UF de Destino. |
