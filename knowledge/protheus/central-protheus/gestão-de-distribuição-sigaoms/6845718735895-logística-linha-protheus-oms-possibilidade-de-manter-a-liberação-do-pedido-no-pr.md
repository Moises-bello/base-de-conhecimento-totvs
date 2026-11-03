---
article_id: 6845718735895
category: Gestão de Distribuição (SIGAOMS)
content_hash: 8e144c1d6b7145c670676ffd9a25a0289bb94287d0f2e11ff2ab6273b0768493
fetched_at: '2026-06-28T22:45:50.069017+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Possibilidade de manter a liberação do pedido
  no procedimento do estorno do item do pedido de venda
type: support-article
updated_at: '2025-08-21T12:44:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6845718735895-Log%C3%ADstica-Linha-Protheus-OMS-Possibilidade-de-manter-a-libera%C3%A7%C3%A3o-do-pedido-no-procedimento-do-estorno-do-item-do-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16756711786903) Tempo aproximado para leitura: **00:01:42 min** **Dúvida**É possível manter a liberação do pedido no procedimento do estorno do item do pedido de venda?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na rotina **Montagem de Carga - OMSA200** é possível estornar o item do pedido, a partir da ação **Est. Ped**, sem perder a sua liberação na tabela **SC9 - Pedidos Liberados**.  
  
Para isso, é necessário que o parâmetro **MV\_OMSESTP - Indica se estorna liberacao do pedido de vendas de uma carga ao dividir um item.** Onde **.T. (default) efetua o estorno -** seja parametrizado com **.T.**  
  
Para o procedimento, selecione a carga desejada, acione o botão **Carregamento, Manutenção,** posicione no pedido de venda e em **Outras Ações**, execute a ação **Est.Ped**:

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16757420785175)

Marque os itens que serão estornados. No botão **Editar** é possível fazer a divisão da quantidade do item do pedido de venda. Neste exemplo, a quantidade liberada no pedido é 3 e a quantidade informada para a quebra é 1.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16757417405207)

Veja como foi atualizada a **tabela SC9**:

![sc9_estorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16757480504215)

Dessa forma, ao criar uma nova carga, o item estornado será apresentado para a montagem e não haverá a necessidade de realizar uma nova liberação do seu pedido:

![nova carga.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16757520675735)

**Saiba mais**A relação dos parâmetros utilizados no **TOTVS OMS - Order Management System**, poderão ser acessadas no *link*: [Logística - Linha Protheus - OMS - Parâmetros disponíveis para utilização do TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003269681-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-dispon%C3%ADveis-para-utiliza%C3%A7%C3%A3o-do-TOTVS-OMS)
