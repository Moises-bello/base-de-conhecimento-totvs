---
article_id: 360022891092
category: ADVPL - Relatório
content_hash: 3ad3f8f79215a43dec77cac320118ed55d14ef055bdb562ca76ef532a1a6176e
fetched_at: '2026-06-28T22:40:22.820961+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao imprimir
  relatório birt
type: support-article
updated_at: '2021-12-29T15:03:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022891092-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-imprimir-relat%C3%B3rio-birt
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:10:00 min  
  
Ocorrência**Erros ao imprimir relatório Birt.  
O erro indica de falta de espaço devido a configuração do Tomcat no TOTVS *Web Viewer.*   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020803911/mceclip0.png)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020804011/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**

Caso esteja usando o navegador ***Chrome**.* Feche-o e teste novamente.  
Persistindo pare o serviço do *webserver*, edite o arquivo

C:\TOTVS\WebServer\server\bin\setenv.bat e dobre os valores das chaves -Xms e -Xmx (abaixo destacado)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020804331/mceclip2.png)
