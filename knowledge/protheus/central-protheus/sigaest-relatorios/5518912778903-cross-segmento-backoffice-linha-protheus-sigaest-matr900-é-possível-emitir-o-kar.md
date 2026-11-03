---
article_id: 5518912778903
category: SIGAEST - RELATORIOS
content_hash: 3e8fe2d01605573f0c243dea9d3e7c67203511a7994f928fdcb3f5eadc0a1e22
fetched_at: '2026-06-28T22:39:06.162491+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - É possível
  emitir o Kardex de armazéns bloqueados?
type: support-article
updated_at: '2022-04-18T14:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5518912778903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-%C3%89-poss%C3%ADvel-emitir-o-Kardex-de-armaz%C3%A9ns-bloqueados
---

**Dúvida**É possível emitir um Kardex para consulta das movimentações de armazéns bloqueados?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**No Protheus, as Consultas ao Produto (MATC050) e Consulta ao Kardex (MATC030), por padrão das Consultas, fazem validação da disponibilidade do Armazém para gerar as consultas. Portanto, com armazéns bloqueados na filtragem de consulta, retornará o Help REGBLOQ com bloqueio na tabela NNR. Portanto, a alternativa seria emitir o Relatório Kardex por Período (MATR900), onde, independentemente do filtro de armazém, o fonte valida e traz as movimentações de todos os armazéns independentemente do seu status.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
