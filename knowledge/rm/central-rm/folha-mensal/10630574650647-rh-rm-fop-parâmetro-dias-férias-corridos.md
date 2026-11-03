---
article_id: 10630574650647
category: Folha Mensal
content_hash: 14e5036974026a587b11fcc028206945b9511117f16f74aa494cca50782a3ddc
fetched_at: '2026-06-28T22:46:58.288976+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Parâmetro: Dias Férias Corridos'
type: support-article
updated_at: '2024-09-16T18:57:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10630574650647-RH-RM-FOP-Par%C3%A2metro-Dias-F%C3%A9rias-Corridos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:46 min****Dúvida**Cadastro de férias conta mais dias do que o informado no campo **Dias de férias**, data fim fica impossibilitada de alterar e o campo **Dias férias corridos** aparece com mais dias do que o informado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, é necessário entender o campo **Somente Dias Uteis** que fica no caminho: **Cadastro do funcionário | parâmetros | somente dias uteis.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10630106027799)

Ao marcar esse campo o sistema entende que esse funcionário utilizará apenas dias uteis para o cálculo das férias, sendo assim ignora os sábados domingos e feriados para o cadastro das férias.  
  
Por exemplo, vou cadastrar 30 dias de férias para um funcionário, com data início 01/05, o sistema vai se comportar da seguinte forma com o parâmetro marcado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10630251837975)

Com o parâmetro desmarcado ficará assim:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10630308518423)
