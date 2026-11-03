---
content_hash: ba4dd141f2f26565e316ea681232ac93be3449544912baff1991e057a8976529
fetched_at: '2026-06-29T00:10:03.715035+00:00'
page_id: '452719141'
product: rm
source: tdn-rm
title: Relatório de Justificativas de Exceções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719141
version: 1
---

**Relatório de Justificativas de Exceções**   
Para facilitar a utilização, o Relatório de justificativa de exceção passou a ser gerado pelo novo gerador de relatórios(Rm Reports).  
   
Utilize este relatório para justificar atrasos, faltas e extras no período informado.   
Poderá ser visualizado o totalizador das horas, o saldo do banco de horas e o percentual das extras. Para que o sistema considere o percentual das extras para geração das horas do saldo de banco de horas, o parâmetro "Considera percentual para exibir no saldo do banco de horas diário" deverá estar marcado.   
   
**Observação**  
No Parâmetro do novo gerador de relatórios (RM Reports) podemos informar o *Tempo mínimo justificativa* em minutos, onde só serão impressas as exceções que ultrapassarem o tempo mínimo determinado.   
**Exemplo**  
*Horário do funcionário*:  
08:00E 12:00S 14:00E 18:00S  
*Batidas do funcionário:*  
02/04/2001 - 08:00E 12:00S 14:00E 18:30S  
03/04/2001 - 08:00E 12:00S 14:00E 18:40S  
**Tempo mínimo = 00:30**  
O sistema irá imprimir apenas a exceção do dia 03/04/2001, pois no dia 02/04/2001 o funcionário fez apenas 00:30 minutos de extra não ultrapassando o tempo mínimo estipulado neste módulo de 00:30 minutos.  
**Observação**  
A utilização desse relatório dependerá de um modelo criado pela TOTVS, no qual ficará disponível no momento da instalação do aplicativo RM Chronus.
