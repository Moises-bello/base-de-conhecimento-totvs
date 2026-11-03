---
content_hash: d01a7cb2c8442bd3630772c7540b89ad89552133d0a7f635c35381fcad480e11
fetched_at: '2026-06-28T21:35:19.179468+00:00'
page_id: '198934765'
product: fluig
source: tdn-fluig
title: Consumo de serviços na API pública e no componente SDK
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198934765
version: 47
---

Atenção

Esta página foi revisada para considerar as novas configurações de server do fluig para a atualização 1.6.

Caso possua uma atualização anterior do fluig escolha a aba da versão 1.5.13 e anteriores nesta página.

# Índice

true.\*ndicenone

# Objetivo

---

Para utilizar os recursos do componente SDK, existem alguns pré-requisitos e exigências a serem seguidos, como:

* Esta documentação é destinada ao desenvolvedor cliente e parceiro do fluig que deseja consumir interna e externamente os recursos disponíveis na API Pública e no componente SDK.

* As operações na API Pública estão disponíveis através de chamadas REST, que são consumidas via HTTP.

* As operações no componente SDK estão disponíveis após configuração do **fluig-sdk-api** no **classpath** da aplicação dessa forma, através de um **ServiceLocator**, é realizada a chamada ao serviço desejado.

# Consumindo um serviço na API pública

---

Para utilizar um serviço da API Pública, deve ser utilizado o **protocolo OAuth** de autenticação, que através das chaves **Consumer Key**, **Consumer Secret**, configurados no **OAuth App** é gerado através do **OAuth Provider** com um novo **Token Access** e um **Token Secret**.

* O **client** deve ser desenvolvido para suportar autenticação **OAuth 1.0a**.

## Consumindo um serviço do componente SDK a partir de eventos de JavaScript

---

Eventos de Workflow e Eventos de Personalização SocialEste recurso está disponível para eventos javascript de Workflow (que podem ser encontrados [aqui](http://tdn.totvs.com/display/fluig/Desenvolvimento+de+Workflow)) e também para Eventos Sociais (que podem ser encontrados ).

## Exemplos para utilização do componente SDK via eventos de JavaScript

---

**Exemplo 1**

javaEclipse

**Exemplo 2**

javaEclipseObservação

Veja também o [exemplo de uma aplicação web utilizando o fluig SDK](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse/web-sdk) através do artefato **web-sdk**. Diponível no **[git.fluig](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse)**.

# Consumindo um serviço no componente SDK

---

Para utilizar o recursos do componente SDK, existem alguns pré-requisitos e exigências a serem seguidos, como:

* Incluir as configurações do servidor do nexus no Maven para realizar o *download* de artefatos de dependência.

  Importante!

  Para que as dependências sejam baixadas corretamente, é necessário fazer a autenticação no Nexus. Para isso, basta solicitar as credenciais de acesso ao Nexus para o time de Atendimento Fluig.  e saiba como solicitar e utilizar as credenciais.

xmlEclipsesettings.xml



nexus
inserir\_o\_usuário\_fornecido
inserir\_a\_senha\_fornecida


nexus
\*
Fluig Nexus Repository.
http://nexus.fluig.com/content/groups/public
]]>

* Configurar o componente **fluig-sdk-api** no **classpath**.
* No caso de criação de um novo projeto WEB ou Widget, seguir o seguinte padrão de projeto Maven.
* O novo projeto Maven deve ter por padrão as seguintes configurações no **pom.xml**:

0.5falsesamples1fade1fluig 1.6xmlEclipsepom.xml
 

com.fluig
fluig-sdk-bom
1.6.0
pom
import
  

com.fluig
fluig-sdk-api

com.fluig
fluig-sdk-common

javax
javaee-api
provided

fluigsdk.sample


org.apache.maven.plugins
maven-war-plugin
2.2

true
false


org.slf4j, com.fluig.api, com.fluig.api.common
]]>2fluig 1.5.13xmlEclipsepom.xml



com.fluig
fluig-sdk-bom
1.5.0
pom
import


com.fluig
foundation-security-authentication-saml
compile

com.fluig
fluig-sdk-api

com.fluig
fluig-sdk-common

javax
javaee-api
provided

fluigsdk.sample


org.apache.maven.plugins
maven-war-plugin
2.2

true
false


org.slf4j, com.fluig.api, com.fluig.api.common
]]>

* Se atentar para as configurações **padrão de autenticação** e **security-role** localizadas no**jboss-web.xml** e **web.xml**conforme abaixo:

0.5falsesamples2fade1fluig 1.6xmlEclipsejboss-web.xml

/sample
false
TOTVSTech

user
totvstech

totvstech
totvstech

sysadmin
wcmadmin

admin
wcmadmin
]]>2fluig 1.5.13xmlEclipsejboss-web.xml

/sample
false
TOTVSTech

user
totvstech

totvstech
totvstech

sysadmin
wcmadmin

admin
wcmadmin

com.totvs.technology.auth.saml.TOTVSAuthenticatorValve
]]>

* No arquivo **web.xml:**

0.5falsesamples3fade1fluig 1.6xmlEclipseweb.xml
REST

REST
REST
/api/rest/\*

REST
user

FORM,FLUIGAUTH
TOTVSTech

/login.jsp
/loginfail.jsp

totvstech

user

sysadmin
]]>2fluig 1.5.13xmlEclipseweb.xml
totvstech

user

sysadmin
]]>

* Realizar **lookup** do serviço via **ServiceLocator**. Seguir padrão da **Super Classe fluigAPI**.

## Serviços disponíveis no componente SDK

---

* + [ArticleService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/ArticleService.html)
  + [CardIndexService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardIndexService.html)
  + [CardService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardService.html)
  + [CollaborationSDKService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/CollaborationSDKService.html)
  + [CommunityService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/CommunityService.html)
  + [ContentFilesService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/ContentFilesService.html)
  + [DocumentService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/DocumentService.html)
  + [FavoritesService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/FavoritesService.html)
  + [FolderDocumentService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/FolderDocumentService.html)
  + [GlobalParameterService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/GlobalParameterService.html)
  + [GroupService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/GroupService.html)
  + [I18NService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/I18NService.html)
  + [PageService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/PageService.html)
  + [PostService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/PostService.html)
  + [SecurityService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/SecurityService.html)
  + [SocialBreadcrumbService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/SocialBreadcrumbService.html)
  + [TasksService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/TasksService.html)
  + [TenantService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/TenantService.html)
  + [UserService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/UserService.html)
  + [WorkflowService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/WorkflowAPIService.html)

## Exemplo para Instanciar Serviço do SDK

---

Veja a seguir o exemplo para a chamado ao serviço no SDK:

javaEclipse

# Auto completar eventos da fluigAPI

---

Este serviço permite visualizar no **Studio** uma lista com todos os métodos disponíveis no **fluigAPI**. Digitando "**fluigAPI.**" e em seguida apertando o atalho **CTRL + Espaço**, a lista de métodos será apresentada.

Por exemplo, ao usar um método com retorno, **fluigAPI.getWorkflowService()** o usuário poderá listar os métodos deste retorno, como **fluigAPI.getWorkflowService().createObervation()**.

Também é possível criar facilmente os objetos que são utilizados nos métodos.

Para isso, basta digitar, por exemplo, **new ProcessObservationVO** e acionar **CTRL + Espaço** que o plugin irá alterar o trecho automaticamente para **new com.fluig.sdk.api.workflow.ProcessObservationVO();**

Atenção!

Este serviço está disponível a partir da  da plataforma. Siga os procedimentos do  para atualizar o plugin.
