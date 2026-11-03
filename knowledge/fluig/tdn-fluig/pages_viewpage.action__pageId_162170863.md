---
content_hash: 31f47225f29c35e75e95769c20848a94e9645a26d6cb1e56015d5e9ff5462e3d
fetched_at: '2026-06-28T21:35:18.579819+00:00'
page_id: '162170863'
product: fluig
source: tdn-fluig
title: Configurando Autenticação Integrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=162170863
version: 53
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é habilitar e configurar a autenticação integrada com Windows no TOTVS Fluig Plataforma.

# Visão Geral

---

A autenticação integrada com o Windows possibilita que os usuários que estejam registrados no Active Directory possam acessar a plataforma sem precisar informar manualmente seus dados de acesso através da tela de login, desde que já esteja autenticado no Windows.

Basicamente o processo de autenticação integrada com o Windows funciona da seguinte maneira:

1. O usuário acessa a plataforma através do seu navegador;
2. A plataforma inicia o processo de autenticação integrada, redirecionando para o servidor IIS;
3. O script de autenticação remota no IIS sabe como autenticar o usuário pelas credenciais de domínio do Windows;
4. O usuário é consultado e validado no Active Directory pelo IIS;
5. IIS redireciona novamente à plataforma com as informações de identidade do usuário retornadas pelo Active Directory;
6. A plataforma valida a integridade das informações recebidas do servidor IIS;
7. Caso as informações do usuário forem válidas, autentica o usuário na plataforma, caso contrário redireciona para a tela de login.

Atenção!

Com essa configuração de autenticação integrada os usuários não são criados automaticamente na plataforma. Eles somente são criados automaticamente quando é utilizado o TOTVS Identity.

# NTLM

---

O NTLM é um protocolo de autenticação utilizado em uma rede Windows. Como veremos nos tópicos a seguir, existem uma série de configurações que devemos realizar nos navegadores para que utilizem este protocolo, e também no script de autenticação remota para que utilize a chamada Autenticação Windows.

Além disso, é importante lembrar que existem limitações com relação a sistemas operacionais que não Windows. Linux e Mac, por exemplo, não podem utilizar o protocolo NTLM. O efeito nestes sistemas operacionais é que se tentarem o acesso via autenticação integrada, uma caixa de diálogo proveniente do navegador pedirá para que o usuário informe suas credenciais.

# Configuração da Autenticação Integrada

---

Para usufruir da autenticação integrada com o Windows, é necessário habilitar este recurso na plataforma e realizar algumas configurações, como a criação do serviço de autenticação remota. As configurações necessárias para o correto funcionamento da autenticação integrada são apresentadas nos tópicos abaixo.

### Habilitando e Configurando na plataforma

O primeiro passo para a configuração da autenticação integrada é habilitá-la na plataforma:

0.5falsefluig-configfadetrue1Passo 1Acessando as configurações do sistema

* Efetue o login na plataforma utilizando o usuário **wcmadmin**, e então acesse **Painel de Controle  ► WCM ► Configurações do Sistema**.

2Passo 2Habilitar Autenticação Integrada

* Na tela de configurações do sistema, acesse a aba **Autenticação**. Para habilitar a autenticação integrada assinale a opção **Habilitar autenticação integrada.**

3Passo 3URL Script Autenticação

* Insira a URL do servidor IIS onde será executado o script de autenticação remota no campo **URL script de autenticação**. A URL deve apontar por padrão para **http(s)://<endereço-iis>/remote\_auth.asp** (A configuração do servidor IIS e da URL para acesso será descrito no tópico Configuração IIS).

  Fique atento!

  As máquinas dos usuários devem conseguir acessar a URL configurada em **URL script de autenticação** da forma como ela foi informada nesse campo.

4Passo 4Informar usuário e senha para autenticação

* Clique no botão **Gerar Novo Token** para gerar um token de autenticação. O token é utilizado para validar a integridade e segurança das requisições de autenticação integrada recebidas pela plataforma.

5Passo 5Gerar Token

* Informe o endereço do servidor Active Directory no campo **Endereço do servidor AD** no seguinte formato **<servidor>:<porta>** e o DN (Distinguished Name) base para a pesquisa de usuários no campo **Base DN**. O DN base é utilizado para informar abaixo de qual entrada no Active Directory será pesquisado e validado os usuários para a autenticação integrada.

