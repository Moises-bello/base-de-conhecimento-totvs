---
article_id: 360044977834
category: ADVPL - Web Service
content_hash: a2a9f9f5465e4b4e679c06aa8fd8d7d231c2549cd50eaadeffdae616e108a7f3
fetched_at: '2026-06-28T22:40:10.504837+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Response WebService
  soap https
type: support-article
updated_at: '2022-09-06T18:48:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044977834-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Response-WebService-soap-https
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como alterar o response que esta em **HTTP** para **HTTPS**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12  
  
**Solução**A Informação ***soap:Envelope***indica o endereço da definição do pacote **SOAP** utilizado e este endereço é um endereço **HTTP**.

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
```

Já o **HTTP** da resposta segue a definição do **NameSpace** configurado no **WS** do **Protheus**, e não a configuração https do Server.   
Para alterar o protocolo da resposta, utilize o **NameSpace**, indica onde o serviço será publicado.

```
Exemplo:  
WSSERVICE NameService DESCRIPTION "ADVPL - Serviço TESTE" NameSpace "https://www.totvs.com/"
```

**Response HTTP**![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063070413/unnamed.png)  
**Response HTTPS**  
![unnamed__1_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063070393/unnamed__1_.png)

O **NameSpace** na lista de serviços é definido na configuração do *Job* do Webservice que responde ao **WS** na chave  **NameSpace**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8688657738391/mceclip1.png)

**Exemplo**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8688599451799/mceclip0.png)

**Saiba Mais**[Webservice](https://tdn.totvs.com/display/tec/WSSERVICE)
