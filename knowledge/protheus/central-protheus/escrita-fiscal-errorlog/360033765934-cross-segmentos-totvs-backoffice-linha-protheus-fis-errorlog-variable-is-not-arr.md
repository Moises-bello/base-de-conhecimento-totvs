---
article_id: 360033765934
category: Escrita Fiscal - Error.log
content_hash: 96ccefa5de0bd69a3fd1cd3e41cf01016b3829bc734e95443c26a92f3d1510ca
fetched_at: '2026-06-28T22:39:32.845948+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Error.log - variable
  is not array - Type [U] on XFISLF(IMPXFIS.PRW)
type: support-article
updated_at: '2023-02-08T12:25:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033765934-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Error-log-variable-is-not-array-Type-U-on-XFISLF-IMPXFIS-PRW
---

**Dúvida**

Como solucionar o error.log; variable is not array - Type [U] on XFISLF(IMPXFIS.PRW)

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Preencher o campo Form. Livro "F4\_LIVRO" somente com formula "Advpl" e entre aspas duplas.

**Obs.**Não confundir o preenchimento do campo (Form. Livro / F4\_LIVRO com Nr. Livro / F4\_NRLIVRO), este preenchimento equivocado poderá causar erros de inclusão e ou visualização de operações realizadas com este determinado TES.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043471734/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044319713/mceclip1.png)
