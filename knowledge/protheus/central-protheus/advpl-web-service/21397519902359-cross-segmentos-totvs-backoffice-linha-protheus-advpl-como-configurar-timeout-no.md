---
article_id: 21397519902359
category: ADVPL - Web Service
content_hash: 20f02aa237bd9a75fd1e574795ca3a8302ba134c41263cc8a22752332aa42c22
fetched_at: '2026-06-28T22:40:10.576374+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como configurar
  timeout no Rest?
type: support-article
updated_at: '2024-02-16T13:05:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21397519902359-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-configurar-timeout-no-Rest
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21397513848855) Tempo aproximado para leitura: **00****:01:00 min**

**Dúvida**Como configurar timeout no Rest?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Deve se verificar se o Time-Out ocorre no consumo da api ou na própria API na qual está sendo consumida.

No consumo:

TimeOut em serviços o qual serão consumidos, dentro da classe FwRest, utilize o comando abaixo:

```
oRestClient:nTimeOut := 1200 //valor em segundos
```

Fornecedor da API:

Caso seja na API, essa configuração é de responsabilidade do fornecedor da API, e se for no consumo deve verificar aonde altera o parâmetro de tempo de resposta do endpoint.

Ou se for seu próprio serviço Rest existe a configuração abaixo no arquivo appserver.ini

```
[HTTPV11]   
Enable=1 
AddressFamily=1 
Sockets=HTTPREST
TimeOut=60000 ; equivale a 1 minuto.
```

**Saiba mais**

[FwRest](https://tdn.totvs.com/display/public/framework/FWRest)

[Configuração Rest](https://tdn.totvs.com/pages/releaseview.action?pageId=435098014)
