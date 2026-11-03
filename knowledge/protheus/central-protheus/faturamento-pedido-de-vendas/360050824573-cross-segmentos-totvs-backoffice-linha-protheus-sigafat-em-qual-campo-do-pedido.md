---
article_id: 360050824573
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f52e8fac088a87d095a91d54138a35b7049550c0208e1afd87bd4ad32acc2d27
fetched_at: '2026-06-28T22:38:41.174507+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Em qual campo
  do pedido de venda (mata410), posso verificar qual foi o orçamento (MATA415) que
  gerou esse pedido, e no orçamento de vendas, o pedido vinculado
type: support-article
updated_at: '2023-09-27T11:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050824573-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Em-qual-campo-do-pedido-de-venda-mata410-posso-verificar-qual-foi-o-or%C3%A7amento-MATA415-que-gerou-esse-pedido-e-no-or%C3%A7amento-de-vendas-o-pedido-vinculado
---

**Dúvida**

Em qual campo do pedido de venda (**mata410**), posso verificar qual foi o orçamento (**MATA415**) que gerou esse pedido, e no orçamento de vendas, o pedido vinculado?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões

**Solução**

No orçamento, o campo é o **ck\_numpv(Pedido de Venda)**, ele fica desabilitado na tabela , sendo necessário colocar como usado e no browse no configurador para aparecer na linha de item do orçamento.  
  
No pedido, o campo é o **c6\_numorc (N.orçamento)**, que provavelmente deverá ser habilitado no configurador igual ao **ck\_numpv** para que apareça no pedido.

**Saiba mais sobre pedido de vendas:**

**[MP-FAT-Como-efetuar-um-pedido-de-venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002905022-MP-FAT-Como-efetuar-um-pedido-de-venda)**

**[MP - FAT - Exclusão de Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003259602-MP-FAT-Exclus%C3%A3o-de-Pedido-de-Vendas)**

**[MP-FAT-Como-incluir-anexar-um-documento-no-pedido-de-venda-sem-alterar-o-pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029089252-MP-FAT-Como-incluir-anexar-um-documento-no-pedido-de-venda-sem-alterar-o-pedido)**

**[MP-FAT-Como-cadastrar-abas-no-pedido-de-venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028357991-MP-FAT-Como-cadastrar-abas-no-pedido-de-venda)**

**[MP-FAT-Solicitação de Pedido De Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028649832-MP-FAT-Solicita%C3%A7%C3%A3o-de-Pedido-De-Vendas)**
