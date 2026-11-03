---
content_hash: 8f4fcd11d289a8ca98100b0d2eab05d3dedc886f1b37d7d33f43bfb4bbc14723
fetched_at: '2026-06-29T00:11:16.201172+00:00'
page_id: '664205609'
product: rm
source: tdn-rm
title: Endereçamento do Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=664205609
version: 16
---

Importante

Recurso disponível na release 12.1.2205 ou superior.

## **01. VISÃO GERAL**

Este anexo permite que endereços de locais de estoque sejam vinculados a um ou mais produtos. São exibidos apenas os endereços ativos como opção.

Só será possível vincular endereçamento a produtos de último nível e que não sejam controlados por número de série.

Atenção

O Endereçamento tem como objetivo facilitar as contagens durante o Inventário. O Controle de estoque continua sendo feito por Local de Estoque e portanto NÃO será feito por Endereçamento.

Informações Adicionais

[Parametrização e cadastro de endereçamento](https://tdn.totvs.com/pages/viewpage.action?pageId=662417226)

## **02. EXEMPLO DE UTILIZAÇÃO**

1. No módulo de Gestão de Estoque, Compras e Faturamentos, no cadastro de produtos selecione o anexo de Endereçamento de Produtos.
2. Dentro da visão do anexo de Endereçamento faça a inclusão de um novo endereço.  
     
     
   A tela de edição do Endereçamento do Produto, também possibilita que o mesmo seja marcado como Indisponível, ao fazer isso ele não será utilizado no cadastro de novos Inventários. Quando um Endereço é inativado, todos os vínculos de produtos associados a ele serão marcados como Indisponível também e este campo será bloqueado para que não seja possível ter um vínculo ativo (disponível) associado a um endereço inativo, como exemplificado abaixo.
3. Após realizar a inclusão do endereço, o mesmo será exibido na visão do anexo.

## **03. TABELAS UTILIZADAS**

* TPRDENDERECO - Tabela responsável pelo endereçamento de estoque do Produto
