---
article_id: 13576975756823
category: RH - Rescisão
content_hash: 1eb71936c490d71433a210c674690b79df6bbba7a1e5f02e323b383369e589a3
fetched_at: '2026-06-28T22:43:50.823353+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que valor verba de falta com Sim IR lançada
  em rescisão não é abatido na base IR id 0015
type: support-article
updated_at: '2025-09-09T21:33:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13576975756823-RH-Linha-Protheus-GPE-Por-que-valor-verba-de-falta-com-Sim-IR-lan%C3%A7ada-em-rescis%C3%A3o-n%C3%A3o-%C3%A9-abatido-na-base-IR-id-0015
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34822434091031) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que valor verba de falta com Sim IR lançada em rescisão não é abatido em base IR id 0015?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**O valor de verba falta com Sim para IR não é abatido na base IR id 0015 em rescisão devido as incidências Ref Férias e Ref 13.

Caso a verba de falta esteja com Sim IR e Sim Ref Férias, o valor será abatido em base IR Férias e com Sim Ref 13 o valor será abatido em base IR 13 salário. Para o valor ser abatido na base IR id 0015, os campos Ref Férias e Ref 13 devem estar com Não, pois essa é uma verba de folha de pagamento.

Cadastro da verba, aba **Incidências**, caminho rotina **>Atualizações >Definição cálculo >Verbas:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13576874940823)

**Saiba mais**

[RH - Linha Protheus - GPE - Valor INSS 13º salário não é deduzido para a base de IR 13º salário em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550714-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-n%C3%A3o-%C3%A9-deduzido-para-a-base-de-IR-13%C2%BA-sal%C3%A1rio-em-rescis%C3%A3o?source=search)
