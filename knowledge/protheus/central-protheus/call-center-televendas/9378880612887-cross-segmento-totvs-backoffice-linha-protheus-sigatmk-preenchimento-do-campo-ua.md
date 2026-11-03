---
article_id: 9378880612887
category: Call Center - Televendas
content_hash: 1aed7830d8d32058d3920314f445608868525c354bed3658c74e4e8277a41b28
fetched_at: '2026-06-28T22:41:30.207387+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Preenchimento
  do CAMPO UA_DTLIM
type: support-article
updated_at: '2022-11-01T16:49:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9378880612887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Preenchimento-do-CAMPO-UA-DTLIM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como é preenchido o campo **UA\_DTLIM**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**

Não há parametrização específica para o campo **UA\_DTLIM**, o que é  preciso fazer é a alteração do campo no grupo de atendimento, **U0\_VALIDAD**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9932157121175)  
  
Alterando este campo, ao inserir um orçamento ele informará **UA\_DTLIM** com a quantidade de dias que solicitou:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9932161602583)​  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9932181215639)​

Veja no exemplo que um orçamento incluso em 17.09.2020, com o campo U0\_VALIDAD igual a 3, resultou na validade do orçamento de 20.09.2020.
