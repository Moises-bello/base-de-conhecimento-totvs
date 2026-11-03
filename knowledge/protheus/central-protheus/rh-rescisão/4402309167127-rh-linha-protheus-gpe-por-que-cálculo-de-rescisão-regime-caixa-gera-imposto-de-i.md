---
article_id: 4402309167127
category: RH - Rescisão
content_hash: 4c4ab92d81c9786e553f4c05117e8ef938986f0d793f6c14800e150d2f427225
fetched_at: '2026-06-28T22:43:53.535723+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que cálculo de rescisão regime caixa gera imposto
  de inferior a 10,00
type: support-article
updated_at: '2025-06-16T18:46:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402309167127-RH-Linha-Protheus-GPE-Por-que-c%C3%A1lculo-de-rescis%C3%A3o-regime-caixa-gera-imposto-de-inferior-a-10-00
---

**Dúvida**Por que cálculo de rescisão gera imposto de renda inferior a 10,00?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Em regime de pagamento caixa, para apuração do imposto de renda o sistema considera a base de IR mês anterior e desconto IR mês anterior, deste modo tendo um outro calculo no mesmo mês será somada a base IR mês anterior com a base IR atual, assim é encontrado o valor total IR e subtraído o IR anterior. Caso esta subtração seja inferior a 10,00 o sistema somente esta descontando a diferença do valor total imposto de renda.

**Exemplo:**

Base IR mês anterior: 2.296,57 (pagamento em 07.06.2021)

IR mês anterior: 29,44 (pagamento em 07.06.2021)

Base IR saldo de salário rescisão: 103,15 (pagamento em 08.06.2021).

Base Total IR: 2.296,57 + 103,15 = 2.399,72

2.399,72 \* 7,5% - 142,80 = 37,18 (valor total IR)

37,18 - 29,44 (IR já descontado em 07.06.2021) = 7,74 IR Rescisão

**Saiba mais:**Para adquirir mais conhecimento acesse o(s) link(s) abaixo:

[MP - GPE - Como conferir o valor de Imposto de Renda em rescisão para pagamento regime caixa, contendo IR pago quinto dia útil, IR adiantamento e IR rescisão.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051386673-MP-GPE-Como-conferir-o-valor-de-Imposto-de-Renda-em-rescis%C3%A3o-para-pagamento-regime-caixa-contendo-IR-pago-quinto-dia-%C3%BAtil-IR-adiantamento-e-IR-rescis%C3%A3o-?source=search)
