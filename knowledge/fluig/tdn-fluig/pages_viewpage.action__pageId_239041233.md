---
content_hash: e2677215d963ceee0a50d2e1dbb9c70d3e6e7f646186fb5ca269bbeb2d52c446
fetched_at: '2026-06-28T21:35:22.779915+00:00'
page_id: '239041233'
product: fluig
source: tdn-fluig
title: Autorização para client de Serviços REST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239041233
version: 58
---

# Índice

3true.\*ndicenone

# Objetivo

---

Para acessar com segurança recursos e serviços externos ao fluig (seja a partir de  ou desenvolvimentos sobre a plataforma), pode-se utilizar o recurso **Serviços REST** no fluig.

Este consiste em um cadastro de configurações de acesso e segurança do serviço externo a ser consumido, ou seja, para cada caso de protocolo de segurança sendo OAuth 1, OAuth 2 ou *Basic* *Authentication**,*serão informados e cadastrados os *tokens* de acesso, chaves, usuário, senha, etc.

Na atualização 1.6.2 do fluig disponibilizamos as autorizações *Custom e None Authentication. Com a Custom*é possível realizar o cadastro de acesso e segurança do serviço externo a ser consumido de forma personalizada, não obedecendo o cadastro padrão fixo do protocolo HTTP. Para acessar um serviço interno que não necessite de autenticação, utilize o *None Authentication*. 

# Cadastro de *client* para chamada a serviços externos

---

Para exibir o cadastro de **serviços REST****,**acesse o fluig com o usuário administrador, acione o menu **Painel de Controle**, localize o agrupador **Desenvolvimento** e acione a opção **Serviços**. O recurso contém opções para inclusão, alteração, exclusão, consulta e teste dos *clients*.

Em atualizações anteriores à **1.6.5 (Liquid)**, esse recurso está disponível no agrupador **Gerais** do ****Painel de Controle****.

Dependendo do *client* de serviço a ser cadastrado, pode-se utilizar mecanismos de autenticação distintos, como OAuth 1, OAuth 2, *Basic, Custom* e até sem autenticação, com o *NONE*. Para cada tipo de autenticação existem informações específicas, que deverão ser preenchidas.

Importante!

A escolha do protocolo a ser utilizado fica a cargo do cliente, bem como a obtenção dos *tokens* e demais informações necessárias para o cadastro do *client*.

## Métodos HTTP suportados

---

* Para tipo de autorização OAuth 1, os métodos HTTP disponíveis são: *PUT, POST, GET, DELETE*.
* Para tipo de autorização OAuth 2, os métodos HTTP disponíveis são: *PUT, POST, GET, DELETE, PATCH*.
* Para tipo de autorização *Basic*, os métodos HTTP disponíveis são: *PUT, POST, GET, DELETE, PATCH*.
* Para tipo de autorização *Custom*, os métodos HTTP disponíveis são: *PUT, POST, GET, DELETE, PATCH*.
* Em Nenhuma Autorização (None), os métodos HTTP disponíveis são: *PUT, POST, GET, DELETE, PATCH*.

## OAuth 1

---

OAuth 1fadetrueCadastro

* Para cadastrar *client* com o tipo de autorização OAuth 1, informar os campos:

| Campo | Condição |
| --- | --- |
| Código do Serviço | Obrigatório |
| Domínio | Obrigatório |
| Tipo de Autenticação | Obrigatório |
| *Consumer Key* | Obrigatório |
| *Consumer Secret* | Obrigatório |
| *Token* de acesso | Obrigatório |
| *Token* secreto | Obrigatório |
| URL *Token* de acesso | Obrigatório |
| URL solicitação de *Token* | Obrigatório |
| URL Autorização de Usuário | Obrigatório |
| URL para teste de Serviço | Opcional |

Imagem

## OAuth 2

---

OAuth 2fadeCadastro

O uso de Refresh Token e da URL Refresh Token se fazem obrigatório para o OAuth 2.0 quando utilizado com um access Token passivo de expiração.

* Para cadastrar *client* com o tipo de autorização OAuth 2, informar os campos:

| Campo | Condição |
| --- | --- |
| Código do Serviço | Obrigatório |
| Domínio | Obrigatório |
| Tipo de Autenticação | Obrigatório |
| Id Cliente | Obrigatório |
| *Client Secret* | Obrigatório |
| *Refresh Token* | Apenas se disponibilizado pelo Serviço |
| *Token* de acesso | Obrigatório |
| URL *Refresh Token* | Apenas se disponibilizado pelo Serviço |
| URL para teste de Serviço | Opcional |

Nota

