---
content_hash: 843a94dbc9221f5bf1c84e9cb592596bd6e1c1801dd815e2621ff7470591fe7d
fetched_at: '2026-06-28T21:35:30.327459+00:00'
page_id: '842293735'
product: fluig
source: tdn-fluig
title: Identity | Configuração do Microsoft Entra ID como Provedor no TOTVS Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842293735
version: 11
---

# Falando de configuração do Microsoft Entra ID como Provedor no TOTVS Identity...

---

Essa documentação reúne os passos para a configuração do Microsoft Entra ID como provedor no Identity, que consiste na criação do aplicativo no Microsoft Entra ID, preenchimento dos campos para cadastro do provedor no Identity e então a configuração da autenticação do aplicativo novamente no Microsoft Entra ID.

## Criação do aplicativo no Microsoft Entra ID

---

Para a criação do aplicativo, acesse o Microsoft Entra ID e siga os passos abaixo:

MicrosoftPasso 1

Dentro do Microsoft Entra ID, acesse a opção de **Aplicativos Empresariais,** crie um novo aplicativo que não está na galeria, adicione o Nome para identificar que é o TOTVS Identity e clique em **Criar**.

Passo 2

Depois selecione quem poderá usar a aplicação, isso fica a critério do administrador, clique em**Registrar**:

Será exibida a mensagem de aplicativo criado:

Passo 3

Depois disto, abra o aplicativo criado e copie o valor de **ID do aplicativo**, guarde este valor para ser informado no Identity:

Passo 4

Na aba Permissões de API, Clique em + Adicionar uma permissão > Selecione Microsoft Graph > Escolha Permissões delegadas (Delegated permissions) > Na caixa de pesquisa, digite openid e marque a caixa openid, na mesma pesquisa, digite profile e marque a caixa profile, por fim, pesquise por email e marque a caixa email. Clique em Adicionar permissões na parte inferior.

Voltando à aba Permissões de API, clique em Conceder consentimento do administrador para [Nome da sua Organização] e depois confirme. 

## Configuração do provedor no TOTVS Identity

---

Para realizar o cadastro de um provedor genérido no TOTVS Identity, siga os passos abaixo:

identityPasso 1

Acesse o menu Segurança > **Cadastro de provedor**, clique em Cadastrar novo provedor e selecione a opção **Generic**:

Passo 2

Preencha o nome do provedor com o nome desejado, lembre-se que isso será exibido na tela de login, por exemplo, se você colocar o nome ‘Azure’, será exibido um botão ‘Logar com Azure’ na tela de login. Avance a configuração e no campo Identificador do aplicativo no Provedor, preencha com o valor de ID do aplicativo que foi criado no Microsoft:

Passo 3

No Microsoft, clique em **Credenciais de cliente**para cadastrar um ClientSecret:

Passo 4

Em seguida clique em **Novo segredo do cliente.**Preencha com a descrição que desejar e selecione a expiração, o máximo possível é 24 meses. Lembre-se de que será necessário trocar a chave na configuração do Identity quando a mesma expirar. Clique em **Adicionar** e copie o valor do secret gerado, importante que ao sair dessa tela e voltar, a informação do valor não será mais exibida em tela.

Passo 5

Cole o valor do secret no campo **Senha do Aplicativo** no Provedor na configuração do Identity e preencha o campo de **Escopos** conforme orientado pelo seu provedor. Os escopos mais comuns são: openid, profile e email. Marque o parâmetro **Auto Cadastro** para que os usuários sejam criados no momento em que tentarem o login a partir do Microsoft.

Passo 6

Na tela seguinte, selecione o Tipo de protocolo OIDC e o GrantType Authorize e clique em **Avançar**:

Passo 7

Volte ao aplicativo criado no Microsoft Entra ID e clique em **Pontos de extremidade**:

Copie o valor do campo **Ponto de extremidade de autorização OAuth 2.0 (v2)** e cole no campo **Auth URL**:

Faça o mesmo com o parâmetro **Ponto de extremidade de token OAuth 2.0 (v2)**e cole no campo **Token URI do Identity**.

Passo 8

Siga os passos abaixo para obter e configurar o endereço JWKS:

1. No painel do Microsoft Azure, copie a URL do campo **Documento de metadados do OpenID Connect**.
2. **Abra** essa URL em uma nova aba do seu navegador.
3. Na página de texto (JSON) que aparecer, localize o parâmetro `"jwks_uri"` e **copie somente o valor da URL dele**.

   > *O valor será algo parecido com: `https://login.microsoftonline.com/seu-tenant-id/discovery/v2.0/keys`*
4. Agora, você irá **modificar a URL** que acabou de copiar. Ao final dela, **acrescente** o texto **`?appId=`** seguido pelo seu **Client ID** (ID do Aplicativo).
5. **Cole** a URL completa e modificada no campo **URI com os certificados do Provedor (JWKS)** da plataforma Identity.

   **Exemplo Prático:**

   * **URL copiada do `jwks_uri`:** `https://login.microsoftonline.com/00000xxx-xxx0000-0000-0x0x0x0x/discovery/v2.0/keys`
   * **Seu Client ID:** `000xxx-x00-000-000x-0x0xxx000`
   * **URL final (para colar no campo JWKS):** `https://login.microsoftonline.com/00000xxx-xxx0000-0000-0x0x0x0x/discovery/v2.0/keys?appId=000xxx-x00-000-000x-0x0xxx000`

Passo 9

Clique em **Avançar**na configuração do Identity e no bloco de**Informações de busca de autenticação**preencha o campo **Parâmetro do provedor**que contém o ID Token ou o Access Token com o valor ‘**id\_token**’, esse valor pode mudar dependendo do provedor:

Passo 10

Desça a tela até o campo **Variável com nome completo do usuário** e preencha com ‘**name**’, em seguida marque o campo**Identificador de nome completo**:

Passo 11

Nessa mesma tela, preencha o campo **E-mail do usuário** com o valor ‘**preferred\_username**’ e marque o parâmetro **Code deve ser enviado por Form Param**, em seguida clique em **Avançar**.

Passo 12

Volte ao metadado do aplicativo do Microsoft Entra ID e copie o valor do campo **issuer**:

Cole esse valor no campo **Emissor do token padrão** da configuração no Identity, substituindo o valor **{tenantid}** pelo ID da sua organização no Microsoft Entra ID. Caso tenha dificuldade em encontrar essa informação, utilize a [documentação da própria Microsoft](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) (em inglês).

Passo 13

Por fim, preencha o campo **Receptor do token padrão** com o Audience do provedor, neste caso é o ID da aplicação do Microsoft Entra ID e clique em **Salvar**:

Passo 14

Na tela de provedores cadastrados, clique em **Copiar URL**no provedor que foi cadastrado:

Atenção!

No caso de edição do provedor, o campo **Alterar senha** só deve ser preenchido caso haja necessidade de alteração da senha do aplicativo no provedor do login social.

## Configuração da autenticação no Microsoft Entra ID

---

Volte a aplicação no Microsoft Entra ID e siga os passos abaixo:

autenticacaoPasso 1

Clique em **URIs de Redirecionamento:**

Passo 2

Em seguida Adicione uma plataforma WEB e adicione a URL do Identity como URL de Redirecionamento, em seguida Salve as alterações:

Passo 3

Após isto, é necessário vincular os usuários dentro do Microsoft a este novo aplicativo TOTVS Identity, para que eles possam efetivamente fazer a autenticação no Identity.

## Documentações relacionadas

---

* [Microsoft - Como encontrar seu tenant ID (em Inglês)](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)
