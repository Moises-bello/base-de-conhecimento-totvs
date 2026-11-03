---
content_hash: e1e795f4b1d3610118f4b958f1154832b0802f4510cce8a39c4c5b3f109c44bd
fetched_at: '2026-06-29T00:12:02.589493+00:00'
page_id: '901960798'
product: rm
source: tdn-rm
title: Informações do ICMS de partilha com a UF destinatária (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960798
version: 5
---

# ICMSUFDest - Informações do ICMS de partilha com a UF destinatária

Este grupo será gerado sempre que:

O campo IEUFDest (grupo do emitente) estiver preenchida.

A regra de ICMS da natureza de operação tiver a Operação Tributária como "Diferencial de Aliquota".

Possuir linha de ICMS nos tributos do item de movimento.

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMSUFDest** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-1** | **Grupo de Escolha** | **Informações do ICMS de partilha com a UF destinatária** |
| cUFDest | ICMSUFDest | 1-1 | Elemento | Preencher com o campo  **UF** do Grupo **enderDest** |
| vBCUFDest | ICMSUFDest | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (ICMS)  Item do movimento, pasta Tributos e Valores |
| pFCPUFDest | ICMSUFDest | 1-1 | Elemento | TPRDCODFISCAL.PERFECP  Cadastro do produto, Anexos | Dados Fiscais por UF | UF do destinatário | aba Identificação Campo %FECP |
| pICMSUFDest | ICMSUFDest | 1-1 | Elemento | TTRBMOV.ALIQUOTA (ICMS)  Item do movimento, pasta Tributos e Valores |
| vFCPUFDest | ICMSUFDest | 1-1 | Elemento | Calculado (vBCUFDest \* pFCPUFDest) |
| vICMSUFDest | ICMSUFDest | 1-1 | Elemento | Calculado (vBCUFDest \* pICMSufDest)  Item do movimento, pasta Tributos e Valores |
| vICMSUFEmi | ICMSUFDest | 1-1 | Elemento | TTRBMOV.VALOR (ICMS)  Item do movimento, pasta Tributos e Valores |
| cBenefUFDest | ICMSUFDest | 0-1 | Elemento | TPRDCODFISCAL.CODFISCAL ou DCFOPCODAJUSTE ou DPRDBENEFICIOFISCAL.  O sistema disponibiliza três opções de busca para preenchimento, considerando o campo UF do destinatário. Consulte mais detalhes em: ]]> |

Exemploxml
  
200.00
8.00
12.00
16.00
32.00
24.00
123
  
]]>
