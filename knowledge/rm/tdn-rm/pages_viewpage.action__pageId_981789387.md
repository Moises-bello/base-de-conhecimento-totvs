---
content_hash: 50886884e79871963868cd3a8b4e4c3ead8ca5f0d78a87dcff1e020f02e4f025
fetched_at: '2026-06-29T00:12:15.755037+00:00'
page_id: '981789387'
product: rm
source: tdn-rm
title: Informações relativas ao ICMS - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981789387
version: 2
---

# ICMS -  Informações relativas ao ICMS

ICMSleftICMS00

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMS00** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **Prestação sujeito à tributação normal do ICMS** |
| CST | ICMS00 | 1-1 | Elemento | 00 - Tributação normal ICMS |
| vBC | ICMS00 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| pICMS | ICMS00 | 1-1 | Elemento | TTRBMOV.ALIQUOTA |
| vICMS | ICMS00 | 1-1 | Elemento | TTRBMOV.VALOR |

ICMS20

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMS20** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **Prestação sujeito à tributação com redução de BC do ICMS** |
| CST | ICMS20 | 1-1 | Elemento | 20 - Tributação com BC reduzida do ICMS |
| pRedBC | ICMS20 | 1-1 | Elemento | TTRBMOV.FATORREDUCAO |
| vBC | ICMS20 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| pICMS | ICMS20 | 1-1 | Elemento | TTRBMOV.ALIQUOTA |
| vICMS | ICMS20 | 1-1 | Elemento | TTRBMOV.VALOR |

ICMS45

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMS45** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **ICMS Isento, não Tributado ou diferido** |
| CST | ICMS45 | 1-1 | Elemento | 40 - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido  DNATUREZA.SITTRIBUTARIA |

ICMS20

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMS60** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **Tributação pelo ICMS60 - ICMS cobrado por substituição tributária.** **Responsabilidade do recolhimento do ICMS atribuído ao tomador ou 3º por ST** |
| CST | ICMS60 | 1-1 | Elemento | 60 - ICMS cobrado por substituição tributária |
| vBCSTRet | ICMS60 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| vICMSSTRet | ICMS60 | 1-1 | Elemento | TTRBMOV.VALOR |
| pICMSSTRet | ICMS60 | 1-1 | Elemento | TTRBMOV.ALIQUOTA |
| vCred | ICMS60 | 0-1 | Elemento | **Se** utiliza Crédito Outorgado (DFILIAL.UTILIZACREDITOOUTORGADO)  **então** essa tag terá valor = TTRBMOV.VALOR \* (DFILIAL.PERCCREDITOOUTORGADO / 100).  **Senão**, será igual a TTRBMOV.VALOR. |

ICMS90

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMS90** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **ICMS Outros** |
| CST | ICMS90 | 1-1 | Elemento | 90 - ICMS Outros |
| pRedBC | ICMS90 | 0-1 | Elemento | TTRBMOV.FATORREDUCAO |
| vBC | ICMS90 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| pICMS | ICMS90 | 1-1 | Elemento | TTRBMOV.ALIQUOTA |
| vICMS | ICMS90 | 1-1 | Elemento | TTRBMOV.VALOR |
| vCred | ICMS90 | 0-1 | Elemento | **Se** utiliza Crédito Outorgado (DFILIAL.UTILIZACREDITOOUTORGADO)  **então** essa tag terá valor = TTRBMOV.VALOR \* (DFILIAL.PERCCREDITOOUTORGADO / 100).  **Senão**, será igual a TTRBMOV.VALOR. |

ICMSOutraUF

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMSOutraUF** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **ICMS devido à UF de origem da prestação, quando diferente da UF do emitente** |
| CST | ICMSOutraUF | 1-1 | Elemento | 90 - ICMS Outra UF |
| pRedBCOutraUF | ICMS90 | 0-1 | Elemento | TTRBMOV.FATORREDUCAO |
| vBCOutraUF | ICMS90 | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| pICMSOutraUF | ICMS90 | 1-1 | Elemento | TTRBMOV.ALIQUOTA |
| vICMSOutraUF | ICMS90 | 1-1 | Elemento | TTRBMOV.VALOR |

ICMSSN

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMSSN** | **[ICMS](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **1-1** | **Grupo de Escolha** | **ICMS devido à UF de origem da prestação, quando diferente da UF do emitente** |
| CST | ICMSSN | 1-1 | Elemento | 01 - Simples Nacional |
| indSN | ICMSSN | 0-1 | Elemento | DFILIAL.OPTANTESIMPLES |
