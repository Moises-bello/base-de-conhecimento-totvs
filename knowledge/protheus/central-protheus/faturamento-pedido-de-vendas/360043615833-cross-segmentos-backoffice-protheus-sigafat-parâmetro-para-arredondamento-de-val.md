---
article_id: 360043615833
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6772dacc826ae1a47f3fa86ebcb03e0130c8e5c09a7cce92c7a7f824a096d50d
fetched_at: '2026-06-28T22:38:39.913511+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetro para arredondamento
  de valor no pedido de vendas
type: support-article
updated_at: '2026-06-18T12:58:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043615833-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Par%C3%A2metro-para-arredondamento-de-valor-no-pedido-de-vendas
---

**Dúvida**

Qual o parâmetro devo configurar para usar o arredondamento no pedido de vendas?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

Verifique o conteúdo do parâmetro **MV\_ARREFAT** ele indica o padrão de arredondamento no total do pedido de venda:

* **S** - Arredonda o valor;
* **N** - Não arredonda, apresenta o valor truncado.

*Exemplo:*  
Supondo que, num determinado documento fiscal, o cálculo de uma venda resultou no valor R$ 60,436.  
De acordo com a configuração do parâmetro, o valor seria gravado da seguinte forma:

* **MV\_ARREFAT** configurado para arredondamento **(S)**: R$ 60,44
* **MV\_ARREFAT** configurado para não realizar arredondamento **(N)**: R$ 60,43.

Caso o parâmetro **MV\_ARREFAT** não exista, o sistema assumirá como padrão o não arredondamento **(N)**.

**Saiba Mais:**

[**Parâmetros de Arredondamento (SIGAFAT)**](https://tdn.totvs.com/x/hj6bEg)

[**Aumento de casas decimais no ambiente Faturamento (SIGAFAT)**](https://tdn.totvs.com/x/twEmDg)
