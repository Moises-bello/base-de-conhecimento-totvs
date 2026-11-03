---
article_id: 4906505418263
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d81dd49e8a7d5221915c3e4d78ab7f35d049129e10d703cd33484147b4b2488e
fetched_at: '2026-06-28T22:38:38.608069+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Preenchimento
  da descrição C6_DESCRI no pedido de venda
type: support-article
updated_at: '2022-03-21T14:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4906505418263-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-da-descri%C3%A7%C3%A3o-C6-DESCRI-no-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Preenchimento da descrição do produto no pedido de venda.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da Versão 11.  
  
**Solução**

Existem três formas de preencher a descrição do produto(**C6\_DESCRI**) no Pedido de Venda:

**1-** Descrição do cadastro do produto do campo B1\_DESCRI, é gatilhado no pedido assim que informa o código do produto no campo C6\_PRODUTO.

Observação: A descrição do produto gatilhada do campo **B1\_DESC** após salva o pedido fica gravada no banco, e caso altere a descrição do produto na SB1, a mesma não será atualizada. É necessário incluir o item novamente para trazer a descrição atual no pedido de venda.

2- Descrição do produto da rotina **ProdutoXCliente** (**MATA370)**, que é uma rotina que permite criar uma descrição de produto especifica para cada cliente, e ao informar o código do produto será cadastrado , saiba mais [aqui](https://tdn.totvs.com/x/1E_ZDg)

Observação: Quando há descrição do produto na **SB1**(cadastro do produto) e descrição criada para o cliente na SA7 (produtoxcliente), será gatilhado da **SA7**.

3- Descrição do produto digita no campo **C6\_DESCRI** na inclusão ou alteração de pedido, isto possibilita que se houver faturamento que precise adicionar informação, é possível fazer dentro do pedido de venda.
