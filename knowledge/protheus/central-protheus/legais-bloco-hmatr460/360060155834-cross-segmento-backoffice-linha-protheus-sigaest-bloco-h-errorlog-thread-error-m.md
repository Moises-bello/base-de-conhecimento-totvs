---
article_id: 360060155834
category: LEGAIS - BLOCO H/MATR460
content_hash: 18d15548a30fb5b05331051c11b71b39560c23a707da96dde0d8ac8b8bf37f4c
fetched_at: '2026-06-28T22:42:15.012104+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco H - Error.log
  "THREAD ERROR  - [Microsoft][SQL Server Native Client 11.0][SQL Server]Lock request
  time out period exceeded."
type: support-article
updated_at: '2021-06-14T14:20:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060155834-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-H-Error-log-THREAD-ERROR-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-Lock-request-time-out-period-exceeded
---

**Dúvida**

Ao gerar o SPED com o Bloco H ocorre o seguinte error.log: *THREAD ERROR ([14620], Error : 1222 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Lock request time out period exceeded*. O que fazer para resolver?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para solucionar o problema, aplique os pacotes acumulados de Estoque e Livros Fiscais conforme a sua release.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

***Pacotes acumulados Livros Fiscais:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)

**Observação**: Sempre atualizar primeiramente em ambiente de homologação.

Após aplicar, efetue a validação gerando novamente o SPED com a pergunta "Gera inventário?" = Sim e "Data Inventário" = Data do inventário a ser gerada no Bloco H.

**Saiba mais:**

*[MP - SIGAEST - Como gerar o Bloco H do SPED Fiscal no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H)*
