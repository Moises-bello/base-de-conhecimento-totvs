---
article_id: 360019921072
category: ADVPL - Rotina Automática
content_hash: d3959fe1ddf6c48ac26e626666590bf90674d351e9a2bc72ac3662f7bf7a2ff9
fetched_at: '2026-06-28T22:40:23.961704+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Customização WS  REST
  utilizando a rotina automática  A430RESERV
type: support-article
updated_at: '2021-12-29T13:57:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019921072-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Customiza%C3%A7%C3%A3o-WS-REST-utilizando-a-rotina-autom%C3%A1tica-A430RESERV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Estamos desenvolvendo uma customização WS  REST utilizando a rotina automática   
A430RESERV. Porem parece estar deixando o registro preso no SB2

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**A rotina MATA500 não está preparada para REST, mas está em MVC e poderia publicar o serviço REST utilizando [FWRestModel](http://tdn.totvs.com/display/PROT/FWRestModel+-+API+RESTful+dos+modelos+de+dados+do+Protheus)
