---
article_id: 360058144434
category: RH - Rescisão
content_hash: 3c51b6d8dd50bd480f0981fc341bdd7883da2dc67b7c5bbcfe64de667e94cb14
fetched_at: '2026-06-28T22:43:51.072924+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular rescisão complementar é apresentado
  o log de ocorrência: Tabela de INSS (Tabela S001) não cadastrada'
type: support-article
updated_at: '2025-06-16T17:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058144434-RH-Linha-Protheus-GPE-Ao-calcular-rescis%C3%A3o-complementar-%C3%A9-apresentado-o-log-de-ocorr%C3%AAncia-Tabela-de-INSS-Tabela-S001-n%C3%A3o-cadastrada
---

**Dúvida**Por que ao calcular rescisão complementar é apresentado o log de ocorrência: Tabela de INSS (Tabela S001) não cadastrada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O log é apresentado porque em tabela S001 não constam os dados referentes a competência da rescisão original.  
  
**Exemplo:**Rescisão original calculada em 01.2019. Ao calcular a rescisão complementar em 11.2020, o sistema apresenta o log.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100781353/mceclip0.png)

Em **>Atualizações >Definições de Cálculo >Manutenção Tabelas >Tabela S001**, deverá ser lançadas as informações referentes ao período da rescisão original.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098537114/mceclip1.png)