Para o OAuth 2 utilizamos a autenticação do tipo Baerer

Imagem

## *Basic Authentication*

---

0.5falseBasic AuthfadeCadastro

* Para cadastrar *client* com o tipo de autorização *Basic*, informar os campos:

| Campo | Condição |
| --- | --- |
| Código do Serviço | Obrigatório |
| Domínio | Obrigatório |
| Tipo de Autenticação | Obrigatório |
| Usuário | Obrigatório |
| Senha | Obrigatório |
| Confirmação da Senha | Obrigatório |
| URL para teste do Serviço | Opcional |

Imagem

## *Custom**Authentication*

---

0.5falseCustomfadetrue1Cadastro

* Para cadastrar *client* com o tipo de autorização *Custom*, informar os campos:

| Campo | Condição |
| --- | --- |
| Código do Serviço | Obrigatório |
| Domínio | Obrigatório |
| Tipo de Autenticação | Obrigatório |
| Personalizado | Obrigatório |
| URL para teste do Serviço | Opcional |

2Imagem

## *None Authentication*

---

0.5falseNonefadetrue1Cadastro

* Para cadastrar *client* com o tipo Nenhuma *(None*) autorização, informar os campos:

| Campo | Condição |
| --- | --- |
| Código do Serviço | Obrigatório |
| Domínio | Obrigatório |
| Tipo de Autenticação | Obrigatório |
| URL para teste do Serviço | Opcional |

2Imagem

# Testando configurações de autorização do *client* cadastrado

---

Após o cadastro do *client*, é possível testar as configurações de acesso utilizando a URL para teste do Serviço (*Endpoint GET*) cadastrado. Basta selecionar o *client* e clicar no botão**Testar Serviço:**

# Consumindo o serviço com autenticação OAuth 1, OAuth 2, *Basic Authentication, Custom Authentication e None Authentication*

---

### Chamada via JavaScript

Para consumo do serviço a partir do desenvolvimento de *workflows* ou de desenvolvimento sobre a plataforma, deve-se informar os seguintes parâmetros no Javascript:

#### Como montar os parâmetros?

Para envio dos parâmetros no JSON, é obrigatório utilizar o nome das chaves conforme descrito abaixo.

* ***companyId:** Id da empresa. (sempre com o valor: getValue("WKCompany") + '') em versões recentes este parâmetro é opcional.*
* ***serviceCode*:** Chave única cadastrada.
* ***endpoint*:** *Endpoint* que será chamado.
* **timeoutService:** definir limite de tempo (em segundos) durante a chamada ao serviço, parâmetro opcional.

Para *endpoint*'s que recebem QueryParam e PathParam, os parâmetros devem ser incluídos diretamente no *endpoint*. (endpoint : '/api/public/2.0/users/create?queryParam=exemple',)

* ***method*:** Método HTTP do serviço. (opcional, padrão sendo GET)
* ***params*:** Existem duas maneiras de utilizar este parâmetro, sendo: **params** utilizado para passar o valor em JSON e **strParams**, no caso da utilização deste, o valor a ser passado precisa estar em String.
* ***options*:** Parâmetros em formato JSON para configuração do *request* (se o mesmo não for definido ele vai com as opções padrões que seria encoding: UTF-8 e mediaType: application/json).
* **headers:** Parâmetros em formato JSON para configuração do *header* do *request*

Para habilitar a utilização de serviços REST pelo protocolo SSL, na propriedade **options** é necessário informar **useSSL: true.**

#### Exemplo de chamada aos serviços com HTTP*method**POST*no JavaScript do desenvolvimento

jsEclipsetrue

#### Retorno da chamada

A chamada "clientService.invoke(JSON.stringify(data));" retorna um objeto com os parâmetros abaixo:

* ***companyId:** Id da empresa. (sempre com o valor: getValue("WKCompany") + '')*
* ***serviceCode*:** Chave única cadastrada.
* ***description*:** Informa o *serviceCode* e se obteve sucesso. Ex: "google:SUCCESS".
* ***endopint*:** *Endpoint* chamado.
* ***result*:** *String* com o resultado retornado.
* ***method*:** Método http do serviço.
* **strParams:** Parâmetros em formato *String*.
* ***params*:** Parâmetros em formato *Map*<*String*, *Object*> utilizados.

### Chamada via componente SDK

O recurso para consumo do serviço externo também está disponível no componente SDK através do [AuthorizeClientSdkService.](https://api.fluig.com/old/sdk/com/fluig/sdk/service/AuthorizeClientSdkService.html)

Veja a seguir o exemplo para a chamado ao serviço no SDK:

javaEclipsetrue
