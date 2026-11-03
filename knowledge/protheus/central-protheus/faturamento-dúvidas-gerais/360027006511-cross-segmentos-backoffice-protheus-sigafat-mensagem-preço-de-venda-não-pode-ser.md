---
article_id: 360027006511
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 68a829ab37cf3e2dace2195e4cab8fb732378969601c62bd70abaeaa05b0788b
fetched_at: '2026-06-28T22:38:29.850460+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Mensagem "Preço de venda
  não pode ser inferior ao preço contratado" no Pedido de Vendas
type: support-article
updated_at: '2025-11-26T13:43:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027006511-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Mensagem-Pre%C3%A7o-de-venda-n%C3%A3o-pode-ser-inferior-ao-pre%C3%A7o-contratado-no-Pedido-de-Vendas
---

**Ocorrência**  
Ao incluir um pedido de vendas quando coloco o código do produto vou confirmar o pedido ele apresenta a mensagem:

*"Este item de pedido de venda esta vinculado a um contrato de parceria, portanto o preço de venda não pode ser inferior ao preço contratado..."*

Analisando os contratos de parcerias desse cliente não tem nenhum contrato em aberto/ou tem algum parcialmente faturado.

Como faço para corrigir e fazer um novo Pedido de Venda sem vincular ao contrato de parceria já existente?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026406191)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**

Essa mensagem ocorre devido ao parâmetro **MV\_PRCCTR** que quando está ativo ".T." ele defini que se caso exista contrato de parceria, o sistema irá utiliza-lo durante a captação do Pedido de Venda ou Orçamento.   
  
**Solução**

Para solucionar essa ocorrência, deixe o parâmetro **MV\_PRCCTR** igual a **.F.**

**Saiba mais:**

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetros para Contrato de Parceria no Pedido e Orçamento de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018070412-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Par%C3%A2metros-para-Contrato-de-Parceria-no-Pedido-e-Or%C3%A7amento-de-Vendas)
