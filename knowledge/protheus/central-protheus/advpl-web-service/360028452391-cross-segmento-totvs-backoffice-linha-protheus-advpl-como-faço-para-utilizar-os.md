---
article_id: 360028452391
category: ADVPL - Web Service
content_hash: e4cade55af473cff02c8069f7a644c7e66fb4ab5b0eeb433e2c947ef9cc013b8
fetched_at: '2026-06-28T22:40:10.193384+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Como faço para
  utilizar os web services do módulo de Gestão de Contratos
type: support-article
updated_at: '2021-05-06T17:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028452391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-fa%C3%A7o-para-utilizar-os-web-services-do-m%C3%B3dulo-de-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como faço para utilizar os *web services* do modulo de Gestão de Contratos (SIGAGCT)? **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.17  
  
**Solução**

1. Ter configurado um *web service* RESTFul:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028535091/mceclip0.png)
2. Acessar pelo navegador o endereço de IP (*Internet Protocol*) e porta configurado no serviço RESTFul seguindo do caminho (*path*) do serviço desejado:  
     
   Exemplo: [http://localhost:85/rest](http://localhost:85/rest/api/protheus/wscnta300/v1/contracts) + path da API  
   <http://localhost:85/rest/api/protheus/wscnta300/v1/contracts>
3. Validar o resultado pelo navegador (se o verbo for GET) ou ferramentas terceiras (ex: Postman, SoapUI e etc):![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028536992/mceclip1.png)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028536891/mceclip2.png)

**Saiba mais**[Lista de APIs - Referencelist](https://api.totvs.com.br/referencelist)

[Especificação de Serviços - Meus Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=384583453#Especifica%C3%A7%C3%A3odeServi%C3%A7os-MeusContratos-2.Objetivo)  
[Web Services REST/Server](http://tdn.totvs.com/pages/viewpage.action?pageId=185747842)
