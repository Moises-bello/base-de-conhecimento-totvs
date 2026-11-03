---
content_hash: 440e6f44e78a5c209395ab19dd850ddb9aa67ce7637626166a9c08736eff5372
fetched_at: '2026-06-28T21:35:20.685954+00:00'
page_id: '233765477'
product: fluig
source: tdn-fluig
title: ARQ - Mensagem "Atenção, não constam no banco de dados as configurações da
  plataforma", como resolver?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233765477
version: 21
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Banco de Dados:** Oracle, MySQL

# Ocorrência

Após a atualização da plataforma, ao tentar iniciar os serviços são exibidos avisos e erros no arquivo de log, como no exemplo abaixo:

javaEclipseserver.logtruetrue(PhysicalConnection.java:715)
at oracle.jdbc.driver.T4CConnection.(T4CConnection.java:385)
at oracle.jdbc.driver.T4CDriverExtension.getConnection(T4CDriverExtension.java:30)
at oracle.jdbc.driver.OracleDriver.connect(OracleDriver.java:564)
at org.jboss.jca.adapters.jdbc.local.LocalManagedConnectionFactory.getLocalManagedConnection(LocalManagedConnectionFactory.java:323)
... 14 more
Caused by: oracle.net.ns.NetException: Listener refused the connection with the following error:
ORA-12514, TNS:listener does not currently know of service requested in connect descriptor
at oracle.net.ns.NSProtocolStream.negotiateConnection(NSProtocolStream.java:272)
at oracle.net.ns.NSProtocol.connect(NSProtocol.java:263)
at oracle.jdbc.driver.T4CConnection.connect(T4CConnection.java:1360)
at oracle.jdbc.driver.T4CConnection.logon(T4CConnection.java:486)
... 19 more
16:49:25,803 INFO [stdout] (Thread-69) ===============================================================
16:49:25,803 INFO [stdout] (Thread-69) == Atenção, não constam no banco de dados as configurações ==
16:49:25,803 INFO [stdout] (Thread-69) == da plataforma. Certifique-se que a instalação/atualização ==
16:49:25,803 INFO [stdout] (Thread-69) == foi realizada através do instalador gráfico ou linha ==
16:49:25,803 INFO [stdout] (Thread-69) == de comando. ==
16:49:25,803 INFO [stdout] (Thread-69) ===============================================================
16:49:25,803 ERROR [stderr] (Thread-69) com.totvs.technology.wcm.WCMService$NoConfigException
16:49:25,803 ERROR [stderr] (Thread-69) at com.totvs.technology.wcm.WCMService.validateConfigurations(WCMService.java:705)
16:49:25,803 ERROR [stderr] (Thread-69) at com.totvs.technology.wcm.WCMService.doStartUp(WCMService.java:411)
16:49:25,803 ERROR [stderr] (Thread-69) at com.totvs.technology.wcm.WCMService.access$300(WCMService.java:86)
16:49:25,803 ERROR [stderr] (Thread-69) at com.totvs.technology.wcm.WCMService$StandAloneScanner.run(WCMService.java:931)
16:49:25,803 ERROR [stderr] (Thread-69) at java.lang.Thread.run(Thread.java:745)
16:49:25,803 INFO [stdout] (Thread-69) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
16:49:25,803 INFO [stdout] (Thread-69) Startup stoped.
16:49:25,803 INFO [stdout] (Thread-69) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
]]>

# Causa

No arquivo de log, o aviso *"Throwable while attempting to get a new connection: null: javax.resource.ResourceException: Could not create connection"* indica que não foi possível realizar a conexão com o banco de dados.

Logo abaixo é exibido o aviso *"Caused by: java.sql.SQLRecoverableException: Listener refused the connection with the following error: ORA-12514, TNS:listener does not currently know of service requested in connect descriptor"* indicando que a instância do banco foi iniciada antes do *listener* ou que o Oracle não reconhece o serviço configurado.

# Solução

Verifique as configurações do banco e se as informações estão corretas no arquivo de configuração da plataforma.

0.5falsesamplefadetrue4A partir da 2.0

* Acesse o diretório **[diretório\_instalação****]****\appserver\standalone\configuration** e edite o arquivo **standalone****.xml**;
* Procure pelo bloco **<****datasources>**;
* Nesse bloco verifique todas as informações relacionadas à conexão com o banco, como por exemplo, usuário, senha e nome da base.

Exemplo de configuração com banco de dados Oracle:

xmlEclipsestandalone.xmltrue

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

10
20

usuario
senha


true
false

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false


oracle.jdbc.driver.OracleDriver
]]>true31.6.5-190514 a 1.8.2

* Acesse o diretório **[diretório\_instalação****]****\appserver\domain\configuration** e edite o arquivo **domain****.xml**;
* Procure pelo bloco **<****datasources>**;
* Nesse bloco verifique todas as informações relacionadas à conexão com o banco, como por exemplo, usuário, senha e nome da base.

Exemplo de configuração com banco de dados Oracle:

xmlEclipsedomain.xmltrue

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

10
20

usuario
senha


true
false

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false


oracle.jdbc.driver.OracleDriver
]]>11.6.0 a 1.6.5-190507

* Acesse o diretório **[diretório\_instalação****]****\appserver\domain\configuration** e edite o arquivo **domain****.xml**;
* Procure pelo bloco **<****datasources>**;
* Nesse bloco verifique todas as informações relacionadas à conexão com o banco, como por exemplo, usuário, senha e nome da base.

Exemplo de configuração com banco de dados Oracle:

xmlEclipsedomain.xmltrue

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

10
20

usuario
senha


true
false

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false


oracle.jdbc.driver.OracleDriver
]]>2Até a versão 1.5.13

* Acesse o diretório **[diretório\_instalação****]\jboss\standalone\configuration** e edite o arquivo **standalone.xml**;
* Procure pelo bloco **<****datasources>**;
* Nesse bloco verifique todas as informações relacionadas à conexão com o banco, como por exemplo, usuário, senha e nome da base.

Exemplo de configuração com banco de dados Oracle:

xmlEclipsestandalone.xmltrue

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

10
20

usuario
senha


true
false

false

jdbc:oracle:thin:@192.168.0.1:1521:FLUIG
oracleDriver
alter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI'
TRANSACTION\_READ\_COMMITTED

5
15

usuario
senha


true
false

30000

false


oracle.jdbc.driver.OracleDriver
]]>Observações!

Para saber mais sobre como configurar o banco de dados Oracle acesse .

Consulte também a página .