6Passo 6Salvar Configurações e Exportar Script

* Informe um login e senha do Active Directory que possua privilégios suficientes para ler informações dos usuários no Active Directory informado no passo anterior. O login deve ser informando no campo **Usuário de domínio** e a senha no campo **Senha.**

7Passo 7

* Clique no botão **Salvar** para salvar as configurações de autenticação. Em seguida clique no botão **Exportar** para gerar e salvar o script de autenticação remota que deverá ser publicado no servidor IIS.

É importante lembrar que existem diversas configurações à serem executadas antes que possamos utilizar a Autenticação Integrada, estas serão detalhadas nos tópicos a seguir. Se estas configurações não forem finalizadas antes que a autenticação integrada seja habilitada, os usuários poderão ter dificuldades para autenticar na plataforma, ou até mesmo poderão ser impedidos de ter acesso.

### Configuração IIS

Para disponibilizar o serviço de autenticação remota é necessário ter um servidor Windows com o Internet Information Services (IIS) habilitado. Siga o passo-a-passo abaixo para habilitar o IIS:

Caso a função Servidor Web (IIS) já tenha sido adicionada ao servidor este passo-a-passo pode ser ignorado. Importante apenas garantir que os serviços de função **ASP** e **Autenticação do Windows** tenham sidos instalados para o Servidor Web (para mais detalhes confira o **passo 4**).

0.5falseconfig-iisfade1Passo 1

* Para habilitar o IIS (caso não esta habilitado ainda), devemos utilizar o **Gerenciador de Servidores** e adicionar uma nova função. Para adicionar uma nova função, clique na opção **Funções** e em seguida em **Adicionar funções**.

2Passo 2

* A tela de **Assistente para Adicionar Funções** é aberta. Assinale a opção **Servidor Web (IIS)** e clique no botão **Próximo**.

3Passo 3

* Uma tela com uma introdução ao Servidor Web (IIS) é apresentada. Clique no botão **Próximo** para continuar com a instalação.

4Passo 4

* Para que seja possível configurar e disponibilizar o serviço de **autenticação remota** é necessário a instalação dos seguintes serviços de função: **ASP**, **Extensões ISAPI** e **Autenticação do Windows**. Assinale estes serviços de funções e clique em **Próximo**.

* Os serviços de funções **ASP** e **Extenções ISAPI** são necessários para a execução do script ASP responsável pela autenticação remota e o serviço de função **Autenticação do Windows** é necessário para que o navegador possa enviar as credenciais para a aplicação efetuar as validações necessárias no Active Directory.

5Passo 5

* A tela de confirmação de instalação é apresentada. Clique em **Instalar** para finalizar a instalação do Servidor Web (IIS).

6Passo 6

* Após finalizar a instalação é apresentada a tela de **Resultados da Instalação** com o resumo dos itens instalados. Clique em **Fechar.**

##### Configuração e Disponibilização do Serviço

Após possuir o IIS instalado e com as funções de serviços necessárias é possível configurar o serviço de **autenticação remota**. Lembrando que o apoio da equipe de infraestrutura é fundamental, siga o passo-a-passo abaixo para configurar e disponibilizar o serviço de **autenticação remota**:

0.5falsedsso-app-iisfade1Passo 1

* Primeiramente devemos criar um arquivo chamado **redirect.html** com o seguinte conteúdo (lembre-se que a chave FLUIG-HOST deve ser substituída pelo endereço do servidor fluig).

Lembrando que no campo **URL script de autenticação**, deve ser informado o mesmo nome do domínio utilizado na plataforma, por exemplo, URL='[http://suaempresa.com.br/portal/home?dssoError=invalidUser'](http://suaempresa.com.br/portal/home?dssoError=invalidUser%27)).

xmlredirect.html

]]>

* Seguindo, devemos **criar um diretório** de conteúdo para o site que iremos criar nos próximos passos. Neste diretório colocamos o script ASP baixado da plataforma (ver item ) e o arquivo **redirect.html**.

2Passo 2

