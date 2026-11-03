---
article_id: 360012428531
category: Ativo Fixo - Responsáveis x Bens
content_hash: 358b0d5ad3670187790bf90ad395f783dfa2748a09fcd0af50ea1af1e17ccb6b
fetched_at: '2026-06-28T22:41:47.370963+00:00'
product: protheus
section_id: 1500001547682
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF  - variable does not exist
  NOPC
type: support-article
updated_at: '2023-12-15T17:04:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012428531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-variable-does-not-exist-NOPC
---

**Ocorrência**

Ao realizar a adição de um responsável no cadastro de ativos, o sistema aborta com o erro "**variable does not exist NOPC**".

**Ambiente**

Protheus – Ativo Fixo – 12.1.17

**Causa**

O erro ocorre devido as validações do **X3\_WHEN** dos campos: "**ND\_ITEM**", "**ND\_CODRESP**", **"ND\_DTINI**", "**ND\_DTFIM**", onde os mesmos devem estar em branco.

**Solução**

Para solução deste caso, deverá ser aplicado o **UPDDISTR** com o **dicionário diferencial (SDF.BRA) e completo (SXS.BRA)** conforme portal: <https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117DD/>
