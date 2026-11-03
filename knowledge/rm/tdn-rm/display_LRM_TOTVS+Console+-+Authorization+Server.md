---
content_hash: 1bbbf7ef4b4a22f6af2e3f22eba28402bde88385213b89b8de54025731907ec1
fetched_at: '2026-06-29T00:08:18.737206+00:00'
page_id: '266966877'
product: rm
source: tdn-rm
title: TOTVS Console - Authorization Server
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Console+-+Authorization+Server
version: 127
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo** | - |
| **Segmento Executor** |  | | |
| **Projeto1** | [TOTVS Console - Fase 1](http://jiraproducao.totvs.com.br/secure/RapidBoard.jspa?rapidView=359&projectKey=FRW_FRW003&view=planning&selectedIssue=FRW_FRW003-2) | **IRM1** | [FRW\_FRW003-1](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-1) |
| **Requisito1** | [FRW\_FRW003-2](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-2) | **Subtarefa1** | [FRW\_FRW003-8](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-8) |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *[Especificações OAuth 2](https://oauth.net/2/)*  *[Especificações OpenId Connect](http://openid.net/connect/)*  *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Uma das responsabilidades do TOTVS Console é prover um servidor de autorização e autenticação OAuth 2.0 e OpenId Connect gerando chaves de acesso para os aplicativos que necessitam consumir os serviços web da TOTVS. 

## Definição da Regra de Negócio

## **OAuth 2.0**

OAuth 2.0 é um protocolo aberto para permitir a autorização segura de forma simples e padronizada para aplicações Web, Mobile e Desktop. 

A segurança baseada em tokens consiste em enviar um token de acesso em cada requisição para acesso à recursos restritos. Um token típico, além de outras informações, contém o que chamamos de escopos (scopes), que representam a intenção do usuário ao acessar determinado recurso, por exemplo: acesso de leitura, escrita, gerenciamento de recursos, etc.

Esta implementação deve ser dividida em três partes:

1. Criar um mecanismo de obter *tokens* de autorização;
2. Criar um mecanismo de validar estes *tokens* no acesso à recursos;
3. Garantir que os recursos não estejam acessíveis caso este *token* não exista;

Importante:

* Esta especificação não trata sobre a forma de envio desses tokens dos clientes para o servidor de recursos. Consumo da API é responsabilidade do OAuth Client.
* OAuth 2.0 é usado para autorizar o acesso. [OAuth 2 não é sobre autenticação](http://oauth.net/articles/authentication/), o padrão não diz nada sobre o usuário e sim sobre o que um aplicativo cliente pode ou não fazer. O aplicativo cliente não conhece nada sobre quem concedeu esta autorização. Para isto existe outro padrão, chamado [OpenId Connect](http://openid.net/connect/).

## Papeis principais

O OAuth 2.0 define quatro papéis principais:

**User (Resource Owner):** Entidade capaz de possibilitar acesso a um recurso protegido. Quando ele é uma pessoa, nos referimos ao usuário final.

**Resource Server:**  É o servidor que hospeda os recursos protegidos capaz de aceitar e responder as solicitações usando tokens de acesso. 

**Authorization Server:** É o servidor capaz de fornecer *tokens* de acesso a um cliente depois de uma autenticação com sucesso do resource owner e obtendo autorização. Chamado de STS (Security Token Service)

**Client:** É a aplicação que acessa um recurso protegido em nome do resource owner e com sua autorização. 

## Fluxos OAuth 2.0

Há uma distinção importante a ser feita com relação aos aplicativos clientes. Dependendo do tipo de cliente é preciso utilizar uma maneira diferente de obter o *token* para se manter seguro. Não existe uma única maneira segura para todos os tipos de clientes. Estas maneiras são chamadas de Fluxos.

Uma das restrições podem ser entendidas da seguinte forma: quando uma aplicação solicita um token de autorização em nome de um usuário, onde este token pode ser entregue? 

#### Authorization Code

Normalmente utilizado por aplicações que são processadas em um servidor, por exemplo uma aplicação web ASP.NET MVC. Necessita de um interação com o usuário para conceder a autorização.

#### Implicit

Normalmente utilizado aplicações nativas, baseadas em um navegador, por exemplo, uma aplicação Angular JS ou um aplicativo móvel. Necessita de um interação com o usuário para conceder a autorização.

#### Resource Owner Password Credential

Normalmente utilizado em aplicações confiáveis, pois ela deve coletar as credenciais do usuário e obter a autorização munido dessas credenciais. Não necessita de uma interação com o usuário para conceder a autorização, pois já foram utilizadas as suas credenciais.

#### Client Credentials

Este fluxo é utilizado para interação direto do aplicativo cliente com o servidor de recursos. Não existe um usuário envolvido neste fluxo. São utilizadas credenciais do próprio cliente.

## Tipos de Clientes

**Confidential Client:** É o cliente capaz de manter confidencialidade das suas credenciais. Estamos falando de credenciais de clientes e não de usuários. Tipicamente temos um *ClienteId* e um *ClientSecrect*. Ex.: MVC App (Server to Server)

**Public Client:** São incapazes de manter a confidencialidade de suas credenciais. Aplicativos Mobile, ou baseados no browser. Ex.: Mobile App, JS App.

## Endpoints

Authorization Endpoint:  utilizado pelo cliente para obter autorização do resource owner através de redirecionamento. OAuth 2.0 não especifica a forma como o resource owner deve se autenticar, isso significa que normalmente o redirecionamento se dará para uma página de login.

Token Endpoint: utilizado pelo cliente para trocar um código de autorização por um *token* de acesso (*client authentication*).

Redirection Endpoint: ponto do cliente onde será recebido o *token*. Os fluxos apresentados são baseados em redirecionamento. Utilizado pelo servidor de autorização para retornar respostas contendo as credenciais de autorização para o *client*.

## OpenId Connect

O OpenId Connect 1.0 é uma extensão para identidade sobre o protocolo OAuth 2.0. Com ele temos mais um token no fluxo, chamado de "id token", o qual permite que aplicativos clientes tenham acesso à identitidade do usuário final permitindo implementar a funcionalidade de autenticação. Mais detalhes na [especificação](http://openid.net/specs/openid-connect-core-1_0.html).

## Identity Server 4

A implementação de um servidor de autorização ou STS - *Security Token Service*, não é trivial. Precisaríamos desenvolver diferentes fluxos, pontos de extremidade, ter um meio de gerar *tokens* e mais. Por isto, vamos utilizar um framework chamado [Identity Server 4](https://github.com/IdentityServer/IdentityServer4).

É uma implementação open source, extensível, faz parte do .NET Foundation, mantida pela comunidade .NET apoiada pela Microsoft. Ela já está preparada também para o .NET Core, permitindo assim que o TOTVS Console seja utilizado ambientes Windows, Linux e OSx.

Conforme, determinado na especificação OAuth 2.0, um STS necessita de alguns dados de Configuração (Clients e Scopes) e gera dados operacionais (Tokens auto-contidos, Tokens de Referência, Consentimentos de Autorização).

Para fins de desenvolvimento e testes, o Identity Server 4, fornece mecanismos de armazenamentos dessas informações em memória. Em um ambiente de produção, necessitamos criar mecanismos para armazenamento físico destas informações.

A comunidade open source já fornece uma camada de persistência baseada no Entity Framework Core para armazenamento destas informações em bancos de dados SQL Server. Entretanto, como estratégia para disponibilização do TOTVS Console em ambientes multiplataforma, será criada uma camada de persistência utilizando MongoDB. Mais informações em:

TOTVS Console

O TOTVS Console terá a estrutura de um projeto ASP.NET Core o qual será responsável por expor os endpoints do IdentityServer (STS) dentre outros recursos, como gerenciamento de usuários, ambientes TOTVS (Resource Servers).

Além de expor a infraestrutura do IdentityServer, o TOTVS Console deverá fornecer e integrar páginas para o fluxo de login e consentimento de autorização.  

Para o fluxo de login funcionar corretamente o TOTVS Console deve prover também um serviço de autentição que irá consultar uma fonte de usuários centralizada. Por isso um dos recursos dele será um mecanismo para gerenciamento e armazenamento de usuários. Os registros de usuários poderão ser originados do Fluig Identity ou das próprias linhas de ERP, sendo mesclados e centralizados no TOTVS Console. Mais detalhes em: <linkar espec da parte de usuários>

### Estrutura do Projeto

Termos uma solução chamada TOTVSConsole, que conterá, inicialmente um projeto chamado TC.Host, do tipo ASP.NET MVC Application e utilizará o .NET Core como framework. Esse projeto conterá as páginas e demais classes necessárias para o fluxo de Login, consentimento de autorização. Futuramente poderá ser desmembrado em outros projetos auxiliares.

Nele também estarão contidos as coleções de Clientes, Scopos, Usuários e o mecanismo de persistência em memória para fins de desenvolvimento e testes. Este projeto será evoluído para o seu formato de produção à medida que forem implementadas os demais recursos necessários.

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

## Dicionário de Dados

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
