---
article_id: 360027790991
category: Escrita Fiscal - Error.log
content_hash: 79f286c3121f59a95045ec8de441af47c6d1b6ff007327e992d4ac524017bbdf
fetched_at: '2026-06-28T22:39:32.851863+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - File is in EOF -
  c:\totvs12\data\protheus_data_ofc\system\sx6010.dtc in file D:\bamboo-agent-5.7.2\
  xml-data\build-dir\TP11-BUILDV2APPSRV-TEC11WIN32RPO32\advtec9_tt11\advpl\advplfile.cpp
  at line 65
type: support-article
updated_at: '2021-07-08T13:39:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027790991-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-File-is-in-EOF-c-totvs12-data-protheus-data-ofc-system-sx6010-dtc-in-file-D-bamboo-agent-5-7-2-xml-data-build-dir-TP11-BUILDV2APPSRV-TEC11WIN32RPO32-advtec9-tt11-advpl-advplfile-cpp-at-line-65
---

**Ocorrência**

Error log.

Update error - File is in EOF - c:\totvs12\data\protheus\_data\_ofc\system\sx6010.dtc in file D:\bamboo-agent-5.7.2\  
xml-data\build-dir\TP11-BUILDV2APPSRV-TEC11WIN32RPO32\advtec9\_tt11\advpl\advplfile.cpp at line 65  
 on GETNEXTIDX6(APLIB060.PRW) 23/10/2018 18:06:47 line : 1752  
  
[TOTVS build: 7.00.131227A-20180727 NG]  
Called from GETNEXTIDX6(APLIB060.PRW) 23/10/2018 18:06:47 line : 1752  
Called from GRAVALOG(APLIB060.PRW) 23/10/2018 18:06:47 line : 1436  
Called from RECLOCK(APLIB060.PRW) 23/10/2018 18:06:47 line : 509  
Called from GRAVATIT(FISXAPUR.PRX) 18/01/2019 10:22:05 line : 3032

**Ambiente**

P12.1.17  
  
**Solução**

Para a correção desse erro deverá ser excluído o índice (.cdx) da tabela SX6 em modo exclusivo e em seguida acessar novamente o sistema para recriar o arquivo.
