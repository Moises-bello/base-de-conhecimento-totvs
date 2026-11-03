---
article_id: 360017409032
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7e9fb181843bbe4b1223069827d5b82f938e02e8b511a8e07d1f1b0ac8987611
fetched_at: '2026-06-28T22:38:38.418297+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Aba de Rentabilidade no Pedido de Vendas
type: support-article
updated_at: '2023-10-16T11:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017409032-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Aba-de-Rentabilidade-no-Pedido-de-Vendas
---

**Dúvida**

Qual a configuração completa para utilização de Rentabilidade no pedido de venda (MATA410)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A pasta rentabilidade, tem por objetivo demonstrar a lucratividade de uma venda, independente do prazo de recebimento e dos impostos envolvidos.

 A pasta de rentabilidade é composta por:

* **Valor Total:** É a soma de: **C6\_QTDVEN** \* **C6\_PRCVEN;**
* **C.M.V:** A Coluna **C.M.V** (Custo de Mercadoria Vendida) é o custo Médio do Produto.
* **Valor Presente:** A coluna **Valor Presente** que é uma fórmula matemático-financeira capaz de determinar o valor presente de pagamentos futuros descontados a uma taxa de juros apropriada.  
  O Valor Presente muda conforme a condição de Pagamento escolhida e com base no conteúdo do parâmetro **MV\_JUROS**, que por padrão vem com 5%;
* **Fórmula**: Valor Presente = Valor / ((1+ (Taxa Juros / 100)) \*\* (Prazo\_pgto / 30))
* **Lucro Bruto:** A coluna **Lucro Bruto** nada mais é do que a diferença entre o Valor Presente e o CMV.
* **Fórmula:** Lucro Bruto = Vlr. Presente – C.M.V
* **Margem de Contribuição:** A**margem de contribuição** é calculada da seguinte forma: **Fórmula:** Margem de contribuição (%) = Lucro Bruto / (Vlr. Presente \* 100)

**Saiba Mais:**

**[Campo "Valor Total" na aba Rentabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10822083471255-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Valor-Total-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas)**

**[Campo "C.M.V" na aba Rentabilidade da Planilha Financeira no Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10822862254871-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-C-M-V-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas)**

**[Campo "Lucro Bruto" na aba Rentabilidade da Planilha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823189023895-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Lucro-Bruto-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas)**

**[Campo "Margem de contribuição (%)" na aba Rentabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823362992791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Margem-de-contribui%C3%A7%C3%A3o-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas)**

**[Campo "Valor Presente" na aba Rentabilidade da Planilha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823494000407-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Valor-Presente-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas)**

**[Principais dúvidas na aba Rentabilidade da Planilha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823823828631-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-D%C3%BAvidas-na-Aba-Rentabilidade-da-planilha-financeira)**

**[Processo para utilização de Rentabilidade no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/RojpDw)**
