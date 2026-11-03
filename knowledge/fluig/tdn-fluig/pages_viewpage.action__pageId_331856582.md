---
content_hash: e07ec6e015804a50dd7c3a562416d0949007f9abd3f8f583492bebfcdc395a0d
fetched_at: '2026-06-28T21:35:26.072302+00:00'
page_id: '331856582'
product: fluig
source: tdn-fluig
title: Identity | Configurações de aplicativos padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331856582
version: 39
---

# Falando de configurações de aplicativos padrão...

---

O TOTVS Identity oferece duas categorias distintas de aplicativos: [Padrão](http://tdn.totvs.com/pages/viewpage.action?pageId=331856582) e [GoodData](https://tdn.totvs.com/x/ji0PEQ). Aplicativos Padrão oferecem maior versatilidade, pois ao contrário dos apps GoodData, não estão condicionados a um serviço em particular e podem ser integrados com um espectro maior de aplicações.

A categoria de aplicativos Padrão é subdivida por quatro modos distintos de login (autenticação): Aplicativo Thick, Plugin, SAML e Executável SAML.

* **[Thick:](https://tdn.totvs.com/x/IL4KDg)** O modo de login Thick realiza a autenticação em programas *desktop*, como o Skype, com o apoio de uma aplicação chamada Desktop Launcher. O Desktop Launcher preenche automaticamente as credenciais na tela de login dos programas configurados quando estes são executados pelo usuário.

* [**Plugin:**](https://tdn.totvs.com/x/B2AtE) O modo Plugin funciona de forma semelhante ao Thick, mas ao invés de programas, as credenciais são inseridas nas páginas de login de *websites*. Esse processo depende de uma extensão que deve estar instalada no navegador do usuário.

* [**SAML:**](https://tdn.totvs.com/x/8v04E) Aplicativos padrão que fazem uso da autenticação via SAML também são voltados a aplicações *web*, como o [TOTVS Fluig Plataforma](http://tdn.totvs.com/pages/viewpage.action?pageId=73080143), mas não dependem de *plugins* para realizar o login. Contudo, é necessário que a aplicação suporte o padrão SAML para que seja possível integrá-la ao Identity usando este modo de login.

* **Executável SAML:** Também utiliza o padrão SAML para realizar a autenticação dos usuários, mas direcionado para programas *desktop,* [como o Logix](http://tdn.totvs.com/pages/releaseview.action?pageId=192089455)*,* ao invés de aplicações *web*.

## Editar aplicativo padrão

---

**01.** Acione o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acione o nome do aplicativo para visualizar as configurações.

**03.** Acione **Editar**.

**04.** Altere o nome do aplicativo, se desejado.

**04.** Altere a descrição do aplicativo, se desejado.

**05.** Defina ou altere a categoria do aplicativo, se desejado.

**06.** Defina se o aplicativo será navegável ou não.

**07.** Habilite ou desabilite a segurança OAuth 2.0

#f2f2f2#f2f2f2

Determinados aplicativos não permitem habilitar/desabilitar a segurança OAuth 2.0, por exemplo, o aplicativo Fluig.

**08.** Acione **Salvar** para gravar as alterações.

## Trocar logo do aplicativo

---

**01.** Acione o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acione o nome do aplicativo para visualizar as configurações.

**03.**Acione **Trocar Logo**.

**04.** Acione **Carregar imagem** para escolher uma imagem salva na estação de trabalho.

#f2f2f2#f2f2f2

O tamanho de imagem recomendada é de 190x190.

**05.** Ajuste a imagem conforme necessidade.

#f2f2f2#f2f2f2

A interface permite redimensionar a imagem escolhida, dar zoom, girar ou rotacionar, tudo isso para que a logo seja posicionada da melhor forma possível.

**06.** Acione **Concluir**.

## Clonar aplicativo

---

**01.** Acione o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acione o nome do aplicativo para visualizar as configurações.

**03.** Acione **Clonar**.

#f2f2f2#f2f2f2

Será gerado um novo aplicativo idêntico ao original, ou seja, com as mesmas configurações, porém sem os usuários e grupos vinculados e com o nome acrescido de uma numeração, por exemplo, o primeiro clone de um app será nomeado "Aplicativo\_1".

## Copiar token de configuração

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Token de Configuração**.

**04.** Acionar  para copiar o valor do token.

#f2f2f2#f2f2f2

Um dos exemplos de utilização do token é na , em que o valor do token deve ser informado durante a configuração.

## Remover aplicativo

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Editar**.

**04.** Acionar **Deletar Aplicativo**.

**05.** Marcar a opção **Eu compreendo que uma vez que este aplicativo for removido, o mesmo não poderá ser recuperado.**

**06.** Acionar **Confirmar e Deletar**.

#f2f2f2#f2f2f2

O aplicativo será retirado do  dos usuários a que tenha sido atribuído e não poderá mais ser acessado.

Dica

O processo para remover um aplicativo é assíncrono, por este motivo, algumas rotinas internas demoram alguns segundos a mais que a tela espera para responder, por isso, em alguns casos após confirmar a exclusão do aplicativo, sugerimos que recarregue a página ou acione a tecla (F5) do teclado, para de fato visualizar que o aplicativo foi excluído.

## Baixar metadados do IDP

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar a aba **Entrar**.

**04.** Acionar **Baixar metadados do IDP**.

## Atribuir o aplicativo aos usuários

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Usuários**.

#f2f2f2#f2f2f2

Será pré-selecionada a aba Remover Usuários, onde são listados todos os usuários que já possuem o aplicativo atribuído.

**04.** Selecionar aba **Adicionar usuários**.

**05.** Localizar o usuário a quem deseja atribuir o aplicativo.

#f2f2f2#f2f2f2

Serão listados todos os usuários ativos da empresa que ainda não possuem o aplicativo atribuído. É possível utilizar a pesquisa por nome ou e-mail e/ou os filtros para localizar o usuário rapidamente.

**06.** Acionar **Vincular** localizado ao lado direito do nome do usuário.

#f2f2f2#f2f2f2

O aplicativo será adicionado ao  corporativo do usuário.

## Retirar o aplicativo de um usuário

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Usuários**.

#f2f2f2#f2f2f2

Será pré-selecionada a aba Remover Usuários, onde são listados todos os usuários que já possuem o aplicativo atribuído.

**04.** Acionar **Remover** localizado ao lado direito do nome do usuário.

#f2f2f2#f2f2f2

O aplicativo será retirado do  do usuário e não poderá mais ser acessado.

Caso o usuário pertença a um grupo ao qual o aplicativo também foi atribuído, é necessário remover o usuário do grupo para retirar o aplicativo.

## Atribuir o aplicativo aos grupos

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Grupos**.

#f2f2f2#f2f2f2

Será pré-selecionada a aba Remover Grupos, onde são listados todos os grupos que já possuem o aplicativo atribuído.

**04.** Selecionar aba **Adicionar grupos**.

**05.** Localizar o grupos ao qual deseja atribuir o aplicativo.

#f2f2f2#f2f2f2

Serão listados todos os grupos da empresa que ainda não possuem o aplicativo atribuído. É possível utilizar a pesquisa por nome e/ou os filtros para localizar o grupo rapidamente.

**06.** Acionar **Vincular** localizado ao lado direito do nome do grupo.

#f2f2f2#f2f2f2

O aplicativo será adicionado ao  corporativo de todos os usuários do grupo.

## Retirar o aplicativo de um grupo

---

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acionar **Grupos**.

#f2f2f2#f2f2f2

Será pré-selecionada a aba Remover Grupos, onde são listados todos os grupos que já possuem o aplicativo atribuído.

**04.** Acionar **Remover** localizado ao lado direito do nome do grupo.

#f2f2f2#f2f2f2

O aplicativo será retirado do  dos usuários que pertencem ao grupo e não poderá mais ser acessado.

]]>
