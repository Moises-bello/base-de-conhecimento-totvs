---
article_id: 360021997251
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8389c3a3fc0dc92c7a0dcee47d32921c43b5949ad918518384ece363bc4ad674
fetched_at: '2026-06-28T22:42:43.598175+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A410ALTPV
type: support-article
updated_at: '2023-10-19T12:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021997251-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A410ALTPV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:25 min  
  
Ocorrência**No módulo de **SIGAFAT - Faturamento**, ao alterar um pedido de vendas que está vinculado a uma ordem de produção é apresentada o *help* **A410ALTPV - A quantidade deste pedido não poderá ser alterada, pois a Ordem de Produção que está vinculada já foi produzida e/ou movimentada**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Esse incidente ocorre, pois o Sistema foi parametrizado para atualizar a tabela de controle interno **SGJ -** **Amarração Pedido de Venda x Ordem de Produção** por meio da ativação do parâmetro **MV\_PVCOMOP - Ativa a gravação na tabela SGJ - Amarração Pedido de Venda x Ordem de Produção** e a ordem de produção já foi produzida totalmente ou parcialmente.  
  
**Solução**Para solucionar essa ocorrência, deverá desativar o parâmetro **MV\_PVCOMOP** para não gravar a tabela **SGJ** ou não apontar a ordem de produção seja parcial ou total.  
  
**Importante**  
Somente os **Pedidos de Venda** gerados após a desativação do parâmetro, não serão controlados pela tabela **SGJ**.  
Esta tabela é usada internamente pelo Sistema para controlar os registros de amarração do pedido de venda com as ordens de produção.  
Nesta tabela terão informações como número da **OP - Ordem Produção**, produto, número do pedido de venda, quantidade da ordem/pedido de venda, entre outras informações.
