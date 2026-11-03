---
article_id: 27992050172183
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9132ccd0379ea93611d8aad7f8682aaed7c50fb4e4b2be3a3702a5b8387d5f06
fetched_at: '2026-06-28T22:38:39.702528+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como faturar/realizar documentos
  de saída
type: support-article
updated_at: '2024-11-22T17:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27992050172183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-faturar-realizar-documentos-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27992050140567) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como faturar/realizar documento de saída?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**1 - Realizar um pedido de venda na rotina "Pedidos de venda (MATA410)"

* Preencher os campos obrigatórios do cabeçalho, por padrão: "Numero (C5\_NUM)", "Tipo Pedido (C5\_TIPO)", "Cliente (C5\_CLIENT)", "Loja (C5\_LOJACLI)", "Tipo Cliente (C5\_TIPOCLI)" e "Cond. Pagto (C5\_CONDPAG)".
* Preencher os campos obrigatórios dos itens, por padrão [só os que tem que inserir manualmente]: "Produto (C6\_PRODUTO)", "Quantidade (C6\_QTDVEN)", "Prc Unitario (C6\_PRCVEN)", "Tipo Saida (C6\_TES)  
  Há outros campos obrigatório mas são preenchidos por gatilhos automáticos ao preencher os campos citados acima.

2 - Liberar para análise do crédito e estoque na rotina "Liberação de pedidos de vendas (MATA440)"

* Nessa etapa, após análise o sistema pode bloquear por crédito ou estoque, veja no Saiba Mais desse KCS como verificar.

3 - Faturar na rotina "Documentos de saída (MATA460A)"

* Preencher os parâmetros da rotina corretamente
* Selecionar os itens liberados do mesmo pedido de venda que entrarão na nota fiscal de saída (legenda verde)
* Apertar o botão "Prep. doc's"

4 - Para visualizar a nota fiscal de saída, entre na rotina "Consulta de notas fiscais de saída (MATC090)"

OBS 1: O documento de saída pode ser feito manualmente pela rotina MATA920 - NF Manual de saída, porém não atualizará estoque ou duplicatas financeiras.

Dúvidas nesse processo NA rotina "NF Manual de saída (MATA920)", contate a Equipe Protheus Fiscal.

OBS 2: Para excluir um documento de saída, vá na rotina "Exclusão de documentos de saída (MATA521A)", contudo só poderá ser excluído nessa rotina se a nota fiscal de saída foi feita em um faturamento na rotina "Documentos de saída (MATA460A)", se a nota foi feita manualmente na rotina "NF Manual de saída (MATA920)" não será possível.

**Saiba mais:**

[**Como identificar e liberar bloqueios do Pedido de Vendas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014207291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas)
