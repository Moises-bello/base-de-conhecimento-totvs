---
content_hash: e611081dd86927e270e7c4414e17cb5170f6e6fb382804db5620597c8166d05a
fetched_at: '2026-06-28T21:35:22.344686+00:00'
page_id: '235592303'
product: fluig
source: tdn-fluig
title: Identity | Configuração do Desktop Launcher
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235592303
version: 34
---

# Falando de Desktop Launcher...

---

Aplicativos que estão instalados localmente em um computador e que exigem credenciais de login podem ser acessados pelo Identity utilizando uma ferramenta chamada Desktop Launcher.

Quando o Desktop Launcher estiver instalado e configurado, ele acessa as suas credenciais em todos os aplicativos *desktop* adicionados ao Launchpad. Quando um aplicativo *desktop* for aberto, o Desktop Launcher irá recuperar as suas informações de login do Identity e irá inseri-las no aplicativo em seu computador.

Esta documentação demonstra como fazer o *download*, instalar e configurar o Desktop Launcher, e como abrir os aplicativos *desktop* pelo Launchpad.

# Pré-requisitos

* Consultar os requisitos mínimos na [Matriz de Portabilidade - TOTVS Identity](https://tdn.totvs.com/x/eDAxE).

* Embora não seja obrigatório para instalar o Desktop Launcher, é recomendado possuir um aplicativo *desktop* previamente cadastrado no Identity, conforme demonstrado na documentação [Como configurar aplicativos Desktop no Identity,](https://tdn.totvs.com/x/IL4KDg) para testar a configuração da aplicação.

# Obter o Desktop Launcher

O *download* do Desktop Launcher pode ser feito por qualquer usuário do Identity. Para administradores, o *download* está disponível na página [Gerenciar conta](https://tdn.totvs.com/x/79q7E#Gerenciarconta-ObteroDesktopLauncher) e para usuários comuns, [Meu Perfil](https://tdn.totvs.com/x/gNq7E#Meuperfil-ObteroDesktopLauncher).

# Instalar o Desktop Launcher

Após o *download* do pacote de instalação do Desktop Launcher, conforme o procedimento acima, o processo de instalação pode ser iniciado.

* Acionar o pacote de instalação do Desktop Launcher com o botão direito do *mouse* e selecionar **Executar como administrador**. Será apresentado o *wizard* de instalação.

* Acionar ***Next***.

* Conferir os dados de instalação e acionar ***Install***. O procedimento de instalação será iniciado e pode durar vários minutos.

* Acionar ***Finish***. Um atalho para execução do Desktop Launcher será criado na Área de trabalho do Windows.

**Instalação do Desktop Launcher**

# Configurar o Desktop Launcher

Para realizar as configurações no Desktop Launcher, o usuário deve executar o aplicativo através do atalho criado na área de trabalho do Windows e seguir os procedimentos abaixo.

falseconfigPasso 1

* Acionar ***Advanced Settings*** no canto inferior direito do aplicativo.

Passo 2

* Informar o domínio da empresa no Identity nos campos **SSOProfileStoreRestUrl** e **UserStoreRestUrl**. Por exemplo, [https://suaempresa.fluigidentity.com.](https://minhaempresa.fluigidentity.com.)

* Caso o computador esteja instalado em uma rede que utiliza proxy, informe as configurações de proxy na seção **Http Proxy**. Caso contrário, mantenha a opção *No Proxy*.

* Acionar ***Update*** para salvar as configurações.

Passo 3

* Informar as credenciais de acesso ao Identity nos campos ***Account Name*** (e-mail) e ***Password*** (senha pessoal).

* Essas informações são atreladas ao nome do usuário do Windows e armazenadas para que quando o computador for iniciado o Desktop Launcher seja executado e faça o login automaticamente.

* Acionar ***Log In***.

Passo 4

* Se as configurações estiveram corretas e as credenciais informadas válidas, serão exibidos todos os aplicativos que foram adicionados ao Launchpad do usuário no Identity.

* Caso seja necessário fazer login com outro usuário, acionar ***Logout*** no canto inferior direito da tela principal do Desktop Launcher. As informações anteriormente atreladas à conta do Windows serão substituídas pelo novo login.

Update SSOProfile

Sempre que for realizada alguma alteração em um [aplicativo *desktop* no Identity](http://tdn.totvs.com/x/IL4KDg), é recomendado acionar o botão ***Update* SSOProfile**, para que as atualizações sejam verificadas pelo Desktop Launcher.

# Informar as credenciais do aplicativo no Launchpad

Além da configuração do Desktop Launcher na estação de trabalho, o aplicativo *desktop* no Identity precisa ser configurado com as credenciais de acesso do usuário ao aplicativo em questão e o caminho do executável no computador.

No exemplo abaixo, o executável do Skype está localizado no diretório "C:\Program Files (x86)\Skype\Phone\Skype.exe".

falselaunchpadUsuário ComumAdministrador

# Configurar inicialização automática do Desktop Launcher

É possível configurar o Desktop Launcher para ser executado automaticamente junto à inicialização do sistema operacional Windows, simplificando a autenticação do usuário. Os passos a seguir demonstram os procedimentos necessários para a inicialização automática.

* Abrir o programa **Executar** do Windows (atalho de teclado: Windows + R).

* Informar o comando abaixo para abrir o diretório de inicialização automática no Windows Explorer:

* Copiar o atalho do Desktop Launcher criado na Área de Trabalho para o diretório de inicialização automática.

]]>
