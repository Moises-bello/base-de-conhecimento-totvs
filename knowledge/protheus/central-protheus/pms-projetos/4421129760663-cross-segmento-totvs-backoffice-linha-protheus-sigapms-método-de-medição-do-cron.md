---
article_id: 4421129760663
category: PMS - Projetos
content_hash: f26bd067ba0997cfc94cb7241313dd202f46930d6ff480627276090bc07524a4
fetched_at: '2026-06-28T22:37:15.122927+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Método de Medição
  do Cronograma
type: support-article
updated_at: '2022-02-02T14:40:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421129760663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-M%C3%A9todo-de-Medi%C3%A7%C3%A3o-do-Cronograma
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Qual a finalidade do Método de Medição do Cronograma?

![medicao.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421129615895/medicao.png)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as Versões

**Solução**

Método utilizado pelo sistema utilizado para calcular o progresso físico previsto da tarefa;

**1-0/100** : técnica utilizada em tarefas de curta duração. O sistema prevê o 100% do progresso físico   
na data final prevista da tarefa.  
**2-20/80** Técnica utilizada em tarefas de curta duração. O sistema prevê 20% de progresso na data   
prevista para o início e o 80% restante do progresso físico na data final prevista para a tarefa.  
**3-Eventos :** Técnica dos eventos-marco (milestones) é recomendada em tarefas discretas e de longa   
duração. Na tarefa devem ser informados os eventos marco e suas datas com o percentual previsto   
de execução para a data do evento. No caso de não existirem os eventos cadastrados, o sistema irá   
utilizar o método proporcional ao tempo.  
**4-Proporcional ao tempo** : técnica utilizada em tarefas de longa duração. O sistema calcula o   
progresso físico previsto de acordo com o calendário e a duração da tarefa.  
**5-Proporcional ao Custo** : Técnica utilizada em tarefas de longa duração. O sistema calcula o   
progresso físico previsto de acordo com o custo previsto ao longo da tarefa.  
Exemplo de medição:  
Para exemplificar, utilizaremos uma tarefa com as seguintes características :

5. Início dia 01/08 (sexta feira) fim 08/08 (sexta feira)  
6. Calendário de segunda a sexta feira  
7. Consumo de custo previsto:   
a. 40% no primeiro dia (materiais)  
b. 60% rateado 10% em cada dia (mão-de-obra)  
8. Eventos marco:  
a. Finalização de X, no dia 04/08, 30%  
b. Finalização de Y no dia 07/08, 70%  
c. Finalização da tarefa no dia 08/08, 100%  
Tabela de progresso físico previsto segundo cada tipo de medição (os percentuais são sempre referentes   
ao total da tarefa)

**![tipos_de_med.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421137220759/tipos_de_med.png)**

**Saiba mais em : [Cronograma do Projeto](https://tdn.totvs.com/x/Q6rxF)**