* No IIS agora precisamos **criar um novo site,** que será a aplicação responsável em fornecer o serviço de autenticação remota. Para criar um novo site clique na ação **Adicionar Site**. A tela **Adicionar Site** será apresentada, informe o **nome do site** (por exemplo fluigsso), o **tipo**, **endereço IP** e **porta**, que devem ser definidos pelo administrador do servidor.

O endereço informado nas configurações do site é o valor que deve ser informado no campo **URL script de autenticação** na configuração da autenticação integrada na plataforma (ver passo 3 do item ).

3Passo 3

* Outro ponto a ser configurado é autenticação deste site. Realizamos isto através do item **Autenticação**.

4Passo 4

* Devemos habilitar a forma de autenticação do **Autenticação do Windows** e desabilitar todas as outras opções de autenticação.

5Passo 5

* Existe um detalhe que deve ser tratado na autenticação, que são os provedores utilizados pela Autenticação do Windows. Clique com o botão direito na opção **Autenticação do Windows** e em seguida clicar na opção **Provedores**.

6Passo 6

* Devemos deixar apenas a opção **NTLM**. Todas as outras devem ser excluídas. Se isso não for feito, pode ser exigido do usuário a entrada de credenciais via caixa de diálogo do navegador. Não esquecer que existe outra configuração a ser feita diretamente no navegador para evitar este problema (veremos em tópicos posteriores).

7Passo 7

* Em alguns casos, não será possível negociar as credenciais do usuário via **NTML** e então o IIS redirecionará o usuário para uma página de erro (HTTP 401.2 - Não autorizado). Para evitar este comportamento é possível definir uma página de erro personalizada onde o usuário é redirecionado para a página de login da plataforma ao invés de uma página de erro do IIS.
* Realizamos isto através do botão **Páginas de Erro**.

8Passo 8

* Para adicionar uma nova página de erro clique na opção **Adicionar.**

9Passo 9

* A tela **Adicionar Página de Erro Personalizado** é apresentada. Informe o código de status **401.2**, selecione a ação de resposta **Inserir conteúdo do arquivo estático na resposta de erro** e no campo **Caminho do Arquivo** informe o caminho relativo (ou seja, apenas o **nome.extensão**, conforme a imagem abaixo) da raiz do site direcionando para o arquivo **redirect.html**.

* Para finalizar e adicionar a página de erro clique no botão **OK**.

10Passo 10

* Finalizadas as configurações, é possível realizar um **teste** diretamente no script. Para isto basta executar o script no navegador com o parâmetro de consulta debug=1, que neste exemplo foi <http://10.80.128.251:8180/remote_auth.asp?debug=1>
* Quando acrescentado o parâmetro de consulta debug=1, o script é informado para executar em modo debug, no qual ele retorna diversos valores que nos ajudam a depurar o serviço de autenticação remota. No exemplo executado, podemos ver que foi retornado o usuário 'João da Silva' e que a autenticação está funcionando corretamente.

* **Uma vez concluída estas configurações é possível efetuar a autenticação integrada.**
* Como teste final, autentique no Windows utilizando as credenciais de um usuário válido do Active Directory. Em seguida acesse a plataforma. O acesso à plataforma não exigirá login e senha e já autenticará o usuário no Windows.

### Configuração do Navegador

---

Atenção

**A configuração do navegador deverá ser realizada em cada terminal cliente.**

É necessário configurar o navegador do usuário para que ele utilize autenticação Windows (NTLM) com o script de autenticação remota (remote\_auth.asp).

Mesmo que o serviço de autenticação remota tenha sido configurado para utilizar autenticação Windows no IIS, o navegador do cliente precisa enviar as credenciais para que o script possa fazer as validações necessárias no Active Directory.

##### Internet Explorer e outros navegadores derivados do Chromium (Microsoft Edge e Google Chrome)

No caso dos navegadores **Internet Explorer** e **Google Chrome**, as configurações de segurança e autenticação devem ser realizadas através das **Opções da Internet,** localizada no painel de controle do Windows, pois assim, estes navegadores irão assumir as configurações realizadas. Observe e siga os passos a seguir:

0.5falseie-chrome-configfadetrue1Passo 1

* Para começar, devemos acessar o menu **Opções da Internet**, pelo painel de controle. Para isso, basta segurar a tecla Windows do teclado, pressionar a tecla "R", digitar "control" no campo correspondente e em seguida clicar no botão OK.

