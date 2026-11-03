---
article_id: 360018229312
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 36678898561461232d2ba612e0b729dabc52c4eb3fb94b38de13c12499f856b2
fetched_at: '2026-06-28T22:38:28.735965+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Campo A1_TPFRET difere
  do campo C5_TPFRETE
type: support-article
updated_at: '2022-09-12T18:41:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018229312-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Campo-A1-TPFRET-difere-do-campo-C5-TPFRETE
---

**Dúvida**

No que difere os campos A1\_TPFRET e C5\_TPFRETE?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat  -  a partir da versão 11.  
  
  
**Solução**

Existe no cadastro de cliente, o campo **A1\_TPFRET**. Quando configurado, o conteúdo deste campo é transferido para o campo **C5\_TPFRETE**.

Existem casos, que o campo da tabela **SC5** possui opções que não são listados no campo da tabela **SA1**.

Para solucionar, configure no campo **A1\_TPFRET**, com as mesmas opções e validações do campo **C5\_TPFRETE**.
