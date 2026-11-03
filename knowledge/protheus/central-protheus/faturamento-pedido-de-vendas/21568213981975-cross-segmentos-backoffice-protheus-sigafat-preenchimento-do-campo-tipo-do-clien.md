---
article_id: 21568213981975
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 22daf01400dda6eed2b99bc60a8e3d35dff33bfee1730fbd9c0f626375906644
fetched_at: '2026-06-28T22:38:39.992259+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo "Tipo
  do cliente (C5_TIPOCLI)" em Fornecedores
type: support-article
updated_at: '2024-02-23T17:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21568213981975-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-Tipo-do-cliente-C5-TIPOCLI-em-Fornecedores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21568239522327) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o preenchimento do campo "Tipo do cliente (C5\_TIPOCLI)" em Fornecedores incluídos no pedido de venda?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

O conteúdo do campo depende de como está cadastrado o campo "Tipo Fornecedor (A2\_TIPO)" no cadastro de fornecedores (Rotina MATA020).

![](https://totvssuporte.zendesk.com/attachments/token/PgopHWAPQZTsfctOTSXpLBdZq/?name=image.png)

* Se A2\_TIPO = F será C5\_TIPOCLI = 'F - Consumidor final' ao incluir o fornecedor no pedido de venda.
* Se A2\_TIPO = J será C5\_TIPOCLI = 'R - Revendedor' ao incluir o fornecedor no pedido de venda.
* Se A2\_TIPO = X será C5\_TIPOCLI = 'X - Exportacao/Importacao' ao incluir o fornecedor no pedido de venda.

**OBSERVAÇÃO:** Isso será válido quando o tipo do pedido de venda permitir a inclusão de fornecedor e não de um cliente, ou seja, pedidos de venda do tipo "D - Devolução de Compras" ou "B - Utiliza fornecedor".
