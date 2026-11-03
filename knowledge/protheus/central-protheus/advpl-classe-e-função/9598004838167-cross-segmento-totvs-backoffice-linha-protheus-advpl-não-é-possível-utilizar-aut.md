---
article_id: 9598004838167
category: ADVPL - Classe e Função
content_hash: 6665c6c4737d78c5f9e576680f6032a2988f91c6ae047065d3ba1fd415159222
fetched_at: '2026-06-28T22:40:20.764802+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Não é possível utilizar
  autenticação OAuth2 com as classes TMailManager e TMailMng?
type: support-article
updated_at: '2022-12-23T20:14:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9598004838167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-N%C3%A3o-%C3%A9-poss%C3%ADvel-utilizar-autentica%C3%A7%C3%A3o-OAuth2-com-as-classes-TMailManager-e-TMailMng
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Não é possível utilizar autenticação OAuth2 com as classes **TMailManager** e **TMailMng**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 12.1.33  
  
**Solução**Foi Implementado na classe **TMailManager** o método **SetOAuthToken**, que define o token **OAuth2** que será utilizado para os protocolos IMAP, POP e SMTP, e implementada na classe **TMailMng** a propriedade **cOAuthToken**, que permitirá definir e ler o token **OAuth2** que será utilizado. Sendo necessário a atualização do binário para versão 20.3.0.14.  
  
**Saiba mais**<https://tdn.totvs.com/display/tec/Application+Server+-+E-mail+-+Office+365>   
[Application Server - 20.3.0.14](https://tdn.totvs.com/display/tec/Application+Server+-+20.3.0.14)
