---
content_hash: 64d8201114d3227ff20af0847c7bfa6451e71c01ef0d92bb8e38f0b893cb2fa1
fetched_at: '2026-06-29T00:05:56.506908+00:00'
page_id: '152797355'
product: rm
source: tdn-rm
title: Instaladores RM por linha de comando
type: documentation
url: https://tdn.totvs.com/display/LRM/Instaladores+RM+por+linha+de+comando
version: 64
---

# **Objetivo**

Os parâmetros de instalação do RM têm como objetivo otimizar o processo de instalação do produto, que tornará a instalação mais rápida e fácil, diminuindo a interação do instalador com o usuário.

# **Como utilizar os parâmetros**

Os parâmetros deverão ser passados no **atalho do instalador**, pelo **executar do Windows** ou via **prompt de comando**.

Atalho do instaladorExecutar do WindowsPrompt de comando

# **Instalação**

### Opções de exibição:

/quiet

* Modo silencioso, sem interação do usuário

 **Observação:** No caso de instalação de uma biblioteca “exe”, se deve substituir o “/quiet” por “/verysilent /suppressmsgboxes”, que pode ser substituído somente por “/silent”, caso queira ver as barras de progresso.

/passive

* Modo autônomo - somente barra de progresso
/q[n | b | r | f] - Define o nível da interface do usuário:

* n - Sem interface do usuário
* b - Interface do Usuário básica
* r - Interface do Usuário reduzida
* f - Interface do Usuário completa (padrão)

**Tipos de Instalação:**

Instalação Local

| SQL | | | |
| --- | --- | --- | --- |
| **Tipo de instalação** | **Parâmetro** | **Opção** | **Explicação** |
| **Local** | layer | Local | Tipo de instalação (3 camadas server, 3 camadas client ou local) |
| db | SQL | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1 | Hostname ou IP do servidor que está instalado o SGDB. |
| dbname | CorporeRM | Nome da instância utilizada no SGDB. |

**Exemplo MSI:**C\BibliotecaRM.msi /passive /qb ***layer=Local db=SQL dbserver=Servidor1 dbname=CorporeRM***

***/passive /qb são parâmetros nativos do MSI.***

**Exemplo EXE:**C\BibliotecaRM.exe  **/SILENT /SUPPRESSMSGBOXES /retry**

**/SILENT /SUPPRESSMSGBOXES /retry  são parâmetros nativos do EXE.**

| ORACLE | | | |
| --- | --- | --- | --- |
| **Tipo de instalação** | **Parâmetro** | **Opção** | **Explicação** |
| **Local** | layer | Server | Tipo de instalação (3 camadas server, 3 camadas client ou local) |
| db | ORACLE | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1/Instancia | Hostname ou IP do servidor que está instalado o SGDB e sua instância. |

**Exemplo MSI**: C\BibliotecaRM.msi /passive /qb ***layer=Local db=ORACLE dbserver=Servidor1/Instancia***

/passive /qb são parâmetros nativos do MSI.

**Exemplo EXE**:  C\BibliotecaRM.exe  **/SILENT /SUPPRESSMSGBOXES /retry**

**/SILENT /SUPPRESSMSGBOXES /retry  são parâmetros nativos do EXE.**

Instalação em 3 Camadas Server

| SQL Server | | | |
| --- | --- | --- | --- |
| **Tipo de instalação** | **Parâmetro** | **Opção** | **Explicação** |
| **3 Camadas Server** | layer | appserver ou jobsever | Tipo de instalação (3 camadas server, 3 camadas client ou local) |
| db | SQL | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1 | Hostname ou IP do servidor que está instalado o SGDB. |
| dbname | CorporeRM | Nome da instância utilizada no SGDB. |
| Fileserverpath | Informar caminho válido | Informar o caminho válido. |

Exemplo MSI: C\BibliotecaRM.msi /passive /qb ***layer=appserver db=SQL dbserver=Servidor1 dbname=CorporeRM***

***/passive /qb são parâmetros nativos do MSI.***

Exemplo EXE:  C\BibliotecaRM.exe  **/SILENT /SUPPRESSMSGBOXES /retry**

**/SILENT /SUPPRESSMSGBOXES /retry  são parâmetros nativos do EXE.**

| ORACLE | | | |
| --- | --- | --- | --- |
| **Tipo de instalação** | **Parâmetro** | **Opção** | **Explicação** |
| **3 Camadas Server** | layer | appserver ou jobsever | Tipo de instalação (3 camadas server, 3 camadas client ou local) |
| db | ORACLE | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1/Instancia | Hostname ou IP do servidor que está instalado o SGDB e sua instância. |
| Fileserverpath | Informar caminho válido | Informar caminho válido |

Exemplo MSI: C\BibliotecaRM.msi /passive /qb ***layer=appserver db=ORACLE dbserver=Servidor1/CorporeRM***

