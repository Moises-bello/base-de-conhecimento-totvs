---
article_id: 23058624552343
category: Faturamento - Orçamentos
content_hash: 0880dcd4e1212fa84456cdeea4ba05eb418f79df260a648dadb7366bec1edebc
fetched_at: '2026-06-28T22:38:25.044587+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Transportadora no pedido
  de venda após aprovação do orçamento de venda
type: support-article
updated_at: '2024-04-25T20:31:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23058624552343-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Transportadora-no-pedido-de-venda-ap%C3%B3s-aprova%C3%A7%C3%A3o-do-or%C3%A7amento-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23058639893399) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao efetivar um orçamento de venda, o pedido de venda não está sendo gerado com o campo de transportadora preenchido, há como resolver?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Para que seja preenchido a transportadora no pedido de venda após efetivação do orçamento de venda:

* 1 - Visualize o cliente do orçamento no campo "CJ\_CLIENTE"
* 2 - Entre na rotina "Clientes (CRMA980)" e preencha o campo Transp. "A1\_TRANSP" com a transportadora.

Agora nas efetivações (Rotina MATA416), a transportadora no pedido de venda "Transp. (C5\_TRANSP)" será criada já preenchida de acordo com a transportadora vinculada do cadastro.
