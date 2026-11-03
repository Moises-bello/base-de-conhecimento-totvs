---
content_hash: f8720a5748520670f480e12d86e624dc785e0e9bcaf6f4aa05e2d419c1ff1cd9
fetched_at: '2026-06-29T00:11:12.236377+00:00'
page_id: '651942057'
product: rm
source: tdn-rm
title: Criação do aplicativo do Azure AD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=651942057
version: 30
---

Índice:

---

.\*ndice:

# Objetivo

---

       A seguir será apresentado o passo-a-passo de como criar um aplicativo do Azure AD para ser usado no RM, como provedor de login.

       Para mais informações sobre as opções de login, acesse o .

# Criando um novo aplicativo do Azure AD

---

**1º-** Acesse o [portal do Azure](https://portal.azure.com/).

Atenção: Para criar um novo aplicativo do Azure AD, é necessário que a instituição tenha um cadastro válido na plataforma do Azure.

**2º-** Pesquise **Azure Active Directory** e selecione-o.

**3º-** Em **Gerenciar**, selecione **Registros de aplicativo** > **Novo registro**.

**4º-** Insira um **Nome** de exibição para o seu aplicativo. Os usuários do seu aplicativo podem ver o nome de exibição quando usam o aplicativo, por exemplo, durante a conexão. No exemplo a seguir usaremos o nome: “TOTVS Login Azure”:

**5º-**Especifique quem pode usar o aplicativo, às vezes, chamado do *público-alvo de entrada*.

**6º-**Não insira nada em **URI de Redirecionamento (opcional)** . Iremos configurar um URI de redirecionamento posteriormente.

**7º-**Selecione **Registrar** para concluir o registro inicial do aplicativo.

Quando o registro for concluído, o portal do Azure exibirá o painel **Visão geral** do registro de aplicativo. Você verá a **ID do Aplicativo (cliente)** . Também chamada de *ID do cliente*, esse valor identifica exclusivamente seu aplicativo na plataforma de identidade da Microsoft.

# Adicionar um URI de Redirecionamento

---

Um *URI de redirecionamento* é a localização para a qual a plataforma de identidade da Microsoft redireciona o cliente de um usuário e envia tokens de segurança após a autenticação.

**1º-** No portal do Azure, em **Registros de aplicativo**, selecione seu aplicativo.

**2º-** Em **Gerenciar**, selecione **Autenticação**.

**3º-** Em **Configurações da plataforma**, selecione **Adicionar uma plataforma**.

**4º-** Em **Configurar plataformas**, selecione o bloco para o tipo de aplicativo (plataforma) para definir as configurações dele. Selecione Web, preencha o campo URIs de Redirecionamento e marque os campos Tokens de acesso (usados para fluxos implícitos) e Tokens de ID (usados para fluxos implícitos e híbridos).

**4º-** Selecione **Configurar** para concluir a configuração da plataforma.

Importante

Para o login com Azure AD apenas no RM.exe basta cadastrar a URI conforme imagem acima, no seguinte formato: [http://{servidor}:{porta}/RMRestCallback/oauth/callback](http://localhost:8051/RMRestCallback/oauth/callback).

Para o login com o RM Portal a URI deste também deverá ser cadastrada no seguinte formato: [http://{servidor}/Corpore.Net/Login.aspx](http://localhost/Corpore.Net/Login.aspx) .

Exemplos: 

* RM.exe: <http://localhost:8051/RMRestCallback/oauth/callback>
* RMPortal:  <http://localhost/Corpore.Net/Login.aspx>

# Adicionar Credenciais

---

As credenciais são usadas por [aplicativos cliente confidenciais](https://docs.microsoft.com/pt-br/azure/active-directory/develop/msal-client-applications) que acessam uma API Web. Exemplos de clientes confidenciais são aplicativos Web, APIs Web ou aplicativos de serviço. As credenciais permitem que seu aplicativo se autentique como ele mesmo, sem nenhuma interação com um usuário no runtime.

Você pode adicionar certificados e segredos do cliente (uma cadeia de caracteres) como credenciais ao registro do aplicativo cliente confidencial.

Obs: No exemplo iremos criar um **segredo do cliente** como forma de ilustrar, porém é aconselhado que se utilize [certificados](https://docs.microsoft.com/pt-br/azure/active-directory/develop/quickstart-register-app#add-a-certificate) em ambiente de produção.

**1º-** No portal do Azure, em **Registros de aplicativo**, selecione seu aplicativo.

**2º-** Selecione **Certificados e segredos** > **Segredos do cliente** > **Novo segredo do cliente**.

**3º-** Adicione uma descrição para o segredo do cliente. Selecione uma data de expiração para o segredo ou especifique um tempo de vida personalizado.

**4º-** Selecione **Adicionar**.

# Autenticação via UPN

---

Click aqui para expandir...

1 - A partir da versão **12.1.2205** patch **12.1.2205.126** foi implementado a opção de realizar a autenticação OAuth via UPN (User Principal Name). Para que essa opção possa ser utilizada, deve-se ter o script de banco de dados atualizado. Para configuração dessa opção, deve-se entrar na tela de "Aplicativos Externos", e no campo “Campo de Correspondência do Provedor” deve ser escolhida a opção “UserPrincipalName” e no campo “Campo de Correspondência do RM” deve ser escolhida a opção “CodExterno”.

Atenção

Para logar no RM usando o UPN(User Principal Name) do Azure AD, é necessário um usuário que tenha acesso ao Azure usando o UPN. Geralmente o usuário administrador possui o "**Emissor de Identidade"** definida como "**MicrosoftAccount**", esse tipo de emissor não consegue logar na Azure AD, utilizando o UPN, apenas o endereço de e-mail relacionado a conta.

Portanto, a configuração padrão do UPN do Azure AD possui o padrão:  
**username@<E-mail of LifeID>.[onmicrosoft.com](http://onmicrosoft.com)** .

Já usuários que foram criados pelo emissor "**MicrosoftAccount**", possuem o padrão:

**second\_username@username\_domain.[onmicrosoft.com](http://onmicrosoft.com)** .

Usuários que forem criados dentro da plataforma Azure pelo usuário Administrador(**MicrosoftAccount**), possuem acesso para usar o UPN como login.

A opção “UserPrincipalName” é o campo “Nome UPN” no campo de usuário no Azure AD

A opção “CodExterno” está disponível na tela de Usuário do RM, na aba “Informação adicional” campo “Código externo”

2 - Para que o sistema possa buscar corretamente a informação do UPN, deve ser informado a URL “me” do graph azure, essa url é o endpoint que contém o UPN. Ela deve ser informada na tela de “Aplicativos Externos” do RM no campo “Url de recuperação da user principal name”. <https://graph.microsoft.com/v1.0/me>

3 - Para que a busca do UPN ocorra corretamente, o registro de aplicativo externo cadastrado no Azure AD e informado no RM, deve ter a opção “user.read” cadastrada no menu “Permissões de APIs” com acesso de administrador.

3.1 - Caso essa opção não esteja cadastrada, clique na opção “Adicionar uma permissão”.

3.1.1 - Escolha a opção “Microsoft Graph”

3.1.2 - Escolha a opção “Permissões delegadas”

3.1.3 - Busque por “user.read”, na seção de “User” escolha a opção “User.Read”

3.2 - Após adição da permissão, conceda a permissão de administrador na opção “Conceder consentimento do administrador para Diretório Padrão”

# Exemplo da configuração no RM

---

Chave Pública (RM) - ID do aplicativo (AzureAD)

Chave Privada (RM) - Valor (AzureAD) 

Url de Autorização - Ponto de extremidade de autorização OAuth 2.0 (v2)  (AzureAD) 

Url de Recuperação do Token de Acesso - Ponto de extremidade do token OAuth 2.0 (v2) (AzureAD) 

Url de Recuperação de Informações da Conta do Usuário - Campo preenchido por padrão com o valor <https://graph.microsoft.com/oidc/userinfo>

Url de Retorno - Campo preenchido por padrão com o valor [http://{servidor}:{porta}/RMRestCallback/oauth/callback](http://localhost:8051/RMRestCallback/oauth/callback). Exemplo: <http://localhost:8051/RMRestCallback/oauth/callback>

Url de Descoberta -  Documento de metadados do OpenID Connect (AzureAD) 

Escopo Padrão - Campo preenchido por padrão com o valor **openid**

[Clique aqui](https://tdn.totvs.com/display/LRM/Aplicativos+Externos) e veja mais sobre a configuração dos aplicativos no RM

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.2205

falsefalse

**Status:** Em andamento

false

**Data:**
