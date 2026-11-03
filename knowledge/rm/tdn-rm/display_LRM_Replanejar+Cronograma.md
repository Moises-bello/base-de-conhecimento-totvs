---
content_hash: 1cfee179f356adb60cfc40b66d891028987916833630f609ee921c097a30e5dd
fetched_at: '2026-06-29T00:09:16.740664+00:00'
page_id: '421385542'
product: rm
source: tdn-rm
title: Replanejar Cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Replanejar+Cronograma
version: 5
---

---

O processo de Replanejar Cronograma ocorre a partir da planilha de atividades sem a necessidade de exportar os valores do pert.

É possível realizar a execução do processo para uma ou mais tarefas. No entanto, quando o processo de replanejamento é disparado, o SOLUM obtém a grandeza base verificando a maioria dentre as tarefas selecionadas. Por exemplo: Em uma Obra com três tarefas, duas de grandeza PERCENTUAL e uma de grandeza QUANTIDADE, a grandeza base será PERCENTUAL.

Com base nisso, independente do número de tarefas selecionadas, ao solicitar o replanejamento, o SOLUM sempre irá verificar se a tarefa em questão possui grandeza diferente da grandeza base. Caso afirmativo, o SOLUM emitirá um alerta informando que tal tarefa possui grandeza diferente e não poderá ser replanejada.

Caso não haja nenhuma grandeza cadastrada, a grandeza base será PERCENTUAL.

Para que uma tarefa possa ser replanejada, deverá estar obrigatoriamente 100% planejada.

Caso o replanejamento ultrapasse os períodos da atividade, a data fim programada da atividade será atualizada para a data fim do próximo período do cronograma.

É aconselhável efetuar o cálculo do cronograma após este processo.

**Observação:**

Períodos que não são passiveis de alteração não serão re-planejados. Os períodos passiveis de alteração são configurados nos 

O replanejamento do cronograma será feito de acordo com a fórmula:

**NVP = VPP + ((VPL - VRL) \* (VPP / VPF))**

NVP: Novo Valor Planejado (Valor Replanejado)

VPL: Valor Planejado no Período Lançado

VRL: Valor Realizado Lançado

VPP: Valor Planejado no Período

VPF: Valores Planejados Futuros (períodos posteriores ao lançado)

Exemplos:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 10,0 | 10,0 | 60,0 | 20,0 | valor lançado |
| Realizado | 10,0 |  |  |  | valor replanejado |
| Replanejado | 10,0 | 10,0 | 60,0 | 20,0 |  |

   
P1 = Recebe o valor real lançado = 10  
P2 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 10 + ((10 - 10) \* (10 / 90)) = 10 + 0 = 10  
P3 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 60 + ((10 - 10) \* (60 / 90)) = 60 + 0 = 60  
P4 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 20 + ((10 - 10) \* (20 / 90)) = 20 + 0 = 20  
 

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 10,0 | 10,0 | 60,0 | 20,0 | valor lançado |
| Realizado | 1,0 |  |  |  | valor replanejado |
| Replanejado | 1,0 | 11,0 | 66,0 | 22,0 |  |

   
P1 = Recebe o valor real lançado = 1  
P2 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 10 + ((10 - 1) \* (10 / 90)) = 10 + 1 = 11  
P3 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 60 + ((10 - 1) \* (60 / 90)) = 60 + 6 = 60  
P4 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 20 + ((10 - 1) \* (20 / 90)) = 20 + 2 = 22  
 

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 10,0 | 10,0 | 60,0 | 20,0 | valor lançado |
| Realizado | 19,0 |  |  |  | valor replanejado |
| Replanejado | 19,0 | 9,0 | 54,0 | 18,0 |  |

   
P1 = Recebe o valor real lançado = 19  
P2 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 10 + ((10 - 19) \* (10 / 90)) = 10 + (-1) = 9  
P3 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 60 + ((10 - 19) \* (60 / 90)) = 60 + (-6) = 54  
P4 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 20 + ((10 - 19) \* (20 / 90)) = 20 + (-2) = 18  
 

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 19,0 | 9,0 | 54,0 | 18,0 | valor lançado |
| Realizado | 19,0 | 5,0 |  |  | valor replanejado |
| Replanejado | 19,0 | 5,0 | 57,0 | 19,0 |  |

   
P1 = Recebe o valor real que já havia sido lançado = 19  
P2 = Recebe o valor real lançado = 5  
P3 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 54 + ((9 - 5) \* (54 / 72)) = 54 + 3 = 57  
P4 = VPP + ((VPL - VRL) \* (VPP / VPF)) = 18 + ((9 - 5) \* (18 / 72)) = 18 + 1 = 19

Obs.: Neste caso, o valor Planejado já inicia com o valor resultante do replanejamento do valor real lançado no período 1.

Na seleção de tarefas sem cronograma realizado o primeiro período passível de alteração recebera o percentual realizado zero, entende-se que a tarefa não foi realizada no período.

Exemplo:

As tarefas A e B foram selecionadas e foi executado o processo de replanejamento.

Tarefa A

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 10,0 | 10,0 | 60,0 | 20,0 | valor lançado |
| Realizado | 1,0 |  |  |  | valor replanejado |
| Replanejado | 1,0 | 11,0 | 66,0 | 22,0 |  |

Tarefa B

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Períodos** | **1** | **2** | **3** | **4** | Legenda: |
| Planejado | 50 | 25 | 25 | 0 | valor lançado |
| Realizado |  |  |  |  | valor replanejado |
| Replanejado | 0,0 | 50 | 50 | 0 |  |

---
