---
article_id: 11152802568215
category: Materiais - Compras (SIGACOM)
content_hash: 54f43ffff5947af68741c0abee83101e0f158f1acce4bcea44ccb4a09ea21d77
fetched_at: '2026-06-28T22:41:23.973088+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Por que o HELP A100NOLOTE
  é apresentado ao tentar excluir um documento de entrada
type: support-article
updated_at: '2022-12-22T20:15:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11152802568215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Por-que-o-HELP-A100NOLOTE-%C3%A9-apresentado-ao-tentar-excluir-um-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:05:00 min** **Dúvida** Por que o HELP A100NOLOTE é apresentado ao tentar excluir um documento de entrada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras  
  
**Solução:**

O ***HELP A100NOLOTE*** é exibido quando o saldo do lote é menor que a quantidade da nota fiscal que está sendo excluída.  
  
É possível que o lote esteja reservado para uma OP ou pedido de venda e caso o documento de entrada for excluído, não haverá saldo para atender à esta OP ou pedido de venda.  
  
Por este motivo, o sistema não permite a exclusão até que o saldo seja o suficiente para atender as OPs e/ou pedidos de venda.  
  
Quando se fala de lote, o saldo fica gravado em 2 tabelas, na **SB2** tabela de saldo em estoque que á apresentado na consulta F4 e também na tabela **SB8**, onde grava o saldo do lote.  
  
Para consultar o saldo do lote pode verificar direto na tabela ou usar as rotina do estoque/consulta/rastreabilidade/ lotes pelo numero do lote dá para consultar.  
  
Poderá também realizar o movimento interno com uma entrada de nota para este lote ou estornar algum movimento do lote que o saldo está empenhado.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
