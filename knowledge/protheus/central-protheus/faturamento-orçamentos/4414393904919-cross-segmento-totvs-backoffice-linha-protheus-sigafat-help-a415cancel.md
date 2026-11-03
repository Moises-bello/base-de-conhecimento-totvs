---
article_id: 4414393904919
category: Faturamento - Orçamentos
content_hash: 76b2f2bf1ddddf93177d1dd8b9da9ef711d39c704b5135b48ba930db9ee27857
fetched_at: '2026-06-28T22:38:24.945780+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFAT - Help: A415CANCEL.'
type: support-article
updated_at: '2021-11-29T18:33:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414393904919-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A415CANCEL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min **Dúvida**Ao realizar o cancelamento de orçamento(MATA415), é apresentada a seguinte mensagem: A415CANCEL - O orçamento de venda não pode ser cancelado pois já foi baixado ou cancelado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414393737751/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

É necessário verificar se o orçamento foi cancelado ou realmente foi baixado, podendo ser feito pelo conteúdo do campo **CJ\_STATUS** desse orçamento.  
  
**- Status B (Legenda Vermelha):** Orçamento Baixado - Indica que a venda já foi aprovada através da rotina Aprovações de Venda (MATA416), ou seja, o Orçamento já foi transformado em Pedido de Venda (MATA410). Após a geração do Pedido, não será possível reabrir o Orçamento de Venda, saiba mais em: <https://tdn.totvs.com/x/tPSRDg>

**- Status C (Legenda Preta):** Orçamento Cancelado - Indica que houve cancelamento deste Orçamento, este cancelamento pode ocorrer de forma Manual (Outras Ações > Cancelar) ou Automática (Parâmetro MV\_ORCVLD);

O Status B (Legenda Vermelha), Orçamento Baixado, não pode ser revertido, ainda que seja realizada a exclusão do Pedido de Vendas (MATA410), pois trata-se de uma regra de negociação.

Uma vez que o Pedido de Vendas foi gerado, o valor e as condições da venda são exclusivos deste pedido, caso este seja excluído, entende-se que a negociação não vale mais e, por isso, deve ser gerada uma nova negociação com a inclusão de um novo Orçamento de Venda (MATA415). Este conceito precede de versões anteriores a versão 11.

É possível realizar a cópia do Orçamento de Venda encerrado, caso queira manter as mesmas características.
