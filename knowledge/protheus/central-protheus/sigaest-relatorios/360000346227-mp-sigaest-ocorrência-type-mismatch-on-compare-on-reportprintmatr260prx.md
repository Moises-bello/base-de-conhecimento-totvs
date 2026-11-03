---
article_id: 360000346227
category: SIGAEST - RELATORIOS
content_hash: 17c76133f9ae867388893146d7972126fd334b77cfc293ef04316ac738833ea2
fetched_at: '2026-06-28T22:39:06.268873+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: 'MP - SIGAEST - Ocorrência: type mismatch on compare  on REPORTPRINT(MATR260.PRX)'
type: support-article
updated_at: '2021-04-28T15:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000346227-MP-SIGAEST-Ocorr%C3%AAncia-type-mismatch-on-compare-on-REPORTPRINT-MATR260-PRX
---

**Dúvida**:

Ao executar o Relatório Posição de Estoque (MATR260) é exibico o error.log "**type mismatch on compare on** **REPORTPRINT(MATR260.PRX)**". O que fazer para resolver?

**Ambiente**

Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**:

Para a correção do erro, aplique o pacote Acumulado do módulo de Estoque/Custos:

***Pacotes acumulados Estoque/Custos:***

**12.1.27**- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **| 12.1.25**- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** **12.1.23**- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

**OBS:**Aplicar sempre primeiramente em ambiente de homologação. Em caso de sucesso, aplicar em ambiente de produção.

Em seguida, basta executar novamente o relatório que causou o error.log e notará que não será mais gerado o mesmo.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)*
