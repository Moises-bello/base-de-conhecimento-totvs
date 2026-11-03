---
article_id: 7726180493719
category: Materiais - Compras (SIGACOM)
content_hash: 2e25c1282b5cfe746dec683791b50480335b2f1817f3f37b71947d81de77ce00
fetched_at: '2026-06-28T22:41:24.253120+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Qual a relação do Contrato
  de Parceria com a Tabela de Preços ?
type: support-article
updated_at: '2022-07-27T11:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726180493719-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Qual-a-rela%C3%A7%C3%A3o-do-Contrato-de-Parceria-com-a-Tabela-de-Pre%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a relação do Contrato de Parceria com a Tabela de Preços ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

A rotina Contrato de Parceria (MATA125) destina-se às empresas que possuem contrato de fornecimento de produtos por um determinado período, eliminando a necessidade da inclusão de diversas Solicitações de Compras e da realização de Cotações, agilizando o processo de compra. Ou seja é firmado um contrato para determinados produtos e preço previamente negociados com o Fornecedor.

Para utilizar um produto em um Contrato de Parceria preencha com SIM o campo "Contrato" do cadastro de Produtos (B1\_CONTRAT), na aba cadastrais da rotina de Cadastro do Produto (MATA010).

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7735822105751/imagem1.png)

**Obs1**: Os produtos cadastrados com essa condição, não podem ser utilizados nas rotinas de Solicitação de Compra, Pedido de Compra e Solicitação por Ponto de Pedido.

Dessa forma, como o conceito da rotina de Contrato de Parceria refere-se a um acordo pré-estabelecido para um produto e seu respectivo preço, a Tabela de Preços (COMA010) não é utilizada quando existe um Contrato de Parceria.

**Obs2**: As rotinas Contrato de Parceria (MATA125) e Solicitação de Compras (MATA110) não possuem um campo para alimentar a Tabela de Preços (COMA010), portanto, caso um Contrato de Parceria seja vinculado em uma Autorização de Entregas, e uma Solicitação de Compras seja vinculada a um Pedido de Compras, não haverá preenchimento do campo C7\_CODTAB, referente a Tabela de Preços.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
