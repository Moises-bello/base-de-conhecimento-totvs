---
content_hash: e8ca35ede8148cb6053ac368947626a8ea15832b0222376c71cb2e6cd6d0ccc0
fetched_at: '2026-06-29T00:08:51.658962+00:00'
page_id: '337357208'
product: rm
source: tdn-rm
title: 1786229 MATESTCNTFTOF01-1206 DT Processamento Pendente - Item e OS
type: documentation
url: https://tdn.totvs.com/display/LRM/1786229+MATESTCNTFTOF01-1206+DT+Processamento+Pendente+-+Item+e+OS
version: 4
---

# Processamento Pendente - Item e OS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Funções:** | Estornar Item não recebido. |
| **Situação/Requisito:** | Quanto um item de movimento gerado através de OS não tem necessidade de consumo o mesmo não pode ser excluído. |
| **Solução/Implementação:** | Melhoria nos processos de **Estornar item não recebido** quando executados em movimentos gerados pelo TOTVS Manutenção (RMOfficina). Ao executar este processo para os movimentos relacionados à Ordem de Serviço, os itens selecionados serão apagados da tabela de Itens de Movimentos Gerados a partir de OS. Caso o item esteja parcialmente faturado/recebido não será executado o estorno e será emitido uma mensagem ao usuário orientando a utilizar o processo de Concluir Pedido.  Os processos de **Concluir Pedido** e **Estornar item não recebido** não serão apresentados para os movimentos de Ordem de Serviço. Não será permitido excluir itens de movimentos gerados pelo TOTVS Manutenção quando o movimento for acessado pelo módulo TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | 1786229. |
| **Requisito:** | MovMovimentoAction; MovEstornoItemFatParcAction |
| **Documento de Referência:** | Concluir Pedido: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.ConclusaoPedidos.aspx>  Estornar item não recebido: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.EstornarItemNaoRecebido.aspx> |
