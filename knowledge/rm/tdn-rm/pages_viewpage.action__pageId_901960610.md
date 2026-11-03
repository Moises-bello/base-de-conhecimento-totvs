---
content_hash: b389704a46ec192b3631714237c0c0759847bbc0d912eaddbcb99f13b5efc0d0
fetched_at: '2026-06-29T00:12:02.574425+00:00'
page_id: '901960610'
product: rm
source: tdn-rm
title: Tributação com Diferimento (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960610
version: 5
---

# ICMS51 - Tributação Isenta, Não tributada

Este grupo será gerado sempre que o CFOP informado no item estiver configurado com o CST 51

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMS51** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-1** | **Grupo de Escolha** | **Tributação com Diferimento** |
| CST | ICMS51 | 1-1 | Elemento | DREGRAICMS.SITTRIBUTARIA |
| **--- x — Sequência opcional do XML:** Será gerado sempre que na **Regra de ICMS** o campo **ICMS Desonerado** estiver marcado | | | | |
| vICMSDeson | ICMS51 | 1-1 | Elemento da Sequencia | TTRBMOV.VALORICMSDESONERADO |
| cBenef | ICMS51 | 1-1 | Elemento da Sequencia | PRDCODFISCAL.CODFISCAL ou DCFOPCODAJUSTE ou DPRDBENEFICIOFISCAL.  O sistema disponibiliza três opções de busca para preenchimento. Consulte mais detalhes em: ]]> |

Exemploxml
51
2.00
7
]]>
