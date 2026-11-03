---
article_id: 360052167734
category: RH - Rescisão
content_hash: 29d9f9c6dd194066171f95249f266d463e9039a5d8efdd9c52f1af77b5f52cb0
fetched_at: '2026-06-28T22:43:50.966880+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - Rescisão não gera desconto INSS mesmo quando o id 0048
  (provento saldo de salário) possui incidência Sim INSS
type: support-article
updated_at: '2025-09-08T18:45:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052167734-RH-Linha-Protheus-Rescis%C3%A3o-n%C3%A3o-gera-desconto-INSS-mesmo-quando-o-id-0048-provento-saldo-de-sal%C3%A1rio-possui-incid%C3%AAncia-Sim-INSS
---

**Dúvida**Por que rescisão não gera desconto INSS mesmo quando o ID 0048 (provento saldo de salário) possui incidência Sim INSS.?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O cálculo de rescisão possui lançamento de verba de desconto com incidência Sim para INSS, desta maneira caso o valor de desconto seja igual ou superior ao valor de provento (saldo de salário id 0048 por exemplo) o cálculo de rescisão não possui base para calcular o desconto de INSS.

**Exemplo 1:**

No cálculo a seguir a rescisão possui saldo de salário 30 dias e desconto de faltas 30 dias. Como a verba de desconto faltas possui incidência Sim para INSS, a base do encargo fica zerada e não calcula o desconto INSS.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083941914)

**Exemplo 2:**

Cálculo de rescisão pedido de demissão desconta aviso, não apresenta desconto INSS devido o Id 0113 (desconto aviso) está com Sim para INSS, deste modo o valor do desconto aviso é deduzido em base INSS.

**Cenário:**

Salário: 2.000,00

Saldo de salário rescisão 15 dias: 1.000,00 (2.000,00 \ 30 \* 15).

Com o desconto aviso prévio Id 0113 está com Sim INSS, o valor de 2.000,00 é deduzido da base INSS 1.000,00, assim não tendo cálculo de INSS.

**Cadastro Id 0113**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13753582016151)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13753584065559)**

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
