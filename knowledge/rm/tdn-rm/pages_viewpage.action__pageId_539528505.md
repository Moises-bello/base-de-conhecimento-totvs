---
content_hash: db705bd4119b336e97e5cd4646e7c7c6daf96dad2bfe4d64d274b87759cf0aeb
fetched_at: '2026-06-29T00:10:37.296167+00:00'
page_id: '539528505'
product: rm
source: tdn-rm
title: Autorização / Autenticação em API's
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539528505
version: 26
---

## **Introdução**

A maior parte das API's do RM exigem que seja realizada a autorização/autenticação para concluir a chamada, por razões de segurança. Neste documento, serão explicadas e definidas as possíveis formas de autenticação para consumo de API's do RM, suas vantagens e desvantagens e como utilizá-las.

---

## **Indíce**

**Abaixo estão contidos os tipos de autenticação suportados pelas API's do RM:**

Sumário

## **Autenticação Bearer (Bearer Authentication)**

---

Como definido pelo Swagger, uma **Autenticação Bearer** utiliza de *tokens de segurança* para realizar a autenticação entre servidor, que gera este token e client, que repassa esse token como prova de que está fazendo uma chamada confiável.

> **Autenticação Bearer** (também chamada de Autenticação com token) é um [Esquema de autenticação HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) que envolve tokens de segurança chamados de bearer tokens. O nome Bearer Authentication ou Autenticação Bearer vem do inglês e pode ser entendido como "Permita o acesso ao portador deste token" O bearer token é uma informação textual encriptada, normalmente gerado pelo servidor em resposta à uma solicitação de login.
>
> Para mais informações, acesse: [Bearer Authentication - Swagger](https://swagger.io/docs/specification/authentication/bearer-authentication/)

Dentro do RM, é possível gerar um token, em formato JWT (Json Web Token) que será utilizado como token de autorização nas API's do sistema. Existem duas formas de se gerar este token, que iremos explicar agora:

Todos os tokens são gerados em **server-side**, pelo Host do RM

### **Token assinado pelo RM/TOTVS**

Por padrão, o RM realiza a geração e assinatura de um token utilizando as credenciais padrões embutidas no sistema, não necessitando, apesar de recomendado, de ser incluído um certificado válido manualmente.

Por padrão, o RM certifica e valida um token padrão do sistema porém, **para um nível maior de segurança, é recomendada a implementação de um certificado confiável próprio para validação,**

### **Token assinado por um certificado digital do cliente**

O RM também permite que seja inserido um certificado próprio do cliente, certificado este possuído apenas por ele e assim, mais seguro do que o padrão. Para realizar a configuração deste certificado dentro do RM, siga os passos abaixo:

**INSTALAÇÃO DE CERTIFICADO**

* Antes de realizar a configuração de um certificado digital para geração de tokens no RM, é necessário instalar o certificado no servidor da aplicação. Para realizar essa instalação, siga a documentação: 

  Apesar de a documentação de instalação de certificados seguir os passos para um certificado de SSL, os passos são os mesmos mas lembre-se de validar se o certificado digital utilizado suporta a assinatura de tokens

**CONFIGURAÇÃO**

* Para gerar um token **assinado** por um certificado digital do cliente, é necessário:

• Um certificado válido (Conforme passo anterior).

• Acrescentar no arquivo de configuração do Host (**RM.Host.exe.config** | **RM.Host.Service.exe.config**) as seguintes informações:

• **Tag JWTCERTIFICATETHUMBPRINT (Obrigatório):** Este é o thumbprint do certificado. Para conseguir este thumbprint, siga o **passo 7** da documentação de instalação do certificado ()

**• Tag JWTISSUERNAME (Opcional):**O nome da API que gerou o Token (Caso não seja fornecido, a assinatura será feita como *"totvs-rm-host*").

**• Tag JWTAUDIENCE** **(Opcional):** Destinatário do token, representa a aplicação que irá usá-lo.

### **Como utilizar**

Abaixo estão as instruções de como buscar um **bearer token**, tanto com base em um certificado embutido automaticamente na aplicação quanto um inserido manualmente.

**Exemplo de utilização - Sucesso:**

1. Realize uma requisição **POST** ao endpoint **http(s)://{dominio}:{porta}/api/connect/token/** via **Postman**, **SoapUi**, ou outro programa que realize requisições **HTTP REST**.
2. No corpo da requisição envie um JSON explicitando **usuário e senha** do RM para qual a autenticação está sendo direcionada:

• **username**  
• **password**

perlMidnightComando cUrl (pode ser copiado para o Postman)

A requisição deve parecer com a abaixo

O token de segurança será gerado e já poderá ser utilizado no cabeçalho das requisições subsequentes às **API's** disponibilizadas pela **TOTVS**.

Exemplo de **Token de Segurança** gerado com sucesso e pronto para ser utilizado:

Utilize o token gerado incluindo-o no cabeçalho da requisição através da diretiva:

**• Authorization: Bearer {token}**

Inclusão do token no cabeçalho da requisição:

Após a inclusão do cabeçalho de autorização, realize uma requisição HTTP em uma das API's disponibilizadas pela **TOTVS** e verifique o resultado.

Requisição realizada na API de Usuário utilizando o token gerado:

Verifique que a requisição foi realizada com sucesso e os dados foram apresentados corretamente.

falseVer mais - Exemplo utilização - Falha

• Falha na requisição. Token expirado:

### **Gerar Token Informando Alias**

Na versão 2306, é possível gerar um **token** passando o **"service\_alias"** no corpo da API **"connect/token"**, evitando a necessidade de configurar completamente o subdomínio em alguns casos.

**"service\_alias" =** informar o Alias que precisa para gerar o Token.

Abaixo segue a chamada para gerar um **token** utilizando um "Alias".

jsJson

### **Gerar Token Informando Alias com SubDomainMask**

Para gerar um **token** informando o "**Alias**" com o "**subdomainMask**" corretamente, é necessário que o valor do "**serviceAlias**" seja exatamente igual ao valor do "**subdomainMask**".

Por exemplo, se o domínio for "[cliente1.site.com](http://cliente1.site.com)" e o valor do "**serviceAlias**" for "**cliente1**", o **token** será gerado corretamente.

O "**serviceAlias**" é o valor do "Alias" que está cadastrado no arquivo "Alias.dat".

**Alias.dat**

Caso o domínio seja diferente o **token** não é gerado.

Exemplo: **cliente1.site.com** diferente de **serviceAlias** que é **cliente2**

Atenção

Caso o ambiente esteja configurado com **multitenancy** e a "**subdomainMask**" seja diferente da **URL**, o token não será gerado.

### **Duração do Token**

A duração do token de acesso pode ser visualizada na resposta da API de geração de token. Sua duração padrão é de 5 minutos, e pode ser alterada, através da *tag* **JWTTokenExpireMinutes**, que pode ser inserida no *RM.Host.exe.config*, podendo ser configurada entre 1 e 43200 minutos (30 dias).

Já o *refresh* token tem a duração padrão de 16 horas, e também pode ser alterada, mas através da *tag* **JWTRefreshTokenExpireMinutes**, podendo ser configurada entre 1 e 129600 minutos (90 dias).

A alteração da duração do token somente está disponível no RM a partir da versão 12.1.2310.

### **Renovação do Token**

**Exemplo de utilização - Sucesso:**

Realize uma requisição http ao endpoint **http(s)://{dominio}:{porta}/api/connect/token/** via **Postman**, **SoapUi**, ou outro programa que realize requisições http rest.

Na requisição deve-se utilizar o método **POST**.

No corpo da requisição utilize no body:

• refresh\_token  
• grant\_type

Token de Segurança gerado com sucesso e pronto para ser utilizado:

A partir da versão 12.1.2205, foi adicionado um serviço que é inicializado na subida do "Rm.Host" e executa de 5 em 5 horas. Este serviço executa a limpeza dos Refresh\_Tokens expirados da tabela GAPITOKENS.

## **Validação de JWT**

---

Para confirmar que o token não foi adulterado durante a comunicação entre aplicações e o RM, é necessário validá-lo e para isso, *é necessário possuir a chave pública responsável pela assinatura do JWT*. Como a assinatura de tokens de segurança do RM funciona de forma assimétrica (Qualquer aplicação é capaz de validar o token recebido pelo RM, através de chaves públicas, porém *apenas o RM é capaz de assinar um token de segurança*, através de chaves privadas), a API de JWKS fornece a lista de JWK's possíveis para validação do token:

false

Para mais informações acerca de **Json Web Tokens (JWT)** e toda a arquitetura, acesse: [Json Web Tokens - jwt.io](https://jwt.io/), [RFC7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519), [RFC7515 - JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515), [RFC7516 - JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516), [RFC7517 - JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517) e [RFC7518 - JSON Web Algorithms (JWA)](https://datatracker.ietf.org/doc/html/rfc7518)

## **Autenticação Basic**

---

A autenticação do tipo **Basic**não é recomendada pelo seu baixo nível de segurança. Sempre que possível, opte pela autenticação **Bearer** explicada acima

**COMO UTILIZAR**

**Exemplo de utilização - Sucesso:**

Realizando autenticação Basic no Postman:

falseVer mais - Exemplo utilização - Falha

Perceba que o código HTTP 401 (Unauthorized) foi apresentado, quando o usuário, por algum motivo, não pode ser autenticado na aplicação.

• Falha na autenticação do Usuário **"teste":**
