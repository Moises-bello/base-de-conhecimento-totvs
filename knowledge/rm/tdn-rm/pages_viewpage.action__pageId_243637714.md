---
content_hash: afdc8e57a417514b4c7e9b81f58883cdc228edc0d6cacb2485735ad1a040c6b5
fetched_at: '2026-06-29T00:08:12.180349+00:00'
page_id: '243637714'
product: rm
source: tdn-rm
title: OFERTA P – Procedimento para instalação e configuração do ambiente.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243637714
version: 2
---

Antes da instalação

Esse documento visa disponibilizar instruções claras, na necessidade de configurar um novo pool de clientes do Oferta P. A estrutura padrão considera para o ambiente de produção: 3 servidores de aplicação, 2 servidores de JOB, 1 servidor portal/educamobile e 1 servidor de Banco de Dados.

É necessário verificar as permissões administrativos para acesso aos ambientes e a disponibilidade da equipe CLOUD para publicação dos IP externos/domínios que serão utilizadas no Totvsupdate, Portal e EducaMobile

## Checklist

Checklist para instalação e configuração do Oferta P

|  |  |
| --- | --- |
| **ITEM** | **STATUS** |
| Instalação N Camadas |  |
| Net Framework. 4.5 |  |
| Instalação do Portal do Cliente |  |
| Instalação do EducaMobile |  |
| Balanceamento Nativo |  |
| Isolamento de Processos |  |
| Configuração Tarefa - Commands |  |
| Totvs Update |  |
| Enable 32-bit Applications |  |
| SmartClient |  |
| Instalação do IIS (Internet Information Services) |  |
| Publicação dos Dominios do Portal e EducaMobile |  |
| Instalação e parametrização de acesso ao Banco de Dados. |  |
| Configuração do Aliaspatch |  |
| License Server . |  |

## Requisitos de Hardware

**Infraestrutura - App + Job**

* 03 VM, 08 VCPU, 16 GB Memória, 70 GB HD SAS 15k, Windows Server 2012 Standard (APP - Produção)
* 02 VM, 08 VCPU, 16 GB Memória, 70 GB HD SAS 15k, Windows Server 2012 Standard (JOB - Produção)
* 01 VM, 04 VCPU, 08 GB Memória, 60 GB HD SAS 15k, Windows Server 2012 Standard (APP - Teste)
* 01 VM, 06 VCPU, 08 GB Memória, 80 GB HD SAS 15k, Windows Server 2012 Standard (JOB RM - Teste)

* 5 Mbps de Link de Internet
* Backup do ambiente de Produção (Aplicação e Banco de Dados)

**Infraestrutura** **- IIS** **Portal**

* 01 VM, 08 VCPU, 16 GB Memória, 70 GB HD SAS 15k (2 Partições), Windows Server 2012 Standard (IIS Portal - Produção)
* 01 VM, 04 VCPU, 08 GB Memória, 70 GB HD SAS 15k (2 Partições), Windows Server 2012 Standard (IIS Portal - Teste)

**Infraestrutura - Banco De Dados**

* 01 Servidor Físico, Dual Quad Core, 96 GB memória, sem disco local, Placa HBA, Windows Server 2012 Standard (Banco de Dados do RM de Produção e Teste).

* 2,7 TB de Armazenamento de Dados (Dados + Log).
* 200 GB SSD de Armazenamento de Dados ( TempDB).
* Licenciamento do SQL Server 2014 Standard

**Infraestrutura - (Nuvem Privada - Protheus)**

* Firewall Virtual para Segurança e criação de regras de acesso
* 02 VLANs (1 para Aplicação e 1 para Banco de Dados)

## Requisitos de Sistema

* Servidor Windows 2012 64 bits ou superior com biblioteca TOTVS RM Instalado (Avaliar portabilidade da versão)
* Usuário do servidor do banco de dados para acesso ao banco do TOTVS (leitura e gravação SQL Server 2014)
* Usuário do TOTVS para ser usado no Web Service
* Usuário com poderes administrativos na rede em todos os servidores
* Framework 4.5.2
* IIS (Internet Information Services)

