---
content_hash: 3e4bd5e0edc2e0d41864e9f8e721ae08dc520dbeadd3e8537432792b263a5d35
fetched_at: '2026-06-29T00:10:06.616799+00:00'
page_id: '452719321'
product: rm
source: tdn-rm
title: Compensação do cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719321
version: 4
---

**Compensação do cálculo**

*Observação: As opções a seguir ficarão disponíveis para os funcionários que tem no seu histórico um registro de horário do tipo flexível.*

**Tipo de Compensação:** Este campo indica em qual período o funcionário poderá compensar seus intervalos compensáveis. É possível escolher as seguintes opções:

* Diária: A compensação será realizada apenas entre as extras e atrasos e faltas do dia.
* Semanal: A compensação será realizada apenas entre as extras e atrasos e faltas da semana.
* Período: A compensação será realizada apenas entre as extras e atrasos e faltas do período.
* Jornada: A compensação será realizada apenas entre as extras e atrasos e faltas da jornada.

**Observação:** Para a compensação semanal ou por período, caso a(s) falta(s) ou o(s) atraso(s) que iriam provocar a perda do DSR sejam *compensadas* *dentro da semana de referencia* deste DSR, não ocasionará a perda deste DSR.  
   
**Não compensa se número de horas de atraso / falta acima de:** Neste campo deve ser informado o limite de horas diárias de atrasos e faltas que poderão ser compensados. Caso exista um atraso / falta  superior ao valor informado, todo o atraso será descontado, não efetuando a compensação deste atraso / falta. Esse comportamento somente será aplicado quando está definido o tipo de compensação por Jornada.

***Exemplo:*** ***Horário Planejado – Horário flexível*** **Não compensa se número de horas de atraso / falta acima de:** 01:00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Saída2** |
| 01/08/2008 | 08:00 | *12:00* | 1400 | 18:00 |
| 02/08/2008 | 08:00 | *12:00* | 1400 | 18:00 |
| 03/08/2008 | 08:00 | *12:00* | 1400 | 18:00 |

 ***Horário Executado***

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Saída2** |
| 01/08/2008 | 09:00 | *12:00* | 14:00 | 19:30 |
| 02/08/2008 | 09:10 | *12:00* | 14:00 | 19:30 |
| 03/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |

   
   
   
   
Na situação acima, para o dia 01/08 foi compensado o atraso de 08:00 as 09:00 com a extra de 18:00 as 19:00 e serão gerados 30 minutos de extra de 19:00 as 19:30.  
Já no dia 02/08 o atraso foi de 01:10, no intervalo de 08:00 as 09:10, ficando acima  do valor informado neste parâmetro e nenhuma parte deste atraso será compensada, gerando então 01:10 de atraso e 01:30 de horas extras.   
   
**Utiliza Extra de Compensado:** Este parâmetro define se poderão ser utilizadas as horas extras de dias de compensado (normalmente o sábado) para a compensação de atrasos e faltas, caso não utilize, estas horas extras serão lançadas para o movimento ou banco de horas, de acordo com parametrização do sindicato.   
   
**Utiliza Extra de Descanso:** Este parâmetro define se poderão ser utilizadas as horas extras de dias de descanso (normalmente o domingo) para a compensação de atrasos e faltas, caso não utilize, estas horas extras serão lançadas para o movimento ou banco de horas, de acordo com parametrização do sindicato.  
   
**Utiliza Extra de Feriado:** Este parâmetro define se poderão ser utilizadas as horas extras de dias de feriado para a compensação de atrasos e faltas, caso não utilize, estas horas extras serão lançadas para o movimento ou banco de horas, de acordo com parametrização do sindicato.  
   
**Compensa Faltas:** Este campo define se as faltas serão compensadas junto com os atrasos. Se este campo não estiver confirmado, o Sistema irá lançar as faltas para o funcionário mesmo que o seu saldo de horas extras seja suficiente para compensá-las. Apenas é possível compensar as faltas utilizando-se a compensação *Semanal* ou por *Período***.**  
   
**Considera ocorrências compensadas no espelho:** Esse parâmetro define se irá considerar as ocorrências (Extras, atrasos, faltas) compensadas no cálculo na totalização do espelho do período.  
   
**Exemplo:**  
**Horário Executado**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Extras compensadas** | **Atrasos compensados** |
| 20/12/2012 | 11:00 | *18:00* | 03:00 | 03:00 |

Com o parâmetro desmarcado o espelho do período não totaliza nenhum valor de extra/atraso, caso o parâmetro seja marcado o sistema vai totalizar no dia 03:00 hrs de atrasos e extras.  
**Início da compensação de atrasos e faltas:** Este parâmetro determina qual será a primeira extra a ser compensada, da primeira faixa para a ultima ou da ultima faixa para a primeira.  
***Exemplo:*** ***Horário Planejado – Horário flexível***

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Saída2** |
| 01/08/2008 | 08:00 | *12:00* |  |  |

**Faixas de distribuição:**

|  |  |
| --- | --- |
|  | **Extra normal** |
| Primeira faixa | 02:00 |
| Segunda faixa | 02:00 |
| Terceira faixa | 24:00 |

**Horário Executado:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Extras** | **Atrasos** |
| 01/08/2008 | 11:00 | *18:00* | 6:00 | 03:00 |

No exemplo acima, temos 2 horas de extras em cada faixa. Caso seja selecionada a opção de compensar a partir da primeira faixa, serão compensadas com as 3 horas de atraso as duas horas da primeira faixa e uma hora da segunda faixa, sobrando para o movimento / banco de horas 1 hora na segunda faixa e 2 horas na terceira faixa. Caso seja selecionada a opção de compensar a partir da ultima faixa, serão compensadas com as 3 horas de atraso as duas horas da terceira faixa e uma hora da segunda faixa, sobrando para o movimento / banco de horas 1 hora na segunda faixa e 2 horas na primeira faixa.  
**Considera Percentual:** Este parâmetro define se irá considerar o percentual de cada extra para a compensação, ou seja,  as horas extras de cada faixa serão multiplicadas pelo seu percentual de incidência antes da compensação de atrasos por extras.  
**Exemplo:**

|  |  |
| --- | --- |
| Extra 50% | **01:00** |
| Atraso | 01:30 |

Caso o parâmetro esteja marcado, a hora extra existente irá compensar o atraso (01:00 de extra compensando 1:30 de atraso). Caso esteja desmarcado, será compensada 01:00 de extra com 01:00 de atraso e ainda sobrarão 00:30 de atraso.  
**Observação:** O percentual de incidência será buscado no respectivo campo cadastrado para o evento na tabela de eventos do Totvs Folha de Pagamento, que estiver associado ao evento correspondente do Totvs Automação de Ponto pela tabela de relacionamento de eventos, segundo o parâmetro do sindicato associado ao funcionário.
