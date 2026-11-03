---
article_id: 360036421614
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 284489aad4db3a3eb31f358de09e1abbb5399f34c64be0343d3baf65253abd4e
fetched_at: '2026-06-28T22:38:23.958349+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Atualização
  automática de Preço Portal do Vendedor - Pedido e Orçamento
type: support-article
updated_at: '2023-08-30T21:18:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036421614-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-autom%C3%A1tica-de-Pre%C3%A7o-Portal-do-Vendedor-Pedido-e-Or%C3%A7amento
---

**Dúvida**

Atualização automática de Preço Portal do Vendedor - **Pedido** e **Orçamento**

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

Após o preenchimento prévio das informações do cliente no cabeçalho e também informar o produto nos itens, o Preço Unitário do produto será atualizado automaticamente ao término do preenchimento do campo **Quantidade** na inclusão, seguindo a sequência da regra abaixo:

1.Tabela de Preço definida pelo parâmetro **MV\_PVTABPV** (para Pedido de Vendas) ou **MV\_PVTABOC** (para Orçamento);

2.Tabela de Preço configurada para o Cliente através do campo Tabela **Preco** (**A1\_TABELA**) no Cadastro de **Clientes**;

3.Tabela de Preço definida pelo parâmetro **MV\_TABPAD** (Tabela de preço padrão);

4.Valor definido pelo campo **Preço** **Venda** (**B1\_PRV1**) no Cadastro de Produtos;

5.Se não encontrar nenhum dos preços acima, o valor deverá ser 0 (zero).

Detalhes em : **[TVSLEU\_Parâmetro filtro de produtos e gatilho tabela de preço no Portal do Vendedor](https://tdn.totvs.com/pages/releaseview.action?pageId=244440071)**
