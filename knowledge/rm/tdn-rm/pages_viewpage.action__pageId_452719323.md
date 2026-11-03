---
content_hash: 642636acfff53dd12b0b8278b8ac956655a3fa3218d3ab449e3f126c5503a92f
fetched_at: '2026-06-29T00:10:06.633809+00:00'
page_id: '452719323'
product: rm
source: tdn-rm
title: Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719323
version: 3
---

**Cálculo**

**Localização: Automação de Ponto| Parametrizador| Sindicato| Etapa 1 - Cálculo**

**Calcula funcionário sem movimento** Com esse parâmetro habilitado será feito o cálculo de horas de falta quando o funcionário não tiver nenhuma batida no período.

**Quebra intervalo executado entre jornadas planejadas que fazem interseção** Com esse parâmetro habilitado o sistema irá quebrar o intervalo executado entre as jornadas planejadas que fizerem interseção conforme exemplo abaixo:

Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada2 | Saída2 |
| 01/02/2011 | 08:00 | 12:00 | 14:00 | 18:00 |
| 02/02/2011 | 08:00 | 12:00 | 14:00 | 18:00 |
| 03/02/2011 | 08:00 | 12:00 | 14:00 | 18:00 |
| 04/02/2011 | Descanso |  |  |  |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada2 | Saída2 |
| 01/02/2011 | 08:00 | 12:00 | 14:00 |  |
| 02/02/2011 |  | 09:00 |  |  |
| 03/02/2011 | 08:00 | 12:00 | 14:00 |  |
| 04/02/2011 |  | 09:00 |  |  |

O sistema irá calcular:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Horas Trabalhadas | Atrasos | Extras | Extras de Descanso |
| 01/08/2008 | 22:00 |  | 14:00 |  |
| 02/08/2008 | 01:00 | 07:00 |  |  |
| 03/08/2008 | 14:00 |  | 06:00 |  |
| 04/08/2008 |  |  |  | 09:00 |

 Com o parâmetro desabilitado o sistema irá considerar todo intervalo executado conforme a jornada de entrada, considere como exemplo o mesmo Horário Planejado e mesmo Horário Executado acima.  
O sistema irá calcular:

|  |  |  |  |
| --- | --- | --- | --- |
| Data | Horas Trabalhadas | Extras | Faltas |
| 01/08/2008 | 23:00 | 15:00 |  |
| 02/08/2008 |  |  | 08:00 |
| 03/08/2008 | 23:00 | 15:00 |  |
| 04/08/2008 |  |  |  |

**Alterar extra executada e extra autorizada na movimentação do funcionário** Com esse parâmetro habilitado o valor dos campos de Extra Autorizada e Extra Executada no espelho serão substituidos pelos valores calculados por fórmula, para aqueles funcionários que utilizam banco de horas diário.

**Alterar somente extra autorizada na movimentação** Com esse parâmetro habilitado o valor do campo de Extra Autorizada será substituido pelo valore calculado por fórmula, para aqueles funcionários que utilizam banco de horas diário.

**Considera percentual para o movimento:** Permite o lançamento de horas das horas para o movimento considerando o percentual de incidência do evento. Para isso, é necessário que o evento associado no Sindicato| Eventos tenha um percentual de incidência informado.

**Considera percentual para o banco de horas:** Permite o lançamento das horas para o banco de horas considerando o percentual de incidência do evento. Para isso, é necessário que o evento associado no Sindicato| Eventos tenha um percentual de incidência informado.
