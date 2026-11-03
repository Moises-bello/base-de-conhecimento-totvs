---
article_id: 360060652994
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a3ed6bbb19e59006918a590f7b03270017c21352c96d958b387b560a7365a531
fetched_at: '2026-06-28T22:39:58.681174+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFTS - Na tela de
  transmissão de cancelamento não mostra a operação para ser transmitida
type: support-article
updated_at: '2021-10-06T18:45:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060652994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFTS-Na-tela-de-transmiss%C3%A3o-de-cancelamento-n%C3%A3o-mostra-a-opera%C3%A7%C3%A3o-para-ser-transmitida
---

**Dúvida**Na tela de transmissão de cancelamento não mostra a operação para ser transmitida.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**A operação só aparece no grid se os campos abaixo estiverem preenchidos:  
F3\_CODRSEF = S ,  F3\_CODRET = 111 e F3\_DTACANC preenchido com a data de cancelamento.
