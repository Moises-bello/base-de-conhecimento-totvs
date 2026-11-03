---
article_id: 11328527907607
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: ccea6dc32ab3e2cd5a692947f52542130ffbd59bcc3c4d8b3cf40a3e64631dd5
fetched_at: '2026-06-28T22:39:56.232874+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - E090 - Número do
  RPS Inválido (Brasília)
type: support-article
updated_at: '2025-06-02T12:08:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11328527907607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-E090-N%C3%BAmero-do-RPS-Inv%C3%A1lido-Bras%C3%ADlia
---

**Ocorrência**Como deve ser corrigida a rejeição E090 - Número do RPS Inválido?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11328523176471)  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre por conta do provedor utilizado por Brasília/DF controlar o sequencial de númeração do RPS.  
  
**Solução**O provedor consiste em números de RPS que **devem primeiro ser solicitados através do portal** no seguinte caminho **“Solicitação de Documentos Fiscais” -> “ Solicitação”**, nesta opção serão gerados números de RPS a serem consumidos, exemplo de 1 a 50.  
  
Após isso, com base nas numerações disponibilizadas pela prefeitura, deverão ser utilizadas no Protheus.
