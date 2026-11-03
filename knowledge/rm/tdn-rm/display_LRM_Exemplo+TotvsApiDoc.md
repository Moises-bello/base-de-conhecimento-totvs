---
content_hash: 39091eea13096b4b6fd6910e8fc767688a9ac7e398a2a339e91dbca3d9ed2169
fetched_at: '2026-06-29T00:10:23.226403+00:00'
page_id: '500281497'
product: rm
source: tdn-rm
title: Exemplo TotvsApiDoc
type: documentation
url: https://tdn.totvs.com/display/LRM/Exemplo+TotvsApiDoc
version: 2
---

]]>]]>

# Pré-Requisitos

---

Lista de Pré-Requisitos do TAI

### Portal RM (MSI e EXE)

#bbb#f1f1f1ChromeDriver - WebDriver for Chrome

O Webdriver é utilizado para a checagem funcional do Portal. A versão do Webdriver  tem que ser a mesma do Google Chrome Instalado.

Mais informações em: [http://chromedriver.chromium.org/downloads](https://www.google.com/url?q=http://chromedriver.chromium.org/downloads&sa=D&source=hangouts&ust=1558453082539000&usg=AFQjCNHRgSBISia2oPYfXGgoK9I4fAAOcA)

]]>]]>

# Checklist Manual x CheckList Automatizado

---

Checklist manual realizado pela homologação:

<http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testPlayer/GTFBH-C72>

#bbb#f1f1f1GTFBH-T1357 (1.0) 1. Testes após instalação da BibliotecaRM.MSI

]]>

Arquivos TOTVSReportsCompare.exe e TOTVSReportsCompare.exe.config

]]>]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyRMMSIEXEInstallationFolderAndFiles()

]]>

]]>

Execução de Jobs Locais

Execução de Jobs Server

]]>

Método: RMMSIEXEFunctionalCheck

Classe: ExecuteFunctionalOperations()

Método: ExecuteJobs

Classe: VerifyJobExecutionFromApiJobScheduler()

]]>

]]>

Executar o sistema

Teste de conexão Biblioteca entre Server X Cliente

]]>

Método: RMExecute

Classe: ExecuteRMExe

]]>

]]>

Instalação em diretório diferente do default

Instalação modo Client

Instalação modo Local

Instalação modo Server

]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>

]]>

Instalação Client - Verificar arquivos do server (Host entre outros)

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyEnvironmentRequiredFiles()

]]>

]]>

Instalação modo Local: tag JobServerEnabled="false"

Instalação modo Local: tag JobServerLocalOnly="false"

Instalação modo Server: tag JobServerEnabled="true"

Instalação modo Server: tag JobServerLocalOnly="false"

Tag JobServer3Camadas modo Client = "True"

Tag Jobserver3Camadas modo Local = "False"

Tag JobServer3Camadas modo Server = "True"

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyIfConfigValuesAreCorrect()

]]>

]]>

RM.Lib.Version.dll (Verificar Versão)

RMGerador.dll (Verificar Versão)

RMVersion.dll (Verificar Versão)

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyFilesVersion()

]]>

]]>

Tag do host no arquivo RM.Lib.Gerador.Execute.exe.config

Tag EnableCompression

Tag Host

Tag LocalizationLanguage

Tag Port

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyIfConfigTagsExists()

]]>#bbb#f1f1f1GTFBH-T1358 (1.0) 2. Testes após instalação do RMPortal.MSI

]]>

Abrir os módulos do portal

Execução do portal

Teste de conexão Portal entre Server X Cliente

]]>]]>

Classe: RMPortalExecute

Método: RMPortalExecute()

]]>

]]>

Instalação com biblioteca RM Client

Instalação com biblioteca RM Local

Instalação com biblioteca RM Server

Instalação em diretório diferente do default

Instalação sem biblioteca RM

]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>

]]>

RM.Lib.Version.dll

RMVersion.dll

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyFilesVersion()

]]>

]]>

Tag EnableCompression

Tag Host

