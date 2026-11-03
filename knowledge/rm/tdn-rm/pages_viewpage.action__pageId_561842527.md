---
content_hash: f5cf0ca21d7062884716b74ad4522a6185529c50772cf4c4cd11eadf18df0223
fetched_at: '2026-06-29T00:10:48.374537+00:00'
page_id: '561842527'
product: rm
source: tdn-rm
title: Integração do RM com Azure AD via SAML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561842527
version: 29
---

# Índice

---

      .\*ndice:

# Objetivo

---

       Este documento demonstra como integrar o sistema RM com o Azure AD como provedor de Identidade.

# Introdução

---

       O Azure AD (Azure Active Diretory) permite o compartilhamento da informação de identidade em um ampla variedade de aplicativos utilizando o padrão SAML que é suportado na linha RM.

# Configurando o Azure AD

---

false

Nessa etapa, iremos realizar as configurações iniciais para a integração entre **RM** e **Azure AD**

Este passo-a-passo será todo instruído utilizando o **Azure AD** no idioma Inglês, porém os passos são os mesmos, independente do idioma

Configurando o Aplicativo Confiável no Azure AD1º Passo - Enterprise Applications:

Antes de mais nada, precisaremos de um "Enterprise Application", pois esta é a aplicação que receberá todas as configurações referentes à integração.

Ao acessar o portal do Azure, selecionamos o serviço "Enterprise Application" para acesso ao assistente de configuração.

2º Passo - Criando uma nova aplicação:

* Clique em 'New application'

* Clique em 'Create your own application' para criar uma nova aplicação.  Preencha o Nome do Aplicativo e clique em 'Create'

* Após a criação, você deve será redirecionado para a página do aplicativo criado.

Atenção

Caso deseje utilizar a integração SSO do RM.exe e do Portal Corpore.Net, **deverão ser criados 2 aplicativos, 1 para o RM.exe e outro para o Portal.**

# Configurando as Regras de Declaração para o aplicativo RM (MDI)

---

falseConfigurando o Aplicativo Confiável no Azure ADbottomConfigurando o Aplicativo

Agora iremos configurar o SSO (Single Sign On) do aplicativo criado com o **RM.exe**.

* Após acessar o cadastro do aplicativo no Azure AD selecione a opção **"Set up single sign on",** para que as configurações sejam exibidas.

* Selecione o método de SSO (Single Sign On) **SAML**:

* Após clicar em SAML, você será direcionado para a página de configuração do aplicativo.

Seguimos para os próximos passos

Configuração SAML Básica

* Após acessar o aplicativo é necessário realizar as configurações básicas do aplicativo. Basta clicar em editar na guia de configurações SAML básicas.

As configurações são:

| Propriedade | Descrição |
| --- | --- |
| Identifier (Entity ID) | Identificador do aplicativo no Azure AD, este valor deve ser exclusivo em todos os aplicativos. |
| Reply URL (Assertion Consumer Service URL) | URL do **provedor de serviços (RM)**  de resposta que o Azure AD enviará uma requisição ao consumir o aplicativo. |
| Sign on URL **(opcional)** | URL de logon do **provedor de serviços (RM).** É utilizado caso o **provedor de serviços (RM)** possua uma página de login. |
| Relay State **(opcional)** | É um campo que serve para redirecionar os usuários após a conclusão da autenticação no **provedor de serviços (RM)** |
| Logout URL **(opcional)** | É a URL que o sistema será redirecionado ao efetuar o Logout. |

* Após clicar em 'Edit', é necessário preencher as informações abaixo

* Preencha os campos abaixo e clique em salvar:

| Chave | Valor | Descrição |
| --- | --- | --- |
| **Identifier (Entity ID)** | **My\_Identifier** | Um **valor á sua escolha**, pois este valor será utilizado para identificar o emissor de uma solicitação, resposta ou afirmação. |
| **Reply URL** (**A**ssertion **C**onsumer **S**ervice URL) | https://**{DOMINIO}**:**{PortaHttp}**/RMCloudPass/SSOSaml2 | Url do **provedor de serviços (RM)**que será responsável por receber a resposta de login do **IDP** (**Azure AD**) |

Atenção

O Identifier (Entity ID) é utilizado no **provedor de serviços (RM)** como **emissor** da requisição, ao realizar o login.

É **recomendado** que o **Identifier** (Entity ID) seja uma URL contendo seu próprio nome de domínio para se identificar.

* Após salvar as configurações básicas ficarão da seguinte maneira

Seguimos para o próximo passo

Atributos e Reivindicações

* Nesta etapa iremos configurar o Atributo para que o **provedor de serviços (RM)** consiga identificar internamente que este aplicativo é o RM.exe. Basta clicar em editar na guia de Atributos e Reinvindicações.

* Após clicar em 'Edit', é necessário alterar o **Unique User Identifier** (Name ID) para **user.mail,**

Por padrão o **Unique User Identifier** (Name ID) vem com o valor user.userprincipalname, porém a chave utilizada para fazer o match do usuário entre o **Identity Provider** (Azure AD) e o **provedor de serviços (RM)**é o **e-mail**.

Após alterar o **Unique User Identifier** (Name ID) é necessário adicionar o atributi  **ExecutablePath** , clique em "Add new claim"

O atributo a seguir será adicionado:

| Atributo | Valor | Descrição |
| --- | --- | --- |
| **ExecutablePath** | "" | Este atributo será enviado para o **provedor de serviços (RM)**onde a partir desta informação ele seguirá a regra de negócio para executar a abertura do RM.exe |

