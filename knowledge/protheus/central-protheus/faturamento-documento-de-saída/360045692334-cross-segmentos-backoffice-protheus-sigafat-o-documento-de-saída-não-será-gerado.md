---
article_id: 360045692334
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3679c58d7d48e0b929f2ce8cda46c7facb6bc039ff97b020e461ccc86ad33f0b
fetched_at: '2026-06-28T22:38:44.104279+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - O documento de saída não
  será gerado neste momento, pois não há itens aptos a faturar
type: support-article
updated_at: '2025-08-01T15:11:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045692334-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-O-documento-de-sa%C3%ADda-n%C3%A3o-ser%C3%A1-gerado-neste-momento-pois-n%C3%A3o-h%C3%A1-itens-aptos-a-faturar
---

**Dúvida**

Ao tentar faturar um pedido pelo browser da rotina **"Pedidos de Vendas** **(MATA410)"**, ocorre a mensagem abaixo  no assistente e não conclui o faturamento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065158253)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**

Essa mensagem ocorre quando há **bloqueio de crédito e/ou estoque** no pedido de venda.

**Motivo 1: Bloqueio de Crédito**  
É necessário avaliar na rotina **"Análise de Crédito de Pedido de Venda (MATA450)"**, se  existe bloqueio de crédito para o pedido, a legenda dele estará na cor **azul** e o campo **"C9\_BLCRED"** estará marcado com uma numeração diferente de 10, indicando o motivo do bloqueio.

Estando com essa marcação, verifique se o cliente possui crédito disponível para a venda.

**[Verificações a realizar quando o sistema apresenta um bloqueio indevido de Crédito](https://tdn.totvs.com/x/z2k-Dg)**

**Motivo 2: Bloqueio de Estoque**Caso o campo **"C9\_BLCRED"**  esteja vazio, é necessário avaliar na rotina **"Liberação de Estoque (MATA455)"**, se  existe bloqueio de estoque para o pedido, a legenda dele estará na cor**preta**e o campo **"C9\_BLEST"** estará marcado com uma numeração diferente de 10, indicando o motivo do bloqueio.

Estando com essa marcação, verifique se o produto possui saldo em estoque disponível para a venda.

**[Verificações a realizar quando o sistema apresenta um bloqueio indevido de Estoque](https://tdn.totvs.com/x/zGk-Dg)**

**Motivo 3: Parâmetro "MV\_GERABLQ"**

Caso o parâmetro esteja como **"N"**, o produto possua controle de **lote e/ou localização** e tenha **bloqueio de estoque**, o sistema **não permite** a liberação do pedido **(não grava registro na tabela SC9)**.

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Qual a funcionalidade do parâmetro MV\_GERABLQ na Liberação do Pedido de Venda ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047411193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-a-funcionalidade-do-par%C3%A2metro-MV-GERABLQ-na-Libera%C3%A7%C3%A3o-do-Pedido-de-Venda)**

Uma vez resolvido os bloqueios, o pedido estará apto a faturar e o assistente finalizará o faturamento.
