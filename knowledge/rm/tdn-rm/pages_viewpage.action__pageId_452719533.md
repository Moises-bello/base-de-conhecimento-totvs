---
content_hash: 4e24cd28897a241f49eca5c0c9b291584087d9c043119bc324dc5d32e142e41d
fetched_at: '2026-06-29T00:10:08.540988+00:00'
page_id: '452719533'
product: rm
source: tdn-rm
title: Montagem Automática
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719533
version: 2
---

**Montagem Automática**   
O processo de montagem automática tem a finalidade de ajustar o cenário de controle de lotação e verba da empresa, preenchendo os dados dos controles conforme parametrizado através do "Parametrizador" e de acordo com o cenário atual da empresa, ou seja, caso a empresa possua seu controle de lotação/verba baseados no cadastro de seção em qualquer nível, por exemplo, ao executar este processo, serão verificados os quantitativos de funcionários alocados nas seções e preenchidos os limites de vagas/verbas de acordo com os quantitativos de funcionários/salários destas seções. Para saber mais detalhes sobre as possibilidades de parametrização e como fazê-las verifique nos links abaixo no item "Como Fazer".  
   
Ao parametrizar seu controle de lotação ou necessite fazer alguma manutenção que interfira na forma de controle do mesmo, é necessário que execute este processo para que as modificações feitas reflitam em seu controle, caso contrário, os limites ficarão irreais e não serão feitos os controles corretamente. Vale ressaltar que, caso possua quantitativos de vagas e verbas que sejam maiores que os quantitativos já alocados esses valores serão alterados, ou seja, se o quantitativo de vagas for maior que o número de funcionários alocados, ao executar este processo, será necessário dar manutenção novamente nestes controles.  
   
**Exemplo:**  
   
A Seção 01.01 possui os seguintes funcionários:  
   
1)      João José    –  Salário: 1.000,00  
2)      Maria João   – Salário: 2.200,00  
3)      João Maria   – Salário: 2.000,00  
   
A Seção 02.01 possui somente o funcionário abaixo:  
   
1)      José João     – Salário: 1.300,00  
   
Com o controle de lotação parametrizado como seção em qualquer nível tanto para vaga quanto para verba, serão preenchidos os limites para todas as seções da hierarquia onde os funcionários estão lotados e não somente das seções folha.  No exemplo acima, ao executar o processo de montagem automática, os limites das seções ficariam da seguinte forma:

|  |  |  |
| --- | --- | --- |
| **Seção** | **Limite Func.** | **Limite Verba** |
| 0 | 4 | 6.500,00 |
| 01 | 3 | 5.200,00 |
| 01.01 | 3 | 5.200,00 |
| 02 | 1 | 1.300,00 |
| 02.01 | 1 | 1.300,00 |

Caso faça a parametrização e não execute a montagem automática, os limites de verba e de vagas das seções acima ficariam com valor 0 (zero), considerando que sempre foram excedidos os limites pois já possuem funcionários lotados nas seções em questão.   
   
**Observação:**

* Na execução do processo, na etapa "Selecionar faixa para a Montagem Automática do Controle de Lotação", tanto em Controle  de Vaga ou Verba, se for informado um intervalo de seção/função, o processo será executado somente para este intervalo. Caso contrário, se não for informado nenhum intervalo, o processo é executado para todas as seções/funções. Se o intuito for executar o processo somente para uma seção/função, deverá ser informado os mesmos valores nos blocos "De" e "Até".  
   

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  Como Parametrizar o Controle de Lotação
