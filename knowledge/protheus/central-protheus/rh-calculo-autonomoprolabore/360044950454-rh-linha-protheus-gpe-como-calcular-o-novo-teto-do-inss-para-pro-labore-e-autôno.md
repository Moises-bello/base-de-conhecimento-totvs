---
article_id: 360044950454
category: RH - Calculo Autonomo/Prolabore
content_hash: a534b83df4b7ded81a6f4205e70b00bce929db20b6be991cd9ec67a01c06954b
fetched_at: '2026-06-28T22:43:15.125822+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular o novo teto do INSS para pro labore
  e autônomo
type: support-article
updated_at: '2025-04-15T17:43:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044950454-RH-Linha-Protheus-GPE-Como-calcular-o-novo-teto-do-INSS-para-pro-labore-e-aut%C3%B4nomo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25169825994903)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Como calcular o novo teto do INSS para pro labore e autônomo?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Deverá verificar o mnemônico **P\_PERCAUTO** em Atualizações > Definições de cálculo > Mnemônicos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27417773888407)

O percentual do desconto é controlado pelo mnemônico **P\_PERCAUTO**

O cálculo é da seguinte forma:

Tabela S001(INSS), campo “Sal.Contr. ate” \* percentual do campo **P\_PERCAUTO**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27417773892503)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27417743413015)**

**Exemplo:**

**P\_PERCAUTO = 0.11**

Tabela S001(INSS) campo “Sal.Contr. ate” = 7.786,02

7.786,02 \*11% = 856,46

**OBS**. O teto máximo do INSS para 2024 foi ajustado para R$ 7.786,02. Isso significa que, independentemente do valor do salário, a contribuição será calculada com base nesse limite máximo.

**Para os autônomos e Pro labores não será usado a tabela progressiva.**

**Saiba Mais**

[RH - Linha Protheus - GPE - Cálculo de INSS para Autônomos e Pro-Labores - Emenda Constitucional Nº 103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042817594-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-INSS-para-Aut%C3%B4nomos-e-Pro-Labores-Emenda-Constitucional-N%C2%BA-103)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=525805955>

<https://tdn.totvs.com/pages/releaseview.action?pageId=531017649>

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
