---
content_hash: 231a9b934c40b8d3f457fe446604cf0d1f3f0b62accbea3dc5710a011712870e
fetched_at: '2026-06-29T00:11:21.269628+00:00'
page_id: '691451196'
product: rm
source: tdn-rm
title: Grupo de Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+de+Produto
version: 17
---

Atenção

Recurso disponível na release 12.1.2209 ou superior.

## **01. VISÃO GERAL**

Este anexo permite que um Produto do estoque seja vinculado a um ou vários Grupo de Produtos. Sendo possível inserir, editar ou remover vínculos de Grupo de Produto de determinado Produto.

Informações Adicionais

[Cadastro do Grupo de Produto](https://tdn.totvs.com/display/LRM/Grupo+de+Produtos)

## **02. EXEMPLO DE UTILIZAÇÃO**

1. No módulo de Gestão de Estoque, Compras e Faturamentos, no cadastro de produtos selecione o anexo de Grupo de Produto.
2. Dentro da visão do anexo de Grupo de Produto faça a inclusão de um novo Grupo de Produto. São exibidos apenas os Grupos de Produtos ativos como opção.  
     
     
   Na edição/criação do vínculo do Grupo de Produto, é possível definir qual Grupo de Produto será o principal, sendo possível definir apenas um como principal. Caso o usuário tente marcar mais de um Grupo como principal, será exibida a consistência abaixo, informando que já existe um grupo principal para o produto em questão.
3. Após incluir um novo vínculo do Grupo de Produto, o mesmo será exibido na tela de anexo do Produto.

## **03. TABELAS UTILIZADAS**

* TPRDGRUPOPRODUTO - Tabela responsável pelo vinculo entre Produto e Grupo de Produto.
