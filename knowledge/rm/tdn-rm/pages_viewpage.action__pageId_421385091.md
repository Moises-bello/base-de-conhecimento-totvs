---
content_hash: 7779094e44f84130f6ae86eb1d4ed56daabb4173cc9a4e58d0ebfca0dda66342
fetched_at: '2026-06-29T00:09:13.704171+00:00'
page_id: '421385091'
product: rm
source: tdn-rm
title: Atualiza Cronograma pelos lançamentos de Medição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385091
version: 4
---

O processo "Atualizar o cronograma pelos lançamentos de medição", tem como objetivo atualizar o Cronograma Medido ou o Cronograma Realizado com as medições realizadas no contrato.  
 Para isso basta clicar no botão "Atualizar o cronograma pelos lançamentos de medição", na visão de Contrato, que será apresentada uma tela onde:  
    
Deverá ser definido qual cronograma será atualizado (Cronograma Medido ou Realizado);  
Se os valores e quantidades atualizadas serão substituídos ou acumulados:  
    
 Caso substituídos, os valores dos cronogramas MEDIDO e REALIZADO serão substituídos pelo valor de lançamento do contrato;  
 Caso acumulados, os valores dos cronogramas MEDIDO e REALIZADO serão somados com o valor de lançamento do contrato;  
 A atualização de ambos os cronogramas é feita automaticamente.  
    
 Para visualizar a atualização basta selecionar a tarefa que foi utilizada para medição no contrato e abrir o cronograma, serão visualizados os valores de acordo com a quantidade associada e o percentual medido da tarefa, demonstrados através dos períodos em que foram realizadas as medições.

Exemplo 1 :A tarefa x tem quantidade igual a 100, valor unitário igual a 10, foram associadas 100% da quantidade para o contrato e medido 50% no período 1 e 50% no período 2. Ao clicar no botão "Atualizar o cronograma pelos lançamentos de medição", será atualizado o cronograma com estes lançamentos.  
   
Visualização do cronograma com a tarefa X selecionada e atualizados os Cronogramas Medido e Realizado:

|  |  |  |  |
| --- | --- | --- | --- |
| Período 1 |  |  | Período 2 |
| Realizado: | Percentual: | 100 | 50 |
| Realizado: | Quantidade: | 100 | 50 |
| Realizado: | Valor: | 1.000,00 | 500,00 |
| Medido: | Percentual: | 100 | 50 |
| Medido: | Quantidade: | 100 | 50 |
| Medido: | Valor: | 1.000,00 | 500,00 |

   
Exemplo 2: A tarefa x tem quantidade igual a 100, valor unitário igual a 10, foram associadas 50% da quantidade para o contrato e medido 50% no período 1 e 50% no período 2. Ao clicar no botão "Atualizar o cronograma pelos lançamentos de medição", será atualizado o cronograma com estes lançamentos.  
   
Visualização do cronograma com a tarefa X selecionada e atualizados os Cronogramas Medido e Realizado:

|  |  |  |  |
| --- | --- | --- | --- |
| Período 1 |  |  | Período 2 |
| Realizado: | Percentual: | 50 | 25 |
| Realizado: | Quantidade: | 50 | 25 |
| Realizado: | Valor: | 500,00 | 250,00 |
| Medido: | Percentual: | 50 | 25 |
| Medido: | Quantidade: | 50 | 25 |
| Medido: | Valor: | 500,00 | 250,00 |

Exemplo 3.: Considerando o exemplo anterior, já existem os valores acima lançados no cronograma, agora definiremos que será atualizado o cronograma medido, e os valores serão acumulados.

|  |  |  |  |
| --- | --- | --- | --- |
| Período 1 |  |  | Período 2 |
| Realizado: | Percentual: | 50 | 25 |
| Realizado: | Quantidade: | 50 | 25 |
| Realizado: | Valor: | 500,00 | 250,00 |
| Medido: | Percentual: | 100 | 50 |
| Medido: | Quantidade: | 100 | 50 |
| Medido: | Valor: | 1.000,00 | 500,00 |

Caso os valores fossem substituídos a tabela permaneceria igual à tabela do Exemplo2.

Os valores dos períodos principais e complementares serão somados aos valores já existentes, já os períodos de estorno serão abatidos;  
Não aconselhamos a conversão de dados do Contrato para o Cronograma acumulando valores quando o lançamento no cronograma tiver sido feito de forma diferente do contrato, ou seja, o lançamento do cronograma foi feito em valor e o contrato em quantidade. Nesse caso, o lançamento do cronograma será alterado para quantidade.
