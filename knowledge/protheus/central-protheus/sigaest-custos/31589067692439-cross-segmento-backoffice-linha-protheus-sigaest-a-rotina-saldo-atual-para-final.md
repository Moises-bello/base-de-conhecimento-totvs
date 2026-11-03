---
article_id: 31589067692439
category: SIGAEST - CUSTOS
content_hash: b75c9e30a3bdfd68eb103beeaee3f91baba64557cab899784c814122bb0e881d
fetched_at: '2026-06-28T22:39:00.565373+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A rotina Saldo Atual
  para Final (MATA350) deve atualizar o campo B2_CMFIM1?
type: support-article
updated_at: '2025-04-22T21:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31589067692439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-A-rotina-Saldo-Atual-para-Final-MATA350-deve-atualizar-o-campo-B2-CMFIM1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31589053036951) Tempo aproximado para leitura: 00**:01:00 min** **Dúvida**

Utilizo o método de custo online onde meu parametro MV\_CUSMED possui conteúdo "O" de online e ao executar a rotina Saldo Atual para Final não está atualizando o campo B2\_CMFIM1, o mesmo deveria ser atualizado?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Na rotina **MATA350**, nunca atualiza o campo **B2\_CMFIM1**. Ela é responsável apenas por atualizar os campos de saldo **Qtde** e **Valor**, ou seja, **B2\_QFIM** e **B2\_VFIM1**, respectivamente. Esses campos são utilizados no fechamento e geram a SB9, com os valores de início para o próximo período (**B9\_QINI** e **B9\_VINI1**). O custo médio para o próximo período é o próprio **B2\_CM1**.

O campo **B2\_CMFIM1** é atualizado pela rotina **MATA330** (Recalculo do custo médio). Para os clientes que utilizam o **MV\_CUSMED = O (online)**, pode ser necessário executar o recalculo para o cálculo da MOD. Isso pode resultar na atualização do campo **B2\_CMFIM1** de outro produto.

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
