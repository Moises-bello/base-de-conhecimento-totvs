---
article_id: 360028559112
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6ecbcae37d5f7bad55e9b0d633e2f1ebef46a75a77f40e85aa1d2d6c8aea3616
fetched_at: '2026-06-28T22:38:28.711225+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT-Faturamento x
  Cartão de Crédito
type: support-article
updated_at: '2021-09-02T15:51:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028559112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-x-Cart%C3%A3o-de-Cr%C3%A9dito
---

**Dúvida**

Como tratar a venda por cartão de credito no Faturamento Protheus?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT-  Todas as versões

**Solução**

O faturamento do pedido de venda (**MATA410**) não trabalha com cartão de crédito, o conceito do módulo é gerar nota fiscal (**MATA461**) com geração títulos do tipo NF.

O que se tem de opção para tratar no pedido é apenas a forma de pagamento que fica dentro de outras ações, como uma espécie de histórico do pedido, mas a geração será sempre um título do tipo NF.  
  
Para vendas  com cartão de crédito como parte de operação, o Protheus possui os módulos de Automação Comercial (**SigaLoja, SIGAFRT, PDV**).

No módulo de Call Center é possível trabalhar com conceito de cartão de crédito, mas apenas com a opção **clisitef**, não trabalha com **pin-pad** (máquina de cartão). Durante a finalização da venda (**TMKA273**) é digitado o número do cartão pelo operador de Call Center na tela de atendimento.

Se o pedido não tiver nenhuma restrição de crédito e estoque, ao faturar é gerado um título da operação de cartão de crédito, como é efetuado nos módulos de Automação Comercial, se tiver restrição de crédito ou estoque, o pedido passa a usar a regra de faturamento e aí, somente emitirá um título do tipo NF na geração da nota após as liberações de crédito e estoque.

Mais informações sobre venda com TEF no Call Center, consulte:

Artigo**: [MP-TMK-Integração TEF x Call Center](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028518872-MP-TMK-Integra%C3%A7%C3%A3o-TEF-x-Call-Center?source=search)**

Help On Line: **[Help On Line - Call Center](%C2%A0http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigatmk.htm)**

**![Acesso_documenta__o_TEF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360029590011/Acesso_documenta__o_TEF.gif)**

**Importante: Com validação da legislação NT2020.006, relacionado a formas de pagamento, uma vez que o módulo de Faturamento não trabalha com forma cartão de crédito, como ocorre nos módulos de automação comercial, para o preenchimento da TAG <tBand>será necessário tratar via ponto de entrada PE01NFESEFAZ**,**mais orientações acesse a documentação: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 443 Rejeição: Código da bandeira de cartão de crédito e/ou débito inexistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004653542--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-443-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-bandeira-de-cart%C3%A3o-de-cr%C3%A9dito-e-ou-d%C3%A9bito-inexistente-?source=search)**
