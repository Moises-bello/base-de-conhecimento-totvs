---
content_hash: 4148ad326219c7441d4db420788b82ab8af2fe7acd0c069f9de6b4f2893fb5ca
fetched_at: '2026-06-29T00:10:07.022566+00:00'
page_id: '452719358'
product: rm
source: tdn-rm
title: Horário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719358
version: 5
---

**Horário**   
**Utiliza horário contíguo:** Este parâmetro faz com que o sistema considere a movimentação do funcionário com base na data de entrada da jornada.  
   
**Exemplo:**  
*Horário Planejado*

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada 2** |
| 01/08/2008 | 21:30 |  |  |
| 02/08/2008 |  | *06:00* | 21:30 |
| 03/08/2008 |  | *06:00* |  |

*Realizado – Horário normal*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Horas Trab** | **Extras** |
| 01/08/2008 | 21:00 |  |  | 03:00 | 00:30 |
| 02/08/2008 |  | *06:00* | 21:20 | 08:40 | 00:10 |
| 03/08/2008 |  | *07:00* |  | 07:00 | 01:00 |

*A - Realizado – Horário Contiguo*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Horas Trab** | **Extras** |
| 01/08/2008 | 21:00 |  |  | 09:00 | 00:30 |
| 02/08/2008 |  | *06:00* | 21:20 | 09:40 | 01:10 |
| 03/08/2008 |  | *07:00* |  | 00:00 | 00:00 |

*B - Realizado – Horário Contiguo – Visualização conforme horário contiguo*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Horas Trab** | **Extras** |
| 01/08/2008 | 21:00 | *06:00+* |  | 09:00 | 00:30 |
| 02/08/2008 | 21:20 | *07:00+* |  | 09:40 | 01:10 |
| 03/08/2008 |  |  |  | 00:00 | 00:00 |

   
**Considerar jornadas de descanso para interjornada:** Com este parâmetro desmarcado, é levado em consideração a Interjornada de 35h semanais, sendo 11h de interjornada ou o tempo mínimo informado entre jornadas, e 24h de descanso. Com o parâmetro marcado, o comportamento do sistema continua sendo de levar em consideração apenas as 11h entre jornadas de trabalho.  
  
  
   
**Tempo mínimo entre jornadas:** Este campo será utilizado para informar o número mínimo de horas que o funcionário deve ter entre o fim de uma jornada e o início da próxima jornada. Para os casos que um mesmo índice do horário contém mais de um id jornada o tempo mínimo também será aplicado.

   
**Exemplo:**  
   
*Horário Planejado*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Saída2** |
| 01/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |
| 02/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |
| 03/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |

*Horário Executado*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada2** | **Saída2** |
| 01/08/2008 | 08:00 | *12:00* | 14:00 | 23:00 |
| 02/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |
| 03/08/2008 | 08:00 | *12:00* | 14:00 | 18:00 |

No exemplo acima, entre a saída do dia 01/08 e a entrada do dia 02/08 há apenas o intervalo de 9 horas. O sistema irá calcular, de acordo com os eventos cadastrados, 2 horas de extras de Interjornada, além de incluir um aviso no novo cálculo (ou alerta no calculo antigo, caso seja gerado o log.).
