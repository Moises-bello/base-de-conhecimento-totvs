---
article_id: 360021027631
category: ADVPL - Rotina Automática
content_hash: fc03c1dbea4b5396832e4c11f137cb719fad8233dc0a0545e89d63ed813bc0f1
fetched_at: '2026-06-28T22:40:25.073711+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização de Reserva
  na Rotina Loja701 utilizando Reserva
type: support-article
updated_at: '2022-06-21T17:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021027631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-de-Reserva-na-Rotina-Loja701-utilizando-Reserva
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Estou desenvolvendo uma integração, onde vamos utilizar o ExecAuto LOJA701.  
Estou com uma dúvida referente à reserva. Estou fazendo conforme descrito no conteúdo do link [http://tdn.totvs.com/pages/releaseview.action?pageId=6787264 ,](http://tdn.totvs.com/pages/releaseview.action?pageId=6787264)porém a reserva não está sendo realizada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para que seja feita a reserva automática, deve ser passado o campo"AUTRESERVA" no array de cabeçalho informando o código da Loja (Campo SLJ->LJ\_CODIGO) que deseja efetuar a reserva e, no array de itens deve ser passado o campo LR\_ENTREGA = 3 informando assim que este item deve ser realizada a reserva automática.  
  
**Saiba mais**  
[SIGALOJA\_LOJA701](SIGALOJA%200017%20Como%20utilizar%20a%20rotina%20LOJA701%20por%20meio%20de%20ExecAuto?)
