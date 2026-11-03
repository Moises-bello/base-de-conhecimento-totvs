---
content_hash: 3d285173989d570fd50be0281aa6cab30cdf62e1f572f8da425f9e4d9ab10ffc
fetched_at: '2026-06-29T00:09:35.890656+00:00'
page_id: '425459414'
product: rm
source: tdn-rm
title: Configurar o arquivo de Configuração AppServer.ini - Protheus 11
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459414
version: 11
---

**Configurar o arquivo de Configuração AppServer.ini- Protheus 11**

---

Obs: o arquivo abaixo é meramente um exemplo.

**[p11sql]nome do ambiente no dbaccess**

SourcePath=C:\TOTVS\Protheus\P11\_sql\apo

RootPath=C:\TOTVS\Protheus\P11\_sql\protheus\_data

StartPath=\system\

RpoDb=top

RpoLanguage=portuguese

RpoVersion=110

LocalFiles=ctree

localdbextension=.dtc

HELPSERVER=localhost/p115

PictFormat=DEFAULT topDatabase=mssql

topServer=localhost

topAlias=p11sql  \*\_+nome da base de dados+\_\*

PORT=7890

RegionalLanguage=BRA

specialkey=p11\_sql

PanelPort=1234

**[Drivers]**

ACTIVE=TCP

**[TCP]**

TYPE=TCPIP

PORT=9876 \*

**[HTTP\]  Bloco que define o webservice do EAI TOTVS Protheus**

ENABLE=1

PORT=83

PATH=\web\EAI

ENVIRONMENT=p11sql

RESPONSEJOB=JOB\_EAI\_0101

**[localhost:83] Bloco que define o servidor onde está o webservice  do EAI TOTVS Protheus por host**

ENABLE=1

PATH=C:\TOTVS\Protheus\P11\_sql\protheus\_data

ENVIRONMENT=p11sql

INSTANCENAME=EAI

RESPONSEJOB=JOB\_EAI\_0101

DEFAULTPAGE=wsindex.apw

**[10.31.6.76:83\] Bloco que define o servidor onde está o webservice  do EAI TOTVS Protheus por IP**

ENABLE=1

PATH=C:\TOTVS\Protheus\P11\_sql\protheus\_data

ENVIRONMENT=p11sql

INSTANCENAME=EAI

RESPONSEJOB=JOB\_EAI\_0101

DEFAULTPAGE=wsindex.apw

**[bhd050101845:83\] Bloco que define o servidor onde está o webservice  do EAI TOTVS Protheus por DNS**

ENABLE=1

PATH=C:\TOTVS\Protheus\P11\_sql\protheus\_data

ENVIRONMENT=p11sql

INSTANCENAME=EAI

RESPONSEJOB=JOB\_EAI\_0101

DEFAULTPAGE=wsindex.apw

**[LICENSECLIENT]**

;SERVER=172.16.97.24

;server=10.31.6.76

;PORT=5555

**[JOB\_EAI\_0101]**  Bloco que define  os parâmetros do serviço do  appserver

TYPE=WEBEX

ENVIRONMENT=p11sql

INSTANCES=10,100

SIGAWEB=WS

INSTANCENAME=EAI

ONSTART=\_\_WSSTART

ONCONNECT=\_\_WSCONNECT

PREPAREIN=99,01

NAMESPACE=http://www.totvs.com.br/rm/ ;

WEBSERVICELOCATION=http://172.16.104.22:84

;URLLocation=http://172.16.104.22:84

DEFAULTPAGE=wsindex.apw

**[ONSTART]**

JOB=JOB\_EAI\_0101

REFRESHRATE=600

**[General]**

CHECKSPECIALKEY=0

InstallPath=C:\TOTVS\Protheus\P11\_sql

CONSOLELOG=1

**[SERVICE]**

NAME=.1035-PROTHEUS11A

DISPLAYNAME=.1035-PROTHEUS11A