Tag Port

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyIfConfigTagsExists()

]]>

]]>

Tag JobServer3Camadas modo Client = "True"

Tag Jobserver3Camadas modo Local = "False"

Tag PathSavePersonalizationPortal = Local da instalação

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyIfConfigValuesAreCorrect()

]]>#bbb#f1f1f1GTFBH-T1359 (1.0) 3. Testes após instalação da BibliotecaRM.EXE

]]>

Arquivos TOTVSReportsCompare.exe e TOTVSReportsCompare.exe.config

]]>]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyRMMSIEXEInstallationFolderAndFiles()

]]>

]]>

Execução de Jobs Locais

Execução de Jobs Server

]]>

Classe: RMMSIEXEFunctionalCheck

Método: ExecuteFunctionalOperations()

Classe: ExecuteJobs

Método: VerifyJobExecutionFromApiJobScheduler()

]]>

]]>

Executar o sistema

Teste de conexão Biblioteca entre Server X Cliente

]]>

Classe: RMExecute

Método: ExecuteRMExe

]]>

]]>

Instalação em diretório diferente do default

Instalação modo Client

Instalação modo Local

Instalação modo Server

]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>

]]>

Instalação Client - Verificar arquivos do server (Host entre outros)

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyEnvironmentRequiredFiles()

]]>

]]>

Instalação modo Local: tag JobServerEnabled="false"

Instalação modo Local: tag JobServerLocalOnly="false"

Instalação modo Server: tag JobServerEnabled="true"

Instalação modo Server: tag JobServerLocalOnly="false"

Tag JobServer3Camadas modo Client = "True"

Tag Jobserver3Camadas modo Local = "False"

Tag JobServer3Camadas modo Server = "True"

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyIfConfigValuesAreCorrect()

]]>

]]>

RM.Lib.Version.dll (Verificar Versão)

RMGerador.dll (Verificar Versão)

RMVersion.dll (Verificar Versão)

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyFilesVersion()

]]>

]]>

Tag do host no arquivo RM.Lib.Gerador.Execute.exe.config

Tag EnableCompression

Tag Host

Tag LocalizationLanguage

Tag Port

]]>

Classe: RMMSIEXEInstallationCheck

Método: ExecuteRMMSIEXEInstallationCheck()

Classe: RMMSIEXEInstallationFolderAndFiles

Método: VerifyIfConfigTagsExists()

]]>#bbb#f1f1f1GTFBH-T1360 (1.0) 4. Testes após instalação da RMPortal.EXE

]]>

Abrir os módulos do portal

Execução do portal

Teste de conexão Portal entre Server X Cliente

]]>]]>

Classe: RMPortalExecute

Método: RMPortalExecute()

]]>

]]>

Instalação com biblioteca RM Client

Instalação com biblioteca RM Local

Instalação com biblioteca RM Server

Instalação em diretório diferente do default

Instalação sem biblioteca RM

]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>

]]>

RM.Lib.Version.dll

RMVersion.dll

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyFilesVersion()

]]>

]]>

Tag EnableCompression

Tag Host

Tag Port

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyIfConfigTagsExists()

]]>

]]>

Tag JobServer3Camadas modo Client = "True"

Tag Jobserver3Camadas modo Local = "False"

Tag PathSavePersonalizationPortal = Local da instalação

]]>

Classe: RMPortalInstallationCheck

Método: ExecuteRMPortalInstallationCheck()

Classe: RMPortalInstallationFolderAndFiles

Método: VerifyIfConfigValuesAreCorrect()

]]>#bbb#f1f1f1GTFBH-T1361 (1.0) 5. Testes após instalação do Totvs Business Connect - TBC

]]>

Instalação da versão especifica

Instalação em diretório diferente do default

]]>]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>

]]>

Conferir instalação no IIS

]]>

Classe: TBCInstallationCheck

Método: ExecuteTBCInstallationCheck()

Classe: TBCInstallationOnIIS

Método: VerifyTBCInstallationOnIIS()

]]>

]]>

Conferir remoção completa após desinstalação

]]>

