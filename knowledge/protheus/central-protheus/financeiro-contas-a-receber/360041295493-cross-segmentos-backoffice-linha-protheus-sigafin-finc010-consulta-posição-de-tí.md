---
article_id: 360041295493
category: Financeiro - Contas a Receber
content_hash: 9e5106c72b3422af6cdaf215632dd01691e9d4e9490facd2b3011eb899fd0a3b
fetched_at: '2026-06-28T22:38:14.110817+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINC010 - Consulta
  Posição de título a receber
type: support-article
updated_at: '2024-12-12T17:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041295493-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINC010-Consulta-Posi%C3%A7%C3%A3o-de-t%C3%ADtulo-a-receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28480829047703)**Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como funciona a pergunta “Considera Lojas” na rotina FINC010?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**A pergunta **Considera Loja**:

- Totaliza ou não o limite de crédito do cadastro de um cliente independente da loja ou não.

- Mostra todos os registros (um a um) do cadastro de um cliente independente ou não da loja.

**Exemplo*****:***

Caso a empresa tenho no cadastro do cliente:

**Cod. Cliente**=123456  loja=01 Limite de crédito=R$ 500,00

**Cod. Cliente**=123456  loja=02 Limite de crédito=R$ 1.500,00

**Cod. Cliente**=123456  loja=03 Limite de crédito=R$ =2.000,00

Caso a empresa faça um pedido de venda:

**Pedido de venda** 01 no valor de R$ 100,00 para o cliente cod. 123456 loja 01

**Pedido de venda** 02 no valor de R$ 200,00 para o cliente cod. 123456 loja 02

**Pedido de venda** 03 no valor de R$ 300,00 para o cliente cod. 123456 loja 02

Ao utilizar a pergunta com o conteúdo **Considera Loja=SIM**

Ao posicionar no código do cliente 123456 referente a loja 02, a rotina somente irá mostrar o limite do cliente referente a loja 02 que será de R$ 1.500,00 e ao clicar no botão **Pedidos** irá somente mostrar o pedido de venda 02 (que é o único que foi amarrado ao cliente 123456 da loja 02)

 Ao utilizar a pergunta com o conteúdo **Considera Loja=NÃO**

Ao posicionar no código do cliente 123456 referente a loja 02, a rotina somente soma todos os limites dos clientes do código 123456 ignorando o cadastro das lojas de seus clientes, totalizando um limite de crédito de R$ 4.000,00 e ao clicar no botão “Pedidos” irá mostrar todos os pedidos de venda com o código de cliente 123456 independente do código da loja, mostrando os pedidos de venda 01 de R$ 100,00, pedido 02 de R$ 200,00 e o pedido 03 de R$ 300,00

 Segue abaixo imagens referente ao processo.

![kcs_01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053915094)

![kcs_02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360054766713)

![kcs_03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053915074)

![kcs_04.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053915054)

![kcs_05.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053915034)

![kcs_06.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360054766693)

![kcs_07.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053915014)

![kcs_08.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360054766673)

![kcs_09.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053914954)

![kcs_10.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053914974)

![kcs_11.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053914934)

![kcs_12.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360054766653)

![kcs_13.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053914914)

![kcs_14.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053914894)
