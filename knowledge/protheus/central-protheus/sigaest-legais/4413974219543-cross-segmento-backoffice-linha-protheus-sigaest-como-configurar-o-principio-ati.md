---
article_id: 4413974219543
category: SIGAEST - LEGAIS
content_hash: 54dc6bfc0af0a46323a877413cff00e77d6ebf735c4c0ef6e2a1c8d4924d9d4e
fetched_at: '2026-06-28T22:38:51.620389+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar o
  Principio Ativo do Produto dentro do Registro de Medicamentos (MATR924)?
type: support-article
updated_at: '2021-11-24T14:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413974219543-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-Principio-Ativo-do-Produto-dentro-do-Registro-de-Medicamentos-MATR924
---

**Dúvida**Trabalho com produtos que são medicamentos, esses produtos tem o Principio Ativo, que preciso que seja impresso no MATR924, como configurar ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para esse cenário, recomendamos a seguinte configuração:

1. Ajustar o Parâmetro MV\_PRATIVO = B5\_CEME:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413974153623/mceclip0.png)

O campo B5\_CEME é um campo da tabela de dados adicionais do produto, após configurar esse campo como conteúdo do parâmetro MV\_PRATIVO ao extrair o relatório MATR924 essa informação será apresentada conforme pode verificar abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414002172567/mceclip1.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios Legais](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
