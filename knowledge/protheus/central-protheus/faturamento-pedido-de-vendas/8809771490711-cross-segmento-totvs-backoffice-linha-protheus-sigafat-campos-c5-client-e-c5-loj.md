---
article_id: 8809771490711
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 629ceedd062a190a798b838383a530e5cdd774ca27dda0ff71791407742a2211
fetched_at: '2026-06-28T22:38:38.659579+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat – Campos C5_CLIENT
  e C5_LOJAENT quando C5_TIPO = D/B
type: support-article
updated_at: '2022-09-12T18:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8809771490711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Campos-C5-CLIENT-e-C5-LOJAENT-quando-C5-TIPO-D-B
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**

Gostaria que ao utilizar o tipo D ou B de pedidos de vendas, os campos C5\_CLIENT e C5\_LOJAENT passassem a consultar a tabela SA2 - Fornecedores, mas estão sendo travados para inserção de valores.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat – Todas as versões

**Solução**

Por padrão, o sistema não faz essa validação, uma vez que o uso do fornecedor deve ser para uso para retorno de onde veio com C5\_TIPO = D (Devolução de Compras) ou complementar pontualmente um processo de poder de terceiros com C5\_TIPO = B (Utiliza Fornecedor).

**Exemplos:**

**C5\_TIPO = N/C/I/P**

É possível definir os campos C5\_CLIENT e C5\_LOJAENT para registros diferentes, devido a consulta na tabela SA1, por processos como Contrato de Parceria, onde é preciso que o cliente de entrega seja diferente do cliente de faturamento.

**C5\_TIPO = B/D**

Os campos por padrão vem travados para alteração quando é selecionado esses tipos (B ou D), como podemos ver nas validação desses campos:

Validação do campo C5\_CLIENT quando C5\_TIPO = D ou B, é travado nativamente:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8809692875671/mceclip0.png)

Validação do campo C5\_LOJAENT quando C5\_TIPO = D ou B, é travado nativamente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8809693074583/mceclip1.png)

Visualização no Protheus:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8809720455703/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8809698606999/mceclip3.png)
