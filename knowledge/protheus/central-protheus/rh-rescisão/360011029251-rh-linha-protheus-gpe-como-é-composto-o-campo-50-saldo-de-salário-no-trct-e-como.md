---
article_id: 360011029251
category: RH - Rescisão
content_hash: cd8edf1f74b15ab8be369f9835a5a3290018ac89ac894c91cd5b54eb2a106fac
fetched_at: '2026-06-28T22:43:48.650172+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como é composto o campo 50 (Saldo de Salário) no
  TRCT e como abater as Faltas do mesmo
type: support-article
updated_at: '2025-04-16T18:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011029251-RH-Linha-Protheus-GPE-Como-%C3%A9-composto-o-campo-50-Saldo-de-Sal%C3%A1rio-no-TRCT-e-como-abater-as-Faltas-do-mesmo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26561077067799)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como é composto o campo 50 (Saldo de Salário) no TRCT e como abater as Faltas do mesmo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**50 - **Saldo de Salário**:

Será impressa a verba com identificador de cálculo 0048 (Saldo de Salário), porém se o parâmetro "Comp. Cpo 50" no pergunte da impressão estiver preenchido, as verbas de faltas serão deduzidas. Caso não haja saldo para a dedução serão deduzidas tantas quanto forem possíveis, o campo Saldo de Salário ficará zerado e o restante das faltas lançadas em outros descontos. Se o parâmetro "Comp. Cpo 50" não estiver preenchido, no campo 50 será impresso apenas o saldo de salário calculado na rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26561077071127)

Para que seja abatido a Falta, a verba em questão deve possuir o identificador de Cálculo 0054 - Faltas, e o tipo da verba deve ser "Dias".

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
