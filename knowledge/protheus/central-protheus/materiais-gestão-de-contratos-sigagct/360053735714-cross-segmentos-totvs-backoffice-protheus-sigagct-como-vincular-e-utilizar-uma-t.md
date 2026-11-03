---
article_id: 360053735714
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6d3740943c34945f915277d90fa6fd2659d0c1c9e7abfb5d2c6b8602fe283bc8
fetched_at: '2026-06-28T22:37:21.671228+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como vincular e utilizar
  uma Tabela de Preço de Venda no cadastro de um Contrato ?
type: support-article
updated_at: '2026-05-07T14:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053735714-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-vincular-e-utilizar-uma-Tabela-de-Pre%C3%A7o-de-Venda-no-cadastro-de-um-Contrato
---

**Dúvida**  
Como vincular e utilizar uma Tabela de Preço de Venda no cadastro de um Contrato ?

**Ambiente**  
Protheus – Gestão de contrato – A partir da versão 12  
  
**Solução**  
  
No módulo Faturamento:

* Acesse a rotina tabela de preço e inclua o preço de venda, vinculando a u produto, e  com a respectiva faixa de quantidade (campo DA1\_QTDLOT) caso deseje utilizar. Caso nao se desje utilizar pode-se informar 999.999,99 neste campo
* Vincular a tabela de preço cadastrada ao cliente que será utilizado no Contrato.

No Gestão de Contratos:

* Ao inserir o produto da tabela de preço no item da planilha do contrato que possui o cliente que foi vinculada a tabela de preço, o preço unitário será gatilhado automaticamento no item da planilha.

***Obs:***

Caso não seja vinculada a tabela de preço no cadastro de cliente, após informar o produto da tabela de preço, o valor untário é gatilhado no item da planilha, apenas ao ser informada a tabela de preço no campo do item da planilha do contrato (CNB\_TABPRC).

Exemplo utilizando Faixa de Quantidade:

Ao inserir um contrato de venda e selecionar uma tabela de preço, e a quantidade estiver estiver informada na tabela, o sistema vai substituir o valor unitário digitado do produto pelo preço de venda que está atrelado na tabela, exemplo na 1a linha está informada a quantidade 30, sendo assim o valor a ser considerado será 70,00.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092416473)

Ao incluir um contrato de venda, e nos itens da planilha selecionar o produto quantidade  e a respectiva tabela de preço, conforme informada acima como exemplo, independente do valor unitário informado nos itens, o que será considerado automaticamente serão os valores de preço da tabela de venda.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090714974)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
