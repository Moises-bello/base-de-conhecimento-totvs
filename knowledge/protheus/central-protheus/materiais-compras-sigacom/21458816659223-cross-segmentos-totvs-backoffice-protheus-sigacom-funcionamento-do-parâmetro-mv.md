---
article_id: 21458816659223
category: Materiais - Compras (SIGACOM)
content_hash: 96b952ff2e5c0f68f1356d99071442f8d34456bfe068cd80b51e110fbb8b8d30
fetched_at: '2026-06-28T22:41:18.698182+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Funcionamento do Parâmetro
  MV_COTFIAP em uma Compra Centralizada.
type: support-article
updated_at: '2024-02-19T16:42:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21458816659223-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Funcionamento-do-Par%C3%A2metro-MV-COTFIAP-em-uma-Compra-Centralizada
---

**Dúvida**

Como funciona o parâmetro MV\_COTFIAP em uma Compra Centralizada?

**Ambiente**

Protheus – Compras – A partir da versão 12

**Solução**

O parâmetro indica se os pedidos gerados por cotações em compra centralizada serão administrados pela filial de compra (C) ou pela filial de entrega (E).

Se o conteúdo do parâmetro for igual a (C), o pedido será gerado para a empresa centralizadora, definida na Rotina MATA110 ao Centralizar a SC.

Ou, se o conteúdo do parâmetro for igual a (E), o pedido será gerado para a empresa que consta no campo "Filial de Entrega - CFILENT".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458864643607)

No entanto, para que o pedido de compra seja gerado para a Filial de Entrega, o sistema realiza algumas validações, conforme abaixo:

1. Verifica se os produtos selecionados estão cadastrados na Filial de Entrega ou se a tabela SB1 é compartilhada.

2. Verifica se o fornecedor selecionado está cadastrado na Filial de Entrega ou se a tabela SA2 é compartilhada.

3. Verifica se a condição de pagamento selecionada está cadastrada na Filial de Entrega ou se a tabela SA4 é compartilhada.

Se as condições acima não forem atendidas, o Pedido de Compra será gerado para a empresa Centralizadora, mesmo que o parâmetro MV\_COTFIAP esteja definido como "E".

***Saiba Mais :***

*[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*

*[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*