Classe: TBCInstallationCheck

Método: ExecuteTBCUninstallationCheck()

Classe: TBCUninstallationFolderAndFiles

Método: VerifyTBCUninstallationFolderAndFiles()

]]>

]]>

Conferir remoção completa após desinstalação no IIS

]]>

Classe: TBCInstallationCheck

Método: ExecuteTBCUninstallationCheck()

Classe: TBCUninstallationOfIIS

Método: VerifyTBCUninstallationOfIIS()

]]>#bbb#f1f1f1GTFBH-T1346 (1.0) 0. Utilizar o instalador EXE e MSI.

]]>

Instalação da Biblioteca RM (MSI versão anterior + EXE versão atual)

]]>]]>

Método: InstallMsi()

Método: InstallExe()

Método: UninstallRM()

Método: UninstallMSI()

]]>#bbb#f1f1f1GTFBH-T1347 (1.0) 6. Verificar se a instalação do sistema foi realizada no caminho corretamente

]]>

Avaliar se o processo de instalação foi efetivado na pasta padrão

]]>]]>

Classe: RMEnvironment

Método: CheckEnvironmentFolders();

]]>#bbb#f1f1f1GTFBH-T1348 (1.0) 7. Verificar se a estrutura de pastas em C:\Totvs\CorporeRM

]]>

Avaliar se a estrutura de pastas está correta

]]>]]>

Classe: RMEnvironment

Método: CheckEnvironmentFolders();

]]>#bbb#f1f1f1GTFBH-T1350 (1.0) 8. Acessar a aplicação após a instalação (todos os módulos)

]]>

Acessar os produtos através do RM.EXE

]]>]]>

Classe: RMExecute

Método: ExecuteRMExe()

]]>#bbb#f1f1f1GTFBH-T1356 (1.0) 9. Avaliação e verificação dos objetos Gerenciais

]]>

Avaliar na pastas de relatórios se todos foram gerados corretamente

]]>]]>

Classe: RMEnvironment

Método: CheckEnvironmentFolders();

]]>#bbb#f1f1f1GTFBH-T1355 (1.0) Acessar o Portal três camadas

]]>

Realizar o teste em três camadas no Portal

]]>]]>

Classe: RMPortalExecute

Método: RMPortalExecute();

]]>]]>]]>

# Funcionalidades

---

   Lista de Funcionalidades do TAI:

### Biblioteca RM (MSI e EXE)

#bbb#f1f1f1Desinstalação da BibliotecaRM via arquivo MSI

Desinstala a BibliotecaRM a partir de um arquivo msi.

#bbb#f1f1f1Instalação da BibliotecaRM via arquivo MSI

Instala a BibliotecaRM a partir de um arquivo msi, permitindo escolher o tipo da instalação entre Server / Client / Local

#bbb#f1f1f1Instalação da BibliotecaRM via arquivo EXE

Instala a BibliotecaRM a partir de um arquivo exe, desde que haja uma versão anterior instalada.

#bbb#f1f1f1Verificação do ambiente da BiblilotecaRM

Realiza as seguintes verificações no ambiente da Biblioteca:

* se os arquivos do TotvsReportsCompare estão presentes
* se o atributo LayerSideKind dos arquivos estão de acordo com o tipo da instalação escolhida
* se as pastas requeridas estão presentes e com arquivo contido nelas
* se as tags de config estão presentes de acordo com o tipo da instalação escolhida
* se as tags de config estão corretas de acordo com o tipo da instalação escolhida
* se a versão de arquivos chave do sistema estão corretas
* se existir arquivos de log´s de instalação da BibliotecaRM das camadas "Client" e "Server" será executado uma comparação dos arquivos que possuírem nomeclatura iniciando com "RM". Esta comparação verifica tamanho, versão e data do arquivo.
#bbb#f1f1f1Verificação de funcionalidades da BibliotecaRM

Realiza as seguintes verificações de funcionalidades da Biblioteca:

