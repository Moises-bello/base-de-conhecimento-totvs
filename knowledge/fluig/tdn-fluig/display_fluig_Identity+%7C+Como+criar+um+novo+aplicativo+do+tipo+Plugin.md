---
content_hash: 5eefade8705d9b9711ef69a849156800ac9fcc5e33e662316f1925ed352fe5d0
fetched_at: '2026-06-28T21:35:24.745436+00:00'
page_id: '271409159'
product: fluig
source: tdn-fluig
title: Identity | Como criar um novo aplicativo do tipo Plugin
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Como+criar+um+novo+aplicativo+do+tipo+Plugin
version: 31
---

# Falando de aplicativo do tipo Plugin...

---

O tipo Plugin refere-se aplicativos *web* que, geralmente, exigem apenas o preenchimento dos campos nome de usuário e senha para autenticação. O Identity utiliza uma extensão do navegador (Chrome, Firefox, Internet Explorer) para injetar essas credenciais no formulário de acesso.

oculto

O passo a passo dessa documentação foi repassado ao artigo <https://totvssuporte.zendesk.com/knowledge/api/articles/360024966414> (Como criar um novo aplicativo do tipo Plugin)

Quando for feita alguma alteração, lembrar de repassar a esse artigo!

# Obter dados para criação do aplicativodados

O primeiro passo para criar o aplicativo é obter os dados do formulário *web* utilizado para autenticação no *site*. Neste guia utilizaremos o serviço de gerenciamento de projetos **JIRA** como exemplo para a criação de um aplicativo Plugin através do navegador Google Chrome.

Esse mesmo procedimento pode servir de base para outros *sites* (diferentes do JIRA) e realizado através dos demais navegadores homologados para o Identity.

falsedadosPasso 1

* Acesse o *site* do serviço que deseja configurar no aplicativo Plugin, nesse caso o JIRA de sua empresa.

Passo 2

* Clique com o botão direito do mouse sobre o campo de texto onde deve ser informado o nome de usuário (login) e selecione a opção **Inspecionar**. O navegador apresentará o código-fonte da página com o campo selecionado já em evidência.

Passo 3

* Localize o parâmetro *name*, que identifica o nome do campo de login. No exemplo abaixo, o valor do *name* é "os\_username".

**Clique para ampliar**

E se o campo não tem name?

Caso o campo do formulário de autenticação não possua o parâmetro *name*, pode ser utilizado o parâmetro id.

Passo 4

* Realize o mesmo procedimento com o campo de senha da página e localize o parâmetro *name*. No exemplo abaixo, o valor do *name* é "os\_password".

**Clique para ampliar**

Passo 5

* Localize no código-fonte da página, próximo aos campos usuário/senha, a tag *form*, que representa o formulário de acesso, e os parâmetros *name* e *action*.

* No exemplo abaixo, o valor do *name* é "loginform" e do *action* é "#".

**Clique para ampliar**

Passo 6

* Ao final desse processo, os seguintes dados do formulário devem ter sido coletados para a criação do aplicativo Plugin:

