---
article_id: 39096852277399
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2517fd0052212bff5440b0b760b780e9ceced21ac8f904c484c25ebb700a18f6
fetched_at: '2026-06-28T22:38:39.822262+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410SLDLOTE ao incluir
  Pedido de Venda
type: support-article
updated_at: '2026-03-18T12:48:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39096852277399-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410SLDLOTE-ao-incluir-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39096852268183)** **Tempo aproximado para leitura:****00:01:00 min**

**Dúvida**

Como resolver o Help A410SLDLOTE na inclusão de itens no Pedido de Venda (MATA410) utilizando controle de lote / poder de terceiros?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O HelpA410SLDLOTE ocorre quando a quantidade informada no item do pedido de venda (C6\_QTDVEN) é superior ao saldo disponível para o lote específico selecionado na tabela **SB8** (Saldo por Lote), geralmente vinculado a uma nota de entrada de poder de terceiros.

Para solucionar, siga uma das orientações abaixo:

1. **Ajuste de Quantidade:** Certifique-se de que a quantidade digitada no item seja igual ou inferior ao saldo disponível no lote selecionado.
2. **Seleção Automática:** Deixe o campo de lote em branco no item do pedido. Dessa forma, o Protheus realizará a busca e seleção automática do saldo disponível no momento da liberação do pedido.

**Observação:** Se o saldo no **SB8** estiver zerado ou inconsistente com o físico, o setor de estoque deve revisar o vínculo da Nota Fiscal de entrada ou realizar um inventário para correção do rastro.
