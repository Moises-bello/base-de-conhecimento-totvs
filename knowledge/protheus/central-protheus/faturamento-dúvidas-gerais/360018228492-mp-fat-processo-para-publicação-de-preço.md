---
article_id: 360018228492
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 36086c32a82f1010034f27cee0330062c41467ff3cd42f48a39f75c563d48cf4
fetched_at: '2026-06-28T22:38:31.331257+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Processo para publicação de Preço
type: support-article
updated_at: '2021-04-28T15:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018228492-MP-FAT-Processo-para-publica%C3%A7%C3%A3o-de-Pre%C3%A7o
---

**Dúvida**

Como efetuar a efetivação da publicação de preço?

**Ambiente**

Microsiga Protheus - a partir da versão 11.  
   
**Solução**

**Publicação de Preço**

Para que seja alterado uma tabela de preços no momento da efetivação de uma publicação, é necessário habilitar o parâmetro**MV\_LJCNVDA = (.T.)**

Se não for informado nenhuma tabela no momento da efetivação, será criado uma nova tabela com os itens da publicação.

**Importante:**

É necessário verificar se na tabela de preço, o produto está com a data vigência correta.

Pois se tiver em branco ou com data superior a data base, no momento da efetivação da publicação de preço, o sistema criará uma nova tabela.
