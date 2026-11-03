---
content_hash: 9461b575e314e08df5a3ea4029a2d11514535a7888886d8e55d3ecf9b4b74e7b
fetched_at: '2026-06-28T21:35:19.212050+00:00'
page_id: '198952866'
product: fluig
source: tdn-fluig
title: Acessar API através do cliente OAuth
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198952866
version: 11
---

# Índice

truenone

# Objetivo

---

Este guia irá auxiliar a acessar a API pública através do cliente OAuth.

# Pré-requisitos

---

Para que se tenha uma compreensão completa destas informações, alguns conhecimentos são considerados pré-requisitos, entre eles:

* Visão geral sobre o fluig
* Visão geral sobre o

# Cadastro das chaves

---

Tendo em mão as *consumer keys*, é necessário cadastrá-las no fluig como um *OAuth App*, utilizando o *provider* padrão, as chaves criptografadas são informadas no cadastro, as descriptografadas são utilizadas no cliente.

# Utilização

---

* Para utilizar o cliente é necessário incluir a dependência:

Dependência
com.fluig
oauth-client
1.0
]]>

* Crie e configure o client para o domínio desejado.

java

* Realize o processo de autenticação, é necessário informar o usuário e senha para autorizar o acesso.

java

* É possível recuperar os *tokens* de acesso, após a autenticação.

java

* Após autenticado o cliente permite assinar outras conexões do tipo *HttpURLConnection*, isso permite fazer realizar chamadas REST.

java

# Exemplo

---

O projeto de exemplo está disponível no [git.fluig.com](http://git.fluig.com). Para fazer *download* do arquivo **oauth-client** [clique aqui](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse).
