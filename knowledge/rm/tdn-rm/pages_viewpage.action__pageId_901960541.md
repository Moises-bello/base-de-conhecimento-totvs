---
content_hash: 8ac414247e65ef074991f0dbd801f64615fd355e5d3b308eae6d733a56f89fff
fetched_at: '2026-06-29T00:12:02.566013+00:00'
page_id: '901960541'
product: rm
source: tdn-rm
title: Prestação sujeito à tributação com redução de BC do ICMS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960541
version: 20
---

# ICMS20 - Prestação sujeito à tributação com redução de BC do ICMS

Este grupo será gerado sempre que o CFOP informado no item estiver configurado com o CST 20

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMS20** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-1** | **Grupo de Escolha** | **Prestação sujeito à tributação com redução de BC do ICMS** |
| CST | ICMS20 | 1-1 | Elemento | DREGRAICMS.SITTRIBUTARIA |
| pRedBC | ICMS20 | 1-1 | Elemento | TTRBMOV.FATORREDUCAO (ICMS) |
| vBC | ICMS20 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (ICMS)  Item do movimento, pasta Tributos e Valores |
| pICMS | ICMS20 | 1-1 | Elemento | TTRBMOV.ALIQUOTA (ICMS)  Item do movimento, pasta Tributos e Valores |
| vICMS | ICMS20 | 1-1 | Elemento | TTRBMOV.VALOR (ICMS)  Item do movimento, pasta Tributos e Valores |
| **--- x — Sequência opcional do XML:** Será gerado sempre que na **Regra de ICMS** o campo **ICMS Desonerado** estiver marcado | | | | |
| vICMSDeson | ICMS20 | 1-1 | Elemento da Sequencia | TTRBMOV.VALORICMSDESONERADO |
| cBenef | ICMS20 | 1-1 | Elemento da Sequencia | TPRDCODFISCAL.CODFISCAL ou DCFOPCODAJUSTE ou DPRDBENEFICIOFISCAL.  O sistema disponibiliza três opções de busca para preenchimento. Consulte mais detalhes em: |
| **--- x — Sequência opcional do XML:**Será gerado sempre que na **Regra de ICMS** o campo **Operação com FCP** estiver marcado | | | | |
| pFCP | ICMS20 | 1-1 | Elemento da Sequencia | TPRDCODFISCAL.PERFECP  Cadastro do produto, Anexos | Dados Fiscais por UF | edite a UF desejada | aba Identificação Campo %FECP |
| vFCP | ICMS20 | 1-1 | Elemento da Sequencia | Calculado (vBC \* pFCP) |

ExemploICMSRelatorioICMS com operação FCPxml
20
10.00
135.89
18.00
24.46
5.02
6.82
]]>Campos\_RelatorioICMS Desoneradoxml
20
10.00
135.00
18.00
24.30
3.24
7
]]>
