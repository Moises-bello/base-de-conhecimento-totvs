---
content_hash: 59a3e645bc20945f7455a0fc5dcf24387497d4db4c42a5273fbfd51a8c87a700
fetched_at: '2026-06-28T21:35:26.093207+00:00'
page_id: '334343906'
product: fluig
source: tdn-fluig
title: Identity | Configurações de aplicativos GoodData
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334343906
version: 49
---

# Falando de configurações de aplicativos GoodData...

---

Aplicativos GoodData são uma categoria específica de aplicativo disponibilizada pelo TOTVS Identity. Diferente dos aplicativos do tipo [Padrão](https://tdn.totvs.com/x/xrrHEw), que são genéricos e podem ser configurados com virtualmente qualquer serviço, os aplicativos GoodData são pré-configurados para esta aplicação. Para isso, foram definidos dois tipos de aplicativos GoodData: Fluig Analytics e TOTVS Analytics.

Além de configurar o aplicativo, é necessário abrir um ticket para o Suporte TOTVS Identity solicitando que a autenticação SSO (Single Sign On) seja habilitada pela GoodData. [Saiba mais](https://tdn.totvs.com/x/ji0PEQ).

## Editar aplicativos GoodData

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Alterar o nome do aplicativo, se desejado.

**04.** Alterar a descrição do aplicativo, se desejado.

**05.** Definir se o aplicativo será navegável, ou seja, permitir que os usuários se associem ao aplicativo.

**06.** Acionar **Salvar**.

## Excluir o aplicativo

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar o botão **Remover aplicativo**.

**04.** Na caixa de confirmação, acionar **Remover**.

## Baixar os metadados do aplicativo

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar o *link* **Baixar metadados do IDP**.

#f2f2f2#f2f2f2

Os metadados do aplicativo são utilizados para realizar a autenticação SSO (*Single Sign On*) entre o Identity e a GoodData.

## Atribuir o aplicativo aos usuários

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Selecionar a aba **Usuários**.

**04.** Acionar **Adicionar usuários**.

**05.** Localizar no painel os usuários que devem ser adicionados ao aplicativo.

#f2f2f2#f2f2f2

É possível utilizar o campo de pesquisa para filtrar os usuários por nome ou e-mail.

**06.** Acionar o botão **Adicionar** localizado do lado direito do usuário.

#f2f2f2#f2f2f2

O Identity irá solicitar ao fluig/TOTVS Analytics a criação da conta deste usuário na GoodData e a associação dele ao projeto configurado no aplicativo. Usuários preexistentes no projeto não são sincronizados com o Identity; todas as contas criadas a partir de aplicativos GoodData serão novas.

## Retirar o aplicativo de um usuário

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Selecionar a aba **Usuários**.

**04.** Localizar na lista de Usuários adicionados ao aplicativo aquele(s) que deve(m) ser removido(s).

#f2f2f2#f2f2f2

É possível utilizar o campo Filtrar usuários para procurar por nome ou e-mail e o campo Filtrar usuários por grupo para pesquisar apenas usuários de um grupo específico.

**05.** Acionar o botão **Remover** localizado ao lado direito do(s) usuário(s) que deve(m) ser retirado(s) do aplicativo.

#f2f2f2#f2f2f2

O usuário será retirado do aplicativo e uma solicitação para desassociá-lo do projeto será enviada à GoodData. A conta do usuário não é excluída do fluig/TOTVS Analytics.

## Atribuir o aplicativo a grupos

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Selecionar a aba **Grupos**.

**04.** Acionar **Adicionar grupos**.

**05.** Localizar no painel os grupos que devem ser adicionados ao aplicativo.

**06.** Acionar o botão **Adicionar** localizado ao lado dos grupos que devem ser atrelados ao aplicativo.

#f2f2f2#f2f2f2

O Identity irá solicitar ao fluig/TOTVS Analytics que seja realizada a criação da conta dos integrantes deste(s) grupo(s) na GoodData e a associação ao projeto configurado no aplicativo. Usuários preexistentes no projeto não são sincronizados com o Identity; todas as contas criadas a partir de aplicativos GoodData serão novas.

## Retirar o aplicativo de um grupo

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Selecionar a aba **Grupos**.

**04.** Localizar na lista de Grupos adicionados ao aplicativo aquele(s) que deve(m) ser removido(s).

#f2f2f2#f2f2f2

É possível utilizar o campo Filtrar grupos para pesquisar um grupo pelo nome.

**05.** Acionar o botão **Remover** localizado ao lado direito do(s) grupo(s) que deve(m) ser retirado(s) do aplicativo.

#f2f2f2#f2f2f2

Os usuários do grupo serão retirados do aplicativo e uma solicitação para desassociá-los do projeto será enviada à GoodData. As contas dos usuários não serão excluídas do fluig/TOTVS Analytics.

Os integrantes de um grupo associado a um aplicativo do tipo GoodData não podem ser removidos individualmente do aplicativo. É necessário desassociar o usuário em questão do grupo para que o vínculo com o aplicativo seja removido.

## Obter código do aplicativo, URL de acesso direto e URL de *logout* direto

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar o link **Mais informações** localizado ao lado do título Informações do aplicativo.

**04.** Será exibido um painel com o código do aplicativo, a URL de acesso direto e a URL de *logout* direto.

]]>
