---
article_id: 360018404851
category: ADVPL - Classe e Função
content_hash: ade1b43ec22b19f25612e0037f455de2ffe6ff4a90a7c3a8c30f87f063d86a7b
fetched_at: '2026-06-28T22:40:14.532020+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Cannot open the
  connection for the driver (BIRT)
type: support-article
updated_at: '2022-01-03T21:24:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018404851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cannot-open-the-connection-for-the-driver-BIRT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Após imprimir o relatório birt pelo menu ocorre o erro:  
**"**org.eclipse.birt.report.engine.api.EngineException: An exception occurred during processing. Please see the following message for details: Cannot open the connection for the driver: org.eclipse.birt.report.data.oda.jdbc.dbprofile. org.eclipse.datatools.connectivity.oda.OdaException ; com.microsoft.sqlserver.jdbc.SQLServerException:   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Pode ocorrer tanto pela configuração do appserver.INI o arquivo jdbc

Pode também ocorre o erro abaixo

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013681132/mceclip3.png)  
**Solução**

O erro questionado trata-se de uma informação dada pela aplicação java que tenta acesso ao banco de dados. No caso, é informada que é necessária a verificação de permissão de porta e conexão TCPIP utilizado no banco e porta apontada para conexão e o driver utilizado.

REPORTDATABASE deverá esta configurado corretamente no caso do SQL dever habilitar a porta correta pois esse é o motivo do erro.

REPORTDATABASEPORT caso esteja com a porta desabilitada ou incorreta gera o erro abaixo

```
com.microsoft.sqlserver.jdbc.SQLServerException: The TCP/IP connection to the host HOSTNAME, port 1433 has failed.  
  
Error: "Connection refused: connect. Verify the connection properties. Make sure that an instance of SQL Server is running on the host and accepting TCP/IP connections at the port.  
  
Make sure that TCP connections to the port are not blocked by a firewall
```

Verifique a seção REPORTSERVICE no appserve.ini a chave REPORTDATABASE, REPORTDATABASEPORT, REPORTJDBCDRIVER  atualize o JAVA e verifique se o driver está na pasta correspondente sqljdbc.jar e reinicie a maquina.

```
[REPORTSERVICE]  
  
REPORTDATABASE=MSSQL  
REPORTDATABASEPORT=1433  
  
REPORTJDBCDRIVER=C:\TOTVS\WebServer\server\webapps\WebViewer\drivers\sqljdbc4.jar
```

Para estabelece a comunicação na pasta WEB-INF "WebServer\server\webapps\WebViewer\WEB-INF" deverá conter usuario e sennha no arquivo seuambiente.properties

```
username=BIRT  
password=123456
```

**Saiba mais**[Possíveis problemas e soluções](http://tdn.totvs.com/pages/viewpage.action?pageId=271165836)  
[BIRT | Instalação e Configuração](http://tdn.totvs.com/pages/viewpage.action?pageId=175865862)
