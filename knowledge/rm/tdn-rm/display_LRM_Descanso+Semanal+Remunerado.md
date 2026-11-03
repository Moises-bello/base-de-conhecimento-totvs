---
content_hash: 9ff457ce81b166f06f7bb02a007fd695ed44d09d7b07bceb83595beade952665
fetched_at: '2026-06-29T00:10:04.518077+00:00'
page_id: '452719211'
product: rm
source: tdn-rm
title: Descanso Semanal Remunerado
type: documentation
url: https://tdn.totvs.com/display/LRM/Descanso+Semanal+Remunerado
version: 8
---

**Descanso Semanal Remunerado**

**Carência para desconto do D.S.R** Defina o número máximo de horas de atraso que o funcionário poderá ter sem que o mesmo perca o Descanso Semanal Remunerado (D.S.R), essas horas poderão ser aplicadas diariamente ou semanalmente.

**Tipo de carência D.S.R** Defina qual será o tipo de carência, Diário ou Semanal, para que o funcionário não perca do D.S.R conforme as horas informadas no campo Carência para desconto do D.S.R.

**Dia do D.S.R** Defina qual será o dia da semana considerado com base para o cálculo do Descanso Semanal Remunerado.

**Considera intervalos de tolerância para o cálculo de D.S.R** Habilitando esse parâmetro as ocorrências de atrasos que foram toleradas serão consideradas como horas trabalhadas para o calculo do D.S.R., e caso desmarcado, serão consideradas como atraso.

Exemplo:

Horário do Funcionário: 08:00E 12:00S 14:00E 18:00S

Tolerância : 10 minutos presença e ausência para todos as batidas

Carência para Desconto do D.S.R. : 04:00

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1ª Semana |  |  |  |  |  |  |  |
| SEG | 08:00E 12:00S |  |  |  |  |  | ATRASO |
| TER | 08:10E 12:00S 14:00E 18:00S |  |  |  |  |  | ATRASO TOLERADO |
| QUA | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  |  |
| QUI | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  |  |
| SEX | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  |  |
| SAB | COMPENSADO |  |  |  |  |  |  |
| DOMINGO | DESCANSO |  |  |  |  |  | DSR |

Com o parâmetro marcado, o atraso tolerado será considerado como hora trabalhada, e o total de atrasos na semana será 04:00, dentro da carência para desconto do D.S.R., que não será perdido.

Com o parâmetro desmarcado, o atraso tolerado será desconsiderado como hora trabalhada, e o total de atrasos na semana será 04:10, excedendo a carência para desconto do D.S.R., que será perdido.

**Considera os feriados para o cálculo de D.S.R** Habilitando esse parâmetro as horas de feriado informadas no cadastro do funcionário serão somadas ao número de horas do D.S.R. Quando o funcionário perder o DSR na semana do feriado, ele também perderá as horas relativas ao feriado. Caso contrário o cálculo de D.S.R não irá considerar os feriados da semana.

Se o feriado cair durante as férias e o funcionário retornar ao trabalho nessa mesma semana, mas faltar algum dia, ele perde o DSR do feriado.

**Exemplo:**

* Feriado na última semana de férias, com retorno ao trabalho na mesma semana:

| **Data** | **Dia da Semana** | **Jornada Esperada** | **Detalhes** |
| --- | --- | --- | --- |
| 19/04 | Segunda | Férias |  |
| 20/04 | Terça | Férias |  |
| **21/04** | **Quarta** | **Férias** | **Feriado** |
| 22/04 | Quinta | Férias |  |
| **23/04** | **Sexta** | **Retorno ao Trabalho** | **Faltou** |
| 24/04 | Sábado | Compensado |  |
| **25/04** | **Domingo** | **Descanso** | **Perdeu o DSR do Feriado e da Semana** **gerou DSP** |

No exemplo acima, a falta após o retorno ao trabalho faz com que o funcionário perca tanto o DSR da semana quanto o DSR referente ao feriado.

**Considera atraso para perda de D.S.R** Habilitando esse parâmetro o sistema passa a considerar também os atrasos para a perda de D.S.R no cálculo.

**Considera D.S.R proporcional**Habilitando este parâmetro o sistema irá considerar o D.S.R proporcional ao número de horas informado no parâmetro do funcionário. Para cada dia de perda de D.S.R o sistema irá descontar do total do D.S.R o valor proporcional informado.

Exemplo:  
Número de Horas do DSR: 08h: 00m  
Núm. Horas DSR Proporcional: 01h: 36m  
Horário do Funcionário: 08:00E 12:00S 14:00E 18:00S

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1ª Semana |  |  |  |  |  |  |  |
| SEG | 08:00E 12:00S 14:00E 17:00S |  |  |  |  |  | FALTA |
| TER | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  | ATRASO |
| QUA | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  |  |
| QUI | 08:00E 12:00S 14:00E 18:00S |  |  |  |  |  |  |
| SEX | COMPENSADO |  |  |  |  |  |  |
| SAB | DESCANSO |  |  |  |  |  |  |
| DOMINGO | 08:00E 12:00S 14:00E 17:00S |  |  |  |  |  | DSR |

Caso contrário o sistema calculará como D.S.R Perdido apenas o valor informado no campo Número Horas D.S.R. Proporcional localizado no parâmetro do funcionário multiplicado pelo número de vezes que ele perderia o D.S.R. O D.S.R passará a ser a diferença do Número de Horas do D.S.R menos o número de horas do D.S.R Perdido.Ao analisar a semana do funcionário, não marcando este parâmetro, o sistema consideraria para esta semana 08:00 de D.S.R perdido, visto que o funcionário teve um atraso ou uma falta que o faria perder o D.S.R.

Como ficaria o cálculo:  
D.S.R PERDIDO.:  
Número de Horas D.S.R Proporcional: 01h: 36m  
Número de Ocorrência que perde o D.S.R: um Atraso = 1   
D.S.R PERDIDO = (Número de Horas D.S.R Proporcional x Número de Ocorrência que perde o D.S.R);  
D.S.R PERDIDO = 01:36 x 1 = 01:36 horas  
   
D.S.R.:  
Número de Horas D.S.R: 08h: 00m  
D.S.R Perdido: 01h: 36m  
D.S.R = (Número de Horas D.S.R – D.S.R PERDIDO)  
D.S.R = 8h: 00m – 01h: 36m = 06h: 24m  
   
**Considera D.S.R acumulado quando feriado coincidir com descanso** Habilitando este parâmetro o sistema não irá pagar D.S.R de Feriado quando o dia do feriado coincindir com o dia de Descanso.
