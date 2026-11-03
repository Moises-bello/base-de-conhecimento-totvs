---
article_id: 360038340133
category: Materiais - Compras (SIGACOM)
content_hash: bd851b8475a7da60a303d1c1dcbf833000c3ee74488e0d67630b2ae32c471a3a
fetched_at: '2026-06-28T22:41:08.762121+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Conversão de valores
  da moeda do Documento de Entrada para o título
type: support-article
updated_at: '2023-03-08T19:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038340133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Convers%C3%A3o-de-valores-da-moeda-do-Documento-de-Entrada-para-o-t%C3%ADtulo
---

**Dúvida**

Como o sistema se comporta no Documento de Entrada para conversão dos valores no Título Financeiro?

**Ambiente**

Microsiga – Compras – A partir da versão 12  
  
**Solução**

O documento (linha do item) é gerado em real e na aba duplicata que consta a informação do título será apresentada a informação conforme a moeda informada.

**Exemplo:**

Na linha do item consta como 8 mil reais.

Na aba duplicata é apresentada a informação de conversão de acordo com a moeda informada, nesse caso como foi informado moeda 2 (dólar) com taxa 3,00 o sistema realiza a conversão dos 8 mil reais em 2666,67 dólares, ou seja 8000 dividido por 3,00 é igual a 2666,666666666667.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049668894/mceclip0.png)

Na rotina de Contas a Pagar (**FINA050**) é possível consultar os campos demonstrando o valor original em reais (**E2\_VALOR**) e o campo de conversão conforme a moeda (**E2\_VLCRUZ**).  
  
![](https://totvssuporte.zendesk.com/attachments/token/ukZVjoGHqbdD2UJHqgciEGDEL/?name=inline286085296.png)​![](https://totvssuporte.zendesk.com/attachments/token/S2us00sS6UkQW3TXWYwv578yb/?name=inline-2074601101.png)

**Obs:** O sistema por padrão sempre ira trazer a MOEDA 1 no Documento de Entrada mesmo que a Moeda esteja por exemplo= 2  no pedido de compras. A Alteração deve ser feita manualmente no Documento de Entrada.

No entanto temos um ponto de entrada para essa questão:

[MT103TXPC - Alteração da taxa d moeda e check box conforme Pedido de Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=107383186)
