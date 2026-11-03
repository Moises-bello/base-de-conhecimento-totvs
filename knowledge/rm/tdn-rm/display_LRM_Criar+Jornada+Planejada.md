---
content_hash: 95d4ab1a21f6d6a7daa4faf8a2012aad7bc12098b6b0ba66083025bfda53a007
fetched_at: '2026-06-29T00:10:03.639748+00:00'
page_id: '452719106'
product: rm
source: tdn-rm
title: Criar Jornada Planejada
type: documentation
url: https://tdn.totvs.com/display/LRM/Criar+Jornada+Planejada
version: 2
---

Os passos a seguir são comuns a qualquer tipo de horário, logo depois veremos as particularidades para cada tipo de horário.

**Índice da Jornada:** Associe a letra conforme o índice do horário, tenha como referência a data.

**Tipo da Jornada:** Para cada índice devemos associar um tipo de jornada, onde:  
Trabalho: Intervalo de horas normais que o funcionário deverá estar trabalhando, caso contrário será calculada falta ou atraso.  
Compensado: Intervalo de horas que o funcionário deverá estar compensando, caso trabalhe será calculada hora extra de compensado.  
Descanso: Intervalo de horas que o funcionário deverá estar descansando, caso trabalhe será calculada hora extra de descanso.  
Sem Trabalho (Batida Nula): Intervalo de horas que não são geradas horas normais para o funcionário e caso exista algum intervalo executado será calculada hora extra normal no dia.

**Intervalos Planejados da Jornada**  
Os intervalos planejados da jornada podem ser as batidas de trabalho do horário que o funcionário deverá realizar, ou um intervalo de compensação ou mesmo de descanso para o funcionário.  
Lembre-se que para cada entrada deve existir uma saída correspondente.  
   
Além dos intervalos planejados nessa etapa é possível cadastrar os intervalos de tolerância para cada batida quando o tipo da jornada for de trabalho, as tolerâncias serão consideradas para cálculo de atrasos ou extras.  
É possível então definir que nos dez minutos após a primeira batida do horário de trabalho não serão calculados atrasos, ou mesmo nos dez minutos que antecedem a primeira batida do horário de trabalho não serão calculadas extras, permitindo também que seja cadastrada um número de horas para abater a tolerância.  
   
Daqui em diante cada passo irá respeitar o tipo de horário escolhido.  
   
Jornada Planejada para Horário Rígido  
Jornada Planejada para Horário Flexível  
Jornada Planejada para Horário Núcleo  
Jornada Planejada para Horário Semi-Flexível
