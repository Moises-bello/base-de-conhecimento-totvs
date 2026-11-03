---
article_id: 360000185427
category: ADVPL - Web Service
content_hash: 97773547bd5c324ed648e4661c7bb709d54a0036d3031081bafeed7335cccf61
fetched_at: '2026-06-28T22:40:10.196151+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Comportamento
  error.log thread webservice
type: support-article
updated_at: '2023-04-30T19:43:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000185427-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Comportamento-error-log-thread-webservice
---

**Dúvida**Qual o comportamento error.log thread WS, ao apresentar internal server erro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Ao ocorrer algum tipo de INTERNAL SERVER ERRO gerado a partir de uma thread de WS o conteúdo de error.log não será mais retornado e uma mensagem padrão de erro será retornada ao client.   
As mensagens de error.log contém informações internas do server (INTERNAL SERVER ERRO) que ao serem retornadas ficam expostas ao client.   
Tratativa realizada por conta das recomendações oWasp.  
  
**Saiba mais**  
<http://tdn.totvs.com/display/PROT/ADV0001_WebService_INTERNAL_SERVER_ERRO>
