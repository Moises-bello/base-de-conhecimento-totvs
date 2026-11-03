---
article_id: 25003537992471
category: eSocial - Gerar XML/ Integração Evento
content_hash: 69caecf628073075310c4f67aa728fa0b80fb4a1b5593ad74e3c20fe71549fe0
fetched_at: '2026-06-28T22:47:11.959007+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Ao integrar algum evento com o governo ocorre o erro
  de Schema The value 'IDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' has a length of '37';
  this differs from the allowed length of '36'
type: support-article
updated_at: '2026-06-15T12:30:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25003537992471-RH-RM-FOP-eSocial-Ao-integrar-algum-evento-com-o-governo-ocorre-o-erro-de-Schema-The-value-IDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-has-a-length-of-37-this-differs-from-the-allowed-length-of-36
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25003478065943) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao integrar algum evento com o governo ocorre o erro de Schema The value 'IDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' has a length of '37'; this differs from the allowed length of '36'  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões

**Causa**O erro ocorre pois no momento de gerar o XML, o campo ID é gerado com algum número, ou sequência indevida, gerando assim a rejeição pelo governo.  
  
**Solução**Para correção dessa ocorrência siga os passos abaixo  
1- Necessário regerar o XML e integrar novamente. Para isso, selecione o evento desejado, vá em **Processos | Gerar XML**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25003487643671)

2- Após integre com o TAF ou envie ao eSocial quando utilizar o Middleware.
