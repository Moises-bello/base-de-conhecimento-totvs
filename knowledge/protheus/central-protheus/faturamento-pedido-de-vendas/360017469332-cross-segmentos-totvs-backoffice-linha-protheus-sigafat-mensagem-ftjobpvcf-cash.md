---
article_id: 360017469332
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5893a99e1223032d71f9662f488c1ade585699404e3b069e077b77fade809996
fetched_at: '2026-06-28T22:38:41.151401+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (LInha Protheus) - SIGAFAT - mensagem:
  FTJOBPVCF - Cash flow for sales order após incluir um pedido de venda'
type: support-article
updated_at: '2021-09-06T20:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017469332-Cross-Segmentos-TOTVS-Backoffice-LInha-Protheus-SIGAFAT-mensagem-FTJOBPVCF-Cash-flow-for-sales-order-ap%C3%B3s-incluir-um-pedido-de-venda
---

**Dúvida**

Do que se trata a mensagem : **FTJOBPVCF** - Cash flow for sales order após incluir um pedido de venda?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (LInha Protheus) - SIGAFAT - a partir da versão 12.  
  
**Solução**

O FTJOBPVCF é o Job de atualização do fluxo de caixa no Financeiro para os Pedidos de Venda.

Sempre que inserido um pedido de venda o sistema inicializa o Job para atualização das informações no financeiro, consultando o enviroment da empresa, a filial onde o pedido foi incluído e o módulo (SIGAFAT), gera a informação no server:

![image2021-9-6_16-37-19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407940667671/image2021-9-6_16-37-19.png)

Entre parênteses o sistema informa o número do pedido inserido.

Esse tratamento via JOB foi definido por ser um processo mais rápido e com a intenção de não comprometer a memória e não causar perda de performance.

Observação: O JOB é padrão do Protheus e sempre será acionado, quando inserido um pedido de vendas que utiliza um TES que gera duplicata (o mesmo não é acionado quando o TES não gerar duplicata para o financeiro), porém, vale ressaltar, que a execução deste Job não consome licenças.

**Desabilitar o Job:**

É possível desabilitar a execução do FTJOBPVCF através do ponto de entrada:

* **FtNRunFlCx** : <https://tdn.totvs.com/x/vbMJE>

A partir dessa configuração, o sistema deixa de atualizar o fluxo de caixa na inclusão do pedido de vendas, sendo necessário a atualização pelo módulo Financeiro (SIGAFIN).

**Performance:**

* Ao trabalhar os pedidos de venda com o campo "Tipo de Liberação" (C5\_TIPLIB) igual a 1, o processamento do Job pode ser um pouco mais ágil;
* Atualmente É possível utilizar o ponto de entrada M410REC para não considerar no processamento do fluxo de caixa os pedidos de vendas com data de entrega (C6\_ENTREG) inferior a data-base do sistema (<http://tdn.totvs.com.br/display/public/PROT/M410REC+-+Reprocessamento+do+Fluxo+de+Caixa>), esta configuração melhora a performance da função Ma410Fluxo.

**Saiba mais**: <https://tdn.totvs.com/x/BWU-Dg>
