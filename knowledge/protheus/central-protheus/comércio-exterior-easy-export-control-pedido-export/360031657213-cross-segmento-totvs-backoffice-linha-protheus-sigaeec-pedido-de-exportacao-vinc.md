---
article_id: 360031657213
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 74b36f55da771297d1d42d2a231908535978d69f472d2cb9e8e85e9e890d920c
fetched_at: '2026-06-28T22:36:59.038979+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Pedido de Exportacao
  vinculado o Pedido de Vendas nao ser liberado automaticamente
type: support-article
updated_at: '2022-06-14T20:04:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031657213-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Pedido-de-Exportacao-vinculado-o-Pedido-de-Vendas-nao-ser-liberado-automaticamente
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como proceder inclusão do Pedido de Exportação e ao confirmar a geração do Pedido de Vendas não seja liberado automaticamente.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 11.80  
  
**Solução**Para que o Pedido de Vendas não seja criado já liberado, na rotina de pedido de vendas MATA410 selecione F12 e abrirá a caixa de Parâmetros.  
O sistema preenche automaticamente o campo C6\_QTDLIB com o conteúdo do campo C6\_QTDVEN.   
Para que o pedido não seja liberado automaticamente deixe como Sugere Qtde Liber. = Nâo.  
![](https://totvssuporte.zendesk.com/attachments/token/FMevaoaoBzENeJ1B3pzgUwBts/?name=inline224526537.png)
