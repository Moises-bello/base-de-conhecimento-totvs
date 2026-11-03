---
article_id: 39581236482071
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 500eb4f676a186b6176a18fac92a4b17ed4e35cd58dc9934cfbcbdc4954aecc3
fetched_at: '2026-06-28T22:38:58.499076+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Grupo I80 Rastreabilidade
  de Produtos(NT 2016.002)
type: support-article
updated_at: '2026-04-07T19:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39581236482071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Grupo-I80-Rastreabilidade-de-Produtos-NT-2016-002
---

A NT 2016.002 determina que o campo qLote na NF-e deve informar a quantidade do lote vinculada à operação, não a produção total. Não há obrigatoriedade de informar a produção total do lote no XML da NF-e. A soma das quantidades dos lotes deve ser igual à quantidade comercial (qCom). Exemplo: se o lote tem 10.000 unidades e vende 100, qCom e qLote devem ser 100.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39581230259863) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como preencher corretamente na NF-e as informações referentes ao lote fabricado pelo fornecedor e a quantidade comercializada, e se há obrigatoriedade de informar a quantidade total produzida no lote?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução** 

A **NT 2016.002** estabelece que o campo de quantidade do lote (`qLote`) representa a quantidade de itens daquele lote que estão vinculados à operação documentada na NF-e, **e não a produção total do lote pelo fornecedor****.**

A norma não prevê, de forma expressa, a obrigatoriedade de informar a quantidade total produzida do lote nos campos estruturados do XML. Dessa forma, qualquer informação relacionada à produção total pode ser tratada de forma complementar, como na descrição do produto ou em documentos auxiliares, não sendo padronizada na estrutura da NF-e. Assim, sua utilização pode ser considerada facultativa sob a ótica fiscal.

Adicionalmente, a soma das quantidades informadas nos lotes deve corresponder obrigatoriamente à quantidade comercial da nota fiscal (`qCom`). O cenário em que o fornecedor informa, nos campos estruturados, uma quantidade de lote superior à quantidade comercial não está aderente ao conceito da norma. O grupo de rastreabilidade da NF-e (Grupo I80) tem como objetivo garantir a rastreabilidade dos itens efetivamente transacionados, e não refletir a produção total do lote fabricante.

* Identifique a quantidade efetivamente comercializada na operação.
* Informe esta quantidade no campo referente à quantidade comercial (`qCom`).
* Informe a mesma quantidade no campo de quantidade do lote (`qLote`), refletindo apenas os itens transacionados nesta nota.
* Garanta que a soma das quantidades informadas nos lotes (caso o produto seja composto por múltiplos lotes) seja exatamente igual à quantidade comercial total da nota fiscal.

**Exemplo prático**: Se o fornecedor produziu 10.000 unidades em um lote, mas está vendendo apenas 100 unidades, a NF-e deve refletir qCom = 100 e qLote = 100. A produção total do lote não compõe os campos estruturados da NF-e.

**Saiba Mais**

[*NF-e - NT 2016.002 - Grupo 180 Rastreabilidade de Produtos*](https://tdn.totvs.com.br/display/public/ConSeg/NF-e+-+NT+2016.002+-+Grupo+180+Rastreabilidade+de+Produtos)
