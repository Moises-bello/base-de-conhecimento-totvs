---
article_id: 16538657526679
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7ad9a7c9d16afbb5866a3bc882c7b4c3ca6bff43787f2d7bf4953e971d917eaf
fetched_at: '2026-06-28T22:38:39.863785+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Help: Este Documento não
  poderá ser alterado pois existe um vinculo com pedido de compras ja recebido'
type: support-article
updated_at: '2024-11-28T14:40:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16538657526679-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-Este-Documento-n%C3%A3o-poder%C3%A1-ser-alterado-pois-existe-um-vinculo-com-pedido-de-compras-ja-recebido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16538700096535) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como resolver o "Help: Este Documento não poderá ser alterado pois existe um vinculo com pedido de compras ja recebido" ao alterar um pedido de vendas.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Ocorrência**

O sistema apresenta esse Help pois no campo **"Ped. Compra" (C6\_PEDCOM)** está um pedido de compra que já teve algum item atendido por um **documento de entrada (Rotina MATA103)**, colocando valor no campo **"Qtd. Entregue" (C7\_QUJE)** do **pedido de compra (Rotina MATA121)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16538546120599)

**Solução**

**- 1. (Não perdendo a amarração):** Para que seja possível alterar o pedido de venda, é preciso que o pedido de compra que está no campo **"Ped. Compra" (C6\_PEDCOM)** esteja com legenda "verde", ou seja, com o campo **"Qtd. Entregue" (C7\_QUJE) = 0**, assim:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16538534675095)

**OBS:** Os parâmetros **MV\_ALTPED** e **MV\_ALTPEDC** não tem relação direta com esse processo.

Para que o pedido de compra fique em aberto, é necessário que sejam excluídos todos os documentos de entrada que atenderam seus itens, ou seja, documentos de entrada com o campo **"No do pedido" (D1\_PEDIDO)** igual a numeração do pedido de compra.

Dúvidas em como identificar os documentos de entrada que atenderam aos pedidos de compra, contate a Equipe Protheus Compras.

**- 2. (Perdendo a amarração):** O vínculo entre os registros trava a manutenção do pedido por uma questão de integridade, quando o pedido de compra paralelo possui quantidade entregue **(C7\_QUJE > 0)** e havendo a possibilidade de manutenção do pedido com base na retirada da informação da filial do pedido de compra se trata de uma saída contorno, visto que o operador assume a quebra de integridade, o que será feito já que o pedido será alterado com seu paralelo já movimentado.

Desta maneira, é necessário alterar o pedido de vendas e retirar o conteúdo do campo **"C6\_FILPED"**, desta forma a alteração será liberada mediante aviso sobre a quebra de integridade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20255825180183)
