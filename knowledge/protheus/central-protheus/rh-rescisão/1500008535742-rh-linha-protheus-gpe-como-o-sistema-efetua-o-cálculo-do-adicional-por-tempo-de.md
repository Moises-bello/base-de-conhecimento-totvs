---
article_id: 1500008535742
category: RH - Rescisão
content_hash: 0d2bbf6febde40e7bc6a9c1bdf90b50df746f4f6f4699ec82b4091f277b92ddc
fetched_at: '2026-06-28T22:43:49.542797+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema efetua o cálculo do adicional por
  tempo de serviço (ATS) sobre as verbas indenizatórias quando a base de cálculo é
  salário + verbas
type: support-article
updated_at: '2025-07-23T11:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008535742-RH-Linha-Protheus-GPE-Como-o-sistema-efetua-o-c%C3%A1lculo-do-adicional-por-tempo-de-servi%C3%A7o-ATS-sobre-as-verbas-indenizat%C3%B3rias-quando-a-base-de-c%C3%A1lculo-%C3%A9-sal%C3%A1rio-verbas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26625679592727)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como o sistema efetua o cálculo do adicional por tempo de serviço-ATS sobre as verbas indenizatórias quando a base de cálculo é salário + verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Este documento exemplifica a regra de cálculo do sistema para efetuar a apuração do adicional por tempo de serviço (**ATS**) sobre as verbas indenizatórias na rescisão quando o adicional é configurado com base de cálculo de **salário + verbas**.

Para solucionar essa dúvida, realize os seguintes passos:

**1. Cadastro do funcionário**É necessário que o funcionário recebe algum tipo de adicional por tempo de serviço entre anuênio, biênio, triênio, quadriênio e quinquênio e esteja vinculado a um sindicato que possua a configuração para cálculo do adicional por tempo de serviço.

Neste exemplo, o funcionário recebe salário mensal de R$ 2.000,00, recebe triênio e está vinculado ao sindicato 01:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012939541)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012939601)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012939621)

**2. Cadastro do sindicato**É necessário que o sindicato possua as configurações preenchidas para cálculo do adicional por tempo de serviço.

Neste exemplo, a base de cálculo é sobre salário + verbas e o triênio está configurado com percentual de 3%:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012939761)

**3. Cálculo da rescisão**Foi incluído uma verba em lançamentos por funcionário com incidência para ATS no valor de R$ 2.000.00:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012583082)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012939901)

Cálculo da rescisão:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012583522)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012940241)

Explicação do cálculo do adicional por tempo de serviço:

1. O sistema verifica qual é a base de cálculo do adicional por tempo de serviço. No caso, será o salário base + verbas que possuam incidência para ATS. No exemplo, a única verba que possui incidência para o ATS é a 013, então a base de cálculo é de R$ 2.000,00 (salário base) + R$ 2.000,00 (verba 013), que resulta em **R$ 4.000,00**. Como o triênio é de **3%**, o valor base para triênio de todas as verbas indenizatórias será de **R$ 120,00** (3% x R$ 4.000,00).
2. Para cada verba indenizatória será efetuado proporcionalização sobre o valor base conforme os dias ou avos de direito:  
   1. ATS Férias indenizadas: R$ 120,00 ÷ 12 X 12 = R$ 120,00.
   2. ATS Férias proporcionais: R$ 120,00 ÷ 12 X 4 = R$ 40,00.
   3. ATS Férias sobre aviso: R$ 120,00 ÷ 12 X 2 = R$ 20,00.
   4. ATS Sobre aviso prévio indenizado: R$ 120,00 ÷ 30 X 42 = R$ 168,00.
   5. ATS 13º salário indenizado: R$ 120,00 ÷ 12 X 4 = R$ 40,00.

**IMPORTANTE**  
A base de cálculo é única do ATS, ou seja, **NÃO**há diferenciação na base de cálculo para as férias indenizadas e para o 13º salário, por exemplo.

A apuração da base de cálculo do ATS ocorre antes da geração das verbas indenizatórias (tais como férias indenizadas, férias proporcionais e 13º salário) no roteiro da rescisão, ou seja, **NÃO** há possibilidade de realizar parametrização para que uma verba indenizatória entre na base de cálculo do ATS.

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
