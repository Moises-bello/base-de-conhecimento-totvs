---
article_id: 1500005473302
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7af8f09f975d079db2f3de803ddee9bfc73c8ce780c74d320313113138c4d91f
fetched_at: '2026-06-28T22:38:41.212060+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Crosss Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre
  geração de título através do pedido de venda
type: support-article
updated_at: '2023-12-28T16:59:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005473302-Crosss-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-gera%C3%A7%C3%A3o-de-t%C3%ADtulo-atrav%C3%A9s-do-pedido-de-venda
---

**Dúvida**É possível gerar um título na inclusão de um pedido de venda?

**Ambiente**Crosss Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

No processo de pedido venda somente é possível gerar título, quando se trata do uso da função **Adiantamento**, onde é definido o adiantamento na condição de pagamento, e em outras ações do pedido de venda (**MATA410**), Adiantamento, se não há um título no módulo Financeiro do tipo  **RA**, o sistema te dará a opção de incluir neste momento , para posteriormente relacionar ao pedido, conforme documentação: **[MP -FAT- Como vincular ou Desvincular R.A. à um Pedido de Vendas pela Rotina MATA410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-MP-FAT-Como-vincular-ou-Desvincular-R-A-%C3%A0-um-Pedido-de-Vendas-pela-Rotina-MATA410?source=search)**.  
  
Fora isso, não é possível gerar o título na inclusão do pedido, o fator gerador da integração com o Financeiro e por sua vez, geração de títulos é a preparação da nota de saída , via rotina **mata461**.

**Saiba Mais:** [Adiantamento no Pedido de Vendas](https://tdn.totvs.com/x/-pgcKw)
