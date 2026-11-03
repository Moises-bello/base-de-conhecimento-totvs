---
content_hash: 4442b6977a50939828483324fbddc59986e4771d0a7d74a6f930a52c8e4d5fbe
fetched_at: '2026-06-28T21:35:24.899159+00:00'
page_id: '272156616'
product: fluig
source: tdn-fluig
title: DES - Como solucionar o erro ao tentar abrir uma conexão com o banco de dados
  Progress?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272156616
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.6.0 e superiores

# Ocorrência

Ao tentar abrir uma conexão com o banco de dados Progress no evento validateForm ocorre erro em log:

javaEclipse1024Arquivo de log>>>>>>>>>>>>>>>>>>>>>>>PASSO 01
15:33:48,635 INFO [org.apache.commons.httpclient.HttpMethodDirector] (EJB ASYNC - 635) Retrying request
15:33:48,636 INFO [org.apache.commons.httpclient.HttpMethodDirector] (EJB ASYNC - 635) I/O exception (java.net.ConnectException) caught when processing request: Conexão recusada
15:33:48,636 INFO [org.apache.commons.httpclient.HttpMethodDirector] (EJB ASYNC - 635) Retrying request
15:33:48,650 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) >>>>>>>>>>>>>>>>>>>>>>>>PASSO 02
15:33:48,650 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) ic: javax.naming.InitialContext@5c50f59a
15:33:48,651 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) >>>>>>>>>>>>>>>>>>>>>>>>PASSO 03
15:33:48,651 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) dsMGCAD: org.jboss.jca.adapters.jdbc.WrapperDataSource@1fbb6069
15:33:48,651 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) dsMGMOV: org.jboss.jca.adapters.jdbc.WrapperDataSource@4d4bffdc
15:33:48,652 WARN [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) >>>>>>>>>>>>>>>>>>>>>>>>>>> PASSO 04
15:33:48,652 WARN [com.arjuna.ats.arjuna] (http-pool-threads - 96) ARJUNA012140: Adding multiple last resources is disallowed. Trying to add LastResourceRecord(XAOnePhaseResource(LocalXAResourceImpl@1b1eca40[connectionListener=9b2f932 connectionManager=c6df2a4 warned=false currentXid=< formatId=131077, gtrid\_length=29, bqual\_length=36, tx\_uid=0:ffff7f000001:4dccde2a:58a5bc15:a0e157, node\_name=1, branch\_uid=0:ffff7f000001:4dccde2a:58a5bc15:a0e184, subordinatenodename=null, eis\_name=java:/jdbc/ProgressMGCAD > productName=OpenEdge RDBMS productVersion=10.2B07 jndiName=java:/jdbc/ProgressMGCAD])), but already have LastResourceRecord(XAOnePhaseResource(LocalXAResourceImpl@3477d674[connectionListener=41d9f113 connectionManager=4f3d754c warned=false currentXid=< formatId=131077, gtrid\_length=29, bqual\_length=36, tx\_uid=0:ffff7f000001:4dccde2a:58a5bc15:a0e157, node\_name=1, branch\_uid=0:ffff7f000001:4dccde2a:58a5bc15:a0e15f, subordinatenodename=null, eis\_name=java:/jdbc/FluigDS > productName=MySQL productVersion=5.6.29 jndiName=java:/jdbc/FluigDS]))
15:33:48,655 ERROR [com.datasul.technology.webdesk.customization.ScriptingLog] (http-pool-threads - 96) DATASET\_SQL\_ERRO==============> java.sql.SQLException: javax.resource.ResourceException: IJ000457: Unchecked throwable in managedConnectionReconnected() cl=org.jboss.jca.core.connectionmanager.listener.TxConnectionListener@9b2f932[state=NORMAL managed connection=org.jboss.jca.adapters.jdbc.local.LocalManagedConnection@4ba0c9f1 connection handles=0 lastUse=1488566028654 trackByTx=false pool=org.jboss.jca.core.connectionmanager.pool.strategy.OnePool@292a1401 pool internal context=SemaphoreArrayListManagedConnectionPool@284062ed[pool=ProgressMGCAD] xaResource=LocalXAResourceImpl@1b1eca40[connectionListener=9b2f932 connectionManager=c6df2a4 warned=false currentXid=null productName=OpenEdge RDBMS productVersion=10.2B07 jndiName=java:/jdbc/ProgressMGCAD] txSync=null]]]>

# Causa

As bibliotecas (.jar) disponíveis estão desatualizadas.

# Solução

Remover as bibliotecas antigas na pasta [diretório\_instalação]\appserver\modules\com\progress\main e incluir as novas bibliotecas disponíveis .
