---
article_id: 360019498011
category: NFe - Nota Fiscal Eletrônica
content_hash: 7a95c1c3645331afd975d844c49bb147b70c5966412821b7ac217c09f5ea884d
fetched_at: '2026-06-28T22:40:01.634625+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como corrigir
  a mensagem de motivo de cancelamento?'
type: support-article
updated_at: '2021-10-11T18:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019498011--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-corrigir-a-mensagem-de-motivo-de-cancelamento
---

**Dúvida**Como corrigir a mensagem de motivo de cancelamento na transmissão da nota?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para correção basta consultar essas notas que pedem o motivo de cancelamento em **Monitor >> Faixa >> Mensagens.**  
  
Assim, será gravado o retorno dessa nota no campo **F3\_CODRSEF** na tabela SF3.

Código **100** caso a nota esteja autorizada na SEFAZ

Código **101** caso a nota esteja cancelada na SEFAZ

Código **102** caso a nota esteja inutilizada na SEFAZ  
  
Com o código correto no campo não irá mais solicitar o motivo do cancelamento.

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015182031/Capturar.JPG)
