---
article_id: 10562595895447
category: RH - Rescisão
content_hash: 356283aca06af147ee8dfb06177b5bce1c60aaa46f78c64434eddf2980d240c9
fetched_at: '2026-06-28T22:43:48.402039+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Por que INSS 13 salário rescisão complementar
  por dissídio não é abatido em base IR 13 salário
type: support-article
updated_at: '2025-09-11T00:53:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10562595895447-RH-Linha-Protheus-GPE-Por-que-INSS-13-sal%C3%A1rio-rescis%C3%A3o-complementar-por-diss%C3%ADdio-n%C3%A3o-%C3%A9-abatido-em-base-IR-13-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34856722084759) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que INSS 13 salário rescisão complementar por dissídio não é abatido em base IR 13 salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.1.25  
  
**Solução**O valor de INSS 13 salário em rescisão complementar por dissídio não é abatido em base IR 13 salário, devido a configuração das verbas. Em rescisão original é calculado INSS 13 salário Id 0070 e este Id estando com Sim para IR e Sim Ref 13, o valor é abatido em base IR 13 salário rescisão original.

Em rescisão complementar por dissídio a diferença de INSS 13 salário é calculada no Id 0401, deste modo o Id 0401 ou o Id 0169 devem estar com Sim IR 13 salário e sim Ref 13 para devido abatimento em base IR 13 salário.

**Saiba mais**

[RH - Linha Protheus - GPE - Valor INSS 13º salário não é deduzido para a base de IR 13º salário em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550714-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-n%C3%A3o-%C3%A9-deduzido-para-a-base-de-IR-13%C2%BA-sal%C3%A1rio-em-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Em cálculo de rescisão complementar, sistema considera para base de IR 13º Salário o valor já pago na rescisão original mais o valor pago na rescisão complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945351-RH-Linha-Protheus-GPE-Em-c%C3%A1lculo-de-rescis%C3%A3o-complementar-sistema-considera-para-base-de-IR-13%C2%BA-Sal%C3%A1rio-o-valor-j%C3%A1-pago-na-rescis%C3%A3o-original-mais-o-valor-pago-na-rescis%C3%A3o-complementar?source=search)