## Banco de Dados

Antes de iniciar a instalação é importante validar alguns problemas conhecidos para a instalação do SQL Server no Windows Server 2012.   
 Abaixo Knowledge Base:  
 <https://support.microsoft.com/pt-br/kb/2681562>   
 As seções a seguir listam os requisitos mínimos de hardware e de software para instalação e execução do SQL Server 2012:  
 <https://msdn.microsoft.com/pt-br/library/ms143506%28v=sql.110%29.aspx>

## Processo de instalação e criação de instância

Após a liberação de acesso ao servidor de Banco de Dados, será necessário realizar a instalação do SQL Server Microsoft SQL Server 2014 Standard Edition (64-bit).   
 Segue abaixo algumas recomendações sobre a instalação:

* Não utilize uma Instância Nomeada;
* Marque a opção Automatic no Startup Type (Tipo de Inicialização) para os serviços Server Agent, Server Database Engine e Server Browser;
* Informe o collation SQL\_Latin1\_General\_CP1\_CI\_AI;
* Selecione a opção Mixed Mode - Nessa opção, poderão autenticar tanto contas Windows e contas criadas posteriormente dentro do SQL;

* Defina a senha do usuário sa. Atenção: o sa é o usuário master do seu SQL Server, por isso não atribua uma senha fraca e não esqueça a senha.
* Adicionar uma conta Windows ao grupo de administradores do SQL. Clicando em ADD ou pode adicionar uma conta de administrador e também o usuário atual clicando no botão Add Current User.

Após a instalação do SQL Server, realize a restauração de uma Base de Dados exemplo/vazia da versão 12.1, está Base de Dados será utilizada como teste para conexão com o Banco de Dados e para parametrização inicial da Biblioteca. Necessária a execução do script de Acerta Usuário para criação dos logins rm/sysdba e permissões correspondentes <http://tdn.totvs.com/x/QQixAw>   
 Para comunicação com o Banco de Dados, solicite a equipe de cloud as liberação dos ips/portas dos servidores de app, job e portal.   
 Realize a configuração conforme link abaixo:  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=61933690>

## Instalação e Configuração N Camadas

Na Arquitetura N camadas, apesar da complexidade do ambiente, a divisão das tarefas em camadas possibilita maior distribuição do processamento do sistema.

**CLIENT** - Na camada cliente temos apenas os formulários que serão abertos na execução do programa.   
 **APP** - A camada de aplicação é responsável pela execução da Regra de Negócio e Cálculos além de fazer a comunicação com a Camada de Banco de Dados.   
 **JOB** - A camada de Jobs é responsável pela execução dos processos e também faz a comunicação com a Camada de Banco de Dados.

A .NET Framework é uma biblioteca de classes que reúne todas as funções normalmente associadas ao sistema operacional. O .NET Framework permite a criação de código gerenciado que não pode danificar o sistema de execução. Acesse o Server Manager e realize a instalação da versão 4.5:   
   
   
   
   
 Em seguida será necessário realizar a instalação da Biblioteca CorporeRM em todos os servidores. Porém é necessário considerar as carateriticas do ambiente N camadas.

**Servidores de Aplicação**

Instalar a Biblioteca RM nos Servidores de Aplicação (no momento de instalação, selecionar ambiente 3 camadas e Server). Ao selecionar Modo Server serão copiados para a pasta de instalação somente os arquivos necessários para o processamento de informações, ou seja, arquivos necessários para a execução do Host

Dever ser realizada a separação entre JobServer e AppServer:

* Habilitar JobServer3Camadas em todos os configs;
* Desabilitar a execução de Jobs no AppServer;
* Habilitar execução de Jobs no JobServer;
* Reiniciar os Hosts.

**Servidores de JOB**

    
 É um dos serviços executados pelo Host em background, na arquitetura N camadas, esse serviço é habilitado somente no servidor de Jobs. É responsável por executar os processos submetidos pelos aplicativos, que entram em uma fila de execução (GJOBXEXECUCAO). Para instalar um servidor de Jobs Server, siga os mesmos passos de instalação de um servidor de Aplicação, após conclusão da instalação da Biblioteca RM é necessário habilitar o processamento de Jobs no servidor