true2Passo 2

* Na sequência, alterar a exibição para **Ícones** para facilitar a visualização e clicar na opção **Opções da Internet**.

true1Passo 3

* Em seguida clicar na aba **Segurança**, selecionar **Intranet** **local** e posteriormente, clicar em **Sites.**

true3Passo 4

* Para adicionar o endereço do servidor de autenticação remota precisamos clicar no botão **Avançadas**:

* Informamos a URL do servidor de autenticação remota no campo **Adicionar este site à zona** e então clicamos no botão **Adicionar**. Podemos fechar a tela clicando no botão **Fechar**:

true4Passo 5

* É importante garantir que as configurações de **Autenticação do Usuário** estejam definidas para **Login automático** com o nome de usuário e senha atuais, para a **Intranet Local.** Para consultar esta tela, basta selecionar **Intranet Local** e clicar no botão **Nível personalizado:**

##### Mozilla Firefox

O Firefox deve ser configurado de uma maneira um pouco diferente:

0.5falsefirefox-configfadetrue1Passo 1

* Em primeiro lugar, precisamos digitar [about:config](http://aboutconfig/) na barra de endereços, para poder acessar as configurações do Firefox:

* Uma mensagem de alerta normalmente é exibida. Para continuar, basta clicar no botão de confirmação. No nosso exemplo, o botão **Serei cuidadoso, prometo!**

true2Passo 2

* As configurações de NTLM podem ser facilmente encontradas se digitarmos no campo **Localizar**, a palavra “ntlm”. Devemos manter as configurações como exibidas abaixo. A mais importante é **network.automatic-ntlm-auth.trusted-urls**, onde devemos informar a URL do servidor de autenticação remota:

* **Feito isso, temos também o Firefox configurado para utilização da autenticação integrada com o Windows do fluig.**

### Group Policies

---

Configurar o navegador de alguns poucos usuários é uma tarefa simples, porém, o cliente terá problemas quando possui milhares de usuários a serem configurados.

Para estes casos, podemos utilizar a estratégia de distribuição das configurações, baseadas na utilização de **Group Policies (GPO)**. Durante o procedimento de autenticação no domínio, pode ser executada uma série de tarefas automáticas, como por exemplo, configurar o navegador do usuário.

##### Internet Explorer e Google Chrome

O administrador deverá definir a seguinte configuração de GPO:

Configuração do Computador ► Modelos Administrativos ► Componentes do Windows ► Internet Explorer ► Painel de Controle da Internet ► Página Segurança:

Após habilitar a **Lista de Atribuições de Sites a Zonas**, o cliente deverá definir a URL do servidor de autenticação remota como **membro da Zona da Intranet**.

Desta forma, toda vez que um usuário membro do domínio efetuar o login, as configurações necessárias serão realizadas. Se executada todos os dias, a GPO também deve evitar que um usuário mais avançado desfaça as configurações necessárias para a autenticação remota.

##### Mozilla Firefox

No caso do navegador **Mozilla Firefox**, não existe maneira direta de configurar o navegador a partir da GPO, porém, existem scripts que realizam esta configuração, e estes scripts podem ser executados a partir de uma GPO.

O administrador que desejar realizar as configurações no Firefox, poderá seguir a seguinte configuração:

Para este procedimento será necessário desenvolver uma personalização que aplica as configurações no Firefox (script).

Configuração do Usuário ► Configurações do Windows ► Scripts (Logon/Logoff) ► Logon

# Opções de Arquitetura para Alta Disponibilidade

---

A autenticação remota pode utilizar uma arquitetura baseada em um único servidor. O problema é que neste cenário, se o script estiver off-line, o usuário não conseguirá autenticar na plataforma. O administrador deverá desabilitar a autenticação integrada na plataforma ou corrigir o que for necessário para que o script fique online.

Existe uma opção onde podemos criar dois servidores de autenticação remota, o que fornece uma boa redundância do componente. Se um servidor estiver fora do ar, ou se uma aplicação estiver fora, o outro servidor assume a responsabilidade de manter online o serviço de autenticação remota.

Para isso é necessário disponibilizar um *Load Balancer*que terá a responsabilidade de fazer o redirecionamento, caso um dos dois servidores de autenticação remota esteja off-line.