Atenção

O Atributo**não precisa conter valor**, apenas estando na requisição o sistema conseguirá seguir o fluxo de login correto, o comportamento do **provedor de serviços (RM)**  é o mesmo **caso o atributo possua valor**.

Caso o atributo **ExecutablePath** não seja adicionado no aplicativo, a integração seguirá o fluxo de login SSO incorreto.

**Estas informações são sensíveis ao texto, caso a grafia da palavra esteja diferente da documentação, a integração pode não funcionar da maneira correta.**

* Após salvar, os Atributos e Reinvindicações ficarão da seguinte maneira

Seguimos para o próximo passo

5º Passo - Adicionando a URL da aplicação ao XML:

* Agora precisamos do XML que servirá como arquivo de configuração do RM em um momento posterior. Na terceira aba, de nome **SAML Signing Certificate**, baixamos o arquivo **Federation Metadata** XML:

* Agora buscaremos a URL da nossa aplicação no MyApplications. Para isso, acesse o link: <https://myapplications.microsoft.com/> e procure pela aplicação recém-criada no Azure AD

* Clicamos nos 3 pontinhos/dots e selecionamos Copy Link

* Agora no XML que baixamos, vamos ao final dele e nas tags **SingleSignOnService**, definimos a propriedade Location como o link que copiamos no item anterior:

Abaixo temos um código-exemplo de como deve ficar. **LEMBRE-SE DE ALTERAR O LOCATION PARA A SUA URL DO MYAPPS**

xmlRDark

]]>

Salvamos o arquivo e podemos passar para a integração com a MDI.

# Configurando as Regras de Declaração para o aplicativo Portal

---

falseConfigurando o Aplicativo Confiável no Azure ADtrue1º Passo

Agora iremos configurar o SSO (Single Sign On) do aplicativo criado com o **RM Portal**.

* Após acessar o cadastro do aplicativo no Azure AD selecione a opção **"Set up single sign on",** para que as configurações sejam exibidas.

* Selecione o método de SSO (Single Sign On) **SAML**:

2º Passo:

Defina os parâmetros do Aplicativo conforme abaixo.

**1** - **Configuração Básica de SAML**

| Chave | Valor |
| --- | --- |
| *Identificador* | Valor **único** determinado para a aplicação |
| *URL de Resposta* | [http://{endereço}:{porta}/R](https://localhost/CorporeRM/login.aspx)MCloudPass/SSOSaml2 |

Atenção

Caso seja utilizado SSL no ambiente, a *URL de Resposta* deverá ser preenchida com *HTTPS*.

**2** - **Atributos e Declarações**

| Chave | Valor |
| --- | --- |
| *emailaddress* | user.mail |
| *Identificador Exclusivo do Usuário* | user.mail |

Atenção

As configurações do menu de *Atributos e Declarações* devem permanecer exatamente da forma acima, pois é por meio deste identificador que o match do usuário entre o Azure AD e o RM será feito.

**3** - **Certificados SAML**

| Chave | Informação |
| --- | --- |
| *XML de Metadados de Federação* | Arquivo que será inserido no sistema para realizar a integração |

**4** - **Ajuste do atributo entityID no XML de Metadados de Federação**

Após baixar o arquivo de Metadados de Federação (XML), é necessário revisá-lo e, caso o atributo `entityID —` localizado dentro da tag `<EntityDescriptor> —` não contenha o identificador configurado para o aplicativo, o valor deve ser ajustado manualmente.  
  
No exemplo abaixo, o identificador do aplicativo é **RM\_SAML\_Portal**, portanto o XML deve ficar assim:

RDark]]>Observação

O XML de Metadados de Federação baixado do Azure AD é gerado a partir da configuração do tenant (locatário) e, por padrão, utiliza o identificador do serviço do Azure, no formato <https://sts.windows.net/{tenant-id}/>.  
Esse valor representa o provedor de identidade (IdP), e não o aplicativo configurado.  
Por isso, é necessário substituir o valor do entityID pelo identificador do aplicativo (Service Provider – SP) cadastrado no Azure AD, garantindo a correspondência correta durante a autenticação SAML.

Atenção**Para o Portal CorporeRM não é necessário configurar o RelaySate.**

---

# Integração SAML no RM

---

         

Atenção

* Quando a configuração for referente à MDI (RM.exe) o XML baixado deve ser alterado e as URI's de **SingleSignOnService** do aplicativo **RM.exe** deve ser alterada contemplando o **MyApps** tal qual demonstrado no **5º Passo da integração com a MDI**.

* **Importando o metadado do Azure AD no RM**

Após obter o metadados personalizado, ele deve ser importado no RM em: Ambiente → Parâmetros → Parâmetros Globais → Integração SAML

Caso queira integrar o Azure AD com a MDI, via SAML, adicionar o metadado no campo "Metadata Identity Provider - RM.exe"

Caso queira integrar o Azure com o Portal, via SAML, adicionar o metadado no campo "Metadata Identity Provider - Portal".

  

Existe a possibilidade de integrar o **Azure AD** com a **MDI** e o **Portal** de forma simultânea, basta adicionar o metadado nos campos "**Metadata Identity Provider - RM.exe**" e "**Metadata Identity Provider - Portal**".

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.27 e superiores

false

**Processo:** Integração SAML

falsefalse

**Status:** Finalizado

false

**Data:**
