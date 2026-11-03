---
article_id: 360029827433
category: ADVPL - Classe e Função
content_hash: abb2d8800bd671574b02e929c3ea1f67edc32a735f024bb4abc2928dcc8d7507
fetched_at: '2026-06-28T22:40:20.476488+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Invalid Class TAMQP
type: support-article
updated_at: '2022-01-11T21:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029827433-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Invalid-Class-TAMQP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao tentar utilizar as classes de comunicação tAMQP do tipo AMQP, gera o erro abaixo:

```
invalid class TAMQP on U__SENDER(TAMQP.PRW)
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Causa**O erro ocorre pois a classe ainda não esta disponível no binário atual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338191/mceclip0.png)  
  
**Solução**A classe está disponível apenas no **AppServer Lobo-Guará**, de 64 bits, a partir do release do Protheus 12.1.23.  
  
**Saiba mais**[tAMQP](http://tdn.totvs.com/display/tec/tAMQP)