**/passive /qb são parâmetros nativos do MSI.**

Exemplo EXE:  C\BibliotecaRM.exe  **/SILENT /SUPPRESSMSGBOXES /retry**

**/SILENT /SUPPRESSMSGBOXES /retry  são parâmetros nativos do EXE.**

Instalação em 3 Camadas Client

| Tipo de instalação | Parâmetro | Opção | Explicação |
| --- | --- | --- | --- |
| **3 Camadas Client** | layer | client | Tipo de instalação (3 camadas server, 3 camadas client ou local) |
| hostserver | Servidor1 | Hostname ou IP do servidor que está instalado como 3 camadas server. |
| hostport | 8050 | Porta utilizada pelo servidor que está instalado como 3 camadas server. |

Exemplo MSI: C\BibliotecaRM.msi /passive /qb **layer=client hostserver=Servidor1 hostport=8050**

**/passive /qb são parâmetros nativos do MSI.**

Exemplo EXE:  C\BibliotecaRM.exe **/SILENT /SUPPRESSMSGBOXES /retry**

**/SILENT /SUPPRESSMSGBOXES /retry  são parâmetros nativos do EXE.**

Instalação Portais - Forma Personalizada

**Para a instalação de Portais de Forma Personalizada**

Exemplo do comando: msiexec /q /i "TOTVS RM Portal - 12.1.2205.1.msi" addlocal=**Default**, AppPortalPep, AppPortalCliente com as opções abaiixo:

A opção "/q" realiza a instalação de forma "silenciosa", sem abrir nenhuma tela para o usuário. -

A opção "addlocal" permite selecionar quais componentes do instalador deseja-se instalar.

Atualmente, os componentes possíveis de serem instalados são:

* **Default**
* AppPortalCliente
* AppRHUnificado
* AppProcessoSeletivo
* AppEducacional
* AppGestaoEducacional
* AppPortalDaObra
* AppPortalFarmacia
* AppPortalDoFornecedor
* AppPortalDoProfessor
* AppPortalPep
* AppPortalPvi
* AppPortalBiblioteca
* AppPortalPaciente
* AppPortalPvi
* AppPortalBackOffice
* AppPortalPrestador

**Importante:** Para que os portais funcionem, é necessária a instalação do componente Default, que contem arquivos comuns e obrigatórios para cada um dos portais.

  

 **Observação:** o caminho do instalador deve obrigatoriamente ser adicionado entre aspas. Veja abaixo alguns exemplos válidos:

* C:\>"BibliotecaRM - 12.1.17.1.msi"
* C:\>"BibliotecaRM - 12.1.17.1.exe"

### Parâmetros:

TOTVS Update

**Quando usado configtotvsupdate=true, é obrigatório o uso dos parâmetros servertotvsupdate e portatotvsupdate para que ocorra a configuração automática.**

******Observação: Disponível a partir da versão 12.1.24.******

| TOTVS Update | | |
| --- | --- | --- |
| **Parâmetro** | **Opção** | **Explicação** |
| configtotvsupdate | True | Irá configurar o TOTVS Update automático. |
| servertotvsupdate | Servidor1 | Servidor para atualização. |
| portatotvsupdate | 12124 | Numero de porta de acesso ao servidor informado |

****Exemplo MSI**: C\BibliotecaRM.msi /passive /qb configtotvsupdate=true servertotvsupdate=Servidor1 portatotvsupdate=12124**

TOTVS Rac

**A partir da 12.1.34**

| ORACLE | | |
| --- | --- | --- |
| **Parâmetro** | **Opção** | **Explicação** |
| useOracleRac | True | Habilita o uso do Oracle Rac |

**Exemplo MSI**: **C\BibliotecaRM.msi /passive /qb*****l**ayer=Local db=ORACLE dbserver=Servidor1/Instancia insthostcleanner=true dbuser=usuario1 dbpassword=senha1 useOracleRac=True***

HostCleanner | Informações de banco

****Quando usado insthostcleanner=true, é obrigatório o uso dos parâmetros db, dbserver, ****dbuser, dbpassword e****quando SGBD for SQL dbname, caso seja ORACLE não é necessário dbname.****

********Observação: Disponível a partir da versão 12.1.23.********

| SQL | | |
| --- | --- | --- |
| **Parâmetro** | **Opção** | **Explicação** |
| insthostcleanner | True | Irá instalar o Host Cleanner automático. |
| db | SQL | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1 | Hostname ou IP do servidor que está instalado o SGDB. |
| dbname | CorporeRM | Nome da instância utilizada no SGDB. |
| dbuser | usario1 | Usuário que será usado para fazer login no SGDB. |
| dbpassword | senha1 | Senha que será usado para fazer login no SGDB. |
| ``` AliasName ``` | CorporeRM | Nome que será atribuído ao Alias. |

