---
article_id: 360027918491
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3e6aafca3de8ab9bf520a10ad61492d005f5453f8084552413b4fec43d543421
fetched_at: '2026-06-28T22:39:58.428570+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  335 - DSFNET - Número do RPS deve ser subsequente ao anterior enviado
type: support-article
updated_at: '2025-06-25T21:02:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027918491-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-335-DSFNET-N%C3%BAmero-do-RPS-deve-ser-subsequente-ao-anterior-enviado
---

**Ocorrência**Ao realizar transmissão para municípios do provedor DSFNET é apresentada a seguinte rejeição: 335 - Número do RPS deve ser subsequente ao anterior enviado. Foi enviado o RPS 210, deve ser enviado o RPS 209.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre pelo fato de municípios que utilizam o provedor DSFNET possuir um controle da numeração de RPS enviada.  
  
**Solução**  
Para solucionar essa ocorrência deverá utilizar a numeração do RPS que a própria rejeição cita, exemplo:  
  
*Número do RPS deve ser subsequente ao anterior enviado. Foi enviado o RPS 210, deve ser enviado o RPS 209.*  
  
Ou seja, foi enviado o RPS 210, porém o prefeitura está esperando a RPS 209.
