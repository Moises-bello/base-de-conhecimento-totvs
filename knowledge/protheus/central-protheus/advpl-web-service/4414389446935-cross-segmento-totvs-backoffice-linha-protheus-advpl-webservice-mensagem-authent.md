---
article_id: 4414389446935
category: ADVPL - Web Service
content_hash: 8910ffc12a8484e72842b5115f4efefb6978c026f7e364b0da12e22861077d0d
fetched_at: '2026-06-28T22:40:10.550601+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- WebService mensagem
  Authentication: User not authorized'
type: support-article
updated_at: '2025-12-01T19:12:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414389446935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-WebService-mensagem-Authentication-User-not-authorized
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29275831257751) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao tentar se conectar ao WebService é apresentado a mensagem:***Authentication: User not authorized***.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Versão 12.1.2410  
  
**Solução**  
A partir da release 12.1.2410 do Protheus, o comportamento padrão de autenticação de WebServices **SOAP** e **REST** será alterado, a chave ***Security***estará ligada por padrão sem a possibilidade de ser desligada, reforçando assim a segurança do sistema; desta forma será exigida autenticação para acessar os dados do seu ambiente.

**Saiba mais**  
[Alteração de Comportamento - Autenticação SOAP e REST](https://tdn.totvs.com/pages/viewpage.action?pageId=539697514)

[12.1.2410 - Autenticação Soap e Rest](https://tdn.totvs.com/display/public/framework/DFRM1-35680+DT+Bloqueio+de+REST+e+SOAP+sem+security)
