---
article_id: 18297841898775
category: RH - Rescisão
content_hash: 2fc036f21133a3bb8968dc62ce23ad91acfa40a9f5f810f519400bf3ab8bb336
fetched_at: '2026-06-28T22:43:54.439461+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão complementar sem ser por dissídio calcula
  indevidamente diferença saldo de salário
type: support-article
updated_at: '2025-05-21T11:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18297841898775-RH-Linha-Protheus-GPE-Rescis%C3%A3o-complementar-sem-ser-por-diss%C3%ADdio-calcula-indevidamente-diferen%C3%A7a-saldo-de-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18297885370263) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que rescisão complementar sem ser por dissídio calcula indevidamente diferença saldo de salário?]  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A rescisão complementar sem ser por dissídio calcula indevidamente diferença de saldo de salário, geralmente pela mudança do conteúdo mnemônico P\_DIASRES. Para ambas rescisões o mnemônico deve conter o mesmo conteúdo.

**Exemplo:**

**Rescisão original em 02.2023**

**P\_DIASRES = 2**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18297605899159)

**Salário 2.000,00**

**Demissão em 10.02.2023.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18297616702359)

**2.000,00 \ 30 \* 10 = 666,67.**

**Em 03.2023, cálculo rescisão complementar sem ser por dissídio para pagamento de hora extra.**

**P\_DIASRES = 1**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18297701826199)

**Rescisão complementar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18297695655319)

Com o mnemônico P\_DIASRES = 1, a divisão saldo de salário é por dias mês, assim o valor saldo de salário fica desta forma: 2.000,00 \ 28 \* 10 = 714,28. Deste modo o sistema subtrai ao valor pago em rescisão original e apresenta a diferença em rescisão complementar: 714,28 - 666,67 = 47,62.

**Saiba mais**  
Para adquirir maior conhecimento acesse o *link* abaixo

[RH - Linha Protheus - GPE - Como calcular rescisão de acordo com os dias do mês ou sempre por 30 (divisão salário) (P\_DIASRES)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315674-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-acordo-com-os-dias-do-m%C3%AAs-ou-sempre-por-30-divis%C3%A3o-sal%C3%A1rio-P-DIASRES-?source=search)
