---
article_id: 4417449367831
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9d6ec74a617d54e85cc0b4695b759b34f43dc72095bad90fed477bc020dc3f24
fetched_at: '2026-06-28T22:38:38.621201+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - type mismatch
  on compare on MATABPRVEN(OMSA010.PRX)
type: support-article
updated_at: '2021-12-29T16:52:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417449367831-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-type-mismatch-on-compare-on-MATABPRVEN-OMSA010-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao preencher um pedido de venda e  incluir o produto o sistema apresenta uma mensagem  (**MV\_ESTADO**) em uma caixa box e logo após apresenta erro log: **type mismatch on compare  on MATABPRVEN(OMSA010.PRX) 08/09/2020 11:51:49 line : 4297**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417443455895/mceclip0.png)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Causa**

O problema ocorre por que a filial em que o pedido está sendo efetuado não possui o parâmetro **mv\_estado**.

O sistema emite a mensagem de help sobre **mv\_estado**, no momento que se utiliza uma tabela de preço no pedido de vendas (**mata410**).  
  
Se houver mais de uma filial no sigamat da empresa, é preciso certificar que essas filiais possuam o parâmetro cadastrado para cada uma de forma individual.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Via configurador, inclua o parâmetro **mv\_estado** para filial em que o erro está sendo gerado.  
2. Reinicie o smartclient e efetue o processo do pedido novamente.
