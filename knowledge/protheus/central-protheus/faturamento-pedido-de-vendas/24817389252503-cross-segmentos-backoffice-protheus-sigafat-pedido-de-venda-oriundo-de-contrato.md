---
article_id: 24817389252503
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3085ed5e3eff6eb7ee49868ad9d64d0375d0088b25978f8e6ee345851e63f9b5
fetched_at: '2026-06-28T22:38:39.942943+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de venda oriundo de
  contrato (SIGAGCT) tem campos bloqueados
type: support-article
updated_at: '2026-04-02T14:56:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24817389252503-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-venda-oriundo-de-contrato-SIGAGCT-tem-campos-bloqueados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24817389198615) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Por que pedidos de venda oriundos de contratos (SIGAGCT) tem campos bloqueados?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

Conforme a legislação, foram permitidos a alteração de apenas alguns campos, quando um pedido de venda é oriundo de um contrato com todas as regras já determinadas, não podendo ser alteradas, pois tudo já foi definido na etapa do contrato, segue exemplos de alguns campos que podem ser alterados:

![](https://totvssuporte.zendesk.com/attachments/token/En6yuyEgURhbHrCguG9xLnAnX/?name=image.png)  
  
Os demais campos (Exemplos: C6\_ABATMAT e C6\_ABATISS), são campos dos quais foram avaliados que não são obrigatórias suas alterações.

Alguns campos são permitidos alterações por padrão, pois se entende que não tem como determiná-los exatamente no momento da firmação do contrato pré-pedido de venda.

**Caso precise alterar ainda assim existem as opções:**

* Refazer contrato no SIGAGCT para que o pedido de venda seja gerado com as informações corretas pré-acordadas no contrato
* Usar o ponto de entrada do saiba mais (no final dessa documentação)

**Saiba mais:**

[CN121PED - Tratamento especifico antes da geração do pedido de compra ou venda](https://tdn.totvs.com/x/3QMtE)