| Campo | Exemplo |
| --- | --- |
| URL da página de login | [http://jira.suaempresa.com.br/secure/Dashboard.jspa](http://jiraproducao.totvs.com.br/secure/Dashboard.jspa) |
| Campo Nome do Usuário | os\_username |
| Campo Senha | os\_password |
| Nome do Formulário de Login | loginform |
| Ação do Formulário de Login | # |

# Criação de um novo aplicativo Plugin

De posse dos dados do formulário, acesse a empresa no Identity para dar continuidade à criação do aplicativo.

falsepluginPasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

Passo 2

* Acione o botão **Novo aplicativo** e selecione a opção **Padrão**.

* Na aba **Visão Geral**, informe o nome e uma descrição para o aplicativo, e acione **Salvar**. As demais propriedades do aplicativo, como Categoria e Logo poderão ser definidas futuramente.

* Acesse a aba **Entrar** e acione o botão **Editar**.

Passo 3

* Na aba **Entrar** serão configurados os campos do formulário que devem ser preenchidos automaticamente pelo *plugin* do Identity. config

* Para isso utilize os dados coletados no  e preencha os valores nos respectivos campos. Ao final, clique em **Salvar**.

**Clique para ampliar**

E se a página usar ID ao invés de name?

Caso o formulário de acesso do *site* utilize parâmetros id para os campos de usuário e senha, ao invés do parâmetro *name*, marque as opções **Campo de Nome do Usuário é ID** e **Campo de Senha é ID**. Se a tag *form* da página também não possuir o parâmetro *name*, e apenas o id, preencha esse último no campo **ID do Formulário de Login**.

Passo 4

* Uma vez configurado e salvo, o aplicativo pode ser disponibilizado no Launchpad dos usuários.vincular

* Acesse os helps para verificar como incluir apps [para os usuários](https://tdn.totvs.com/x/xrrHEw#Configura%C3%A7%C3%B5esdeaplicativospadr%C3%A3o-Atribuiroaplicativoaosusu%C3%A1rios) ou [para os grupos](https://tdn.totvs.com/x/xrrHEw#Configuraçõesdeaplicativospadrão-Atribuiroaplicativoaosgrupos).

Passo 5

* Ao invés de atribuir o novo aplicativo diretamente a usuários/grupos, o administrador pode apenas disponibilizá-lo publicamente para que os usuários interessados incluam o aplicativo em seus Launchpads manualmente. Para isso, basta habilitar a opção **Navegável** localizada na aba **Visão Geral** do aplicativo.

# Utilização do aplicativo

Após a criação do aplicativo, os usuários cadastrados no contexto da empresa no Identity poderão utilizá-lo para autenticar-se no *site*/serviço.

falseutilizaçãoPasso 1

* Se o novo aplicativo criado pelo administrador já estiver disponível no Launchpad do usuário, avance para o Passo 2.

* Caso o administrador ainda não tenha  o aplicativo ao usuário, ou a algum dos grupos a que ele pertence, o usuário deve clicar no botão **Adicionar App** do Launchpad.

* Será apresentada a lista de aplicativos navegáveis da empresa. O usuário deve buscar pelo aplicativo desejado (por exemplo, "JIRA Corporativo") e clicar no botão **Adicionar**.

* O aplicativo será listado no Launchpad do usuário com a observação "Não Configurado".

Passo 2

* Clique sobre o botão em forma de engrenagem no canto do ícone do aplicativo para exibir a barra lateral de propriedades.

Passo 3

* Na barra lateral exibida, informe o login e senha de acesso ao *site* configurado no aplicativo e clique no botão **Salvar**.

* Clique no botão **Esconder**, no canto esquerdo da barra lateral, para retornar ao Launchpad.

Passo 4

* Por fim, clique sobre o ícone do aplicativo no Launchpad para acessá-lo. Uma nova aba será aberta no navegador e as credenciais informadas no aplicativo serão injetadas no formulário de acesso ao serviço (neste exemplo, o JIRA).

* Caso o navegador ainda não possua a extensão do Fluig Identity instalada, um alerta será apresentado orientando o usuário a realizar a instalação. Uma vez concluído esse procedimento, o aplicativo deve ser acessado novamente.

**Instalação da extensão do Fluig Identity para Google Chrome. A extensão também está disponível para Internet Explorer e Mozilla Firefox.**

Passo 5  

* No Google Chrome, especificamente, pode ser exibida uma janela de confirmação como a mostrada abaixo. Caso isso ocorra, deve ser selecionada a opção **Sair**, para que o navegador saia da tela de login e acesse o serviço.

**Clique no botão Sair, caso uma janela de confirmação como a acima seja apresentada pelo navegador Google Chrome.**

# JavaScript customizado

---

Atenção

A partir da versão 1.3.4 do plugin TOTVS Identity não é permitida a utilização de JavaScript customizado.

Em aplicativos do tipo Plugin, caso a extensão do Identity não seja capaz de incluir as credenciais apenas com os campos HTML informados na , em virtude da forma como a página de login foi desenvolvida, pode ser criado um JavaScript customizado para injetar os dados de acesso no formulário de autenticação.

Quando um código for informado no campo **Javascript Customizado** da aba **Entrar** nas configurações do aplicativo, os demais campos serão ignorados.

**O código customizado deve ser incluído nas configurações do aplicativo, no campo Javascript Customizado**

Embora não exista um JavaScript padrão, capaz de funcionar com qualquer página de login da *Web*, o exemplo abaixo pode ser utilizado como base para o desenvolvimento. Ele se aplica a formulários que usam botões *submit* para confirmar o acesso.

jsExemplo genérico de JavaScript customizado
]]>

# Acessando aplicativos do tipo Plugin no Mobile

O **TOTVS Identity** é compatível com os *browsers* mobile e pode ser acessado a partir do seu smartphone, no entanto, o aplicativo do tipo plugin no Identity depende de uma extensão para navegador, que atualmente é desenvolvida apenas para os navegadores Chrome e Firefox. Infelizmente, estes navegadores possuem algumas limitações na versão mobile que não permitem a execução das extensões como em um navegador desktop.

Se você não usa aplicativos plugin, não terá nenhum problema com os navegadores comuns, mas se você usa, não se preocupe, você poderá acessar o **TOTVS Identity** através do [Yandex browser with protect](https://play.google.com/store/apps/details?id=com.yandex.browser). Este browser mobile se comporta como o *browser* Chrome desktop e você poderá instalar a extensão e usar os aplicativos plugin normalmente.
