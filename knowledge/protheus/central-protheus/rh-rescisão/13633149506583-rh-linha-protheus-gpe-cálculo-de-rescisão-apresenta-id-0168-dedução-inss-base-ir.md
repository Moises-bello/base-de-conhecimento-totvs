---
article_id: 13633149506583
category: RH - Rescisão
content_hash: 3a40ee190288852b5a00089d7126ddffac06ffeb34ff108b6a5d61af99e26d66
fetched_at: '2026-06-28T22:43:48.522064+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de rescisão apresenta Id 0168 (dedução
  INSS Base IR férias) em duplicidade
type: support-article
updated_at: '2025-09-09T21:33:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13633149506583-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-Id-0168-dedu%C3%A7%C3%A3o-INSS-Base-IR-f%C3%A9rias-em-duplicidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34822402293783) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Por que cálculo de rescisão apresenta Id 0168 (dedução INSS Base IR férias) em duplicidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**O cálculo de rescisão apresenta o Id 1068 em duplicidade devido os valores integrados roteiro FER e os valores calculados em rescisão, assim o cálculo apresenta o Id duas vezes, um lançamento com origem K (férias) e outro com origem R (rescisão).

**Exemplo:**

**Cálculo férias de 01.04.2023 a 20.04.2023**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633033511959)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633050678551)

**Id 0168 verba 754**

**Integrado FER e calculada rescisão em 22.04.2023**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633053137943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633053908503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633038527383)

**464,15 + 3094,35 + 1031,45 ( salário 2 dias mais férias 20 dias mais 1\3 férias) = 4590,05**  
  
**4589,95 = INSS 468,78**  
  
**Conferência INSS rescisão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13633074215447)

Como demonstrado a rescisão apresenta a verba 754 Id 0168 origem K (integrada roteiro FER) valor de 403,79 e a rescisão apresenta a mesma verba 754 Id 0168 origem R (calculada rescisão) valor de 17,57, assim a soma dos dois lançamentos totalizam no desconto INSS férias e rescisão.

**Saiba mais**

[RH - Linha Protheus - GPE - Como conferir INSS salário e INSS férias em cálculo de folha de pagamento com o parâmetro MV\_DINSSFM = N](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008686801-RH-Linha-Protheus-GPE-Como-conferir-INSS-sal%C3%A1rio-e-INSS-f%C3%A9rias-em-c%C3%A1lculo-de-folha-de-pagamento-com-o-par%C3%A2metro-MV-DINSSFM-N?source=search)

[RH - Linha Protheus - GPE - Ao confirmar a rescisão apresenta mensagem: Verificar o campo quantidade de lançamentos no cadastro da(s) verba(s) abaixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205811-RH-Linha-Protheus-GPE-Ao-confirmar-a-rescis%C3%A3o-apresenta-mensagem-Verificar-o-campo-quantidade-de-lan%C3%A7amentos-no-cadastro-da-s-verba-s-abaixo?source=search)

[RH - Linha Protheus - GPE - Cálculo de rescisão após retorno de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047533313-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-ap%C3%B3s-retorno-de-f%C3%A9rias?source=search)
