---
article_id: 360018290771
category: ADVPL - Classe e Função
content_hash: 040aee87fbbfd1a364fbb04065cf3abc6a41aa1a1ecbab548e442f5f32d4853c
fetched_at: '2026-06-28T22:40:16.666327+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: invalid classe
  twebchannel e twebengine'
type: support-article
updated_at: '2022-03-09T19:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018290771-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-invalid-classe-twebchannel-e-twebengine
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**  
Ao tentar utilizar as classes de comunicação mobile TWebChannel() ou TWebEngine() é exibido o seguinte erro no console do AppServer (*Application Server*):

```
invalid class TWEBCHANNEL on U_WEBENGINE(WEBENGINE.PRW)   
  
invalid class TWEBENGINE on U_WEBENGINE(WEBENGINE.PRW) 
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**O erro ocorre pois a classe ainda não esta disponível no binário atual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338191/mceclip0.png)  
  
**Solução**A classe está disponível apenas no **AppServer Lobo-Guará**, de 64 bits, a partir do release do Protheus 12.1.23.  
  
**Saiba mais**[TWEBENGINE](http://tdn.totvs.com/display/tec/TWebEngine)  
[TWEBCHANNEL](http://tdn.totvs.com/display/tec/TWebChannel)[Novo Binário: AppServer Lobo-Guará](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010698491-Novo-Bin%C3%A1rio-AppServer-Lobo-Guar%C3%A1-)
