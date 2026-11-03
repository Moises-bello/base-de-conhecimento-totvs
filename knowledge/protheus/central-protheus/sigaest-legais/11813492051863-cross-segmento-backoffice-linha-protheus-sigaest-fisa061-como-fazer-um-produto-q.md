---
article_id: 11813492051863
category: SIGAEST - LEGAIS
content_hash: 43d39a157526a16438becdcdc3ac0e0fc9c2a022a591495c0e1c5cb8aacafc28
fetched_at: '2026-06-28T22:38:51.678193+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FISA061 - Como fazer
  um produto que deixou de ser importado pare de gerar SA8?
type: support-article
updated_at: '2023-01-20T18:12:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11813492051863-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FISA061-Como-fazer-um-produto-que-deixou-de-ser-importado-pare-de-gerar-SA8
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:37 min** **Dúvida**Ao possuir produtos que outrora foram adquiridos através de operação de importação, mas que atualmente são adquiridos no mercado nacional, como tratar para que o FCI deixe de gerar parcela importada?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Implementado tratamento para considerar os valores de VI (Valor da Parcela Importada)e Quantidade se a data da última compra do componente considerando o campo de "Situação Tributaria(D1\_CLASFIS)" ou não de acordo com o parâmetro "MV\_FCIPERI".

| **Nome de Var.** | MV\_FCIPERI |
| --- | --- |

| Tipo | Caracter |
| **Cont. Por** | F |
| Descrição | U = Padrão / F = Considera operação nacional |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