Após a instalação do Servidor de JOB, acesse o RM.AliasManager.exe para que seja realizada as configurações do número de Jobs executados simultaneamente, intervalo de monitoramento da fila de processos e se o servidor irá processar somente seus próprios Jobs. Determine a quantidade de execuções simultâneas conforme a quantidade de núcleos disponíveis nos servidores de JOB, reduza o intervalo de monitoramento e desmarque o processamento de somente seus próprios Jobs.

<JobServerMaxThreads>15</JobServerMaxThreads>  
 <JobServerLocalOnly>false</JobServerLocalOnly>  
 <JobServerPollingInterval>2</JobServerPollingInterval>

Em todos os servidores deverá ser inclusa as tags FileServerPath e LogPath   
  

**FileServerPath:** Define um único diretório para geração e leitura de arquivos temporários, assim todos os Hosts do ambiente irão gerar os arquivos somente neste diretório. Em ambientes N camadas, de-se adicionar a Tag "FileServerPath" nos arquivos (RM.Host.exe.config ou RM.host.Service.exe.config) de todos os servidores de APP e Job. Exemplo: <add key="FileServerPath" value="\\Servidor\Pasta" />

 

**LogPath:** Define o caminho onde serão gerados os log's do sistema. Exemplo: <add key="LogPath" value="\\Servidor\Pasta" />

**Enablecompression**: Habilita compressão de dados para melhorar desempenho de rede, contudo o custo para compactação e descompactação dos dados em redes Gigabits, pode ser superior a transferências sem a compactação.   
 Exemplo: <add key="enablecompression" value "true" />

Realize a configuração conforme link abaixo:  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=236432384>

## 5.1 Isolamento de processos

O isolamento de processo consiste em habilitar o RM.Host.JobRunner para execução das threads/processos realizados pelos usuários. Dessa forma garantimos que o serviço do Host mantenha-se estável e dedicado somente à abertura de telas e realizações de alguns cálculos de regras de negócio dos aplicativos.

Está configuração deve ser executada somente na camada JOB, após a instalação da BibliotecaRM é necessário aplicar o isolamento de processos. Procedimento que será realizado a partir da inserção das seguintes tags no arquivo RM.Host.Service.exe:

<add key="ISOLATEPROCESS" value="true" />  
 <add key="ENABLEPROCESSISOLATION" value="true" />

Vale ressaltar que o arquivo RM.Host.JobRunner.exe deverá possuir o mesmo conteúdo do arquivo RM.Host.Service.exe.

Realize a configuração conforme link abaixo:  
 <http://tdn.totvs.com/display/public/LRM/BD0006_Isolamento_Processos_BR>

## 5.2 Balanceamento Nativo

Com o Balanceamento Nativo, todas as requisições serão balanceadas entre os hosts disponíveis descritos no arquivo de configuração do aplicativo (RM.exe.config ou outros como por exemplo RMLabore.exe.config), mantendo o consumo de memória RAM e CPU dimensionado entre eles (4 serviços RM.Host.Service). Além disso, quando se utiliza Multiplos Hots é possível obter contingência caso algum deles venha a ter inconsistência, não afetando o ambiente de produção.

Obs.: Está configuração não deve ser realizada na camada JOB

Após a instalação da biblioteca CorporeRM em modo server, é necessário acessar o executável RM.Host.ServiceManager.exe e adicionar quatro hosts. É necessária atenção na inclusão das portas, estas não devem se repetir entre os servidores, conforme imagem abaixo.   
   
   
   
   
   
 Realize está configuração em todos os servidores de aplicação e verifique se os arquivos. config correspondentes foram criados com sucesso.

Realize a configuração conforme link abaixo:  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=233756539>

## 6. Commands (NGEN)

Precisamos rodar o Commands.bat em todos servidores e clientes, este possui o objetivo de registrar os componentes do RM no Assembly e na imagem nativa (NGEN)   
 Devido à demora na execução completa, recomendo que execute a bat somente no final no expediente.

