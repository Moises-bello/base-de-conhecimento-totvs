---
article_id: 360055140073
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7b1a8a8b616170e35873b0ba45025a7e32fa5e6fa953881bdf15a770897bb826
fetched_at: '2026-06-28T22:42:45.895892+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Reservar saldo para o pedido ao realizar
  o apontamento de produção
type: support-article
updated_at: '2025-02-28T13:28:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055140073-Manufatura-Linha-Protheus-SIGAPCP-Reservar-saldo-para-o-pedido-ao-realizar-o-apontamento-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30308487682199)***Tempo aproximado para leitura: **00:01:09 min**  
**Dúvida**Como apontar uma **OP - Ordem de Produção** que está relacionada a um pedido de venda e não liberar o saldo para estoque, ou seja, deixar reservado para o pedido?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para liberar ou não a produção do pedido de venda amarrado a **OP** é necessário configurar o campo **Libera PV - F5\_LIBPVPR** no **MATA230 - Movs. Internas** da **TM - Tipo de Movimentação** que é utilizada para realizar o apontamento de produção.  
  
Quando o campo **F5\_LIBPVPR** está igual a **S- Sim** o saldo é liberado para o pedido de venda.  
  
Quando o campo **F5\_LIBPVPR** está igual a **N- Não** o saldo é liberado para o estoque.  
  
**Importante**  
Essa opção só é aplicada quando o produto não possui controle de endereçamento e o produto produzido não é encaminhado para o **CQ - Controle de Qualidade.**
