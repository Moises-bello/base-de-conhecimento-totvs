---
article_id: 360020640791
category: Financeiro - Contas a Pagar
content_hash: ec5db969d011d45ec2abbacb6e713b56252fb4a4ffba0949521ff989de8441ea
fetched_at: '2026-06-28T22:38:09.877482+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA080 - Não permite excluir/cancelar baixa de PA que contém
  calculo de impostos
type: support-article
updated_at: '2022-06-14T17:47:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020640791-MP-SIGAFIN-FINA080-N%C3%A3o-permite-excluir-cancelar-baixa-de-PA-que-cont%C3%A9m-calculo-de-impostos
---

**Ocorrência**Após realizar a baixa de título tipo PA que contém retenção de imposto, o sistema não permite cancelar ou excluir essa baixa.  
  
 **Ambiente**Protheus - Financeiro - Versão 12  
  
 **Causa**O bloqueio da exclusão ou cancelamento de baixa de Pagamento Antecipado com retenção de imposto ocorre devido os impostos retidos na inclusão do PA não serem refeitos no cancelamento da baixa. Quando realizamos a baixa do PA, na verdade estamos realizando o cancelamento do pagamento e a exclusão dos impostos retidos sobre o mesmo. Caso houvesse a possibilidade de efetuar o cancelamento dessa baixa, esse título não poderia ser usado em outro processo no sistema como compensação. O valor desse não pagamento não teria integridade uma vez que os impostos não são refeitos.
