---
article_id: 22541257056023
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 97071c32ccd812c96b92e4e3f7eeec5632849d67e296a5cb9cf4f139f866101e
fetched_at: '2026-06-28T22:38:40.968057+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tabela de preço não sugere
  preço de venda
type: support-article
updated_at: '2024-07-11T14:33:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22541257056023-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tabela-de-pre%C3%A7o-n%C3%A3o-sugere-pre%C3%A7o-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22541257022999) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que fazer quando a tabela de preço não sugere preço de venda?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**É possível usar tabelas de preço para o preço ser sugerido para determinado cliente, ou, ao usar certo tipo de condição de pagamento, etc.

**Caso sua tabela de preço não leve o preço unitário "Prc. lista (C6\_PRUNIT)", cheque:**

1 - Cheque se a DATABASE (data do dia do sistema) e o C5\_EMISSAO (data de emissão do pedido de venda) estão no intervalo definido no intervalo de "Data de validade inicial (DA0\_DATDE)" de até "Data de validade final (DA0\_DATATE)" da tabela de preço.

2 - Cheque se a tabela de preços inserida no pedido de venda possui o campo "Tabela Ativa (DA0\_ATIVO=1).

3 - Cheque se o pedido de venda não é beneficiamento "Tipo (C5\_TIPO)" = "B - Utilizar Fornecedor", caso seja, o preço do produto na tabela de preços não é levado ao "Preço de lista (C6\_PRUNIT)" realmente, pois não se trata de uma venda, o preço do item será amarrado e será o mesmo da nota fiscal de entrada por questões legais.
