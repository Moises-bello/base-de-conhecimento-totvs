---
content_hash: fa852e75933acba1869f125de48296ee46569f54fbdbaf9a39aee5018ad3e1a7
fetched_at: '2026-06-29T00:06:02.517240+00:00'
page_id: '198945881'
product: rm
source: tdn-rm
title: ER_Cadastro_de_Fabricantes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Cadastro_de_Fabricantes
version: 10
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

Migração do **Cadastro de Fabricantes** para o ambiente Fluig utilizando o TOTVS HTML Framework. 

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

#### Cadastro de Fabricantes

Opção para cadastrar fabricantes.

Esta tabela é responsável pelo cadastro dos fabricantes dos produtos controlados pela empresa.

A denominação "Fabricante" para esta tabela é default do sistema e poderá ser alterada através do menu **Opções | Parâmetros Gerais | Tabelas | Fabricante**.

Observações:

* É possível copiar o cadastro de fabricantes de uma coligada para outra. Para isso, utilize o processo ‘**Copiar Fabricantes entre Coligadas**’ e informe para qual coligada, se a cópia será só do registro corrente ou todos e se o registro já existir na coligada destino se mantém o registro existente ou se mantem.
* Para que o sistema efetue a cópia é necessário que os Parâmetros do Fabricante e Máscara das Tabelas de Classificação sejam iguais nas coligadas.

No **TOTVS Gestão de Estoque, Compras e Faturamento** o **Cadastro de Fabricantes** está localizado no seguinte caminho: **BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Fabricantes** 

#### Migração

Para o **Cadastro de Fabricantes** do **TOTVS Gestão de Estoque, Compras e Faturamento** serão desenvolvidas telas Web utilizando o TOTVS HTML Framework. 

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro. 

#### Campos e Regras

O **Cadastro de Fabricantes** possui algumas regras que serão listadas abaixo.

* Os campos Código e Descrição são obrigatórios.
* No seguinte caminho **BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | **Gestão de Estoque, Compras e Faturamento | 04.01 Parâmetros Gerais | 04.01.04 Tabelas | 04.01.04.02 Fabricante**** é possível parametrizar os seguintes itens:
  + Na aba **Outros Dados**, o box de **Classificação** é exibida conforme o parâmetro **Usa Tabelas de Classificação**.
  + Nome fabricante.
  + Máscara do campo código.
* Os campos com valores decimais possuem duas casas decimais como padrão.

##### Tabelas Utilizadas

* TFAB

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
