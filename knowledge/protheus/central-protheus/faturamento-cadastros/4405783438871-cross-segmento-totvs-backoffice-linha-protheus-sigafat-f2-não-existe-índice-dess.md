---
article_id: 4405783438871
category: Faturamento - Cadastros
content_hash: a0e9d0271295e090164a40d970a875ca53c59f62b85e8c000f33c077e5dd50fb
fetched_at: '2026-06-28T22:38:36.529434+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  F2 - Não existe
  índice desse alias no Sindex
type: support-article
updated_at: '2021-08-06T12:38:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405783438871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-F2-N%C3%A3o-existe-%C3%ADndice-desse-alias-no-Sindex
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao efetuar a contabilização da nota de saída (CTBANFS), gera o HELP:

F2 - Não existe índice desse alias no Sindex

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405783226263/mceclip0.png)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**O erro ocorre por que está sendo referenciado a tabela **SF2** apenas como **F2** na query de valor (**CT5\_VLR01**) do lançamento padrão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o cadastro de lançamento padronizado (**CTBA080**) e valide a query informada no campo **CT5\_VLR01.**  
2. Ajuste o nome de tabela e salve o cadastro.

3. Após o ajuste do lançamento, efetue a contabilização.
