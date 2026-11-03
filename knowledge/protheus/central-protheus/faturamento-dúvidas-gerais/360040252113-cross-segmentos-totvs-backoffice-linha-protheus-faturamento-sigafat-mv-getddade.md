---
article_id: 360040252113
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4a772ed6868a3b67757c0ceea1eeac05fa78089d1b9034fd2fb8cc5816e9e228
fetched_at: '2026-06-28T22:38:29.911346+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - MV_GETDDADE e MV_GETDADL
type: support-article
updated_at: '2024-04-22T18:53:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040252113-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-MV-GETDDADE-e-MV-GETDADL
---

**Dúvida**

Ao incluir e editar a linha do pedido de venda (**MATA410)**, fica aparecendo a tela abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052773394/mceclip0.png)

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - todos as versões.

**Solução**

Basta clicar sobre a **label** produto, aparecerá uma caixinha de mensagem **Edição por célula**, clique sobre a mensagem, aí, voltará ao padrão, sem abrir a tela em questão, que é a de edição por linha.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053674373/mceclip2.png)

Obs. Para que não ocorra a alteração os parâmetros **MV\_GETDADE** igual a **2** e **MV\_GETDADL** como **.F.**,assim permanecerá por célula e sem mudança no menu.

As configurações do parâmetro **MV\_GETDADE** também atuam na rotina de Orçamento de Vendas (**MATA415**), portanto as mesmas regras informadas acima para aplicação do pedido de venda, também são tratadas na  aplicação no Orçamento de vendas .

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405471513367/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405471518999/mceclip1.png)
