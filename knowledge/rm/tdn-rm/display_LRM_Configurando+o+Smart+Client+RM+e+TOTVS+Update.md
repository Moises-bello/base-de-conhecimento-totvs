---
content_hash: 3da4b6bf3cbfdc95ad89cf3a918697bf70bd435f87f6bb16aafe734f5dfe71c0
fetched_at: '2026-06-29T00:06:17.980413+00:00'
page_id: '215482828'
product: rm
source: tdn-rm
title: Configurando o Smart Client RM e TOTVS Update
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+o+Smart+Client+RM+e+TOTVS+Update
version: 135
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é auxiliar na configuração do Smart Client RM e da atualização automática (TOTVS Update) dos servidores e do próprio Smart Client.

# Introdução

---

        O **TOTVS Update** é utilizado para realizar atualizações automáticas no ambiente 3 Camadas, seja Client (Smart Client) ou Server (Host). O TOTVS Update é utilizado para atualizar o ambiente, já o **SmartClient**, é utilizado para instalar o sistema para comunicação via HTTP. Para configurar o SmartClient é necessária a configuração do TOTVS Update, pois os dois compartilham o servidor de Atualização.

         O **Smart Client RM** nada mais é que o mesmo RM.exe utilizado nos ambientes locais e três camadas, e utiliza protocolo TCP ou HTTP para se comunicar com o servidor de aplicação, o Host.

Atenção!

O **TOTVS Update**não foi projetado para atualização dos Portais RM (Ex: Corpor.Net, Portal Educacional, FrameHTML).

O **TOTVS** **Update** não é um instalador RM, trata-se de uma configuração realizada no RM.

ObservaçãoNão é possível utilizar o Smart Client ou TOTVS Update para funcionalidades ainda em Delphi.

**Como funciona****:**

O TOTVS Update atualiza automaticamente o ambiente de acordo com a versão de uma máquina específica, utilizada como "**Servidor de atualização**".   
O Servidor de atualização é uma instalação Server do RM, portanto é necessário atualizar manualmente, através de um instalador, o **"Servidor de Atualização"** com a versão que será replicada para outras estações.  
É necessário reiniciar os serviços Host do RM no Servidor de Atualização, para que os novos arquivos sejam disponibilizados para o SmartClient receber as atualizações.

**Exemplo:**TOTVS Update é utilizado para atualizações automáticas do sistema RM entre Releases (Ex.: 12.1.**12** para 12.1.**13**) e Patchs (Ex.: 12.1.12.**111** para 12.1.12.**112**) em ambientes 3 camadas.

        O "**Servidor de atualização**" pode ser o próprio ou um dos servidores de aplicação, ou seja, onde estará sendo executado o HOST que irá responder pelo Smart Client RM.

false

**Ao realizar a instalação inicial no "Servidor de atualização" utilize a camada "Server".**

# Como configurar

---

Importante

