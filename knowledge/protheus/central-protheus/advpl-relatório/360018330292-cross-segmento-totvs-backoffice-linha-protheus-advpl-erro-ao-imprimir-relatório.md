---
article_id: 360018330292
category: ADVPL - Relatório
content_hash: 65dee8f2df90c1918e5778504e04500c6fd09190b682086301bc6d585c8b04ea
fetched_at: '2026-06-28T22:40:22.824379+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao imprimir
  relatório BIRT
type: support-article
updated_at: '2021-12-29T15:07:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018330292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-imprimir-relat%C3%B3rio-BIRT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min*** **Ocorrência**Erro ao imprimir Relatorio birt pelo menu![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013996611/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**Não foi configurado o [REPORTSERVICE] no appserver.ini  
  
**Solução**

É so segui as orientações da documentação abaixo, para configurar a seção REPORTSERVICE

[**BIRT | Instalação e Configuração**](http://tdn.totvs.com/pages/viewpage.action?pageId=175865862)

Exemplo:

ENABLED=1

REPORTENGINE=TOMCAT

WSURL=http://localhost:88/webservices/

WEBVIEWER=http://localhost:8080/WebViewer/

REPORTDATABASE=MSSQL

REPORTDATABASENAME=P12

REPORTDATABASEPORT=1433

REPORTDATABASESERVER=localhost

REPORTDATABASESCHEMA=DB2

REPORTDATABASEINSTANCE=teste

REPORTDATABASELOCALE=EN\_US.CP1252

REPORTWEBSERVERPATH=/
