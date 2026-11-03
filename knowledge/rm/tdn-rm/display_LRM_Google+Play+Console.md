---
content_hash: 8fb9f991d0749787ecada47a74e9504817d034682de599101a89574105c7bfcd
fetched_at: '2026-06-29T00:12:01.460746+00:00'
page_id: '895593878'
product: rm
source: tdn-rm
title: Google Play Console
type: documentation
url: https://tdn.totvs.com/display/LRM/Google+Play+Console
version: 1
---

Links

Link para acesso as lojas:

* [Google Play Console](https://play.google.com/console/)
* [Google Cloud Plataforma](https://console.cloud.google.com/)
true0.5google-play-consoleGoogle Play ConsoleGoogle Play Consoleslideusuarios-lojausuariosUsuáriosUsuários100%

# **Administração de usuários**

Convidar usuáriosconvidar-usuárioConvidar usuário

1 - Acesse a opção **"Usuários e permissões"** presente no menu lateral. Em seguida clique no botão **"Convidar novos usuários".**

2 - Para convidar você deverá informar no campo **"Endereço de e-mail"** o endereço de e-mail do novo usuário e as funcões do usuário em **"Permissões da conta"**.

Se desejar pode ser definido uma data para expiração do acesso no campo **"Expiração do acesso".**

Associe um app ao usuario e envie o convite em **"Convidar usuário"**. 

permissoesPermissõesPermissões

Os administradores ao convidar um usuário novo ele deverá conceder acesso as seguintes funções.

**Acesso de apps:**

  - Editar e excluir apps em rascunho.

**Versões:**

  - Enviar para produção, excluir dispositivos e usar a Assinatura de apps do Google Play.

  - Liberar apps para as faixas de teste.

  - Gerenciar faixas de teste e editar listas de testadores.

**Presença na loja:** 

  - Gerenciar presença na loja.

**Feedback dos usuários:**

  - Responder a avaliações

AplicativosAplicativosAplicativos100%

# **Administração dos apps**

Administração dos appscriar-appCriar apps

1 - Clique em **"Criar app"** para cadastrar as informações do app. Após cadastrar as informações clique em **"Criar app".**

token-lojaContas de serviçoContas de serviço

# **Administração Contas de Serviço**

**As contas de serviço permitem acesso à API Google Play Developer Publishing por um aplicativo em vez de um usuário final. Elas permitem o acesso à API a partir de um servidor autônomo, como servidores de criação automática. As ações da API são atribuídas à conta de serviço, e as permissões podem ser configuradas na página de Contas e direitos do usuário.**

**Obs.:** Para fazer as configurações de contas de serviço, devemos utilizar o usuário proprietário da loja.

adm-servicogoogle-cloudGoogle Cloud PlatformGoogle Cloud Platform

1 - Acesse o *Google Cloud Paltform,*clique em "**Contas e Serviços**"  e selecione o projeto "***Google Play Android Developer***";

2 - Clique em "**Criar uma conta de serviço**";

3 - Preencha os detalhes e clique em "**Criar**";

* Informe os campos "**Nome da Conta de serviço**  " e "**Descrição da conta de Serviço**"  e depois clique em "**Criar e Continuar**".

* Selecione o papel "**Usuário de conta de serviço**" e depois clique em "**Concluir**".

4 - Na lista de contas , procure a conta que acabou de criar e clique no "S*ide menu*" e selecione a opção "**Gerenciar Chaves**";

Esse processo irá gerar as chaves de acesso para a conta.

5 - Clique em "**Adicionar chave**" e logo após "**Criar Nova Chave**".

Selecione o tipo de chave recomendado "**Json**".

**OBS.: AO CLICAR NO BOTÃO CRIAR, SERÁ FEITO DOWNLOAD DO JSON COM AS CHAVES, NÃO PERCA ESSE ARQUIVO !!!**

acesso-apiAcesso à APIAcesso à API

1 - Na lista de "**Contas de serviço**" , procure pela conta que foi criada e clique em "**Permitir acesso**";

2 -Adicione o App que será vinculado a essa conta;

3 - Para finalizar o processo , clique em "**Convidar Usuário**"
