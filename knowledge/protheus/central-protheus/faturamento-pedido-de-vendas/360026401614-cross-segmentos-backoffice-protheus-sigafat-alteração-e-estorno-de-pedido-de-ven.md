---
article_id: 360026401614
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c9ffe9d17f0f0759ed52bf8e56423d761fe71d8868e39039b035ce11b30526a9
fetched_at: '2026-06-28T22:38:39.630177+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Alteração e estorno de Pedido
  de Venda liberado que contém Ordem de Separação
type: support-article
updated_at: '2025-04-15T19:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026401614-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Altera%C3%A7%C3%A3o-e-estorno-de-Pedido-de-Venda-liberado-que-cont%C3%A9m-Ordem-de-Separa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31437032780951) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**

É possível realizar alteração e estorno de liberação de um Pedido de Venda (MATA410) que possui Ordem de Separação (SIGAACD)?

**Ambiente**

Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para bloquear a alteração de itens do Pedido de Venda que possuem uma Ordem de Separação associada, utilize o parâmetro MV\_CBPE023 configurado como .T.  
Com esse parâmetro habilitado, o sistema impede a alteração apenas dos itens que já possuem ordem de separação, permitindo ainda a inclusão de novos itens no pedido.

**Observação 1:** A ordem de separação atua sobre os itens da tabela SC6, e não sobre o pedido como um todo.

#### **Estorno do Pedido de Venda com Ordem de Separação**

Para controlar o estorno do Pedido de Venda com Ordem de Separação vinculada, utilize o parâmetro MV\_CBPE013.  
Se este estiver configurado como .T., o sistema bloqueará o estorno, exibindo a seguinte mensagem (**Help CBMT460EST**):

|  |
| --- |
|  |

Caso seja necessário que todo o pedido não seja alterado, deverá trabalhar com um ponto de entrada no pedido de venda, seja para validação de linha de item ou na confirmação do pedido via botão **Salvar**, podendo utilizar o pontos de entradas:  
  
**M410LIOK** para linha de item: **[M410LIOK - Validação de linha de pedido](http://tdn.totvs.com/pages/releaseview.action?pageId=6784149)**  
**MT410TOK** para o botão Salvar: **[MT410TOK - Validar confirmação da operação](http://tdn.totvs.com/pages/viewpage.action?pageId=6784353)**

Saiba mais: **[Separação - ACDV166 - Automação de Coleta de Dados - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=545240659)**

**Observação 2:** Para maiores informações sobre o processo do módulo ACD contate a equipe Protheus Estoque/Custos/ACD
