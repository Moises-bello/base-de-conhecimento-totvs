---
article_id: 360058656174
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 618033de22da91d4dd0f975f67335d028a51359dc063f5e95c8c445f9c821e26
fetched_at: '2026-06-28T22:39:44.389518+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Modificação E2_EMIS1
type: support-article
updated_at: '2022-06-01T21:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058656174-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Modifica%C3%A7%C3%A3o-E2-EMIS1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Quando modificamos algum valor na importação o campo E2\_EMIS1 é modificado no financeiro com a data base do sistema.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Export Control – Todas versões.

**Solução**

Por regra do módulo de Comex o título no financeiro sempre será recriado ao modificar algum valor que tenha impacto direto no câmbio, assim o campo E2\_EMIS1 sempre irá considerar a *database* do sistema no momento da recriação.

Caso a contabilização seja realizado baseado neste campo, sugerimos modificar para algum campo confiável que não seja modificado no momento de regerar o título ou utilizar algum ponto de entrada para modificar este comportamento.
