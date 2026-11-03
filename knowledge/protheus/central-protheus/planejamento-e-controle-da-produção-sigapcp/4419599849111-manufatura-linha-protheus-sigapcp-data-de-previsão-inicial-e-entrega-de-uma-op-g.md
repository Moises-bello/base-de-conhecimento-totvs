---
article_id: 4419599849111
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6aa6795df8fe7b4fb79a566e014a9478756e5277e6bd5b0fb7befe9b3d409e82
fetched_at: '2026-06-28T22:42:42.160637+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Data de previsão inicial e entrega
  de uma OP gerada por vendas
type: support-article
updated_at: '2022-12-01T14:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419599849111-Manufatura-Linha-Protheus-SIGAPCP-Data-de-previs%C3%A3o-inicial-e-entrega-de-uma-OP-gerada-por-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como são determinadas as datas registradas em **C2\_DATPRI - Previsão Inicial** e **C2\_DATPRF - Entrega** de uma **OP - Ordem de Produção** gerada pela opção **Vendas** do **MATA650 - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o parâmetro do processo de **Vendas** do **MATA650,** **Avalia o Pedido de Venda** possui o conteúdo **Individualmente**, o campo **C2\_DATRF** é preenchido com o conteúdo do campo **C6\_ENTREG - Data de entrega** de cada pedido selecionado e para o qual está sendo gerada a **OP**.  
Já quando o parâmetro **Avalia o Pedido de Venda** possui o conteúdo **Agrupadamente**, deve-se observar o conteúdo do parâmetro **Avalia os Pedidos de Venda Priorizando**, se este parâmetro tiver o conteúdo **Num. Pedido**, será considerada o conteúdo do campo **C6\_ENTREG** do pedido de venda selecionado de numeração mais baixa. Se este parâmetro tiver o conteúdo **Data de Entrega**, será preenchido no campo **C2\_DATRF** com o conteúdo do campo **C6\_ENTREG**mais baixo, de acordo com os pedidos de venda selecionados.  
Já o campo **C2\_DATPRI** é preenchido levando em consideração o conteúdo do campo **C2\_DATRF** menos o prazo de entrega do item.
