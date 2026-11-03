---
article_id: 360058322574
category: BI - Business- Intelligence - Workflow
content_hash: fce40667f7e90dfc05d1e51ab906071cc756ce0d680142c37c72e6e2a88eba5e
fetched_at: '2026-06-28T22:37:02.972233+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Campo WFA_Tipo do Workflow
type: support-article
updated_at: '2022-05-13T17:48:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058322574-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Campo-WFA-Tipo-do-Workflow
---

**Dúvida**Quais os possíveis conteúdos do campo WFA\_TIPO?  
  
**Ambiente**MP – WF – A partir da versão 11.80  
  
**Solução**A tabela WFA é utilizada para guardar informações dos processos de envio de e-mails do workflow. O campo WFA\_TIPO é definido da seguinte maneira: 

**0: Email está sendo processado**  
**1: Email está na caixa de entrada (pasta INBOX)**  
**2: Email está na caixa de saída (pasta OUTBOX)**  
**3: Email está na foi enviado (pasta SENT)**  
**4: Email foi arquivado (pasta ARCHIVE)**  
**5: Email enviado com erro (pasta OUTBOX/ERROR)**  
**6: Email recebido com erro (pasta INBOX/ERROR)**  
**7: Email ignorado (pasta IGNORED)**  
**8: Email de workflow via-link enviado**
