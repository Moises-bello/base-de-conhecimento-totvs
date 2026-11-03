---
article_id: 20701971470615
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3f1c3fde5554370ce78fe98c0b21653ea09fa31f158c5c2b08f8b46893547d8a
fetched_at: '2026-06-28T22:38:39.607318+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Orçamento não reabre
  após exclusão de pedido de venda por ele gerado
type: support-article
updated_at: '2024-01-19T16:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20701971470615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Or%C3%A7amento-n%C3%A3o-reabre-ap%C3%B3s-exclus%C3%A3o-de-pedido-de-venda-por-ele-gerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20701996168855) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Orçamento não reabre após exclusão de pedido de venda por ele gerado, como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

No final do processo de venda, a partir de um **Orçamento de Venda (MATA415)**, ocorre a **Aprovação de Venda (MATA416)**, gerando um **Pedido de Venda (MATA410)**. Para mais detalhes do processo, consulte: [Aprovação de Vendas (MATA416)](https://tdn.totvs.com/x/UzJxIQ)

Com a conclusão do processo, o Orçamento que deu origem ao pedido de vendas assume o Status B (Legenda Vermelha): Orçamento Baixado.

O Status B (Legenda Vermelha), Orçamento Baixado, não pode ser revertido, ainda que seja realizada a exclusão do Pedido de Vendas (MATA410), pois trata-se de uma regra de negociação.

Uma vez que o Pedido de Vendas foi gerado, o valor e as condições da venda são exclusivos deste pedido, caso este seja excluído, entende-se que a negociação não vale mais e, por isso, deve ser gerada uma nova negociação com a inclusão de um novo Orçamento de Venda (MATA415). Este conceito precede de versões anteriores a versão 11.

É possível realizar a cópia do Orçamento de Venda encerrado, caso queira manter as mesmas características.

Caso necessite realizar um tratamento customizado na exclusão do Pedido de Vendas (MATA410), avalie a possibilidade de uso de um dos pontos de entrada abaixo:

* MA410DEL - Executado antes de deletar registro no SC5: https://tdn.totvs.com/x/DIVn
* A410EXC - Exclusão do pedido de vendas: <https://tdn.totvs.com/x/IoRn>
* MTA410E - Executado após deletar o registro no SC6: https://tdn.totvs.com/x/hoVn

**Saiba mais:**

[Orçamento de Venda (MATA415) não reabre após exclusão do Pedido de Venda (MATA410)](https://tdn.totvs.com/x/tPSRDg)
