---
article_id: 360026075333
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: b49e5e642cde4b967c2be9a2081a5c6774f18410482ba1a9528b7d2824ba49e5
fetched_at: '2026-06-28T22:36:58.989308+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Como bloquear
  o Pedido de Exportação?
type: support-article
updated_at: '2022-06-14T20:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026075333-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-bloquear-o-Pedido-de-Exporta%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como bloquear o pedido de exportação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Neste caso, o tratamento de bloqueio deve ser realizado por ponto de entrada:

1. Não faturar o pedido até a liberação: se a customização objetiva não faturar um pedido de venda que foi originado pelo pedido de exportação, deve ser verificado um ponto de entrada no pedido de venda (SIGAFAT), para implementar esta regra;  
2. Não gerar o pedido de venda: se a customização objetiva condicionar a geração do pedido de venda após a gravação do pedido de exportação, deve ser usado o ponto de entrada ExecBlock("EECCAD00", .F., .F.,"INTEG\_FAT") - [DT PE EECCAD00 Customização de funções auxiliares](http://tdn.totvs.com/pages/releaseview.action?pageId=211060029)  
3. Para condicionar as ações que podem ser executadas no pedido de exportação**:** pode ser usado o ponto de entrada ExecBlock("EECAP100",.F.,.F.,{"AP100MAN\_INICIO"}), intervindo na opção selecionada pelo usuário através da variável nOpcAux - [DT PE EECAP100 Pedido de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=397378412)
