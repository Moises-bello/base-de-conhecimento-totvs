---
article_id: 360037713054
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 75c41b450b11eb0a04b4a74937e9e1194d997d68ff8c2041181636ba744d6e36
fetched_at: '2026-06-28T22:38:28.688337+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Mensagem de  adiantamentos
  relacionados na confirmação do pedido
type: support-article
updated_at: '2022-12-19T19:35:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713054-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagem-de-adiantamentos-relacionados-na-confirma%C3%A7%C3%A3o-do-pedido
---

**Dúvida**

Ao confirmar a inserção do pedido de venda (**MATA410**) está gerando a mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049478814/mceclip0.png)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A mensagem está relacionada a condição de pagamento (**MATA360**) utilizada no pedido, se o campo Adiantamento da condição de pagamento estiver  como Sim, indica que ao utilizar a condição de pagamento no pedido, deverá relacionar títulos de adiantamento a ele para abatimento do valor da nota ao faturar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049479134/mceclip1.png)

Para que a mensagem não ocorra, utilize uma condição de pagamento que não tenha a opção de Adiantamento igual a Sim.

Para maiores detalhes sobre a funcionalidade de Recebimento Antecipado (Adiantamento), acesse a FAQ no TDN: **[FAT0149\_RA\_–\_Recebimento\_Antecipado\_(Adiantamento)\_MATA410\_Pedido\_de\_Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=267796506)**
