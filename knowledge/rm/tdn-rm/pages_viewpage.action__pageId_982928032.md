---
content_hash: e1ddb5e6b0bac88bdcf393eb647699d8a1a15afcb6f21eb130bad599460b5dd4
fetched_at: '2026-06-29T00:12:16.226843+00:00'
page_id: '982928032'
product: rm
source: tdn-rm
title: Injeção de portais Angular dentro do MDI (RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982928032
version: 1
---

Constantemente temos a necessidade de criar novos portais web que precisam ser injetados no RM (MDI) para nos permitir usar telas mais atuais (Componentes PO-UI com Animalia DS).

Para tal, se faz necessário implementar a autenticação do usuário, porém, por dentro do RM, é importante criar mecanismos para que o usuário já logado não precise realizar uma nova autenticação para cada tela de portal que ele for acessar dentro do sistema.

Para tal finalidade, o time de framework disponibiliza uma biblioteca armazenada no repositório privado da totvs no npm (verdaccio), o qual segue abaixo:

**[@totvs/common-api](https://npm.totvs.io/-/web/detail/@totvs/common-api)**

Essa biblioteca injeta o token do usuário através de **interceptors** para que cada requisição da api já seja enviada autenticada, e o token de acesso é armazenado no Session Storage do navegador com o nome **ERPTOKEN****.**

Além da instalação dessa biblioteca dentro do projeto angular, se faz necessário implementar a lógica para uso do token na inicialização do app, um exemplo dessa implementação pode ser encontrado no repositório interno:

**[Exemplo projeto portal-imobiliario](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/portal-imobiliario?path=/src/app/common/guard/authentication/authentication.guard.ts&version=GBmain&line=49&lineEnd=52&lineStartColumn=1&lineEndColumn=4&lineStyle=plain&_a=contents)**

# **Biblioteca TOTVS Angular Common-Api (Verdaccio) - Uso de token autenticado do RM por dentro da MDI em portais Angular**

# **Configuração do pacote no totvs.io (verdaccio)**

---

No projeto precisa ser incluído um arquivo .npmrc com o conteúdo abaixo para permitir autenticação do usuário (desenvolvedor) no totvs.io (verdaccio):

**registry=<https://npm.totvs.io>**

# **Instalação do pacote no** **totvs.io (ve****rdaccio)**

---

Após incluir o arquivo .npmrc, rode o comando node para autenticar o usuário local no repositório npm da totvs:

**npm logout 2>nul & npm login**

Adicionalmente pode ser incluído no arquivo package.json um script com o comando, a fim de facilitar a execução, conforme exemplo:

# **Server Side -****Injeção da url do portal por dentro do MDI**

---

Para realizar a injeção de um portal angular por dentro do RM, será necessário criar um projeto winforms, que implemente uma classe com herança da classe **RMSActionWebTHF**, conforme exemplo:

Lembrar também de adicionar as configurações de **layerside LayerSideKind.Client** para o projeto criado em winforms, conforme exemplo:

É necessário criar uma classe de webaction que sobrescreva o método **GetRelativeAddress()**responsável pelo redirecionamento para a rota da aplicação em angular, conforme:

E por último, adicionar o novo **item de menu** dentro do menu desejado, definindo a nova **webaction** criada anteriormente como a classe a ser invocada, conforme:

```

```
