---
content_hash: cf832d6e6fd2891936e1aca102d5b2075bf0eef9d28c2b7bb9fce8318feaa190
fetched_at: '2026-06-29T00:09:35.904099+00:00'
page_id: '425459424'
product: rm
source: tdn-rm
title: Configurar o arquivo de Configuração AppServer.ini- Protheus 12
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459424
version: 11
---

**Configurar o arquivo de Configuração AppServer.ini- Protheus 12**

---

**Obs: o arquivo abaixo é meramente um exemplo.**

**[PADRAO]**

SourcePath=C:\Protheus1210\apo

RootPath=C:\Protheus1210\protheus\_data

StartPath=\system\ x2\_path= RpoDb=top

RpoLanguage=Portuguese

RpoVersion=120

Trace=0

LocalFiles=CTREE

localdbextension=.dtc

TopMemoMega=1

TOPDATABASE=MSSQL

TOPSERVER=localhost

TOPALIAS=EAI\_PR1210 ;

TOPALIASRM=EAI\_RM1210 ;

TOPALIAS=EAI\_PR1210 ;

TOPALIASRM=EAI\_RM\_1212\_TOP

TOPALIASRM=EAI\_RM\_1212\_T

TOPPORT=7890

REGIONALLANGUAGE=BRA

**\*\[TDS\]\***

```
ALLOWEDIT=* ALLOWAPPLYPATCH=* \[Drivers\] Active=TCP
```

```
*\[TCP\]*
```

```
TYPE=TCPIP Port=1234
*\[Service\]* Name=TOTVS-Appserver12 DisplayName=TOTVS | Appserver 12 service
*\[GENTCPIP\]*
```

```
Enable=0
```

**\*\[HTTP\]\***

```
ENABLE=1
```

```
PORT=83
```

```
PATH=C:\Protheus1210\protheus_data\web\eai
```

**\*\[LOCALHOST:83\]\***

```
ENABLE=1
```

```
PATH=C:\Protheus1210\protheus_data\web\eai
```

```
ENVIRONMENT=PADRAO
```

```
INSTANCENAME=EAI
```

```
RESPONSEJOB=JOB_EAI
```

```
DEFAULTPAGE=wsindex.apw*\[BHD0001894:83\]*
```

ENABLE=1

```
PATH=C:\Protheus1210\protheus_data\web\eai
```

```
ENVIRONMENT=PADRAO
```

```
INSTANCENAME=EAI
```

```
RESPONSEJOB=JOB_EAI
```

```
DEFAULTPAGE=wsindex.apw
```

**\*\[10.31.3.171:83\]\***

```
ENABLE=1
```

```
PATH=C:\Protheus1210\protheus_data\web\eai
```

```
ENVIRONMENT=PADRAO
```

```
INSTANCENAME=EAI
```

```
RESPONSEJOB=JOB_EAI
```

```
DEFAULTPAGE=wsindex.apw
```

**\*\[JOB\_EAI\]\***

```
TYPE=WEBEX
```

```
ENVIRONMENT=PADRAO
```

```
INSTANCES=1,30
```

```
SIGAWEB=WS
```

```
INSTANCENAME=EAI
```

```
ONSTART=__WSSTART
```

```
ONCONNECT=__WSCONNECT
```

```
PREPAREIN=99,01
```

**\*;\[ONSTART\]\* ;**

```
JOBS=JOB_EAI ;
```

```
\[OnStart\] ;
```

```
jobs=FWSCHDMANAG_PADRAO,FWSCHDQUEUE_PADRAO ;
```

```
RefreshRate=120 ;
```

```
\[FWSCHDMANAG_PADRAO\]
```

```
;Main=FWSCHDMANAG
```

```
;Environment=PADRAO
```

```
;\[FWSCHDQUEUE_PADRAO\]
```

```
;Main=FWSCHDQUEUE
```

```
;Environment=PADRAO
```
