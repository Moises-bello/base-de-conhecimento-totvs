---
article_id: 4408794341271
category: PMS - Dúvidas Gerais
content_hash: 5979bcc8c4902b398e463c1decd6e17fe6829dc1c25889ef0204a6beb81953fa
fetched_at: '2026-06-28T22:37:17.627223+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Como funciona o Calculo de
  Custos sobre o campo "AFA_ACUMUL" da rotina PMSA410
type: support-article
updated_at: '2024-02-23T12:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408794341271-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Como-funciona-o-Calculo-de-Custos-sobre-o-campo-AFA-ACUMUL-da-rotina-PMSA410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563604500759) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**  
Como utilizar o calculo de custos do campo "**AFA\_ACUMUL**" da rotina PMSA410.

Este campo retorna os custos previstos do Recurso ou Produto, o AFA\_ACUMUL está presente nas duas abas da tarefa Produtos e Aloc. Recursos. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408793902615)

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**

O campo **Calc. Custo** define o método de apropriação do custo para o produto.

As opções são as seguintes:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408794248727)

* **1- 50/50:** o sistema prevê que a apropriação será feita 50% no início previsto da tarefa e 50% na data final prevista para a tarefa.
* **2- 0/100:** o sistema prevê o 100% da apropriação do custo na data final prevista para tarefa.
* **3- Rateado:** método no qual os custos serão distribuídos durante a execução da tarefa. O sistema prevê a apropriação de custos rateando este o progresso físico previsto da tarefa.
* **4- Necessidade:** a apropriação é feita na data de necessidade do produto (isto é definido uma vez que seja estabelecida a data de início e fim da tarefa). Geralmente utilizado em tarefas de longa duração.  
  ***Recalc. Custo**: se informado SIM, o custo será atualizado quando for executada a rotina de reajuste de custos, se NÃO o custo só poderá ser modificado manualmente.*
* **5- Apropriação:** A apropriação realiza o custo do produto, recursos  empregados na tarefa do projeto.
* **6- Rateio Aprop:**Rateio com apropriação, realiza o custo da apuração dos serviços executados considerando os gastos específicos de materiais ou recursos. ( Valida o campo AFA\_DTAPRO). Realiza uma divisão de custos proporcional, levando em consideração de acordo com a execução do projeto.
* **7 - Cron. Consumo:**  Considera o custo do que foi realizado no dia, ou seja, o valor que não está acumulado (inicial e final do projeto).

\* Ponto de entrada que pode ser utilizado no custo **PMSXCUSPRV - Custo previsto do projeto.**

**Saiba mais: <https://tdn.totvs.com/x/frBn>**

\* Campos onde são gravados os custos do projeto: **<https://tdn.totvs.com/x/yr0IHw>**

\* Parâmetro que pode influenciar no calculo do custo **MV\_PMSCUST** (Indica se utiliza o custo pela quantidade unitária ou total)
