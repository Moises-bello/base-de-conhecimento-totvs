---
article_id: 360015175151
category: Administração de Pessoal
content_hash: 1f8f35eb3ee6c9a8fe7911233e8898e85ca8f9b71964c8723f26dec5dfcb758b
fetched_at: '2026-06-28T22:47:02.338211+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Discriminar eventos de diferença no envelope
type: support-article
updated_at: '2024-09-16T18:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015175151-RH-RM-FOP-Discriminar-eventos-de-diferen%C3%A7a-no-envelope
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17267552180759)Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como discriminar eventos de diferença no envelope?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Realize os seguintes passos do exemplo abaixo para criar os eventos que serão discriminados na diferença:   
  
1. Acesse: **Administração de Pessoal | Eventos | Eventos** e incluir um evento de diferença salarial para o evento de Horas Extras. Para este exemplo foi criado o evento **0500** **Dif. Hora Extra 100%.** O evento de diferença terá as mesmas incidências do evento de **Hora Extras 100%**. As únicas diferenças serão o código e a descrição. Veja:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17267558538007)  
  
2. Acesse o cadastro do evento **0083 Hora Extra 100%** e no campo **Evento de Diferença de Salário** informe o evento de diferença criado no passo 1.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12627504452247)  
  
3. Após parametrizar os eventos dos passos 1 e 2, acesse: **Folha Mensal | Lançamentos | Diferença Salarial** e execute o cálculo da **Diferença Salarial**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10261891351831)  
  
4. No envelope do funcionário o evento será discriminado. Veja abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010073231)  
  
**Importante**Os procedimentos deste artigo podem ser aplicados igualmente a outros eventos com possuam diferenças.  
  
**Saiba Mais**[RH - RM - FOP - Diferença salarial por dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008178291-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio)