* O parâmetro AliasName, quando informado, será usado também para definir o DefaultDB no arquivo de configuração do RM.Host.

****Exemplo MSI**: C\BibliotecaRM.msi /passive /qb ***layer=Local db=SQL dbserver=Servidor1 dbname=CorporeRM insthostcleanner=true dbuser=usuario1 dbpassword=senha1*****

| ORACLE | | |
| --- | --- | --- |
| **Parâmetro** | **Opção** | **Explicação** |
| insthostcleanner | True | Irá instalar o Host Cleanner automático. |
| db | SQL | Sistema Gerenciador de Banco de dados utilizado. |
| dbserver | Servidor1 | Hostname ou IP do servidor que está instalado o SGDB. |
| dbuser | usario1 | Usuário que será usado para fazer login no SGDB. |
| dbpassword | senha1 | Senha que será usado para fazer login no SGDB. |

**Exemplo MSI**: **C\BibliotecaRM.msi /passive /qb*****l**ayer=Local db=ORACLE dbserver=Servidor1/Instancia insthostcleanner=true dbuser=usuario1 dbpassword=senha1 useOracleRac=True***

Linguagem

Para passar os parâmetros de Linguagem. use a expressão **LANG**

**Observação:**Informar conforme nomenclatura descrita em: [http://msdn.microsoft.com/en-US/library/ee825488(v=cs.20).aspx](https://www.google.com/url?q=http://msdn.microsoft.com/en-US/library/ee825488%28v%3Dcs.20%29.aspx&sa=D&source=hangouts&ust=1544878133600000&usg=AFQjCNEG7DqnLgxcpPFeIEyIJzeFxAj4ig) ( Válido somente para a Instalação .msi)

A Instalação .exe aceita somente **pt**, **es** e **en**

****Exemplo MSI:****C\BibliotecaRM.msi /passive /qb *layer=Local db=SQL dbserver=Servidor1 dbname=CorporeRM **lang=pt-BR***

Quantidade de Hosts

Para passar os parâmetros de quantidade de hosts, use a expressão:

**Quantidade de Hosts**

QTDhost

**Exemplo:** C\BibliotecaRM.msi /passive /qb layer=local hostserver=Servidor1 hostport=8050 ApiPort=9090 HttpPort=9091 lang=pt-BR **QTDhost=3**

ApiPort e Httpport

**ApiPort:**

ApiPort

**HttpPort:**

HttpPort

**Exemplo:** C\BibliotecaRM.msi /passive /qb layer=local hostserver=Servidor1 hostport=8050 **ApiPort=9090 HttpPort=9091** lang=pt-BR QTDhost=3

**Observação:** Quando a quantidade de Hosts for maior que a recomendada , a instalação irá respeitar a quantidade recomendada.

Outros Parâmetros

**Habilitar segurança nos portais (WebConfigs):**

  

APLICASEGURANCAWEBCONFIG

**Exemplo:**

**No msi:**

       "C:\TOTVS RM Portal.msi" /quiet /qn layerSide=Local **APLICASEGURANCAWEBCONFIG=TRUE** (para habilitar)

        ou

       "C:\TOTVS RM Portal.msi" /quiet /qn layerSide=Local **APLICASEGURANCAWEBCONFIG=FALSE** (para não habilitar)

**No exe:**

       "C:\TOTVS RM Portal.exe" /verySILENT /suppressmsgboxes **/APLICASEGURANCAWEBCONFIG=TRUE** (para habilitar)

        ou

       "C:\TOTVS RM Portal.exe" /verySILENT /suppressmsgboxes **/APLICASEGURANCAWEBCONFIG=FALSE** (para não habilitar)

**Garbage Collector MultiThread (gcServer)**

O Garbage Collector, quando operando em ambiente Server, proporciona desempenho otimizado para hosts que possuem múltiplos núcleos, uma vez que a infraestrutura do .Net framework cria uma thread de coleta para cada núcleo.

Esta tag será adicionada automaticamente com valor “true” nos arquivos de configuração do Host (Arquivos alterados **RM.Host.exe.config, RM.Hostservice.exe.config e RM.Lib.Gerador.Execute.exe.config**)

**Exemplo:** C\BibliotecaRM.msi .../gcServer="true"

**Observação:** Por padrão, durante a instalação, a tag será adicionada como “false” no arquivo "RM.Host.JobRunner.exe.config" e deverá permanecer como “false”.

# **Desinstalação**

Parâmetros para desinstalação

| Parâmetro | Opção | Explicação |
| --- | --- | --- |
| dellal | Yes | No | Apaga todos os arquivos contido na pasta do RM. |

Exemplo MSI: msiexec /x "C:\BibliotecaRM.msi" /passive /qb **delall=Yes**

**/x, /passive, /qb são parâmetros nativos do MSI.**

**Os parâmetros de desinstalação RM serão utilizados somente nos instaladores MSI.**

Command Line

50%50%
