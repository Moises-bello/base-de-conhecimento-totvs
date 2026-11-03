---
article_id: 360062216533
category: ADVPL - Web Service
content_hash: f80d46b56baf3428a13ea828bf2f0ea5e4cb332db42b788cb7d62ecc215d27f1
fetched_at: '2026-06-28T22:40:10.474980+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - FwRest- (Host Não
  Encontrado)
type: support-article
updated_at: '2021-12-29T14:03:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062216533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-FwRest-Host-N%C3%A3o-Encontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao realizar um teste com a classe FWRest para consumir uma API está retornando (HOST NÃO ENCONTRADO)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL - A partir da versão 12  
  
**Solução**

Algumas ***apis***não retornam o código ***http***no retorno da requisição. Para estas ***apis***deve ser verificado o código ***http***diretamente para verificar se houve ou não erro. Para ligar este comportamento deve ser utilizado o método ***SetChkStatus(.F.)***.

A classe ***fwrest()*** só recupera os dados do Header e do Response quando não é um ***redirect().***

Nesse caso sugerimos a utilização da classe ***HttpPost()***.

**Saiba Mais**

[SetChkStatus](https://tdn.totvs.com/display/framework/FWRest%C2%A0)

[HttpGetStatus](https://tdn.totvs.com/display/tec/HTTPGetStatus)

[HttpPost](https://tdn.totvs.com/display/tec/HTTPPost)