**Para uma melhor estabilidade e gestão de configuração do ambiente, sugerimos que utilizem o configurador global. Mais informações podem ser acessadas clicando [aqui](http://tdn.totvs.com.br/display/LRM/Smart+Client+RM+com+Configurador+global).**

       A partir da versão 12.1.22 pode-se configurar o TOTVS Update durante a instalação da BibliotecaRM:

falseVeja como configurar pelo instalador

Na instalação da **BibliotecaRM 12.1.22** foi implementado a opção de Configuração do **TOTVS UPDATE**.

A opção para configurar o TOTVS Update ficará localizada na tela de Configurações do instalador e  somente será habilitada quando o tipo de instalação for **N camadas**, de acordo com o tipo de camada selecionada, conforme imagem abaixo:

**Tipos de Instalação:**

* **Ambiente N Camadas Client**

Após marcar a opção para configurar o TOTVS Update, será necessário informar o **nome do servidor** e **porta do servidor** de atualização. Assim, a instalação atualizará o arquivo **RM.exe.config** com a propriedade **<add key="UpdateServer" value="host:porta"/>**, onde o host e porta informados na tela serão informados no valor desta TAG.

* **Ambiente N Camadas -> Servidor de Aplicação (AppServer)**

Após marcar a opção para configurar o TOTVS Update, a instalação atualizará o arquivo **RM.Host.exe.config** e **RM.Host.Service.exe.config**com a propriedade **<add key="UpdateServerEnabled" value="true"/>**. e também atualizará o arquivo **RM.exe.config** com a propriedade **<add key="UpdateServer" value="host:porta"/>**, onde o host e porta informados na tela serão informados no valor desta TAG.

No caso de uma instalação que possua múltiplos hosts, apenas o primeiro host terá seus arquivos de configuração alterados.

**Observação:**

A configuração do TOTVS Update não estará disponível para o tipo de camada **Servidor de Processos (JobServer)** ou para **Ambiente Local.**Lembrando que o AppServer e JobServer são atualizados manualmente, via instalador.

         Veja como configurar o TOTVS Update manualmente: Para que o TOTVS Update funcione é necessário alterações no arquivo .Config de acordo com a camada que receberá atualizações.

falsePrincipaltrue1Servidor de Atualização

Para habilitar o serviço de atualização insira a tag **<add key="UpdateServerEnabled" value="true"/>** no arquivo RM.Host.Service.exe.Config, no caminho: C:/TOTVS/CorporeRM/RM.net e reinicie o serviço do HOST.

Ainda no servidor de atualização, é preciso inserir a tag <add key="UpdateServer" value="host:porta"/> no arquivo RM.exe.Config.

Veja o **exemplo** dos arquivos de configuração para este cenário:  e

false

**O servidor de aplicação pode ser utilizado como servidor de atualização**, entretanto neste cenário, onde a maquina de app é a mesma de atualização, **não** se deve realizar a configuração de atualização do server com as tags abaixo no arquivo RM.Host.Service.exe.config:

<add key="UpdateServer" value="host:porta"/> - Informe o nome da máquina e porta que o HOST do Servidor de Atualização utilizará.

<add key="UpdateStartTime" value="HH:mm"/> - Informe o horário que o servidor iniciará a busca por atualizações no Servidor de Atualização.  
<add key="UpdateEndTime" value= "HH:mm"/> - Horário que o servidor finalizará a busca por atualizações no Servidor de Atualização.

Tal apontamento é desnecessário, pois a atualização desta máquina deverá ser realizada manualmente.

2Server

Para que um ambiente Server seja atualizado é necessário inserir no arquivo RM.Host.Service.exe.Config, no caminho C:\totvs\CorporeRM\RM.net, as tags:

**<add key="UpdateServer" value="host:porta"/> - I**nforme o nome da máquina e porta que o HOST do Servidor de Atualização utilizará.

**<add key="UpdateStartTime" value="HH:mm"/> -** Informe o horário que o servidor iniciará a busca por atualizações no Servidor de Atualização.

**<add key="UpdateEndTime" value= "HH:mm"/> -** Horário que o servidor finalizará a busca por atualizações no Servidor de Atualização.

Veja o **exemplo** do arquivo de configuração para este cenário:

false

A partir da versão 12.1.13 o instalador do sistema, oferece a opção de instalação como JobServer ou AppServer. O Servidor de atualização pode ser configurado como JOB ou APP, pois nenhuma dessas opções interferem em sua execução.

Exemplo, em um ambiente N camadas os servidores seriam JobServer, Aplicação e Atualização.

**ATENÇÃO:**

**Não é recomendado** a utilização do Servidor de Atualização como JobServer ou AppServer. Indicamos sua exclusividade para as atualizações.

---

Ao encontrar atualizações disponíveis, o serviço RM.Host.Service.exe será finalizado para que as atualizações sejam realizadas.   
Finalizadas as atualizações o serviço será reiniciado.  
É necessário reiniciar o serviço para que os novos arquivos sejam disponibilizados para o SmartClient receber as atualizações.

**ATENÇÃO:**

Caso exista(m) usuário(s) ou serviço(s) utilizando o ambiente, ele(s) serão desconectado(s)!

Quando o Host estiver rodando com o usuário "NETWORK SERVICE" será necessário utilizar um usuário de rede ou da máquina com privilégios necessários para gerenciar os serviços, pois o RM.Update não tem permissão suficiente para subir novamente o serviço do Host.

Exemplo:

:

---

**O servidor de aplicação pode ser utilizado como servidor de atualização**, entretanto neste cenário, onde a maquina de app é a mesma de atualização, **não** se deve realizar a configuração de atualização do server com as tags <add key="UpdateServer" value="host:porta"/> - Informe o nome da máquina e porta que o HOST do Servidor de Atualização utilizará.

---

 Quando o ambiente utilizar balanceamento nativo, com múltiplos hosts (host1, host2), as tags do Totvs Update devem ser configuradas apenas no config de um dos hosts. Exemplo: ,  ou  . Não se deve realizar a configuração em todos os configs, pois não existe balanceamento para o Totvs Update.

Caso o Sistema RM já esteja instalado no Servidor de Atualização, utilize o passo a passo contido no link abaixo:

**[Configuração para simular 3 camadas - JobServer](http://tdn.totvs.com/pages/viewpage.action?pageId=181143177)**

3Client

Para que um ambiente Client seja atualizado é necessário inserir no arquivo RM.exe.Config, no caminho: C:\totvs\CorporeRM\[RM.net](http://RM.net), a tag:

**<add key="UpdateServer" value="host:porta"/> -** Informe o nome da máquina e porta que o HOST do Servidor de Atualização está utilizando.

Veja o **exemplo** do arquivo de configuração para este cenário:

Enquanto o Sistema RM estiver atualizando, o serviço RM.Host.Service.exe será finalizado. Assim todos os usuários serão desconectados do sistema.

Ao iniciar o aplicativo RM.exe será exibida a tela de verificação de atualização do sistema.

Caso haja alguma alteração de versão, release ou patch do Sistema RM no Servidor de Atualização, o sistema irá iniciar o processo de atualização e depois abrirá normalmente.

Download do SmartClientDownload do SmartClientDownload do SmartClient

**Para download do RM.exe (smart client), basta acessar o link conforme exemplo abaixo:**

**h[ttp://Servidor\_na\_nuvem:8051/wsUpdate](http://servidor_na_nuvem:8051/wsUpdate)**

Composição do link: Http://<endereço do host>:porta(8051 por default)/wsUpdate;

A tag UpdateServerEnabled deve estar configurada = true, caso contrário o acesso a este link será desabilitado pelo Host.

Ambientes que utilizam SSL

Em ambientes que utilizam SSL o link muda para:

**[https://Servidor\_na\_nuvem:8051/wsUpdate/Index](https://servidor_na_nuvem:8051/wsUpdate/Index)**

****Caso não consiga acessar o link, verifique se a porta está liberada. Para isso, execute o seguinte comando no cmd do Server:****

**netsh http add urlacl url=http://+:8051/ user=NetworkService**

Será apresentada a tela a seguir, clique em "**Aqui**":

**Tela de Download do Client SmartClient:**

A partir da versão 12.1.2209 será apresentada a tela abaixo, nesse caso, clique em **"Download"**:

Após fazer o download do arquivo e execute-o. Será iniciada a instalação do Sistema RM.

**Instalador do SmartClient:**

Observação

* Caso já exista instalação do Sistema RM no computador Client ou TS, faça a desinstalação do mesmo.
* É necessária a configuração do Servidor de Atualização (TOTVS Update) para utilizar o TOTVS SmartClient.
* O executável baixado **não deve** ser renomeado, para o correto funcionamento do Smart Client.

Caso a tela abaixo seja apresentada, siga os passos a seguir:

1. Acesse os serviços do Windows(Painel de Controle/ Ferramentas Administrativas/ Serviços), clique com o botão direito sobre **RM.Host.Service**, depois em Propriedades.

2. Na aba **Logon** marque a caixa **Conta do Sistema Local** e depois clique em **OK**.

4Log

A tag **<add key="UpdateLogEnabled" value="true" />** pode ser habilitada nas estações que serão atualizadas. Desta forma ao executar o TOTVS Update será gerado o arquivo de log "\_updatelog.txt", na pasta do RM contendo informações da atualização.

5Cache de Download

Para otimizar o processo de instalação/atualização através do TOTVS Update é possível definir uma pasta compartilhada na rede que será utilizada como cache dos arquivos baixados do servidor de atualização.

 Para habilitar o cache, é necessário adicionar uma nova chave no arquivo de configuração do Host (RM.Host.Service.exe.config).

**<add key="UpdateCachePath" value="\\SERVIDOR\PASTA"/>**

Quando esta opção é ativada, o cliente irá primeiro verificar se o arquivo a ser atualização já foi baixado por outro cliente e em seguida fará a cópia do mesmo a partir desta pasta da rede.

Para o correto funcionamento, todos os clientes deverão ter acesso de escrita e leitura nesta pasta compartilhada.

Caso o arquivo não tenha sido baixado, o primeiro cliente que fizer o download do servidor irá fazer a atualização do arquivo na pasta de cache para que outros clientes que forem fazer a atualização busquem o arquivo nesta pasta.

Observações

* Caso o cliente não tenha acesso a esta pasta, o arquivo será baixado do servidor normalmente.
* A atualização do client, só será executada caso o serviço de host do servidor de atualização esteja ativo, independente de existir ou não arquivos de atulaização no diretório compartilhado.
* A tag para utilização do cache de download deve ser adicionada apenas no arquivo de configuração do host do servidor de atualização. Não é necessário adicionar a tag nos clientes.

Veja o **exemplo** do arquivo de configuração para este cenário:

Observação

Para a execução de TLS 1.1 e 1.2 no Windows 7 é necessário adicionar os registros abaixo, visto que são os protocolos de comunicação ativos atualmente e que por padrão não são ativos na versão Windows7:

Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]  
"DisabledByDefault"=dword:00000000

**Arquivo disponível para download:**

falseObservação

**O TOTVS Update atualizará os ambientes de acordo com a versão instalada/utilizada no Servidor de atualização.**É necessário reiniciar os serviços Host do RM no Servidor de Atualização, para que os novos arquivos sejam disponibilizados para o SmartClient receber as atualizações.

Download do SmartClient

O processo de atualização do Smart Client é seguro e não causará dano algum a(s) máquina(s) envolvida(s) nesse processo. Caso algum antivírus instalado na(s) máquina(s) envolvida(s) aponte o RM.exe (Smart Client) como ameaça, inclui-a o executável na lista de exceções do antivírus, caso o download tenha sido bloqueado pelo anti-vírus, ou simplesmente prossiga com a execução, caso o antivírus não tiver bloqueado o download do instalador.

Para minimizar a taxa do antivírus apresentar o arquivo como risco, a partir da release 12.1.28 e dos patches 12.1.27.169 e 12.1.26.214 , mantemos a assinatura digital do instalador e o arquivo baixado do Smart Client terá no seu nome o **domínio + porta** de download, se informados na URL do wsUpdate. 

Exemplo do nome do arquivo:

* Executável baixado: "RM.Install localhost..8051.exe"

**Importante:** O executável baixado **não deve** ser renomeado, para o correto funcionamento do Smart Client.

# Configuração para Acesso Externo

---

Existem duas formas de realizar a configuração do Smart Client para acesso externo:

* **1º Configuração:**

        Publicar o servidor de App e de Atualização, Em seguida no arquivo de configuração, informe o endereço externo na tag "**updateserver**" e no "**host**", conforme exemplo no print abaixo:

* **2º Configuração:**

Realizar a configuração de Gerenciador de config global no ambiente conforme documentação [Gerenciador de Config](https://tdn.totvs.com/display/public/LRM/Gerenciador+de+Config)        

        Segue abaixo, print com exemplo do conteúdo do arquivo após a configuração do config global:

Para saber mais sobre como configurar o Totvs Update para acesso local e remoto, clique [aqui](https://tdn.totvs.com/x/kxHRDg).

# Problemas de comunicação com o servidor de atualização

A partir da versão 12.1.2306 foi adicionada uma funcionalidade para auxiliar na atualização e utilização do sistema quando ocorrer algum tipo de problema ou erro na comunicação com o servidor de atualização.

Caso o servidor esteja fora do ar no momento da inicialização do RM, será apresentada uma tela para que o usuário decida o que fazer, "Tentar Novamente" e repetir o processo de atualização ou descartar a atualização e abrir o RM na versão anterior.

"Sim" para Tentar Novamente ou "Não" para abrir o RM na versão anterior.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.18 ou superiores

false

**Processo:** Smart Client RM e Totvs Update

falsefalse

**Status:** Finalizado

false

**Data:** 22/09/2017

false

**Autores:**
