---
article_id: 1500011497562
category: Call Center - Televendas
content_hash: 527c72344d0045244c80ab8b8b816425748e03aacdad5df14ae5f4483bfb1241
fetched_at: '2026-06-28T22:41:30.180621+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - Cálculo
  de Imposto no Atendimento Televendas
type: support-article
updated_at: '2021-05-20T19:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011497562-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-C%C3%A1lculo-de-Imposto-no-Atendimento-Televendas
---

**Dúvida**Cálculo de Imposto no atendimento Televendas.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - a partir da versões 11.  
  
**Solução**Para visualizar o cálculo do imposto no atendimento Televenda (**TMKA273**) é necessário que parâmetro **MV\_TMKFIS** esteja igual .T. para habilitar a aba Imposto no atendimento.  
  
O cálculo de imposto é gravado em **memória** não em tabela, este é o mesmo comportamento dentro da Planilha Financeira no Pedido de Venda (**MATA410**).  
  
O imposto é demostrado pelo ***total da soma dos itens*** e não por itens, esta informação pode ser visualizada após gerar o documento de saída do pedido de venda, pois estará gravada em tabelas (**SD2** ou **SFT**), tudo dependerá do tipo do imposto para ir para uma tabela ou para a outra.
