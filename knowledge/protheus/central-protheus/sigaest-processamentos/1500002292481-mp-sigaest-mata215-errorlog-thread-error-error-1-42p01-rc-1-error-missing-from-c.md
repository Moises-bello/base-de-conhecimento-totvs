---
article_id: 1500002292481
category: SIGAEST - PROCESSAMENTOS
content_hash: f77e973c412e8c86c031f4de14d3d79a9df6a0453b05b666e5216b87e5133f42
fetched_at: '2026-06-28T22:39:05.014580+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'MP - SIGAEST - MATA215 - Error.log THREAD ERROR  : Error : 1 (42P01) (RC=-1)
  - ERROR: missing FROM-clause entry for table "sc2"'
type: support-article
updated_at: '2021-05-10T17:06:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002292481-MP-SIGAEST-MATA215-Error-log-THREAD-ERROR-Error-1-42P01-RC-1-ERROR-missing-FROM-clause-entry-for-table-sc2
---

**Dúvida**

Ao executar a Rotina de Refaz Empenhos (MATA215) ocorre o seguinte error.log:

*THREAD ERROR -*

*: Error : 1 (42P01) (RC=-1) - ERROR: missing FROM-clause entry for table "sc2".*

Como resolver este problema?

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.23

**Solução**

Para resolver este problema, aplique o pacote acumulado do módulo Estoque/Custos:

**Pacote acumulado Estoque/Custos:**

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

**Observação**: Sempre aplicar o pacote primeiramente em ambiente de homologação. Em caso de sucesso, aplicar em ambiente de produção.

Após a aplicação, basta executar novamente a rotina Refaz Acumulados (MATA215) para que sua execução seja concluída com sucesso.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)*
