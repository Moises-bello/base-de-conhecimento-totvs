---
content_hash: b0de7b31f194ba4120b3f8cc365403eb10f607025848bffb52ed90c8c1306b42
fetched_at: '2026-06-28T21:35:17.270203+00:00'
page_id: '1036760805'
product: fluig
source: tdn-fluig
title: Identity | Configuração do Okta como provedor de login no TOTVS Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1036760805
version: 11
---

# Falando de configuração do Okta como provedor de login...

---

Essa documentação aborda os passos necessários para configurar o Okta como provedor de login no TOTVS Identity.

OktaPasso 1

Acesse seu contexto TOTVS Identity com usuário administrador e abra o menu **Configurações > Segurança > Cadastro de provedor e clique em Cadastrar novo provedor**, selecione o tipo Generic.

Passo 2

**Na aba Provedor:**

* Preencha o campo **Nome do provedor** com o nome que será exibido na tela de login para os usuários.
Passo 3

**Na aba Dados do Aplicativo**:

* Preencha o campo **Identificador do Aplicativo no Provedor (Client ID)** com o ID do aplicativo que foi criado no OKTA para acessar o TOTVS Identity;
* Preencha o campo **ClientSecret** com a chave que foi criada no aplicativo do OKTA.
* Marque o campo Self registration para que os usuários sejam criados no TOTVS Identity no primeiro acesso que fizerem pelo OKTA.
* No campo **Escopos**, preencha ***openid***, ***profile*** e ***email***, que são os valores necessários para esta autenticação.
Passo 4

**Na aba Informações de Protocolo:**

* Preencha o campo Tipo de protocolo com OIDC;
* E marque o valor Authorize no campo Fluxo utilizado para autenticação.
Passo 5

**Na aba Endpoints:**

* Para preencher a aba Endpoints do provedor, você precisará acessar o arquivo de well-known do seu ambiente Okta, para abrí-lo, acesse a seguinte url, substituindo o domínio pelo seu domínio na Okta: <https://meusubdominio.com/.well-known/openid-configuration>.
* Essa url é aberta, não é necessário ter usuário logado para visualizar.

O formato do arquivo é conforme exemplo abaixo e ele contém algumas informações necessárias para esta configuração:

Passo 6

**Voltando ao Identity:**

* Deixe o campo Chamada da API /me para busca de usuário autenticado **desmarcado;**
* Preencha o campo **Auth URL** com o valor do campo **"authorization\_endpoint"** do arquivo acima;
* Preencha o campo **URI de troca de tokens com o Provedor** com o valor do campo **"token\_endpoint";**
* Preencha o campo **URI com os certificados do Provedor** com o valor do campo **"jwks\_uri";**
* Preencha o campo **URI com as informações dos usuários pelo Provedor** com o valor do campo**"registration\_endpoint";**
* O campo **URI com o e-mail do usuário deixe vazio.**
Passo 7

**Na aba Configuração do Identity:**

Seguindo para a próxima aba na configuração do Identity, **Informações de busca de autenticação:**

* Preencha o campo **Parâmetro do provedor que contém o ID Token ou o Access Token** com o valor *id\_token***;**
* Deixe vazios os campos **Parâmetro do provedor com o Access Token, Variável com nome do usuário e Variável com sobrenome do usuário;**
* Preencha o campo **Variável com nome completo do usuário** com o valor*name***;**
* Marque o parâmetro **Identificador de nome completo;**
* O campo **E-mail do usuário, preencha com o valor** *preferred\_username;*
* Deixe o campo **Code deve ser enviado por Form Param** vazio**;**
* Marque o valor***Form Param***no campo **Como os parâmetros de autenticação são enviados para o /code.**
Passo 8

**Na aba Validadores de Segurança:**

* Preencha o campo **Emissor do token padrão** com o valor do campo"issuer" do arquivo well-known;
* No campo **Receptor do token padrão,** preencha o valor do ID do aplicativo criado no OKTA para acessar o TOTVS Identity;
* Após salvar a configuração, será listado na aba **Cadastro de provedores** este novo provedor criado;
* Clique no campo  e será copiada a URL de Redirect que deverá ser colocada no aplicativo dentro do OKTA;
* Clique no campo  e será possível adicionar uma imagem customizada para exibição do provedor na tela de login.
Passo 9

**Na aba Dados do Aplicativo:**

* Caso seja necessário alterar o **ClientSecret deste provedor,** edite o provedor criado e preencha o campo **Alterar Senha do Aplicativo no Provedor(ClientSecret)** na aba**Dados do aplicativo**. Caso você edite os demais campos do Provedor, mas o ClientSecret se mantiver o mesmo ainda, não é necessário preencher este campo, apenas preencha quando houver necessidade de alterar o valor.

## Documentações relacionadas

---
