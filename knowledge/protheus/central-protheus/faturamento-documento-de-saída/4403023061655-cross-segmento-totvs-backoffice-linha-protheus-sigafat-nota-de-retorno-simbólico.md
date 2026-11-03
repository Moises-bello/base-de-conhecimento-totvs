---
article_id: 4403023061655
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 304969ba122548d3764052e53ce66623744d4969c51e1601278416a278de4f2f
fetched_at: '2026-06-28T22:38:43.891748+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota de retorno
  Simbólico no Faturamento
type: support-article
updated_at: '2021-06-21T18:58:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023061655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-de-retorno-Simb%C3%B3lico-no-Faturamento
---

**Dúvida**Como efetuar uma nota de retorno simbólico no módulo Faturamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

No módulo de faturamento, uma nota de retorno simbólico é para efetuar a devolução de um item em **beneficiamento** para que possa dar baixa no **saldo de poder de terceiros**, na tabela **SB6**.

Exemplo: Uma nota de entrada (**MATA103**) do tipo B , com  movimentando estoque e poder de terceiros remessa. E precisa retornar o saldo de poder de terceiros, onde será dado baixa no saldo da tabela SB6, mas não vai movimentar estoque, por que o cliente ficará com o produto.

Neste caso, é efetuado um pedido (**MATA410**) do tipo N, uma tes que trata poder de terceiros devolução, assim, o saldo do estoque (**SB2**) não é alterado, mas é baixado o saldo de poder de terceiros (**SB6**). Após gerar o pedido, basta faturar a nota.

**Documento de entrada :**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403022827671/mceclip0.png)

Veja que na nota de entrada demonstra o código da movimentação de terceiros:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403019453079/mceclip1.png)

**Pedido de Vendas:**

![Pedido_de_retorno_P3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4403019598231/Pedido_de_retorno_P3.gif)

**Nota Saída Gerada Para Retorno Simbólico:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403019607703/mceclip2.png)

**Saldo de Poder de Terceiros:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403022935319/mceclip3.png)

**Saiba Mais sobre outros tipos de retorno de poder de terceiros: [FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/pages/viewpage.action?pageId=446701767#FAT0285-PoderDE/EMTerceiro-RNRF)**
