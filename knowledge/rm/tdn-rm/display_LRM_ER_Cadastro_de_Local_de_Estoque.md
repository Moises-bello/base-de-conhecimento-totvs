---
content_hash: 1ef3cd89531dfd423e0bceff26ed31bd754056b985aab916f1a540b39fd0649a
fetched_at: '2026-06-29T00:06:02.492236+00:00'
page_id: '198945350'
product: rm
source: tdn-rm
title: ER_Cadastro_de_Local_de_Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Cadastro_de_Local_de_Estoque
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Gestão de Estoque, Compras e Faturamento | **Módulo** | Cadastros |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_C&P\_MOV006 | **IRM1** | PCREQ-4508 |
| **Requisito1** | PCREQ-6393 | **Subtarefa1** | PDR\_CP\_MOV006-891 |
| **Chamado2** | N/A | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | N/A | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração do Cadastro de Local de Estoque para o ambiente Fluig utilizando o TOTVS HTML Framework. 

## Definição da Regra de Negócio

 

**TOTVS HTML *Framework***

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *framework*. 

Ela tem como objetivo: 

* Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;
* Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));
* Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;
* Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo:

Mais informações sobre o TOTVS HTML Framework: [tec:TOTVS](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421) 

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos. 

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa. 

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades. 

 

Mais informações sobre o Fluig nos links:  

* <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
* <http://www.fluig.com/>

#### Cadastro de Local de Estoque

Por esta opção cadastra-se a tabela de Local de Estoque por filial.

O Local de Estoque trata-se de uma entidade principal para o correto controle de estoque. É criado conforme local de armazenagem dos produtos nas filiais e tem a sua importância dentro do Gestão de Estoque, Compras e Faturamento, pois  todo o  saldo dos produtos estará vinculado à filial/local de estoque da empresa, permitindo assim a obtenção de informações por local de estoque ou consolidados.

Temos a possibilidade de inativar um local de estoque e desta forma, o mesmo não será mais exibido para movimentações.

Observações:

* A descrição "**Local de Estoque**" para esta tabela é default do sistema, podendo ser alterada através do **Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Local de Estoque**.

Segue abaixo a descrição de determinados campos do cadastro de local de estoque:

* Campos obrigatórios: Filial, Código, Nível de estoque (caso esteja habilitado)
* Campos não obrigatórios: Descrição, Identificador da unidade de negócio, Endereço, Defaults Contábeis
* Código: Informe o código do local de estoque, de acordo com a máscara parametrizada em **Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Local de Estoque**.
* Faixa do Nível de Estoque: Informe em qual das 3 faixas este local irá buscar o estoque mínimo, o estoque máximo e o ponto de pedido, cadastrados nos produtos, na pasta controle de estoque.
* O campo Faixa de Estoque só será visualizado caso o sistema não esteja parametrizado para trabalhar com ressuprimento.
* Unidade de Negócio: Para selecionar a unidade de negócio é necessário o seu cadastramento no Gestão Fiscal, através do **Menu Cadastro | Tabelas Auxiliares | Unidade de Negócio**.
* A unidade de negócio irá representar, nos lançamentos fiscais, a empresa contratante, utilizado pela empresa contratada, para realização de sua atividade.
* As Unidades de Negócio somente serão visualizadas no local de estoque quando cadastrado na filial correspondente.
* A tela de **Defaults Contábeis**não será implementado na primeira versão da migração, por se tratar de uma tela de outro produto, que é customizada pelo **TOTVS Gestão de Estoque, Compras e Faturamento.**

Exemplo:

* No Local de estoque 01 foi cadastrada a Filial Belo Horizonte, somente as Unidades de Negócio da filial Belo Horizonte estarão disponíveis para seleção.
* Defaults Contábeis: Campo a ser informado as contas de débito e/ou credito referente a contabilização do movimento.
* Endereço: Segue a inclusão dos dados referente ao endereço do local de estoque, caso este possua.

No **TOTVS Gestão de Estoque, Compras e Faturamento** o **Cadastro de Locais de Estoque** está localizado no seguinte caminho: **BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Locais de Estoque** 

#### Migração

Para o **Cadastro de Local de Estoque** do **TOTVS Gestão de Estoque, Compras e Faturamento** serão desenvolvidas telas Web utilizando o TOTVS HTML Framework. 

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro. 

##### Tabelas Utilizadas

* TLOC

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
