---
content_hash: 560c77727f9ffa306340e4e521ca424a2baae5b71f38918a8e466e97698b85b2
fetched_at: '2026-06-28T21:35:22.122017+00:00'
page_id: '235321507'
product: fluig
source: tdn-fluig
title: Identity | Introdução à API REST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235321507
version: 39
---

4true.\*ndicenone

# Visão Geral

---

O objetivo deste guia é apresentar a API REST para desenvolvedores. A documentação a seguir fornece uma introdução às APIs REST V2 do TOTVS Identity.

#### Para quem é voltada esta documentação?

Desenvolvedores de uma empresa que seja cliente do Identity. Desenvolvedores podem consumir APIs REST básicas para criar seus próprios clientes ou para fazer uma melhor integração entre seus softwares aplicativos e o Identity.

Atenção

Esta documentação é voltada à API REST específica do TOTVS Identity. Para consultar a documentação da API do TOTVS Fluig Plataforma, acesse .

#### O que eu devo saber?

O esquema de autenticação e autorização das APIs REST V2 do Identity são baseadas no padrão de autenticação servidor a servidor OAuth 2.0 utilizando JWT (JSON Web Token). 

Dependendo do caso de uso, o cliente (empresas ou parceiros) terá suas chaves privadas dedicadas para assinar/criptografar seu token JWT e enviá-lo para autorização para conseguir um access\_token e um refresh\_token.

Para mais detalhes, sinta-se à vontade para pesquisar sobre OAuth 2.0 e JWT.

