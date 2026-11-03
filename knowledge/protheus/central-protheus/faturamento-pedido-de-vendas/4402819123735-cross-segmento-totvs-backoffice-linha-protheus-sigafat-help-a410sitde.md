---
article_id: 4402819123735
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 185ded4aecc49c59e3ffb571c930e3d636b962bfe49df2586adf9ab69ca07491
fetched_at: '2026-06-28T22:38:38.531493+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A410S/ITDE
type: support-article
updated_at: '2022-05-11T17:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402819123735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410S-ITDE
---

**Ocorrência**Ao incluir um pedido de devolução e não informar o campo item origem **C6\_ITEMORI**, apresenta o help **A410S/ITDE**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento- Todas as versões  
  
**Causa**O help é exibido caso não informe o item da nota fiscal de origem (**C6\_ITEMORI**) no pedido de devolução (**C5\_TIPO = D**).  
  
**Solução**Para incluir uma devolução no sistema sem gerar o help é necessário informar os campos no pedido de devolução:

1. Cliente - **C5\_CLIENTE**;
2. Loja - **C5\_LOJA**;
3. Nota Origem - **C6\_NFORI**;
4. Serie Origem - **C6\_SERIORI**;
5. Item Origem - **C6\_ITEMORI**;
6. Produto - **C6\_PRODUTO**.

![devolucao.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402819058327/devolucao.png)
