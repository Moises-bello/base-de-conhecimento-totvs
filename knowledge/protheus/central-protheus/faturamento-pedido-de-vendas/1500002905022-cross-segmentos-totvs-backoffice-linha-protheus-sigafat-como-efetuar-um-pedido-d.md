---
article_id: 1500002905022
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 38050b7ea9920ca49179850ac398ea04c591bfa63d1fe3caf4ae81cbf6449545
fetched_at: '2026-06-28T22:38:41.201044+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Como efetuar um
  pedido de venda
type: support-article
updated_at: '2023-12-15T21:28:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002905022-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-efetuar-um-pedido-de-venda
---

**Dúvida**

Procedimento básico de como criar(incluir) um pedido de venda no módulo Faturamento.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - todas as versões.  
  
**Solução**

Para gerar  um pedido de venda básico no faturamento é necessário:

-Ter um cliente;

-Ter uma condição de pagamento;

-Ter um produto;

-Ter um TES de saída que conterá as instruções de cálculos de impostos, se vai ou não movimentar estoque ou se vai ou não gerar financeiro.

Tendo essas informações, você incluirá no cabeçalho do pedido:

-O tipo do pedido como Normal;

- O cliente e loja, sendo que essa informação de cliente será replicada automaticamente para cliente e loja de entrega;

-A condição de pagamento;

Na linha do item do pedido, você incluirá:

- O produto;

- A quantidade  a ser vendida;

- O preço de venda, sendo que esta informação multiplicada pela quantidade a ser vendida preencherá automaticamente o valor total do pedido;

- O TES de saída (para saber a forma de configurações do TES conforme a operação realizada, consulte nossa equipe de atendimento Fiscal) .

Feito isso, confirme a inclusão do pedido de venda.

![Pedido_de_venda.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101689194)

Saiba mais:   
  
**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso da TES Inteligente no Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034657374-MP-FAT-Uso-da-TES-Inteligente-no-Pedido-de-Venda) [de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034657374-MP-FAT-Uso-da-TES-Inteligente-no-Pedido-de-Venda)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Como vincular ou Desvincular RA no Pedido de Vendas pela Rotina MATA410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-MP-FAT-Como-vincular-ou-Desvincular-R-A-%C3%A0-um-Pedido-de-Vendas-pela-Rotina-MATA410)**

**[MP - FAT - Seleção do produto por Código de Barras - Tecla F10 no Pedido de Vendas (MATA410)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041452913-MP-FAT-Sele%C3%A7%C3%A3o-do-produto-por-C%C3%B3digo-de-Barras-Tecla-F10-no-Pedido-de-Vendas-MATA410-)**

**[SIGAFAT - Exclusão de Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003259602-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclus%C3%A3o-de-Pedido-de-Vendas)**
