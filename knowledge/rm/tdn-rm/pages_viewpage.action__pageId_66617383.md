---
content_hash: d53753c7f3443e8ff906e6ee336f4b4cdec292d395ed1754aa20aa12c36f0b6c
fetched_at: '2026-06-29T00:11:16.254306+00:00'
page_id: '66617383'
product: rm
source: tdn-rm
title: Configuração WebService TOTVS Avaliação e Pesquisa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66617383
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM TOTVS Avaliação e Pesquisa 11.80 |
| **Processo** | : | Executor de Avaliações e Pesquisas |
| **Subprocesso** | : | RM Executor modo Webservice |
| **Data da publicação** | : | 09/07/2013 |

O modo WebService é uma das formas de executar uma prova, e é configurado através do aplicativo RM Executor, que permite ao usuário executar uma prova disponibilizada através de um serviço web, podendo estar localizado no host local ou remoto. Este documento tem como objetivo descrever a configuração do ambiente WebService nos sistemas operacionais Windows XP e 7.

#### Configuração Windows XP

**1º Instalar o TOTVS Avaliação e Pesquisa**

Instale a versão mais atual do TOTVS Avaliação e Pesquisa, para que você tenha acesso à pasta do WebService, conforme mostra a figura abaixo:

**2º Configurar WebService**

Acesse o servidor Web, o IIS (Internet Information Services) no Painel de controle do Windows conforme a figura abaixo:

Crie um novo diretório virtual.  Para o **IIS 6**, utilizando o **Windows XP**:

* Abra **Computador local.**
* Abra a pasta **Sites da Web**.
* Selecione o **Site da Web Padrão**, clicar com o botão direito do mouse, escolher a opção **Novo | Diretório Virtual** e clicar no botão **Avançar**.

* Digite na caixa de texto **Alias** o seguinte: **WebService** e clique em **Avançar**.

* Na tela a seguir selecione o diretório correspondente à pasta WebService, disponibilizada com a  instalação do TOTVS Avaliação e Pesquisa.

* Na etapa de **Permissão de Acesso**, marcar as opções de **Leitura**, **Execução de Scripts** e **Execução de Aplicativos** e depois clicar em **Avançar**.

* Clique em **Concluir** e feche o IIS.

Veja como fica o ambiente após as configurações:

**3º Acesso ao WebService**

Para verificar se o servidor foi configurado corretamente, abra o browser (por exemplo, Internet Explorer) e digite o endereço onde se encontra o arquivo TstExecWebService.asmx.

**Exemplo:** <http://localhost/Webservice/TstExecWebService.asmx>, onde localhost é o nome do servidor e Webservice é o nome da pasta do Webservice.

#### Configuração Windows 7, Vista, Server 2008

**1º Instalar o TOTVS Avaliação e Pesquisa**

Instale a versão mais atual do TOTVS Avaliação e Pesquisa, para que você tenha acesso à pasta do WebService, conforme mostra a figura abaixo:

**2º Configurar WebService**

Acesse o servidor Web, o IIS (Internet Information Services) no Painel de controle do Windows conforme a figura abaixo:

Crie um novo diretório virtual. Para isso:

a - Abra Computador local.

b - Abra pasta Sites da Web.

c - Selecione o Site da Web Padrão (ou Default Web Site), clicar com o botão direito do mouse, escolher a opção Adicionar aplicativo (ou add application).

d - Digite na caixa de texto "Alias" o nome do serviço (Exemplo: Webservice) e selecione o caminho físico C:\totvs\CorporeRM\RMTestis\Webservice.

e- Em “Pool de aplicativos” (ou Application pools), selecione a versão 4.0 do framework. Clique em seguida no botão “ok”.

f - Abra a opção “Pesquisa no diretório” (ou Directory browsing) e clique na opção “Habilitar” (ou Enable).

g - Feche o IIS.

Para verificar se o servidor foi configurado corretamente, abra o browser (por exemplo, Internet Explorer) e digite o endereço onde se encontra o arquivo TstExecWebService.asmx.

**Exemplo**

<http://localhost/Webservice/TstExecWebService.asmx>, onde localhost é o nome do servidor e Webservice é o nome da pasta do Webservice.

**Observação:** A configuração descrita acima é referente a versão do IIS 7, pode ser utilizada também para configurar nos sistemas operacionais Windows 7 e Vista.

**3º Configurações do arquivo Web.config**

| * A configuração do arquivo Web.config é primordial para o funcionamento do sistema em modo WebService, devendo ser executada da mesma forma em todos os sistemas operacionais suportados e citados neste documento. |
| --- |

Depois de realizadas as configurações anteriores, é preciso configurar o arquivo Web.config, localizado na pasta C:\totvs\CorporeRM\RMTestis\ Webservice.

Edite o arquivo Web.config retirando todas as tags  que estão em “appSettings” exceto a tag <add key="Alias" value="CorporeRM" /> e substitua pelas que estão em “appSettings”  dos arquivos RM.Host.exe.config / RM.Host.Service.exe.config localizados na pasta C:\totvs\CorporeRM\RM.Net.

...

<appSettings>

<!--Configurações de Remoting-->

<add key="RemoteLoad" value="false" />

<add key="SelfHosted" value="false" />

<add key="ServerHost" value="localhost" />

<add key="ServerUrl" value="http://localhost/RM.net/" />

**<add key="Alias" value="CorporeRM" />**

 <add key="CommunicationStyle" value="wcf" />

 <add key="WcfProtocol" value="tcp" />

  <add key="TcpPort" value="8060" />

</appSettings>

…

**Importante**

Na tag <add key="Alias" value="CorporeRM" /> o valor de “value” deverá ser substituído pelo valor da tag “Alias” do arquivo Alias.dat localizado em C:\totvs\CorporeRM\RM.Net.

No exemplo abaixo do arquivo Alias.dat “CorporeRm Exemplo” é o valor a ser utilizado na tag “Alias” do arquivo Web.config.

<DbConfig>  
    <Alias>**Corporerm Exemplo**</Alias>

**...**

</DbConfig>

Depois das alterações realizadas o conteúdo do Web.config ficará da seguinte forma:

…

<appSettings>

<!--Configurações de Remoting-->

<add key="JobServer3Camadas" value="false" />

<add key="Port" value="8050" />

<add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />

<add key="EnableCompression" value="true" />

 <add key="Alias" value="CorporeRmExemplo" />

</appSettings>

...

**Observação importante:**

O arquivo Web.config do WebService e RM.Host.exe.config / RM.Host.Service.exe.config devem possuir as mesmas tags de configuração. Caso as tags sejam diferentes, atualize o arquivo web.config do WebService para que ele fique com as mesmas tags do RM.Host.config/ RM.Host.Service.exe.config.

**4º Execução da prova no RM Executor modo Webservice**

Caso ainda não esteja instalado, instalar a última versão do RM Executor.

Execute o RM Executor e informe a inscrição do candidato gerado pelo TOTVS Avaliação e pesquisa.

Selecione o tipo de acesso: WebService (online).

Neste momento será aberta uma janela para que seja informado o endereço do WebService definido na etapa de configuração do IIS: <http://localhost/Webservice/TstExecWebService.asmx>, e clique em OK para fechar a janela.

Clique em OK novamente para iniciar e siga os passos normais para executar a prova.
