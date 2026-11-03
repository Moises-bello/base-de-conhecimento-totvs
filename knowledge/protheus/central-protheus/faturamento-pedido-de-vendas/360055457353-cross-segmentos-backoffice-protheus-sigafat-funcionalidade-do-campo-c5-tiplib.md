---
article_id: 360055457353
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: dbfa8facf197e4f13717af0ced5ed6453e70ee1d264abc649ef3b411a59887ff
fetched_at: '2026-06-28T22:38:39.797433+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionalidade do campo C5_TIPLIB
type: support-article
updated_at: '2026-04-02T19:53:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055457353-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionalidade-do-campo-C5-TIPLIB
---

**Dúvida**

Qual a funcionalidade do campo **C5\_TIPLIB** no Pedido de Vendas?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as Versões  
  
**Solução**

O campo "Tp Liberação (**C5\_TIPLIB**)" no cabeçalho do Pedido de Vendas (**MATA410**) define o critério de liberação do Pedido de Venda.

**1 - Libera por Item:** Nesse caso a liberação de crédito e estoque será feita **por item**.  
**2 - Libera por Pedido:** Nesse caso a liberação de crédito e estoque será feita **por pedido**.

**# Exemplo na Avaliação de Crédito:**

**1.** Cliente: Risco-B;  
**2.** Limite de crédito = 10,00;  
**3.** Incluir Pedido de Venda com 2 itens, um de R$ 10,00 e outro de R$ 1,00;  
**4.** Liberar o pedido;

**Cenário 1 - C5\_TIPLIB = 1 - Libera por Item**  
Neste cenário, o sistema irá **liberar o primeiro** item para faturar e **bloqueará o segundo** item por crédito.

**Cenário 2 - C5\_TIPLIB = 2 - Libera por Pedido**  
Neste cenário, o sistema irá **bloquear os dois itens** por crédito. Como não conseguiu liberar o segundo item, então bloqueará todos os itens por crédito.

**# Exemplo na Avaliação de Estoque:**

**1.** Incluir Pedido de Venda com 2 itens, um com estoque e outro sem estoque;  
**2.** Liberar o pedido;

**Cenário 1 - C5\_TIPLIB = 1 - Libera por Item**  
Neste cenário, o sistema irá **liberar o primeiro** item para faturar e **bloqueará o segundo** item por estoque.

**Cenário 2 - C5\_TIPLIB = 2 - Libera por Pedido**  
Neste cenário, o sistema irá **bloquear os dois itens** por estoque. Como não conseguiu liberar o segundo item, então bloqueará todos os itens por estoque.

**Saiba Mais:**

[**Exemplos da Funcionalidade do campo C5\_TIPLIB**](https://tdn.totvs.com/x/tZYpE)
