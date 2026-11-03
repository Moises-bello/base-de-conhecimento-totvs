---
article_id: 360007168411
category: Materiais - Compras (SIGACOM)
content_hash: eb6eeb1257414bf82605177ae687edf0a35987fbb11e6e015e8df03bf58b6cc5
fetched_at: '2026-06-28T22:41:07.644786+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Gerar Solicitação
  de Compras por Ponto de Pedido com Aglutinação de Produtos?
type: support-article
updated_at: '2022-05-16T22:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007168411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Gerar-Solicita%C3%A7%C3%A3o-de-Compras-por-Ponto-de-Pedido-com-Aglutina%C3%A7%C3%A3o-de-Produtos
---

**Dúvida**Como Gerar Solicitação de Compras por Ponto de Pedido com Aglutinação de Produtos?

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

Para atender as situações em que o comprador deseja gerar as solicitações de compras por ponto  
de pedido aglutinando todos os produtos, que atingiram o ponto de reposição de estoque, em uma  
única tela, na rotina  de "Solicitação para Ponto Pedido" (MATA170), existe a pergunta "Gera SC por produto? (Sim/Não)", disponível no botão “Parâmetros” para a configuração.

A pergunta "Gera SC por produto" permite gerar uma solicitação de compras para cada  
produto, quando configurado com "Sim", ou gerar apenas uma única solicitação de compras para  
todos os produtos que atingiram o ponto de pedido, quando configurado com "Não". Essa última  
opção pode ser útil quando o comprador possui uma quantidade muito grande de itens em ponto  
de pedido e prefere visualizá-los em uma única tela (solicitação), facilitando assim sua análise.

Exemplo:

Perceba como serão geradas as solicitações de compras conforme as seguintes configurações:

**1 -"Gera SC por produto" = Sim**

Ao confirmar o a execução da rotina, será gerada uma solicitação de compras para cada  
produto que estiver em ponto de pedido.

**2- "Gera SC por produto" = Não**

Neste caso, ao confirmar o processamento da rotina, será gerada apenas uma solicitação  
para todos os produtos que estiverem em ponto de pedido.
