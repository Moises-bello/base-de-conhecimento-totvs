---
article_id: 360028449232
category: Materiais - Compras (SIGACOM)
content_hash: 7f647e97cf8ec72c30206fb4470ccf5fad34b378bcd14f67427be3208e83b925
fetched_at: '2026-06-28T22:41:11.761066+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras -  Help
  Uniqueline  - Produto x Fornecedor
type: support-article
updated_at: '2023-01-13T19:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028449232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Help-Uniqueline-Produto-x-Fornecedor
---

**Dúvida**

No momento da inclusão do fornecedor ao informá-lo pela segunda vez na linha do item, mesmo que contenha a informação no campo Cod.Pro.For diferente o sistema gera a mensagem padrão de duplicidade Uniqueline.

![UNIQUELINE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410789920023/UNIQUELINE.png)  
  
**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
**Solução**Na tabela SA5 uma a chave única da tabela é Fornecedor + Loja + Produto e nesta questão, o campo Cod.Pro.For. (A5\_CODPRF) não é chave única e caso somente este campo esteja diferente no cadastro apresentará a Help. Neste caso para conseguir incluir desta forma o cadastro de produto x fornecedor com um produto para o mesmo fornecedor repetidamente, será necessário informar o campo Fabricante.

Verificamos que para o cadastro via rotina padrão somente é possível esse cadastro com o fornecedor repetido se informar um Fabricante diferente.

Para entradas de Notas Via Totvs Colaboração, deve ser utilizado o ponto de entrada ***A140IPRD*** para tratativa.

![ProdxForn.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410789953559/ProdxForn.gif)

***Saiba Mais :***

[A140IPRD - Customização da Identificação do Produto](http://tdn.totvs.com/pages/releaseview.action?pageId=6085834)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
