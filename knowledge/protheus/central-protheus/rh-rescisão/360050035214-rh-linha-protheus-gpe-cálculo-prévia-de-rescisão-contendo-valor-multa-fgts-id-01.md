---
article_id: 360050035214
category: RH - Rescisão
content_hash: d2ad33ebd61c2e3faf97b3f2ec4a9c62c8e21e79f5cee947389ccefc6a028bc0
fetched_at: '2026-06-28T22:43:51.951166+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo Prévia de Rescisão contendo valor multa
  FGTS id 0120
type: support-article
updated_at: '2022-09-29T22:22:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050035214-RH-Linha-Protheus-GPE-C%C3%A1lculo-Pr%C3%A9via-de-Rescis%C3%A3o-contendo-valor-multa-FGTS-id-0120
---

**Dúvida**Cálculo Prévia de Rescisão contendo valor multa FGTS id 0120 com base no saldo total FGTS.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema possui a rotina de Manutenção de Saldos (GPEM360), sendo que ao simular cálculo da rescisão, o cálculo se baseia pelo mês atual da rotina Manutenção de Saldos para cálculo da multa total FGTS - identificador 0120.

Caso seja necessário simular cálculo de mês posterior ao da rotina Manutenção de saldos, é necessário lançar em rescisão o saldo total FGTS no id 0118, assim o valor da multa FGTS id 0120 será composto pelo valor FGTS rescisão e saldo.
