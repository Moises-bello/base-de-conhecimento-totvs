---
article_id: 4402308733591
category: RH - Rescisão
content_hash: 9f7f38e97689355028a99f99e63443eea34a7b646a123eaf951cd008f405d054
fetched_at: '2026-06-28T22:43:49.864382+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que cálculo de rescisão gera ID 0292 (FGTS
  a recuperar Rescisão)
type: support-article
updated_at: '2025-08-20T20:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402308733591-RH-Linha-Protheus-GPE-Por-que-c%C3%A1lculo-de-rescis%C3%A3o-gera-ID-0292-FGTS-a-recuperar-Rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34327590223511)Tempo aproximado para leitura: 01:30 min****Dúvida**Por que cálculo de rescisão gera ID 0292 (FGTS a recuperar Rescisão)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A Geração do ID 0292 (FGTS a recuperar Rescisão) se dá quando existe recolhimento a maior de FGTS em meses anteriores ao cálculo da rescisão.  
  
**Exemplo:**Um funcionário sai de férias em Janeiro e solicita adiantamento da 1ª Parcela do 13º salário. No mês de Fevereiro esse funcionário pede demissão, com isso acabou recolhendo a maior o FGTS referente ao 13º antecipado.

**Exemplo:**

**Cadastro ID 0292.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18879397988503)**

**Cálculo roteiro 131 01.1023.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18879166800023)**

**Rescisão pedido de demissão em 02.2023.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18879166806679)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18879145886743)**

**1.000,00 \* 8% = 80,00 (FGTS 13 roteiro 131)**

**333,33 \* 8% = 26,67 (FGTS 13 rescisão)**

**80,00 - 26,67 = 53,33 valor ID 0292**

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
