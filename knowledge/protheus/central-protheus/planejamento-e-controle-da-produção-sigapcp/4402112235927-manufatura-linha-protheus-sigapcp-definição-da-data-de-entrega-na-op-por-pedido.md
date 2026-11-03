---
article_id: 4402112235927
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 078747795f0307c75c923c3ead75a938a0941d8291755e1d8d76c9588746d649
fetched_at: '2026-06-28T22:42:42.168467+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Definição da data de entrega na OP
  por pedido de venda
type: support-article
updated_at: '2021-06-07T11:04:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402112235927-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-da-data-de-entrega-na-OP-por-pedido-de-venda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como é determinado o conteúdo do campo **C2\_DATPRF - Entrega** de uma **OP - Ordem de produção** gerada por **pedido de venda** e que teve no parâmetro **Avalia o Pedido de Venda** o conteúdo **Agrupadamente**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando a **OP** é gerada **agrupadamente** o Sistema avalia o conteúdo do parâmetro **Avaliar os PVs Priorizando** para determinar de que forma será gerada a **OP**.  
Se esse parâmetro possui o conteúdo **Num Pedido**, é assumido como data de entrega a data de entrega do pedido de venda de menor número.  
Se esse parâmetro possui o conteúdo **Data de Entrega**, é assumido como data de entrega a menor data de entrega dentre os pedidos selecionados para esse item.
