---
article_id: 6517280481047
category: PMS - Dúvidas Gerais
content_hash: 38fad7fbdb8b52af6b833ef1a15e10e11d7853eded1e2f3725994b2922637406
fetched_at: '2026-06-28T22:37:17.740418+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Sistema não está
  calculando horas de apontamento
type: support-article
updated_at: '2022-06-03T12:38:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6517280481047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Sistema-n%C3%A3o-est%C3%A1-calculando-horas-de-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Sistema não está calculando horas de apontamento   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS- Todas as versões  
  
**Solução**

Vamos pontuar alguns cadastros que devem ser verificados para que o apontamento seja realizado:

***1.a*****- *Projeto***- Verificar se o projeto não está com as datas de início e fim estão dentro do período.

***1.b* - *Projeto***- Verificar o calendário utilizado, este calendário dever prever todos os horários que os apontamentos deveram ocorrer, inclusive finais de semana e horários depois do expediente.

***2.a* - *Tarefa***- Verificar o calendário das tarefas, caso ocorra alteração no calendário do projeto e já existir tarefas, verificar se o calendário atende a necessidade dos apontamentos.

***2.b* - *Tarefa***- Verificar as datas de início e fim da tarefa, pois caso o apontamento seja realizado após o vencimento da tarefa esse apontamento não vai calcular a quantidade de horas.

***3.a* - *Recurso*** - Verificar o calendário do recurso, os horários do recurso devem estar equalizados com o calendário do projeto. Caso o calendário do recurso esteja configurado para apontamentos em horário comercial, caso seja realizado apontamentos em finais de semana ou fora do horário comercial as horas não serão computadas. Conforme descrito acima verificar se o calendário do projeto e tarefa estão compatíveis com o calendário do recurso.

***4.a* - *Atualização*** - \*\* Verificar se o rpo que está sendo utilizado o Web Service também foi atualizado, pois como alguns clientes utilizam um outro rpo para o webservice e outro para o portal e outro para o sistema, pode ocorrer que uma patch seja aplicada somente no rpo do sistema deixando o rpo do portal e do webservice sem a devida correção.

Temos material de apoio que pode ser acessado por estes links:

[<https://tdn.totvs.com/pages/releaseview.action?pageId=351382843>]

[<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050196333-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Gerenciamento-de-Apontamento>]

[<https://tdn.totvs.com/pages/releaseview.action?pageId=351382843>]
