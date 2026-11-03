---
article_id: 360020176612
category: Call Center - Dúvidas Gerais
content_hash: fd7e49841055136cfa781225acae59c3089f9551c29b1f15df7d6c71a9fd7454
fetched_at: '2026-06-28T22:41:26.798307+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - Contato vinculado
  à entidade
type: support-article
updated_at: '2022-06-17T14:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020176612-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Contato-vinculado-%C3%A0-entidade
---

**Dúvida**

Como trabalhar com apenas um Contato vinculado à Entidade ?

**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - desde a versão 11.

**Solução**

- Deixe o campo **U5\_TIPO** em branco;

- Configure a rotina **Grupo de Atendimento**, na aba **Lista de Contato**, campo **Contato**(**U0\_VALCONT**) = **Simultaneo**.

Neste caso o contato pode estar em listas distintas (Telemarketing, Televendas e Telecobrança), na mesma data.
