---
article_id: 360018334511
category: RH - Rescisão
content_hash: 47aad56a6885680fd2409bdb278c3869e8352e5268c368afb43da695b921ab15
fetched_at: '2026-06-28T22:43:48.641965+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar Tipo de Rescisões sem saldo de salário
  em caso de funcionário afastado que veio a falecer
type: support-article
updated_at: '2025-08-15T16:53:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018334511-RH-Linha-Protheus-GPE-Como-criar-Tipo-de-Rescis%C3%B5es-sem-saldo-de-sal%C3%A1rio-em-caso-de-funcion%C3%A1rio-afastado-que-veio-a-falecer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19226695613463) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como efetuar uma rescisão para um funcionário que estava em afastamento e veio a falecer, lançando data do afastamento diferente da data de rescisão, sem que o sistema considere saldo de salário?  
  
**Ambiente**

TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal – Todas as versões  
  
**Solução**1. Acesso o módulo Gestão de Pessoal  **Atualizações>Definições de cálculos> Manutenção Tabelas (GPEA320) >  tabela S043** selecionar **tipos de rescisões > Altera:**

2. Criar o novo tipo e preencher o campo saldo de salário com N de acordo com a necessidade para atender essa demanda:

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013583551)**

3. No lançamento de afastamento em **Atualizações > Lançamentos > Ausências (GPEA240)** deve ser inserido a data fim um dia anterior ao falecimento e a data da rescisão deverá ser a data exata que o funcionário faleceu, no tipo de rescisão selecione a nova opção cadastrada.  
  
**Saiba Mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como calcular rescisão por falecimento para funcionário afastado sem data fim afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051337993-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-por-falecimento-para-funcion%C3%A1rio-afastado-sem-data-fim-afastamento?source=search)

[RH - Linha Protheus - Como gerar rescisão por falecimento sem o pagamento do saldo de salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050973894-RH-Linha-Protheus-Como-gerar-rescis%C3%A3o-por-falecimento-sem-o-pagamento-do-saldo-de-sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Deve ser gerado GRRF quando a rescisão é por motivo de falecimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058398794-RH-Linha-Protheus-GPE-Deve-ser-gerado-GRRF-quando-a-rescis%C3%A3o-%C3%A9-por-motivo-de-falecimento?source=search)
