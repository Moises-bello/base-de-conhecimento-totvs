---
article_id: 360022410131
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 781a028abfc85007385e328aab7430a49bb85675e1d8cbc86c7fd899e4f9fc14
fetched_at: '2026-06-28T22:38:41.073172+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao aplicar
  desconto no Pedido de Vendas / Orçamento o sistema recalcula para outro valor/percentual
type: support-article
updated_at: '2024-09-23T19:52:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022410131-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-aplicar-desconto-no-Pedido-de-Vendas-Or%C3%A7amento-o-sistema-recalcula-para-outro-valor-percentual
---

**Dúvida**

Ao aplicar desconto no Pedido de Vendas / Orçamento o sistema recalcula para outro valor/percentual.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Solução**

Veja nosso vídeo How To sobre esse processo: [How To | MP - SIGAFAT - Arredondamento dos descontos](https://youtu.be/LBp4RszLjLE)

O percentual aplicado sempre será calculado proporcional ao valor do item e quantidade do item.

Este proporcional deve ser um valor comportado pelo tamanho de decimais da base senão, ocorrerá diferença no cálculo.

***Obs: Nativo do Protheus apenas uso de dois dígitos para o ambiente Faturamento, caso necessite alterar utilize os [Grupos de Campos Numéricos](https://youtu.be/BXPL4BPr668?si=Q_-ZXQtei4JMYyGe).***

Alternativas :

1 - Utilizar o campo de desconto:**Indenizacao (C5\_DESCONT)**.

2 - Aumentar as casas decimais de modo que comportem o resultado do cálculo pretendido.

Exemplo :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019335851)

**Saiba mais**: [Arredondamento no desconto do Pedido de Venda / Orçamento de Venda](https://tdn.totvs.com/x/aNVZE)
