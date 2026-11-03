---
article_id: 11180410309143
category: Faturamento - Integrações
content_hash: 65eb4ca183f31acb7ec67d3da40bce4ade204d3d19a23e0225758c26e96e0b71
fetched_at: '2026-06-28T22:38:26.416456+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Help:GW1_CDREM
type: support-article
updated_at: '2022-12-23T20:53:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11180410309143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Help-GW1-CDREM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao integrar uma nota de saída (mata461) com o GFE, gera o help:

**O campo Remetente (GW1\_CDREM) não foi preenchido GW1\_CDREM**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

O help em questão ocorre ao sincronizar a Nota via **OMSM011**, por que, na nota fiscal existe o campo **f2\_cliret** preenchido, e quando este campo está preenchido é necessário preencher o campo filial como Sim na GU3 ,campo **GU3\_EMFIL**:

![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AIGoCJmPLjk4qAjhf%2B67hus%2Fy0EsiB7JmNjz5XnLvmCsS70RqCFUC5Khie0nLunFjZu6r%2FwFyCnJVuZV5tA1iSz6K1suYqAyGUyHwEJO9aVcIHUTtK8%2FP6fk4i1kSP99M9gnxseLcFeTg6DRYKEmrHFJTDFThCj0DiUKrJ32g5KuTkHj06Wavgcy06ob5%2BxWIcL8FDKQLMAd2CNVqYrHtjc2hwwj40NyhPqPDA7EA82k9LHzbljvKQZKimSooGMqTv%2Fn9IZe4r8zWhgg61Vt%2BuwnRFPKJQ46O%2FmAw3HPVYEzeGzfI1X4m2LiV5OFnWEjfHjmRi4J09q3bqKolyAZd6Ivo7ZNXfoVi8effFaMekeGwUQgnJmODriKkCo%2FLiFK5buqPgANPFr9DIFlgWjqO5ZlicfoQ6kkrAAo0153qRVlxWvE%2BmA20B4Q7RXxLAP3YPxZcOKtZoejrikzu4ngoGmPBmZP&sz=w1044-h752)

O campo **f2\_cliret** recebe a informação através do campo do pedido de vedna **c5\_cliret**:

C5\_CLIRET: **Local da Retirada**(quando o endereço é diferente do endereço do remetente), onde iremos retirar a mercadoria, quando não sair da Filial.   Esse campos forma criado em razão de atender a Nota técnica abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11180404730135)

Caso o campo c5\_cliret esteja em branco, manterá o campo f2\_cliret em branco, o sistema buscará a integração pelo emissor da filial.
