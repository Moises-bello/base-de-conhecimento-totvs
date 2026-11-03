---
article_id: 5246851038231
category: eSocial - Gerar XML/ Integração Evento
content_hash: de2645bc910e7310cab11c7a70f55b90fc591b8a2630bd6f4b387710e5d2dbea
fetched_at: '2026-06-28T22:47:13.027599+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Foi informado um valor com tamanho inválido no campo
  ID
type: support-article
updated_at: '2024-06-27T18:00:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5246851038231-RH-RM-FOP-eSocial-Foi-informado-um-valor-com-tamanho-inv%C3%A1lido-no-campo-ID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao integrar um evento o governo retorna com o erro **016 Foi informado um valor com tamanho inválido no campo ID**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre pois no momento de gerar o XML, o campo ID é gerado com algum número, ou sequência indevida, gerando assim a rejeição pelo governo.  
  
**Solução**Para correção dessa ocorrência siga os passos abaixo  
1- Necessário regerar o XML e integrar novamente. Para isso, selecione o evento desejado, vá em **Processos | Gerar XML**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5250348417943/mceclip1.png)

2- Após integre com o TAF ou envie ao eSocial quando utilizar o Middleware.
