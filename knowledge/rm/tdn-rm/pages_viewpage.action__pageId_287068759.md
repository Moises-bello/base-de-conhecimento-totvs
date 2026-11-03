---
content_hash: 2ffea4082496758af3a5d0c93b726a121f1abb69fa60159ae2b694f57e043fcc
fetched_at: '2026-06-29T00:08:42.318444+00:00'
page_id: '287068759'
product: rm
source: tdn-rm
title: Segurança de Serviços HTTP no Host - Configurações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287068759
version: 14
---

# Objetivo

---

Este documento tem como objetivo auxiliar na configuração de segurança dos serviços HTTP (API's) expostos pelo RM Host. Por padrão, o Host já possui padrões de segurança já pré-definidos, porém, caso seja de interesse do cliente, é possível personalizar as informações de segurança, conforme explícito abaixo.

# Parâmetros

---

Para personalizar as informações de segurança de API's é necessário realizar alterações nos arquivos de configuração dos hosts correspondentes (**RM.Host.\*.config**). Na tabela abaixo estão contidos os parâmetros de segurança que são possíveis de serem alterados e mais abaixo, a explicação de cada um destes parâmetros.

| Chave | Tipo | Obrigatoriedade | Valor |
| --- | --- | --- | --- |
| **HOSTAUTHENTICATION** | Valor Específico | Opcional | * ***All (Default)*** * *Basic* * *JWT* |
| **JWTALLOWEDSCOPES** | Texto | Opcional | **OBS.: Este parâmetro ainda não é relevante para a linha RM. Reservado para melhorias futuras.**  Identificadores dos recursos expostos via serviço e que devem estar presentes no JWT. Ex.: api1.write, api1.read |
| **JWTAUDIENCE** | Texto | Opcional | Destinatário do token, representa a aplicação que irá usá-lo. Ex.: api1 |
| **JWTCERTIFICATETHUMBPRINT** | Texto | **Obrigatório** | Identifica o certificado utilizado para validar a assinatura do JWT Ex.: D1AE26F90417AC68D13DC0C734F950541F0CCB36 |
| **JWTISSUERNAME** | Texto | Opcional | O nome da API/fornecedor do token (Caso não seja fornecido, a assinatura será feita como*"totvs-rm-host*"). Ex.: https://sts.totvs.com.br |

* **HOSTAUTHENTICATION**

O RM possibilita a autenticação de diversas formas pelas API's, conforme a documentação: . Esta tag de configuração permite que o host aceite apenas um tipo de autenticação ao invés de todos suportados, que é o valor padrão da configuração. Caso seja escolhido um método específico, os outros naturalmente rejeitarão qualquer tentativa de autenticação, retornando o [**HTTP Error 401 - Unauthorized**](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/401).

xml

Na configuração acima, o host só aceitará chamadas que utilizem de **bearer token** em suas tentativas de autenticação.

## Parâmetros Específicos da Autenticação via Token (OAuth2/JWT)

* **JWTAUDIENCE**

Este parâmetro é opcional, e irá determinar quais destinatários/aplicações irão utilizar o token.

xml

* **JWTCERTIFICATETHUMBPRINT**

Caso o objetivo seja utilizar um certificado digital personalizado para registro de tokens JWT, garantindo assim ainda mais segurança para sua aplicação (Vide ), este parâmetro é obrigatório, afinal ele receberá a assinatura (*Thumbprint*) do certificado personalizado salvo no servidor. Caso este parâmetro não seja fornecido, o RM irá registrar os tokens utilizando um certificado padrão embutido e assinado pelo próprio RM

xml

* **JWTISSUERNAME**

Este parâmetro recebe o fornecedor do certificado digital personalizado, caso este seja fornecido (Veja **JWTCERTIFICATETHUMBPRINT**). Este fornecedor será enviado no JWT e será utilizado por aplicações exteriores que façam uso da autenticação com o RM, como o . Caso não seja fornecido, o fornecedor será enviado como *"totvs-rm-host*" automaticamente.

xmlPor padrão, o RM certifica e valida um token padrão do sistema, porém, **para um nível maior de segurança, é recomendada a implementação de um certificado confiável próprio para validação**. Instruções mais detalhadas para implementação podem ser encontradas em 

Abaixo o exemplo de uma configuração de certificado digital para JWT válida:

O certificado para validação de tokens JWT deve estar na pasta Pessoal da máquina local:

# Validação de JWT

---

Para confirmar que o token não foi adulterado durante a comunicação entre aplicações e o RM, é necessário validá-lo e para isso, *é necessário possuir a chave pública responsável pela assinatura do JWT*. Como a assinatura de tokens de segurança do RM funciona de forma assimétrica (Qualquer aplicação é capaz de validar o token recebido pelo RM, através de chaves públicas, porém *apenas o RM é capaz de assinar um token de segurança*, através de chaves privadas), a API de JWKS fornece a lista de JWK's possíveis para validação do token:

false

Para mais informações acerca de **Json Web Tokens (JWT)** e toda a arquitetura, acesse: [Json Web Tokens - jwt.io](https://jwt.io/), [RFC7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519), [RFC7515 - JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515), [RFC7516 - JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516), [RFC7517 - JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517) e [RFC7518 - JSON Web Algorithms (JWA)](https://datatracker.ietf.org/doc/html/rfc7518)

# Exemplos

---

Chamando endpoint via Postman

1. Endpoint protegido sem autenticação:
2. Endpoint protegido com HTTP Basic:
3. Endpoint protegido com Bearer Token (JWT):

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XXXX

false

**Processo:** Estrutura de segurança de serviços HTTP

falseÍndice

.\*ndice:none

falsefalse

**Status:** Em desenvolvimento

false

**Data:**

false

**Autores:**
