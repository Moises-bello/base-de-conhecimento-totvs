---
content_hash: 33fc329a69448e2e643dad6e26e25628460aa74a4c54585a269a040b89c80c1b
fetched_at: '2026-06-29T00:06:02.634403+00:00'
page_id: '198948097'
product: rm
source: tdn-rm
title: ER_Cadastro_de_Representantes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Cadastro_de_Representantes
version: 9
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

Migração do **Cadastro de Representantes** para o ambiente Fluig utilizando o TOTVS HTML Framework. 

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

#### Cadastro de Representantes

 

* A descrição "**Representantes**" para esta tabela é default do sistema, podendo ser alterada através do **Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Representante**.

O **Cadastro de Representantes** tem a finalidade de registrar os parceiros de negócios da empresa, armazenando informações deste relacionamento, como percentuais de Comissão e Repasse, Endereço de Pagamento, Site, E-mail.   
Além das informações cadastrais acima, o sistema disponibiliza o cadastro de Tabelas para a Integração Financeira e Defaults Contábeis, para que a contabilização de Movimentos possa ocorrer a partir destes defaults e, desta forma, todo o processo contábil e financeiro possa ocorrer de acordo com as informações do Representante.  
O sistema ainda permite que o cadastro seja configurado com o parâmetro '**Fatura Cliente Direto**', que pode ser filtrado no momento de imprimir um documento de Nota Fiscal, o qual retorna os dados do Cliente/Fornecedor do Movimento ou os dados do Representante relacionado a este Movimento.

 O campo código é um campo obrigatório.

A tela de **Defaults Contábeis**não será implementado na primeira versão da migração, por se tratar de uma tela de outro produto, que é customizada pelo **TOTVS Gestão de Estoque, Compras e Faturamento.**

No **TOTVS Gestão de Estoque, Compras e Faturamento** o **Cadastro de Representantes** está localizado no seguinte caminho: **BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Representantes** 

#### Regras e Campos

* Apenas o campo **código** é obrigatório, porém ele pode ser editado após a inclusão.
* No seguinte caminho **BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | **Gestão de Estoque, Compras e Faturamento | 04.01 Parâmetros Gerais | 04.01.04 Tabelas | 04.01.04.08 Representante**** é possível parametrizar os seguintes itens:
  + Máscara do campo código
  + Nome da Tabela.
  + Descrição Representante.

#### Migração

Para o **Cadastro de Representantes** do **TOTVS Gestão de Estoque, Compras e Faturamento** serão desenvolvidas telas Web utilizando o TOTVS HTML Framework. 

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro. 

##### Tabelas Utilizadas

* TRPR

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
