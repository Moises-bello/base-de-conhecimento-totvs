---
content_hash: 93b88953c4c62e19db0c7008220be72b0bd370edffdb99d3f23c22b9b183667d
fetched_at: '2026-06-29T00:12:02.558187+00:00'
page_id: '901960458'
product: rm
source: tdn-rm
title: Prestação sujeito à tributação normal do ICMS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960458
version: 9
---

# ICMS00 - Prestação sujeito à tributação normal do ICMS

Este grupo será gerado sempre que o CFOP informado no item estiver configurado com o CST 00

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMS00** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-10** | **Grupo de Escolha** | **Prestação sujeito à tributação normal do ICMS** |
| CST | ICMS00 | 1-1 | Elemento | DREGRAICMS.SITTRIBUTARIA |
| vBC | ICMS00 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (ICMS)  Item do movimento, pasta Tributos e Valores |
| pICMS | ICMS00 | 1-1 | Elemento | TTRBMOV.ALIQUOTA (ICMS)  Item do movimento, pasta Tributos e Valores |
| vICMS | ICMS00 | 1-1 | Elemento | TTRBMOV.VALOR (ICMS)  Item do movimento, pasta Tributos e Valores |
| **--- x — Sequência opcional do XML:** Será gerado sempre que na **Regra de ICMS** o campo **Operação com FCP** estiver marcado e pFCP deve conter valor maior que zero. | | | | |
| pFCP | ICMS00 | 1-1 | Elemento da Sequencia | TPRDCODFISCAL.PERFECP  Cadastro do produto, Anexos | Dados Fiscais por UF | edite a UF desejada | aba Identificação Campo %FECP |
| vFCP | ICMS00 | 1-1 | Elemento da Sequencia | Calculado (vBC \* pFCP) |

Exemploxml
00
844.00
10.00
84.40
5.00
42.20
]]>
