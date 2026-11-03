---
article_id: 1500008498982
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: fbd421178654cc7971bd793a25ec9f033024272178e989f064b0f62e7ee1a3bd
fetched_at: '2026-06-28T22:38:52.716829+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro na função A280CRETRB
  ao instalar Stored Procedure
type: support-article
updated_at: '2025-03-12T12:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008498982-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-na-fun%C3%A7%C3%A3o-A280CRETRB-ao-instalar-Stored-Procedure
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504309678487)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Ao instalar Stored Procedure (SP), principalmente a 17 (Virada de Saldos) ocorre o seguinte error.log:

"*THREAD ERROR. InterFunctionCall: cannot find function A280CRETRB in AppMap on CFG051PROC (CFGX051.PRW)*". O que fazer para resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Para corrigir este erro, basta aplicar as atualizações do módulo:

* **[Pacotes de Atualização - Estoque e Custos e Automação e Coleta de Dados](https://tdn.totvs.com/x/2hgdHw)**

**Observação**: sempre aplicar atualizações primeiramente em ambiente de **homologação**.

Após aplicar, reinstalar a Procedure que estava ocasionando o error.log novamente para que sua inclusão seja feita com sucesso. Saiba mais: **[Procedure Desatualizada e Incompatível, quais as diferenças? É possível utilizar as rotinas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas)**

**Saiba mais:**

[Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

*[Clique aqui e veja mais artigos sobre Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)*
