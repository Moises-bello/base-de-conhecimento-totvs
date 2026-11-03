---
article_id: 360018126132
category: ADVPL - Relatório
content_hash: ba106bd00fdcdc1893793ba6a5f7247b0981848f8b9c49073a639a85833bf3b9
fetched_at: '2026-06-28T22:40:22.795384+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - E006_IO_ERROR:Falha
  durante operação de I/O (BIRT)
type: support-article
updated_at: '2021-12-29T14:59:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018126132-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-E006-IO-ERROR-Falha-durante-opera%C3%A7%C3%A3o-de-I-O-BIRT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**THREAD ERROR ([XXXX], XXXXXXXX, XXX) XX/XX/XXXX XX:XX:XX

E006\_IO\_ERROR:Falha durante operação de I/O. Oper: COPYFILE Cod: 430 on BIRTREPORT:PREPARE(BIRTREPORT.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**O Relatório Birt não encontrou o arquivo .rptdesign

O erro em questão ocorre porque a função **FILE** está retornando falso não encontrando o arquivo no endereço abaixo:

Veja no seu log o trecho conteúdo da variável **CRPTRUN**

Exemplo:

CRPTRUN(C):C:\Totvs\WebServer\server\webapps\WebViewer\webapps\webviewer\report\clientemdawmjiyru5wsvjptk1ftlq=20170927093938.rptdesign

**Solução**No caso relatado acima o caminho do relatório continha duas vezes as pastas "\webapps\webviewer\"

no appserve.ini na seção REPORTSERVICE modifique o caminho e valide o **[CATALINA\_HOME](http://tdn.totvs.com/pages/viewpage.action?pageId=175865862)**

```
[REPORTSERVICE]  
  
REPORTWEBSERVERPATH=/
```

![image2016-7-7 18:48:46.png](http://tdn.totvs.com/download/attachments/175865862/image2016-7-7%2018%3A48%3A46.png?version=1&modificationDate=1467928168000&api=v2)

**ATENÇÂO**

No Ambiente Linux todas as pastas envolvidas para configuração tanto do sistema **Protheus** como do **TOTVS WebViewer** deveram ser minúsculo.
