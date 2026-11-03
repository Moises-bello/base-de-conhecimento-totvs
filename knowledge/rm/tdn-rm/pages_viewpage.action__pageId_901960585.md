---
content_hash: 654acd742acc7d19327189939af98f9a62d768dafc682be05b478e90603f4e2b
fetched_at: '2026-06-29T00:12:02.570196+00:00'
page_id: '901960585'
product: rm
source: tdn-rm
title: Tributação Isenta, Não tributada (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960585
version: 9
---

# ICMS40 - Tributação Isenta, Não tributada

Este grupo será gerado sempre que o CFOP informado no item estiver configurado com o CST 40

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMS40** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-1** | **Grupo de Escolha** | **Tributação Isenta, Não tributada** |
| CST | ICMS40 | 1-1 | Elemento | DREGRAICMS.SITTRIBUTARIA |
| **--- x — Sequência opcional do** **XML:** Será gerado sempre que na **Regra de ICMS** o campo **ICMS Desonerado** estiver marcado | | | | |
| vICMSDeson | ICMS40 | 1-1 | Elemento da Sequencia | TTRBMOV.VALORICMSDESONERADO |
| cBenef | ICMS40 | 1-1 | Elemento da Sequencia | TPRDCODFISCAL.CODFISCAL ou DCFOPCODAJUSTE ou DPRDBENEFICIOFISCAL.  O sistema disponibiliza três opções de busca para preenchimento. Consulte mais detalhes em: |

Exemploxml
41
]]>
