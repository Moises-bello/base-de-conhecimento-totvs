---
article_id: 37535317324823
category: Integrações - Conceito e WebService
content_hash: 2d2883940c8a1c07b04591a6771f23f986676230a5a2e39d06056bf38dbd1609
fetched_at: '2026-06-28T22:46:44.862172+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Como identificar e consumir DataServer e API disponíveis nos
  produtos de RH?
type: support-article
updated_at: '2026-02-04T13:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535317324823-RH-RM-FOP-Como-identificar-e-consumir-DataServer-e-API-dispon%C3%ADveis-nos-produtos-de-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535317307543) Tempo aproximado para leitura: **00:08:03 min**  
  
**Dúvida**  
Para conexão via Webservice, como identificar e consumir **DataServer** e **API** disponíveis nos produtos de **RH da linha RM**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Os produtos de RH da linha RM disponibilizam duas tecnologias para integração e manipulação de dados: **DataServer** e **API (REST)**.  
A seguir, apresentamos as diferenças entre elas e os procedimentos para identificação e consumo.  
  
**Diferença entre DataServer e API**

### 🔹 DataServer

* Presente em **todas as telas do RM**
* Forma **nativa** de comunicação do RM
* Utiliza o formato **XML (SOAP)**
* Permite **consulta, inclusão e alteração** de dados
* Ideal para processos que **ainda não possuem API disponível**

### 🔹 API (Modernização)

* Evolução do DataServer
* Utiliza o padrão **REST / JSON**
* Não está disponível para todas as funcionalidades
* Aderente a padrões modernos de integração

> ⚠️ Ambos permitem **consultar, incluir e alterar dados**, desde que respeitadas as regras de negócio do sistema.

## Escolha a tecnologia desejada

[**Utilizando um DataServer do RM RH**](#utilizandoumdataserverdormrh)

[**Utilizando uma API do RM RH**](#utilizandoumaapidormrh)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**1- DATASERVER**  
[**1.1 - Documentação dos DataServers**](#documentacaodosdataservers)  
[**1.2 - Descobrindo o nome do DataServer desejado**](#dataserver-12)  
[**1.3 - Consumo de DataServer utilizando o SoapUI mesmo sem documentação**](#dataserversoap)  
  
  
**1.1 - DATASERVER - Documentação dos DataServers**  
  
É possível consultar os DataServers disponíveis nos produtos de RH da linha RM através da documentação oficial:

[Documentação oficial dos DataServers](https://apitotvslegado.z15.web.core.windows.net/)

Caso o DataServer desejado **não possua documentação**, ele ainda poderá ser utilizado seguindo os procedimentos descritos nos tópicos abaixo.

**1.2 - DATASERVER - Descobrindo o nome do DataServer desejado**

Para identificar qual DataServer está associado a uma determinada tela do RM:

1. Acesse o **RM**
2. Entre na tela onde deseja **incluir ou alterar registros**
3. Pressione o atalho **CTRL + ALT + F9**

O sistema exibirá o nome do DataServer correspondente à tela.

### Exemplo

Na tela de **Cadastro de Atestados**, o DataServer identificado é SmtAtestadoData:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535317308183)

### 

### Consultando detalhes do DataServer

Para obter informações detalhadas como:

* Chaves primárias
* Tabelas
* Campos disponíveis

Utilize a ferramenta [**TOTVS WS Client**](https://tdn.totvs.com/pages/releaseview.action?pageId=189307798), localizada no diretório de instalação: ...*CorporeRM*\*RM.NET.*

Esta ferramenta tem como objetivo auxiliar a utilização e/ou testar a execução dos DataServers disponíveis no RM. Através da aba **Help**, é possível consultar as chaves primárias, tabela e campos do dataServer.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535317308695)

#### **1.3 - DATASERVER - Consumo de DataServer utilizando o SoapUI mesmo sem documentação**

#### Processo via **SoapUI**

1. Para realizar o consumo dos dados, é necessário, primeiramente, executar um **ReadRecord (Função de consultar dados)** para obter as informações base.

   Para isso, devem ser fornecidas as chaves primárias:

   * **CODPESSOA** (código da pessoa)
   * **SEQATESTADO** (Sequencial Atestados)
   * **DTINICIO** (Data Início Atestado)
   * **CODTPATESTADO** (Tipo Atestado)

   Além das chaves primárias, é imprescindível informar o nome do **DataServer** correspondente, que, neste caso, é o **SmtAtestadoData**.

   Por fim, deve-se especificar o contexto do consumo, fornecendo os seguintes parâmetros:

   * **CODCOLIGADA**
   * **CODUSUARIO**
   * **CODSISTEMA**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535317309591)
2. Após o consumo do DataServer pelo método ReadRecord, será possível extrair uma estrutura XML exemplo na tag **"ReadRecordResult"**, a partir da tag  <![CDATA[ "XML" ]]>.

   Para inserir um novo registro, utilize o método SaveRecord. Informe o nome do DataServer correspondente na chave DataServerName, cole a estrutura XML de exemplo retornada pelo método ReadRecord e informe também o contexto, da mesma forma utilizada na chamada do ReadRecord.  
     
   Atualize os valores base do XML para as informações do novo registro que será inserido. Atente-se ao formato exigido pelas tags, seguindo o mesmo padrão da estrutura XML obtida no ReadRecord.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37538121036439)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### **2- APIs** [**2.1 - Documentação das APIs**](#docapi) [**2.2 - Descobrindo o nome das APIs e testando a comunicação de uma API pelo Swagger**](#nomeapi) [**2.3 - Consumo de API utilizando o Postman mesmo sem documentação**](#apipostman) **2.1 - API - Documentação das APIs**

[**Documentação oficial das APIs**](https://api.totvs.com.br/)

[**Documentação para consultar informações das APIs via Swagger**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058274033-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-API-O-que-%C3%A9-o-Swagger) (O Swagger disponibiliza uma lista com todas as API's disponível do RM, além disso, também permite realizar teste de conexão)

#### 

#### **2.2 - API - Descobrindo o nome das APIs e testando a comunicação de uma API pelo Swagger**

O Swagger estará disponível após a inicialização do serviço de Host em seu ambiente, no endereço:  
**http://{dominio}:{ApiPort}/api/swagger/**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708475399831)

Ao localizar a API desejada, ao clicar sobre ela, será possível consultar a lista detalhada de operações disponíveis. Neste exemplo, estamos utilizando a API de Pessoas (**Person**).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708475401495)

Ao selecionar o método desejado, por exemplo o **GET**, será apresentado um modelo de exemplo detalhado, contendo todas as informações sobre os campos e parâmetros. Para realizar uma requisição diretamente pelo Swagger, clique na opção **“Try it out!”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708489672215)

Em seguida, será solicitada a autenticação por meio das credenciais de um usuário do RM para validar a requisição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708489673239)

Após a autenticação, o resultado da requisição será retornado no campo **“Response Body”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708489674391)

Também é possível realizar operações utilizando outros métodos disponíveis diretamente pelo Swagger. Ao selecionar o método **POST**, será exibido um modelo de exemplo, bem como o campo de texto “**Record**”, no qual é possível informar o **JSON** com os dados preenchidos e executar a requisição clicando novamente na opção “**Try it out!**”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37708489675671)

