---
article_id: 360055299594
category: 'Aplicativo MNTNG '
content_hash: c67a09d0113e707671d4ea24d39c0ac95adfeae588390f65f36173a439d84269
fetched_at: '2026-06-28T22:42:37.623712+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Como corrigir a mensagem DBUseArea
  - DB driver not initialized no app MNTNG
type: support-article
updated_at: '2026-05-08T11:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055299594-Manufatura-Linha-Protheus-APP-MNT-Como-corrigir-a-mensagem-DBUseArea-DB-driver-not-initialized-no-app-MNTNG
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40323721439511)* Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Ao realizar processos no **MNTNG** é apresentada a mensagem **DBUseArea - DB driver not initialized**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Causa**  
Este erro é ocasionado devido a ausência ou configuração incorreta das chaves **DBDataBase, DBServer, DBServer, DBPort e DBAlias**. Este também ocorre devido a utilização das chaves: **TOPDATABASE**, **TOPSERVER**, **TOPPORT** e **TOPALIAS**.  
  
**Solução**  
Ao identificar ou mesmo de forma a evitar a mensagem **DBUseArea - DB driver not initialized** durante a utilização do **App MNTNG**, deve-se realizar algumas configurações simples no arquivo **appserver.ini** conforme descrito a seguir:  
  
Na seção **Environment** a qual esteja vinculado o processo **REST** definir as chaves:

```
DBDataBase=<define o tipo do banco de dados utilizado no ambiente, 
podendo ser informado: DB2, INFORMIX, MSSQL, MYSQL, ORACLE e POSTGRES>
DBServer=<endereço ou IP do servidor TOTVS | DBAcess>
DBPort=<porta de acesso TOTVS | DBAcess>
DBAlias=<nome do banco de dados>
```

Todas as chaves mencionadas devem substituir as respectivas chaves caso estas existam no arquivo de configuração: **TOPDATABASE**, **TOPSERVER**, **TOPPORT** e **TOPALIAS**. Ao fim o arquivo deve ficar semelhante ao apresentado no exemplo:

```
[P12127_DDB_REST]
SourcePath=D:\Totvs\Apo\Apo_12127
RootPath=D:\Totvs\Protheus_Data
StartPath=\system_12127_DDB\
RpoDb=SQL
RpoLanguage=Portuguese
RpoVersion=120
LocalFiles=CTREE
localdbextension=.dtc
TopMemoMega=1
DBDataBase=MSSQL7
DBServer=localhost
DBAlias=P12127_DDB_REST
DBPort=12380
HELPSERVER=Localhost:8080
SpecialKey=NGP12127_DDB_HPS
KillStack=1
StartSysInDb=1
```
