---
article_id: 9358673759127
category: PMS - Dúvidas Gerais
content_hash: 53601d93acd82c505b126b6b2fdb378715c5c794fce653296ef5e0acae18c99a
fetched_at: '2026-06-28T22:37:17.755166+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Calculo de horas (AFU_HQUANT)
  no apontamento do recurso
type: support-article
updated_at: '2024-03-21T14:09:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9358673759127-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Calculo-de-horas-AFU-HQUANT-no-apontamento-do-recurso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22237438930327) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como funciona o calculo de horas (AFU\_HQUANT) apontamento do recurso?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

O cálculo de horas para apontamento de recurso (AFU\_HQUANT) é feito com base no calendário do projeto/tarefa e o do próprio recurso, sendo que somente serão computadas as horas onde ambos os calendários permitem o apontamento. Exemplo:

* Calendário do Projeto:

![Calend_rio_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9358454907927)

Esse calendário permite apontamentos de segunda a sexta das 08:00 as 12:00 hs e das 13:00 as 17:00 hs.

* Calendário do Recurso:

![Calend_rio_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9358455418391)

Esse calendário permite apontamentos de segunda a sexta das 06:00 as 12:00 hs.

Com estes calendários se o usuário for designado no projeto e no momento de realizar o apontamento for informado o horário de início como 00:00 e fim como 23:59 será calculado um total de 4 horas para o apontamento.

![Apontamento.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9358569645975)

Este valor é composto pelo intervalo das 08:00 as 12:00 hs que esta valido em ambos os calendários.

**Saiba mais**: [**PMS0037 - Gerenciamento de Apontamento**](https://tdn.totvs.com/x/BY3vI)
