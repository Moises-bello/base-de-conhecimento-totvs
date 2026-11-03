---
article_id: 8688796094871
category: Materiais - Compras (SIGACOM)
content_hash: 30b12c578dc97580ab75da8340e003fe3cf77914ea4ad9ee5e3c7591d00b12ad
fetched_at: '2026-06-28T22:41:11.620349+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Documento de
  Entrada - Desconto E4_DESCFIN
type: support-article
updated_at: '2022-09-06T18:24:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8688796094871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Documento-de-Entrada-Desconto-E4-DESCFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02**min** **Dúvida**

Porque a rotina de Documento de Entrada (MATA103) não acata o desconto informado na Condição de Pagamento no campo E4\_DESCFIN para os títulos gerados no módulo Financeiro?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Devido ao Cadastro de Condição de Pagamento ser compartilhado entre outros módulos além de Compras, existem campos específicos na tabela SE4 para alguns módulos. O campo "Desconto Financeiro" (E4\_DESCFIN) é utilizado no módulo de Faturamento. Ao utilizar uma Condição de Pagamento com este campo preenchido em um Documento de Entrada, não será gerado nenhum desconto nas duplicatas do fornecedor.

Sendo assim, os valores informados no campo não tem efeito no módulo de Compras, e este é o comportamento esperado.

**Saiba mais em :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
