---
article_id: 360029087532
category: ADVPL - Web Service
content_hash: 0961e239cecee532044bafdc05b934b6f5888c5ef254287f2ee6e62e26225946
fetched_at: '2026-06-28T22:40:10.317985+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Utilização de
  URLs diferentes por grupo de empresas
type: support-article
updated_at: '2022-07-27T14:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029087532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-de-URLs-diferentes-por-grupo-de-empresas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**É possível utilização de URLs diferentes para cada grupo de empresas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Para utilização de URLs diferentes por grupo de empresa, além de informar o TenantId no cabeçalho**,**você precisará criar duas instancias de URI no AppServer.ini.  
  
**Exemplo**

```
[HTTPURI]  
URL       = /REST/01  
PREPAREIN = 01,01  
INSTANCES = 1,2  
  
[HTTPURI2]  
URL       = /REST/02  
PREPAREIN = 02,01  
INSTANCES = 1,2
```

Desse modo quando precisar realizar requisições na empresa 01, irá utilizar a seguinte URI:

```
http://localhost:1285/REST/01
```

Para requisições na empresa 02, utilize a seguinte URI:

```
http://localhost:1285/REST/02
```

**Saiba mais**[02. REST com ERP Microsiga Protheus](http://tdn.totvs.com/display/framework/02.+REST+com+ERP+Microsiga+Protheus)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Abertura de ambiente em Web Service](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410465974167)
