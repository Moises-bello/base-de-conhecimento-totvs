---
content_hash: 34eb6fe3cada7ad4b475ea6c1a9ee7d4b555a337a244cc933bfcf358f7b4bd3b
fetched_at: '2026-06-28T21:35:29.009300+00:00'
page_id: '73080143'
product: fluig
source: tdn-fluig
title: Integração da plataforma com o Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73080143
version: 169
---

# Pré-requisitos

---

* Possuir o TOTVS Fluig Plataforma em **atualização 1.6.x ou superior** instalado e configurado conforme as orientações do [Guia de Instalação fluig](https://tdn.totvs.com/x/zAJbDw). O endereço de acesso à plataforma será solicitado durante a configuração da integração com o TOTVS Identity.

* Solicitar um contexto no Identity ao suporte, conforme as orientações da página [Criação de Conta no Identity](https://tdn.totvs.com/x/sAzMCg).

* Possuir uma empresa cadastrada no Fluig.

#f2f2f2#f2f2f2

Tanto para o cadastro da empresa no Fluig quanto para a criação do contexto no Identity é necessário definir um administrador. O endereço de e-mail deste administrador deve ser o mesmo para ambos os casos.

* Caso já existam usuários cadastrados na empresa do Fluig que será sincronizada, **deve-se garantir que todos estes usuários** possuam um endereço de e-mail cadastrado e que este endereço seja válido e único, ou seja, não tenha sido usado no cadastro de outro usuário.
* Caso tenha mais de uma empresa cadastrada no fluig, recomendamos utilizar contas distintas do Identity para configurar a integração com essas empresas. Utilizar a mesma conta do Identity **(URL e token)**, pode impactar no login de usuários que utilizam o mesmo e-mail em diferentes empresas.

exemplo

* + Empresa1 com um usuário: login: user1 e e-mail: [user@company.com](mailto:user1@rmail.com)
  + Empresa2 com um usuário: login: user2 e e-mail: [user@company.com](mailto:user1@rmail.com) (mesmo e-mail)
  + Caso essas 2 empresas no Fluig forem cadastradas com a mesma conta do Identity, o usuário **user2** conseguirá efetuar o login somente na Empresa1, automaticamente impedindo o login na **Empresa2**.

oculto

O procedimento foi repassado ao artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360024961374> (Como integrar a plataforma ao Identity) (Link quebrado)

Caso seja feita alguma alteração, lembrar de repassar a esse artigo.

# Configurar a integração com o Identity

---

Informação:

Para realizar a integração com o Identity, recomendamos que o ambiente fluig esteja em HTTPS. Acesse nossa documentação e confira mais detalhes e informações sobre a [configuração HTTPS da plataforma.](https://tdn.totvs.com/x/vdMgFQ)

De posse dos dados de acesso ao contexto no Identity e um usuário administrador, é possível iniciar a integração com o Fluig.

oculto

Esse procedimento foi repassado ao artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360024961374> (Como integrar a plataforma ao Identity)

Caso seja feita alguma alteração, lembrar de repassar a esse artigo.

false0.5falsesamplesfadePasso 1

O primeiro procedimento da integração é preencher a URL de acesso ao Fluig no aplicativo Fluig do Identity.

* Acesse o contexto criado no Identity, por exemplo, https://[suaempresa].fluigidentity.com, com as credenciais do administrador;
* Clique no menu **Aplicativos**;
* Pesquise por **Fluig** na lista de aplicativos. É possível localizá-lo utilizando o campo **Pesquisar** no canto superior esquerdo;
* Clique na aba **Entrar**;
* Clique em **Editar** localizado no canto superior direito.

Passo 2

* Informe o endereço de acesso ao Fluig no campo **Domínio**;
* Ao final da URL de acesso, deve ser incluído o caminho **/portal/idp**.

#f2f2f2#f2f2f2

Exemplo

[http://meufluig.com:8080/**portal/idp**.](http://ENDERECO_FLUIGPORTA)

* Marque a opção **Sincronizar login SAML com e-mail do AD** (Recomendado);
* Clique em **Salvar** no final da página.

Informação:

Ao acessar o aplicativo Fluig pelo Identity, o usuário será direcionado para o endereço informado neste campo (Domínio), portanto ele precisa ser preenchido com a URL da aplicação Fluig.

Passo 3

Em seguida, deve-se copiar o token do aplicativo.

* Selecione a aba **Visão Geral**;
* Clique em **Token de Configuração**;
* Copie o valor do token, para ser utilizado posteriormente para configuração da empresa no Fluig (**Passo 5**).

Passo 4

A partir de agora, a configuração será realizada no Fluig.

* Acesse o Fluig com o usuário **wcmadmin**;

  #f2f2f2#f2f2f2

  Caso a integração já tenha sido realizada e você está revisitando esta documentação, para acessar com o usuário **wcmadmin**, utilize a seguinte URL: **http://[endereco]:[porta]/portal/home?wcmadmin=true**.
* Acesse o **Painel de Controle** → agrupador **WCM** → **Empresas**.
* Assinale a empresa desejada e acionar **Editar**.

Atenção

Para cada contexto do Identity é suportada a integração com **apenas uma empresa do Fluig**.

Passo 5

* Acesse a aba **Autenticação**;
* Assinale a opção**"Deseja habilitar o acesso com Identity?**"
* Informe a URL do contexto da empresa no Identity;

#f2f2f2#f2f2f2

Exemplo

<https://suaempresa.fluigidentity.com.>

* Informe o token de configuração obtido no **Passo 3**.

Integração entre o Fluig No-Code e Fluig Plataforma

Nesta página é possível habilitar o botão para ativação da integração entre o , caso o usuário tenha o pacote adquirido. Para saber mais a respeito desta integração, acesse a documentação sobre a [Ativação da oferta TOTVS Fluig No-Code.](https://tdn.totvs.com/x/YW10Ig) 

O usuário também poderá observar os  nesta mesma página.

Passo 6

* Para garantir que os dados informados estão corretos e a conexão com o Identity está disponível, clique em **Ações** → **Testar conexão**;
* Se a mensagem "**Conexão com o servidor do Identity realizada com sucesso**" for apresentada, a configuração está correta e pode ser concluída;
* Clique em **Salvar**. A empresa exibirá o status "Habilitado" na coluna Identity da página Empresas.

E os usuários?

Após a integração, é possível  cadastrados no Fluig automaticamente para o contexto da empresa no Identity ou [adicioná-los manualmente](https://tdn.totvs.com/x/NyaTEg).

ocultoVídeo]]>

# Enviar usuários do Fluig para o Identity enviar

---

Para criar contas no Identity para usuários previamente existentes na empresa do Fluig, está disponível nas propriedades da empresa a opção **Enviar usuários**. Ao utilizar este recurso, as contas do usuário no Fluig e no Identity serão vinculadas automaticamente.

oculto

Esse procedimento foi repassado ao artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360024961374> (Como integrar a plataforma ao Identity)

Caso seja feita alguma alteração, lembrar de repassar a esse artigo.

falseenviarPasso 1

* Clique em **Ações** → **Enviar usuários**;

falseCondições de preenchimento do campo idp\_id no banco de dados do TOTVS Fluig Plataforma

A rotina de integração das contas no Fluig e Identity funciona de acordo com as seguintes condições:

**01.** Se no banco de dados do Fluig, o registro do usuário já tiver o campo idp\_id preenchido, ele não será sincronizado.

**02.** Se o idp\_id não estiver preenchido, o usuário será enviado ao Identity:

**2.1** Caso o e-mail deste usuário já esteja cadastrado em uma conta no domínio do cliente no Identity, o seu ID é preenchido na coluna idp\_id da tabela fdn\_usertenant.

**2.2** Caso o e-mail deste usuário já esteja cadastrado em uma conta no Identity, mas atrelado a um outro domínio, ele também será adicionado ao domínio do cliente e o seu ID é preenchido na coluna idp\_id da tabela fdn\_usertenant.

**2.3** Se ele não estiver cadastrado em nenhum domínio, o usuário é criado no Identity, vinculado ao domínio do cliente e o seu ID é preenchido na coluna idp\_id da tabela fdn\_usertenant.

Passo 2

Uma vez utilizado o recurso de **Enviar usuários**, é possível verificar quais contas foram efetivamente criadas e integradas no Identity através do *log* de envio.

* Clique em **Ações** → **Exportar *log* de envio**.

Passo 3

* Será gerado um arquivo CSV contendo as colunas **login**, **e-mail**, **data de envio** e o **status** da operação de criação do usuário.

Passo 4

* Os usuários enviados são automaticamente atrelados ao aplicativo Fluig no Identity.

Passo 5

* Quando o processo é finalizado, os usuários enviados poderão acessar o Fluig pelo Identity.
* A senha destes usuários no Identity será composta da seguinte forma:

#f2f2f2#f2f2f2

[primeiro nome com a primeira letra maiúscula]@123. Por exemplo:

* **Nome do usuário:** John Steel
* **Login no Identity:** [john.steel@empresa.com.br](mailto:john.steel@empresa.com.br)
* **Senha no Identity:** John@123

* Se um usuário enviado pelo Fluig possuir uma conta prévia no Identity, sua senha de acesso não será alterada.
* Caso o primeiro nome do usuário possua 13 caracteres ou mais, a senha será criada usando apenas os 12 primeiros caracteres do nome + @123. Por exemplo, se o nome do usuário for Joriscleidson, a senha gerada será Joriscleidso@123.
* Se o primeiro nome do usuário for muito curto, o Fluig irá adicionar números ao final da senha até atingir o tamanho mínimo exigido pelo Identity (8 caracteres).

#f2f2f2#f2f2f2

Por exemplo, se o nome da usuária for Lu, a senha gerada será Lu@12345.

* Os usuários podem alterar a senha do Identity através da página **Meu Perfil** a qualquer momento.

Informação:

Caso tenha alguma dúvida durante esse processo, verifique a documentação .

# Múltiplas Empresas

---

Quando a instalação do TOTVS Fluig Plataforma possui múltiplas empresas e uma ou mais empresas tiverem a integração com o Identity habilitada, será feita a autenticação por contexto.

Na autenticação por contexto o usuário deverá acessar o Fluig através da URL com o código da empresa, por exemplo, **[http://meufluig.com/portal/empresa1](http://meufluig.com/portal/empresa)**, para que o Fluig identifique em qual empresa o usuário está se autenticando. Caso não seja informado o código da empresa na URL, será apresentada a página de seleção de empresa para que o usuário informe o código antes de prosseguir com a autenticação.

Atenção

A URL de acesso com o código da empresa é válida somente para o acesso à plataforma Fluig, e não deve ser adicionada na configuração do aplicativo no TOTVS Identity.  No Identity permanece a URL normal, que é: <http://meufluig.com/portal/idp>.

Em empresas cuja integração com o Identity está habilitada, o usuário será direcionado para a página de login do Identity. Nas demais, a página padrão de login do Fluig será carregada para autenticação.

Atenção

Cada contexto do Identity suporta a integração com **apenas uma empresa do Fluig**. As demais empresas de uma mesma instalação do Fluig não poderão ser integradas ao mesmo contexto do Identity.

# Consultar token de integração

---

#f2f2f2#f2f2f2

Para consultar o token de integração, siga os passos abaixo:

**01**. Acesse o contexto criado no Identity, por exemplo, https://[suaempresa].[fluigidentity.com](http://fluigidentity.com), com as credenciais do administrador;

**02**. Clique no menu **Aplicativos;**

**03**. Pesquise por **Fluig** na lista de aplicativos. É possível localizá-lo utilizando o campo **Pesquisar** no canto superior esquerdo;

**04**. Na aba **Visão geral**, clique em **Token de Configuração** e copie o valor do token.

oculto

Página Aplicativos para widgets de Experiências de Uso

---

Após a configuração da integração entre Fluig e Identity, uma página chamada Aplicativos será automaticamente criada e incluída no menu principal do Fluig. Essa página contém os *widgets* de Experiência de Uso e Analytics dispostos no seguinte *layout*:

Os 3 primeiros *slots* destinam-se às *widgets* de **Acesso Centralizado**, exibidas nesta ordem: Geral, Favoritos e Mais Acessados. O *slot* inferior à esquerda destina-se ao *widget* de **Consulta Rápida** e o inferior à direita apresenta o *widget* **Analytics**.

falseA1Acesso centralizado

* Os *widgets* de Acesso Centralizado serão automaticamente configurados caso um ERP já esteja integrado ao Identity.

2Consulta rápida

* Para configurar o *widget* de Consulta Rápida, é necessário editar a página e seguir os procedimentos descritos na documentação [Widgets de Experiência de Uso](https://tdn.totvs.com/x/UADvC).

3Analytics

* Para configurar o *widget* Analytics, é necessário editar a página e seguir os procedimentos descritos na documentação [Widgets de Experiência de Uso](https://tdn.totvs.com/x/UADvC).

falseDesativar página Aplicativos e Experiências de Uso

Para que a página Aplicativos não seja exibida no menu principal do Fluig, deve-se acessar o **Painel de controle** → agrupador **WCM** → **Minhas Páginas** e excluir a página.

Para desabilitar as Experiências de Uso, deve-se acessar as propriedades da empresa através do Painel de Controle do usuário wcmadmin (agrupador **WCM** → **Empresas** → **Editar** → **Cadastrar dados adicionais**) e alterar o valor do parâmetro USER-EXPERIENCE-ACTIVE para ***false**.*

]]>
$("b:contains('oculto')").parent().parent().hide();
]]>