Realize a configuração conforme link abaixo:  
 <http://tdn.totvs.com.br/pages/releaseview.action?pageId=235601768>

## Totvs Update

A Ferramenta TOTVS Update é utilizada para realizar atualizações automáticas no ambiente 3 Camadas, seja Client ou Server.

Recomendo que defina um dos servidores de aplicação como servidor de aplicação, sendo assim, insira a tag <add key="UpdateServerEnabled" value="true"/> no arquivo RM.Host.Service.exe.Config e reinicie o serviço do HOST.

Nos demais servidores do pool insera no arquivo RM.Host.Service.exe.Config e RM.exe.Config as tag <add key="UpdateServer" value="host:porta"/> - Informe o nome da máquina e porta que o HOST do Servidor de Atualização que será utilizado.

Exemplo:

Realize a configuração conforme link abaixo:<http://tdn.totvs.com/display/public/LRM/GLB0008_TOTVS_UPDATE>

Além disso, para que o download da aplicação seja realizado com êxito, necessário solicitar a equipe de Cloud a publicação externamente do ip do servidor de atualização ex: http:// *ip + porta do servidor de atualização* /wsUpdate, direcionando para este servidor interno, possibilitando download da ferramenta "TOTVS Update"

## Instalação e configuração Portal

Requisitos Necessários para instalação e utilização do Portal RM

* Framework 4.0
* IIS (Internet Information Services)
* Biblioteca CorporeRM

Para instalação do Portal, a máquina já deve estar com o IIS instalado.   
   
   
   
   
 Erros na instalação do portal estão diretamente relacionados a má instalação do IIS.

Para configuração do Portal no IIS, acesse o caminho Painel de Controle – Ferramentas Administrativas - o IIS (Internet Information Services). Adicone o diretório Corpore.net no Default Web Site do IIS.

  Reinicie o IIS através do comando issreset através do prompt de comando

Após essas configurações, o portal deverá estar pronto para utilização. Acesse o navegador, e digite o caminho HTTP://localhost/Corpore.net ou no IIS clique com o botão sobre o Corpore.net e selecione a opção 'Manage Application' / 'Browse'.

No servidor de IIS também deverá ser realizada instalação do EducaMobile - TOTVS Educa Mobile - 12.1.11.msi e a mesma parametrização citada acima deverá ser realizada considerando o diretório C:\totvs\CorporeRM\EducaMobile

Cada cliente irá possuir um diretório específico para identificação do Portal, evitando que outros clientes acessem outro portal incorretamente:

Estes diretórios deveram ser adicionados no IIS, assim como ocorreu no com o Corpore.Net.

Realize a instalação da Biblioteca e do Portal conforme link abaixo:  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=59900164>

\_GoBack  
 Lembrando que se faz necessário - juntamente com a equipe de Cloud - criar uma regra para acesso externo no DNS, permitindo acesso ao Portal e Educa Mobile que encontra-se hospedado no servidor de IIS

Exemplos:   
  

**Servidor de IIS**. 172.21.116.18:8084   
  

**Externo**: **cliente**.portaleducacional.cloudtotvs.com.br   
  

**Internamente** estão acessíveis através dos links abaixo:

Portal Educacional: http://+ +ip interno /Corpore.Net   
 Educa Mobile: http://+ +ip interno /EducaMobile

## Testes

Ao fim da execução das etapas anteriores, é recomendado realizar os seguintes testes para garantir que as configurações foram executadas com sucesso:

1º - Através do diretório RM.NET execute o aplicativo rm.exe e acesse a nova MDI, este teste deverá ser realizado com o usuário mestre e em todos os servidores;

2º - Acesse o domínio http:// *ip + porta do servidor de atualização* /wsUpdate para testar o correto funcionamento do smartclient.

3º - Acesse o domínio <http://portaleducacional.cloudtotvs.com.br/corpore.net> e <http://portaleducacional.cloudtotvs.com.br/educamobile> para testar o funcionamento do Portal e do EducaMobile.
