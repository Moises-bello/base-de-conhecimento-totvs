---
article_id: 360031684073
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e8c653d7941788938bfecc7319c3ac675ed7d844c99d16224ee812ac51ff4e0e
fetched_at: '2026-06-28T22:38:41.163771+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tabela de Preços
  Atualização de Pedidos de Venda gravados
type: support-article
updated_at: '2023-08-25T11:53:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031684073-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tabela-de-Pre%C3%A7os-Atualiza%C3%A7%C3%A3o-de-Pedidos-de-Venda-gravados
---

**Ocorrência**Após modificar valores de uma tabela de Preços o sistema não atualiza os valores do Pedido de Vendas e do Orçamento quando mesmo é alterado.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

Para atualizar os preços de produtos já inseridos em um Pedido de Vendas ou Orçamento; de acordo com a nova Tabela de Preços informada (ou alteração de Preço nessa mesma Tabela) utilize o parâmetro **MV\_PVRECAL** como **.F.**, para Pedidos, e o **MV\_ORRECAL** como **.F.** para Orçamentos.

É necessário que ao alterar o Pedido/Orçamento digite novamente a Tabela de Preços no campo para que os valores sejam recalculados.

Sobre envio de Contrato de Parceria:

No momento de gerar a remessa do Contrato o sistema abre a Tela com o Pedido de Vendas que está sendo gerado.

Se deixar o parâmetro **MV\_PVRECAL** = **.F.** basta digitar novamente o código da Tabela antes de salvar o Pedido. Com isto o sistema recalcula o preço unitário de acordo com o valor atual que está na Tabela de Preço.
