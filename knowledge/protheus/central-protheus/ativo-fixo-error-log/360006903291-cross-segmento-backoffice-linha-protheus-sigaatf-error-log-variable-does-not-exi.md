---
article_id: 360006903291
category: Ativo-Fixo - Error log
content_hash: 8db100c87a3d413e3a4b6292026dfc28ed13c973820806deecbb3a554c43abd9
fetched_at: '2026-06-28T22:41:54.837175+00:00'
product: protheus
section_id: 1500001547442
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ERROR LOG variable does
  not exist LCOPIA on AF010AVLR(ATFA010A.PRW)
type: support-article
updated_at: '2023-11-30T19:39:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006903291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ERROR-LOG-variable-does-not-exist-LCOPIA-on-AF010AVLR-ATFA010A-PRW
---

**Ocorrência**

Error log na rotina de cadastro de ativo variable does not exist LCOPIA on AF010AVLR(ATFA010A.PRW)

No módulo **Ativo Fixo**, ao tentar realizar (o processo ou a rotina) **Cadastro ou visualização de bens**   é apresentada a ( error log )  **variable does not exist LCOPIA on AF010AVLR(ATFA010A.PRW)**

**Ambiente**Protheus  – Ativo Fixo – A partir da versão 12.1.07]

**Solução**Execute o compatibilizador UPDDISTR. Caso o erro persista, verifique o X3\_VALID dos campos N3\_VORIG1, N3\_VORIG2, N3\_VORIG3, N3\_VORIG4, N3\_VORIG5.  
Pois o conteúdo correto é AF12VLRM().

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007181411)
