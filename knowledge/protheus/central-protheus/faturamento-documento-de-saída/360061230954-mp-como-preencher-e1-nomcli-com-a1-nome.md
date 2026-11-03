---
article_id: 360061230954
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 875e52e819eea558943cebc0dac41f66fb17d680ad98e130795d91b4012a58cf
fetched_at: '2026-06-28T22:38:45.204050+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP- Como preencher E1_NOMCLI com A1_NOME
type: support-article
updated_at: '2023-05-09T12:53:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061230954-MP-Como-preencher-E1-NOMCLI-com-A1-NOME
---

**Dúvida**Como preencher E1\_NOMCLI com A1\_NOME? Hoje somente é preenchido com A1\_NREDUZ  
  
**Ambiente**Microsiga Protheus - todas as versões.

**Solução**

Por padrão, o sistema sempre utilizará o **A1\_NREDUZ**  do cadastro de cliente (**Mata030**) para preencher **E1\_NOMCLI**, o que pode ser efetuado é utilizar um ponto de entrada para efetuar a mudança da gravação, não há um ponto específico para isso, pode se tentar utilizar o **m460fim (****<https://tdn.totvs.com/pages/viewpage.action?pageId=6784180>****)** para efetuar o tratamento em questão.
