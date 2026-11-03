---
article_id: 360058143894
category: RH - Rescisão
content_hash: 9ecac234a02e4c40fc9d09f6f162fe488e492eb92060e2c2bf739c63effe6f93
fetched_at: '2026-06-28T22:43:51.070030+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular rescisão complementar é apresentado
  o log de ocorrência: Tabela de Imposto de Renda (Tabela S002) não cadastrada'
type: support-article
updated_at: '2025-06-16T17:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058143894-RH-Linha-Protheus-GPE-Ao-calcular-rescis%C3%A3o-complementar-%C3%A9-apresentado-o-log-de-ocorr%C3%AAncia-Tabela-de-Imposto-de-Renda-Tabela-S002-n%C3%A3o-cadastrada
---

**Dúvida**Por que ao calcular rescisão complementar é apresentado o log de ocorrência: Tabela de Imposto de Renda (Tabela S002) não cadastrada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O log é apresentado porque em tabela S002 não constam os dados referentes a competência da rescisão original.  
  
**Exemplo:**Rescisão original calculada em 01.2019. Ao calcular a rescisão complementar em 11.2020, o sistema apresenta o log.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100780953/mceclip0.png)

Em >Atualizações >Definições de Cálculo >Manutenção Tabelas >Tabela S002, deverá ser lançadas as informações referentes ao período da rescisão original.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100781013/mceclip1.png)