* efetua login no RM
* acessa cada um dos módulos do sistema
* acessa actions do módulo e efetua o readView, até que retorne sucesso
* executa um Job via WebAPI

### Portal RM (MSI e EXE)

#bbb#f1f1f1Desinstalação do PortalRM via arquivo MSI

Desinstala o PortalRM a partir de um arquivo msi.

#bbb#f1f1f1Instalação do PortalRM via arquivo MSI

Instala o PortalRM a partir de um arquivo msi

#bbb#f1f1f1Instalação do PortalRM via arquivo EXE

Instala o PortalRM a partir de um arquivo exe, desde que haja uma versão anterior instalada.

#bbb#f1f1f1Verificação do ambiente do PotalRM

Realiza as seguintes verificações no ambiente do Portal:

* se as tags de config estão presentes de acordo com o tipo da instalação escolhida
* se as tags de config estão corretas de acordo com o tipo da instalação escolhida
* se a versão de arquivos chave do sistema estão corretas
#bbb#f1f1f1Verificação de funcionalidades do PortalRM

Realiza as seguintes verificações de funcionalidades do Portal, pode ser testado o ambiente do Teste Sistêmico:

* efetua login no RM
* acessa cada um dos módulos do sistema

### TBC (MSI e EXE)

#bbb#f1f1f1Desinstalação do TBC via arquivo MSI

Desinstala o TBC a partir de um arquivo msi.

#bbb#f1f1f1Instalação do TBC via arquivo MSI

Instala o TBC a partir de um arquivo msi

#bbb#f1f1f1Verificação do ambiente do TBC

Realiza as seguintes verificações no ambiente do TBC na instalação:

* se as configurações no IIS estão corretas
* se os diretórios e arquivos estão corretos

Realiza as seguintes verificações no ambiente do TBC na desinstalação:

* se as configurações no IIS foram removidas
* se os diretórios e arquivos foram removidos
#bbb#f1f1f1Verificação de funcionalidades do TBC

Verifica se a página principal do TBC está respondendo.

Atenção

O caminho padrão definido para a geração dos logs é: %USERPROFILE%\AppData\Local\Temp\TOTVS\TAI.

OBS: Esse caminho poderá ser alterado conforme a necessidade do usuário. Basta modificar a TAG LOGPATH disponível no arquivo de configuração do TAI.

]]>]]>

# Parâmetros

---

   Lista de argumentos aceitos pelo TAI:

#bbb#f1f1f1-t --type=VALUE

Informa o tipo de instalador: Biblioteca | Portal | TBC

#bbb#f1f1f1-m --installMsi

Informa se é instalação via arquivo msi

#bbb#f1f1f1-e --installExe

Informa se é instalação via arquivo exe

#bbb#f1f1f1-u --uninstall

Informa se é desinstalação

#bbb#f1f1f1-s --checkSetup

Informa se vai checar o ambiente

#bbb#f1f1f1-f --checkFunctional

Informa se vai checar as funcionalidades

#bbb#f1f1f1-c --compare

Informa se vai realizar a comparação entre ambientes Client e Server (disponível apenas para a Biblioteca RM)

#bbb#f1f1f1--setupFile=VALUE

Caminho completo do arquivo de setup

#bbb#f1f1f1--installPath=VALUE

Caminho completo da instalação

#bbb#f1f1f1--portalApplication=VALUE

Alias do aplicativo no IIS

#bbb#f1f1f1--threeTier

Teste no ambiente 3 camadas do Teste Sistêmico

#bbb#f1f1f1--machineName=VALUE

Nome da maquina

#bbb#f1f1f1--dbServer=VALUE

Nome da maquina do banco de dados

#bbb#f1f1f1--dbName=VALUE

Nome do banco de dados

#bbb#f1f1f1--layerSide=VALUE

Camada de instalação: Local | Server | Client

#bbb#f1f1f1--alias=VALUE

Alias do RM

#bbb#f1f1f1--user=VALUE

Usuário do RM

#bbb#f1f1f1--password=VALUE

Senha do RM

#bbb#f1f1f1--version=VALUE

