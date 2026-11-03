---
article_id: 360041762193
category: Financeiro - Contas a Pagar
content_hash: bc22a531a9202f6c5de45df2db442bdf17507b4cbb9dcd2a1d9a48a236c1567b
fetched_at: '2026-06-28T22:38:09.873241+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA080 - Exclusão ou cancelamento da baixa de tipo:PA que gerou
  impostos
type: support-article
updated_at: '2021-04-28T15:18:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041762193-MP-SIGAFIN-FINA080-Exclus%C3%A3o-ou-cancelamento-da-baixa-de-tipo-PA-que-gerou-impostos
---

**Dúvida**  
É possível efetuar a exclusão ou o estorno da baixa de um título tipo:PA que gerou impostos?

Apresentando a mensagem "Atenção - Cancelamento de baixa de pagamento adiantamento com cálculo de impostos não permitida"  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11  
   
**Solução**Não é possível, pois quando realizamos a baixa do PA pela rotina **FINA080** - **Baixa de títulos a pagar**, na verdade estamos realizado o cancelamento do pagamento e a exclusão dos impostos retidos.

Caso houvesse a possibilidade de efetuar o cancelamento dessa baixa, esse título não poderia ser usado em outro processo no sistema, como compensação. O valor desse não pagamento, não teria integridade uma vez que os impostos não são refeitos.

Sendo assim, será necessário incluir um novo PA, não há como realizar o cancelamento da baixa.

![foto_01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360055881273/foto_01.jpg)![foto_02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360055881293/foto_02.jpg)![foto_03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360055881253/foto_03.jpg)![foto_04.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360055008474/foto_04.jpg)
