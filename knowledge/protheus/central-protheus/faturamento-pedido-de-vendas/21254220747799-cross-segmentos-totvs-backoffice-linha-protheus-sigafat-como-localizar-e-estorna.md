---
article_id: 21254220747799
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 018e453168c8c6b5368198926c9f61b8506eb5067fc73ac0d302996a44527acb
fetched_at: '2026-06-28T22:38:41.117688+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como localizar
  e estornar o saldo da "Qtd. Reserva" (B2_RESERVA) das "Reservas para Faturamento"
  (SC0)
type: support-article
updated_at: '2025-03-31T15:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254220747799-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-das-Reservas-para-Faturamento-SC0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21254220698263) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Como localizar e retirar o saldo do campo "Qtd. Reserva" (B2\_RESERVA) de um produto?  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**

Quando um produto possui saldo no campo **"Qtd. Reserva" (B2\_RESERVA)**, este saldo está reservado ao processo, não sendo possível usar em qualquer movimentação. Muitas vezes é preciso localizar esse saldo para remover a liberação, para usa-lo em outros processos.

No processo de Faturamento, há algumas maneiras de alimentar a **"Qtd. Reserva" (B2\_RESERVA)** de um produto:

1. **Liberando o produto** em um Pedido de Vendas, após liberação de estoque, assim alimentando a tabela de **Pedidos Liberados (SC9)**;
2. **Realizando inserção de uma reserva** na rotina "**Controle de Reservas (MATA430)**", automaticamente ou manualmente, assim alimentando a tabela de **Reservas para Faturamento (SC0)**;
3. Reserva vinculada à um Orçamento, **do módulo SIGALOJA**, não finalizado, assim alimentando a tabela de **"Itens do Orçamento" (SL2)**.

**Observação: Para saber como Localizar/Estornar as reservas das tabelas de** **Pedidos Liberados (SC9)**

**e** **"Itens do Orçamento" (SL2), consulte o "Saiba mais" no final da documentação.**

**Solução**Para estorno da **"Qtd. Reserva" (B2\_RESERVA)**, é necessário realizar os processos abaixo:

**1 - Verificar/Estornar reservas na tabela de** **Reservas para Faturamento (SC0):**

* Acesse a rotina **"Controle de Reservas" (MATA430)**;
* Realize um filtro na rotina pelo campo "**Produto (C0\_PRODUTO)**" com o código do produto que quer localizar a reserva e pelo campo "**Quantidade (C0\_QUANT)**":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31050160445591)

* Execute o Filtro criado para que o sistema mantenha em tela apenas as reservas do produto informado.

Caso retorne algum registro no filtro, considere eliminar resíduo/excluir a reserva,  para que o saldo seja abatido do campo **"Qtd. Reserva" (B2\_RESERVA).**

**2 - Verificar/Estornar reservas na tabela de Reservas para Faturamento (SC6):**

* Acesse o relatório "**Pedidos Não Entregues (MATR680)**" clique em "**Outras Ações > Personalizar**" "Por Produto" e adicione os campos "**Num.Reserva**" e "**Qtd.Reserva**", salve a personalização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31050153746583)

* Preencha os parâmetros:
  + - Do Produto ?
    - Ate o Produto ?
    - Situacao do Pedido ? = Em aberto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31050153748119)

* Preencha os parâmetros:
  + - Ordem = Total do Produto
    - Layout = Layout salvo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31050153750167)

* Nas colunas "**Num.Reserva**" e "**Qtd.Reserva**" é possível verificar o número da reserva e a quantidade reservada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31050153752343)

Para limpar a reserva acesse o pedido e limpe o campo "**Num. Reserva (C6\_RESERVA)**" no Pedido de Venda e depois execute o passo 1 novamente.

**Saiba mais:**

* [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) de um Pedido Liberado (SC9)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21253646074519-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-de-um-Pedido-Liberado-SC9)
* [Como localizar e estornar o saldo da "Qtd. Reserva" (B2\_RESERVA) dos "Itens do Orçamento" (SL2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254628360215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-localizar-e-estornar-o-saldo-da-Qtd-Reserva-B2-RESERVA-dos-Itens-do-Or%C3%A7amento-SL2)
