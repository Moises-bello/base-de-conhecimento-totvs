---
content_hash: a93abd0a93c275d83c5736e9d5b6dd00d75ba2489e357228e04c71244fef6eae
fetched_at: '2026-06-28T21:35:26.633982+00:00'
page_id: '382557334'
product: fluig
source: tdn-fluig
title: Integração com o G Suite
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382557334
version: 52
---

true.\*ndicenone

---

# Pré-requisitos requisitos

* Fazer o *download* do certificado SAML do contexto ([veja como baixar](https://tdn.totvs.com/x/HZhvI)). Será necessário enviar o certificado para o Google durante a configuração do *Single Sign On* (SSO).

Importante

Ao contrário do [Gmail para empresas](https://gsuite.google.com/products/gmail/), a versão gratuita para consumidores do [Gmail](https://mail.google.com/) não suporta autenticação via protocolo SAML e portanto **não** é coberta pelos procedimentos descritos nessa documentação.

# Gmail para empresas

O Identity dispõe de um aplicativo padrão chamado Gmail Enterprise que pode ser utilizado pelo administrador do contexto para configurar o serviço de e-mail corporativo do Google, o Gmail para empresas.

### Autenticação gmail

A configuração de autenticação SSO (*Single Sign On*) é realizada no aplicativo e também no [Google Admin Console](https://admin.google.com). Confira o procedimento a seguir:

falsegmail\_authtruePasso 1

**01.** Acessar o menu **Configuração** → **Aplicativos**.

**02.** Pesquisar pelo aplicativo **Gmail Enterprise** e clicar sobre o nome para abrir as configurações.

100%100%

Passo 2

**01.** Selecionar a aba **Entrar**.

**02.** Acionar a opção **Editar** no canto superior direito.

**03.** Informe o **Domínio** da empresa no G Suite (essa informação foi definida pelo administrador ao [inscrever a empresa no G Suite](https://support.google.com/a/answer/182080)).

**04.** Acionar **Salvar**.

**05.** Fazer o *download* dos metadados do IDP do aplicativo. Uma informação contida neste arquivo será usada na configuração de SSO do Google Admin Console.

100%100%

Passo 3

**01.** Acessar o Google Admin Console (<https://admin.google.com>).

**02.** Selecionar a opção **Segurança**.

**03.** Expandir **Configurar logon único (SSO, na sigla em inglês)**.

100%100%

Passo 4

**01.** Descer a página até a seção **Configurar Logon único de provedor de identidade de terceiros** e marcar o *checkbox* ao lado do título para habilitá-lo.

**02.** Preencher o campo **URL da página de login** usando a URL "SPInitRedirect" contida no arquivo de metadados () obtido no Passo 2. Exemplo:

[https://minhaempresa.fluigidentity.com/cloudpass/SPInitRedirect/receiveSSORequest/wl19iwktbzegl4cd1426778621960/1](https://joitrei01.customerfi.com/cloudpass/SPInitRedirect/receiveSSORequest/wl19iwktbzegl4cd1426778621960/1)

**03.** Preencher o campo **URL da página de logout** com o endereço "https://[URL do contexto Identity]/cloudpass/login/logout", substituindo [URL do contexto Identity] pelo endereço de acesso à sua empresa no Identity. Exemplo:

<https://minhaempresa.fluigidentity.com/cloudpass/login/logout>

**04.** Preencher o campo **URL para alteração de senha** com o endereço "https://[URL do contexto Identity]/cloudpass/login/forgotPassword", substituindo [URL do contexto Identity] pelo endereço de acesso à sua empresa no Identity. Exemplo:

<https://minhaempresa.fluigidentity.com/cloudpass/login/forgotPassword>

**05.** Para enviar o certificado de confirmação, conforme exigido nos  dessa documentação, acionar **Escolher arquivo**, selecionar o certificado e acionar **Fazer Upload**.

**06.** Acionar **Salvar** para finalizar a configuração.

100%100%

Dica

Ao final desse processo, não esqueça de tornar o aplicativo navegável ou de atribui-lo aos usuários que possuem contas no G Suite.

### Provisionamento

A configuração de provisionamento faz com que usuários do Identity que ainda não possuem contas no G Suite sejam automaticamente criados na ferramenta ao serem atribuídos ao aplicativo.

**01.** Nas configurações do aplicativo Gmail Enterprise, selecionar a aba **Provisionar**.

**02.** Acionar a opção **Editar** no canto superior direito.

**03.** Marcar a opção **Habilitar Provisionamento**.

**04.** Em **Tipo de Autenticação**, selecionar **OAuth 2.0 JWT**.

**05.** No campo **URL REST**, informar <https://www.googleapis.com/admin/directory/v1/users>.

**06.** Em **ID do Cliente**, informar o ID do cliente OAuth gerado pelo Google ao cadastrar uma credencial no [API Console](https://console.developers.google.com/apis/credentials).

A chave privada não precisa ser informada, pois foi definida diretamente no código-fonte do produto.

**07.** Preencher o campo **Nome do usuário do Administrador do Domínio** com o e-mail de um administrador do G Suite.

**08.** No campo **Senha Temporária do Usuário**, definir a senha padrão temporária para os usuários provisionados no G Suite.

**09.** Acionar **Salvar**.

# Agenda

O Identity dispõe de um aplicativo padrão chamado Calendar Enterprise que pode ser utilizado pelo administrador do contexto para configurar a Agenda, o serviço de calendário do Google.

### Autenticação

Além da configuração de autenticação SSO (*Single Sign On*) no aplicativo Calendar Enterprise, é necessário habilitar o SSO no [Google Admin Console](https://admin.google.com), como descrito nos Passos 3 e 4 do procedimento de configuração do Gmail Enterprise ().

falsecalendar\_authtruePasso 1

**01.** Acessar o menu **Configuração** → **Aplicativos**.

**02.** Pesquisar pelo aplicativo **Calendar Enterprise** e clicar sobre o nome para abrir as configurações.

100%100%

Passo 2

**01.** Selecionar a aba **Entrar**.

**02.** Acionar a opção **Editar** no canto superior direito.

**03.** Informe o **Domínio** da empresa no G Suite (essa informação foi definida pelo administrador ao [inscrever a empresa no G Suite](https://support.google.com/a/answer/182080)).

**04.** Acionar **Salvar**.

100%100%

Dica

Ao final desse processo, não esqueça de tornar o aplicativo navegável ou de atribui-lo aos usuários que possuem contas no G Suite.

# Drive

O Identity dispõe de um aplicativo padrão chamado Drive Enterprise que pode ser utilizado pelo administrador do contexto para configurar o Drive, serviço de armazenamento do Google.

### Autenticação

Além da configuração de autenticação SSO (*Single Sign On*) no aplicativo Drive Enterprise, é necessário habilitar o SSO no [Google Admin Console](https://admin.google.com), como descrito nos Passos 3 e 4 do procedimento de configuração do Gmail Enterprise ().

falsedrive\_authtruePasso 1

**01.** Acessar o menu **Configuração** → **Aplicativos**.

**02.** Pesquisar pelo aplicativo **Drive Enterprise** e clicar sobre o nome para abrir as configurações.

100%100%

Passo 2

**01.** Selecionar a aba **Entrar**.

**02.** Acionar a opção **Editar** no canto superior direito.

**03.** Informe o **Domínio** da empresa no G Suite (essa informação foi definida pelo administrador ao [inscrever a empresa no G Suite](https://support.google.com/a/answer/182080)).

**04.** Acionar **Salvar**.

100%100%

Dica

Ao final desse processo, não esqueça de tornar o aplicativo navegável ou de atribui-lo aos usuários que possuem contas no G Suite.
