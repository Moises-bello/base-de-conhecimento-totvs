---
content_hash: 1c36ce0b46d0cfbbc130b7211bb891dea295133b7e2eb532b0b43d6a292f4b13
fetched_at: '2026-06-28T21:35:27.349624+00:00'
page_id: '544184329'
product: fluig
source: tdn-fluig
title: Identity | Token REST API
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Token+REST+API
version: 7
---

# Falando de token REST API...

---

O Identity foi desenvolvido sob conceito de "empresas". Cada empresa possui seu próprio subdomínio, por exemplo, [https://totvs.fluigidentity.com](https://totvs.fluigidentity.com/), e seu próprio conjunto de dados (Ex: aplicativos, grupos). Cada software aplicativo integrado ao Identity terá acesso **somente aos dados da empresa em que a integração foi configurada**.

Cada empresa possui um Client ID e uma chave privada, que irá permitir o acesso aos dados específicos de sua empresa utilizando nossas REST APIs.

## Obter dados da REST API v2

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Token REST API.** 

**03**. Consulte o **ID da Empresa** (*companyId*), único para cada contexto no Identity.

**04.** Consulte o **ID do Cliente** (*clientId*).

**05.** Acione**Baixar a Chave Privada** para fazer o *download* da chave privada da API REST v2 da empresa no Identity.

#f2f2f2#f2f2f2

Consulte a documentação  para obter mais informações sobre a utilização deste recurso.

## Gerar nova chave secreta da API REST v1

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Token REST API.** 

**03.** Acione **Gerar Novo**.

#f2f2f2#f2f2f2

Um novo ID e uma nova chave secreta serão gerados para a empresa.

]]>
