---
article_id: 360043030834
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c49b2a620d71327ad2a3e83bf8fa5fc0d4ba36cf83d2fbf1f06a8b9ae502b400
fetched_at: '2026-06-28T22:39:56.283515+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Aguardando
  Montagem de Lote e Assinatura (STATUS = 1)
type: support-article
updated_at: '2025-06-10T18:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043030834-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Aguardando-Montagem-de-Lote-e-Assinatura-STATUS-1
---

**Dúvida**Qual procedimento realizar quando a nota não sai do status 1**- Aguardando Montagem de Lote e Assinatura**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse problema geralmente ocorre quando a nota não foi processada corretamente pelo TSS.

Um exemplo bem comum é quando a nota foi transmitida no momento que os JOBS estavam parados/comentados no Appserver.ini, geralmente por ter sido aplicado um patch, o qual necessita que sejam parados os JOBS para ter exclusividade. Exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058066994/mceclip1.png)  
  
Sendo assim, caso estejam comentados, favor 'descomentar' a sessão e monitorar a nota. Por padrão ela deverá sair do STATUS = 1 e continuar o processamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058953713/mceclip0.png)