**2.3 - API - Consumo de API utilizando o Postman mesmo sem documentação**

#### Processo via **Postman** (Rest/APIs)

1. Assim como no **SOAP**, o primeiro passo é obter as informações do **JSON** base para realizar o envio. Para isso, deve-se utilizar a **URL** [**Serviços RESTful**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22322698636823-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-API-Servi%C3%A7os-RESTful-no-RM) e informar o **DataServer** correspondente no método **GET**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37538121038487)
2. Além disso, é importante aplicar um filtro por **ID**, pois, caso o **GET** seja executado sem filtros, todos os registros serão retornados por padrão. Isso pode impactar o desempenho e resultar em alguns campos sendo carregados como **nulos**. Portanto, a aplicação de um **filtro por ID** é essencial para garantir que todos os campos sejam retornados corretamente, com as informações completas para nossa base.

   Copie o campo "**ID**" retornado no primeiro **GET** sem filtro, e cole no final do endereço para realizar uma nova busca. Em alguns casos, pode ser retornado no campo ID algum filtro que tenha espaço, conforme exemplo abaixo:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37538121039639)

   O Postman não aceita espaço na URL, em cenários como este deverá localizar o valor da chave primária retornada no JSON e atualizar o valor do campo no **ID**. Neste exemplo, o espaço na tag ID estava sendo retornada no campo DTINICIO.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37538105400727)

3. Para inserir um novo registro, utilizamos o método Post. Diferente do **GET**, no **POST** **não** é necessário informar o **ID** nem aplicar um **filtro**.

Copie apenas as informações retornadas dentro das chaves { } do Json, e remova apenas o campo ["](https://totvssuporte.zendesk.com/knowledge/editor/01KEF9MS6MHW03QZSDMG5HVJ9F/pt-br?brand_id=1509248&template_id=115015907288&ticket_id=26065093)**ID**"que não deverá ser passado. Atualize os valores dos campos conforme desejado para inserção do novo registro, mantendo o mesmo padrão da estrutura JSON que foi retornada no GET executado com filtro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37538121041559)

**Saiba mais**  
[**Cadastro de Funcionário via WebService/API utilizando o DataServer FopFuncData**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120681945879-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rio-via-WebService-API-utilizando-o-DataServer-FopFuncData)  
[**Cadastro de Pessoa via WebService/API utilizando o DataServer RhuPessoaData**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31234428339607-RH-RM-RHU-Cadastro-de-Pessoa-via-WebService-API-utilizando-o-DataServer-RhuPessoaData)  
[**API disponíveis no TOTVS Folha de Pagamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8558471418135-RH-RM-FOP-Webservices-API-dispon%C3%ADveis-no-TOTVS-Folha-de-Pagamento)  
[**Utilizando o SoapUI para consumir DataServers RM via WebServices**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices)  
[**Lista de DataServers Web Services**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5275823964567-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Lista-de-DataServers-Web-Services)
