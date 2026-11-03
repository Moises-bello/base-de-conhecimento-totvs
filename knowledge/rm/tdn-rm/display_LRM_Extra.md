---
content_hash: 97b75cbdc94702564135ec87527687c325426b79654209989e155fd2c42d697f
fetched_at: '2026-06-29T00:10:07.148554+00:00'
page_id: '452719368'
product: rm
source: tdn-rm
title: Extra
type: documentation
url: https://tdn.totvs.com/display/LRM/Extra
version: 3
---

**Extra**   
**Tabela de Extras** Defina como será aplicada a tabela de extra, Dia a dia ou por Período, caso tenha intenção de arredondar as horas extras. Para cadastrar uma tabela vá até a etapa Tabela de extras.  
**Considera início da jornada para definir tipo de extra** Com esse parâmetro habilitado o sistema irá considerar as horas extras executadas considerando o início da jornada do funcionário, ou seja, no dia que ele efetuou a primeira batida da sua jornada de trabalho.

Importante

* Caso o parâmetro **Considera extras de refeição dentro do intervalo de ausência planejada** estiver marcado juntamente com o parâmetro citado acima, nos horários com ausência planejada, a ocorrência de Extra Refeição Autorizada(ERA) não será gerada, fazendo que a ocorrência seja substituída por outro tipo de extra.
* Será necessário desmarcar o parâmetro **Considera início da jornada para definir tipo de extra**, para que a seja entendido como Extra Refeição Autorizada.

**Exemplo:**  
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 |  |  |
| 01/02/2011 | 22:00 |  |  |  |
| 02/02/2011 |  | 05:00 |  |  |
| 03/02/2011 | Descanso |  |  |  |
| 04/02/2011 | 22:00 |  |  |  |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada2 |  |
| 01/02/2011 | 22:00 |  |  |  |
| 02/02/2011 |  | 05:00 | 22:00 |  |
| 03/02/2011 |  | 05:00 | 22:00 |  |
| 04/02/2011 |  | 05:00 |  |  |

Ocorrências geradas  
02/02/2011  22:00 a 03/02/2011  05:00 são geradas 07:00 de Extra Normal  
03/02/2011  22:00 a 03/02/2011  00:00 são geradas 02:00 de Extra de Descanso  
   
Com o parâmetro desabilitado o sistema irá considerar a extra quebrando dia a dia, considere como exemplo o mesmo Horário Planejado e mesmo Horário Executado acima.  
   
   
Ocorrências geradas  
02/02/2011  22:00 a 02/02/2011  00:00 são geradas 02:00 de Extra Normal  
03/02/2011  00:00 a 03/02/2011  05:00 são geradas 05:00 de Extra de Descanso  
03/02/2011  22:00 a 03/02/2011  00:00 são geradas 02:00 de Extra de Descanso

**Considera extras de refeição dentro do intervalo de ausência planejada:** Ao habilitar este parâmetro é gerada ocorrência Extra Refeição Autorizado, caso seja feito um tempo menor de ausência.

Exemplo:

Horário planejado com ausência de refeição:

| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| --- | --- | --- | --- | --- |
| 08/10/2024 | 08:00 | 12:00 | 14:00 | 18:00 |

Horário Executado

| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| --- | --- | --- | --- | --- |
| 08/10/2024 | 08:00 | 12:00 | 13:00 | 18:00 |

Ocorrências:

| Início | Fim | Total | Tipo de ocorrência | Descrição |
| --- | --- | --- | --- | --- |
| 08/10/2024 08:00 | 08/10/2024 12:00 | 04:00 | T | Trabalho |
| 08/10/2024 12:00 | 08/10/2024 13:00 | 01:00 | AREF | Ausência de Refeição |
| 08/10/2024 13:00 | 08/10/2024 14:00 | 01:00 | ERA | Extra Refeição Autorizado |
| 08/10/2024 14:00 | 08/10/2024 08:00 | 18:00 | T | Trabalho |

Exemplo horário com limite de refeição:

Limite de 12:00 as 14:00

| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| --- | --- | --- | --- | --- |
| 08/10/2024 | 08:00 | 12:00 | 14:00 | 18:00 |

Horário Executado

| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| --- | --- | --- | --- | --- |
| 08/10/2024 | 08:00 | 12:30 | 13:40 | 18:00 |

Ocorrências

| Início | Fim | Total | Tipo de ocorrência | Descrição |
| --- | --- | --- | --- | --- |
| 03/10/2024 08:00 | 03/10/2024 12:00 | 04:00 | T | Trabalho |
| 03/10/2024 12:00 | 03/10/2024 12:30 | 00:30 | ERA | Extra Refeição Autorizado |
| 03/10/2024 12:30 | 03/10/2024 13:40 | 01:10 | AREF | Ausência de Refeição |
| 03/10/2024 13:40 | 03/10/2024 14:00 | 00:20 | ERA | Extra Refeição Autorizado |
| 03/10/2024 14:00 | 03/10/2024 18:00 | 04:00 | T | Trabalho |

   
**Distribui extras em faixas considerando a jornada** Com esse parâmetro habilitado o sistema irá distribuir as extras nas faixas cadastradas considerando a jornada iniciada de trabalho do funcionário, ou seja, no dia que ele efetuou a primeira batida da sua jornada de trabalho até a sua saída as horas extras serão distribuídas nas faixas. Com esse parâmetro desabilitado a distribuição das faixas se iniciam a cada dia independentemente se a jornada de trabalho realizada é de um dia para o outro.  
   
Exemplo:  
   
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada 2 |  |
| 01/02/2011 | 22:00 |  |  |  |
| 02/02/2011 |  | 05:00 |  |  |
| 03/02/2011 |  |  | 22:00 |  |
| 04/02/2011 |  | 05:00 |  |  |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada2 |  |
| 01/02/2011 | 22:00 |  |  |  |
| 02/02/2011 |  | 05:00 | 22:00 |  |
| 03/02/2011 |  | 05:00 | 22:00 |  |
| 04/02/2011 |  | 05:00 |  |  |

O funcionário trabalhou do dia 2 ao dia 3, como no dia 3 ele não tem Horário Planejado será calculada 07:00 de horas extras neste dia.  
   
Faixas de extra cadastradas:  
Faixa 1: 2 horas  
Faixa 2: 2 horas  
Faixa 3: 2 horas  
Faixa 4: 2 horas  
   
Com o parâmetro marcado:  
   
No dia 2 teremos:  
02:00 horas na Faixa 1  
   
No dia 3 teremos:  
02:00 horas na Faixa 2  
02:00 horas na Faixa 3  
01:00 hora na Faixa 4  
   
Totalizando para os dois dias:  
02:00 horas na Faixa 1  
02:00 horas na Faixa 2  
02:00 horas na Faixa 3  
01:00 hora na Faixa 4  
   
Com o parâmetro desmarcado:  
   
No dia 2 teremos:  
02:00 horas na Faixa 1  
   
No dia 3 teremos:  
02:00 horas na Faixa 1           
02:00 horas na Faixa 2  
01:00 hora na Faixa 3  
   
Totalizando para os dois dias:  
04:00 horas na Faixa 1  
02:00 horas na Faixa 2  
01:00 hora na Faixa 3

**Gerar extra normal/compensado/descanso/feriado no intervalo de extra de sobreaviso:**Com esse parâmetro marcado, além da ocorrência de sobreaviso, será gerado também a ocorrência de extra normal/descanso/compensado/feriado para o intervalo de sobreaviso trabalhado.

Exemplo:

Sobreaviso cadastrado: 19:00 às 23:30

Horário executado: 18:30 às 22:00

Horas de sobreaviso (SAV): 04:30 horas de 19:00 às 23:30

Horas extras normais (EA): 03:30 horas de 18:30 às 22:00

Horas de sobreaviso extra normal (SAN): 03:00 horas de 19:00 às 22:00

Da mesma forma será gerado para dia de compensado, descaso e feriado.