Versão do sistema xx.x.xx.xxx

#bbb#f1f1f1--hostServer=VALUE

Endereço do host

#bbb#f1f1f1--hostPort=VALUE

Porta do host

#bbb#f1f1f1-? -h --help

Exibe mensagem com os possíveis parâmetros.

]]>]]>

# Exemplos de utilização (Comandos)

---

   Exemplos de comandos para algumas funcionalidades do TAI:

### Biblioteca RM (MSI e EXE)

#bbb#f1f1f1Desinstala biblioteca

TOTVSAutomationInstaller.exe -t=Biblioteca -u --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.msi"

#bbb#f1f1f1Instala biblioteca msi SERVER

TOTVSAutomationInstaller.exe -t=Biblioteca -m --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.msi" --layerSide=Server --dbServer=bhn050103000 --dbName=Exemplo12124

#bbb#f1f1f1Instala biblioteca msi CLIENT

TOTVSAutomationInstaller.exe -t=Biblioteca -m --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.msi"--layerSide=Client --hostServer=bhd005002000 --hostPort=8050

#bbb#f1f1f1Instala biblioteca msi LOCAL

TOTVSAutomationInstaller.exe -t=Biblioteca -m --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.msi" --layerSide=Local --dbServer=bhn050103000 --dbName=Exemplo12124

#bbb#f1f1f1Instala biblioteca exe

TOTVSAutomationInstaller.exe -t=Biblioteca -e --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.exe"

#bbb#f1f1f1Checa ambiente SERVER da biblioteca

TOTVSAutomationInstaller.exe -t=Biblioteca -s --installPath="C:\TOTVS" --layerSide=Server --version=12.1.24.1

#bbb#f1f1f1Checa ambiente CLIENT da biblioteca

TOTVSAutomationInstaller.exe -t=Biblioteca -s --installPath="C:\TOTVS" --layerSide=Client --version=12.1.24.1

#bbb#f1f1f1Checa funcional da biblioteca

TOTVSAutomationInstaller.exe -t=Biblioteca -f --alias=CorporeRM --user=mestre --password=totvs --machineName=bhn050103000

#bbb#f1f1f1Instala biblioteca msi checa ambiente e funcional

TOTVSAutomationInstaller.exe -t=Biblioteca -m -s -f --setupFile="C:\Instaladores\12.1.24\BibliotecaRM - 12.1.24.msi" --layerSide=Server --dbServer=bhn050103183 --dbName=Exemplo12124 --alias=CorporeRM --user=mestre --password=totvs --installPath="C:\TOTVS" --version=12.1.24.1 --machineName=bhn050103000

### Portal RM (MSI e EXE)

#bbb#f1f1f1Instala portal msi

TOTVSAutomationInstaller.exe -t=Portal -m --setupFile="C:\Instaladores\12.1.24\TOTVS RM Portal - 12.1.24.msi"

#bbb#f1f1f1Instala portal exe

TOTVSAutomationInstaller.exe -t=Portal -e --setupExe="C:\Instaladores\12.1.24\TOTVS RM Portal - 12.1.24.exe"

#bbb#f1f1f1Checa instalação portal

TOTVSAutomationInstaller.exe -t=Portal -s --installPath="C:\TOTVS" --layerSide=Client --version=12.1.24.1

#bbb#f1f1f1Checa funcional do portal

TOTVSAutomationInstaller.exe -t=Portal -f --machineName="localhost" --portalApplication="Corpore.Net"

#bbb#f1f1f1Checa ambiente 3 camadas do portal

TOTVSAutomationInstaller.exe -t=Portal -f --threeTier

#bbb#f1f1f1Instala portal msi e checa funcional e 3 camadas

TOTVSAutomationInstaller.exe -t=Portal -m --setupFile="C:\Instaladores\12.1.24\TOTVS RM Portal - 12.1.24.msi" -f --machineName="localhost" --portalApplication="Corpore.Net" --threeTier

#bbb#f1f1f1Instala portal exe e checa funcional e setup

