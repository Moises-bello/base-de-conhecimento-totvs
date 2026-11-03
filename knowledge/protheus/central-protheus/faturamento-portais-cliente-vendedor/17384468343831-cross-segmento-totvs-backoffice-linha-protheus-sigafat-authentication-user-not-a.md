---
article_id: 17384468343831
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: ec58ea3df4456f61048e930a07fe40a75bbfc6f13f19a302c60becdaa2478760
fetched_at: '2026-06-28T22:38:23.879163+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Authentication:
  user not authorized'
type: support-article
updated_at: '2023-09-08T20:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17384468343831-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Authentication-user-not-authorized
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17384465106327) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao inserir o usuário e senha do portal do vendedor, é gerado a mensagem: Authentication: user not authorized

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17384308034967)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da versão 12.  
  
**Solução**  
Desde a LIB Label 20201019, liberada em Outubro de 2020, o comportamento padrão de autenticação de WebServices SOAP e REST foi alterado.  
   
Para os Webservices e REST é necessário a atualização de forma de autenticação., com isso, a partir desta versão da lib,  se a chave **Security** não for informada no arquivo **Appserver.ini**, os serviços serão iniciados exigindo autenticação de usuário.  
   
Para que consiga autenticar o usuário é necessário usar a chave Security nos jobs do portal, configurado conforme abaixo:  
   
![](https://totvssuporte.zendesk.com/attachments/token/2yfghhqElDhRwmYdJpugQMR6Z/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/yzD1zXSEiGMcOXK9IO6OXaY7f/?name=image.png)  
 Sem essa configuração no server.ini, na configuração do Job, o sistema ficará emitindo que o usuário não está autorizado.

Saiba mais sobre portal do vendedor:

[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configuração-completa-do-portal-do-vendedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021311972-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-completa-do-portal-do-vendedor)

[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Portais-Cliente-Vendedor-Inclusão-de-pedido-no-portal-do-Vendedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406286940695-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Portais-Cliente-Vendedor-Inclus%C3%A3o-de-pedido-no-portal-do-Vendedor)