* [Identity API REST](https://app.fluigidentity.com/rest/doc/#/)
* [Nova API REST TOTVS Identity (core)](https://app.fluigidentity.com/api/core/doc/#/)
* [Nova API REST TOTVS Identity (auth)](https://app.fluigidentity.com/api/auth/doc/#/)

# Plataforma

---

A plataforma REST do Identity é baseada nos padrões OAuth 2.0 com JWT (JSON Web Token) para estabelecer a comunicação servidor-a-servidor entre aplicativos.

Mais informações sobre JWT e OAuth 2.0 podem ser encontradas nos links a seguir:

* [JWT Draft](http://tools.ietf.org/html/draft-jones-oauth-jwt-bearer-04)
* [OAuth 2.0 Draft](http://tools.ietf.org/html/draft-ietf-oauth-v2-31)
* [Google’s JWT usage with OAuth2.0](https://developers.google.com/accounts/docs/OAuth2ServiceAccount)

## Escopo do Identity para APIs REST

---

O Identity foi desenvolvido ao redor do conceito de "empresas". Cada empresa possui seu próprio subdomínio, por exemplo, <https://totvs.fluigidentity.com>, e seu próprio conjunto de dados (Ex: aplicativos, grupos). Cada software aplicativo integrado ao Identity terá acesso **somente aos dados da empresa em que a integração foi configurada**.

Cada empresa possui um Client ID e uma chave privada, que irá permitir o acesso aos dados específicos de sua empresa utilizando nossas REST APIs.

# Começando

---

Para cada empresa são atribuídos recursos que garantem a segurança de acesso aos dados da empresa: identificador do cliente (ID do Cliente/*client Id*), identificador da empresa (ID da Empresa (ID da Empresa/*company Id*) e uma chave privada (*private key*). O administrador corporativo pode consultar esses dados através da aba **Segurança** no menu **Configuração** do Identity.

## Crie/Assine o JWT

---

### Criando JWT

Um JWT (JSON Web Token) possui vários campos (como definidos no padrão) para identificar o cliente que está fazendo a chamada. O único campo obrigatório é o campo "issuer" representado pelo atributo ["iss"](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html#issDef) no JWT. O campo "iss" deve receber o valor do **client id** da empresa.

O JSON Web Token deverá se parecer com o seguinte:

### Assinando o JWT

A assinatura do token JWT demanda vários passos para criptografar e assinar partes específicas do JWT, a fim de gerar o *assertion*. Estes passos são fornecidos como parte do padrão mencionado acima.

Em condições ideais, recomendamos fortemente que sejam utilizadas bibliotecas *open source* que já estejam disponíveis para fazer a assinatura do token JWT. Uma destas bibliotecas é a spring-security-jwt (que o Identity utiliza em seu servidor).

Aqui está um exemplo de código de como criar e assinar um JWT:

java

O **JwtHelper** (utilizado no código acima) é uma classe de ajuda da biblioteca **spring-security-jwt**que se encarrega de toda a criptografia base e assina o jwtClaim com a chave privada fornecida pelo desenvolvedor. O uso desta biblioteca ajuda o desenvolvedor a não se preocupar com questões de segurança e se concentrar apenas em fazer as chamadas REST.

A *string **assertion***deve se parecer com o exemplo abaixo (três partes, cada uma separada por um ponto [.]):

Exemplo de assertion

### Enviando/publicando o JWT para o Identity

A ***assertion***gerada no passo acima precisa ser publicada na URL de autenticação OAuth do Identity juntamente com o **grant\_type**, que é definido como **urn:ietf:params:oauth:grant-type:jwt-bearer** pelos padrões JWT.

A URL para publicar estes dados é: http://{hostname}/rest/v2/oauth2/auth

O **{hostname}**para o servidor de produção do Identity será [https://app.fluigidentity.com](https://app.fluigidentity.com/)

O servidor do Identity irá verificar o JWT e sua assinatura e então irá responder com um JSON, onde:

* **refresh\_token**: token utilizado para obter um access\_token novo, quando o antigo access\_token expirar

* **access\_token**: token utilizando para fazer todas as chamadas API REST. O access\_token faz parte do Cabeçalho de Autenticação em todas as requisições API REST

* **client\_id**: REST client-id do Cliente

* **timeIssuedInMillis:** Quando o access\_token/refresh\_token foi requisitado, em milissegundos.

* **expires\_in:** Quando o access\_token expira. Atualmente, o access\_token expira em 3600 segundos (1 hora)

jsResposta

Se em algum momento o cliente perder o refresh\_token, os mesmos passos acima podem ser seguidos para obter um refresh\_token novo.

## Obtendo um novo *Access* Token com o *Refresh* Token fornecido

---

Assim que o access\_token expirar após uma hora, o refresh\_token gerado na chamada mencionada acima pode ser utilizado para obter um novo access\_token. Simplesmente faça uma chamada POST do refresh\_token, como exemplificado abaixo, e o servidor do Identity irá responder com um novo access\_token.

A URL para publicar o refresh\_token é:http://{hostname}/rest/v2/oauth2/token

O servidor irá responder com o seguinte JSON:

jsResposta

## Fazendo as chamadas com o *Access* Token

---

Uma vez que o access\_token for recebido pelo cliente, todas as chamadas subsequentes que precisam ser feitas para acessar os dados da empresa irão exigir o access\_token como parte do Cabeçalho de Autenticação. Aqui está um exemplo utilizando o [plugin Poster](https://addons.mozilla.org/pt-br/firefox/addon/poster/) no Firefox:

### Com o cabeçalho de autenticação (access\_token)

Chamadas com Access TokenChamada

**Cabeçalho**

Resposta

**Resposta**

jsResposta com o cabeçalho de autenticaçãotrue

### Sem o cabeçalho de autenticação (access\_token)

jsResposta sem o cabeçalho de autenticaçãotrue

## Autenticação para as novas APIs REST

---

Para consultar as novas APIs do TOTVS Identity, não é mais usado o Client ID da empresa no Identity, mas sim usuário e senha de login no Identity;

Acesse o endpoint <https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/token> e preencha os campos *username*, *password* e *domain* (subdomínio do seu Identity):

Após clicar em *Try it out*, o *response* será semelhante ao valor abaixo:

jsResposta

### Geração do token com usuário com MFA

Quando o usuário escolhido possui MFA a geração de token é feita em 2 etapas, a primeira é como passo anterior porém ao clicar em *Try it out*, o *response* será semelhante ao valor abaixo:

jsResposta

Para o segundo passo é usado o mesmo endpoint <https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/token>, porém deve se alterar o grant\_type para "<http://fluigidentity.com/api/mfa/totp>"

O campo MFA\_TOKEN é o token gerado na requisição anterior e o TOTP\_TOKEN é o token do aplicativo ao clicar em *Try it out*, o *response* será semelhante ao valor abaixo:

jsResposta

Utilize o valor do *access\_token* para realizar consultas nos endpoints da Nova API ([core](https://app.fluigidentity.com/api/core/doc/#/) e [auth](https://app.fluigidentity.com/api/auth/doc/#/)). O valor do *access\_token* precisa ser enviado no cabeçalho da requisição, da mesma forma que a requisição para a API antiga (descrito acima), no entanto, deve utilizar o scheme [Bearer](https://tools.ietf.org/html/rfc6750#section-2.1).

Este token terá validade de 10 minutos, para renová-lo, altere o *grant\_type* do endpoint para *refresh\_token* e preencha o campo *refresh\_token* com o valor gerado anteriormente.

## APIs adicionais

---

API com as principais funções do TOTVS Identity:  
<https://app.fluigidentity.com/api/core/doc/>

API com as consultas de relatórios padrão:  
<https://app.fluigidentity.com/api/report/doc/>

API com os eventos padrões de grupos, usuários e aplicativos:  
<https://app.fluigidentity.com/api/events/doc/>

 ]]>