TOTVSAutomationInstaller.exe -t=Portal -e --setupFile="C:\Instaladores\12.1.24\TOTVS RM Portal - 12.1.24.exe" -f --machineName="localhost" --portalApplication="Corpore.Net" -s --installPath="C:\TOTVS" --layerSide=Client   
--version=12.1.24.1

### TBC (MSI e EXE)

#bbb#f1f1f1Instala e checa TBC instalação

TOTVSAutomationInstaller.exe -t=TBC -m -s --setupFile="C:\Instaladores\12.1.24\TOTVS Business Connect - 12.1.24.msi" --installPath="C:\TOTVS"

#bbb#f1f1f1Checa TBC Funcional

TOTVSAutomationInstaller.exe -t=TBC -f

#bbb#f1f1f1Desinstala e checa TBC msi

TOTVSAutomationInstaller.exe -t=TBC -m -s --setupFile="C:\Instaladores\12.1.24\TOTVS Business Connect - 12.1.24.msi" --installPath="C:\TOTVS"

]]>

# Exemplos de utilização (Bats)

---

   Exemplos de Bats para algumas funcionalidades do TAI:

### Biblioteca RM (MSI e EXE)

[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RemoveRM.bat](http://tdn.totvs.com/download/attachments/486180568/RemoveRM.bat?version=1&modificationDate=1558696992837&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_ENVIRONMENT\_COMPARE.bat](http://tdn.totvs.com/download/attachments/486180568/RM_ENVIRONMENT_COMPARE.bat?version=1&modificationDate=1558696993061&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_EXE.bat](http://tdn.totvs.com/download/attachments/486180568/RM_EXE.bat?version=1&modificationDate=1558696993184&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_EXE\_CLIENT.bat](http://tdn.totvs.com/download/attachments/486180568/RM_EXE_CLIENT.bat?version=1&modificationDate=1558696993296&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_EXE\_LOCAL.bat](http://tdn.totvs.com/download/attachments/486180568/RM_EXE_LOCAL.bat?version=1&modificationDate=1558696993415&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_EXE\_SERVER.bat](http://tdn.totvs.com/download/attachments/486180568/RM_EXE_SERVER.bat?version=1&modificationDate=1558696993546&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_MSI\_CLIENT.bat](http://tdn.totvs.com/download/attachments/486180568/RM_MSI_CLIENT.bat?version=1&modificationDate=1558696993664&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_MSI\_LOCAL.bat](http://tdn.totvs.com/download/attachments/486180568/RM_MSI_LOCAL.bat?version=1&modificationDate=1558696993815&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_MSI\_SERVER.bat](http://tdn.totvs.com/download/attachments/486180568/RM_MSI_SERVER.bat?version=1&modificationDate=1558696993949&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_PATCH\_CLIENT.bat](http://tdn.totvs.com/download/attachments/486180568/RM_PATCH_CLIENT.bat?version=1&modificationDate=1558696994069&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_PATCH\_LOCAL.bat](http://tdn.totvs.com/download/attachments/486180568/RM_PATCH_LOCAL.bat?version=1&modificationDate=1558696994191&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RM\_PATCH\_SERVER.bat](http://tdn.totvs.com/download/attachments/486180568/RM_PATCH_SERVER.bat?version=1&modificationDate=1558696994315&api=v2)

]]>

### Portal RM (MSI e EXE)

[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

PORTAL\_\_PATCH\_3Camadas.bat](http://tdn.totvs.com/download/attachments/486180568/PORTAL__PATCH_3Camadas.bat?version=1&modificationDate=1558698895639&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

PORTAL\_EXE.bat](http://tdn.totvs.com/download/attachments/486180568/PORTAL_EXE.bat?version=1&modificationDate=1558698896110&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

PORTAL\_MSI.bat](http://tdn.totvs.com/download/attachments/486180568/PORTAL_MSI.bat?version=1&modificationDate=1558698896589&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

PORTAL\_MSI\_3Camadas.bat](http://tdn.totvs.com/download/attachments/486180568/PORTAL_MSI_3Camadas.bat?version=1&modificationDate=1558698896947&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

PORTAL\_PATCH.bat](http://tdn.totvs.com/download/attachments/486180568/PORTAL_PATCH.bat?version=1&modificationDate=1558698897361&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RemovePortal.bat](http://tdn.totvs.com/download/attachments/486180568/RemovePortal.bat?version=1&modificationDate=1558698897693&api=v2)

]]>

