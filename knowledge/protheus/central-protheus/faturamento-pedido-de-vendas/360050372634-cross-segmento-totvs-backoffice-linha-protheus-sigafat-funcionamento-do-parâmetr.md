---
article_id: 360050372634
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3c63c4a079640f3a9528d40fceeee4ca5b998dd58e7c4d3bc1eacf5a6335fa3b
fetched_at: '2026-06-28T22:38:38.526515+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  do parâmetro MV_TIPCPDT
type: support-article
updated_at: '2023-08-15T14:52:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050372634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-TIPCPDT
---

**Dúvida**

Qual o parâmetro que define o preenchimento da Data de Entrega na Cópia do Pedido de Venda?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O parâmetro **MV\_TIPCPDT** objetiva o preenchimento da **data de entrega** na **cópia do pedido de venda (MATA410)**.

Seu conteúdo pode ser:  
**1** = Copia a data do pedido original.  
**2** = Se a data de entrega for menor que a data da emissão do pedido mantém a data da emissão do pedido. Caso contrário mantém a data da entrega.  
**3** = Aplica a diferença de dias entre a emissão e a entrega do pedido original na cópia.

**Veja exemplos de uso na documentação TDN "[FAT0089 - Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)****", aba/índice "Parâmetros".**

**OBS:** Ao alterar a data de entrega o sistema altera também a data do vencimento dos títulos na Planilha financeira com base na informação da data de entrega 

**Saiba mais:**

**[MV\_TIPCPDT - Preenchimento da Data de Entrega na Cópia do Pedido de Venda](https://tdn.totvs.com/x/EwKLAw)**
