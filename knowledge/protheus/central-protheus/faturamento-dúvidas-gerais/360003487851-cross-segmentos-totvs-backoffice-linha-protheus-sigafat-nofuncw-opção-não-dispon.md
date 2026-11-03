---
article_id: 360003487851
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 7834a489f6a9d536fc6c4cadcf57a1c9f2b6216b6e5f5962b223b89cc41d3b21
fetched_at: '2026-06-28T22:38:29.997982+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nofuncw-Opção
  não disponível no Protheus função:  A410WnLoc() called by LEDITCOL.'
type: support-article
updated_at: '2021-09-20T20:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003487851-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nofuncw-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-fun%C3%A7%C3%A3o-A410WnLoc-called-by-LEDITCOL
---

****![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min****

**Ocorrência**

Ao clicar no **C6\_LOCALIZ** gera o Help: **NOFUNCW - Problema: Opção não disponível no Protheus função: A410WnLoc() called by LEDITCOL.**

Em alguns casos, é gerado o error.log: **InterFunctionCall: cannot find function A410WNLOC in AppMap on LEDITCOL(MSGETDAD.PRW).**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT - a partir da release 12.1.17.  
  
**Causa**

A função **A410WNLOC** era utilizada na release 11.80 e na versão 12 foi descontinuada de uso, o que pode ter ocorrido é que os **Ambientes Migrados** mantiveram a instrução no **x3\_WHEN** do campo **C6\_LOCALIZ**.

**Solução**  
Para solucionar a ocorrência, vá no **X3\_WHEN (Modo de Edição)** do campo **C6\_LOCALIZ**, e retire a validação **A410WnLoc**, que o problema deixará de ocorrer.

Outra opção, é fazer o download do dicionário de dados do portal do cliente relacionado a release utilizada e processar o **UPDDISTR** para que o dicionário de dados seja corrigido e fique conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409048362519/mceclip0.png)

Obs: O tratamento indicado na FAQ, requer conhecimento técnico de estrutura Protheus, caso necessite de apoio mais técnico, contate a equipe de framework.
