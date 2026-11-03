---
article_id: 20986122493975
category: Financeiro - Reinf
content_hash: 142a8c2a9cef34c0c4d1dd559130e5d9e6b62d329c44a12a2b51ba992a7aee76
fetched_at: '2026-06-28T22:37:51.772610+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Cancelar baixa
  de pagamento antecipado com calculo de impostos não permitida
type: support-article
updated_at: '2024-01-30T23:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20986122493975-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Cancelar-baixa-de-pagamento-antecipado-com-calculo-de-impostos-n%C3%A3o-permitida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20992752146967)** Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**

No módulo Financeiro, realizado a abaixa parcial do PA com impostos de forma manual, ao tentar estorno ou cancelamento é exibido a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986129659927)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Reinf -  A partir da versão 12.1.33

**Causa**

O bloqueio da exclusão ou cancelamento de baixa de Pagamento Adiantado ocorre devido os impostos retidos na inclusão do PA não serem refeito no cancelamento da baixa.

Quando realizamos a baixa do PA, na verdade, estamos realizados o cancelamento do pagamento e a exclusão dos impostos retidos no mesmo.

Caso houvesse a possibilidade de efetuar o cancelamento dessa baixa, esse título não poderia ser usado em outro processo no sistema, como compensação.

O valor desse não pagamento não teria integridade uma vez que os impostos não são refeitos.

**Solução**

Será necessário incluir um novo PA, não há como realizar o cancelamento da baixa.

**Saiba mais:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada FINA080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058862353-Cross-Segmentos-Linha-BackOffice-Protheus-SIGAFIN-Pontos-de-entrada-FINA080)
