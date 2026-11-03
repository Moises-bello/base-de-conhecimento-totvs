---
article_id: 360051082714
category: ADVPL - Web Service
content_hash: 5f77604ca2f63bfbf002c733351c9157bc5fd4139316bf1b61b5d4e998817fe8
fetched_at: '2026-06-28T22:40:10.328844+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - WebServer:Retorno
  Protocolo HTTP
type: support-article
updated_at: '2021-05-06T19:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051082714-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-WebServer-Retorno-Protocolo-HTTP
---

**Dúvida**Quais as funções de retorno para Protocolo HTTP?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões

**Solução**Somente o **REST** possui uma função que permite informar o código **HTTP**, o **SOAP** permite informar uma mensagem de erro, e os demais casos, não há como informar.

*REST*    - **SetRestFault.***SOAP*   - **SetSoapFault**, não permite informar o código **HTTP**.  
*WEBEX* - Não existe nenhuma função.

**Saiba Mais**[SetRestFault](https://tdn.totvs.com/display/framework/SetRestFault)  
[SETSOAPFAULT](https://tdn.totvs.com/pages/releaseview.action?pageId=6814739)
