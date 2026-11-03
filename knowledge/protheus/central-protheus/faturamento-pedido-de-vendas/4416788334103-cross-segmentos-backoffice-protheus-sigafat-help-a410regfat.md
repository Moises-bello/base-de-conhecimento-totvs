---
article_id: 4416788334103
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: dad906a7d98bc61d665def738a4514c0f3330d90a221b0233413e2a10a753090
fetched_at: '2026-06-28T22:38:39.818249+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410REGFAT
type: support-article
updated_at: '2024-04-25T17:47:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416788334103-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410REGFAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23054106788247) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No momento de fazer a exclusão do pedido de venda o sistema informa o HELP A410REGFAT.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23054191407511)**

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Causa**O pedido já foi parcialmente faturado.  
  
**Solução**O Help A410REGFAT ocorre caso algum item já tenha sido ***FATURADO***, impedindo a exclusão do PV. Para exclusão do pedido de venda, a nota não deve estar vinculada, avalie através da opção tracker no pedido de venda se possui alguma NF e verifique se é possível excluir. Após a exclusão da NF, exclua o pedido de venda.   
Realizar alterações em ambiente de homologação para validação.
