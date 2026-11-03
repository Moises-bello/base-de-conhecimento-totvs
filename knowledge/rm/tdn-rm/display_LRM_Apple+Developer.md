---
content_hash: 5a1709a388f48c2f2fdb8c687d66ba21f35fa700fe24efef6f7178f8e4382ccb
fetched_at: '2026-06-29T00:12:01.447697+00:00'
page_id: '895593822'
product: rm
source: tdn-rm
title: Apple Developer
type: documentation
url: https://tdn.totvs.com/display/LRM/Apple+Developer
version: 1
---

Links

Link para acesso as lojas:

* [App Store Connect](https://appstoreconnect.apple.com)
* [Certificates, Identifiers & Profiles - Apple Developer](https://developer.apple.com/account/)
* [Ajuda da conta de desenvolvedor](https://developer.apple.com/pt/help/account/)
true0.5apple-developerApple DeveloperApple Developerslideusuarios-lojausuariosUsuáriosUsuários100%

# **Administração de usuários**

Convidar usuáriosconvidar-usuárioConvidar usuário

1 - Acesse a opção **"Usuários e acesso"** presente no menu superior. Em seguida clique no botão + em destaque na cor azul.

2 - Para convidar você deverá informar os dados do convidado nos seus respectivos campos. No campo **"E-mail"** informe o endereço de e-mail do novo usuário e as funções do usuário em **"Funções"**.

Se desejar pode ser definido funções adicionais em **"Recursos adicionais".**

Associe um app ao usuario em **"Apps"** e envie o convite em **"Convidar"**. 

permissoesPermissõesPermissões

Os administradores ao convidar um usuário novo deverá conceder acesso as seguintes funções.

**Funções:**

Gerenciador de apps.

AplicativosAplicativosAplicativos100%

# **Administração dos apps**

Administração dos appscriar-appCriar apps

Acesse <https://appstoreconnect.apple.com/apps> e Clique no botão + em destaque na cor azul  ao lado da palavra **"Apps"** para cadastrar as informações do app. Após cadastrar as informações clique em **"Criar".**

certificadosCertificados

Após a criação do app é necessário associar um app a um certificado. Para isso acesse <https://developer.apple.com/account/resources/certificates/list> e clique em **"Certificates, Identifiers e Profiles"**em seguida clique em **"Profiles".**

2 - Para associar o app ao certificado. Siga o passo a passo e no final do processo clique em **"Generate".**

contas-serviçoContas de serviçoContas de serviço

# **Administração Contas de Serviço**

**Essa API REST permite automatizar tarefas em ferramentas de desenvolvedor, como App Store Connect,Xcode e Certificados, Identificadores e Perfis, para oferecer maior flexibilidade e eficiência em seus fluxos de trabalho.**

**Obs.:**Para fazer as configurações de contas de serviço, devemos utilizar o usuário proprietário da loja.

adm-servico-applechaves-appleChaves

1- Acesse a *"****App Store Connect"*** na área de **"Apps"** clique no menu superior **"Usuário e acesso"**e depois clique no menu **"Chave".**

Primeiro acesso

Caso seja a primeira configuração, precisaremos solicitar acesso e confirmar o envio.

2 - Clicar em para incluir uma nova conta de serviço.

* Informe os campos  "**Nome**" e "**Acesso**"**,** depois clique em **Gerar.**

3- Clique em "**Baixar chave de API**" e anote as demais informações destacadas na imagem abaixo, para enviar para o solicitante posteriormente.

Enviar para o solicitante as informações destacadas ( **Issue ID, ID da Chave e Arquivo .p8** )

**Obs.: O Arquivo será gerado com a extensão .p8, com isso será necessário informar ao solicitante que o arquivo precisará ser convertido em base64.**

Revogar acesso

# **Revogar acesso**

Temos a possibilidade de revogar uma chave caso seja necessário, para isso selecione a chave que deseja revogar e clique em "**Editar**" e depois em "**Revogar chave**"
