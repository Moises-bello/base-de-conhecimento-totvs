---
article_id: 1500004100582
category: FATURAMENTO - RELATÓRIOS
content_hash: 90f08936402d3b7bcda70bf3fbe82512c670b068cc93c52450851e0cf407463c
fetched_at: '2026-06-28T22:38:22.907256+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Relatório de
  Pedidos não Entregues (MATR680) apresenta pedidos com Quant. Pendente negativa
type: support-article
updated_at: '2022-10-04T20:21:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004100582-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Relat%C3%B3rio-de-Pedidos-n%C3%A3o-Entregues-MATR680-apresenta-pedidos-com-Quant-Pendente-negativa
---

**Dúvida**

Ao gerar o relatório de Pedidos não entregues (MATR680), o sistema está trazendo pedidos com a coluna Quant. Pendente preenchida com valores negativos.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**No Protheus, é possível que ao inserir um pedido de venda, seja liberada uma quantidade maior do que a vendida, ou seja, caso informe uma quantidade de 10 unidades no campo "Quantidade" (C6\_QTDVEN), por exemplo, é possível preencher a "Qtd. Liberada" (C6\_QTDLIB) com 11 ou mais unidades. Isso depende da configuração do parâmetro **MV\_LIBACIM**.

O relatório de Pedidos não entregues (MATR680), possui um parâmetro em sua geração que é o "Situação do Pedido ?" que pode ser preenchido como:

* Em aberto: Demonstrará os pedidos que possuam a "Quantidade" (C6\_QTDVEN) diferente da "Qtd.Entregue" (C6\_QTDENT), porém ainda possuam saldo a ser enviado;
* Todos: Demonstrará todos os pedidos que possuam "Quantidade" (C6\_QTDVEN) diferente da "Qtd.Entregue" (C6\_QTDENT).

**Solução**

Caso não queira visualizar pedidos que tenham sido liberadas mais unidades que as informadas no campo "Quantidade" (C6\_QTDVEN), basta preencher o parâmetro "Situação do Pedido ?" com a opção "Em aberto" e o sistema demonstrará apenas pedidos que não tenham sido completamente atendidos, ignorando os pedidos que tenham sido atendidos acima do previsto.
