---
article_id: 20166703694743
category: RH - Rescisão
content_hash: a2462b4b7782a138fb8021c7da0c289da4a9651c4b209ec287ac1fb86995438d
fetched_at: '2026-06-28T22:43:49.906360+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que rescisão calcula INSS 13º mesmo quando
  13º é quitado em roteiros 131 e 132
type: support-article
updated_at: '2023-12-28T14:19:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20166703694743-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-calcula-INSS-13%C2%BA-mesmo-quando-13%C2%BA-%C3%A9-quitado-em-roteiros-131-e-132
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20166703667095) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que rescisão calcula INSS 13º mesmo quando 13º é quitado em roteiros 131 e 132?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A rescisão calcula INSS 13º devido a base INSS rescisão 13º ser superior a base INSS 13º roteiro 132, deste modo é calculada apenas a diferença desconto INSS.

**Exemplo:**

**Cálculo roteiro 132.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20166744224407)

**Base INSS 13: 2.000,00**

**Desconto INSS 13 = 160,20**

**Rescisão.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20166744238231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20166703669527)

**Base INSS 13 = 2.000,00 + 166,67 = 2.166,67**

**Desconto INSS 13 = 175,20**

**175,20 - 160,20 = 15,00**

**Diferença INSS 13º verba 423 15,00.**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Configuração de verbas de desconto de 13º salário na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059185253-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-de-desconto-de-13%C2%BA-sal%C3%A1rio-na-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Por que rescisão calcula 13 proporcional ID 0114 mesmo quando todo 13 salário já é pago nos roteiros 131 e 132](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20053706957975-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-calcula-13-proporcional-ID-0114-mesmo-quando-todo-13-sal%C3%A1rio-j%C3%A1-%C3%A9-pago-nos-roteiros-131-e-132?source=search)

[RH - Linha Protheus - GPE - Valor ID 0247 desconto 13 segunda parcela em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20141090186519-RH-Linha-Protheus-GPE-Valor-ID-0247-desconto-13-segunda-parcela-em-rescis%C3%A3o?source=search)
