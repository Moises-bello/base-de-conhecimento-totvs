---
article_id: 360024912671
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 92c8f755e22584ffb35620ea482a24fd12b4c3e9261effb3a2327014ef59d5ed
fetched_at: '2026-06-28T22:38:58.566439+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Como incluir uma Ordem de Produção para uma venda?
type: support-article
updated_at: '2021-11-22T12:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024912671-MP-SIGAEST-Como-incluir-uma-Ordem-de-Produ%C3%A7%C3%A3o-para-uma-venda
---

**Dúvida**  
Como fazer a **inclusão de uma Ordem de Produção (MATA650)**para uma venda que farei ao meu cliente/fornecedor?  
  
**Ambiente**Protheus - Estoque - A partir da versão 12.1.17  
  
**Solução**Existe cenários em que a empresa tem a necessidade de incluir uma Ordem de Produção já vinculando a um **P****edido de Venda** que terá o produto que será produzido. Isso acontece no caso de uma empresa que já faz um Pedido de Vendas a um cliente e o produto ainda não foi produzido. Desta forma, a produção que será feita será exclusivamente para este pedido.

Para fazer esta OP já vinculando-a a um Pedido de Venda, basta seguir os passos a seguir:

1. Incluir o Pedido de Venda liberado com a quantidade que será produzida (**não** preparar o documento de saída);  
2. Na rotina de Ordem de Produção(**MATA650**), clicar em "Outras Ações" ->"Vendas";  
3. Ao abrir a tela de parametrização, atentar-se em filtrar o **cliente**, **número de pedido** e o **período** em que fez o pedido (verificar as outras informações da tela de parametrização para que o sistema filtre os pedidos de vendas que serão considerados na produção);

4. Será aberto uma tela com os pedidos de venda filtrados. Lembrando que o status do pedido deve ser verde (Pedido de Venda em aberto) pois somente com pedidos com este status conseguirá gerar a OP. Caso esteja com status vermelho (Pedido de Venda encerrado), deverá verificar se o pedido já foi utilizado para geração de uma ordem anterior ou se o mesmo esta bloqueado para uso.

5. Clicar no botão "Gera O.P". Então a ordem de produção será gerada, o campo **C2\_PEDIDO** será preenchido com o número do mesmo, além dos campos **C6\_NUMOP** e **C6\_ITEMOP**.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
