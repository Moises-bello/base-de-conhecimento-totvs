---
article_id: 7431764289559
category: RH - Rescisão
content_hash: 3bfe0f43861b0df925b66c0037574558d655bca262495b876730cb4974d89367
fetched_at: '2026-06-28T22:43:53.762241+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Qual o impacto de calcular rescisão original com
  o mnemônico P_DIASRES = 2 e calcular rescisão complementar por dissídio com o P_DIASRES
  = 1
type: support-article
updated_at: '2025-06-16T18:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7431764289559-RH-Linha-Protheus-GPE-Qual-o-impacto-de-calcular-rescis%C3%A3o-original-com-o-mnem%C3%B4nico-P-DIASRES-2-e-calcular-rescis%C3%A3o-complementar-por-diss%C3%ADdio-com-o-P-DIASRES-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o impacto de calcular rescisão original com o mnemônico P\_DIASRES = 2 e calcular rescisão complementar por dissídio com o P\_DIASRES = 1?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O P\_DIASRES determina a divisão quanto ao cálculo saldo de salário em rescisão, caso o parâmetro seja alterado entre o cálculo da rescisão original para a complementar, pode não ocorrer diferença quanto ao saldo de salário.

**Exemplo:**

**Rescisão original em 10.2021 Salário 8.499,99**

**P\_DIASRES = 2**

**8.499,99 \ 30 \* 19 = 5.383,33**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7431551880727/mceclip0.png)

**Rescisão complementar por dissídio em 02.2022 Salário 8.647,61**

**P\_DIASRES = 1**

**8.647,61 \ 31 \* 19 = 5.300,15**

**5.300,15 - 5.383,33 = -83,18**

**Deste modo em rescisão complementar por dissídio, o sistema não irá calcular diferença saldo de salário.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7431664539415/mceclip1.png)**

**Rescisão complementar por dissídio sem calcular a verba 161.**

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:

[RH - Linha Protheus - GPE - Como calcular rescisão de acordo com os dias do mês ou sempre por 30 (divisão salário) (P\_DIASRES)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315674-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-acordo-com-os-dias-do-m%C3%AAs-ou-sempre-por-30-divis%C3%A3o-sal%C3%A1rio-P-DIASRES-?source=search)
