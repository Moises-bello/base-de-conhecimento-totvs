---
article_id: 360019724912
category: RH - Rescisão
content_hash: 052f48ce621902abd80015082cbc0c1c79e9ceceb8d7262aaec015fbacbdda79
fetched_at: '2026-06-28T22:43:52.007398+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular verba de Aviso Trabalhado na Rescisão
type: support-article
updated_at: '2025-06-16T17:52:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019724912-RH-Linha-Protheus-GPE-Como-calcular-verba-de-Aviso-Trabalhado-na-Rescis%C3%A3o
---

**Dúvida**Ao calcular rescisão, como fazer com que seja calculada a verba de Aviso Trabalhado (ID 0112)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Quando o aviso do funcionário for trabalhado, o sistema pode pagar esse valor na verba de saldo salário – Id 0048 ou na verba de aviso prévio trabalhado – Id 0112.

O identificador 0112 foi criado para diferenciar o valor pago referente a dias trabalhados normais e dias trabalhados sobre aviso.

O mesmo é gerado sob a condição do tipo de aviso ser trabalhado e a coluna “saldo sal” estiver igual a N, essas definições são feitas na tabela S043 – Tipo de Rescisão.

Então fica a critério do cliente configurar o tipo de rescisão utilizado para demonstrar esse valor na verba de saldo salário ou aviso prévio trabalhado.
