---
content_hash: ce774d1af00066ffd5165a7efca759e7eeff9c1cdf1a736ed1db3e997588f246
fetched_at: '2026-06-29T00:10:04.167037+00:00'
page_id: '452719207'
product: rm
source: tdn-rm
title: Atrasos e Faltas
type: documentation
url: https://tdn.totvs.com/display/LRM/Atrasos+e+Faltas
version: 1
---

**Atrasos e Faltas**   
**Tabela de atrasos** Defina como será aplicada a tabela de atrasos, Dia a dia ou por Período, caso tenha intenção de lançar horas de atrasos diferentes do que as calculadas pelo sistema.  
**Considera Atraso fora da jornada de trabalho** Com esse parâmetro habilitado quando o funcionário executar batidas fora da sua jornada de trabalho será calculado atraso e não falta na jornada.  
Exemplo:  
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 |  |  |
| 25/02/2011 | 08:00 | 14:00 |  |  |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 |  |  |
| 25/02/2011 | 15:00 | 21:00 |  |  |

Ocorrências geradas  
25/02/2011  08:00 a 14:00 são geradas 06:00 de Atraso  
25/02/2011  15:00 a 21:00 são geradas 06:00 de Extra  
   
Com o parâmetro desabilitado o sistema irá gerar falta, considere como exemplo o mesmo Horário Planejado e mesmo Horário Executado acima.  
   
Ocorrências geradas  
25/02/2011  08:00 a 14:00 são geradas 06:00 de Falta  
25/02/2011  15:00 a 21:00 são geradas 06:00 de Extra  
   
**Número de horas de falta** Caso queira descontar um valor de horas de falta diferente da jornada cadastrada no horário do funcionário informe o valor a ser descontado nesse campo.  
   
Exemplo:  
   
Número de horas de Falta: 05:45  
   
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 |  |  |
| 25/02/2011 | 08:00 | 14:00 | 06:00 de Trabalho |  |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 |  |  |
| 25/02/2011 | Falta |  |  |  |

Ocorrência gerada  
25/02/2011  08:00 a 14:00 são geradas 05:45 de Falta devido ao valor informado no campo Número de horas de Falta.  
   
Caso o campo não seja preenchido será calculadas 06:00 de Falta conforme Horário Planejado.  
**Considera ausência quando existir batida sem par** Com esse parâmetro habilitado o sistema irá calcular falta quando não existir uma batida de saída para uma batida de entrada, caso não esteja habilitado quando existir uma batida de entrada sem uma batida de saída correspondente o sistema irá calcular extra.