### TBC (MSI e EXE)

[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

TBC.bat](http://tdn.totvs.com/download/attachments/486180568/TBC.bat?version=1&modificationDate=1558699479438&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

RemoveTBC.bat](http://tdn.totvs.com/download/attachments/486180568/RemoveTBC.bat?version=1&modificationDate=1558699479281&api=v2)

]]>
[![](/download/thumbnails/486180568/bat-file-format-symbol.png?version=1&modificationDate=1558698503067&api=v2)

TBC\_EXE.bat](http://tdn.totvs.com/download/attachments/486180568/TBC_EXE.bat?version=1&modificationDate=1558699479580&api=v2)

]]>]]>]]>]]>

# Logs

---

   Lista dos Logs gerados pelo TAI:

### Biblioteca RM (MSI e EXE)

#bbb#f1f1f1BibliotecaInstallationReport.json

Relatório sobre o ambiente após a instalação da Biblioteca RM.

js1JSONtrue#bbb#f1f1f1EnvironmentReport.json

Relatório sobre a estrutura de pastas após a instalação da Biblioteca RM.

Objetivo: Avalia todos os arquivos do ambiente e retorna o nome, a versão, a data de criação e o tamanho do arquivo.

js1JSONtrue#bbb#f1f1f1CompareFilesReport.json

Relatório sobre a comparação entre os arquivos comuns a uma instalação client e uma outra server da Biblioteca RM.

Objetivo: Avalia se os arquivos comuns entre uma instalação client e outra server tem o mesmo tamanho, se estão na mesma versão, se tem o mesmo nome e se foram criados no mesmo dia.

js1JSONtrue#bbb#f1f1f1FunctionalLibReport.json

Relatório sobre a realização de testes funcionais (Execução de Jobs) contra uma instalação da Biblioteca RM.

Objetivo do Teste: Avaliar se a execução de jobs funciona corretamente.

js1JSONtrue#bbb#f1f1f1MDIReport.json

Relatório sobre a realização de testes funcionais (Execução de Controllers) contra uma instalação da Biblioteca RM.

Objetivo do Teste: Avaliar se as actions principais do sistema são executadas corretamente.

js1JSONtrue

### Portal RM (MSI e EXE)

#bbb#f1f1f1PortalInstallationReport.json

Relatório sobre o ambiente após a instalação do RM Portal.

js1JSONtrue#bbb#f1f1f1ReportPortal.json

Relatório sobre a realização de testes funcionais contra o ambiente de instalação do RM Portal.

Objetivo do teste: Através do Webdriver, realiza-se testes de login, logoff e testes gerais de tela.

js1JSONtrue#bbb#f1f1f1ReportPortal3camadas.json

Relatório sobre a realização de testes funcionais contra o ambiente de instalação do RM Portal (Teste Sistêmico).

Objetivo do teste: Através do Webdriver, realiza-se testes de login, logoff e testes gerais de tela.

js1JSONtrue

### TBC (MSI e EXE)

#bbb#f1f1f1TBCReport.json

Relatório sobre o ambiente após a instalação do TBC.

js1JSONtrue#bbb#f1f1f1TBCFunctionalReport.json

Relatório sobre a realização de testes funcionais contra o ambiente de instalação do TBC.

Objetivo do teste: Verificar se a tela principal do TBC responde corretamente à requisições.

js1JSONtrue

### SummaryReport

#bbb#f1f1f1SummaryReport.json

Relatório conclusivo sobre a instalação de um determinado ambiente, seja ele Biblioteca RM, Portal RM ou TBC.

js1JSONtrue]]>
