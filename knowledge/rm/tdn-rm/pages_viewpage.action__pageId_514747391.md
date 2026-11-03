---
content_hash: 06ce430f4820a8fd35e5ebfde2ad64920f2b1133474e7d10c32d29449f0c7ec8
fetched_at: '2026-06-29T00:10:26.808194+00:00'
page_id: '514747391'
product: rm
source: tdn-rm
title: DT - TOP Mobile - Movimentações de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514747391
version: 15
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | Gestão de Obras e Projetos |
| Função: | Movimentações de Produto no TOP Mobile |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPORCAPLAN001-8883](https://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-8883)  [TOPORCAPLAN001-8734](https://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-8734) |

## **02. SITUAÇÃO/REQUISITO**

Criação de funcionalidade que permite solicitar produtos para o sistema de Suprimento/Faturamento através do TOP Mobile, sendo de compra ou requisição de material.

## **03. SOLUÇÃO**

Para atender a criação da nova API, foi incluído na tela de QR Code para Configuração do Sincronismo do TOP Mobile, o campo para informar a URL da API.

Exemplo de URL de API:

[http://nomedocomputador:porta/api/construction-projects/v1/product-movement-parameter?companyId=1&projectId=156&page=1&pageSize=10&order=+Description](http://bhn050102771.bh01.local:8052/api/construction-projects/v1/product-movement-parameter?companyId=1&projectId=156&page=1&pageSize=10&order=+Description)

Ao realizar a leitura do QR Code gerado na tela acima, os campos de Url serão automaticamente preenchidos.

No TOP, ao acessar o menu Projeto / Construção e Projetos / Movimentações de Produto, é possível realizar o cadastro dessas movimentações, informando o Tipo de Movimento e algumas parametrizações.

Mais informações, acessar: [Movimentações de Produto](https://tdn.totvs.com/pages/viewpage.action?pageId=525013681)

Após cadastro no TOP, essas informações serão exibidas no TOP Mobile.

       

Ao selecionar o tipo de requisição desejado, se a mesmo estiver parametrizado para utilizar contrato, a tela de seleção de contratos será exibida para que o contrato associado ao pedido seja selecionado. Apenas contratos de serviços serão exibidos.

Ao informar o Contrato e Avançar, a dela de itens da Requisição é exibida para que o Produto e Tarefa sejam selecionados.

Se o tipo de requisição não estiver parametrizado para utilizar contrato, após selecionar o tipo de requisição desejado, será aberta a tela de itens da Requisição.

  

Na tela de itens da Requisição, ao clicar no ícone com as quantidades dos Produtos adicionados ou clicar em Finalizar, é aberto a tela que  permite visualizar os itens de movimento, que serão apresentados antes de salvar.

Nessa tela, é permitido remover, alterar a quantidade, cancelar ou confirmar e salvar os produtos.

Também é permitido acessar a tela para inclusão de novos produtos, através da opção "Adicionar mais Produtos".

Nas telas de Contrato e Produto/Tarefa é possível visualizar as movimentações realizadas anteriormente, sendo possível visualizar os seu itens e consequentemente excluir o movimento gerado.

 

Clicando no botão "Filtrar", é possível consultar todas as requisições baseadas em informações do filtro, tais como Data de Criação, Período, Usuário, Identificador do Movimento, Número do Movimento e Tarefa. Ao confirmar o filtro, as opções selecionadas serão exibidas na tela principal, onde existe a possibilidade de excluí-las.

  

Para que o saldo do produto seja exibido é necessário definira o produto e a tarefa pois o local de estoque e filial estão definidos na obra representada pela tarefa, e o saldo exibido corresponde ao que foi definido na parametrização da movimentação selecionada para gerar o movimento.
